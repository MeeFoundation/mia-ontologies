---
id: http://www.example.org/mia/cells/cell-02
title: "ATT"
type: cell-databook
version: 1.2.0
created: 2026-07-10
description: >
  Cell DataBook of category "ATT" (cell:origin: cat:Companies). May carry one or two required subject values.
mia:
  origin: "cat:Companies"
  creator: ":Self"
  memberCount: "cell:OneMember"
  subject: ":Self"
  memberTopics: "topic-11"
  topics:
    - id: "http://www.example.org/mia/topics/topic-11"
      claimant: ":Self"
      subject: ":Self"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
---

## Topics

<a id="topic-11"></a>
### Topic 11

#### Overview

This topic captures Alice Walker's AT&T account topic. Alice self-enters her mobile phone number (+15108149999, E.164 format). AT&T is not a PDN node, so Alice records this data herself rather than receiving it from AT&T.

#### Topic Graph

```turtle
<!-- databook:id: alice-att-topic-graph -->
<!-- databook:graph: http://www.example.org/mia/topics/topic-11#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Self <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → Phone
        rdf:type cco:ent00000023 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "+15108149999" ;
        rdfs:comment "E.164 format (international standard)"@en
    ] .
```
