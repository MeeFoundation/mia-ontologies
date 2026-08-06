---
id: http://www.example.org/mia/categories/passport-cell
title: "Passport (Cell)"
type: cell-databook
version: 1.1.0
created: 2026-07-10
description: >
  Cell DataBook of category "Passport" (mia.catType: Passport). Content may include topics/folder/note links, and may carry one or two required subject values.
mia:
  creator: ":Self"
  memberCount: "cell:OneMember"
  subject: ":Self"
  memberTopics: "https://www.example.org/mia/topics/self.self(passport)(19)"
  topics:
    - id: "https://www.example.org/mia/topics/self.self(passport)(19)"
      title: "About Alice Walker in the Federal cell as claimed by Alice Walker"
      claimant: ":Self"
      subject: ":Self"
      template: "persona:PassportDocument"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
        - http://mee.foundation/ontologies/persona/shapes/passport
      process:
        transformer: human
        timestamp: 2026-06-20T00:00:00Z
        agent:
          name: Paul Trevithick
          role: author
  shape: "pshapes:PassportDocumentShape"
---

## Topics

<a id="topic-19"></a>
### Topic 19 — About Alice Walker in the Federal cell as claimed by Alice Walker

#### Overview

This topic captures Alice Walker's US passport identity data. Alice self-enters her legal name (Margery Alice Walker), date of birth (1985-07-04), US passport number (123456789), issue date (2021-07-04), expiration date (2031-07-04), place of birth (Austin, Texas, USA), gender marker (F), and a photo. Validated by the `Passport` per-template SHACL shapes.

#### Topic Graph

```turtle
<!-- databook:id: alice-passport-topic-graph -->
<!-- databook:graph: https://www.example.org/mia/topics/self.self(passport)(19)#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

:Self persona:hasIdentityDocument :Alice_US_Passport ;
    <https://purl.org/cco/ont00001879> :Alice_Passport_Number .  # Person designated by → Passport Number

:Alice_US_Passport rdf:type owl:NamedIndividual ,
                             persona:PassportDocument ;
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

    cco:ent00000069 [  # has issue date → Calendar Date Identifier
        rdf:type cco:ont00001340 ;
        <https://purl.org/cco/ont00001765> "2021-07-04"
    ] ;

    cco:ent00000070 [  # has expiration date → Calendar Date Identifier
        rdf:type cco:ont00001340 ;
        <https://purl.org/cco/ont00001765> "2031-07-04"
    ] ;

    # ── Passport number (two-relation form: Person designated-by, document is-carrier-of) ──

    <http://purl.obolibrary.org/obo/BFO_0000101> :Alice_Passport_Number ;  # document is carrier of → Passport Number

    # ── Issuing country ──────────────────────────────────────────────────────

    <https://purl.org/cco/ont00001879> [  # designated by → Issuing Jurisdiction
        rdf:type cco:ent00000068 ;
        <https://purl.org/cco/ont00001765> "USA"
    ] ;

    # ── Place of birth ───────────────────────────────────────────────────────

    <https://purl.org/cco/ont00001879> [  # designated by → Place of Birth
        rdf:type cco:ent00000067 ;
        <https://purl.org/cco/ont00001765> "Austin, Texas, USA"
    ] ;

    # ── Gender marker ────────────────────────────────────────────────────────

    <https://purl.org/cco/ont00001879> [  # designated by → GenderMarker
        rdf:type persona:GenderMarker ;
        <https://purl.org/cco/ont00001765> "F"
    ] ;

    # ── Photo ────────────────────────────────────────────────────────────────

    persona:hasPhoto "https://example.org/alice-passport-photo.jpg"^^xsd:anyURI .

:Alice_Passport_Number rdf:type owl:NamedIndividual ,
                                cco:ent00000066 ;  # Passport Number
    rdfs:label "Alice Walker's US Passport Number"@en ;
    <https://purl.org/cco/ont00001765> "123456789" .  # placeholder US passport number
```
