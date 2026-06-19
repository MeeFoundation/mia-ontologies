---
id: http://www.example.org/mia/alice(citibank)citibank
title: "Alice Walker — Citibank"
type: databook
version: 2.0.3
created: 2026-06-15
description: >
  Alice Walker's Citibank context. Records her VISA debit card, checking account,
  and online banking credentials. Asserted by Citibank (a PDN Organization node).
mia:
  name: "Citibank"
  contextCategory: "context:FinancialServices"
  assertedBy: "identity:Organization"
  subject: "identity:Self"
graph:
  named_graph: http://www.example.org/mia/alice(citibank)citibank#graph
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

This context captures Alice Walker's financial relationship with Citibank. Citibank is a PDN Organization node which directly asserts the information about Alice in this context. The information in this context has been transmitted from the Citibank PDN node to Alice's Mia. It includes a VISA debit card linked to a checking account, plus an online service account for online.citi.com.

## Identity Data

```turtle
<!-- databook:id: citibank-identity -->
<!-- databook:graph: http://www.example.org/mia/alice(citibank)citibank#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Self rdf:type owl:NamedIndividual ,
               persona:Person ;
    rdfs:label "Alice Walker (Citibank)"@en ;
    rdfs:comment "Alice Walker's persona in the context of her Citibank relationship."@en ;
    persona:hasPaymentCard :Alice_Debit_Card ;
    persona:hasBankAccount :Alice_Checking_Account ;
    cco:ent00000045 :Alice_Citibank_Online .  # holds user account

:Alice_Debit_Card rdf:type owl:NamedIndividual ,
                           cco:ent00000051 ;  # Debit Card
    rdfs:label "Alice Walker's VISA Debit Card"@en ;
    <https://purl.org/cco/ont00001879> [  # designated by → Card Number (PAN)
        rdf:type cco:ent00000052 ;
        <https://purl.org/cco/ont00001765> "4111-1111-1111-1111"
    ] ;
    <https://purl.org/cco/ont00001879> [  # designated by → CVV
        rdf:type cco:ent00000053 ;
        <https://purl.org/cco/ont00001765> "123"
    ] ;
    <https://purl.org/cco/ont00001879> [  # designated by → Expiration Date
        rdf:type cco:ent00000054 ;
        <https://purl.org/cco/ont00001765> "12/28"
    ] ;
    persona:accessesBankAccount :Alice_Checking_Account .

:Alice_Checking_Account rdf:type owl:NamedIndividual ,
                                 persona:CheckingAccount ;
    rdfs:label "Alice Walker's Citibank Checking Account"@en ;
    <https://purl.org/cco/ont00001879> [  # designated by → Account Number
        rdf:type persona:CheckingAccountNumber ;
        <https://purl.org/cco/ont00001765> "9876543210"
    ] ;
    <https://purl.org/cco/ont00001879> [  # designated by → Routing Number
        rdf:type persona:RoutingNumber ;
        <https://purl.org/cco/ont00001765> "021000089"
    ] .

:Alice_Citibank_Online rdf:type owl:NamedIndividual ,
                                cco:ent00000033 ;  # Online Service Account
    rdfs:label "Alice Walker's Citibank Online Account"@en ;
    cco:ent00000034 "Citibank" ;                   # has service name
    cco:ent00000035 "awalker@gmail.com" ;           # has user handle (username)
    cco:ent00000036 "https://online.citi.com" ;    # has service URI
    persona:hasPassword "C1t1b@nk#2024!" .         # has password
```
