---
id: http://www.example.org/mia/cells/cell-01
title: "Boston Hub Society"
type: cell-databook
version: 1.2.0
created: 2026-07-10
description: >
  Cell DataBook for folder "Boston Hub Society" (cell:category: cat:Affiliations). It is a multi-member cell with three members about :BHS, :Self, and :Bob_Johnson.
mia:
  category: "cat:Affiliations"
  creator: ":Self"
  owner: ":Self"
  member:
    - "graph-01"
    - "graph-14"
    - "graph-03"
  graphs:
    - id: "http://www.example.org/mia/graphs/graph-01"
      claimant: ":BHS"
      subject: ":BHS"
    - id: "http://www.example.org/mia/graphs/graph-03"
      claimant: ":Bob_Johnson"
      subject: ":Bob_Johnson"
    - id: "http://www.example.org/mia/graphs/graph-14"
      claimant: ":Self"
      subject: ":Self"
---

## Graphs

<a id="graph-01"></a>
### Graph 01

#### Overview

This graph captures the Boston Hub Society as an `o:Organization`. In our example BHS is compatible with PDN and participates directly as a member of this cell, alongside Alice and Bob. BHS asserts a basic profile about itself here. BHS is the claimant.

#### Graph

```turtle
<!-- databook:id: bhs-org-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-01#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix o: <http://mee.foundation/ontologies/organization#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:BHS rdf:type owl:NamedIndividual ,
             o:Organization ;
    rdfs:label "Boston Hub Society"@en ;

    <https://w3id.org/cco-domains/cco/ont00001917> [  # described by → Organization Note
        rdf:type cco:ent00000048 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "An informal Boston-area professional networking society. Current members include Alice Walker and Bob Johnson."
    ] .
```

<a id="graph-03"></a>
### Graph 03

#### Overview

This graph captures Bob Johnson's BHS profile as transmitted from Bob's own instance of the app to Alice's over the PDN. It records the name Bob presents to the Boston Hub Society. Bob is the claimant.

#### Graph

```turtle
<!-- databook:id: bob-bhs-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-03#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Bob_Johnson rdf:type owl:NamedIndividual ,
              persona:Person ;
    rdfs:label "Bob Johnson (BHS)"@en ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → GivenName
        rdf:type cco:ent00000002 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "Bob"
    ] ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → FamilyName
        rdf:type cco:ent00000004 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "Johnson"
    ] .
```

<a id="graph-14"></a>
### Graph 14

#### Overview

This graph captures Alice Walker's BHS profile — the identity data she shares with the Boston Hub Society. It includes her current Paradise, CA address, her phone number, and her Gmail address. Alice is the claimant.

#### Graph

```turtle
<!-- databook:id: alice-bhs-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-14#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Self rdfs:comment "Alice Walker's persona for her BHS profile."@en ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → AlternateName
        rdf:type cco:ent00000006 ;  # AlternateName
        <https://w3id.org/cco-domains/cco/ont00001765> "Alice Walker"
    ] ;

    <https://w3id.org/cco-domains/domains/AddressOntology#ent00000324> :Address_BHS ;  # has address → current address

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → Phone
        rdf:type cco:ent00000023 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "+15108149999"
    ] ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → Email
        rdf:type cco:ent00000024 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "awalker@gmail.com"
    ] .


:Address_BHS rdf:type owl:NamedIndividual ,
                      cco:ent00000010 ;  # USPostalAddress
    rdfs:label "Alice Walker's BHS Address"@en ;
    <http://purl.obolibrary.org/obo/BFO_0000178> [  # has continuant part → Street
        rdf:type cco:ent00000011 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "123 Sleepy Hollow"
    ] ;
    <http://purl.obolibrary.org/obo/BFO_0000178> [  # has continuant part → City
        rdf:type cco:ent00000012 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "Paradise"
    ] ;
    <http://purl.obolibrary.org/obo/BFO_0000178> [  # has continuant part → State
        rdf:type cco:ent00000013 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "CA"
    ] ;
    <http://purl.obolibrary.org/obo/BFO_0000178> [  # has continuant part → ZIP
        rdf:type cco:ent00000015 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "95969"
    ] ;
    <http://purl.obolibrary.org/obo/BFO_0000178> [  # has continuant part → Country
        rdf:type cco:ent00000014 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "USA"
    ] .

:BHS_AddressDesignation rdf:type owl:NamedIndividual ,
                                  cco:ent00000016 ;  # AddressDesignation
    rdfs:label "Alice Walker's BHS address designation"@en ;
    <http://purl.obolibrary.org/obo/BFO_0000057> :Self ;
    <https://w3id.org/cco-domains/domains/AddressOntology#ent00000324> :Address_BHS .

```
