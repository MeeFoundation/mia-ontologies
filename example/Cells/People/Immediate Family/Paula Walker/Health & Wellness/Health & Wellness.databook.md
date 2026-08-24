---
id: http://www.example.org/mia/cells/cell-13
title: "Health & Wellness"
type: cell-databook
version: 1.2.0
created: 2026-07-10
description: >
  Cell DataBook for folder "Health & Wellness" (cell:origin: cat:HealthWellness). It is a one-member cell with one memberTopic about :Self and one otherTopic about :Paula_Walker (the cell's subject).
mia:
  origin: "cat:HealthWellness"
  creator: ":Self"
  memberCount: "cell:OneMember"
  memberTopics: "topic-35"
  otherTopics: "topic-17"
  topics:
    - id: "http://www.example.org/mia/topics/topic-35"
      claimant: ":Self"
      subject: ":Self"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
    - id: "http://www.example.org/mia/topics/topic-17"
      claimant: ":Self"
      subject: ":Paula_Walker"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
---

## Topics

<a id="topic-35"></a>
### Topic 35

#### Overview

This topic captures Alice's own bare identity claim (just her given name) — the cell's one required `memberTopics` entry. A `cell:OneMember` cell in the user's own category-cell tree always has `:Self` as its one member (the user either created the cell themselves or received it via sharing — either way `:Self` participates), regardless of what the cell's `subject` is. Alice is both the claimant and the subject.

#### Topic Graph

```turtle
<!-- databook:id: alice-health-wellness-member-topic-graph -->
<!-- databook:graph: http://www.example.org/mia/topics/topic-35#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

:Self <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → GivenName
    rdf:type cco:ent00000002 ;  # GivenName
    <https://w3id.org/cco-domains/cco/ont00001765> "Alice"  # has text value
] .
```

<a id="topic-17"></a>
### Topic 17

#### Overview

This topic captures Paula Walker's physical body characteristics — properties that are intrinsic to her as a person and do not belong to any particular institutional or social topic — as recorded by Alice. Height is recorded as a CCO Height quality with a RatioMeasurementICE (68 inches). Eye color is modeled as Paula bearing a BlueEyeColor quality directly. Hair color is borne by her ScalpHair continuant part. Alice is the claimant; Paula is the cell's `subject` but, since this cell now has a real memberTopic (topic 35, above) about Alice herself, Paula's topic is linked as an `otherTopic` rather than the required `memberTopics` entry.

#### Topic Graph

```turtle
<!-- databook:id: paula-health-topic-graph -->
<!-- databook:graph: http://www.example.org/mia/topics/topic-17#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

:Paula_Walker rdfs:comment "Paula Walker's physical body characteristics."@en ;

    # ── Height ───────────────────────────────────────────────────────────────

    <http://purl.obolibrary.org/obo/BFO_0000196> :Paula_Height ;
    <http://purl.obolibrary.org/obo/BFO_0000196> :Paula_Height_Measurement ;

    # ── Eye color ────────────────────────────────────────────────────────────

    <http://purl.obolibrary.org/obo/BFO_0000196> [  # bearer of → Eye Color
        rdf:type cco:ent00000040 ;  # Blue Eye Color
        rdfs:comment "Eye color: Blue"@en
    ] ;

    # ── Hair ─────────────────────────────────────────────────────────────────

    <http://purl.obolibrary.org/obo/BFO_0000178> [  # has continuant part → Scalp Hair
        rdf:type cco:ont00000058 ;  # Scalp Hair
        <http://purl.obolibrary.org/obo/BFO_0000196> [  # bearer of → Hair Color
            rdf:type cco:ont00000026 ;  # Hair Color
            <https://w3id.org/cco-domains/cco/ont00001765> "Grey" ;
            rdfs:comment "Hair color: Grey"@en
        ]
    ] .


:Paula_Height rdf:type owl:NamedIndividual ,
                       <https://w3id.org/cco-domains/cco/ont00000967> ;  # Height (CCO Quality)
    rdfs:label "Paula Walker's height"@en .

:Paula_Height_Measurement rdf:type owl:NamedIndividual ,
                                   <https://w3id.org/cco-domains/cco/ont00001022> ;  # Ratio Measurement ICE
    <https://w3id.org/cco-domains/cco/ont00001983> :Paula_Height ;
    <https://w3id.org/cco-domains/cco/ont00001863> <https://w3id.org/cco-domains/cco/ont00001677> ;  # uses measurement unit: Inch
    <https://w3id.org/cco-domains/cco/ont00001769> "68"^^xsd:decimal .  # has decimal value
```
