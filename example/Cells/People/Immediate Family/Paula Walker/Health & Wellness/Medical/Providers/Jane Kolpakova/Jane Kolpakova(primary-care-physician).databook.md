---
id: http://www.example.org/mia/categories/Jane-Kolpakova(primary-care-physician)
title: "Dr. Jane Kolpakova"
type: cell-databook
version: 1.1.0
created: 2026-07-10
description: >
  Cell DataBook of category "Dr. Jane Kolpakova" (cell:origin: cat:PrimaryCarePhysician). Content may include topics/folder/note links, and may carry one or two required subject values.
mia:
  origin: "cat:PrimaryCarePhysician"
  creator: ":Self"
  memberCount: "cell:OneMember"
  subject: ":Jane_Kolpakova"
  memberTopics: "https://www.example.org/mia/topics/jane-kolpakova.self(Jane-Kolpakova)(primary-care-physician)(25)"
  topics:
    - id: "https://www.example.org/mia/topics/jane-kolpakova.self(Jane-Kolpakova)(primary-care-physician)(25)"
      title: "About Jane Kolpakova in the PrimaryCarePhysician cell as claimed by Alice Walker"
      claimant: ":Self"
      subject: ":Jane_Kolpakova"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
      process:
        transformer: human
        timestamp: 2026-07-08T00:00:00Z
        agent:
          name: Paul Trevithick
          role: author
---

## Topics

<a id="topic-25"></a>
### Topic 25 — About Jane Kolpakova in the PrimaryCarePhysician cell as claimed by Alice Walker

#### Overview

This topic captures Alice's record of Dr. Jane Kolpakova, who is the primary care physician for Alice's mother, Paula Walker. Alice keeps this information so she and her sister Carol can coordinate Paula's medical appointments.

#### Topic Graph

```turtle
<!-- databook:id: jane-kolpakova-alice-topic-graph -->
<!-- databook:graph: https://www.example.org/mia/topics/jane-kolpakova.self(Jane-Kolpakova)(primary-care-physician)(25)#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Jane_Kolpakova rdf:type owl:NamedIndividual ,
               persona:Person ;
    rdfs:label "Jane Kolpakova (Primary Care Physician)"@en ;

    <https://purl.org/cco/ont00001879> [  # designated by → GivenName
        rdf:type cco:ent00000002 ;  # GivenName
        <https://purl.org/cco/ont00001765> "Jane"  # has text value
    ] ;

    <https://purl.org/cco/ont00001879> [  # designated by → FamilyName
        rdf:type cco:ent00000004 ;  # FamilyName
        <https://purl.org/cco/ont00001765> "Kolpakova"  # has text value
    ] ;

    <https://purl.org/cco/ont00001917> [  # described by → Person Note
        rdf:type cco:ent00000048 ;
        <https://purl.org/cco/ont00001765> "Paula Walker's primary care physician"
    ] .
```
