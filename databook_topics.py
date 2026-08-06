#!/usr/bin/env python3
"""
databook_topics.py — shared helpers for locating a single embedded topic's
content inside a (possibly multi-topic) cell-databook file, used by both
draw.py and extract-topic.py.

Since topic-databooks were merged into their owning cell-databooks, a cell
file's body may contain several ```turtle fences — one per embedded topic
(see the `mia.topics` list in that cell's frontmatter). Each fence still
carries its own `<!-- databook:graph: {topic_id}#graph -->` marker, computed
from the topic's own `id` per the unchanged `{id}#graph` named-graph
convention (CLAUDE.md's "DataBook IRI convention") — so isolating one
topic's fence only requires knowing that topic's `id`, no new marker scheme.
"""
import re

FRONTMATTER_RE = re.compile(r"^(---\n)(.*?\n)(---\n?)(.*)$", re.DOTALL)


def split_frontmatter(text):
    """Return (fm_text, closing_dashes_incl_trailing_newline, body)."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        raise ValueError("no frontmatter found")
    return m.group(2), m.group(3), m.group(4)


def extract_topic_block(body_text, target_graph):
    """Return the turtle lines (databook: comment lines stripped) for the
    single ```turtle fence in body_text whose <!-- databook:graph: X -->
    marker equals target_graph, or None if no fence matches. A merged
    cell-databook body may contain multiple ```turtle fences, one per
    embedded topic."""
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


def find_topic_entry(topics, topic_arg):
    """Match topic_arg against a mia.topics list's id or id-local-name."""
    for t in topics or []:
        if not isinstance(t, dict):
            continue
        tid = t.get("id", "")
        if tid == topic_arg or tid.rsplit("/", 1)[-1] == topic_arg:
            return t
    return None
