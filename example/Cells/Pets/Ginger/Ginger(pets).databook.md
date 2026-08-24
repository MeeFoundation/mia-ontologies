---
id: http://www.example.org/mia/cells/cell-41
title: "Ginger"
type: cell-databook
version: 1.1.0
created: 2026-08-22
description: >
  Cell DataBook for folder "Ginger" (cell:origin: cat:Pets). A user-defined instance folder for Alice's specific cat, Ginger, nested under the generic Pets category — mirroring how e.g. "Bob Johnson" reuses its parent "Others" folder's own origin class rather than being Custom. It is a one-member cell with one memberTopic about :Self and one otherTopic about :Ginger (the cell's subject).
mia:
  origin: "cat:Pets"
  creator: ":Self"
  memberCount: "cell:OneMember"
  memberTopics: "topic-36"
  otherTopics: "topic-37"
  topics:
    - id: "http://www.example.org/mia/topics/topic-36"
      claimant: ":Self"
      subject: ":Self"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
    - id: "http://www.example.org/mia/topics/topic-37"
      claimant: ":Self"
      subject: ":Ginger"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
---

## Topics

<a id="topic-36"></a>
### Topic 36

#### Overview

This topic is the cell's one required `memberTopics` entry — a `cell:OneMember` cell in the user's own category-cell tree always has `:Self` as its one member (see Check 21), regardless of what the cell's `subject` is — here, Ginger herself. Alice is both the claimant and the subject. Deliberately empty: the `memberTopics` requirement is about `t:subject`/`t:claimant` (asserted at the `mia.topics[]` YAML level, not in this Turtle body), not about carrying any particular content — there is no rule requiring a member's topic to assert anything at all about them.

#### Topic Graph

```turtle
<!-- databook:id: alice-ginger-member-topic-graph -->
<!-- databook:graph: http://www.example.org/mia/topics/topic-36#graph -->
```

<a id="topic-37"></a>
### Topic 37

#### Overview

This topic captures Alice's basic claim about Ginger herself — just enough to back the cell's `subject: ":Ginger"` with a real topic (see Check 22). Ginger's actual medications live in the nested Medications cell instead; this is a minimal, standalone identification.

#### Topic Graph

```turtle
<!-- databook:id: alice-ginger-subject-topic-graph -->
<!-- databook:graph: http://www.example.org/mia/topics/topic-37#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Ginger rdf:type owl:NamedIndividual ;
    rdfs:label "Ginger (Alice's cat)"@en .
```
