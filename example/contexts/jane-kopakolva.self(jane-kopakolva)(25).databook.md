---
id: https://www.example.org/mia/contexts/jane-kopakolva.self(jane-kopakolva)(25)
title: "About Jane Kopakolva in the PrimaryCarePhysician cell as claimed by Alice Walker"
type: context-databook
version: 1.0.4
created: 2026-07-08
description: >
  Alice's record of Dr. Jane Kopakolva, the primary care physician for
  Alice's mother, Paula Walker.
mia:
  claimant: ":Self"
  subject: ":Jane_Kopakolva"
  about-by: "context:OBScontext"
graph:
  named_graph: https://www.example.org/mia/contexts/jane-kopakolva.self(jane-kopakolva)(25)#graph
  rdf_version: "1.1"
shapes:
  - http://www.example.org/shapes
process:
  transformer: human
  timestamp: 2026-07-08T00:00:00Z
  agent:
    name: Paul Trevithick
    role: author
---

## Overview

This context captures Alice's record of Dr. Jane Kopakolva, who is the primary care physician for Alice's mother, Paula Walker. Alice keeps this information so she and her sister Carol can coordinate Paula's medical appointments.

## Identity Data

```turtle
<!-- databook:id: jane-kopakolva-alice-identity -->
<!-- databook:graph: https://www.example.org/mia/contexts/jane-kopakolva.self(jane-kopakolva)(25)#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Jane_Kopakolva rdf:type owl:NamedIndividual ,
               persona:Person ;
    rdfs:label "Jane Kopakolva (Primary Care Physician)"@en ;

    <https://purl.org/cco/ont00001879> [  # designated by → GivenName
        rdf:type cco:ent00000002 ;  # GivenName
        <https://purl.org/cco/ont00001765> "Jane"  # has text value
    ] ;

    <https://purl.org/cco/ont00001879> [  # designated by → FamilyName
        rdf:type cco:ent00000004 ;  # FamilyName
        <https://purl.org/cco/ont00001765> "Kopakolva"  # has text value
    ] ;

    <https://purl.org/cco/ont00001917> [  # described by → Person Note
        rdf:type cco:ent00000048 ;
        <https://purl.org/cco/ont00001765> "Paula Walker's primary care physician"
    ] .
```
