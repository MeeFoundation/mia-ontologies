---
id: http://www.example.org/mia/alice(health)alice
title: "Alice Walker — Physical Body"
type: databook
version: 1.0.0
created: 2026-06-20
description: >
  Alice Walker's physical body characteristics: height, eye color, and hair color.
  Self-asserted by Alice.
mia:
  name: "PhysicalBody"
  contextCategory: "context:Health"
  assertedBy: ":Self"
  subject: ":Self"
graph:
  named_graph: http://www.example.org/mia/alice(health)alice#graph
  rdf_version: "1.1"
shapes:
  - http://www.example.org/shapes
process:
  transformer: human
  timestamp: 2026-06-20T00:00:00Z
  agent:
    name: Paul Trevithick
    role: author
---

## Overview

This context captures Alice Walker's physical body characteristics — properties that are intrinsic to her as a person and do not belong to any particular institutional or social context. Height is recorded as a CCO Height quality with a RatioMeasurementICE (68 inches). Eye color is modeled as Alice bearing a BlueEyeColor quality directly. Hair color is borne by her ScalpHair continuant part.

## Identity Data

```turtle
<!-- databook:id: alice-health-identity -->
<!-- databook:graph: http://www.example.org/mia/alice(health)alice#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

:Self rdf:type owl:NamedIndividual ,
               persona:Person ;
    rdfs:label "Alice Walker (Physical Body)"@en ;
    rdfs:comment "Alice Walker's physical body characteristics."@en ;

    # ── Height ───────────────────────────────────────────────────────────────

    <http://purl.obolibrary.org/obo/BFO_0000196> :Alice_Height ;
    <http://purl.obolibrary.org/obo/BFO_0000196> :Alice_Height_Measurement ;

    # ── Eye color ────────────────────────────────────────────────────────────

    <http://purl.obolibrary.org/obo/BFO_0000196> [  # bearer of → Eye Color
        rdf:type cco:ent00000040 ;  # Blue Eye Color
        rdfs:comment "Eye color: Blue"@en
    ] ;

    # ── Hair ─────────────────────────────────────────────────────────────────

    <http://purl.obolibrary.org/obo/BFO_0000178> [  # has continuant part → Scalp Hair
        rdf:type cco:ont00000058 ;  # Scalp Hair
        <http://purl.obolibrary.org/obo/BFO_0000196> [  # bearer of → Hair Color
            rdf:type cco:ont00000026 ;  # Hair Color
            <https://purl.org/cco/ont00001765> "Grey" ;
            rdfs:comment "Hair color: Grey"@en
        ]
    ] .


:Alice_Height rdf:type owl:NamedIndividual ,
                       <https://purl.org/cco/ont00000967> ;  # Height (CCO Quality)
    rdfs:label "Alice Walker's height"@en .

:Alice_Height_Measurement rdf:type owl:NamedIndividual ,
                                   <https://purl.org/cco/ont00001022> ;  # Ratio Measurement ICE
    <https://purl.org/cco/ont00001983> :Alice_Height ;
    <https://purl.org/cco/ont00001863> <https://purl.org/cco/ont00001677> ;  # uses measurement unit: Inch
    <https://purl.org/cco/ont00001769> "68"^^xsd:decimal .  # has decimal value
```
