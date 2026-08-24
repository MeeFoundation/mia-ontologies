---
id: http://www.example.org/mia/cells/cell-19
title: "Paula Walker"
type: cell-databook
version: 1.1.0
created: 2026-07-10
description: >
  Cell DataBook for folder "Paula Walker" (cell:origin: cat:Employee). It is a one-member cell with one memberTopic about :Self and one otherTopic about :Paula_Walker.
mia:
  origin: "cat:Employee"
  creator: ":Self"
  memberCount: "cell:OneMember"
  memberTopics: "topic-20"
  otherTopics: "topic-06"
  topics:
    - id: "http://www.example.org/mia/topics/topic-06"
      claimant: ":Self"
      subject: ":Paula_Walker"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
    - id: "http://www.example.org/mia/topics/topic-20"
      claimant: ":Self"
      subject: ":Self"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
---

## Topics

<a id="topic-06"></a>
### Topic 06

#### Overview

This topic captures Alice's record of her colleague Paula Walker in their shared Acme employment topic. Alice is the claimant.

#### Topic Graph

```turtle
<!-- databook:id: paula-acme-topic-graph -->
<!-- databook:graph: http://www.example.org/mia/topics/topic-06#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Paula_Walker rdf:type owl:NamedIndividual ,
               persona:Person ;
    rdfs:label "Paula Walker (Acme)"@en .
```

<a id="topic-20"></a>
### Topic 20

#### Overview

This topic captures Alice Walker's employee identity at Acme. It records her work email address (alice@acme.com) and her Acme social network, which includes colleague Paula Walker. Alice is the claimant.

#### Topic Graph

```turtle
<!-- databook:id: alice-acme-topic-graph -->
<!-- databook:graph: http://www.example.org/mia/topics/topic-20#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Self rdfs:comment "Alice Walker's persona for her employment at Acme."@en ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → AlternateName
        rdf:type cco:ent00000006 ;  # AlternateName
        <https://w3id.org/cco-domains/cco/ont00001765> "Alice Walker"
    ] ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → Email
        rdf:type cco:ent00000024 ;  # Email
        <https://w3id.org/cco-domains/cco/ont00001765> "alice@acme.com"  # has text value
    ] ;

    persona:hasSocialNetwork :Alice_Acme_Network .


:Alice_Acme_Network rdf:type owl:NamedIndividual ,
                             cco:ont00001183 ;  # Social Network
    rdfs:label "Alice Walker's Acme connections"@en ;
    <http://purl.obolibrary.org/obo/BFO_0000115> :Paula_Walker .  # has member part
```
