---
id: http://www.example.org/mia/paula-walker.paula-walker(paula-walker)(05)
title: "About Paula Walker in the Family context as asserted by Paula Walker"
type: context-databook
version: 2.0.3
created: 2026-06-14
description: >
  Paula Walker's self-asserted family persona, received from Paula's Mia via PDN.
mia:
  category: "http://www.example.org/mia/categories/family"
  assertedBy: ":Paula_Walker"
  subject: ":Paula_Walker"
  about-by: "context:OBO-Context"
graph:
  named_graph: http://www.example.org/mia/paula-walker.paula-walker(paula-walker)(05)#graph
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

This context captures Paula Walker's self-asserted family persona as transmitted from Paula's Mia to Alice's Mia over the PDN.

## Identity Data

```turtle
<!-- databook:id: paula-family-paula-identity -->
<!-- databook:graph: http://www.example.org/mia/paula-walker.paula-walker(paula-walker)(05)#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Paula_Walker rdf:type owl:NamedIndividual ,
               persona:Person ;
    rdfs:label "Paula Walker (Family) self-asserted"@en .
```
