#!/usr/bin/env python3
"""
draw.py  —  Generate a Graphviz diagram from a Persona context .ttl file.

Usage:   python draw.py <context_file.ttl>
Output:  <context_file>.png next to the input file.

Requires: pip install rdflib graphviz   +   brew install graphviz
"""

import sys
from hashlib import md5
from pathlib import Path

from rdflib import BNode, Graph, Literal, Namespace, URIRef
from rdflib.namespace import OWL, RDF, RDFS
from graphviz import Digraph

# ── Namespaces ────────────────────────────────────────────────────────────────
PERSONA = Namespace("http://mee.foundation/ontologies/persona#")

DESIGNATED_BY  = URIRef("https://purl.org/cco/ont00001879")
HAS_TEXT_VALUE = URIRef("https://purl.org/cco/ont00001765")

# ── Human-readable labels for well-known IRIs ─────────────────────────────────
LABELS = {
    # persona: context classes
    str(PERSONA.Persona):               "p:Persona",
    str(PERSONA.Company):               "p:Company",
    str(PERSONA.Career):                "p:Career",
    str(PERSONA.Government):            "p:Government",
    str(PERSONA.Federal):               "p:Federal",
    str(PERSONA.State):                 "p:State",
    str(PERSONA.BirthCertificate):      "p:BirthCertificate",
    str(PERSONA.Municipality):          "p:Municipality",
    str(PERSONA.People):                "p:People",
    str(PERSONA.Family):                "p:Family",
    str(PERSONA.Friends):               "p:Friends",
    str(PERSONA.Professionals):         "p:Professionals",
    str(PERSONA.Colleague):             "p:Colleague",
    # persona: domain classes
    str(PERSONA.CheckingAccount):       "CheckingAccount",
    str(PERSONA.CheckingAccountNumber): "Account Number",
    str(PERSONA.RoutingNumber):         "Routing Number",
    str(PERSONA.PhysicalCard):          "PhysicalCard",
    str(PERSONA.Wallet):                "Wallet",
    str(PERSONA.DriversLicense):        "DriversLicense",
    str(PERSONA.HealthInsuranceCard):   "HealthInsuranceCard",
    # persona: properties
    str(PERSONA.holdsPaymentCard):      "holdsPaymentCard",
    str(PERSONA.holdsBankAccount):      "holdsBankAccount",
    str(PERSONA.accessesBankAccount):   "accessesBankAccount",
    str(PERSONA.hasSocialNetwork):      "hasSocialNetwork",
    str(PERSONA.hasPersona):             "hasPersona",
    str(PERSONA.hasPassword):           "has password",
    str(PERSONA.holdsWallet):           "holdsWallet",
    "http://purl.obolibrary.org/obo/BFO_0000101":  "is carrier of",
    str(PERSONA.hasImageScan):          "hasImageScan",
    # cco: entity classes (designators / identifiers)
    "https://purl.org/cco/ent00000001": "FullName",
    "https://purl.org/cco/ent00000002": "GivenName",
    "https://purl.org/cco/ent00000003": "AdditionalName",
    "https://purl.org/cco/ent00000004": "FamilyName",
    "https://purl.org/cco/ent00000006": "AlternateName",
    "https://purl.org/cco/ent00000008": "SSN",
    "https://purl.org/cco/ent00000010": "USPostalAddress",
    "https://purl.org/cco/ent00000011": "StreetAddress",
    "https://purl.org/cco/ent00000012": "CityName",
    "https://purl.org/cco/ent00000013": "StateName",
    "https://purl.org/cco/ent00000014": "CountryName",
    "https://purl.org/cco/ent00000015": "PostalCode",
    "https://purl.org/cco/ent00000016": "AddressDesignation",
    "https://purl.org/cco/ent00000023": "TelephoneNumber",
    "https://purl.org/cco/ent00000024": "EmailAddress",
    "https://purl.org/cco/ent00000033": "OnlineServiceAccount",
    "https://purl.org/cco/ent00000049": "PaymentCard",
    "https://purl.org/cco/ent00000051": "Debit Card",
    "https://purl.org/cco/ent00000052": "Card Number",
    "https://purl.org/cco/ent00000053": "CVV",
    "https://purl.org/cco/ent00000054": "Expiration Date",
    # cco: ont classes
    "https://purl.org/cco/ont00001262": "Person",
    "https://purl.org/cco/ont00001183": "SocialNetwork",
    "https://purl.org/cco/ont00000995": "MaterialArtifact",
    "https://purl.org/cco/ont00000020": "Container",
    "https://purl.org/cco/ont00000058": "ScalpHair",
    "https://purl.org/cco/ont00001022": "RatioMeasurementICE",
    "https://purl.org/cco/ont00000967": "Height",
    # cco: properties
    str(DESIGNATED_BY):                        "designated by",
    str(HAS_TEXT_VALUE):                       "has text value",
    "https://purl.org/cco/ent00000034":        "has service name",
    "https://purl.org/cco/ent00000035":        "has user handle",
    "https://purl.org/cco/ent00000036":        "has service URI",
    "https://purl.org/cco/ent00000045":        "holds user account",
    "https://purl.org/cco/ont00001780":        "has mother",
    "https://purl.org/cco/ont00001786":        "is mother of",
    "https://purl.org/cco/ont00001769":        "has decimal value",
    "https://purl.org/cco/ont00001863":        "uses measurement unit",
    "https://purl.org/cco/ont00001983":        "is ratio measurement of",
    "https://purl.org/cco/ent00000017":        "has start date",
    "https://purl.org/cco/ent00000018":        "has end date",
    "http://purl.obolibrary.org/obo/BFO_0000051":  "has part",
    "http://purl.obolibrary.org/obo/BFO_0000115":  "has member part",
    "http://purl.obolibrary.org/obo/BFO_0000153":  "occupies temporal region",
    "http://purl.obolibrary.org/obo/BFO_0000139":  "has participant",
    "http://purl.obolibrary.org/obo/BFO_0000178":  "has continuant part",
    "http://purl.obolibrary.org/obo/BFO_0000196":  "bearer of",
    "http://purl.obolibrary.org/obo/BFO_0000038":  "TemporalInterval",
}

# Triples to skip — annotation-only
SKIP_PROPS = {
    str(RDF.type),
    str(RDFS.label),
    str(RDFS.comment),
    str(OWL.versionInfo),
    str(OWL.imports),
}

# rdf:type values that are not worth showing as class boxes
SKIP_TYPES = {OWL.NamedIndividual, OWL.Thing, OWL.Ontology}


def lbl(iri: URIRef) -> str:
    s = str(iri)
    if s in LABELS:
        return LABELS[s]
    return s.split("#")[-1] if "#" in s else s.split("/")[-1]


def nid(key: str) -> str:
    return "n" + md5(key.encode()).hexdigest()[:12]


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("Usage: python draw.py <context_file.ttl>")
    src = Path(sys.argv[1])
    if not src.exists():
        sys.exit(f"File not found: {src}")

    g = Graph()
    g.parse(str(src), format="turtle")

    individuals = {
        s for s in g.subjects(RDF.type, OWL.NamedIndividual)
        if isinstance(s, URIRef)
    }

    dot = Digraph(
        name=src.stem,
        graph_attr={
            "rankdir": "TB",
            "fontname": "Helvetica",
            "fontsize": "11",
        },
        node_attr={"fontname": "Helvetica", "fontsize": "11"},
        edge_attr={"fontname": "Helvetica", "fontsize": "9"},
    )
    added: set[str] = set()

    def class_node(iri: URIRef) -> str:
        i = nid("class:" + str(iri))
        if i not in added:
            dot.node(i, lbl(iri), shape="plaintext", fontsize="10")
            added.add(i)
        return i

    def ind_node(iri: URIRef) -> str:
        i = nid("ind:" + str(iri))
        if i not in added:
            local = str(iri).split("#")[-1] if "#" in str(iri) else str(iri).split("/")[-1]
            types = set(g.objects(iri, RDF.type))
            is_persona = PERSONA.Persona in types or URIRef("https://purl.org/cco/ont00001262") in types
            fill = "yellow" if is_persona else "white"
            dot.node(i, f":{local}", shape="box", style="filled", fillcolor=fill)
            added.add(i)
        return i

    def lit_node(value: str, key: str) -> str:
        i = nid("lit:" + key)
        if i not in added:
            dot.node(i, value, shape="none", fontcolor="darkgreen", fontsize="10")
            added.add(i)
        return i

    MIA_NS = "http://www.example.org/mia#"

    def ext_node(iri: URIRef) -> str:
        """Node for an individual defined in another context file."""
        i = nid("ext:" + str(iri))
        if i not in added:
            local = str(iri).split("#")[-1] if "#" in str(iri) else str(iri).split("/")[-1]
            dot.node(i, f":{local}", shape="box", style="dashed")
            added.add(i)
        return i

    for ind in individuals:
        src_nid = ind_node(ind)

        # rdf:type → class boxes; draw class→ind so class ranks above instance
        for t in g.objects(ind, RDF.type):
            if t in SKIP_TYPES or not isinstance(t, URIRef):
                continue
            cn = class_node(t)
            dot.edge(cn, src_nid, label="isa", style="dashed", fontsize="9", dir="back")

        # all properties
        for pred, obj in g.predicate_objects(ind):
            if str(pred) in SKIP_PROPS:
                continue
            if isinstance(obj, BNode):
                bid = nid("bnode:" + str(obj))
                if bid not in added:
                    dot.node(bid, "_:blank", shape="plaintext", fontsize="9")
                    added.add(bid)
                dot.edge(src_nid, bid, label=lbl(pred), fontsize="9")
                btype = g.value(obj, RDF.type)
                if btype:
                    cn = class_node(btype)
                    dot.edge(cn, bid, label="isa", style="dashed", fontsize="9", dir="back")
                tv = g.value(obj, HAS_TEXT_VALUE)
                if tv:
                    ln = lit_node(str(tv), str(ind) + str(obj))
                    dot.edge(bid, ln, label="has text value", fontsize="9")
            elif isinstance(obj, URIRef):
                if obj in individuals:
                    dot.edge(src_nid, ind_node(obj), label=lbl(pred))
                elif str(obj).startswith(MIA_NS):
                    dot.edge(src_nid, ext_node(obj), label=lbl(pred))
            elif isinstance(obj, Literal):
                ln = lit_node(str(obj), str(ind) + str(pred) + str(obj))
                dot.edge(src_nid, ln, label=lbl(pred))

    # contextType annotation on the ontology IRI → styled graph label, top-right
    ontology_iri = g.value(predicate=RDF.type, object=OWL.Ontology)
    if ontology_iri:
        ctype = g.value(ontology_iri, PERSONA.contextType)
        if ctype:
            dot.attr(
                label=(
                    f'<<TABLE BORDER="1" CELLBORDER="0" CELLPADDING="5" '
                    f'BGCOLOR="lightblue" COLOR="steelblue" STYLE="rounded">'
                    f'<TR><TD><FONT FACE="Helvetica" POINT-SIZE="10">'
                    f'ContextType: {lbl(ctype)}'
                    f'</FONT></TD></TR></TABLE>>'
                ),
                labelloc="t",
                labeljust="r",
            )

    out = str(src.with_suffix(""))
    dot.render(out, format="png", cleanup=True)
    print(f"Written: {out}.png")


if __name__ == "__main__":
    main()
