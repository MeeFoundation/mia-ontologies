---
id: http://www.example.org/mia/categories/Citibank(banking-payments)
title: "Citibank"
type: cell-databook
version: 1.1.0
created: 2026-07-10
description: >
  Cell DataBook of category "Citibank" (cell:origin: cat:BankingPayments). May carry one or two required subject values.
mia:
  origin: "cat:BankingPayments"
  creator: ":Self"
  memberCount: "cell:TwoMember"
  subject:
    - ":Self"
    - ":Citibank"
  memberTopics:
    - "topic-09"
    - "topic-27"
  topics:
    - id: "http://www.example.org/mia/topics/topic-09"
      claimant: ":Citibank"
      subject: ":Self"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
    - id: "http://www.example.org/mia/topics/topic-27"
      claimant: ":Self"
      subject: ":Citibank"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
---

## Topics

<a id="topic-09"></a>
### Topic 09 — About Alice Walker in the BankingPayments cell as claimed by Citibank

#### Overview

This topic captures Alice Walker's financial relationship with Citibank. Citibank is a PDN Organization node which directly claims the information about Alice in this topic. The information in this topic has been transmitted from the Citibank PDN node to Alice's Mia. It includes a VISA debit card linked to a checking account, plus an online service account for online.citi.com.

#### Topic Graph

```turtle
<!-- databook:id: citibank-topic-graph -->
<!-- databook:graph: http://www.example.org/mia/topics/topic-09#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix o: <http://mee.foundation/ontologies/organization#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Citibank rdf:type owl:NamedIndividual ,
                   o:Organization ;
    rdfs:label "Citibank"@en .

:Self rdfs:comment "Alice Walker regarding her Citibank relationship."@en ;
    cco:ent00000073 :Alice_Debit_Card ;             # has payment card
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
    cco:ent00000070 [  # has expiration date → Calendar Date Identifier
        rdf:type cco:ont00001340 ;
        <https://purl.org/cco/ont00001765> "12/28"
    ] ;
    persona:accessesBankAccount :Alice_Checking_Account .

:Alice_Checking_Account rdf:type owl:NamedIndividual ,
                                 persona:CheckingAccount ;
    rdfs:label "Alice Walker's Citibank Checking Account"@en ;
    <https://purl.org/cco/ont00001879> [  # designated by → Checking Account Number
        rdf:type cco:ent00000071 ;
        <https://purl.org/cco/ont00001765> "9876543210"
    ] ;
    <https://purl.org/cco/ont00001879> [  # designated by → Routing Number
        rdf:type cco:ent00000072 ;
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

<a id="topic-27"></a>
### Topic 27 — About Citibank in the BankingPayments cell as claimed by Alice Walker

#### Overview

This topic captures Alice Walker's own self-claimed notes about Citibank as an institution — her own record of the organization, distinct from Citibank's own claimed record about her (topic 09). Together the two topics give this cell's `memberTopics` the two distinct subjects (`:Self`, `:Citibank`) required for a `cell:TwoMember` cell.

#### Topic Graph

```turtle
<!-- databook:id: alice-citibank-org-topic-graph -->
<!-- databook:graph: http://www.example.org/mia/topics/topic-27#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix o: <http://mee.foundation/ontologies/organization#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Citibank rdf:type owl:NamedIndividual ,
                   o:Organization ;
    rdfs:label "Citibank"@en ;

    <https://purl.org/cco/ont00001917> [  # described by → Organization Note
        rdf:type cco:ent00000048 ;
        <https://purl.org/cco/ont00001765> "My primary checking account is here — used for rent and bill-pay autopay. Opened 2019."
    ] .
```
