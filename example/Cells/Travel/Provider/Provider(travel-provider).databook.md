---
id: http://www.example.org/mia/cells/cell-51
title: "Provider"
type: cell-databook
version: 1.1.0
created: 2026-09-11
description: >
  Cell DataBook for folder "Provider" (cell:category: cat:TravelProvider). It is a
  one-member cell with one member entry about :Self — a minimal stub, since
  "Provider" is a purely organizational category node with no content or
  relationship of its own beyond Alice's required membership. It also carries the
  topic cat:TravelProvider's own TemplateCell now requires (cell:isTopicCell true),
  deliberately empty, since its real content lives in its own leaf cell (Hilton)
  instead.
mia:
  category: "cat:TravelProvider"
  creator: ":Self"
  owner: ":Self"
  member:
    id: "http://www.example.org/mia/graphs/graph-98"
    claimant: ":Self"
    subject: ":Self"
    template: "pshapes:ContactInfoShape"
  topic:
    id: "http://www.example.org/mia/graphs/graph-56"
    claimant: ":Self"
    subject: ":Self"
---

## Graphs

<a id="graph-98"></a>
### Graph 98

#### Overview

This graph is the cell's one required `member` entry — a cell with a single `member` entry in the user's own tree of cells always has `:Self` as that member (see Check 21), regardless of what the cell's subject is. The "Provider" cell is a purely organizational category node (`cell:category: cat:TravelProvider`) with no relationship or subject of its own beyond Alice's required membership, so this stub carries no further claims. Alice is both the claimant and the subject. It carries her given name, satisfying the `ContactInfoShape` `ctpl:TravelProviderTemplateCell` sets as `cell:memberGraphShape`.

#### Graph

```turtle
<!-- databook:id: alice-travel-provider-member-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-98#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

:Self rdf:type owl:NamedIndividual ,
               persona:Person .

:Self <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → GivenName (ContactInfoShape)
        rdf:type cco:ent00000002 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "Alice"
    ] .
```

<a id="graph-56"></a>
### Graph 56

#### Overview

This graph is the cell's required `topic` — required now that `cat:TravelProvider`'s own `TemplateCell` is `isTopicCell: true` (Check 31), even though "Provider" is a purely organizational scaffold cell with no topic content of its own (the real content lives in this category's own leaf cell, Hilton, instead). Deliberately empty — no triples at all, per Check 32's own allowance — and so carries no `template:` value either, the same as every other scaffold cell's empty topic. Alice is both the claimant and the subject.

#### Graph

```turtle
<!-- databook:id: alice-travel-provider-topic-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-56#graph -->
```
