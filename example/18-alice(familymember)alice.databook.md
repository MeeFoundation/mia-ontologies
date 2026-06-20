---
id: http://www.example.org/mia/alice(family)alice
title: "Alice Walker — Family"
type: databook
version: 2.0.3
created: 2026-06-01
description: >
  Alice Walker's family context. Records her family social network, with Paula Walker
  as a member. Self-asserted by Alice.
mia:
  name: "Family"
  contextCategory: "context:FamilyMember"
  assertedBy: ":Self"
  subject: ":Self"
graph:
  named_graph: http://www.example.org/mia/alice(family)alice#graph
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

This context captures Alice Walker's family relationships. It records her family social network, which includes Paula Walker as a member. Paula's own family context (`02-paula(family)alice`) is the peer record in this relationship.

## Identity Data

```turtle
<!-- databook:id: alice-family-identity -->
<!-- databook:graph: http://www.example.org/mia/alice(family)alice#graph -->
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

    persona:hasSocialNetwork :Alice_Family_Network .


:Alice_Family_Network rdf:type owl:NamedIndividual ,
                               cco:ont00001183 ;  # Social Network
    rdfs:label "Alice Walker's family connections"@en ;
    <http://purl.obolibrary.org/obo/BFO_0000115> :Paula_Walker .  # has member part
```
