#!/usr/bin/env python3
"""
yaml-to-rdf.py  —  Synthesize cell: triples from the `mia.` YAML
frontmatter of cell-databooks.

Why this exists: `databook extract` only pulls fenced Turtle blocks out of a
DataBook — but cell-databook files carry most of their content as `mia.`
YAML frontmatter, not Turtle. Without this script, cell:Cell individuals
(and cell:SCGraph's subject/claimant) never appear in the graph SHACL
validates, so cell-shacl.ttl's :SCGraphShape never fires against real
instance data. This script closes that gap by mapping each `mia.` field to
its corresponding ontology property, matching the mapping tables
documented in README.md's Cell Ontology section.

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
that id + "#graph" — matching cell.ttl's cell:subject/cell:claimant doc
comments, and the IRI cell:member/cell:topic actually reference.

Usage:   python3 yaml-to-rdf.py [repo-root] > yaml-data.ttl
Output:  Turtle triples on stdout — merge with `riot` alongside data extracted
         via `databook extract` (see EXAMPLE.md's Validation section).

Requires: pip install pyyaml
"""

import os, re, sys, yaml, glob

from databook_graphs import resolve, as_list

CELL = "http://mee.foundation/ontologies/cell#"


def frontmatter(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    return yaml.safe_load(m.group(1)) if m else None


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
    # nothing substantive to say still carries a minimal stub cell:member
    # entry rather than omitting member content. Member count itself is
    # never stored — it's simply the number of distinct subjects among
    # mia.member/mia.topic, derivable by counting whenever needed.
    emit_type(triples, subj, CELL + "MemberCell")

    if mia.get("creator"):
        emit_obj(triples, subj, CELL + "creator", resolve(mia["creator"]))

    # cell:owner — one or more p:Person/o:Organization IRIs, resolved the
    # same way as cell:creator (never a bare graph-local-name).
    for owner_iri in as_list(mia.get("owner")):
        emit_obj(triples, subj, CELL + "owner", resolve(owner_iri))

    for graph_iri in as_list(mia.get("member")):
        emit_obj(triples, subj, CELL + "member", resolve(graph_iri))

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
    """Emit cell:SCGraph/claimant/subject/template for one mia.graphs[]
    entry — replaces the old process_topic_databook, which read the same
    fields from a separate graph-databook file's own frontmatter."""
    claimant = graph.get("claimant")
    subject = graph.get("subject")
    if not (claimant and subject):
        return  # no subject/claimant — not an SCGraph, skip
    subj = graph["id"]
    emit_type(triples, subj, CELL + "SCGraph")
    emit_obj(triples, subj, CELL + "claimant", resolve(claimant))
    emit_obj(triples, subj, CELL + "subject", resolve(subject))

    # cell:template — domain cell:Graph, 0..N, present only on graphs that
    # contain instance(s) of a persona:PersonaTemplate subclass (cell.ttl's
    # graph.png diagram). A graph may hold more than one template's worth of
    # content at once (e.g. a single graph combining ServiceAccount, DebitCard,
    # and CheckingAccount instances), so this accepts either a bare string or
    # a YAML list.
    for template in as_list(graph.get("template")):
        emit_obj(triples, subj, CELL + "template", resolve(template))


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
