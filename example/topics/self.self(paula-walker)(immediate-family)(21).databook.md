---
id: https://www.example.org/mia/topics/self.self(paula-walker)(immediate-family)(21)
title: "About Alice Walker in the ImmediateFamily cell as claimed by Alice Walker"
type: topic-databook
version: 2.0.18
created: 2026-06-01
description: >
  Alice Walker's family topic. Records her maternal relationship with Paula Walker
  and her family social network. Self-claimed by Alice.
mia:
  claimant: ":Self"
  subject: ":Self"
graph:
  named_graph: https://www.example.org/mia/topics/self.self(paula-walker)(immediate-family)(21)#graph
  rdf_version: "1.1"
shapes:
  - http://mee.foundation/ontologies/persona/shapes
  - http://mee.foundation/ontologies/topic/shapes
process:
  transformer: human
  timestamp: 2026-06-20T00:00:00Z
  agent:
    name: Paul Trevithick
    role: author
---

## Overview

This topic captures Alice Walker's family relationships. It records her maternal relationship with Paula Walker and her family social network, which includes Paula Walker and Carol Walker (Alice's sister) as members. Paula's own family topic (`paula-walker.paula-walker(paula-walker)(immediate-family)(05)`) is the peer record in this relationship; Carol's own claimed record about their mother appears separately in the "Med. App. Info" cell (topic 28).

## Topic Graph

```turtle
<!-- databook:id: alice-family-topic-graph -->
<!-- databook:graph: https://www.example.org/mia/topics/self.self(paula-walker)(immediate-family)(21)#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Self rdfs:comment "Alice Walker's persona for her family relationships."@en ;

    <https://purl.org/cco/ont00001879> [  # designated by → AlternateName
        rdf:type cco:ent00000006 ;  # AlternateName
        <https://purl.org/cco/ont00001765> "Alice Walker"
    ] ;

    cco:ont00001780 :Paula_Walker ;  # has mother

    persona:hasSocialNetwork :Alice_Family_Network .


:Alice_Family_Network rdf:type owl:NamedIndividual ,
                               cco:ont00001183 ;  # Social Network
    rdfs:label "Alice Walker's family connections"@en ;
    <http://purl.obolibrary.org/obo/BFO_0000115> :Paula_Walker ,  # has member part
                                                  :Carol_Walker .  # has member part (Alice's sister)
```
