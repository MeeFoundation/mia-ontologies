---
id: http://www.example.org/mia/cells/cell-30
title: "Immediate Family"
type: cell-databook
version: 1.1.0
created: 2026-07-10
description: >
  Cell DataBook for folder "Immediate Family" (cell:origin: cat:ImmediateFamily). It is a
  one-member cell with one memberTopic about :Self — a minimal stub,
  since "Immediate Family" is a purely organizational category node with no
  content or relationship of its own beyond Alice's required membership.
mia:
  origin: "cat:ImmediateFamily"
  creator: ":Self"
  memberCount: "cell:OneMember"
  memberTopics: "topic-48"
  topics:
    - id: "http://www.example.org/mia/topics/topic-48"
      claimant: ":Self"
      subject: ":Self"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
---

## Topics

<a id="topic-48"></a>
### Topic 48

#### Overview

This topic is the cell's one required `memberTopics` entry — a `cell:OneMember` cell in the user's own category-cell tree always has `:Self` as its one member (see Check 21), regardless of what the cell's `subject` is — here, Alice herself. The "Immediate Family" cell is a purely organizational category node (`cell:origin: cat:ImmediateFamily`) with no relationship or subject of its own beyond Alice's required membership, so this stub carries no further claims. Alice is both the claimant and the subject. Deliberately empty: the `memberTopics` requirement is about `t:subject`/`t:claimant` (asserted at the `mia.topics[]` YAML level, not in this Turtle body), not about carrying any particular content — there is no rule requiring a member's topic to assert anything at all about them.

#### Topic Graph

```turtle
<!-- databook:id: alice-immediate-family-member-topic-graph -->
<!-- databook:graph: http://www.example.org/mia/topics/topic-48#graph -->
```
