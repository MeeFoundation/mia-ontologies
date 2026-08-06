---
id: https://www.example.org/mia/topics/self.self(alice-walker)(employee)(10)
title: "About Alice Walker in the Alice Walker cell as claimed by Alice Walker"
type: topic-databook
version: 2.0.14
created: 2026-06-14
description: >
  Alice Walker's JSContactCard business card persona. Records her professional contact
  details: name, work email, work phone, employer, department, job title, and LinkedIn URL.
mia:
  claimant: ":Self"
  subject: ":Self"
  template: "persona:JSContactCard"
graph:
  named_graph: https://www.example.org/mia/topics/self.self(alice-walker)(employee)(10)#graph
  rdf_version: "1.1"
shapes:
  - http://mee.foundation/ontologies/persona/shapes
  - http://mee.foundation/ontologies/topic/shapes
  - http://mee.foundation/ontologies/persona/shapes/jscontactcard
process:
  transformer: human
  timestamp: 2026-06-19T00:00:00Z
  agent:
    name: Paul Trevithick
    role: author
---

## Overview

This topic captures Alice Walker's professional business card in JSContactCard format. It records her full name, work email (alice@acme.com), work phone (+15108149999), employer (Acme), department (Engineering), job title (Software Engineer), and LinkedIn profile URL. Validated by the `JSContactCard` per-template SHACL shapes.

## Topic Graph

```turtle
<!-- databook:id: alice-business-card-topic-graph -->
<!-- databook:graph: https://www.example.org/mia/topics/self.self(alice-walker)(employee)(10)#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Self rdfs:comment "Alice Walker's JSContact card persona — professional contact details taking details from her Acme topic."@en ;

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
