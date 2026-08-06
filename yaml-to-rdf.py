#!/usr/bin/env python3
"""
yaml-to-rdf.py  —  Synthesize cat:/cell:/topic: triples from the `mia.` YAML
frontmatter of cell and topic DataBooks, plus the filesystem structure of a
user's own instance tree.

Why this exists: `databook extract` only pulls fenced Turtle blocks out of a
DataBook — but cell-databook files carry most of their content as `mia.`
YAML frontmatter, not Turtle. Without this script, cell:Cell individuals
(and topic:SCTopicGraph's subject/claimant) never appear in the graph SHACL
validates, so cell-shacl.ttl and topic-shacl.ttl's :SCTopicGraphShape never
fire against real instance data. This script closes that gap by mapping
each `mia.` field to its corresponding ontology property, matching the
mapping tables documented in README.md's Cell/Topic Ontology sections.

There is no separate category-databook DataBook type any more (category.ttl
1.30.0 / cell.ttl 3.19.0): a folder's sole DataBook is its co-located
cell-databook, which doubles as both real/placeholder content holder and
the folder's tree-node marker. cat:Folder individuals and their
catType/category/child/cell values are therefore synthesized entirely from
the filesystem, not read from any YAML field:
  - a folder's synthesized cat:Folder IRI is derived from its (primary)
    cell-databook's own id, stripping a trailing -N (a 2nd+ cell sharing
    the folder), if present, and appending -cat;
  - catType/category come from reverse-matching that cell-databook's own
    filename (its parenthetical segment, or its whole bare local name when
    the filename convention's compression rule applies) against the class
    names actually declared in category.ttl;
  - child comes from which direct subfolders themselves directly contain a
    cell-databook file;
  - cell is simply every cell-databook file co-located in that same folder.
cat:label is never synthesized — a category's display name is now just its
own OS folder name, used verbatim, with no override represented anywhere.

Since topic-databooks were merged into their owning cell-databooks (each
topic's Turtle content and Overview now live in that cell file's body; its
`claimant`/`subject`/etc. now live in a `mia.topics` list on that same cell's
frontmatter — see CLAUDE.md's "Topic ID Naming Convention" section), there is
no separate `example/topics/*.databook.md` glob any more: `process_cell_databook`
below also iterates `mia.topics` and emits the same three triples per entry
that a standalone topic-databook file's frontmatter used to supply.

A topic's `claimant`/`subject` are typed on its plain `mia.topics[].id`, not
that id + "#graph" — matching topic.ttl's topic:subject/topic:claimant doc
comments, and the IRI cell:memberTopics/cell:otherTopics actually reference.

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


def kebab_case(name):
    """Acronym-aware kebab-casing per CLAUDE.md's Category/Cell DataBook
    Filename Convention: a hyphen is inserted only at a lowercase->uppercase
    boundary, or an uppercase-run->lowercase boundary (i.e. before the
    uppercase letter that hands an acronym run off to a new capitalized
    word). Non-letter characters (e.g. the literal parens in an org-variant
    class's local name, "BankingPayments(org)") are passed through unchanged
    and never trigger a boundary, so an org-variant class's kebab form never
    collides with its plain counterpart's ("banking-payments(org)" vs.
    "banking-payments")."""
    out = []
    n = len(name)
    for i, ch in enumerate(name):
        if i > 0 and ch.isalpha() and ch.isupper():
            prev = name[i - 1]
            nxt = name[i + 1] if i + 1 < n else ""
            lower_to_upper = prev.isalpha() and prev.islower()
            upper_run_to_lower = prev.isalpha() and prev.isupper() and nxt.isalpha() and nxt.islower()
            if lower_to_upper or upper_run_to_lower:
                out.append("-")
        out.append(ch.lower())
    return "".join(out)


def build_category_class_table(category_ttl_path):
    """Parse category.ttl's actual `cat:X rdf:type owl:Class` declarations
    (not hardcoded) into a {kebab_local_name: raw_local_name} lookup table,
    e.g. {'immediate-family': 'ImmediateFamily', 'ssa': 'SSA', 'category':
    'Category', ...}, so it stays correct as category.ttl evolves. Warns to
    stderr (does not raise) on a kebab collision between two distinct class
    names and keeps the first-declared one — not expected today given
    kebab_case's parens-preserving handling of org-variant names."""
    text = open(category_ttl_path, encoding="utf-8").read()
    raws = re.findall(r"^cat:(\S+)\s+rdf:type\s+owl:Class", text, re.MULTILINE)
    table = {}
    for raw in raws:
        local = raw.replace("\\(", "(").replace("\\)", ")")
        key = kebab_case(local)
        if key in table and table[key] != local:
            print(
                f"WARNING: kebab collision {key!r}: {table[key]!r} vs {local!r} "
                f"(keeping {table[key]!r})",
                file=sys.stderr,
            )
            continue
        table[key] = local
    return table


def normalize_for_compression(s):
    """Case/format-insensitive normalization used only to decide whether a
    folder's own verbatim name compression-matches its catType: apply the
    acronym-aware kebab_case (handles PascalCase run boundaries), then
    collapse any run of non-alphanumeric characters (spaces, '&', '.', etc.
    — whatever punctuation a verbatim folder name may contain) into a
    single hyphen, then strip leading/trailing hyphens. E.g. "Health &
    Wellness" and "HealthWellness" both normalize to "health-wellness"."""
    s1 = kebab_case(s)
    s2 = re.sub(r"[^a-z0-9]+", "-", s1)
    return s2.strip("-")


def cell_filename_root(path):
    """<VerbatimFolderName>(<catType-kebab>) or bare <VerbatimFolderName>,
    with an optional trailing -N (a 2nd+ cell sharing the folder) and the
    .databook.md extension stripped, from a cell-databook's own filename.
    No -cell token any more — cell-databook is the sole DataBook type in a
    user's instance tree, so nothing needs to be disambiguated by it."""
    base = os.path.basename(path)[: -len(".databook.md")]
    return re.sub(r"-\d+$", "", base)


def resolve_cat_type(filename_root, class_table):
    """Return the class-table's raw local name matched against the
    filename's parenthetical catType segment (already kebab-cased, so
    looked up directly), or — when the compression rule collapsed it to a
    bare verbatim folder name — that name run through
    normalize_for_compression first. Returns None if unmatched."""
    m = re.match(r"^(?P<local>.+)\((?P<catseg>[^()]+)\)$", filename_root)
    catseg = m.group("catseg") if m else normalize_for_compression(filename_root)
    return class_table.get(catseg)


def derive_cat_iri(cell_iri):
    """A folder's synthesized cat:Folder IRI: its (primary) cell's own IRI
    with an optional trailing -N (a 2nd+ cell sharing the folder) stripped,
    then -cat appended."""
    return re.sub(r"-\d+$", "", cell_iri) + "-cat"


def primary_cell_fm(fms_in_dir):
    """Prefer the DataBook whose id has no trailing -N as the folder's
    'primary' cell, for deriving the folder's own -cat IRI and catType
    segment; falls back to the lexicographically-first -N id if every id in
    this directory has one (not exercised by any current example folder,
    but kept for forward-compatibility with the ontology's
    already-documented multi-cell-per-folder case). Note: a folder whose
    own verbatim name legitimately ends in a bare digit would be
    misdetected as an -N variant here — not a concern for any current
    example folder, but a known sharp edge of dropping the old -cell
    token's unambiguous anchor for this suffix."""
    for fm in fms_in_dir:
        if not re.search(r"-\d+$", fm["id"]):
            return fm
    return sorted(fms_in_dir, key=lambda fm: fm["id"])[0]


def process_category_folder(dirpath, fms_in_dir, cell_dirs, class_table, triples):
    """Emit the folder's synthesized cat:Folder individual. cell_dirs is the
    full {dirpath: [frontmatter, ...]} map, used to test which direct
    subfolders are themselves category-tree nodes (i.e. directly contain
    their own cell-databook file — cell.ttl's folder ownership boundary
    rule)."""
    p_fm = primary_cell_fm(fms_in_dir)
    cat_iri = derive_cat_iri(p_fm["id"])
    emit_type(triples, cat_iri, CAT + "Folder")

    matched = resolve_cat_type(cell_filename_root(p_fm["_path"]), class_table)
    if matched and matched != "Category":
        emit_type(triples, cat_iri, CAT + "CategoryDefined")
        emit_obj(triples, cat_iri, CAT + "category", CAT + matched)
        emit_lit(triples, cat_iri, CAT + "catType", matched)
    else:
        emit_type(triples, cat_iri, CAT + "UserDefined")
        emit_lit(triples, cat_iri, CAT + "catType", matched or "Category")

    for fm in fms_in_dir:  # cat:cell — every cell-databook co-located here
        emit_obj(triples, cat_iri, CAT + "cell", fm["id"])

    for entry in sorted(os.listdir(dirpath)):  # cat:child — direct marker subfolders
        sub = os.path.join(dirpath, entry)
        if os.path.isdir(sub) and sub in cell_dirs:
            child_p_fm = primary_cell_fm(cell_dirs[sub])
            emit_obj(triples, cat_iri, CAT + "child", derive_cat_iri(child_p_fm["id"]))
    # No cat:label triple is ever emitted — a category's display name is now
    # simply its own OS folder name, used verbatim.


def process_cell_databook(fm, triples):
    subj = fm["id"]
    mia = fm.get("mia", {}) or {}

    emit_type(triples, subj, CELL + "Cell")

    if mia.get("origin"):
        # cell:origin — domain cell:Cell, so asserted on every cell
        # regardless of facet, including a bare placeholder with no real
        # content yet (cell.ttl 3.20.0).
        emit_obj(triples, subj, CELL + "origin", resolve(mia["origin"]))

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

    for topic in as_list(mia.get("topics")):
        process_embedded_topic(topic, triples)


def process_embedded_topic(topic, triples):
    """Emit topic:SCTopicGraph/claimant/subject for one mia.topics[] entry —
    replaces the old process_topic_databook, which read the same three
    fields from a separate topic-databook file's own frontmatter."""
    claimant = topic.get("claimant")
    subject = topic.get("subject")
    if not (claimant and subject):
        return  # no subject/claimant — not an SCTopicGraph, skip
    subj = topic["id"]
    emit_type(triples, subj, TOPIC + "SCTopicGraph")
    emit_obj(triples, subj, TOPIC + "claimant", resolve(claimant))
    emit_obj(triples, subj, TOPIC + "subject", resolve(subject))


def main(root):
    class_table = build_category_class_table(os.path.join(root, "category.ttl"))
    triples = []

    cell_dirs = {}
    for path in sorted(
        # No -cell token in filenames any more — every *.databook.md under
        # example/Cells/ is a cell-databook (category-databook was retired
        # in category.ttl 1.30.0).
        glob.glob(os.path.join(root, "example", "Cells", "**", "*.databook.md"), recursive=True)
    ):
        if "under-development" in path.split(os.sep):
            continue
        fm = frontmatter(path)
        if not fm or fm.get("type") != "cell-databook":
            continue
        fm["_path"] = path
        cell_dirs.setdefault(os.path.dirname(path), []).append(fm)

    for dirpath in sorted(cell_dirs):
        process_category_folder(dirpath, cell_dirs[dirpath], cell_dirs, class_table, triples)
        for fm in sorted(cell_dirs[dirpath], key=lambda fm: fm["id"]):
            process_cell_databook(fm, triples)

    print("\n".join(triples))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
