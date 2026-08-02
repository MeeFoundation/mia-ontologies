---
id: https://www.example.org/mia/topics/self.bob-johnson(bob-johnson)(others)(08)
title: "About Alice Walker in the Others cell as claimed by Bob Johnson"
type: topic-databook
version: 2.0.14
created: 2026-06-13
description: >
  Claims Bob makes about Alice.
mia:
  claimant: ":Bob_Johnson"
  subject: ":Self"
graph:
  named_graph: https://www.example.org/mia/topics/self.bob-johnson(bob-johnson)(others)(08)#graph
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

This topic captures Bob's record of Alice in their 1:1 relationship topic, transmitted from Bob's Mia to Alice's Mia over the PDN. Bob notes Alice's favorite drink.

## Topic Graph

```turtle
<!-- databook:id: alice-bob-bob-topic-graph -->
<!-- databook:graph: https://www.example.org/mia/topics/self.bob-johnson(bob-johnson)(others)(08)#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Self <https://purl.org/cco/ont00001917> [  # described by → Person Note
        rdf:type cco:ent00000048 ;
        <https://purl.org/cco/ont00001765> "Favorite drink: pepsi"
    ] .
```
