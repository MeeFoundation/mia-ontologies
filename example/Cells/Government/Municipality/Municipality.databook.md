---
id: http://www.example.org/mia/cells/cell-27
title: "Municipality"
type: cell-databook
version: 1.1.0
created: 2026-07-10
description: >
  Cell DataBook for folder "Municipality" (cell:category: cat:Municipality). It is a
  one-member cell with one member entry about :Self — a minimal stub,
  since "Municipality" is a purely organizational category node with no
  content or relationship of its own beyond Alice's required membership.
mia:
  category: "cat:Municipality"
  creator: ":Self"
  owner: ":Self"
  member: "graph-45"
  graphs:
    - id: "http://www.example.org/mia/graphs/graph-45"
      claimant: ":Self"
      subject: ":Self"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/graph/shapes
---

## Graphs

<a id="graph-45"></a>
### Graph 45

#### Overview

This graph is the cell's one required `member` entry — a cell with a single `member` entry in the user's own category-cell tree always has `:Self` as that member (see Check 21), regardless of what the cell's `subject` is — here, Alice herself. The "Municipality" cell is a purely organizational category node (`cell:category: cat:Municipality`) with no relationship or subject of its own beyond Alice's required membership, so this stub carries no further claims. Alice is both the claimant and the subject. Deliberately empty: the `member` requirement is about `g:subject`/`g:claimant` (asserted at the `mia.graphs[]` YAML level, not in this Turtle body), not about carrying any particular content — there is no rule requiring a member's graph to assert anything at all about them.

#### Graph

```turtle
<!-- databook:id: alice-municipality-member-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-45#graph -->
```
