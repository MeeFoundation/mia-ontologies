---
id: http://www.example.org/mia/cells/cell-01
title: "Boston Hub Society"
type: cell-databook
version: 1.2.0
created: 2026-07-10
description: >
  Cell DataBook for folder "Boston Hub Society" (cell:origin: cat:Affiliations). It is a multi-member cell with three memberTopics about :BHS, :Self, and :Bob_Johnson.
mia:
  origin: "cat:Affiliations"
  creator: ":Self"
  memberCount: "cell:ThreePlusMember"
  memberTopics:
    - "topic-01"
    - "topic-14"
    - "topic-03"
  topics:
    - id: "http://www.example.org/mia/topics/topic-01"
      claimant: ":BHS"
      subject: ":BHS"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
    - id: "http://www.example.org/mia/topics/topic-03"
      claimant: ":Bob_Johnson"
      subject: ":Bob_Johnson"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
    - id: "http://www.example.org/mia/topics/topic-14"
      claimant: ":Self"
      subject: ":Self"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
---

## Topics

<a id="topic-01"></a>
### Topic 01

#### Overview

This topic captures the Boston Hub Society as an `o:Organization`. In our example BHS is compatible with PDN and participates directly as a member of this cell, alongside Alice and Bob. BHS asserts a basic profile about itself here. BHS is the claimant.

#### Topic Graph

```turtle
<!-- databook:id: bhs-org-topic-graph -->
<!-- databook:graph: http://www.example.org/mia/topics/topic-01#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix o: <http://mee.foundation/ontologies/organization#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:BHS rdf:type owl:NamedIndividual ,
             o:Organization ;
    rdfs:label "Boston Hub Society"@en ;

    <https://w3id.org/cco-domains/cco/ont00001917> [  # described by → Organization Note
        rdf:type cco:ent00000048 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "An informal Boston-area professional networking society. Current members include Alice Walker and Bob Johnson."
    ] .
```

<a id="topic-03"></a>
### Topic 03

#### Overview

This topic captures Bob Johnson's BHS profile as transmitted from Bob's Mia to Alice's Mia over the PDN. It records the name Bob presents to the Boston Hub Society. Bob is the claimant.

#### Topic Graph

```turtle
<!-- databook:id: bob-bhs-topic-graph -->
<!-- databook:graph: http://www.example.org/mia/topics/topic-03#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Bob_Johnson rdf:type owl:NamedIndividual ,
              persona:Person ;
    rdfs:label "Bob Johnson (BHS)"@en ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → GivenName
        rdf:type cco:ent00000002 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "Bob"
    ] ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → FamilyName
        rdf:type cco:ent00000004 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "Johnson"
    ] .
```

<a id="topic-14"></a>
### Topic 14

#### Overview

This topic captures Alice Walker's BHS profile — the identity data she shares with the Boston Hub Society. It includes her current Paradise, CA address, her phone number, and her Gmail address. Alice is the claimant.

#### Topic Graph

```turtle
<!-- databook:id: alice-bhs-topic-graph -->
<!-- databook:graph: http://www.example.org/mia/topics/topic-14#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Self rdfs:comment "Alice Walker's persona for her BHS profile."@en ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → AlternateName
        rdf:type cco:ent00000006 ;  # AlternateName
        <https://w3id.org/cco-domains/cco/ont00001765> "Alice Walker"
    ] ;

    <https://w3id.org/cco-domains/domains/AddressOntology#ent00000324> :Address_BHS ;  # has address → current address

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → Phone
        rdf:type cco:ent00000023 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "+15108149999"
    ] ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → Email
        rdf:type cco:ent00000024 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "awalker@gmail.com"
    ] .


:Address_BHS rdf:type owl:NamedIndividual ,
                      cco:ent00000010 ;  # USPostalAddress
    rdfs:label "Alice Walker's BHS Address"@en ;
    <http://purl.obolibrary.org/obo/BFO_0000178> [  # has continuant part → Street
        rdf:type cco:ent00000011 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "123 Sleepy Hollow"
    ] ;
    <http://purl.obolibrary.org/obo/BFO_0000178> [  # has continuant part → City
        rdf:type cco:ent00000012 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "Paradise"
    ] ;
    <http://purl.obolibrary.org/obo/BFO_0000178> [  # has continuant part → State
        rdf:type cco:ent00000013 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "CA"
    ] ;
    <http://purl.obolibrary.org/obo/BFO_0000178> [  # has continuant part → ZIP
        rdf:type cco:ent00000015 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "95969"
    ] ;
    <http://purl.obolibrary.org/obo/BFO_0000178> [  # has continuant part → Country
        rdf:type cco:ent00000014 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "USA"
    ] .

:BHS_AddressDesignation rdf:type owl:NamedIndividual ,
                                  cco:ent00000016 ;  # AddressDesignation
    rdfs:label "Alice Walker's BHS address designation"@en ;
    <http://purl.obolibrary.org/obo/BFO_0000057> :Self ;
    <https://w3id.org/cco-domains/domains/AddressOntology#ent00000324> :Address_BHS .

```
