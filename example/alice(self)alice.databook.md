---
id: http://www.example.org/mia
title: "Alice Walker — Selfness"
type: databook
version: 4.0.5
created: 2026-06-19
description: >
  Alice Walker's selfness — the central identity individual. Records her preferred
  name (Alice Walker) and her maternal relationship to Paula Walker. Physical body
  characteristics have moved to 24-alice(health)alice.
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

This context captures Alice Walker's selfness — the central identity individual for Alice's Mia instance. It holds Alice's preferred name (the name she goes by across all contexts) and her maternal family relationship. Physical body characteristics (height, eye color, hair color) have moved to `24-alice(health)alice`. All other identity data (addresses, identifiers, payment cards, etc.) belongs to context-specific personas in the numbered context files. Alice's `persona:Person` individual always uses the IRI `:Self` across all of her context files.

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

    # FAMILY RELATIONSHIPS

    cco:ont00001780 :Paula_Walker .  # has mother
```
