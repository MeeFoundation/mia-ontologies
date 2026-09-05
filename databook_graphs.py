#!/usr/bin/env python3
"""
databook_graphs.py — shared helpers for locating a single embedded graph's
content inside a (possibly multi-graph) cell-databook file, used by both
draw.py and extract-graph.py.

Since graph-databooks were merged into their owning cell-databooks, a cell
file's body may contain several ```turtle fences — one per embedded graph
(see the `mia.graphs` list in that cell's frontmatter). Each fence still
carries its own `<!-- databook:graph: {graph_id}#graph -->` marker, computed
from the graph's own `id` per the unchanged `{id}#graph` named-graph
convention (CLAUDE.md's "DataBook IRI convention") — so isolating one
graph's fence only requires knowing that graph's `id`, no new marker scheme.

Also carries `resolve()`/`as_list()` — shared by `yaml-to-rdf.py` and
`validate-tier2.py`, both of which need to turn a `mia.*` YAML value (a
CURIE, a bare `:X` local name, or a bare `graph-<NN>` local name) into the
same full IRI.
"""
import re

FRONTMATTER_RE = re.compile(r"^(---\n)(.*?\n)(---\n?)(.*)$", re.DOTALL)

MIA_NS = "http://www.example.org/mia#"
GRAPHS_BASE = "http://www.example.org/mia/graphs/"

PREFIXES = {
    "cat": "http://mee.foundation/ontologies/category#",
    "cell": "http://mee.foundation/ontologies/cell#",
    "persona": "http://mee.foundation/ontologies/persona#",
    "pets": "http://mee.foundation/ontologies/pets#",
    "vehicles": "http://mee.foundation/ontologies/vehicles#",
}

GRAPH_LOCAL_RE = re.compile(r"^graph-\d+$")


def resolve(val):
    """Resolve a YAML-string value (curie, bare graph local name, or bare
    MIA local name) to a full IRI.

    mia.member/topic entries are written as bare graph
    id local names (e.g. "graph-22") rather than the full
    http://www.example.org/mia/graphs/... IRI — the base is constant across
    every graph id in the dataset (mia.graphs[].id and the #graph names still
    spell it out in full, since those double as the graph's actual named-graph
    identity), so repeating it on every member/topic list entry is
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


def as_list(v):
    if v is None:
        return []
    return v if isinstance(v, list) else [v]


def split_frontmatter(text):
    """Return (fm_text, closing_dashes_incl_trailing_newline, body)."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        raise ValueError("no frontmatter found")
    return m.group(2), m.group(3), m.group(4)


def extract_graph_block(body_text, target_graph):
    """Return the turtle lines (databook: comment lines stripped) for the
    single ```turtle fence in body_text whose <!-- databook:graph: X -->
    marker equals target_graph, or None if no fence matches. A merged
    cell-databook body may contain multiple ```turtle fences, one per
    embedded graph."""
    in_fence = False
    current_graph = None
    current_lines = []
    for line in body_text.split("\n"):
        s = line.strip()
        if s == "```turtle":
            in_fence, current_graph, current_lines = True, None, []
            continue
        if in_fence and s == "```":
            in_fence = False
            if current_graph == target_graph:
                return current_lines
            continue
        if in_fence:
            m = re.match(r"<!--\s*databook:graph:\s*(\S+)\s*-->", s)
            if m:
                current_graph = m.group(1)
                continue
            if s.startswith("<!-- databook:"):
                continue
            current_lines.append(line)
    return None


def find_graph_entry(graphs, graph_arg):
    """Match graph_arg against a mia.graphs list's id or id-local-name."""
    for g in graphs or []:
        if not isinstance(g, dict):
            continue
        gid = g.get("id", "")
        if gid == graph_arg or gid.rsplit("/", 1)[-1] == graph_arg:
            return g
    return None
