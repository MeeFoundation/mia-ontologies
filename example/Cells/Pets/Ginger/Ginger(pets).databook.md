---
id: http://www.example.org/mia/cells/cell-41
title: "Ginger"
type: cell-databook
version: 1.1.0
created: 2026-08-22
description: >
  Cell DataBook for folder "Ginger" (cell:origin: cat:Pets). A user-defined instance folder for Alice's specific cat, Ginger, nested under the generic Pets category — mirroring how e.g. "Bob Johnson" reuses its parent "Others" folder's own origin class rather than being Custom. It is a one-member cell with one member entry about :Self and one graph about :Ginger (the cell's subject).
mia:
  origin: "cat:Pets"
  creator: ":Self"
  memberCount: "cell:OneMember"
  members: "graph-36"
  topic: "graph-37"
  graphs:
    - id: "http://www.example.org/mia/graphs/graph-36"
      claimant: ":Self"
      subject: ":Self"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/graph/shapes
    - id: "http://www.example.org/mia/graphs/graph-37"
      claimant: ":Self"
      subject: ":Ginger"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/graph/shapes
---

## Graphs

<a id="graph-36"></a>
### Graph 36

#### Overview

This graph is the cell's one required `members` entry — a `cell:OneMember` cell in the user's own category-cell tree always has `:Self` as its one member (see Check 21), regardless of what the cell's `subject` is — here, Ginger herself. Alice is both the claimant and the subject. Deliberately empty: the `members` requirement is about `g:subject`/`g:claimant` (asserted at the `mia.graphs[]` YAML level, not in this Turtle body), not about carrying any particular content — there is no rule requiring a member's graph to assert anything at all about them.

#### Graph

```turtle
<!-- databook:id: alice-ginger-member-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-36#graph -->
```

<a id="graph-37"></a>
### Graph 37

#### Overview

This graph captures Alice's basic claim about Ginger herself — just enough to back the cell's `subject: ":Ginger"` with a real graph (see Check 22). Ginger's actual medical care and her day-to-day care & feeding instructions live in the nested Medical and Care & Feeding cells instead; this is a minimal, standalone identification.

#### Graph

```turtle
<!-- databook:id: alice-ginger-subject-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-37#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Ginger rdf:type owl:NamedIndividual ;
    rdfs:label "Ginger (Alice's cat)"@en .
```
