---
id: http://www.example.org/mia/cells/cell-18
title: "California DMV"
type: cell-databook
version: 1.1.0
created: 2026-07-10
description: >
  Cell DataBook of category "California DMV" (cell:origin: cat:DriversLicense). May carry one or two required subject values.
mia:
  origin: "cat:DriversLicense"
  creator: ":Self"
  memberCount: "cell:OneMember"
  subject: ":Self"
  memberTopics: "topic-15"
  topics:
    - id: "http://www.example.org/mia/topics/topic-15"
      claimant: ":Self"
      subject: ":Self"
      template: "persona:DriversLicenseDocument"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
        - http://mee.foundation/ontologies/persona/shapes/driverslicense
  shape: "pshapes:DriversLicenseDocumentShape"
---

## Topics

<a id="topic-15"></a>
### Topic 15

#### Overview

This topic captures Alice Walker's California driver's license identity data. Alice self-enters her legal name (Margery Alice Walker), date of birth (1985-07-04), California license number (A1234567), expiration date (2031-07-04), issuing jurisdiction (CA), and a photo. Validated by the `DriversLicense` per-template SHACL shapes.

#### Topic Graph

```turtle
<!-- databook:id: alice-driverslicense-topic-graph -->
<!-- databook:graph: http://www.example.org/mia/topics/topic-15#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

:Self persona:hasIdentityDocument :Alice_CA_DriversLicense ;
    <https://w3id.org/cco-domains/cco/ont00001879> :Alice_DL_Number .  # Person designated by → Drivers License Number

:Alice_CA_DriversLicense rdf:type owl:NamedIndividual ,
                                   persona:DriversLicenseDocument ;
    rdfs:label "Alice Walker's California Driver's License"@en ;
    rdfs:comment "Alice Walker's California state-issued driver's licence identity data."@en ;

    # ── Legal name (matches Texas Birth Certificate) ─────────────────────────

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → GivenName (legal first name)
        rdf:type cco:ent00000002 ;  # GivenName
        <https://w3id.org/cco-domains/cco/ont00001765> "Margery"
    ] ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → AdditionalName (middle name)
        rdf:type cco:ent00000003 ;  # AdditionalName
        <https://w3id.org/cco-domains/cco/ont00001765> "Alice"
    ] ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → FamilyName
        rdf:type cco:ent00000004 ;  # FamilyName
        <https://w3id.org/cco-domains/cco/ont00001765> "Walker"
    ] ;

    # ── Dates ────────────────────────────────────────────────────────────────

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → Birthdate
        rdf:type cco:ent00000046 ;  # Birthdate
        <https://w3id.org/cco-domains/cco/ont00001765> "1985-07-04"
    ] ;

    cco:ent00000070 [  # has expiration date → Calendar Date Identifier
        rdf:type cco:ont00001340 ;  # Calendar Date Identifier
        <https://w3id.org/cco-domains/cco/ont00001765> "2031-07-04"
    ] ;

    # ── License number (two-relation form: Person designated-by, document is-carrier-of) ──

    <http://purl.obolibrary.org/obo/BFO_0000101> :Alice_DL_Number ;  # document is carrier of → Drivers License Number

    # ── Issuing jurisdiction ─────────────────────────────────────────────────

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → Issuing Jurisdiction
        rdf:type cco:ent00000068 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "CA"
    ] ;

    # ── Photo ────────────────────────────────────────────────────────────────

    persona:hasPhoto "https://example.org/alice-dl-photo.jpg"^^xsd:anyURI .

:Alice_DL_Number rdf:type owl:NamedIndividual ,
                          cco:ent00000065 ;  # Drivers License Number
    rdfs:label "Alice Walker's California Driver's License Number"@en ;
    <https://w3id.org/cco-domains/cco/ont00001765> "A1234567" .  # placeholder California DL number
```
