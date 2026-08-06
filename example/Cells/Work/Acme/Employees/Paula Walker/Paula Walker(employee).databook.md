---
id: http://www.example.org/mia/categories/Paula-Walker(employee)
title: "Paula Walker"
type: cell-databook
version: 1.1.0
created: 2026-07-10
description: >
  Cell DataBook of category "Paula Walker" (cell:origin: cat:Employee). Content may include topics/folder/note links, and may carry one or two required subject values. This is a cell:OneMember cell — Paula is the subject, not a member; her own topic is linked via otherTopics rather than memberTopics, per CLAUDE.md Check 18.
mia:
  origin: "cat:Employee"
  creator: ":Self"
  memberCount: "cell:OneMember"
  subject: ":Paula_Walker"
  memberTopics: "https://www.example.org/mia/topics/self.self(Paula-Walker)(employee)(20)"
  otherTopics: "https://www.example.org/mia/topics/paula-walker.self(Paula-Walker)(employee)(06)"
  topics:
    - id: "https://www.example.org/mia/topics/paula-walker.self(Paula-Walker)(employee)(06)"
      title: "About Paula Walker in the Employee cell as claimed by Alice Walker"
      claimant: ":Self"
      subject: ":Paula_Walker"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
      process:
        transformer: human
        timestamp: 2026-06-19T00:00:00Z
        agent:
          name: Paul Trevithick
          role: author
    - id: "https://www.example.org/mia/topics/self.self(Paula-Walker)(employee)(20)"
      title: "About Alice Walker in the Employee cell as claimed by Alice Walker"
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

<a id="topic-06"></a>
### Topic 06 — About Paula Walker in the Employee cell as claimed by Alice Walker

#### Overview

This topic captures Alice's record of her colleague Paula Walker in their shared Acme employment topic. Alice self-claims this topic; it is paired with Paula's own Acme persona in `20-alice(acme)alice`.

#### Topic Graph

```turtle
<!-- databook:id: paula-acme-topic-graph -->
<!-- databook:graph: https://www.example.org/mia/topics/paula-walker.self(Paula-Walker)(employee)(06)#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Paula_Walker rdf:type owl:NamedIndividual ,
               persona:Person ;
    rdfs:label "Paula Walker (Acme)"@en .
```

<a id="topic-20"></a>
### Topic 20 — About Alice Walker in the Employee cell as claimed by Alice Walker

#### Overview

This topic captures Alice Walker's employee identity at Acme. It records her work email address (alice@acme.com) and her Acme social network, which includes colleague Paula Walker. Alice's business card topic (`21-alice(business-card)alice`) derives professional contact details from this topic.

#### Topic Graph

```turtle
<!-- databook:id: alice-acme-topic-graph -->
<!-- databook:graph: https://www.example.org/mia/topics/self.self(Paula-Walker)(employee)(20)#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Self rdfs:comment "Alice Walker's persona for her employment at Acme."@en ;

    <https://purl.org/cco/ont00001879> [  # designated by → AlternateName
        rdf:type cco:ent00000006 ;  # AlternateName
        <https://purl.org/cco/ont00001765> "Alice Walker"
    ] ;

    <https://purl.org/cco/ont00001879> [  # designated by → Email
        rdf:type cco:ent00000024 ;  # Email
        <https://purl.org/cco/ont00001765> "alice@acme.com"  # has text value
    ] ;

    persona:hasSocialNetwork :Alice_Acme_Network .


:Alice_Acme_Network rdf:type owl:NamedIndividual ,
                             cco:ont00001183 ;  # Social Network
    rdfs:label "Alice Walker's Acme connections"@en ;
    <http://purl.obolibrary.org/obo/BFO_0000115> :Paula_Walker .  # has member part
```
