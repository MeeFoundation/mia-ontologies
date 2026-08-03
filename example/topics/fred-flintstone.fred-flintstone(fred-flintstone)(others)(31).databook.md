---
id: https://www.example.org/mia/topics/fred-flintstone.fred-flintstone(fred-flintstone)(others)(31)
title: "About Fred Flintstone in the Others cell as claimed by Fred Flintstone"
type: topic-databook
version: 1.0.0
created: 2026-08-03
description: >
  Fred Flintstone's self-claimed persona, received from Fred's Mia via PDN.
  Records Fred's name and his social network connection to Alice.
mia:
  claimant: ":Fred_Flintstone"
  subject: ":Fred_Flintstone"
graph:
  named_graph: https://www.example.org/mia/topics/fred-flintstone.fred-flintstone(fred-flintstone)(others)(31)#graph
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

This topic captures Fred Flintstone's self-claimed persona, transmitted from Fred's Mia to Alice's Mia over the PDN. It records Fred's name and his social network link to Alice.

## Topic Graph

```turtle
<!-- databook:id: fred-fred-fred-topic-graph -->
<!-- databook:graph: https://www.example.org/mia/topics/fred-flintstone.fred-flintstone(fred-flintstone)(others)(31)#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Fred_Flintstone rdf:type owl:NamedIndividual ,
              persona:Person ;
    rdfs:label "Fred Flintstone"@en ;
    rdfs:comment "Fred Flintstone's self-claimed persona in his 1:1 relationship with Alice."@en ;

    <https://purl.org/cco/ont00001879> [  # designated by → GivenName
        rdf:type cco:ent00000002 ;  # GivenName
        <https://purl.org/cco/ont00001765> "Fred"  # has text value
    ] ;

    <https://purl.org/cco/ont00001879> [  # designated by → FamilyName
        rdf:type cco:ent00000004 ;  # FamilyName
        <https://purl.org/cco/ont00001765> "Flintstone"  # has text value
    ] ;

    persona:hasSocialNetwork :Fred_Fred_Network .


:Fred_Fred_Network rdf:type owl:NamedIndividual ,
                          cco:ont00001183 ;  # Social Network
    rdfs:label "Fred Flintstone's Alice connection"@en ;
    <http://purl.obolibrary.org/obo/BFO_0000115> :Self .  # has member part → Alice
```
