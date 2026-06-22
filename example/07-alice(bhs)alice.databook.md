---
id: http://www.example.org/mia/alice(bhs)alice
title: "Alice Walker — Boston Hub Society Profile"
type: databook
version: 2.0.3
created: 2026-06-11
description: >
  Alice Walker's self-asserted BHS profile, including her current address, phone number,
  and email address as shared with the Boston Hub Society group.
mia:
  name: "Boston Hub Society"
  category: "context:Group"
  assertedBy: ":Self"
  subject: ":Self"
  about-by: "context:SBS-Context"
graph:
  named_graph: http://www.example.org/mia/alice(bhs)alice#graph
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

This context captures Alice Walker's BHS profile — the identity data she shares with the Boston Hub Society group. It includes her current Paradise, CA address, her phone number, and her Gmail address.

## Identity Data

```turtle
<!-- databook:id: alice-bhs-identity -->
<!-- databook:graph: http://www.example.org/mia/alice(bhs)alice#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Self rdf:type owl:NamedIndividual ,
               persona:Person ;
    rdfs:label "Alice Walker (BHS)"@en ;
    rdfs:comment "Alice Walker's persona in the context of her BHS group (aka her BHS profile)."@en ;

    <https://purl.org/cco/ont00001879> [  # designated by → AlternateName
        rdf:type cco:ent00000006 ;  # AlternateName
        <https://purl.org/cco/ont00001765> "Alice Walker"
    ] ;

    <https://purl.org/cco/ont00001879> :Address_BHS ;  # designated by → current address

    <https://purl.org/cco/ont00001879> [  # designated by → Phone
        rdf:type cco:ent00000023 ;
        <https://purl.org/cco/ont00001765> "+15108149999"
    ] ;

    <https://purl.org/cco/ont00001879> [  # designated by → Email
        rdf:type cco:ent00000024 ;
        <https://purl.org/cco/ont00001765> "awalker@gmail.com"
    ] .


:Address_BHS rdf:type owl:NamedIndividual ,
                      cco:ent00000010 ;  # USPostalAddress
    rdfs:label "Alice Walker's BHS Address"@en ;
    <http://purl.obolibrary.org/obo/BFO_0000178> [  # has continuant part → Street
        rdf:type cco:ent00000011 ;
        <https://purl.org/cco/ont00001765> "123 Sleepy Hollow"
    ] ;
    <http://purl.obolibrary.org/obo/BFO_0000178> [  # has continuant part → City
        rdf:type cco:ent00000012 ;
        <https://purl.org/cco/ont00001765> "Paradise"
    ] ;
    <http://purl.obolibrary.org/obo/BFO_0000178> [  # has continuant part → State
        rdf:type cco:ent00000013 ;
        <https://purl.org/cco/ont00001765> "CA"
    ] ;
    <http://purl.obolibrary.org/obo/BFO_0000178> [  # has continuant part → ZIP
        rdf:type cco:ent00000015 ;
        <https://purl.org/cco/ont00001765> "95969"
    ] ;
    <http://purl.obolibrary.org/obo/BFO_0000178> [  # has continuant part → Country
        rdf:type cco:ent00000014 ;
        <https://purl.org/cco/ont00001765> "USA"
    ] .
```
