---
id: http://www.example.org/mia/bob(bob)bob
title: "Bob Johnson — Bob context (Bob's view)"
type: context-databook
version: 2.0.2
created: 2026-06-15
description: >
  Bob Johnson's self-asserted Bob-context persona, received from Bob's Mia via PDN.
  Records Bob's name and his social network connection to Alice.
  Dyad partner is Alice's record of Bob in the Bob context.
mia:
  name: "Bob"
  category: "context:People"
  assertedBy: ":Bob_Johnson"
  subject: ":Bob_Johnson"
  about-by: "context:OBO-Context"
  dyad: "http://www.example.org/mia/bob(bob)alice"
graph:
  named_graph: http://www.example.org/mia/bob(bob)bob#graph
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

This context captures Bob Johnson's self-asserted Bob-context persona, transmitted from Bob's Mia to Alice's Mia over the PDN. It records Bob's name and his social network link to Alice. It is paired (dyad) with `05-bob(bob)alice`, Alice's record of Bob in the same context.

## Identity Data

```turtle
<!-- databook:id: bob-bob-bob-identity -->
<!-- databook:graph: http://www.example.org/mia/bob(bob)bob#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Bob_Johnson rdf:type owl:NamedIndividual ,
              persona:Person ;
    rdfs:label "Bob Johnson (Bob)"@en ;
    rdfs:comment "Bob Johnson's self-asserted persona in the 1:1 Bob context."@en ;

    <https://purl.org/cco/ont00001879> [  # designated by → GivenName
        rdf:type cco:ent00000002 ;  # GivenName
        <https://purl.org/cco/ont00001765> "Bob"  # has text value
    ] ;

    <https://purl.org/cco/ont00001879> [  # designated by → FamilyName
        rdf:type cco:ent00000004 ;  # FamilyName
        <https://purl.org/cco/ont00001765> "Johnson"  # has text value
    ] ;

    persona:hasSocialNetwork :Bob_Bob_Network .


:Bob_Bob_Network rdf:type owl:NamedIndividual ,
                          cco:ont00001183 ;  # Social Network
    rdfs:label "Bob Johnson's Bob connection"@en ;
    <http://purl.obolibrary.org/obo/BFO_0000115> :Self .  # has member part → Alice
```
