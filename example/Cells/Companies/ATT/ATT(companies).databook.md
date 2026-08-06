---
id: http://www.example.org/mia/categories/ATT(companies)
title: "AT&T"
type: cell-databook
version: 1.1.0
created: 2026-07-10
description: >
  Cell DataBook of category "AT&T" (cell:origin: cat:Companies). Content may include topics/folder/note links, and may carry one or two required subject values.
mia:
  origin: "cat:Companies"
  creator: ":Self"
  memberCount: "cell:OneMember"
  subject: ":Self"
  memberTopics: "https://www.example.org/mia/topics/self.self(ATT)(companies)(11)"
  topics:
    - id: "https://www.example.org/mia/topics/self.self(ATT)(companies)(11)"
      title: "About Alice Walker in the Companies cell as claimed by Alice Walker"
      claimant: ":Self"
      subject: ":Self"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
      process:
        transformer: human
        timestamp: 2026-06-19T00:00:00Z
        agent:
          name: Paul Trevithick
          role: author
---

## Topics

<a id="topic-11"></a>
### Topic 11 — About Alice Walker in the Companies cell as claimed by Alice Walker

#### Overview

This topic captures Alice Walker's AT&T account topic. Alice self-enters her mobile phone number (+15108149999, E.164 format). AT&T is not a PDN node, so Alice records this data herself rather than receiving it from AT&T.

#### Topic Graph

```turtle
<!-- databook:id: alice-att-topic-graph -->
<!-- databook:graph: https://www.example.org/mia/topics/self.self(ATT)(companies)(11)#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Self <https://purl.org/cco/ont00001879> [  # designated by → Phone
        rdf:type cco:ent00000023 ;
        <https://purl.org/cco/ont00001765> "+15108149999" ;
        rdfs:comment "E.164 format (international standard)"@en
    ] .
```
