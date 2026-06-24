---
id: http://www.example.org/mia/self.self(companies)(12)
title: "About Alice Walker in the Companies context as asserted by Alice Walker"
type: context-databook
version: 2.0.2
created: 2026-06-01
description: >
  Alice Walker's AT&T context. Records her mobile phone number as self-entered data
  about her AT&T account relationship.
mia:
  category: "http://www.example.org/mia/categories/companies"
  assertedBy: ":Self"
  subject: ":Self"
  about-by: "context:SBS-Context"
graph:
  named_graph: http://www.example.org/mia/self.self(companies)(12)#graph
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

This context captures Alice Walker's AT&T account context. Alice self-enters her mobile phone number (+15108149999, E.164 format). AT&T is not a PDN node, so Alice records this data herself rather than receiving it from AT&T.

## Identity Data

```turtle
<!-- databook:id: alice-att-identity -->
<!-- databook:graph: http://www.example.org/mia/self.self(companies)(12)#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Self rdf:type owl:NamedIndividual ,
               persona:Person ;
    rdfs:label "Alice Walker (AT&T)"@en ;

    <https://purl.org/cco/ont00001879> [  # designated by → Phone
        rdf:type cco:ent00000023 ;
        <https://purl.org/cco/ont00001765> "+15108149999" ;
        rdfs:comment "E.164 format (international standard)"@en
    ] .
```
