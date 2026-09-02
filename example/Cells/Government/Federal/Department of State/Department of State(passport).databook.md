---
id: http://www.example.org/mia/cells/cell-05
title: "Department of State"
type: cell-databook
version: 1.2.0
created: 2026-07-10
description: >
  Cell DataBook for folder "Department of State" (cell:category: cat:Passport). It is a one-member cell with one member entry about :Self.
mia:
  category: "cat:Passport"
  creator: ":Self"
  owner: ":Self"
  member: "graph-19"
  graphs:
    - id: "http://www.example.org/mia/graphs/graph-19"
      claimant: ":Self"
      subject: ":Self"
      template: "persona:PassportDocument"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/graph/shapes
        - http://mee.foundation/ontologies/persona/shapes/passport
---

## Graphs

<a id="graph-19"></a>
### Graph 19

#### Overview

This graph captures Alice Walker's US passport identity data. Alice self-enters her legal name (Margery Alice Walker), date of birth (1985-07-04), US passport number (123456789), issue date (2021-07-04), expiration date (2031-07-04), place of birth (Austin, Texas, USA), gender marker (F), and a photo. Validated by the `Passport` per-template SHACL shapes. Alice is the claimant.

#### Graph

```turtle
<!-- databook:id: alice-passport-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-19#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

:Self persona:hasIdentityDocument :Alice_US_Passport ;
    <https://w3id.org/cco-domains/cco/ont00001879> :Alice_Passport_Number .  # Person designated by → Passport Number

:Alice_US_Passport rdf:type owl:NamedIndividual ,
                             persona:PassportDocument ;
    rdfs:label "Alice Walker's US Passport"@en ;
    rdfs:comment "Alice Walker's US passport identity data."@en ;

    # ── Legal name (matches Texas Birth Certificate and Driver's License) ────

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → GivenName (legal first name)
        rdf:type cco:ent00000002 ;  # GivenName
        <https://w3id.org/cco-domains/cco/ont00001765> "Margery"
    ] ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → AdditionalName (middle name)
        rdf:type cco:ent00000003 ;  # AdditionalName
        <https://w3id.org/cco-domains/cco/ont00001765> "Alice"
    ] ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → FamilyName
        rdf:type cco:ent00000004 ;  # FamilyName
        <https://w3id.org/cco-domains/cco/ont00001765> "Walker"
    ] ;

    # ── Dates ────────────────────────────────────────────────────────────────

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → Birthdate
        rdf:type cco:ent00000046 ;  # Birthdate
        <https://w3id.org/cco-domains/cco/ont00001765> "1985-07-04"^^xsd:date
    ] ;

    cco:ent00000069 [  # has issue date → Calendar Date Identifier
        rdf:type cco:ont00001340 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "2021-07-04"^^xsd:date
    ] ;

    cco:ent00000070 [  # has expiration date → Calendar Date Identifier
        rdf:type cco:ont00001340 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "2031-07-04"^^xsd:date
    ] ;

    # ── Passport number (two-relation form: Person designated-by, document is-carrier-of) ──

    <http://purl.obolibrary.org/obo/BFO_0000101> :Alice_Passport_Number ;  # document is carrier of → Passport Number

    # ── Issuing country ──────────────────────────────────────────────────────

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → Issuing Jurisdiction
        rdf:type cco:ent00000068 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "USA"
    ] ;

    # ── Place of birth ───────────────────────────────────────────────────────

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → Place of Birth
        rdf:type cco:ent00000067 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "Austin, Texas, USA"
    ] ;

    # ── Gender marker ────────────────────────────────────────────────────────

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → GenderMarker
        rdf:type persona:GenderMarker ;
        <https://w3id.org/cco-domains/cco/ont00001765> "F"
    ] ;

    # ── Photo ────────────────────────────────────────────────────────────────

    persona:hasPhoto "https://example.org/alice-passport-photo.jpg"^^xsd:anyURI .

:Alice_Passport_Number rdf:type owl:NamedIndividual ,
                                cco:ent00000066 ;  # Passport Number
    rdfs:label "Alice Walker's US Passport Number"@en ;
    <https://w3id.org/cco-domains/cco/ont00001765> "123456789" .  # placeholder US passport number
```
