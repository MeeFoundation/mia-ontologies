---
id: https://www.example.org/mia/contexts/paula-walker.self(paula-walker)(acme)(06)
title: "About Paula Walker in the Employee category as claimed by Alice Walker"
type: context-databook
version: 2.0.4
created: 2026-06-14
description: >
  Alice's record of her colleague Paula Walker in the Acme employment context.
  Self-claimed by Alice; describes Paula as an individual.
mia:
  category: "http://www.example.org/mia/categories/paula-walker(acme)"
  claimant: ":Self"
  subject: ":Paula_Walker"
  about-by: "context:OBScontext"
graph:
  named_graph: https://www.example.org/mia/contexts/paula-walker.self(paula-walker)(acme)(06)#graph
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

This context captures Alice's record of her colleague Paula Walker in their shared Acme employment context. Alice self-claims this context; it is paired with Paula's own Acme persona in `20-alice(acme)alice`.

## Identity Data

```turtle
<!-- databook:id: paula-acme-identity -->
<!-- databook:graph: https://www.example.org/mia/contexts/paula-walker.self(paula-walker)(acme)(06)#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Paula_Walker rdf:type owl:NamedIndividual ,
               persona:Person ;
    rdfs:label "Paula Walker (Acme)"@en .
```
