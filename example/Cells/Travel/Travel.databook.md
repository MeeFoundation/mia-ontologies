---
id: http://www.example.org/mia/cells/cell-45
title: "Travel"
type: cell-databook
version: 1.0.0
created: 2026-08-30
description: >
  Cell DataBook for folder "Travel" (cell:category: cat:Travel). It is a one-member cell with one
  member entry about :Self — a minimal stub, since "Travel" is a purely organizational category
  node with no content or relationship of its own beyond Alice's required membership. Nested inside
  it is the "Kyoto Trip 2027" cell for a specific trip.
mia:
  category: "cat:Travel"
  creator: ":Self"
  owner: ":Self"
  member: "graph-64"
  graphs:
    - id: "http://www.example.org/mia/graphs/graph-64"
      claimant: ":Self"
      subject: ":Self"
---

## Graphs

<a id="graph-64"></a>
### Graph 64

#### Overview

This graph is the cell's one required `member` entry — a cell with a single `member` entry in the user's own category-cell tree always has `:Self` as that member (see Check 21), regardless of what the cell's `subject` is. The "Travel" cell is a purely organizational category node (`cell:category: cat:Travel`) with no relationship or subject of its own beyond Alice's required membership, so this stub carries no further claims. Alice is both the claimant and the subject. Deliberately empty: the `member` requirement is about `g:subject`/`g:claimant` (asserted at the `mia.graphs[]` YAML level, not in this Turtle body), not about carrying any particular content — there is no rule requiring a member's graph to assert anything at all about them.

#### Graph

```turtle
<!-- databook:id: alice-travel-member-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-64#graph -->
```
