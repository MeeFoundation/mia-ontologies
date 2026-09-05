#!/usr/bin/env python3
"""
validate-tier2.py — Tier 2 per-template SHACL validation, driven purely by
each graph's own `cell:template` (YAML `template:`) value.

Replaces the old hand-curated, per-graph bash command list in EXAMPLE.md with
one script implementing two rules (see CLAUDE.md's Validation/Check 5):

1. Each cell-databook is validated in isolation from every other cell — the
   outer loop below processes one cell-databook file at a time, and no two
   cells' extracted graph data are ever merged into the same `shacl validate`
   call. (The shared foundation/application ontologies merged in below are
   schema, not another cell's instance data, so merging those in doesn't
   violate this.)

2. Within a cell, a graph's own `template:` YAML value (one or more) is the
   *sole* indicator of what to validate that graph against — resolved via
   the TEMPLATE_TO_SHAPE table below, purely from each shape's own
   `sh:targetClass` (with two documented, named exceptions). A graph with no
   `template:` value needs no Tier 2 validation and is skipped outright.

Root-cause scoping fix: a class-wide shape targeting `persona:Person` directly
— in practice only `JSContactCardPersonShape`, since every other template's
shape targets a narrow, specific document/account class that only the one
real individual per graph is ever typed as — would otherwise fire on *every*
`persona:Person` individual present in a graph's merged test data, including
an incidental one such as the bare `:Self rdf:type ... persona:Person` every
graph re-asserts under the self-containment convention, which is not the
graph's own real subject and may legitimately lack a GivenName.

The graph's own YAML `subject:` isn't a safe stand-in for "the individual to
validate" here either — a member graph's `subject` can legitimately name a
non-`persona:Person` party (e.g. a Kyoto trip's Agent member has `subject:
":Alice_Travel_Agent"`, an `a:Agent`, while the real JSContactCard-conformant
content is asserted on `:Self` in that same graph). So whenever the resolved
shape's own declared target is exactly `sh:targetClass persona:Person`,
`scope_shape` (below) instead re-targets it at every *substantive*
`persona:Person` individual actually present in the graph's own extracted
data — one that carries at least one property beyond the bare `rdf:type`
triple the self-containment convention re-asserts — via `sh:targetNode`,
excluding any bare, data-free mention. Every *other* template's shape keeps
its own original targeting untouched — a narrow document/account class has no
such incidental-mention risk, so rewriting those would misfire, not fix
anything (e.g. `persona:PassportDocument` is asserted on a reified
`:Alice_US_Passport` individual, never on the graph's own `subject`, `:Self`).
In every case, every *other* root shape co-located in the same physical
shapes file is also stripped of its own targeting for that one validate
call, so it can't spuriously fire on the same merged data either.

Usage:   python3 validate-tier2.py
Exit:    0 if every checked graph conforms, 1 if any graph reports a
         violation or a template has no entry in TEMPLATE_TO_SHAPE.

Requires: pip install pyyaml rdflib   (plus Apache Jena's `riot`/`shacl` on PATH)
"""
import glob
import os
import subprocess
import sys
import tempfile

import yaml
from rdflib import Graph, URIRef
from rdflib.namespace import OWL, RDF, SH

from databook_graphs import as_list, extract_graph_block, split_frontmatter

# --- shapes-file namespace bases -------------------------------------------
# Each *-shacl.ttl file's own `@prefix :` base — a shape CURIE resolves to
# SHAPE_NS[shapes_file] + local_name.
SHAPE_NS = {
    "cell-templates-shacl.ttl":     "http://mee.foundation/ontologies/persona/shapes#",
    "persona-shacl.ttl":            "http://mee.foundation/ontologies/persona/shapes#",
    "shacl/jscontactcard-shacl.ttl": "http://mee.foundation/ontologies/persona/shapes#",
    "other/pets-shacl.ttl":         "http://mee.foundation/ontologies/pets/shapes#",
    "other/vehicles-shacl.ttl":     "http://mee.foundation/ontologies/vehicles/shapes#",
}

# --- template CURIE -> (shapes file, shape local name) ----------------------
# Rule: a shape's own sh:targetClass normally *is* the template CURIE it
# validates — so this table is just that pairing, one row per shape. Two
# documented exceptions, where the template is a label-only class distinct
# from the shape's real target (see persona-templates.ttl's own
# class-hierarchy comment, and CLAUDE.md Check 26's identical exemption):
#   persona:JSContactCard -> targets persona:Person directly (no reified document)
#   persona:DebitCard     -> targets cco:ent00000051 (a multi-typed CCO individual)
# Add a new row here whenever a new persona:PersonaTemplate-labeled
# document/shape pair is introduced.
TEMPLATE_TO_SHAPE = {
    "persona:BirthCertificateDocument": ("cell-templates-shacl.ttl",      "BirthCertificateDocumentShape"),
    "persona:DriversLicenseDocument":   ("cell-templates-shacl.ttl",      "DriversLicenseDocumentShape"),
    "persona:PassportDocument":         ("cell-templates-shacl.ttl",      "PassportDocumentShape"),
    "persona:MedicalAppointmentRecord": ("cell-templates-shacl.ttl",      "MedicalAppointmentRecordShape"),
    "persona:ServiceAccount":           ("cell-templates-shacl.ttl",      "ServiceAccountShape"),
    "persona:Residence":                ("cell-templates-shacl.ttl",      "ResidenceShape"),
    "persona:Itinerary":                ("cell-templates-shacl.ttl",      "ItineraryShape"),
    "persona:CheckingAccount":          ("persona-shacl.ttl",             "CheckingAccountShape"),
    "persona:DebitCard":                ("persona-shacl.ttl",             "DebitCardShape"),               # exception
    "persona:JSContactCard":            ("shacl/jscontactcard-shacl.ttl", "JSContactCardPersonShape"),     # exception
    "pets:Pet":                         ("other/pets-shacl.ttl",          "PetShape"),
    "pets:PetMedicationRecord":         ("other/pets-shacl.ttl",          "PetMedicationRecordShape"),
    "vehicles:Vehicle":                 ("other/vehicles-shacl.ttl",      "VehicleShape"),
}

BASE_ONTOLOGY_FILES = [
    "project_files/bfo-core.ttl",
    "project_files/PersonOntology.ttl",
    "project_files/AddressOntology.ttl",
    "project_files/StagingOntology.ttl",
    "project_files/UnitsOfMeasureOntology.ttl",
    "project_files/InformationEntityOntology.ttl",
    "project_files/dron-upper.ttl",
    "project_files/ncbitaxon-subset.ttl",
    "project_files/vbo-subset.ttl",
    "project_files/wikidata-vehicle-makes-subset.ttl",
    "project_files/wikidata-vehicle-models-subset.ttl",
    "project_files/prov-upper.ttl",
    "persona.ttl", "persona-templates.ttl", "cell.ttl", "category.ttl",
    "cell-templates.ttl", "other/pets.ttl", "other/vehicles.ttl",
    "organization.ttl", "agent.ttl",
]

TARGET_PROPS = [SH.targetClass, SH.targetNode, SH.targetObjectsOf, SH.targetSubjectsOf]

# The one class broad enough to risk an incidental same-type individual
# inside a single isolated graph (the self-containment convention's bare
# `:Self rdf:type ... persona:Person`) — see module docstring.
BROAD_PERSON_CLASS = URIRef("http://mee.foundation/ontologies/persona#Person")


def frontmatter(path):
    fm_text, _, body = split_frontmatter(open(path, encoding="utf-8").read())
    return yaml.safe_load(fm_text), body


def build_base(out_path):
    """Merge the shared foundation + application ontologies once, exactly as
    Tier 1/the old Tier 2 shared block already did."""
    subprocess.run(
        ["riot", "--output=turtle", *BASE_ONTOLOGY_FILES],
        check=True, stdout=open(out_path, "w"), stderr=subprocess.DEVNULL,
    )


def substantive_person_nodes(data_path):
    """Every persona:Person individual in data_path that carries at least
    one property beyond the bare rdf:type assertion the self-containment
    convention re-asserts on every referenced individual — i.e. excludes an
    incidental cross-referenced party (e.g. a bare `:Self`) that has no real
    content of its own in this particular graph."""
    dg = Graph()
    dg.parse(data_path, format="turtle")
    persons = set(dg.subjects(RDF.type, BROAD_PERSON_CLASS))
    return [p for p in persons if any(pred != RDF.type for pred, _ in dg.predicate_objects(p))]


def scope_shape(shapes_file, shape_local_name, data_path):
    """Load shapes_file and deactivate every root shape except the one
    named (strip their sh:targetClass/targetNode/etc., leaving their
    property/constraint triples intact in case the chosen shape reaches
    them as a nested value-shape via sh:node) — so nothing else co-located
    in the same physical file can independently fire against the small
    per-graph test data.

    If the chosen shape's own declared target is exactly
    `sh:targetClass persona:Person` (the one class broad enough to risk an
    incidental same-type individual within a single isolated graph — see
    module docstring), also re-target it at every substantive
    `persona:Person` individual actually found in data_path via
    sh:targetNode. Every other template's shape already targets a narrow,
    specific class with no such risk, so it's left with its own original
    targeting unchanged.

    Returns the scoped graph, serialized to a temp .ttl file path."""
    ns = SHAPE_NS[shapes_file]
    shape_uri = URIRef(ns + shape_local_name)

    g = Graph()
    g.parse(shapes_file, format="turtle")

    roots = {s for tp in TARGET_PROPS for s in g.subjects(tp, None)}
    if shape_uri not in roots:
        raise ValueError(f"{shape_local_name!r} has no target declaration in {shapes_file}")

    for s in roots:
        if s != shape_uri:
            for tp in TARGET_PROPS:
                g.remove((s, tp, None))

    if (shape_uri, SH.targetClass, BROAD_PERSON_CLASS) in g:
        g.remove((shape_uri, SH.targetClass, BROAD_PERSON_CLASS))
        for node in substantive_person_nodes(data_path):
            g.add((shape_uri, SH.targetNode, node))
    g.remove((None, OWL.imports, None))

    fd, path = tempfile.mkstemp(suffix=".ttl")
    os.close(fd)
    g.serialize(destination=path, format="turtle")
    return path


def run_shacl(shapes_path, data_path):
    result = subprocess.run(
        ["shacl", "validate", "--shapes", shapes_path, "--data", data_path, "--text"],
        capture_output=True, text=True,
    )
    text = result.stdout.strip()
    return text == "Conforms", text


def main():
    base_path = tempfile.mktemp(suffix=".ttl")
    build_base(base_path)

    checked = skipped = violations = unresolved = 0

    for cell_path in sorted(glob.glob("example/Cells/**/*.databook.md", recursive=True)):
        if "under-development" in cell_path.split(os.sep):
            continue
        fm, body = frontmatter(cell_path)
        if not fm or fm.get("type") != "cell-databook":
            continue
        mia = fm.get("mia", {}) or {}

        for entry in as_list(mia.get("graphs")):
            if not isinstance(entry, dict):
                continue
            gid = entry["id"]
            gid_local = gid.rsplit("/", 1)[-1]
            templates = as_list(entry.get("template"))
            if not templates:
                print(f"SKIP     {cell_path} {gid_local} (no template)")
                skipped += 1
                continue

            lines = extract_graph_block(body, f"{gid}#graph")
            if lines is None:
                print(f"ERROR    {cell_path} {gid_local}: no turtle block found")
                unresolved += 1
                continue

            fd, raw_path = tempfile.mkstemp(suffix=".ttl")
            with os.fdopen(fd, "w") as f:
                f.write("\n".join(lines))
            data_path = tempfile.mktemp(suffix=".ttl")
            subprocess.run(
                ["riot", "--output=turtle", base_path, raw_path],
                check=True, stdout=open(data_path, "w"), stderr=subprocess.DEVNULL,
            )

            for template in templates:
                label = f"{cell_path} {gid_local} [{template}]"
                if template not in TEMPLATE_TO_SHAPE:
                    print(f"UNKNOWN  {label}: no TEMPLATE_TO_SHAPE entry")
                    unresolved += 1
                    continue
                shapes_file, shape_local_name = TEMPLATE_TO_SHAPE[template]
                shape_path = scope_shape(shapes_file, shape_local_name, data_path)
                conforms, text = run_shacl(shape_path, data_path)
                checked += 1
                if conforms:
                    print(f"OK       {label}")
                else:
                    print(f"VIOLATION {label}\n{text}")
                    violations += 1

    print()
    print(f"Checked: {checked}   Skipped (no template): {skipped}   "
          f"Violations: {violations}   Unresolved: {unresolved}")
    sys.exit(1 if (violations or unresolved) else 0)


if __name__ == "__main__":
    main()
