---
id: http://www.example.org/mia/categories/bob-johnson(others)-cell
title: "Bob Johnson (Cell)"
type: cell-databook
version: 1.1.0
created: 2026-07-10
description: >
  Cell DataBook of category "Bob Johnson" (mia.catType: Others). Content may include topics/folder/note links, and may carry one or two required subject values.
mia:
  creator: ":Self"
  memberCount: "cell:TwoMember"
  subject:
    - ":Bob_Johnson"
    - ":Self"
  memberTopics:
    - "https://www.example.org/mia/topics/bob-johnson.bob-johnson(bob-johnson)(others)(02)"
    - "https://www.example.org/mia/topics/self.self(bob-johnson)(others)(12)"
    - "https://www.example.org/mia/topics/bob-johnson.self(bob-johnson)(others)(04)"
    - "https://www.example.org/mia/topics/self.bob-johnson(bob-johnson)(others)(08)"
  topics:
    - id: "https://www.example.org/mia/topics/bob-johnson.bob-johnson(bob-johnson)(others)(02)"
      title: "About Bob Johnson in the Others cell as claimed by Bob Johnson"
      claimant: ":Bob_Johnson"
      subject: ":Bob_Johnson"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
      process:
        transformer: human
        timestamp: 2026-06-19T00:00:00Z
        agent:
          name: Paul Trevithick
          role: author
    - id: "https://www.example.org/mia/topics/bob-johnson.self(bob-johnson)(others)(04)"
      title: "About Bob Johnson in the Others cell as claimed by Alice Walker"
      claimant: ":Self"
      subject: ":Bob_Johnson"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
      process:
        transformer: human
        timestamp: 2026-06-19T00:00:00Z
        agent:
          name: Paul Trevithick
          role: author
    - id: "https://www.example.org/mia/topics/self.bob-johnson(bob-johnson)(others)(08)"
      title: "About Alice Walker in the Others cell as claimed by Bob Johnson"
      claimant: ":Bob_Johnson"
      subject: ":Self"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
      process:
        transformer: human
        timestamp: 2026-06-19T00:00:00Z
        agent:
          name: Paul Trevithick
          role: author
    - id: "https://www.example.org/mia/topics/self.self(bob-johnson)(others)(12)"
      title: "About Alice Walker in the Others cell as claimed by Alice Walker"
      claimant: ":Self"
      subject: ":Self"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
      process:
        transformer: human
        timestamp: 2026-06-19T00:00:00Z
        agent:
          name: Paul Trevithick
          role: author
---

## Topics

<a id="topic-02"></a>
### Topic 02 — About Bob Johnson in the Others cell as claimed by Bob Johnson

#### Overview

This topic captures Bob Johnson's self-claimed Bob-topic persona, transmitted from Bob's Mia to Alice's Mia over the PDN. It records Bob's name and his social network link to Alice.

#### Topic Graph

```turtle
<!-- databook:id: bob-bob-bob-topic-graph -->
<!-- databook:graph: https://www.example.org/mia/topics/bob-johnson.bob-johnson(bob-johnson)(others)(02)#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Bob_Johnson rdf:type owl:NamedIndividual ,
              persona:Person ;
    rdfs:label "Bob Johnson (Bob)"@en ;
    rdfs:comment "Bob Johnson's self-claimed persona in the 1:1 Bob topic."@en ;

    <https://purl.org/cco/ont00001879> [  # designated by → GivenName
        rdf:type cco:ent00000002 ;  # GivenName
        <https://purl.org/cco/ont00001765> "Bob"  # has text value
    ] ;

    <https://purl.org/cco/ont00001879> [  # designated by → FamilyName
        rdf:type cco:ent00000004 ;  # FamilyName
        <https://purl.org/cco/ont00001765> "Johnson"  # has text value
    ] ;

    persona:hasSocialNetwork :Bob_Bob_Network .


:Bob_Bob_Network rdf:type owl:NamedIndividual ,
                          cco:ont00001183 ;  # Social Network
    rdfs:label "Bob Johnson's Bob connection"@en ;
    <http://purl.obolibrary.org/obo/BFO_0000115> :Self .  # has member part → Alice
```

<a id="topic-04"></a>
### Topic 04 — About Bob Johnson in the Others cell as claimed by Alice Walker

#### Overview

This topic captures Alice's record of Bob Johnson in their 1:1 relationship topic. Alice notes Bob's favorite drink.

#### Topic Graph

```turtle
<!-- databook:id: bob-bob-alice-topic-graph -->
<!-- databook:graph: https://www.example.org/mia/topics/bob-johnson.self(bob-johnson)(others)(04)#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Bob_Johnson rdf:type owl:NamedIndividual ,
              persona:Person ;
    rdfs:label "Bob Johnson (Bob-colleague-of-alice)"@en ;

    <https://purl.org/cco/ont00001917> [  # described by → Person Note
        rdf:type cco:ent00000048 ;
        <https://purl.org/cco/ont00001765> "Fav drink: oat milk cappuccino"
    ] .
```

<a id="topic-08"></a>
### Topic 08 — About Alice Walker in the Others cell as claimed by Bob Johnson

#### Overview

This topic captures Bob's record of Alice in their 1:1 relationship topic, transmitted from Bob's Mia to Alice's Mia over the PDN. Bob notes Alice's favorite drink.

#### Topic Graph

```turtle
<!-- databook:id: alice-bob-bob-topic-graph -->
<!-- databook:graph: https://www.example.org/mia/topics/self.bob-johnson(bob-johnson)(others)(08)#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Self <https://purl.org/cco/ont00001917> [  # described by → Person Note
        rdf:type cco:ent00000048 ;
        <https://purl.org/cco/ont00001765> "Favorite drink: pepsi"
    ] .
```

<a id="topic-12"></a>
### Topic 12 — About Alice Walker in the Others cell as claimed by Alice Walker

#### Overview

This topic captures Alice Walker's self-claimed persona in her 1:1 relationship with Bob Johnson. It records the name Alice presents to Bob and her social network link to him.

#### Topic Graph

```turtle
<!-- databook:id: alice-bob-alice-topic-graph -->
<!-- databook:graph: https://www.example.org/mia/topics/self.self(bob-johnson)(others)(12)#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Self rdfs:comment "Alice Walker's persona for her 1:1 relationship with Bob."@en ;

    <https://purl.org/cco/ont00001879> [  # designated by → AlternateName
        rdf:type cco:ent00000006 ;  # AlternateName
        <https://purl.org/cco/ont00001765> "Alice Walker"
    ] ;

    <https://purl.org/cco/ont00001879> [  # designated by → GivenName
        rdf:type cco:ent00000002 ;  # GivenName
        <https://purl.org/cco/ont00001765> "Alice"  # has text value
    ] ;

    <https://purl.org/cco/ont00001879> [  # designated by → FamilyName
        rdf:type cco:ent00000004 ;  # FamilyName
        <https://purl.org/cco/ont00001765> "Walker"  # has text value
    ] ;

    persona:hasSocialNetwork :Alice_Bob_Network .


:Alice_Bob_Network rdf:type owl:NamedIndividual ,
                             cco:ont00001183 ;  # Social Network
    rdfs:label "Alice Walker's Bob connection"@en ;
    <http://purl.obolibrary.org/obo/BFO_0000115> :Bob_Johnson .  # has member part
```
