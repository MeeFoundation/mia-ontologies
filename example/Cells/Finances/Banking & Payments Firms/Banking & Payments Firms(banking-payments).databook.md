---
id: http://www.example.org/mia/cells/cell-24
title: "Banking & Payments Firms"
type: cell-databook
version: 1.2.0
created: 2026-07-10
description: >
  Cell DataBook for folder "Banking & Payments Firms" (cell:category: cat:BankingPayments). It is a
  one-member cell with one member entry about :Self — a minimal stub,
  since "Banking & Payments Firms" is a purely organizational category node with no
  content or relationship of its own beyond Alice's required membership.
mia:
  category: "cat:BankingPayments"
  creator: ":Self"
  owner: ":Self"
  member: "graph-42"
  graphs:
    - id: "http://www.example.org/mia/graphs/graph-42"
      claimant: ":Self"
      subject: ":Self"
      template: "persona:JSContactCard"
---

## Graphs

<a id="graph-42"></a>
### Graph 42

#### Overview

This graph is the cell's one required `member` entry — a cell with a single `member` entry in the user's own category-cell tree always has `:Self` as that member (see Check 21), regardless of what the cell's `subject` is — here, Alice herself. The "Banking & Payments Firms" cell is a purely organizational category node (`cell:category: cat:BankingPayments`) with no relationship or subject of its own beyond Alice's required membership. Alice is both the claimant and the subject. It carries her given name, satisfying the `JSContactCardPersonShape` `ctpl:BankingPaymentsTemplateCell` sets as `cell:memberGraphShape` — no longer deliberately empty.

#### Graph

```turtle
<!-- databook:id: alice-banking-payments-member-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-42#graph -->
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
