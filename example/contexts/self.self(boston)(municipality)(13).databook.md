---
id: https://www.example.org/mia/contexts/self.self(boston)(municipality)(13)
title: "About Alice Walker in the Municipality context as asserted by Alice Walker"
type: context-databook
version: 2.0.4
created: 2026-06-01
description: >
  Alice Walker's previous residential address in Boston, MA (January 2020 to August 2025).
  Self-asserted by Alice; closed temporal interval indicates this is a past address.
mia:
  category: "http://www.example.org/mia/categories/boston(municipality)"
  assertedBy: ":Self"
  subject: ":Self"
  about-by: "context:SBS-Context"
graph:
  named_graph: https://www.example.org/mia/contexts/self.self(boston)(municipality)(13)#graph
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

This context captures Alice Walker's previous residential address: 456 Commonwealth Ave, Boston, MA 02215. The address designation spans January 2020 to August 2025. See `14-alice(paradise)alice` for her current address.

## Identity Data

```turtle
<!-- databook:id: alice-boston-identity -->
<!-- databook:graph: https://www.example.org/mia/contexts/self.self(boston)(municipality)(13)#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

:Self rdf:type owl:NamedIndividual ,
               persona:Person ;
    rdfs:label "Alice Walker (Boston)"@en ;

    <https://purl.org/cco/ont00001879> :Address_Boston .  # designated by → Boston address


:Boston_Residence rdf:type owl:NamedIndividual ,
                           cco:ent00000016 ;  # AddressDesignation
    rdfs:label "Alice's Boston Residence (2020-2025)"@en ;
    rdfs:comment "Alice lived at this Boston address from 2020 to 2025."@en ;
    <http://purl.obolibrary.org/obo/BFO_0000139> :Self ;  # has participant
    <https://purl.org/cco/ont00001879> :Address_Boston ;                  # designated by
    <http://purl.obolibrary.org/obo/BFO_0000153> :Interval_2020_2025 .   # occupies temporal region

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
        <https://purl.org/cco/ont00001765> "456 Commonwealth Ave"
    ] ;
    <http://purl.obolibrary.org/obo/BFO_0000178> [  # has continuant part → City
        rdf:type cco:ent00000012 ;
        <https://purl.org/cco/ont00001765> "Boston"
    ] ;
    <http://purl.obolibrary.org/obo/BFO_0000178> [  # has continuant part → State
        rdf:type cco:ent00000013 ;
        <https://purl.org/cco/ont00001765> "MA"
    ] ;
    <http://purl.obolibrary.org/obo/BFO_0000178> [  # has continuant part → ZIP
        rdf:type cco:ent00000015 ;
        <https://purl.org/cco/ont00001765> "02215"
    ] .
```
