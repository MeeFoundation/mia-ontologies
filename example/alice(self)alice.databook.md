---
id: http://www.example.org/mia
title: "Alice Walker — Selfness"
type: databook
version: 4.0.3
created: 2026-06-19
description: >
  Alice Walker's selfness — the central identity individual. Records physical
  characteristics intrinsic to Alice (height, eye color, hair color) and her
  maternal relationship to Paula Walker.
mia:
  name: "Alice Walker"
  assertedBy: ":Self"
  subject: ":Self"
graph:
  named_graph: http://www.example.org/mia#graph
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

This context captures Alice Walker's selfness — the central identity individual for Alice's Mia instance. It holds only properties intrinsic to Alice as a person: physical characteristics and family relationships. All other identity data (names, addresses, identifiers, payment cards, etc.) belongs to context-specific personas in the numbered context files. Alice's `persona:Person` individual always uses the IRI `:Self` across all of her context files.

## Identity Data

```turtle
<!-- databook:id: alice-self-identity -->
<!-- databook:graph: http://www.example.org/mia#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

:Self rdf:type owl:NamedIndividual ,
               persona:Person ;
    rdfs:label "Alice Walker"@en ;
    rdfs:comment "Alice Walker's selfness — the central identity individual."@en ;

    # PREFERRED NAME (goes by across all contexts)
    <https://purl.org/cco/ont00001879> [  # designated by → AlternateName
        rdf:type cco:ent00000006 ;  # AlternateName
        <https://purl.org/cco/ont00001765> "Alice Walker" ;
        rdfs:comment "Name she goes by professionally and socially"@en
    ] ;

    # PHYSICAL CHARACTERISTICS

    <http://purl.obolibrary.org/obo/BFO_0000196> :Alice_Height ;
    <http://purl.obolibrary.org/obo/BFO_0000196> :Alice_Height_Measurement ;

    <http://purl.obolibrary.org/obo/BFO_0000196> [  # bearer of → Eye Color
        rdf:type cco:ent00000040 ;  # Blue Eye Color
        rdfs:comment "Eye color: Blue"@en
    ] ;

    <http://purl.obolibrary.org/obo/BFO_0000178> [  # has continuant part → Scalp Hair
        rdf:type cco:ont00000058 ;  # Scalp Hair
        <http://purl.obolibrary.org/obo/BFO_0000196> [  # bearer of → Hair Color
            rdf:type cco:ont00000026 ;  # Hair Color
            <https://purl.org/cco/ont00001765> "Grey" ;
            rdfs:comment "Hair color: Grey"@en
        ]
    ] ;

    # FAMILY RELATIONSHIPS

    cco:ont00001780 :Paula_Walker .  # has mother


:Alice_Height rdf:type owl:NamedIndividual ,
                       <https://purl.org/cco/ont00000967> ;  # Height (CCO Quality)
    rdfs:label "Alice Walker's height"@en .

:Alice_Height_Measurement rdf:type owl:NamedIndividual ,
                                   <https://purl.org/cco/ont00001022> ;  # Ratio Measurement ICE
    <https://purl.org/cco/ont00001983> :Alice_Height ;
    <https://purl.org/cco/ont00001863> <https://purl.org/cco/ont00001677> ;  # uses measurement unit: Inch
    <https://purl.org/cco/ont00001769> "68"^^xsd:decimal .  # has decimal value
```
