---
id: http://www.example.org/mia/categories/Google(companies)
title: "Google"
type: cell-databook
version: 1.1.0
created: 2026-07-10
description: >
  Cell DataBook of category "Google" (cell:origin: cat:Companies). May carry one or two required subject values.
mia:
  origin: "cat:Companies"
  creator: ":Self"
  memberCount: "cell:OneMember"
  subject: ":Self"
  memberTopics: "self.self(Google)(companies)(16)"
  topics:
    - id: "http://www.example.org/mia/topics/self.self(Google)(companies)(16)"
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

<a id="topic-16"></a>
### Topic 16 — About Alice Walker in the Companies cell as claimed by Alice Walker

#### Overview

This topic captures Alice Walker's Google account topic. Alice self-enters her Gmail address (awalker@gmail.com). Google is not a PDN node, so Alice records this data herself rather than receiving it from Google.

#### Topic Graph

```turtle
<!-- databook:id: alice-google-topic-graph -->
<!-- databook:graph: http://www.example.org/mia/topics/self.self(Google)(companies)(16)#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Self <https://purl.org/cco/ont00001879> [  # designated by → Email
        rdf:type cco:ent00000024 ;
        <https://purl.org/cco/ont00001765> "awalker@gmail.com"
    ] .
```
