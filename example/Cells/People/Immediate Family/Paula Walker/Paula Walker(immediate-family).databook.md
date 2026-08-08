---
id: http://www.example.org/mia/cells/cell-23
title: "Paula Walker"
type: cell-databook
version: 1.1.0
created: 2026-07-10
description: >
  Cell DataBook of category "Paula Walker" (cell:origin: cat:ImmediateFamily). May carry one or two required subject values.
mia:
  origin: "cat:ImmediateFamily"
  creator: ":Self"
  memberCount: "cell:TwoMember"
  subject:
    - ":Paula_Walker"
    - ":Self"
  memberTopics:
    - "topic-05"
    - "topic-21"
    - "topic-07"
  topics:
    - id: "http://www.example.org/mia/topics/topic-05"
      claimant: ":Paula_Walker"
      subject: ":Paula_Walker"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
    - id: "http://www.example.org/mia/topics/topic-07"
      claimant: ":Self"
      subject: ":Paula_Walker"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
    - id: "http://www.example.org/mia/topics/topic-21"
      claimant: ":Self"
      subject: ":Self"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
---

## Topics

<a id="topic-05"></a>
### Topic 05

#### Overview

This topic captures Paula Walker's self-claimed family persona as transmitted from Paula's Mia to Alice's Mia over the PDN.

#### Topic Graph

```turtle
<!-- databook:id: paula-family-paula-topic-graph -->
<!-- databook:graph: http://www.example.org/mia/topics/topic-05#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Paula_Walker rdf:type owl:NamedIndividual ,
               persona:Person ;
    rdfs:label "Paula Walker (Family) self-claimed"@en .
```

<a id="topic-07"></a>
### Topic 07

#### Overview

This topic captures Alice's record of her family member Paula Walker. Alice claims Paula's name in the family topic.

#### Topic Graph

```turtle
<!-- databook:id: paula-family-alice-topic-graph -->
<!-- databook:graph: http://www.example.org/mia/topics/topic-07#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Paula_Walker rdf:type owl:NamedIndividual ,
               persona:Person ;
    rdfs:label "Paula Walker (Family)"@en ;

    <https://purl.org/cco/ont00001879> [  # designated by → GivenName
        rdf:type cco:ent00000002 ;  # GivenName
        <https://purl.org/cco/ont00001765> "Paula"  # has text value
    ] ;

    <https://purl.org/cco/ont00001879> [  # designated by → FamilyName
        rdf:type cco:ent00000004 ;  # FamilyName
        <https://purl.org/cco/ont00001765> "Walker"  # has text value
    ] .
```

<a id="topic-21"></a>
### Topic 21

#### Overview

This topic captures Alice Walker's family relationships. It records her maternal relationship with Paula Walker and her family social network, which includes Paula Walker and Carol Walker (Alice's sister) as members. Paula's own family topic (`topic-05`) is the peer record in this relationship; Carol's own claimed record about their mother appears separately in the "Med. App. Info" cell (topic 28).

#### Topic Graph

```turtle
<!-- databook:id: alice-family-topic-graph -->
<!-- databook:graph: http://www.example.org/mia/topics/topic-21#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Self rdfs:comment "Alice Walker's persona for her family relationships."@en ;

    <https://purl.org/cco/ont00001879> [  # designated by → AlternateName
        rdf:type cco:ent00000006 ;  # AlternateName
        <https://purl.org/cco/ont00001765> "Alice Walker"
    ] ;

    cco:ont00001780 :Paula_Walker ;  # has mother

    persona:hasSocialNetwork :Alice_Family_Network .


:Alice_Family_Network rdf:type owl:NamedIndividual ,
                               cco:ont00001183 ;  # Social Network
    rdfs:label "Alice Walker's family connections"@en ;
    <http://purl.obolibrary.org/obo/BFO_0000115> :Paula_Walker ,  # has member part
                                                  :Carol_Walker .  # has member part (Alice's sister)
```
