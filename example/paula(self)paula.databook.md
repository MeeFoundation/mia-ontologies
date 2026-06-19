---
id: http://www.example.org/mia/paula(self)paula
title: "Paula Walker — Selfness"
type: databook
version: 2.0.1
created: 2026-06-19
description: >
  Paula Walker's selfness — the central identity individual for Paula in Alice's Mia.
  Received from Paula's Mia via PDN. Establishes Paula as a person; Alice is her daughter.
mia:
  name: "Paula Walker"
  assertedBy: ":Paula_Walker"
  subject: ":Paula_Walker"
graph:
  named_graph: http://www.example.org/mia/paula(self)paula#graph
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

This context captures Paula Walker's selfness as held in Alice's Mia, transmitted from Paula's Mia over the PDN. It establishes Paula as a `persona:Person` individual. Paula's named and relationship context files (`01-paula(acme)alice`, `02-paula(familymember)alice`, `03-paula(familymember)paula`) hold her identity data.

## Identity Data

```turtle
<!-- databook:id: paula-self-identity -->
<!-- databook:graph: http://www.example.org/mia/paula(self)paula#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Paula_Walker rdf:type owl:NamedIndividual ,
                       persona:Person ;
    rdfs:label "Paula Walker"@en ;
    rdfs:comment "Paula Walker's selfness — the central identity individual."@en .
```
