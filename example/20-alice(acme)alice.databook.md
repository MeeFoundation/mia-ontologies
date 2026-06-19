---
id: http://www.example.org/mia/alice(acme)alice
title: "Alice Walker — Acme"
type: databook
version: 2.0.2
created: 2026-06-12
description: >
  Alice Walker's Acme employment context. Records her work email address and her
  Acme social network connection to colleague Paula Walker. Self-asserted by Alice.
mia:
  name: "Acme"
  contextCategory: "context:Employee"
  assertedBy: ":Self"
  subject: ":Self"
graph:
  named_graph: http://www.example.org/mia/alice(acme)alice#graph
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

This context captures Alice Walker's employee identity at Acme. It records her work email address (alice@acme.com) and her Acme social network, which includes colleague Paula Walker. Alice's business card context (`21-alice(business-card)alice`) derives professional contact details from this context.

## Identity Data

```turtle
<!-- databook:id: alice-acme-identity -->
<!-- databook:graph: http://www.example.org/mia/alice(acme)alice#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Self rdf:type owl:NamedIndividual ,
               persona:Person ;
    rdfs:label "Alice Walker (Acme)"@en ;
    rdfs:comment "Alice Walker's persona in the context of her employment at Acme."@en ;

    <https://purl.org/cco/ont00001879> [  # designated by → Email
        rdf:type cco:ent00000024 ;  # Email
        <https://purl.org/cco/ont00001765> "alice@acme.com"  # has text value
    ] ;

    persona:hasSocialNetwork :Alice_Acme_Network .


:Alice_Acme_Network rdf:type owl:NamedIndividual ,
                             cco:ont00001183 ;  # Social Network
    rdfs:label "Alice Walker's Acme connections"@en ;
    <http://purl.obolibrary.org/obo/BFO_0000115> :Paula_Walker .  # has member part
```
