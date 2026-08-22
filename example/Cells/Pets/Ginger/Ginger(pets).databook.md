---
id: http://www.example.org/mia/cells/cell-41
title: "Ginger"
type: cell-databook
version: 1.0.0
created: 2026-08-22
description: >
  Cell DataBook for folder "Ginger" (cell:origin: cat:Pets). A user-defined instance folder for Alice's specific cat, Ginger, nested under the generic Pets category — mirroring how e.g. "Bob Johnson" reuses its parent "Others" folder's own origin class rather than being Custom. It is a one-member cell with one memberTopic about :Self and no otherTopics, so its subject is :Self (Ginger herself has no topic anywhere in this cell — her own record lives in the nested Medications cell instead).
mia:
  origin: "cat:Pets"
  creator: ":Self"
  memberCount: "cell:OneMember"
  subject: ":Self"
  memberTopics: "topic-36"
  topics:
    - id: "http://www.example.org/mia/topics/topic-36"
      claimant: ":Self"
      subject: ":Self"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
---

## Topics

<a id="topic-36"></a>
### Topic 36

#### Overview

This topic captures Alice's own bare identity claim (just her given name) — the cell's one required `memberTopics` entry. A `cell:OneMember` cell in the user's own category-cell tree always has `:Self` as its one member (see Check 21), regardless of what the cell's `subject` is — here, Ginger herself. Alice is both the claimant and the subject.

#### Topic Graph

```turtle
<!-- databook:id: alice-ginger-member-topic-graph -->
<!-- databook:graph: http://www.example.org/mia/topics/topic-36#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

:Self <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → GivenName
    rdf:type cco:ent00000002 ;  # GivenName
    <https://w3id.org/cco-domains/cco/ont00001765> "Alice"  # has text value
] .
```
