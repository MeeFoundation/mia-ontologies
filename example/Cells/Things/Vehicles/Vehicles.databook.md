---
id: http://www.example.org/mia/cells/cell-43
title: "Vehicles"
type: cell-databook
version: 1.0.0
created: 2026-08-29
description: >
  Cell DataBook for folder "Vehicles" (cell:category: cat:Vehicles), nested under "Things". It is a
  one-member cell with one member entry about :Self — a minimal stub, since "Vehicles" is a purely
  organizational category node with no content or relationship of its own beyond Alice's required
  membership.
mia:
  category: "cat:Vehicles"
  creator: ":Self"
  owner: ":Self"
  member: "graph-61"
  graphs:
    - id: "http://www.example.org/mia/graphs/graph-61"
      claimant: ":Self"
      subject: ":Self"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/graph/shapes
---

## Graphs

<a id="graph-61"></a>
### Graph 61

#### Overview

This graph is the cell's one required `member` entry — a cell with a single `member` entry in the user's own category-cell tree always has `:Self` as that member (see Check 21), regardless of what the cell's `subject` is — here, Alice herself. The "Vehicles" cell is a purely organizational category node (`cell:category: cat:Vehicles`) with no relationship or subject of its own beyond Alice's required membership, so this stub carries no further claims. Alice is both the claimant and the subject. Deliberately empty: the `member` requirement is about `g:subject`/`g:claimant` (asserted at the `mia.graphs[]` YAML level, not in this Turtle body), not about carrying any particular content — there is no rule requiring a member's graph to assert anything at all about them.

#### Graph

```turtle
<!-- databook:id: alice-vehicles-member-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-61#graph -->
```
