---
id: http://www.example.org/mia/categories/ownership-cell
title: "Ownership (Cell)"
type: cell-databook
version: 1.1.0
created: 2026-07-10
description: >
  Cell DataBook of category "Ownership" (mia.catType: Ownership). Content may include topics/folder/note links, and may carry one or two required subject values.
mia:
  creator: ":Self"
  memberCount: "cell:OneMember"
  subject: ":Self"
  memberTopics: "https://www.example.org/mia/topics/self.self(ownership)(22)"
  topics:
    - id: "https://www.example.org/mia/topics/self.self(ownership)(22)"
      title: "About Alice Walker in the Ownership cell as claimed by Alice Walker"
      claimant: ":Self"
      subject: ":Self"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
      process:
        transformer: human
        timestamp: 2026-06-19T00:00:00Z
        agent:
          name: Paul Trevithick
          role: author
---

## Topics

<a id="topic-22"></a>
### Topic 22 — About Alice Walker in the Ownership cell as claimed by Alice Walker

#### Overview

This topic captures Alice Walker's day-to-day physical possessions. Her wallet holds her driver's license and payment card. Her health insurance card is carried separately (not in the wallet). Her Social Security card is stored at home for safety.

#### Topic Graph

```turtle
<!-- databook:id: alice-possessions-topic-graph -->
<!-- databook:graph: https://www.example.org/mia/topics/self.self(ownership)(22)#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

:Self persona:hasWallet :Alice_Wallet ;
    persona:hasPhysicalCard :Alice_HealthInsuranceCard ;   # not in wallet — carried separately
    persona:hasPhysicalCard :Alice_SSNCard .               # not in wallet — stored at home for safety


:Alice_Wallet rdf:type owl:NamedIndividual ,
                        persona:Wallet ;
    rdfs:label "Alice Walker's Wallet"@en .


:Alice_DriversLicense rdf:type owl:NamedIndividual ,
                               persona:PhysicalDriversLicense ;
    rdfs:label "Alice Walker's Driver's License"@en ;
    rdfs:comment "Alice Walker's physical Texas driver's license card."@en ;
    <http://purl.obolibrary.org/obo/BFO_0000176> :Alice_Wallet ;            # continuant part of → in wallet
    persona:hasImageScan "file:///scans/alice-drivers-license.png"^^xsd:anyURI .


:Alice_PaymentCard rdf:type owl:NamedIndividual ,
                            persona:PhysicalPaymentCard ;
    rdfs:label "Alice Walker's Payment Card"@en ;
    rdfs:comment "Alice Walker's physical debit card."@en ;
    <http://purl.obolibrary.org/obo/BFO_0000176> :Alice_Wallet .            # continuant part of → in wallet


:Alice_HealthInsuranceCard rdf:type owl:NamedIndividual ,
                                    persona:PhysicalHealthInsuranceCard ;
    rdfs:label "Alice Walker's Health Insurance Card"@en ;
    rdfs:comment "Alice Walker's physical health insurance membership card."@en ;
    persona:hasImageScan "file:///scans/alice-health-insurance-card.png"^^xsd:anyURI .


:Alice_SSNCard rdf:type owl:NamedIndividual ,
                        persona:PhysicalSocialSecurityCard ;
    rdfs:label "Alice Walker's Social Security Card"@en ;
    rdfs:comment "Alice Walker's Social Security card — stored at home, not carried in wallet."@en .
```
