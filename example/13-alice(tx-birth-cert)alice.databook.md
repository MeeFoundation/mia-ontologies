---
id: http://www.example.org/mia/alice(tx-birth-cert)alice
title: "Alice Walker — Texas Birth Certificate"
type: databook
version: 2.0.2
created: 2026-06-01
description: >
  Alice Walker's Texas birth certificate context. Records her legal name (Margery Alice Walker)
  and maiden name (Margery Alice Arnold) as self-entered data.
mia:
  name: "Texas Birth Certificate"
  category: "context:State"
  assertedBy: ":Self"
  subject: ":Self"
  about-by: "context:SBS-Context"
  template: "persona:BirthCertificate"
graph:
  named_graph: http://www.example.org/mia/alice(tx-birth-cert)alice#graph
  rdf_version: "1.1"
shapes:
  - http://www.example.org/shapes
  - http://www.example.org/shapes/birthcertificate
process:
  transformer: human
  timestamp: 2026-06-19T00:00:00Z
  agent:
    name: Paul Trevithick
    role: author
---

## Overview

This context captures Alice Walker's Texas birth certificate identity data. Alice self-enters her legal name (Margery Alice Walker) and maiden name (Margery Alice Arnold) from her physical birth certificate. Validated by the `BirthCertificate` per-template SHACL shapes.

## Identity Data

```turtle
<!-- databook:id: alice-tx-birth-cert-identity -->
<!-- databook:graph: http://www.example.org/mia/alice(tx-birth-cert)alice#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Self rdf:type owl:NamedIndividual ,
               persona:Person ;
    rdfs:label "Alice Walker (Texas Birth Certificate)"@en ;

    <https://purl.org/cco/ont00001879> [  # designated by → GivenName (legal first name)
        rdf:type cco:ent00000002 ;  # GivenName
        <https://purl.org/cco/ont00001765> "Margery"  # has text value
    ] ;

    <https://purl.org/cco/ont00001879> [  # designated by → AdditionalName (middle name)
        rdf:type cco:ent00000003 ;  # AdditionalName
        <https://purl.org/cco/ont00001765> "Alice"  # has text value
    ] ;

    <https://purl.org/cco/ont00001879> [  # designated by → FamilyName
        rdf:type cco:ent00000004 ;  # FamilyName
        <https://purl.org/cco/ont00001765> "Walker"  # has text value
    ] ;

    <https://purl.org/cco/ont00001879> [  # designated by → AlternateName (maiden name)
        rdf:type cco:ent00000006 ;  # AlternateName
        <https://purl.org/cco/ont00001765> "Margery Alice Arnold" ;  # has text value
        rdfs:comment "Maiden name (former legal name before marriage)"@en
    ] .
```
