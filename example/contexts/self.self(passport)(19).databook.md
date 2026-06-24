---
id: http://www.example.org/mia/self.self(passport)(19)
title: "About Alice Walker in the Federal context as asserted by Alice Walker"
type: context-databook
version: 1.0.2
created: 2026-06-20
description: >
  Alice Walker's US passport context. Records her legal name, date of birth, passport number,
  issue and expiration dates, issuing country, place of birth, gender marker, and photo.
  Self-asserted by Alice.
mia:
  category: "http://www.example.org/mia/categories/federal"
  assertedBy: ":Self"
  subject: ":Self"
  about-by: "context:SBS-Context"
  template: "persona:Passport"
graph:
  named_graph: http://www.example.org/mia/self.self(passport)(19)#graph
  rdf_version: "1.1"
shapes:
  - http://www.example.org/shapes
  - http://www.example.org/shapes/passport
process:
  transformer: human
  timestamp: 2026-06-20T00:00:00Z
  agent:
    name: Paul Trevithick
    role: author
---

## Overview

This context captures Alice Walker's US passport identity data. Alice self-enters her legal name (Margery Alice Walker), date of birth (1985-07-04), US passport number (123456789), issue date (2021-07-04), expiration date (2031-07-04), place of birth (Austin, Texas, USA), gender marker (F), and a photo. Validated by the `Passport` per-template SHACL shapes.

## Identity Data

```turtle
<!-- databook:id: alice-passport-identity -->
<!-- databook:graph: http://www.example.org/mia/self.self(passport)(19)#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

:Self rdf:type owl:NamedIndividual ,
               persona:Person ;
    rdfs:label "Alice Walker (Passport)"@en ;
    persona:hasIdentityDocument :Alice_US_Passport .

:Alice_US_Passport rdf:type owl:NamedIndividual ,
                             persona:Passport ;
    rdfs:label "Alice Walker's US Passport"@en ;
    rdfs:comment "Alice Walker's US passport identity data."@en ;

    # ── Legal name (matches Texas Birth Certificate and Driver's License) ────

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

    <https://purl.org/cco/ont00001879> [  # designated by → IssueDate
        rdf:type persona:IssueDate ;
        <https://purl.org/cco/ont00001765> "2021-07-04"
    ] ;

    <https://purl.org/cco/ont00001879> [  # designated by → ExpirationDateIdentifier
        rdf:type cco:ent00000054 ;  # ExpirationDateIdentifier
        <https://purl.org/cco/ont00001765> "2031-07-04"
    ] ;

    # ── Passport number ──────────────────────────────────────────────────────

    <https://purl.org/cco/ont00001879> [  # designated by → PassportNumber
        rdf:type persona:PassportNumber ;
        <https://purl.org/cco/ont00001765> "123456789"  # placeholder US passport number
    ] ;

    # ── Issuing country ──────────────────────────────────────────────────────

    <https://purl.org/cco/ont00001879> [  # designated by → IssuingCountry
        rdf:type persona:IssuingCountry ;
        <https://purl.org/cco/ont00001765> "USA"
    ] ;

    # ── Place of birth ───────────────────────────────────────────────────────

    <https://purl.org/cco/ont00001879> [  # designated by → PlaceOfBirth
        rdf:type persona:PlaceOfBirth ;
        <https://purl.org/cco/ont00001765> "Austin, Texas, USA"
    ] ;

    # ── Gender marker ────────────────────────────────────────────────────────

    <https://purl.org/cco/ont00001879> [  # designated by → GenderMarker
        rdf:type persona:GenderMarker ;
        <https://purl.org/cco/ont00001765> "F"
    ] ;

    # ── Photo ────────────────────────────────────────────────────────────────

    persona:hasPhoto "https://example.org/alice-passport-photo.jpg"^^xsd:anyURI .
```
