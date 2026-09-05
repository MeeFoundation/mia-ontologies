---
id: http://www.example.org/mia/cells/cell-31
title: "Medical"
type: cell-databook
version: 1.1.0
created: 2026-07-10
description: >
  Cell DataBook for folder "Medical" (cell:category: cat:Medical). It is a
  one-member cell with one member entry about :Self — a minimal stub,
  since "Medical" is a purely organizational category node with no
  content or relationship of its own beyond Alice's required membership.
mia:
  category: "cat:Medical"
  creator: ":Self"
  owner: ":Self"
  member: "graph-49"
  graphs:
    - id: "http://www.example.org/mia/graphs/graph-49"
      claimant: ":Self"
      subject: ":Self"
      template: "persona:JSContactCard"
---

## Graphs

<a id="graph-49"></a>
### Graph 49

#### Overview

This graph is the cell's one required `member` entry — a cell with a single `member` entry in the user's own category-cell tree always has `:Self` as that member (see Check 21), regardless of what the cell's `subject` is — here, Alice herself. The "Medical" cell is a purely organizational category node (`cell:category: cat:Medical`) with no relationship or subject of its own beyond Alice's required membership, so this stub carries no further claims. Alice is both the claimant and the subject. It carries her given name, satisfying the `JSContactCardPersonShape` `ctpl:MedicalTemplateCell` sets as `cell:memberGraphShape` — no longer deliberately empty.

#### Graph

```turtle
<!-- databook:id: alice-medical-member-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-49#graph -->
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
