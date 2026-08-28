---
id: http://www.example.org/mia/cells/cell-20
title: "Cells"
type: cell-databook
version: 1.1.0
created: 2026-07-10
description: >
  Cell DataBook for folder "Cells" (cell:origin: cat:Person). It is a
  one-member cell with one member entry about :Self — a minimal stub,
  since "Cells" is a purely organizational category node with no
  content or relationship of its own beyond Alice's required membership.
mia:
  origin: "cat:Person"
  creator: ":Self"
  memberCount: "cell:OneMember"
  members: "graph-38"
  graphs:
    - id: "http://www.example.org/mia/graphs/graph-38"
      claimant: ":Self"
      subject: ":Self"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/graph/shapes
---

## Graphs

<a id="graph-38"></a>
### Graph 38

#### Overview

This graph is the cell's one required `members` entry — a `cell:OneMember` cell in the user's own category-cell tree always has `:Self` as its one member (see Check 21), regardless of what the cell's `subject` is — here, Alice herself. The "Cells" cell is a purely organizational category node (`cell:origin: cat:Person`) with no relationship or subject of its own beyond Alice's required membership, so this stub carries no further claims. Alice is both the claimant and the subject. Deliberately empty: the `members` requirement is about `g:subject`/`g:claimant` (asserted at the `mia.graphs[]` YAML level, not in this Turtle body), not about carrying any particular content — there is no rule requiring a member's graph to assert anything at all about them.

#### Graph

```turtle
<!-- databook:id: alice-cells-member-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-38#graph -->
```
