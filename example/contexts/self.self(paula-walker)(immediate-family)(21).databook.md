---
id: https://www.example.org/mia/contexts/self.self(paula-walker)(immediate-family)(21)
title: "About Alice Walker in the ImmediateFamily cell as claimed by Alice Walker"
type: context-databook
version: 2.0.8
created: 2026-06-01
description: >
  Alice Walker's family context. Records her maternal relationship with Paula Walker
  and her family social network. Self-claimed by Alice.
mia:
  cell: "http://www.example.org/mia/cells/paula-walker(immediate-family)"
  claimant: ":Self"
  subject: ":Self"
  about-by: "context:SBScontext"
graph:
  named_graph: https://www.example.org/mia/contexts/self.self(paula-walker)(immediate-family)(21)#graph
  rdf_version: "1.1"
shapes:
  - http://www.example.org/shapes
process:
  transformer: human
  timestamp: 2026-06-20T00:00:00Z
  agent:
    name: Paul Trevithick
    role: author
---

## Overview

This context captures Alice Walker's family relationships. It records her maternal relationship with Paula Walker and her family social network, which includes Paula Walker as a member. Paula's own family context (`paula-walker.paula-walker(paula-walker)(immediate-family)(05)`) is the peer record in this relationship.

## Identity Data

```turtle
<!-- databook:id: alice-family-identity -->
<!-- databook:graph: https://www.example.org/mia/contexts/self.self(paula-walker)(immediate-family)(21)#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Self rdf:type owl:NamedIndividual ,
               persona:Person ;
    rdfs:label "Alice Walker (Family)"@en ;
    rdfs:comment "Alice Walker's persona in the context of her family relationships."@en ;

    <https://purl.org/cco/ont00001879> [  # designated by → AlternateName
        rdf:type cco:ent00000006 ;  # AlternateName
        <https://purl.org/cco/ont00001765> "Alice Walker"
    ] ;

    cco:ont00001780 :Paula_Walker ;  # has mother

    persona:hasSocialNetwork :Alice_Family_Network .


:Alice_Family_Network rdf:type owl:NamedIndividual ,
                               cco:ont00001183 ;  # Social Network
    rdfs:label "Alice Walker's family connections"@en ;
    <http://purl.obolibrary.org/obo/BFO_0000115> :Paula_Walker .  # has member part
```
