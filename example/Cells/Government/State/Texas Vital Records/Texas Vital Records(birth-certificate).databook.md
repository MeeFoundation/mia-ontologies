---
id: http://www.example.org/mia/cells/cell-10
title: "Texas Vital Records"
type: cell-databook
version: 1.1.0
created: 2026-07-10
description: >
  Cell DataBook for folder "Texas Vital Records" (cell:origin: cat:BirthCertificate). It is a one-member cell with one member entry about :Self.
mia:
  origin: "cat:BirthCertificate"
  creator: ":Self"
  members: "graph-24"
  graphs:
    - id: "http://www.example.org/mia/graphs/graph-24"
      claimant: ":Self"
      subject: ":Self"
      template: "persona:BirthCertificateDocument"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/graph/shapes
        - http://mee.foundation/ontologies/persona/shapes/birthcertificate
  shape: "pshapes:BirthCertificateDocumentShape"
---

## Graphs

<a id="graph-24"></a>
### Graph 24

#### Overview

This graph captures Alice Walker's Texas birth certificate identity data. Alice self-enters her legal name (Margery Alice Walker) and maiden name (Margery Alice Arnold) from her physical birth certificate. Validated by the `BirthCertificate` per-template SHACL shapes. Alice is the claimant.

#### Graph

```turtle
<!-- databook:id: alice-tx-birth-cert-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-24#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Self persona:hasIdentityDocument :Alice_TX_Birth_Certificate .

:Alice_TX_Birth_Certificate rdf:type owl:NamedIndividual ,
                                      persona:BirthCertificateDocument ;
    rdfs:label "Alice Walker's Texas Birth Certificate"@en ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → GivenName (legal first name)
        rdf:type cco:ent00000002 ;  # GivenName
        <https://w3id.org/cco-domains/cco/ont00001765> "Margery"  # has text value
    ] ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → AdditionalName (middle name)
        rdf:type cco:ent00000003 ;  # AdditionalName
        <https://w3id.org/cco-domains/cco/ont00001765> "Alice"  # has text value
    ] ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → FamilyName
        rdf:type cco:ent00000004 ;  # FamilyName
        <https://w3id.org/cco-domains/cco/ont00001765> "Walker"  # has text value
    ] ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → AlternateName (maiden name)
        rdf:type cco:ent00000006 ;  # AlternateName
        <https://w3id.org/cco-domains/cco/ont00001765> "Margery Alice Arnold" ;  # has text value
        rdfs:comment "Maiden name (former legal name before marriage)"@en
    ] .
```
