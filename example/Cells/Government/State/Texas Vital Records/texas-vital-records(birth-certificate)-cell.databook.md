---
id: http://www.example.org/mia/categories/texas-vital-records(birth-certificate)-cell
title: "Texas Vital Records (Cell)"
type: cell-databook
version: 1.1.0
created: 2026-07-10
description: >
  Cell DataBook of category "Texas Vital Records" (mia.catType: BirthCertificate). Content may include topics/folder/note links, and may carry one or two required subject values.
mia:
  creator: ":Self"
  memberCount: "cell:OneMember"
  subject: ":Self"
  memberTopics: "https://www.example.org/mia/topics/self.self(texas-vital-records)(birth-certificate)(24)"
  topics:
    - id: "https://www.example.org/mia/topics/self.self(texas-vital-records)(birth-certificate)(24)"
      title: "About Alice Walker in the State cell as claimed by Alice Walker"
      claimant: ":Self"
      subject: ":Self"
      template: "persona:BirthCertificateDocument"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
        - http://mee.foundation/ontologies/persona/shapes/birthcertificate
      process:
        transformer: human
        timestamp: 2026-06-19T00:00:00Z
        agent:
          name: Paul Trevithick
          role: author
  shape: "pshapes:BirthCertificateDocumentShape"
---

## Topics

<a id="topic-24"></a>
### Topic 24 — About Alice Walker in the State cell as claimed by Alice Walker

#### Overview

This topic captures Alice Walker's Texas birth certificate identity data. Alice self-enters her legal name (Margery Alice Walker) and maiden name (Margery Alice Arnold) from her physical birth certificate. Validated by the `BirthCertificate` per-template SHACL shapes.

#### Topic Graph

```turtle
<!-- databook:id: alice-tx-birth-cert-topic-graph -->
<!-- databook:graph: https://www.example.org/mia/topics/self.self(texas-vital-records)(birth-certificate)(24)#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Self persona:hasIdentityDocument :Alice_TX_Birth_Certificate .

:Alice_TX_Birth_Certificate rdf:type owl:NamedIndividual ,
                                      persona:BirthCertificateDocument ;
    rdfs:label "Alice Walker's Texas Birth Certificate"@en ;

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
