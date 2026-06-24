---
id: http://www.example.org/mia/paula.self(family)(02)
title: "About Paula Walker in the Family context as asserted by Alice Walker"
type: context-databook
version: 2.0.4
created: 2026-06-14
description: >
  Alice's record of her family member Paula Walker, including Paula's given and family name.
mia:
  category: "http://www.example.org/mia/categories/family"
  assertedBy: ":Self"
  subject: ":Paula_Walker"
  about-by: "context:OBS-Context"
graph:
  named_graph: http://www.example.org/mia/paula.self(family)(02)#graph
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

This context captures Alice's record of her family member Paula Walker. Alice asserts Paula's name in the family context.

## Identity Data

```turtle
<!-- databook:id: paula-family-alice-identity -->
<!-- databook:graph: http://www.example.org/mia/paula.self(family)(02)#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Paula_Walker rdf:type owl:NamedIndividual ,
               persona:Person ;
    rdfs:label "Paula Walker (Family)"@en ;

    <https://purl.org/cco/ont00001879> [  # designated by → GivenName
        rdf:type cco:ent00000002 ;  # GivenName
        <https://purl.org/cco/ont00001765> "Paula"  # has text value
    ] ;

    <https://purl.org/cco/ont00001879> [  # designated by → FamilyName
        rdf:type cco:ent00000004 ;  # FamilyName
        <https://purl.org/cco/ont00001765> "Walker"  # has text value
    ] .
```
