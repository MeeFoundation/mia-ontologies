---
id: http://www.example.org/mia/alice(driverslicense)alice
title: "About Alice Walker in the State context as asserted by Alice Walker"
type: context-databook
version: 2.0.3
created: 2026-06-15
description: >
  Alice Walker's California driver's license context. Records her legal name, date of birth,
  license number, expiration date, issuing jurisdiction, and photo. Self-asserted by Alice.
mia:
  category: "http://www.example.org/mia/categories/state"
  assertedBy: ":Self"
  subject: ":Self"
  about-by: "context:SBS-Context"
  template: "persona:DriversLicense"
graph:
  named_graph: http://www.example.org/mia/alice(driverslicense)alice#graph
  rdf_version: "1.1"
shapes:
  - http://www.example.org/shapes
  - http://www.example.org/shapes/driverslicense
process:
  transformer: human
  timestamp: 2026-06-19T00:00:00Z
  agent:
    name: Paul Trevithick
    role: author
---

## Overview

This context captures Alice Walker's California driver's license identity data. Alice self-enters her legal name (Margery Alice Walker), date of birth (1985-07-04), California license number (A1234567), expiration date (2031-07-04), issuing jurisdiction (CA), and a photo. Validated by the `DriversLicense` per-template SHACL shapes.

## Identity Data

```turtle
<!-- databook:id: alice-driverslicense-identity -->
<!-- databook:graph: http://www.example.org/mia/alice(driverslicense)alice#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

:Self rdf:type owl:NamedIndividual ,
               persona:Person ;
    rdfs:label "Alice Walker (Driver's License)"@en ;
    rdfs:comment "Alice Walker's California state-issued driver's licence identity data."@en ;

    # ── Legal name (matches Texas Birth Certificate) ─────────────────────────

    <https://purl.org/cco/ont00001879> [  # designated by → GivenName (legal first name)
        rdf:type cco:ent00000002 ;  # GivenName
        <https://purl.org/cco/ont00001765> "Margery"
    ] ;

    <https://purl.org/cco/ont00001879> [  # designated by → AdditionalName (middle name)
        rdf:type cco:ent00000003 ;  # AdditionalName
        <https://purl.org/cco/ont00001765> "Alice"
    ] ;

    <https://purl.org/cco/ont00001879> [  # designated by → FamilyName
        rdf:type cco:ent00000004 ;  # FamilyName
        <https://purl.org/cco/ont00001765> "Walker"
    ] ;

    # ── Dates ────────────────────────────────────────────────────────────────

    <https://purl.org/cco/ont00001879> [  # designated by → Birthdate
        rdf:type cco:ent00000046 ;  # Birthdate
        <https://purl.org/cco/ont00001765> "1985-07-04"
    ] ;

    <https://purl.org/cco/ont00001879> [  # designated by → ExpirationDateIdentifier
        rdf:type cco:ent00000054 ;  # ExpirationDateIdentifier
        <https://purl.org/cco/ont00001765> "2031-07-04"
    ] ;

    # ── License number ───────────────────────────────────────────────────────

    <https://purl.org/cco/ont00001879> [  # designated by → DriversLicenseNumber
        rdf:type persona:DriversLicenseNumber ;
        <https://purl.org/cco/ont00001765> "A1234567"  # placeholder California DL number
    ] ;

    # ── Issuing jurisdiction ─────────────────────────────────────────────────

    <https://purl.org/cco/ont00001879> [  # designated by → IssuingJurisdiction
        rdf:type persona:IssuingJurisdiction ;
        <https://purl.org/cco/ont00001765> "CA"
    ] ;

    # ── Photo ────────────────────────────────────────────────────────────────

    persona:hasPhoto "https://example.org/alice-dl-photo.jpg"^^xsd:anyURI ;

    persona:hasIdentityDocument :Alice_CA_DriversLicense .

:Alice_CA_DriversLicense rdf:type owl:NamedIndividual ,
                                   persona:DriversLicense ;
    rdfs:label "Alice Walker's California Driver's License"@en .
```
