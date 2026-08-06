---
id: https://www.example.org/mia/topics/carol-walker.carol-walker(med-app-info)(medical-appointment-info)(28)
title: "About Carol Walker in the Med. App. Info cell as claimed by Carol Walker"
type: topic-databook
version: 1.0.0
created: 2026-08-02
description: >
  Carol Walker's own self-claimed persona and contact info, synced to Alice's Mia
  over the PDN — one of this cell's two members, alongside Alice (topic 30).
mia:
  claimant: ":Carol_Walker"
  subject: ":Carol_Walker"
graph:
  named_graph: https://www.example.org/mia/topics/carol-walker.carol-walker(med-app-info)(medical-appointment-info)(28)#graph
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

This topic captures Carol Walker's own self-claimed persona and contact info, shared directly from her own Mia to Alice's over the PDN. This cell's two members are Alice and Carol (its `c:subject`, `:Paula_Walker`, is a third party the cell is *about*, not one of its members) — this topic and its counterpart (topic 30, Alice's own self-claimed contact info) together represent those two members, alongside topic 26 (Alice's claims about Paula's medical appointment).

## Topic Graph

```turtle
<!-- databook:id: carol-self-topic-graph -->
<!-- databook:graph: https://www.example.org/mia/topics/carol-walker.carol-walker(med-app-info)(medical-appointment-info)(28)#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Carol_Walker rdf:type owl:NamedIndividual ,
               persona:Person ;
    rdfs:label "Carol Walker"@en ;

    <https://purl.org/cco/ont00001879> [  # designated by → GivenName
        rdf:type cco:ent00000002 ;  # GivenName
        <https://purl.org/cco/ont00001765> "Carol"
    ] ;

    <https://purl.org/cco/ont00001879> [  # designated by → FamilyName
        rdf:type cco:ent00000004 ;  # FamilyName
        <https://purl.org/cco/ont00001765> "Walker"
    ] ;

    <https://purl.org/cco/ont00001879> [  # designated by → Phone
        rdf:type cco:ent00000023 ;
        <https://purl.org/cco/ont00001765> "+19165550198"
    ] ;

    <https://purl.org/cco/ont00001917> [  # described by → Person Note
        rdf:type cco:ent00000048 ;
        <https://purl.org/cco/ont00001765> "Usually available weekday evenings and weekends for Mom's appointments."
    ] .
```
