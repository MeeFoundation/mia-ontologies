---
id: http://www.example.org/mia/cells/cell-35
title: "Acme"
type: cell-databook
version: 1.1.0
created: 2026-07-10
description: >
  Cell DataBook for folder "Acme" (cell:origin: cat:Organization). It is a
  one-member cell with one member entry about :Self — a minimal stub,
  since "Acme" is a purely organizational category node with no
  content or relationship of its own beyond Alice's required membership.
mia:
  origin: "cat:Organization"
  creator: ":Self"
  members: "graph-53"
  graphs:
    - id: "http://www.example.org/mia/graphs/graph-53"
      claimant: ":Self"
      subject: ":Self"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/graph/shapes
---

## Graphs

<a id="graph-53"></a>
### Graph 53

#### Overview

This graph is the cell's one required `members` entry — a cell with a single `members` entry in the user's own category-cell tree always has `:Self` as that member (see Check 21), regardless of what the cell's `subject` is — here, Alice herself. The "Acme" cell is a purely organizational category node (`cell:origin: cat:Organization`) with no relationship or subject of its own beyond Alice's required membership, so this stub carries no further claims. Alice is both the claimant and the subject. Deliberately empty: the `members` requirement is about `g:subject`/`g:claimant` (asserted at the `mia.graphs[]` YAML level, not in this Turtle body), not about carrying any particular content — there is no rule requiring a member's graph to assert anything at all about them.

#### Graph

```turtle
<!-- databook:id: alice-acme-member-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-53#graph -->
```
