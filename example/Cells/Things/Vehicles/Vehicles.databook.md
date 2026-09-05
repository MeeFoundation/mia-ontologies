---
id: http://www.example.org/mia/cells/cell-43
title: "Vehicles"
type: cell-databook
version: 1.1.0
created: 2026-08-29
description: >
  Cell DataBook for folder "Vehicles" (cell:category: cat:Vehicles), nested under "Things". It is a
  one-member cell with one member entry about :Self — a minimal stub, since "Vehicles" is a purely
  organizational category node with no content or relationship of its own beyond Alice's required
  membership. Also carries an empty topic graph, required now that cat:Vehicles's own TemplateCell
  is isTopicCell: true (Check 31) — the real topic content lives in this category's own leaf cell
  (RAV4) instead.
mia:
  category: "cat:Vehicles"
  creator: ":Self"
  owner: ":Self"
  member:
    id: "http://www.example.org/mia/graphs/graph-61"
    claimant: ":Self"
    subject: ":Self"
    template: "persona:JSContactCard"
  topic:
    id: "http://www.example.org/mia/graphs/graph-89"
    claimant: ":Self"
    subject: ":Self"
---

## Graphs

<a id="graph-61"></a>
### Graph 61

#### Overview

This graph is the cell's one required `member` entry — a cell with a single `member` entry in the user's own category-cell tree always has `:Self` as that member (see Check 21), regardless of what the cell's `subject` is — here, Alice herself. The "Vehicles" cell is a purely organizational category node (`cell:category: cat:Vehicles`) with no relationship or subject of its own beyond Alice's required membership. Alice is both the claimant and the subject. It carries her given name, satisfying the `JSContactCardPersonShape` `ctpl:VehicleProfileTemplateCell` sets as `cell:memberGraphShape` — no longer deliberately empty.

#### Graph

```turtle
<!-- databook:id: alice-vehicles-member-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-61#graph -->
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

<a id="graph-89"></a>
### Graph 89

#### Overview

This graph is the cell's required `topic` — required now that `cat:Vehicles`'s own `TemplateCell` is `isTopicCell: true` (Check 31), even though "Vehicles" is a purely organizational scaffold cell with no topic content of its own (the real content lives in this category's own leaf cell, RAV4, instead). Deliberately empty — no triples at all, per Check 32's own allowance. Alice is both the claimant and the subject.

#### Graph

```turtle
<!-- databook:id: alice-vehicles-topic-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-89#graph -->
```
