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
  owner: ":Self"
  member: "graph-55"
  graphs:
    - id: "http://www.example.org/mia/graphs/graph-55"
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
