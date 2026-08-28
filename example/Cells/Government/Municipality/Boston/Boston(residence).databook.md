---
id: http://www.example.org/mia/cells/cell-07
title: "Boston"
type: cell-databook
version: 1.1.0
created: 2026-07-10
description: >
  Cell DataBook for folder "Boston" (cell:origin: cat:Residence). It is a one-member cell with one member entry about :Self.
mia:
  origin: "cat:Residence"
  creator: ":Self"
  memberCount: "cell:OneMember"
  members: "graph-13"
  graphs:
    - id: "http://www.example.org/mia/graphs/graph-13"
      claimant: ":Self"
      subject: ":Self"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/graph/shapes
---

## Graphs

<a id="graph-13"></a>
### Graph 13

#### Overview

This graph captures Alice Walker's previous residential address: 456 Commonwealth Ave, Boston, MA 02215. The address designation spans January 2020 to August 2025. See graph 18 for her current address. Alice is the claimant.

#### Graph

```turtle
<!-- databook:id: alice-boston-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-13#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

:Self <https://w3id.org/cco-domains/cco/ont00001879> :Address_Boston .  # designated by → Boston address


:Boston_Residence rdf:type owl:NamedIndividual ,
                           cco:ent00000016 ;  # AddressDesignation
    rdfs:label "Alice's Boston Residence (2020-2025)"@en ;
    rdfs:comment "Alice lived at this Boston address from 2020 to 2025."@en ;
    <http://purl.obolibrary.org/obo/BFO_0000057> :Self ;  # has participant
    <https://w3id.org/cco-domains/cco/ont00001879> :Address_Boston ;                  # designated by
    <http://purl.obolibrary.org/obo/BFO_0000199> :Interval_2020_2025 .   # occupies temporal region

:Interval_2020_2025 rdf:type owl:NamedIndividual ,
                             <http://purl.obolibrary.org/obo/BFO_0000038> ;  # TemporalInterval
    rdfs:label "2020-2025"@en ;
    cco:ent00000017 "2020-01-01"^^xsd:date ;
    cco:ent00000018 "2025-08-31"^^xsd:date .

:Address_Boston rdf:type owl:NamedIndividual ,
                         cco:ent00000010 ;  # USPostalAddress
    rdfs:label "Boston Address"@en ;
    <http://purl.obolibrary.org/obo/BFO_0000178> [  # has continuant part → Street
        rdf:type cco:ent00000011 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "456 Commonwealth Ave"
    ] ;
    <http://purl.obolibrary.org/obo/BFO_0000178> [  # has continuant part → City
        rdf:type cco:ent00000012 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "Boston"
    ] ;
    <http://purl.obolibrary.org/obo/BFO_0000178> [  # has continuant part → State
        rdf:type cco:ent00000013 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "MA"
    ] ;
    <http://purl.obolibrary.org/obo/BFO_0000178> [  # has continuant part → ZIP
        rdf:type cco:ent00000015 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "02215"
    ] .
```
