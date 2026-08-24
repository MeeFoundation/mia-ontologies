---
id: http://www.example.org/mia/cells/cell-21
title: "Affiliations"
type: cell-databook
version: 1.1.0
created: 2026-07-10
description: >
  Cell DataBook for folder "Affiliations" (cell:origin: cat:Affiliations). It is a
  one-member cell with one memberTopic about :Self — a minimal stub,
  since "Affiliations" is a purely organizational category node with no
  content or relationship of its own beyond Alice's required membership.
mia:
  origin: "cat:Affiliations"
  creator: ":Self"
  memberCount: "cell:OneMember"
  subject: ":Self"
  memberTopics: "topic-39"
  topics:
    - id: "http://www.example.org/mia/topics/topic-39"
      claimant: ":Self"
      subject: ":Self"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
---

## Topics

<a id="topic-39"></a>
### Topic 39

#### Overview

This topic is the cell's one required `memberTopics` entry — a `cell:OneMember` cell in the user's own category-cell tree always has `:Self` as its one member (see Check 21), regardless of what the cell's `subject` is — here, Alice herself. The "Affiliations" cell is a purely organizational category node (`cell:origin: cat:Affiliations`) with no relationship or subject of its own beyond Alice's required membership, so this stub carries no further claims. Alice is both the claimant and the subject. Deliberately empty: the `memberTopics` requirement is about `t:subject`/`t:claimant` (asserted at the `mia.topics[]` YAML level, not in this Turtle body), not about carrying any particular content — there is no rule requiring a member's topic to assert anything at all about them.

#### Topic Graph

```turtle
<!-- databook:id: alice-affiliations-member-topic-graph -->
<!-- databook:graph: http://www.example.org/mia/topics/topic-39#graph -->
```
