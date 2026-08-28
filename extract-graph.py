#!/usr/bin/env python3
"""
extract-graph.py — print one graph's fenced turtle block from a
cell-databook file that may contain several (one per embedded graph),
matched by its known `<!-- databook:graph: {graph_id}#graph -->` marker.

Why this exists: `databook extract` is a generic fenced-Turtle-block
extractor with no notion of "pick one graph out of several." That's fine
for Tier 1 validation, which wants every graph in a cell merged together
anyway — but Tier 2 validates one graph's data in isolation against a
per-template SHACL shape, and a cell with more than one embedded graph
(e.g. the Med. App. Info cell, which has three) would have its sibling
graphs' triples wrongly pulled in by a whole-file `databook extract`.

Usage: python3 extract-graph.py <cell_file.databook.md> <graph-id-or-local-name>
Output: the matched graph's raw Turtle content on stdout.
"""
import sys

import yaml

from databook_graphs import extract_graph_block, find_graph_entry, split_frontmatter


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: extract-graph.py <cell_file.databook.md> <graph-id-or-local-name>")
    path, graph_arg = sys.argv[1], sys.argv[2]
    text = open(path, encoding="utf-8").read()
    fm_text, _, body = split_frontmatter(text)
    fm = yaml.safe_load(fm_text)
    graphs = (fm.get("mia") or {}).get("graphs") or []
    match = find_graph_entry(graphs, graph_arg)
    if not match:
        sys.exit(f"No mia.graphs entry with id/local-name {graph_arg!r} in {path}")
    lines = extract_graph_block(body, f"{match['id']}#graph")
    if lines is None:
        sys.exit(f"No turtle block found for {match['id']!r} in {path}")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
