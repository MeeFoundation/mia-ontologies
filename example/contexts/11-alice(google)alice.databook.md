---
id: http://www.example.org/mia/alice(google)alice
title: "About Alice Walker in the Companies context as asserted by Alice Walker"
type: context-databook
version: 2.0.2
created: 2026-06-01
description: >
  Alice Walker's Google context. Records her Gmail address as self-entered data
  about her Google account relationship.
mia:
  category: "http://www.example.org/mia/categories/companies"
  assertedBy: ":Self"
  subject: ":Self"
  about-by: "context:SBS-Context"
graph:
  named_graph: http://www.example.org/mia/alice(google)alice#graph
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

This context captures Alice Walker's Google account context. Alice self-enters her Gmail address (awalker@gmail.com). Google is not a PDN node, so Alice records this data herself rather than receiving it from Google.

## Identity Data

```turtle
<!-- databook:id: alice-google-identity -->
<!-- databook:graph: http://www.example.org/mia/alice(google)alice#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Self rdf:type owl:NamedIndividual ,
               persona:Person ;
    rdfs:label "Alice Walker (Google)"@en ;

    <https://purl.org/cco/ont00001879> [  # designated by → Email
        rdf:type cco:ent00000024 ;
        <https://purl.org/cco/ont00001765> "awalker@gmail.com"
    ] .
```
