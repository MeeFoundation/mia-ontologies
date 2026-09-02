#!/usr/bin/env python3
"""
yaml-to-rdf.py  —  Synthesize cell:/g: triples from the `mia.` YAML
frontmatter of cell-databooks.

Why this exists: `databook extract` only pulls fenced Turtle blocks out of a
DataBook — but cell-databook files carry most of their content as `mia.`
YAML frontmatter, not Turtle. Without this script, cell:Cell individuals
(and g:SCGraph's subject/claimant) never appear in the graph SHACL
validates, so cell-shacl.ttl and graph-shacl.ttl's :SCGraphShape never
fire against real instance data. This script closes that gap by mapping
each `mia.` field to its corresponding ontology property, matching the
mapping tables documented in README.md's Cell/Graph Ontology sections.

There is no category-side synthesis here at all — category.ttl 1.31.0
deleted cat:Folder and its subclasses cat:CategoryDefined/cat:UserDefined
outright, along with cat:child/cat:cell/cat:category/cat:catType/cat:label.
A folder's tree position is now purely a filesystem fact (which cell-databook
file physically lives in it), with no RDF individual representing the folder
at all. The only remaining RDF-level record of a cell's classification is
cell:category (cell.ttl 3.20.0), read directly from the explicit `mia.category`
YAML field below — never derived from filename-parsing.

Since graph-databooks were merged into their owning cell-databooks (each
graph's Turtle content and Overview now live in that cell file's body; its
`claimant`/`subject`/etc. now live in a `mia.graphs` list on that same cell's
frontmatter — see CLAUDE.md's "Graph ID Naming Convention" section), there is
no separate `example/graphs/*.databook.md` glob any more: `process_cell_databook`
below also iterates `mia.graphs` and emits the same three triples per entry
that a standalone graph-databook file's frontmatter used to supply.

A graph's `claimant`/`subject` are typed on its plain `mia.graphs[].id`, not
that id + "#graph" — matching graph.ttl's g:subject/g:claimant doc
comments, and the IRI cell:members/cell:topic actually reference.

Usage:   python3 yaml-to-rdf.py [repo-root] > yaml-data.ttl
Output:  Turtle triples on stdout — merge with `riot` alongside data extracted
         via `databook extract` (see EXAMPLE.md's Validation section).

Requires: pip install pyyaml
"""

import os, re, sys, yaml, glob

CELL = "http://mee.foundation/ontologies/cell#"
GRAPH = "http://mee.foundation/ontologies/graph#"
PSHAPES = "http://mee.foundation/ontologies/persona/shapes#"
MIA_NS = "http://www.example.org/mia#"
GRAPHS_BASE = "http://www.example.org/mia/graphs/"

PREFIXES = {
    "cat": "http://mee.foundation/ontologies/category#",
    "cell": CELL,
    "g": GRAPH,
    "pshapes": PSHAPES,
}


GRAPH_LOCAL_RE = re.compile(r"^graph-\d+$")


def resolve(val):
    """Resolve a YAML-string value (curie, bare graph local name, or bare
    MIA local name) to a full IRI.

    mia.members/topic entries are written as bare graph
    id local names (e.g. "graph-22") rather than the full
    http://www.example.org/mia/graphs/... IRI — the base is constant across
    every graph id in the dataset (mia.graphs[].id and the #graph names still
    spell it out in full, since those double as the graph's actual named-graph
    identity), so repeating it on every members/topic list entry is
    pure baggage. A graph id local name always matches "graph-<NN>", which no
    other resolve()-able value (":Self", "cat:Affiliations", ...) ever does,
    so that's what distinguishes the two bare forms below.
    """
    if val.startswith("http://") or val.startswith("https://"):
        return val
    if val.startswith(":"):
        return MIA_NS + val[1:]
    if GRAPH_LOCAL_RE.match(val):
        return GRAPHS_BASE + val
    if ":" in val:
        prefix, local = val.split(":", 1)
        if prefix in PREFIXES:
            return PREFIXES[prefix] + local
    return MIA_NS + val


def frontmatter(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    return yaml.safe_load(m.group(1)) if m else None


def as_list(v):
    if v is None:
        return []
    return v if isinstance(v, list) else [v]


def emit_type(triples, subj, type_iri):
    triples.append(f"<{subj}> a <{type_iri}> .")


def emit_obj(triples, subj, prop, obj_iri):
    triples.append(f"<{subj}> <{prop}> <{obj_iri}> .")


def process_cell_databook(fm, triples):
    subj = fm["id"]
    mia = fm.get("mia", {}) or {}

    emit_type(triples, subj, CELL + "Cell")

    if mia.get("category"):
        # cell:category — domain cell:Cell, so asserted on every cell
        # regardless of facet (cell.ttl 3.45.0, renamed from cell:origin).
        emit_obj(triples, subj, CELL + "category", resolve(mia["category"]))

    # Every real cell-databook is always also typed cell:MemberCell — no bare
    # tree-position-only cell with no member content; a category node with
    # nothing substantive to say still carries a minimal stub cell:members
    # entry rather than omitting member content. Member count itself is
    # never stored — it's simply the number of distinct subjects among
    # mia.members/mia.topic, derivable by counting whenever needed.
    emit_type(triples, subj, CELL + "MemberCell")

    if mia.get("creator"):
        emit_obj(triples, subj, CELL + "creator", resolve(mia["creator"]))

    for graph_iri in as_list(mia.get("members")):
        emit_obj(triples, subj, CELL + "members", resolve(graph_iri))

    topic = as_list(mia.get("topic"))
    if topic:
        # cell:TopicCell — the subclass of cell:MemberCell for a cell
        # that actually carries a cell:topic value (cell.ttl 3.37.0). See
        # CLAUDE.md's TopicCell integrity check.
        emit_type(triples, subj, CELL + "TopicCell")
    for graph_iri in topic:
        emit_obj(triples, subj, CELL + "topic", resolve(graph_iri))

    # No cell:subject synthesis: who/what a cell is about is derivable
    # directly from members/topic (cell.ttl's cell:topic comment) rather
    # than an independently-asserted fact, so it is never stored as its
    # own triple.

    # No cell:shape synthesis either (cell.ttl 3.45.0 removed the
    # property): a cell:MemberCell's validation shape is derivable from
    # its own cell:category value via a reverse lookup on cell-templates.ttl
    # rather than stored per-instance.

    for graph in as_list(mia.get("graphs")):
        process_embedded_graph(graph, triples)


def process_embedded_graph(graph, triples):
    """Emit g:SCGraph/claimant/subject for one mia.graphs[] entry —
    replaces the old process_topic_databook, which read the same three
    fields from a separate graph-databook file's own frontmatter."""
    claimant = graph.get("claimant")
    subject = graph.get("subject")
    if not (claimant and subject):
        return  # no subject/claimant — not an SCGraph, skip
    subj = graph["id"]
    emit_type(triples, subj, GRAPH + "SCGraph")
    emit_obj(triples, subj, GRAPH + "claimant", resolve(claimant))
    emit_obj(triples, subj, GRAPH + "subject", resolve(subject))


def main(root):
    triples = []

    for path in sorted(
        glob.glob(os.path.join(root, "example", "Cells", "**", "*.databook.md"), recursive=True)
    ):
        if "under-development" in path.split(os.sep):
            continue
        fm = frontmatter(path)
        if not fm or fm.get("type") != "cell-databook":
            continue
        process_cell_databook(fm, triples)

    print("\n".join(triples))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
