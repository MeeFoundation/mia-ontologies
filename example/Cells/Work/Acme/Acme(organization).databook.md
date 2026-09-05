---
id: http://www.example.org/mia/cells/cell-35
title: "Acme"
type: cell-databook
version: 1.1.0
created: 2026-07-10
description: >
  Cell DataBook for folder "Acme" (cell:category: cat:Organization). It is a
  one-member cell with one member entry about :Self — a minimal stub,
  since "Acme" is a purely organizational category node with no
  content or relationship of its own beyond Alice's required membership.
mia:
  category: "cat:Organization"
  creator: ":Self"
  owner: ":Self"
  member:
    id: "http://www.example.org/mia/graphs/graph-53"
    claimant: ":Self"
    subject: ":Self"
---

## Graphs

<a id="graph-53"></a>
### Graph 53

#### Overview

This graph is the cell's one required `member` entry — a cell with a single `member` entry in the user's own category-cell tree always has `:Self` as that member (see Check 21), regardless of what the cell's `subject` is — here, Alice herself. The "Acme" cell is a purely organizational category node (`cell:category: cat:Organization`) with no relationship or subject of its own beyond Alice's required membership, so this stub carries no further claims. Alice is both the claimant and the subject. Deliberately empty: the `member` requirement is about `g:subject`/`g:claimant` (asserted at the `mia.member[]`/`mia.topic[]` YAML level, not in this Turtle body), not about carrying any particular content — there is no rule requiring a member's graph to assert anything at all about them.

#### Graph

```turtle
<!-- databook:id: alice-acme-member-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-53#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .

:Self rdf:type owl:NamedIndividual ,
               persona:Person .

:Self <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → GivenName
        rdf:type cco:ent00000002 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "Alice"
    ] .
```
