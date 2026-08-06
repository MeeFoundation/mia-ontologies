#!/usr/bin/env python3
"""
yaml-to-rdf.py  —  Synthesize cat:/cell:/topic: triples from the `mia.` YAML
frontmatter of category, cell, and topic DataBooks.

Why this exists: `databook extract` only pulls fenced Turtle blocks out of a
DataBook — but category-databook and cell-databook files carry all of their
content as `mia.` YAML frontmatter, with no Turtle block at all. Without this
script, cat:Node/cell:Cell individuals (and topic:SCTopicGraph's subject/
claimant) never appear in the graph SHACL validates, so category-shacl.ttl,
cell-shacl.ttl, and topic-shacl.ttl's :SCTopicGraphShape never fire against
real instance data. This script closes that gap by mapping each `mia.` field
to its corresponding ontology property, matching the mapping tables documented
in README.md's Category/Cell/Topic Ontology sections.

A topic DataBook's `mia.claimant`/`mia.subject` are typed on its plain `id`,
not `graph.named_graph` (id + "#graph") — matching topic.ttl's
topic:subject/topic:claimant doc comments, and the IRI cell:memberTopics/
cell:otherTopics actually reference in every cell DataBook's YAML.

Usage:   python3 yaml-to-rdf.py [repo-root] > yaml-data.ttl
Output:  Turtle triples on stdout — merge with `riot` alongside data extracted
         via `databook extract` (see README.md's Validation section).

Requires: pip install pyyaml
"""

import os, re, sys, yaml, glob

CAT = "http://mee.foundation/ontologies/category#"
CELL = "http://mee.foundation/ontologies/cell#"
TOPIC = "http://mee.foundation/ontologies/topic#"
PSHAPES = "http://mee.foundation/ontologies/persona/shapes#"
XSD = "http://www.w3.org/2001/XMLSchema#"
MIA_NS = "http://www.example.org/mia#"

PREFIXES = {
    "cat": CAT,
    "cell": CELL,
    "topic": TOPIC,
    "pshapes": PSHAPES,
}


def resolve(val):
    """Resolve a YAML-string value (curie or bare local name) to a full IRI."""
    if val.startswith("http://") or val.startswith("https://"):
        return val
    if val.startswith(":"):
        return MIA_NS + val[1:]
    if ":" in val:
        prefix, local = val.split(":", 1)
        if prefix in PREFIXES:
            return PREFIXES[prefix] + local
    return MIA_NS + val


def esc(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


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


def emit_lit(triples, subj, prop, value, datatype=None):
    if datatype:
        triples.append(f'<{subj}> <{prop}> "{esc(value)}"^^<{datatype}> .')
    else:
        triples.append(f'<{subj}> <{prop}> "{esc(value)}" .')


def process_category_databook(fm, triples):
    subj = fm["id"]
    mia = fm.get("mia", {}) or {}

    emit_type(triples, subj, CAT + "Node")
    if mia.get("category"):
        emit_type(triples, subj, CAT + "CategoryDefined")
    else:
        emit_type(triples, subj, CAT + "UserDefined")

    if mia.get("catType"):
        emit_lit(triples, subj, CAT + "catType", mia["catType"])

    for cell_iri in as_list(mia.get("cell")):
        emit_obj(triples, subj, CAT + "cell", resolve(cell_iri))

    if mia.get("category"):
        emit_obj(triples, subj, CAT + "category", resolve(mia["category"]))

    for child_iri in as_list(mia.get("child")):
        emit_obj(triples, subj, CAT + "child", resolve(child_iri))

    if mia.get("label"):
        emit_lit(triples, subj, CAT + "label", mia["label"])


def process_cell_databook(fm, triples):
    subj = fm["id"]
    mia = fm.get("mia", {}) or {}

    emit_type(triples, subj, CELL + "Cell")

    member_count = mia.get("memberCount")
    if member_count:
        # Only an actually-instantiated cell (real content, cell:memberCount
        # set) is typed cell:ACell — a pure tree-position placeholder with
        # nothing filed under it yet stays a bare cell:Cell (cell.ttl 3.10.0),
        # and is therefore exempt from cell-shacl.ttl's :ACellShape and the
        # per-member-count shapes, including their required
        # cell:subject/cell:memberTopics.
        emit_type(triples, subj, CELL + "ACell")
        member_iri = resolve(member_count)
        emit_type(triples, subj, member_iri)
        emit_obj(triples, subj, CELL + "memberCount", member_iri)

    if mia.get("creator"):
        emit_obj(triples, subj, CELL + "creator", resolve(mia["creator"]))

    if mia.get("folder"):
        emit_lit(triples, subj, CELL + "folder", mia["folder"], XSD + "anyURI")

    for topic_iri in as_list(mia.get("memberTopics")):
        emit_obj(triples, subj, CELL + "memberTopics", resolve(topic_iri))

    for topic_iri in as_list(mia.get("otherTopics")):
        emit_obj(triples, subj, CELL + "otherTopics", resolve(topic_iri))

    for subject_iri in as_list(mia.get("subject")):
        emit_obj(triples, subj, CELL + "subject", resolve(subject_iri))

    if mia.get("shape"):
        emit_obj(triples, subj, CELL + "shape", resolve(mia["shape"]))


def process_topic_databook(fm, triples):
    mia = fm.get("mia", {}) or {}
    claimant = mia.get("claimant")
    subject = mia.get("subject")
    if not (claimant and subject):
        return  # no subject/claimant — not an SCTopicGraph, skip
    subj = fm["id"]
    emit_type(triples, subj, TOPIC + "SCTopicGraph")
    emit_obj(triples, subj, TOPIC + "claimant", resolve(claimant))
    emit_obj(triples, subj, TOPIC + "subject", resolve(subject))


def main(root):
    triples = []

    for path in sorted(glob.glob(os.path.join(root, "example", "Cells", "**", "*.databook.md"), recursive=True)):
        if "under-development" in path.split(os.sep):
            continue
        fm = frontmatter(path)
        if not fm:
            continue
        t = fm.get("type")
        if t == "category-databook":
            process_category_databook(fm, triples)
        elif t == "cell-databook":
            process_cell_databook(fm, triples)

    for path in sorted(glob.glob(os.path.join(root, "example", "topics", "*.databook.md"))):
        if "under-development" in path.split(os.sep):
            continue
        fm = frontmatter(path)
        if not fm:
            continue
        if fm.get("type") == "topic-databook":
            process_topic_databook(fm, triples)

    print("\n".join(triples))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
