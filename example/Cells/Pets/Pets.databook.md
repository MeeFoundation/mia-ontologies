---
id: http://www.example.org/mia/cells/cell-37
title: "Pets"
type: cell-databook
version: 1.1.0
created: 2026-08-21
description: >
  Cell DataBook for folder "Pets" (cell:category: cat:Pets). It is a
  one-member cell with one member entry about :Self — a minimal stub,
  since "Pets" is a purely organizational category node with no
  content or relationship of its own beyond Alice's required membership.
mia:
  category: "cat:Pets"
  creator: ":Self"
  members: "graph-55"
  graphs:
    - id: "http://www.example.org/mia/graphs/graph-55"
      claimant: ":Self"
      subject: ":Self"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/graph/shapes
---

## Graphs

<a id="graph-55"></a>
### Graph 55

#### Overview

This graph is the cell's one required `members` entry — a cell with a single `members` entry in the user's own category-cell tree always has `:Self` as that member (see Check 21), regardless of what the cell's `subject` is — here, Alice herself. The "Pets" cell is a purely organizational category node (`cell:category: cat:Pets`) with no relationship or subject of its own beyond Alice's required membership, so this stub carries no further claims. Alice is both the claimant and the subject. Deliberately empty: the `members` requirement is about `g:subject`/`g:claimant` (asserted at the `mia.graphs[]` YAML level, not in this Turtle body), not about carrying any particular content — there is no rule requiring a member's graph to assert anything at all about them.

#### Graph

```turtle
<!-- databook:id: alice-pets-member-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-55#graph -->
```
