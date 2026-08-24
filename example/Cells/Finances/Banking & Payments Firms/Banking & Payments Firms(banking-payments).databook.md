---
id: http://www.example.org/mia/cells/cell-24
title: "Banking & Payments Firms"
type: cell-databook
version: 1.2.0
created: 2026-07-10
description: >
  Cell DataBook for folder "Banking & Payments Firms" (cell:origin: cat:BankingPayments). It is a
  one-member cell with one memberTopic about :Self — a minimal stub,
  since "Banking & Payments Firms" is a purely organizational category node with no
  content or relationship of its own beyond Alice's required membership.
mia:
  origin: "cat:BankingPayments"
  creator: ":Self"
  memberCount: "cell:OneMember"
  memberTopics: "topic-42"
  topics:
    - id: "http://www.example.org/mia/topics/topic-42"
      claimant: ":Self"
      subject: ":Self"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
---

## Topics

<a id="topic-42"></a>
### Topic 42

#### Overview

This topic is the cell's one required `memberTopics` entry — a `cell:OneMember` cell in the user's own category-cell tree always has `:Self` as its one member (see Check 21), regardless of what the cell's `subject` is — here, Alice herself. The "Banking & Payments Firms" cell is a purely organizational category node (`cell:origin: cat:BankingPayments`) with no relationship or subject of its own beyond Alice's required membership, so this stub carries no further claims. Alice is both the claimant and the subject. Deliberately empty: the `memberTopics` requirement is about `t:subject`/`t:claimant` (asserted at the `mia.topics[]` YAML level, not in this Turtle body), not about carrying any particular content — there is no rule requiring a member's topic to assert anything at all about them.

#### Topic Graph

```turtle
<!-- databook:id: alice-banking-payments-member-topic-graph -->
<!-- databook:graph: http://www.example.org/mia/topics/topic-42#graph -->
```
