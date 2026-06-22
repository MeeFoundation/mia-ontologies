---
id: http://www.example.org/mia/alice(business-card)alice
title: "Alice Walker — Business Card"
type: context-databook
version: 2.0.2
created: 2026-06-14
description: >
  Alice Walker's JSContactCard business card persona. Records her professional contact
  details: name, work email, work phone, employer, department, job title, and LinkedIn URL.
mia:
  name: "Business Card"
  category: "context:Employee"
  assertedBy: ":Self"
  subject: ":Self"
  about-by: "context:SBS-Context"
  template: "persona:JSContactCard"
graph:
  named_graph: http://www.example.org/mia/alice(business-card)alice#graph
  rdf_version: "1.1"
shapes:
  - http://www.example.org/shapes
  - http://www.example.org/shapes/jscontactcard
process:
  transformer: human
  timestamp: 2026-06-19T00:00:00Z
  agent:
    name: Paul Trevithick
    role: author
---

## Overview

This context captures Alice Walker's professional business card in JSContactCard format. It records her full name, work email (alice@acme.com), work phone (+15108149999), employer (Acme), department (Engineering), job title (Software Engineer), and LinkedIn profile URL. Validated by the `JSContactCard` per-template SHACL shapes.

## Identity Data

```turtle
<!-- databook:id: alice-business-card-identity -->
<!-- databook:graph: http://www.example.org/mia/alice(business-card)alice#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Self rdf:type owl:NamedIndividual ,
               persona:Person ;
    rdfs:label "Alice Walker (Business Card)"@en ;
    rdfs:comment "Alice Walker's JSContact card persona — professional contact details taking details from her Acme context."@en ;

    # ── Name components ──────────────────────────────────────────────────────

    <https://purl.org/cco/ont00001879> [  # designated by → GivenName
        rdf:type cco:ent00000002 ;
        <https://purl.org/cco/ont00001765> "Alice"
    ] ;

    <https://purl.org/cco/ont00001879> [  # designated by → FamilyName
        rdf:type cco:ent00000004 ;
        <https://purl.org/cco/ont00001765> "Walker"
    ] ;

    # ── Contact channels ─────────────────────────────────────────────────────

    <https://purl.org/cco/ont00001879> [  # designated by → EmailAddress (work)
        rdf:type cco:ent00000024 ;
        <https://purl.org/cco/ont00001765> "alice@acme.com" ;
        persona:contactContext "work"
    ] ;

    <https://purl.org/cco/ont00001879> [  # designated by → TelephoneNumber (work, voice)
        rdf:type cco:ent00000023 ;
        <https://purl.org/cco/ont00001765> "+15108149999" ;
        persona:contactContext "work" ;
        persona:phoneFeature "voice"
    ] ;

    # ── Organisation ─────────────────────────────────────────────────────────

    <https://purl.org/cco/ont00001879> [  # designated by → OrganizationName
        rdf:type cco:ent00000047 ;
        <https://purl.org/cco/ont00001765> "Acme"
    ] ;

    <https://purl.org/cco/ont00001879> [  # designated by → OrganizationUnit (department)
        rdf:type persona:OrganizationUnit ;
        <https://purl.org/cco/ont00001765> "Engineering"
    ] ;

    <https://purl.org/cco/ont00001879> [  # designated by → JobTitle
        rdf:type persona:JobTitle ;
        <https://purl.org/cco/ont00001765> "Software Engineer"
    ] ;

    # ── Online services ──────────────────────────────────────────────────────

    <https://purl.org/cco/ont00001879> [  # designated by → WebURL (LinkedIn profile)
        rdf:type persona:WebURL ;
        <https://purl.org/cco/ont00001765> "https://www.linkedin.com/in/alicewalker" ;
        persona:serviceLabel "linkedin"
    ] .
```
