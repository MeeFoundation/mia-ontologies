---
id: http://www.example.org/mia/cells/cell-06
title: "Social Security Administration"
type: cell-databook
version: 1.2.0
created: 2026-07-10
description: >
  Cell DataBook for folder "Social Security Administration" (cell:origin: cat:SSN). It is a one-member cell with one memberTopic about :Self.
mia:
  origin: "cat:SSN"
  creator: ":Self"
  memberCount: "cell:OneMember"
  subject: ":Self"
  memberTopics: "topic-23"
  topics:
    - id: "http://www.example.org/mia/topics/topic-23"
      claimant: ":Self"
      subject: ":Self"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
---

## Topics

<a id="topic-23"></a>
### Topic 23

#### Overview

This topic captures Alice Walker's Social Security Administration record. Alice self-enters her SSN (123-45-6788) from her physical Social Security card. The SSA is not a PDN node, so this data is self-claimed rather than received from the SSA directly.

#### Topic Graph

```turtle
<!-- databook:id: alice-ssa-topic-graph -->
<!-- databook:graph: http://www.example.org/mia/topics/topic-23#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Self rdfs:comment "Alice Walker's persona for her Social Security Administration record."@en ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → SSN
        rdf:type cco:ent00000008 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "123-45-6788"
    ] .
```
