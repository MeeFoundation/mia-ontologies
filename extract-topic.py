#!/usr/bin/env python3
"""
extract-topic.py — print one topic's fenced turtle block from a
cell-databook file that may contain several (one per embedded topic),
matched by its known `<!-- databook:graph: {topic_id}#graph -->` marker.

Why this exists: `databook extract` is a generic fenced-Turtle-block
extractor with no notion of "pick one topic out of several." That's fine
for Tier 1 validation, which wants every topic in a cell merged together
anyway — but Tier 2 validates one topic's data in isolation against a
per-template SHACL shape, and a cell with more than one embedded topic
(e.g. the Med. App. Info cell, which has three) would have its sibling
topics' triples wrongly pulled in by a whole-file `databook extract`.

Usage: python3 extract-topic.py <cell_file.databook.md> <topic-id-or-local-name>
Output: the matched topic's raw Turtle content on stdout.
"""
import sys

import yaml

from databook_topics import extract_topic_block, find_topic_entry, split_frontmatter


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: extract-topic.py <cell_file.databook.md> <topic-id-or-local-name>")
    path, topic_arg = sys.argv[1], sys.argv[2]
    text = open(path, encoding="utf-8").read()
    fm_text, _, body = split_frontmatter(text)
    fm = yaml.safe_load(fm_text)
    topics = (fm.get("mia") or {}).get("topics") or []
    match = find_topic_entry(topics, topic_arg)
    if not match:
        sys.exit(f"No mia.topics entry with id/local-name {topic_arg!r} in {path}")
    lines = extract_topic_block(body, f"{match['id']}#graph")
    if lines is None:
        sys.exit(f"No turtle block found for {match['id']!r} in {path}")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
