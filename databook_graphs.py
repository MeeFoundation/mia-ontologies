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
"""
import re

FRONTMATTER_RE = re.compile(r"^(---\n)(.*?\n)(---\n?)(.*)$", re.DOTALL)


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
