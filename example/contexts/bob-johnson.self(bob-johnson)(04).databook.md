---
id: https://www.example.org/mia/contexts/bob-johnson.self(bob-johnson)(04)
title: "About Bob Johnson in the People context as asserted by Alice Walker"
type: context-databook
version: 2.0.2
created: 2026-06-15
description: >
  Alice's record of Bob Johnson in their 1:1 relationship context.
mia:
  category: "http://www.example.org/mia/categories/people"
  assertedBy: ":Self"
  subject: ":Bob_Johnson"
  about-by: "context:OBS-Context"
graph:
  named_graph: https://www.example.org/mia/contexts/bob-johnson.self(bob-johnson)(04)#graph
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

This context captures Alice's record of Bob Johnson in their 1:1 relationship context. Alice notes Bob's favorite drink.

## Identity Data

```turtle
<!-- databook:id: bob-bob-alice-identity -->
<!-- databook:graph: https://www.example.org/mia/contexts/bob-johnson.self(bob-johnson)(04)#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Bob_Johnson rdf:type owl:NamedIndividual ,
              persona:Person ;
    rdfs:label "Bob Johnson (Bob-colleague-of-alice)"@en ;

    <https://purl.org/cco/ont00001917> [  # described by → Person Note
        rdf:type cco:ent00000048 ;
        <https://purl.org/cco/ont00001765> "Fav drink: oat milk cappuccino"
    ] .
```
