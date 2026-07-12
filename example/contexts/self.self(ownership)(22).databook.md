---
id: https://www.example.org/mia/contexts/self.self(ownership)(22)
title: "About Alice Walker in the Ownership cell as claimed by Alice Walker"
type: context-databook
version: 2.0.6
created: 2026-06-01
description: >
  Alice Walker's possessions context. Records the physical cards she carries day-to-day:
  a wallet containing her driver's license and payment card, plus a health insurance card
  and Social Security card held separately.
mia:
  claimant: ":Self"
  subject: ":Self"
  about-by: "context:SBScontext"
graph:
  named_graph: https://www.example.org/mia/contexts/self.self(ownership)(22)#graph
  rdf_version: "1.1"
shapes:
  - http://www.example.org/shapes
process:
  transformer: human
  timestamp: 2026-06-19T00:00:00Z
  agent:
    name: Paul Trevithick
    role: author
---

## Overview

This context captures Alice Walker's day-to-day physical possessions. Her wallet holds her driver's license and payment card. Her health insurance card is carried separately (not in the wallet). Her Social Security card is stored at home for safety.

## Identity Data

```turtle
<!-- databook:id: alice-possessions-identity -->
<!-- databook:graph: https://www.example.org/mia/contexts/self.self(ownership)(22)#graph -->
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
