#!/usr/bin/env python3
"""
databook_graphs.py — shared helpers for reading cell-databook files: locating
one embedded graph's content inside a (possibly multi-graph) file, and turning
a cell's own frontmatter into `cell:` triples. Used by draw.py,
extract-graph.py, extract-all.py, yaml-to-rdf.py and validate.py.

Since graph-databooks were merged into their owning cell-databooks, a cell
file's body may contain several ```turtle fences — one per embedded graph
(each `mia.member`/`mia.topic` entry in that cell's frontmatter is one such
graph's own metadata dict). Each fence still carries its own
`<!-- databook:graph: {graph_id}#graph -->` marker, computed from the
graph's own `id` per the unchanged `{id}#graph` named-graph convention
(CLAUDE.md's "DataBook IRI convention") — so isolating one graph's fence
only requires knowing that graph's `id`, no new marker scheme.

Also carries `resolve()`/`as_list()` — needed wherever a `mia.*` YAML value
(a CURIE or a bare `:X` local name) must become the same full IRI — and the
`cell:` triple synthesis (`process_cell_databook()`/`process_embedded_graph()`)
that turns one cell-databook's frontmatter into Turtle. Both `yaml-to-rdf.py`
(whole-tree dump) and `validate.py` (one cell at a time) call that synthesis,
so it lives here rather than in either script; `yaml-to-rdf.py`'s hyphenated
filename is not an importable module name in any case.
"""
import re

FRONTMATTER_RE = re.compile(r"^(---\n)(.*?\n)(---\n?)(.*)$", re.DOTALL)

MIA_NS = "http://www.example.org/mia#"
CELL = "http://mee.foundation/ontologies/cell#"

PREFIXES = {
    "cat": "http://mee.foundation/ontologies/category#",
    "cell": "http://mee.foundation/ontologies/cell#",
    "persona": "http://mee.foundation/ontologies/persona#",
    "pets": "http://mee.foundation/ontologies/pets#",
    "vehicles": "http://mee.foundation/ontologies/vehicles#",
    # Shape namespaces — a mia.member[]/mia.topic[].template value is now a
    # sh:NodeShape CURIE (cell:template's range, cell.ttl), not a template
    # type label class name, so these three must resolve too. Same base URIs
    # cat-templates.ttl's own @prefix block declares.
    "pshapes": "http://mee.foundation/ontologies/persona/shapes#",
    "petshapes": "http://mee.foundation/ontologies/pets/shapes#",
    "vehicleshapes": "http://mee.foundation/ontologies/vehicles/shapes#",
}


def resolve(val):
    """Resolve a YAML-string value (curie or bare MIA local name) to a full
    IRI. A `mia.member`/`mia.topic` entry's own `id` is already a full IRI
    (it doubles as the graph's actual named-graph identity), so it's used
    directly rather than passed through here."""
    if val.startswith("http://") or val.startswith("https://"):
        return val
    if val.startswith(":"):
        return MIA_NS + val[1:]
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


def iter_graph_blocks(body_text):
    """Yield (graph_marker, turtle_lines) for every ```turtle fence in
    body_text, in document order, with the fence's own `<!-- databook: -->`
    comment lines stripped (they are markers, not Turtle — riot rejects
    them). graph_marker is the fence's `<!-- databook:graph: X -->` value,
    or None if it carries no such marker. A merged cell-databook body may
    contain several fences, one per embedded graph."""
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
            yield current_graph, current_lines
            continue
        if in_fence:
            m = re.match(r"<!--\s*databook:graph:\s*(\S+)\s*-->", s)
            if m:
                current_graph = m.group(1)
                continue
            if s.startswith("<!-- databook:"):
                continue
            current_lines.append(line)


def extract_graph_block(body_text, target_graph):
    """Return the turtle lines (databook: comment lines stripped) for the
    single ```turtle fence in body_text whose <!-- databook:graph: X -->
    marker equals target_graph, or None if no fence matches."""
    for graph, lines in iter_graph_blocks(body_text):
        if graph == target_graph:
            return lines
    return None


def find_graph_entry(entries, graph_arg):
    """Match graph_arg (an id or id-local-name) against an iterable of
    mia.member/mia.topic entry dicts — callers pass in the concatenation of
    both fields, since either can hold the graph being looked for."""
    for g in entries or []:
        if not isinstance(g, dict):
            continue
        gid = g.get("id", "")
        if gid == graph_arg or gid.rsplit("/", 1)[-1] == graph_arg:
            return g
    return None


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

    for entry in as_list(mia.get("member")):
        emit_obj(triples, subj, CELL + "member", entry["id"])
        process_embedded_graph(entry, triples)

    topic = as_list(mia.get("topic"))
    if topic:
        # cell:TopicCell — the subclass of cell:MemberCell for a cell
        # that actually carries a cell:topic value (cell.ttl 3.37.0). See
        # CLAUDE.md's TopicCell integrity check.
        emit_type(triples, subj, CELL + "TopicCell")
    for entry in topic:
        emit_obj(triples, subj, CELL + "topic", entry["id"])
        process_embedded_graph(entry, triples)

    # No cell:subject synthesis: who/what a cell is about is derivable
    # directly from members/topic (cell.ttl's cell:topic comment) rather
    # than an independently-asserted fact, so it is never stored as its
    # own triple.

    # No cell:shape synthesis either (cell.ttl 3.45.0 removed the
    # property): a cell:MemberCell's validation shape is derivable from
    # its own cell:category value via a reverse lookup on cat-templates.ttl
    # rather than stored per-instance.


def process_embedded_graph(graph, triples):
    """Emit cell:SCGraph/claimant/subject/template for one mia.member[]/
    mia.topic[] entry — replaces the old process_topic_databook, which read
    the same fields from a separate graph-databook file's own frontmatter."""
    claimant = graph.get("claimant")
    subject = graph.get("subject")
    if not (claimant and subject):
        return  # no subject/claimant — not an SCGraph, skip
    subj = graph["id"]
    emit_type(triples, subj, CELL + "SCGraph")
    emit_obj(triples, subj, CELL + "claimant", resolve(claimant))
    emit_obj(triples, subj, CELL + "subject", resolve(subject))

    # cell:template — domain cell:Graph, 0..N, present only on graphs that
    # contain instance(s) of a template type label class (e.g.
    # identitydocuments:Passport, cell.ttl's graph.png diagram). A graph may
    # hold more than one template's worth of content at once (e.g. a single
    # graph combining ServiceAccount, DebitCard, and CheckingAccount
    # instances), so this accepts either a bare string or a YAML list.
    for template in as_list(graph.get("template")):
        emit_obj(triples, subj, CELL + "template", resolve(template))
