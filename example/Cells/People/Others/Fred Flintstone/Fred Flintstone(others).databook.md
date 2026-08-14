---
id: http://www.example.org/mia/cells/cell-17
title: "Fred Flintstone"
type: cell-databook
version: 1.1.0
created: 2026-08-03
description: >
  Cell DataBook of category "Fred Flintstone" (cell:origin: cat:Others). May carry one or two required subject values.
mia:
  origin: "cat:Others"
  creator: ":Self"
  memberCount: "cell:TwoMember"
  subject:
    - ":Fred_Flintstone"
    - ":Self"
  memberTopics:
    - "topic-31"
    - "topic-29"
  topics:
    - id: "http://www.example.org/mia/topics/topic-29"
      claimant: ":Self"
      subject: ":Self"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
    - id: "http://www.example.org/mia/topics/topic-31"
      claimant: ":Fred_Flintstone"
      subject: ":Fred_Flintstone"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
---

## Topics

<a id="topic-29"></a>
### Topic 29

#### Overview

This topic captures Alice Walker's self-claimed persona in her 1:1 relationship with Fred Flintstone. It records the name Alice presents to Fred and her social network link to him.

#### Topic Graph

```turtle
<!-- databook:id: alice-fred-alice-topic-graph -->
<!-- databook:graph: http://www.example.org/mia/topics/topic-29#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Self rdfs:comment "Alice Walker's persona for her 1:1 relationship with Fred."@en ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → AlternateName
        rdf:type cco:ent00000006 ;  # AlternateName
        <https://w3id.org/cco-domains/cco/ont00001765> "Alice Walker"
    ] ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → GivenName
        rdf:type cco:ent00000002 ;  # GivenName
        <https://w3id.org/cco-domains/cco/ont00001765> "Alice"  # has text value
    ] ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → FamilyName
        rdf:type cco:ent00000004 ;  # FamilyName
        <https://w3id.org/cco-domains/cco/ont00001765> "Walker"  # has text value
    ] ;

    persona:hasSocialNetwork :Alice_Fred_Network .


:Alice_Fred_Network rdf:type owl:NamedIndividual ,
                             cco:ont00001183 ;  # Social Network
    rdfs:label "Alice Walker's Fred connection"@en ;
    <http://purl.obolibrary.org/obo/BFO_0000115> :Fred_Flintstone .  # has member part
```

<a id="topic-31"></a>
### Topic 31

#### Overview

This topic captures Fred Flintstone's self-claimed persona, transmitted from Fred's Mia to Alice's Mia over the PDN. It records Fred's name and his social network link to Alice.

#### Topic Graph

```turtle
<!-- databook:id: fred-fred-fred-topic-graph -->
<!-- databook:graph: http://www.example.org/mia/topics/topic-31#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Fred_Flintstone rdf:type owl:NamedIndividual ,
              persona:Person ;
    rdfs:label "Fred Flintstone"@en ;
    rdfs:comment "Fred Flintstone's self-claimed persona in his 1:1 relationship with Alice."@en ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → GivenName
        rdf:type cco:ent00000002 ;  # GivenName
        <https://w3id.org/cco-domains/cco/ont00001765> "Fred"  # has text value
    ] ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → FamilyName
        rdf:type cco:ent00000004 ;  # FamilyName
        <https://w3id.org/cco-domains/cco/ont00001765> "Flintstone"  # has text value
    ] ;

    persona:hasSocialNetwork :Fred_Fred_Network .


:Fred_Fred_Network rdf:type owl:NamedIndividual ,
                          cco:ont00001183 ;  # Social Network
    rdfs:label "Fred Flintstone's Alice connection"@en ;
    <http://purl.obolibrary.org/obo/BFO_0000115> :Self .  # has member part → Alice
```
