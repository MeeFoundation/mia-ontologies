---
id: https://www.example.org/mia/topics/bob-johnson.self(bob-johnson)(others)(04)
title: "About Bob Johnson in the Others cell as claimed by Alice Walker"
type: topic-databook
version: 2.0.13
created: 2026-06-15
description: >
  Alice's record of Bob Johnson in their 1:1 relationship topic.
mia:
  claimant: ":Self"
  subject: ":Bob_Johnson"
graph:
  named_graph: https://www.example.org/mia/topics/bob-johnson.self(bob-johnson)(others)(04)#graph
  rdf_version: "1.1"
shapes:
  - http://mee.foundation/ontologies/persona/shapes
  - http://mee.foundation/ontologies/topic/shapes
process:
  transformer: human
  timestamp: 2026-06-19T00:00:00Z
  agent:
    name: Paul Trevithick
    role: author
---

## Overview

This topic captures Alice's record of Bob Johnson in their 1:1 relationship topic. Alice notes Bob's favorite drink.

## Topic Graph

```turtle
<!-- databook:id: bob-bob-alice-topic-graph -->
<!-- databook:graph: https://www.example.org/mia/topics/bob-johnson.self(bob-johnson)(others)(04)#graph -->
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
