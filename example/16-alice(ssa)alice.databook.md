---
id: http://www.example.org/mia/alice(ssa)alice
title: "Alice Walker — Social Security Administration"
type: context-databook
version: 2.0.2
created: 2026-06-01
description: >
  Alice Walker's SSA context. Records her Social Security Number as self-entered data.
  The SSA is not a PDN node, so Alice self-enters this from her physical SSA card.
mia:
  name: "Social Security Administration"
  category: "context:Federal"
  assertedBy: ":Self"
  subject: ":Self"
  about-by: "context:SBS-Context"
graph:
  named_graph: http://www.example.org/mia/alice(ssa)alice#graph
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

This context captures Alice Walker's Social Security Administration record. Alice self-enters her SSN (123-45-6788) from her physical Social Security card. The SSA is not a PDN node, so this data is self-asserted rather than received from the SSA directly.

## Identity Data

```turtle
<!-- databook:id: alice-ssa-identity -->
<!-- databook:graph: http://www.example.org/mia/alice(ssa)alice#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Self rdf:type owl:NamedIndividual ,
               persona:Person ;
    rdfs:label "Alice Walker (SSA)"@en ;
    rdfs:comment "Alice Walker's persona in the context of her Social Security Administration record."@en ;

    <https://purl.org/cco/ont00001879> [  # designated by → SSN
        rdf:type cco:ent00000008 ;
        <https://purl.org/cco/ont00001765> "123-45-6788"
    ] .
```
