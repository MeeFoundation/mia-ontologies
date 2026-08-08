---
id: http://www.example.org/mia/categories/Boston-Hub-Society(affiliations)
title: "Boston Hub Society"
type: cell-databook
version: 1.1.0
created: 2026-07-10
description: >
  Cell DataBook of category "Boston Hub Society" (cell:origin: cat:Affiliations). May carry one or two required subject values.
mia:
  origin: "cat:Affiliations"
  creator: ":Self"
  memberCount: "cell:ThreePlusMember"
  subject: ":BHS_Group"
  memberTopics:
    - "topic-01"
    - "topic-14"
    - "topic-03"
  topics:
    - id: "http://www.example.org/mia/topics/topic-01"
      claimant: ":BHS_Group"
      subject: ":BHS_Group"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
    - id: "http://www.example.org/mia/topics/topic-03"
      claimant: ":Bob_Johnson"
      subject: ":Bob_Johnson"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
    - id: "http://www.example.org/mia/topics/topic-14"
      claimant: ":Self"
      subject: ":Self"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
---

## Topics

<a id="topic-01"></a>
### Topic 01 — About Boston Hub Society in the Boston Hub Society cell as claimed by Boston Hub Society

#### Overview

This topic captures the Boston Hub Society as a `g:Group` entity. It records the group's membership: Alice Walker (`:Self`) and Bob Johnson (`:Bob_Johnson`). Any permitted member may claim or update this topic.

#### Topic Graph

```turtle
<!-- databook:id: bhs-group-topic-graph -->
<!-- databook:graph: http://www.example.org/mia/topics/topic-01#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix g: <http://mee.foundation/ontologies/group#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:BHS_Group rdf:type owl:NamedIndividual ,
                    g:Group ;
    rdfs:label "Boston Hub Society"@en ;
    rdfs:comment "The Boston Hub Society group instance."@en ;
    <http://purl.obolibrary.org/obo/BFO_0000115> :Self ;        # has member part → Alice
    <http://purl.obolibrary.org/obo/BFO_0000115> :Bob_Johnson . # has member part → Bob
```

<a id="topic-03"></a>
### Topic 03 — About Bob Johnson in the Boston Hub Society cell as claimed by Bob Johnson

#### Overview

This topic captures Bob Johnson's BHS profile as transmitted from Bob's Mia to Alice's Mia over the PDN. It records the name Bob presents to the Boston Hub Society group.

#### Topic Graph

```turtle
<!-- databook:id: bob-bhs-topic-graph -->
<!-- databook:graph: http://www.example.org/mia/topics/topic-03#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Bob_Johnson rdf:type owl:NamedIndividual ,
              persona:Person ;
    rdfs:label "Bob Johnson (BHS)"@en ;

    <https://purl.org/cco/ont00001879> [  # designated by → GivenName
        rdf:type cco:ent00000002 ;
        <https://purl.org/cco/ont00001765> "Bob"
    ] ;

    <https://purl.org/cco/ont00001879> [  # designated by → FamilyName
        rdf:type cco:ent00000004 ;
        <https://purl.org/cco/ont00001765> "Johnson"
    ] .
```

<a id="topic-14"></a>
### Topic 14 — About Alice Walker in the Boston Hub Society cell as claimed by Alice Walker

#### Overview

This topic captures Alice Walker's BHS profile — the identity data she shares with the Boston Hub Society group. It includes her current Paradise, CA address, her phone number, and her Gmail address.

#### Topic Graph

```turtle
<!-- databook:id: alice-bhs-topic-graph -->
<!-- databook:graph: http://www.example.org/mia/topics/topic-14#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Self rdfs:comment "Alice Walker's persona for her BHS group (aka her BHS profile)."@en ;

    <https://purl.org/cco/ont00001879> [  # designated by → AlternateName
        rdf:type cco:ent00000006 ;  # AlternateName
        <https://purl.org/cco/ont00001765> "Alice Walker"
    ] ;

    <https://purl.org/cco/ont00001879> :Address_BHS ;  # designated by → current address

    <https://purl.org/cco/ont00001879> [  # designated by → Phone
        rdf:type cco:ent00000023 ;
        <https://purl.org/cco/ont00001765> "+15108149999"
    ] ;

    <https://purl.org/cco/ont00001879> [  # designated by → Email
        rdf:type cco:ent00000024 ;
        <https://purl.org/cco/ont00001765> "awalker@gmail.com"
    ] .


:Address_BHS rdf:type owl:NamedIndividual ,
                      cco:ent00000010 ;  # USPostalAddress
    rdfs:label "Alice Walker's BHS Address"@en ;
    <http://purl.obolibrary.org/obo/BFO_0000178> [  # has continuant part → Street
        rdf:type cco:ent00000011 ;
        <https://purl.org/cco/ont00001765> "123 Sleepy Hollow"
    ] ;
    <http://purl.obolibrary.org/obo/BFO_0000178> [  # has continuant part → City
        rdf:type cco:ent00000012 ;
        <https://purl.org/cco/ont00001765> "Paradise"
    ] ;
    <http://purl.obolibrary.org/obo/BFO_0000178> [  # has continuant part → State
        rdf:type cco:ent00000013 ;
        <https://purl.org/cco/ont00001765> "CA"
    ] ;
    <http://purl.obolibrary.org/obo/BFO_0000178> [  # has continuant part → ZIP
        rdf:type cco:ent00000015 ;
        <https://purl.org/cco/ont00001765> "95969"
    ] ;
    <http://purl.obolibrary.org/obo/BFO_0000178> [  # has continuant part → Country
        rdf:type cco:ent00000014 ;
        <https://purl.org/cco/ont00001765> "USA"
    ] .
```
