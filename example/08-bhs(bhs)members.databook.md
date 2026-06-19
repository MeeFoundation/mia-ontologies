---
id: http://www.example.org/mia/bhs(bhs)members
title: "Boston Hub Society — Group"
type: databook
version: 2.0.2
created: 2026-06-12
description: >
  The Boston Hub Society group instance, with Alice and Bob as members.
  A g:Group context assertable by any permitted member.
mia:
  name: "Boston Hub Society"
  contextCategory: "context:Group"
  assertedBy: "identity:Self"
  subject: "identity:Group"
graph:
  named_graph: http://www.example.org/mia/bhs(bhs)members#graph
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

This context captures the Boston Hub Society as a `g:Group` entity. It records the group's membership: Alice Walker (`:Self`) and Bob Johnson (`:Bob_Johnson`). Any permitted member may assert or update this context.

## Identity Data

```turtle
<!-- databook:id: bhs-group-identity -->
<!-- databook:graph: http://www.example.org/mia/bhs(bhs)members#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix g: <http://mee.foundation/ontologies/group#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:BHS_Group rdf:type owl:NamedIndividual ,
                    g:Group ;
    rdfs:label "Boston Hub Society"@en ;
    rdfs:comment "The Boston Hub Society group instance."@en ;
    <http://purl.obolibrary.org/obo/BFO_0000115> :Self ;        # has member part → Alice
    <http://purl.obolibrary.org/obo/BFO_0000115> :Bob_Johnson . # has member part → Bob
```
