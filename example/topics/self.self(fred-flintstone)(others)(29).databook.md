---
id: https://www.example.org/mia/topics/self.self(fred-flintstone)(others)(29)
title: "About Alice Walker in the Others cell as claimed by Alice Walker"
type: topic-databook
version: 1.0.0
created: 2026-08-03
description: >
  Alice Walker's self-claimed persona for her 1:1 relationship with Fred Flintstone.
  Records the name and social network connection she shares with Fred.
mia:
  claimant: ":Self"
  subject: ":Self"
graph:
  named_graph: https://www.example.org/mia/topics/self.self(fred-flintstone)(others)(29)#graph
  rdf_version: "1.1"
shapes:
  - http://mee.foundation/ontologies/persona/shapes
  - http://mee.foundation/ontologies/topic/shapes
process:
  transformer: human
  timestamp: 2026-08-03T00:00:00Z
  agent:
    name: Paul Trevithick
    role: author
---

## Overview

This topic captures Alice Walker's self-claimed persona in her 1:1 relationship with Fred Flintstone. It records the name Alice presents to Fred and her social network link to him.

## Topic Graph

```turtle
<!-- databook:id: alice-fred-alice-topic-graph -->
<!-- databook:graph: https://www.example.org/mia/topics/self.self(fred-flintstone)(others)(29)#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Self rdfs:comment "Alice Walker's persona for her 1:1 relationship with Fred."@en ;

    <https://purl.org/cco/ont00001879> [  # designated by → AlternateName
        rdf:type cco:ent00000006 ;  # AlternateName
        <https://purl.org/cco/ont00001765> "Alice Walker"
    ] ;

    <https://purl.org/cco/ont00001879> [  # designated by → GivenName
        rdf:type cco:ent00000002 ;  # GivenName
        <https://purl.org/cco/ont00001765> "Alice"  # has text value
    ] ;

    <https://purl.org/cco/ont00001879> [  # designated by → FamilyName
        rdf:type cco:ent00000004 ;  # FamilyName
        <https://purl.org/cco/ont00001765> "Walker"  # has text value
    ] ;

    persona:hasSocialNetwork :Alice_Fred_Network .


:Alice_Fred_Network rdf:type owl:NamedIndividual ,
                             cco:ont00001183 ;  # Social Network
    rdfs:label "Alice Walker's Fred connection"@en ;
    <http://purl.obolibrary.org/obo/BFO_0000115> :Fred_Flintstone .  # has member part
```
