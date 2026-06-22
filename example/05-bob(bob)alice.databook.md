---
id: http://www.example.org/mia/bob(bob)alice
title: "Bob Johnson — Bob context (Alice's view)"
type: context-databook
version: 2.0.2
created: 2026-06-15
description: >
  Alice's record of Bob Johnson in their 1:1 relationship context.
  Self-asserted by Alice; dyad partner is Bob's self-asserted Bob-context persona.
mia:
  name: "Bob"
  category: "context:People"
  assertedBy: ":Self"
  subject: ":Bob_Johnson"
  about-by: "context:OBS-Context"
  dyad: "http://www.example.org/mia/bob(bob)bob"
graph:
  named_graph: http://www.example.org/mia/bob(bob)alice#graph
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

This context captures Alice's record of Bob Johnson in their 1:1 relationship context. Alice notes Bob's favorite drink. It is paired (dyad) with `06-bob(bob)bob`, Bob's self-asserted Bob-context persona received from Bob's Mia.

## Identity Data

```turtle
<!-- databook:id: bob-bob-alice-identity -->
<!-- databook:graph: http://www.example.org/mia/bob(bob)alice#graph -->
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
