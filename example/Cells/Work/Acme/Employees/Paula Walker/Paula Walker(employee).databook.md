---
id: http://www.example.org/mia/cells/cell-19
title: "Paula Walker"
type: cell-databook
version: 1.2.0
created: 2026-07-10
description: >
  Cell DataBook for folder "Paula Walker" (cell:category: cat:Employee). It is a two-member cell with member entries about :Self and :Paula_Walker.
mia:
  category: "cat:Employee"
  creator: ":Self"
  owner: ":Self"
  member:
    - id: "http://www.example.org/mia/graphs/graph-20"
      claimant: ":Self"
      subject: ":Self"
      template: "persona:JSContactCard"
    - id: "http://www.example.org/mia/graphs/graph-06"
      claimant: ":Self"
      subject: ":Paula_Walker"
      template: "persona:JSContactCard"
---

## Graphs

<a id="graph-06"></a>
### Graph 06

#### Overview

This graph captures Alice's record of her colleague Paula Walker in their shared Acme employment graph — one of the cell's two required `member` entries, satisfying `JSContactCardPersonShape`'s required GivenName alongside her existing `rdfs:label` (`cat:Employee` reverted to `isTopicCell: false`, so this content moved here from `cell:topic`, per Check 32's resolution). Alice is the claimant.

#### Graph

```turtle
<!-- databook:id: paula-acme-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-06#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Paula_Walker rdf:type owl:NamedIndividual ,
               persona:Person ;
    rdfs:label "Paula Walker (Acme)"@en ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → GivenName (JSContactCardPersonShape)
        rdf:type cco:ent00000002 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "Paula"
    ] .
```

<a id="graph-20"></a>
### Graph 20

#### Overview

This graph captures Alice Walker's employee identity at Acme. It records her work email address (alice@acme.com) and her Acme social network, which includes colleague Paula Walker. Alice is the claimant.

#### Graph

```turtle
<!-- databook:id: alice-acme-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-20#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Self rdf:type owl:NamedIndividual ,
               persona:Person .

:Paula_Walker rdf:type owl:NamedIndividual ,
               persona:Person .

:Self rdfs:comment "Alice Walker's persona for her employment at Acme."@en ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → GivenName (JSContactCardPersonShape)
        rdf:type cco:ent00000002 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "Alice"
    ] ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → AlternateName
        rdf:type cco:ent00000006 ;  # AlternateName
        <https://w3id.org/cco-domains/cco/ont00001765> "Alice Walker"
    ] ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → Email
        rdf:type cco:ent00000024 ;  # Email
        <https://w3id.org/cco-domains/cco/ont00001765> "alice@acme.com"  # has text value
    ] ;

    persona:hasSocialNetwork :Alice_Acme_Network .


:Alice_Acme_Network rdf:type owl:NamedIndividual ,
                             cco:ont00001183 ;  # Social Network
    rdfs:label "Alice Walker's Acme connections"@en ;
    <http://purl.obolibrary.org/obo/BFO_0000115> :Paula_Walker .  # has member part
```
