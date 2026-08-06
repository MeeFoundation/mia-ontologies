---
id: https://www.example.org/mia/topics/self.self(med-app-info)(medical-appointment-info)(30)
title: "About Alice Walker in the Med. App. Info cell as claimed by Alice Walker"
type: topic-databook
version: 1.0.0
created: 2026-08-02
description: >
  Alice Walker's own self-claimed contact info, kept for coordinating Paula's
  medical appointments with Carol — one of this cell's two members, alongside
  Carol (topic 28).
mia:
  claimant: ":Self"
  subject: ":Self"
graph:
  named_graph: https://www.example.org/mia/topics/self.self(med-app-info)(medical-appointment-info)(30)#graph
  rdf_version: "1.1"
shapes:
  - http://mee.foundation/ontologies/persona/shapes
  - http://mee.foundation/ontologies/topic/shapes
process:
  transformer: human
  timestamp: 2026-08-02T00:00:00Z
  agent:
    name: Paul Trevithick
    role: author
---

## Overview

This topic captures Alice Walker's own self-claimed contact info, kept in this cell so Carol can reach her while coordinating Paula's medical appointments. This cell's two members are Alice and Carol (its `c:subject`, `:Paula_Walker`, is a third party the cell is *about*, not one of its members) — this topic and its counterpart (topic 28, Carol's own self-claimed persona) together represent those two members, alongside topic 26 (Alice's claims about Paula's medical appointment).

## Topic Graph

```turtle
<!-- databook:id: alice-self-topic-graph -->
<!-- databook:graph: https://www.example.org/mia/topics/self.self(med-app-info)(medical-appointment-info)(30)#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix cco: <https://purl.org/cco/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Self <https://purl.org/cco/ont00001879> [  # designated by → Phone
        rdf:type cco:ent00000023 ;
        <https://purl.org/cco/ont00001765> "+15108149999"
    ] ;

    <https://purl.org/cco/ont00001917> [  # described by → Person Note
        rdf:type cco:ent00000048 ;
        <https://purl.org/cco/ont00001765> "Best reached by text for scheduling Mom's appointments."
    ] .
```
