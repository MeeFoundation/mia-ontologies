---
id: http://www.example.org/mia/bob(bhs)bob
title: "Bob Johnson — BHS Profile"
type: databook
version: 2.0.1
created: 2026-06-15
description: >
  Bob Johnson's BHS profile, received from Bob's Mia via PDN.
  Records Bob's name as he presents himself to the Boston Hub Society.
mia:
  name: "Boston Hub Society"
  category: "context:Group"
  assertedBy: ":Bob_Johnson"
  subject: ":Bob_Johnson"
graph:
  named_graph: http://www.example.org/mia/bob(bhs)bob#graph
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

This context captures Bob Johnson's BHS profile as transmitted from Bob's Mia to Alice's Mia over the PDN. It records the name Bob presents to the Boston Hub Society group.

## Identity Data

```turtle
<!-- databook:id: bob-bhs-identity -->
<!-- databook:graph: http://www.example.org/mia/bob(bhs)bob#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Bob_Johnson rdf:type owl:NamedIndividual ,
              persona:Person ;
    rdfs:label "Bob Johnson (BHS)"@en ;

    <https://purl.org/cco/ont00001879> [  # designated by → GivenName
        rdf:type cco:ent00000002 ;
        <https://purl.org/cco/ont00001765> "Bob"
    ] ;

    <https://purl.org/cco/ont00001879> [  # designated by → FamilyName
        rdf:type cco:ent00000004 ;
        <https://purl.org/cco/ont00001765> "Johnson"
    ] .
```
