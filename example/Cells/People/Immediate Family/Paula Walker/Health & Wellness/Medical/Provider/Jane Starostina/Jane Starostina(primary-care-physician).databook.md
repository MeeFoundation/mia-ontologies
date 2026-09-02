---
id: http://www.example.org/mia/cells/cell-14
title: "Jane Starostina"
type: cell-databook
version: 1.3.0
created: 2026-07-10
description: >
  Cell DataBook for folder "Jane Starostina" (cell:category: cat:PrimaryCarePhysician). It is a one-member cell with one member entry about :Self and one graph about :Jane_Starostina (the cell's subject).
mia:
  category: "cat:PrimaryCarePhysician"
  creator: ":Self"
  owner: ":Self"
  member: "graph-34"
  topic: "graph-25"
  graphs:
    - id: "http://www.example.org/mia/graphs/graph-34"
      claimant: ":Self"
      subject: ":Self"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/graph/shapes
    - id: "http://www.example.org/mia/graphs/graph-25"
      claimant: ":Self"
      subject: ":Jane_Starostina"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/graph/shapes
---

## Graphs

<a id="graph-34"></a>
### Graph 34

#### Overview

This graph captures Alice's own bare identity claim (just her given name) — the cell's one required `member` entry, satisfying the single-member baseline. Alice is both the claimant and the subject.

#### Graph

```turtle
<!-- databook:id: alice-jane-starostina-member-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-34#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

:Self <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → GivenName
    rdf:type cco:ent00000002 ;  # GivenName
    <https://w3id.org/cco-domains/cco/ont00001765> "Alice"  # has text value
] .
```

<a id="graph-25"></a>
### Graph 25

#### Overview

This graph captures Alice's record of Dr. Jane Starostina, who is the primary care physician for Alice's mother, Paula Walker. Alice keeps this information so she and her sister Carol can coordinate Paula's medical appointments. Alice is the claimant; Jane is the cell's `subject` but, since this cell now has a real member entry (graph 34, above) about Alice herself, Jane's graph is linked via `cell:topic` rather than as one of the required `member` entries.

#### Graph

```turtle
<!-- databook:id: jane-starostina-alice-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-25#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Jane_Starostina rdf:type owl:NamedIndividual ,
               persona:Person ;
    rdfs:label "Jane Starostina (Primary Care Physician)"@en ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → GivenName
        rdf:type cco:ent00000002 ;  # GivenName
        <https://w3id.org/cco-domains/cco/ont00001765> "Jane"  # has text value
    ] ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → FamilyName
        rdf:type cco:ent00000004 ;  # FamilyName
        <https://w3id.org/cco-domains/cco/ont00001765> "Starostina"  # has text value
    ] ;

    <https://w3id.org/cco-domains/cco/ont00001917> [  # described by → Person Note
        rdf:type cco:ent00000048 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "Paula Walker's primary care physician"
    ] .
```
