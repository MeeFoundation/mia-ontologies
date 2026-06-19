---
id: http://www.example.org/mia/bob(self)bob
title: "Bob Johnson — Selfness"
type: databook
version: 2.0.2
created: 2026-06-19
description: >
  Bob Johnson's selfness — the central identity individual for Bob in Alice's Mia.
  Received from Bob's Mia via PDN. Records Bob as a person and his social connection
  to Alice.
mia:
  name: "Bob Johnson"
  assertedBy: ":Bob_Johnson"
  subject: ":Bob_Johnson"
graph:
  named_graph: http://www.example.org/mia/bob(self)bob#graph
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

This context captures Bob Johnson's selfness as held in Alice's Mia, transmitted from Bob's Mia over the PDN. It establishes Bob as a `persona:Person` individual and records his social network connection to Alice (`:Self`) via a `hasMember` link.

## Identity Data

<!-- databook:id: bob-self-identity -->
<!-- databook:graph: http://www.example.org/mia/bob(self)bob#graph -->
```turtle
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Bob_Johnson rdf:type owl:NamedIndividual ,
                      persona:Person ;
    rdfs:label "Bob Johnson"@en ;
    rdfs:comment "Bob Johnson's selfness — the central identity individual."@en ;

    <http://purl.obolibrary.org/obo/BFO_0000115> :Self .  # has member part → Alice as asserted by Bob
```
