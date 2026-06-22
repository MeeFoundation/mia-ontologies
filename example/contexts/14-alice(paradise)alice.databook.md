---
id: http://www.example.org/mia/alice(paradise)alice
title: "About Alice Walker in the Municipality context as asserted by Alice Walker"
type: context-databook
version: 2.0.2
created: 2026-06-01
description: >
  Alice Walker's current residential address in Paradise, CA (September 2025 to present).
  Self-asserted by Alice; open-ended temporal interval indicates this is her current address.
mia:
  category: "http://www.example.org/mia/categories/municipality"
  assertedBy: ":Self"
  subject: ":Self"
  about-by: "context:SBS-Context"
graph:
  named_graph: http://www.example.org/mia/alice(paradise)alice#graph
  rdf_version: "1.1"
shapes:
  - http://www.example.org/shapes
process:
  transformer: human
  timestamp: 2026-06-19T00:00:00Z
  agent:
    name: Paul Trevithick
    role: author
---

## Overview

This context captures Alice Walker's current residential address: 123 Sleepy Hollow, Paradise, CA 95969. The address designation has a start date of September 2025 and no end date, indicating it is her current residence. See `15-alice(boston)alice` for her previous address.

## Identity Data

```turtle
<!-- databook:id: alice-paradise-identity -->
<!-- databook:graph: http://www.example.org/mia/alice(paradise)alice#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

:Self rdf:type owl:NamedIndividual ,
               persona:Person ;
    rdfs:label "Alice Walker (Paradise)"@en ;

    <https://purl.org/cco/ont00001879> :Address_Paradise .  # designated by → Paradise address


:Paradise_Residence rdf:type owl:NamedIndividual ,
                            cco:ent00000016 ;  # AddressDesignation
    rdfs:label "Alice's Paradise Residence (2025-present)"@en ;
    rdfs:comment "Alice has lived at this Paradise address since September 2025. No end date indicates current residence."@en ;
    <http://purl.obolibrary.org/obo/BFO_0000139> :Self ;  # has participant
    <https://purl.org/cco/ont00001879> :Address_Paradise ;                  # designated by
    <http://purl.obolibrary.org/obo/BFO_0000153> :Interval_2025_Present .  # occupies temporal region

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
        <https://purl.org/cco/ont00001765> "123 Sleepy Hollow"
    ] ;
    <http://purl.obolibrary.org/obo/BFO_0000178> [  # has continuant part → City
        rdf:type cco:ent00000012 ;
        <https://purl.org/cco/ont00001765> "Paradise"
    ] ;
    <http://purl.obolibrary.org/obo/BFO_0000178> [  # has continuant part → State
        rdf:type cco:ent00000013 ;
        <https://purl.org/cco/ont00001765> "CA"
    ] ;
    <http://purl.obolibrary.org/obo/BFO_0000178> [  # has continuant part → ZIP
        rdf:type cco:ent00000015 ;
        <https://purl.org/cco/ont00001765> "95969"
    ] ;
    <http://purl.obolibrary.org/obo/BFO_0000178> [  # has continuant part → Country
        rdf:type cco:ent00000014 ;
        <https://purl.org/cco/ont00001765> "USA"
    ] .
```
