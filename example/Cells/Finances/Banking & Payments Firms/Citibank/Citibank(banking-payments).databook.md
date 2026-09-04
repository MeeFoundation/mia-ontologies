---
id: http://www.example.org/mia/cells/cell-04
title: "Citibank"
type: cell-databook
version: 1.1.0
created: 2026-07-10
description: >
  Cell DataBook for folder "Citibank" (cell:category: cat:BankingPayments). It is a two-member cell with two members about :Self and :Citibank.
mia:
  category: "cat:BankingPayments"
  creator: ":Self"
  owner: ":Self"
  member:
    - "graph-09"
    - "graph-27"
  graphs:
    - id: "http://www.example.org/mia/graphs/graph-09"
      claimant: ":Citibank"
      subject: ":Self"
    - id: "http://www.example.org/mia/graphs/graph-27"
      claimant: ":Self"
      subject: ":Citibank"
---

## Graphs

<a id="graph-09"></a>
### Graph 09

#### Overview

This graph captures Alice Walker's financial relationship with Citibank. Citibank is a PDN Organization node which directly claims the information about Alice in this graph. The information in this graph has been transmitted from the Citibank PDN node to Alice's own instance of the app. It includes a VISA debit card linked to a checking account, plus an online service account for online.citi.com. Citibank is the claimant.

#### Graph

```turtle
<!-- databook:id: citibank-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-09#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix o: <http://mee.foundation/ontologies/organization#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
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
    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → Card Number (PAN)
        rdf:type cco:ent00000052 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "4111-1111-1111-1111"
    ] ;
    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → CVV
        rdf:type cco:ent00000053 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "123"
    ] ;
    cco:ent00000070 [  # has expiration date → Calendar Date Identifier
        rdf:type cco:ont00001340 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "12/28"
    ] ;
    persona:accessesBankAccount :Alice_Checking_Account .

:Alice_Checking_Account rdf:type owl:NamedIndividual ,
                                 persona:CheckingAccount ;
    rdfs:label "Alice Walker's Citibank Checking Account"@en ;
    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → Checking Account Number
        rdf:type cco:ent00000071 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "9876543210"
    ] ;
    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → Routing Number
        rdf:type cco:ent00000072 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "021000089"
    ] .

:Alice_Citibank_Online rdf:type owl:NamedIndividual ,
                                cco:ent00000033 ;  # Online Service Account
    rdfs:label "Alice Walker's Citibank Online Account"@en ;
    cco:ent00000034 "Citibank" ;                   # has service name
    cco:ent00000035 "awalker@gmail.com" ;           # has user handle (username)
    cco:ent00000036 <https://online.citi.com> ;    # has service URI
    persona:hasPassword "C1t1b@nk#2024!" .         # has password
```

<a id="graph-27"></a>
### Graph 27

#### Overview

This graph captures Alice Walker's own self-claimed notes about Citibank as an institution — her own record of the organization, distinct from Citibank's own claimed record about her (graph 09). Together the two graphs give this cell's `member` the two distinct subjects (`:Self`, `:Citibank`) required for a two-member cell. Alice is the claimant.

#### Graph

```turtle
<!-- databook:id: alice-citibank-org-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-27#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix o: <http://mee.foundation/ontologies/organization#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Citibank rdf:type owl:NamedIndividual ,
                   o:Organization ;
    rdfs:label "Citibank"@en ;

    <https://w3id.org/cco-domains/cco/ont00001917> [  # described by → Organization Note
        rdf:type cco:ent00000048 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "My primary checking account is here — used for rent and bill-pay autopay. Opened 2019."
    ] .
```
