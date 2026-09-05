---
id: http://www.example.org/mia/cells/cell-37
title: "Pets"
type: cell-databook
version: 1.2.0
created: 2026-08-21
description: >
  Cell DataBook for folder "Pets" (cell:category: cat:Pets). It is a
  one-member cell with one member entry about :Self — a minimal stub,
  since "Pets" is a purely organizational category node with no
  content or relationship of its own beyond Alice's required membership.
  Also carries an empty topic graph, required now that cat:Pets's own
  TemplateCell is isTopicCell: true (Check 31) — the real topic content
  lives in this category's own leaf cell (Ginger) instead.
mia:
  category: "cat:Pets"
  creator: ":Self"
  owner: ":Self"
  member:
    id: "http://www.example.org/mia/graphs/graph-55"
    claimant: ":Self"
    subject: ":Self"
    template: "pshapes:JSContactCardPersonShape"
  topic:
    id: "http://www.example.org/mia/graphs/graph-88"
    claimant: ":Self"
    subject: ":Self"
---

## Graphs

<a id="graph-55"></a>
### Graph 55

#### Overview

This graph is the cell's one required `member` entry — a cell with a single `member` entry in the user's own category-cell tree always has `:Self` as that member (see Check 21), regardless of what the cell's `subject` is — here, Alice herself. The "Pets" cell is a purely organizational category node (`cell:category: cat:Pets`) with no relationship or subject of its own beyond Alice's required membership. Alice is both the claimant and the subject. It carries her given name, satisfying the `JSContactCardPersonShape` `ctpl:PetProfileTemplateCell` sets as `cell:memberGraphShape` — no longer deliberately empty.

#### Graph

```turtle
<!-- databook:id: alice-pets-member-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-55#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .

:Self rdf:type owl:NamedIndividual ,
               persona:Person .

:Self <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → GivenName (JSContactCardPersonShape)
        rdf:type cco:ent00000002 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "Alice"
    ] .
```

<a id="graph-88"></a>
### Graph 88

#### Overview

This graph is the cell's required `topic` — required now that `cat:Pets`'s own `TemplateCell` is `isTopicCell: true` (Check 31), even though "Pets" is a purely organizational scaffold cell with no topic content of its own (the real content lives in this category's own leaf cell, Ginger, instead). Deliberately empty — no triples at all, per Check 32's own allowance. Alice is both the claimant and the subject.

#### Graph

```turtle
<!-- databook:id: alice-pets-topic-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-88#graph -->
```
