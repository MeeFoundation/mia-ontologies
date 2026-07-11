---
id: https://www.example.org/mia/contexts/paula-walker.paula-walker(paula-walker)(immediate-family)(05)
title: "About Paula Walker in the ImmediateFamily cell as claimed by Paula Walker"
type: context-databook
version: 2.0.8
created: 2026-06-14
description: >
  Paula Walker's self-claimed family persona, received from Paula's Mia via PDN.
mia:
  claimant: ":Paula_Walker"
  subject: ":Paula_Walker"
  about-by: "context:OBOcontext"
graph:
  named_graph: https://www.example.org/mia/contexts/paula-walker.paula-walker(paula-walker)(immediate-family)(05)#graph
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

This context captures Paula Walker's self-claimed family persona as transmitted from Paula's Mia to Alice's Mia over the PDN.

## Identity Data

```turtle
<!-- databook:id: paula-family-paula-identity -->
<!-- databook:graph: https://www.example.org/mia/contexts/paula-walker.paula-walker(paula-walker)(immediate-family)(05)#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Paula_Walker rdf:type owl:NamedIndividual ,
               persona:Person ;
    rdfs:label "Paula Walker (Family) self-claimed"@en .
```
