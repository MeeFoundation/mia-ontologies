---
id: http://www.example.org/mia/categories/Social-Security-Administration(ssa)
title: "Social Security Administration"
type: cell-databook
version: 1.1.0
created: 2026-07-10
description: >
  Cell DataBook of category "Social Security Administration" (cell:origin: cat:SSA). Content may include topics/folder/note links, and may carry one or two required subject values.
mia:
  origin: "cat:SSA"
  creator: ":Self"
  memberCount: "cell:OneMember"
  subject: ":Self"
  memberTopics: "https://www.example.org/mia/topics/self.self(Social-Security-Administration)(ssa)(23)"
  topics:
    - id: "https://www.example.org/mia/topics/self.self(Social-Security-Administration)(ssa)(23)"
      title: "About Alice Walker in the Federal cell as claimed by Alice Walker"
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

<a id="topic-23"></a>
### Topic 23 — About Alice Walker in the Federal cell as claimed by Alice Walker

#### Overview

This topic captures Alice Walker's Social Security Administration record. Alice self-enters her SSN (123-45-6788) from her physical Social Security card. The SSA is not a PDN node, so this data is self-claimed rather than received from the SSA directly.

#### Topic Graph

```turtle
<!-- databook:id: alice-ssa-topic-graph -->
<!-- databook:graph: https://www.example.org/mia/topics/self.self(Social-Security-Administration)(ssa)(23)#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Self rdfs:comment "Alice Walker's persona for her Social Security Administration record."@en ;

    <https://purl.org/cco/ont00001879> [  # designated by → SSN
        rdf:type cco:ent00000008 ;
        <https://purl.org/cco/ont00001765> "123-45-6788"
    ] .
```
