---
id: http://www.example.org/mia/cells/cell-03
title: "Google"
type: cell-databook
version: 1.1.0
created: 2026-07-10
description: >
  Cell DataBook for folder "Google" (cell:origin: cat:Companies). It is a one-member cell with one memberTopic about :Self.
mia:
  origin: "cat:Companies"
  creator: ":Self"
  memberCount: "cell:OneMember"
  memberTopics: "topic-16"
  topics:
    - id: "http://www.example.org/mia/topics/topic-16"
      claimant: ":Self"
      subject: ":Self"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
---

## Topics

<a id="topic-16"></a>
### Topic 16

#### Overview

This topic captures Alice Walker's Google account topic. Alice self-enters her Gmail address (awalker@gmail.com). Google is not a PDN node, so Alice records this data herself rather than receiving it from Google. Alice is the claimant.

#### Topic Graph

```turtle
<!-- databook:id: alice-google-topic-graph -->
<!-- databook:graph: http://www.example.org/mia/topics/topic-16#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Self <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → Email
        rdf:type cco:ent00000024 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "awalker@gmail.com"
    ] .
```
