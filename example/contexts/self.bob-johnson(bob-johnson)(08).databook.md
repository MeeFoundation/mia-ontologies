---
id: http://www.example.org/mia/self.bob-johnson(bob-johnson)(08)
title: "About Alice Walker in the People context as asserted by Bob Johnson"
type: context-databook
version: 2.0.2
created: 2026-06-13
description: >
  Bob's record of Alice in their 1:1 relationship context, received from Bob's Mia via PDN.
mia:
  category: "http://www.example.org/mia/categories/people"
  assertedBy: ":Bob_Johnson"
  subject: ":Self"
  about-by: "context:SBO-Context"
graph:
  named_graph: http://www.example.org/mia/self.bob-johnson(bob-johnson)(08)#graph
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

This context captures Bob's record of Alice in their 1:1 relationship context, transmitted from Bob's Mia to Alice's Mia over the PDN. Bob notes Alice's favorite drink.

## Identity Data

```turtle
<!-- databook:id: alice-bob-bob-identity -->
<!-- databook:graph: http://www.example.org/mia/self.bob-johnson(bob-johnson)(08)#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Self rdf:type owl:NamedIndividual ,
               persona:Person ;
    rdfs:label "Alice Walker by Bob"@en ;

    <https://purl.org/cco/ont00001917> [  # described by → Person Note
        rdf:type cco:ent00000048 ;
        <https://purl.org/cco/ont00001765> "Favorite drink: pepsi"
    ] .
```
