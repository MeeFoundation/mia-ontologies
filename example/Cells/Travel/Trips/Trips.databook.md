---
id: http://www.example.org/mia/cells/cell-46
title: "Trips"
type: cell-databook
version: 1.0.0
created: 2026-08-30
description: >
  Cell DataBook for folder "Trips" (cell:origin: cat:Trips), nested under "Travel". It is a
  one-member cell with one member entry about :Self — a minimal stub, since "Trips" is a purely
  organizational category node with no content or relationship of its own beyond Alice's required
  membership. Nested inside it is the "Kyoto Trip 2027" cell for a specific trip.
mia:
  origin: "cat:Trips"
  creator: ":Self"
  members: "graph-65"
  graphs:
    - id: "http://www.example.org/mia/graphs/graph-65"
      claimant: ":Self"
      subject: ":Self"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/graph/shapes
---

## Graphs

<a id="graph-65"></a>
### Graph 65

#### Overview

This graph is the cell's one required `members` entry — a cell with a single `members` entry in the user's own category-cell tree always has `:Self` as that member (see Check 21), regardless of what the cell's `subject` is. The "Trips" cell is a purely organizational category node (`cell:origin: cat:Trips`) with no relationship or subject of its own beyond Alice's required membership, so this stub carries no further claims. Alice is both the claimant and the subject. Deliberately empty: the `members` requirement is about `g:subject`/`g:claimant` (asserted at the `mia.graphs[]` YAML level, not in this Turtle body), not about carrying any particular content — there is no rule requiring a member's graph to assert anything at all about them.

#### Graph

```turtle
<!-- databook:id: alice-trips-member-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-65#graph -->
```
