---
id: http://www.example.org/mia/cells/cell-08
title: "Paradise"
type: cell-databook
version: 1.1.0
created: 2026-07-10
description: >
  Cell DataBook for folder "Paradise" (cell:origin: cat:Residence). It is a one-member cell with one member entry about :Self.
mia:
  origin: "cat:Residence"
  creator: ":Self"
  members: "graph-18"
  graphs:
    - id: "http://www.example.org/mia/graphs/graph-18"
      claimant: ":Self"
      subject: ":Self"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/graph/shapes
---

## Graphs

<a id="graph-18"></a>
### Graph 18

#### Overview

This graph captures Alice Walker's current residential address: 123 Sleepy Hollow, Paradise, CA 95969. The address designation has a start date of September 2025 and no end date, indicating it is her current residence. See `15-alice(boston)alice` for her previous address. Alice is the claimant.

#### Graph

```turtle
<!-- databook:id: alice-paradise-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-18#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .



:Paradise_Residence rdf:type owl:NamedIndividual ,
                            cco:ent00000016 ;  # AddressDesignation
    rdfs:label "Alice's Paradise Residence (2025-present)"@en ;
    rdfs:comment "Alice has lived at this Paradise address since September 2025. No end date indicates current residence."@en ;
    <http://purl.obolibrary.org/obo/BFO_0000057> :Self ;  # has participant
    <https://w3id.org/cco-domains/domains/AddressOntology#ent00000324> :Address_Paradise ;  # has address
    <http://purl.obolibrary.org/obo/BFO_0000199> :Interval_2025_Present .  # occupies temporal region

:Interval_2025_Present rdf:type owl:NamedIndividual ,
                                <http://purl.obolibrary.org/obo/BFO_0000038> ;  # TemporalInterval
    rdfs:label "September 2025 to present"@en ;
    rdfs:comment "Open-ended interval — absence of end date indicates current/ongoing."@en ;
    cco:ent00000017 "2025-09-01"^^xsd:date .
    # No cco:ent00000018 = still current

:Address_Paradise rdf:type owl:NamedIndividual ,
                          cco:ent00000010 ;  # USPostalAddress
    rdfs:label "Paradise Address"@en ;
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
```
