---
id: http://www.example.org/mia/cells/cell-12
title: "Paula Walker"
type: cell-databook
version: 1.1.0
created: 2026-07-10
description: >
  Cell DataBook for folder "Paula Walker" (cell:category: cat:ImmediateFamily). It is a two-member cell with three members (two about :Paula_Walker and one about :Self).
mia:
  category: "cat:ImmediateFamily"
  creator: ":Self"
  owner: ":Self"
  member:
    - "graph-05"
    - "graph-21"
    - "graph-07"
  graphs:
    - id: "http://www.example.org/mia/graphs/graph-05"
      claimant: ":Paula_Walker"
      subject: ":Paula_Walker"
    - id: "http://www.example.org/mia/graphs/graph-07"
      claimant: ":Self"
      subject: ":Paula_Walker"
    - id: "http://www.example.org/mia/graphs/graph-21"
      claimant: ":Self"
      subject: ":Self"
---

## Graphs

<a id="graph-05"></a>
### Graph 05

#### Overview

This graph captures Paula Walker's self-claimed family persona as transmitted from Paula's own instance of the app to Alice's over the PDN, plus her given name, required by the `JSContactCardPersonShape` every templated cell's `member` content is now expected to conform to (`cell:memberGraphShape`). Paula is the claimant.

#### Graph

```turtle
<!-- databook:id: paula-family-paula-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-05#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Paula_Walker rdf:type owl:NamedIndividual ,
               persona:Person ;
    rdfs:label "Paula Walker (Family) self-claimed"@en ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → GivenName (JSContactCardPersonShape)
        rdf:type cco:ent00000002 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "Paula"
    ] .
```

<a id="graph-07"></a>
### Graph 07

#### Overview

This graph captures Alice's record of her family member Paula Walker. Alice claims Paula's name in the family graph. Alice is the claimant.

#### Graph

```turtle
<!-- databook:id: paula-family-alice-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-07#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Paula_Walker rdf:type owl:NamedIndividual ,
               persona:Person ;
    rdfs:label "Paula Walker (Family)"@en ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → GivenName
        rdf:type cco:ent00000002 ;  # GivenName
        <https://w3id.org/cco-domains/cco/ont00001765> "Paula"  # has text value
    ] ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → FamilyName
        rdf:type cco:ent00000004 ;  # FamilyName
        <https://w3id.org/cco-domains/cco/ont00001765> "Walker"  # has text value
    ] .
```

<a id="graph-21"></a>
### Graph 21

#### Overview

This graph captures Alice Walker's family relationships. It records her maternal relationship with Paula Walker and her family social network, which includes Paula Walker and Carol Walker (Alice's sister) as members, plus her own given name, required by the `JSContactCardPersonShape` every templated cell's `member` content is now expected to conform to (`cell:memberGraphShape`). Paula's own family graph (`graph-05`) is the peer record in this relationship; Carol's own claimed record about their mother appears separately in the "Medical Appointment" cell (graph 28). Alice is the claimant.

#### Graph

```turtle
<!-- databook:id: alice-family-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-21#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Self rdf:type owl:NamedIndividual ,
               persona:Person .

:Self rdfs:comment "Alice Walker's persona for her family relationships."@en ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → GivenName (JSContactCardPersonShape)
        rdf:type cco:ent00000002 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "Alice"
    ] ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → AlternateName
        rdf:type cco:ent00000006 ;  # AlternateName
        <https://w3id.org/cco-domains/cco/ont00001765> "Alice Walker"
    ] ;

    cco:ont00001780 :Paula_Walker ;  # has mother

    persona:hasSocialNetwork :Alice_Family_Network .


:Alice_Family_Network rdf:type owl:NamedIndividual ,
                               cco:ont00001183 ;  # Social Network
    rdfs:label "Alice Walker's family connections"@en ;
    <http://purl.obolibrary.org/obo/BFO_0000115> :Paula_Walker ,  # has member part
                                                  :Carol_Walker .  # has member part (Alice's sister)
```
