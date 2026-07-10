---
id: https://www.example.org/mia/contexts/self.self(bob-johnson)(others)(12)
title: "About Alice Walker in the Others cell as claimed by Alice Walker"
type: context-databook
version: 2.0.7
created: 2026-06-12
description: >
  Alice Walker's self-claimed persona in the context of her 1:1 relationship with Bob Johnson.
  Records the name and social network connection she shares with Bob.
mia:
  cell: "http://www.example.org/mia/cells/bob-johnson(others)"
  claimant: ":Self"
  subject: ":Self"
  about-by: "context:SBScontext"
graph:
  named_graph: https://www.example.org/mia/contexts/self.self(bob-johnson)(others)(12)#graph
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

This context captures Alice Walker's self-claimed persona in her 1:1 relationship with Bob Johnson. It records the name Alice presents to Bob and her social network link to him.

## Identity Data

```turtle
<!-- databook:id: alice-bob-alice-identity -->
<!-- databook:graph: https://www.example.org/mia/contexts/self.self(bob-johnson)(others)(12)#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Self rdf:type owl:NamedIndividual ,
               persona:Person ;
    rdfs:label "Alice Walker (Bob)"@en ;
    rdfs:comment "Alice Walker's persona in the context of her 1:1 relationship with Bob."@en ;

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

    persona:hasSocialNetwork :Alice_Bob_Network .


:Alice_Bob_Network rdf:type owl:NamedIndividual ,
                             cco:ont00001183 ;  # Social Network
    rdfs:label "Alice Walker's Bob connection"@en ;
    <http://purl.obolibrary.org/obo/BFO_0000115> :Bob_Johnson .  # has member part
```
