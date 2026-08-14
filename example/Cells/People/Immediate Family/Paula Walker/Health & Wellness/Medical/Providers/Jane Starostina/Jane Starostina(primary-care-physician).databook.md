---
id: http://www.example.org/mia/cells/cell-14
title: "Jane Starostina"
type: cell-databook
version: 1.2.0
created: 2026-07-10
description: >
  Cell DataBook for folder "Jane Starostina" (cell:origin: cat:PrimaryCarePhysician). It is a one-member cell with one memberTopic about :Jane_Starostina.
mia:
  origin: "cat:PrimaryCarePhysician"
  creator: ":Self"
  memberCount: "cell:OneMember"
  subject: ":Jane_Starostina"
  memberTopics: "topic-25"
  topics:
    - id: "http://www.example.org/mia/topics/topic-25"
      claimant: ":Self"
      subject: ":Jane_Starostina"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
---

## Topics

<a id="topic-25"></a>
### Topic 25

#### Overview

This topic captures Alice's record of Dr. Jane Starostina, who is the primary care physician for Alice's mother, Paula Walker. Alice keeps this information so she and her sister Carol can coordinate Paula's medical appointments.

#### Topic Graph

```turtle
<!-- databook:id: jane-starostina-alice-topic-graph -->
<!-- databook:graph: http://www.example.org/mia/topics/topic-25#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Jane_Starostina rdf:type owl:NamedIndividual ,
               persona:Person ;
    rdfs:label "Jane Starostina (Primary Care Physician)"@en ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → GivenName
        rdf:type cco:ent00000002 ;  # GivenName
        <https://w3id.org/cco-domains/cco/ont00001765> "Jane"  # has text value
    ] ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → FamilyName
        rdf:type cco:ent00000004 ;  # FamilyName
        <https://w3id.org/cco-domains/cco/ont00001765> "Starostina"  # has text value
    ] ;

    <https://w3id.org/cco-domains/cco/ont00001917> [  # described by → Person Note
        rdf:type cco:ent00000048 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "Paula Walker's primary care physician"
    ] .
```
