---
id: http://www.example.org/mia/cells/cell-49
title: "Previous"
type: cell-databook
version: 1.0.0
created: 2026-09-03
description: >
  Cell DataBook for folder "Previous" (cell:category: cat:Previous). It is a
  one-member cell with one member entry about :Self — a minimal stub,
  since "Previous" is a purely organizational category node with no
  content or relationship of its own beyond Alice's required membership.
mia:
  category: "cat:Previous"
  creator: ":Self"
  owner: ":Self"
  member: "graph-72"
  graphs:
    - id: "http://www.example.org/mia/graphs/graph-72"
      claimant: ":Self"
      subject: ":Self"
---

## Graphs

<a id="graph-72"></a>
### Graph 72

#### Overview

This graph is the cell's one required `member` entry — a cell with a single `member` entry in the user's own category-cell tree always has `:Self` as that member (see Check 21), regardless of what the cell's `subject` is — here, Alice herself. The "Previous" cell is a purely organizational category node (`cell:category: cat:Previous`) with no relationship or subject of its own beyond Alice's required membership, so this stub carries no further claims. Alice is both the claimant and the subject. Deliberately empty: the `member` requirement is about `g:subject`/`g:claimant` (asserted at the `mia.graphs[]` YAML level, not in this Turtle body), not about carrying any particular content — there is no rule requiring a member's graph to assert anything at all about them.

#### Graph

```turtle
<!-- databook:id: alice-previous-member-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-72#graph -->
```
