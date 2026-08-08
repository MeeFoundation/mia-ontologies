---
id: http://www.example.org/mia/cells/cell-24
title: "Health & Wellness"
type: cell-databook
version: 1.1.0
created: 2026-07-10
description: >
  Cell DataBook of category "Health & Wellness" (cell:origin: cat:HealthWellness). May carry one or two required subject values.
mia:
  origin: "cat:HealthWellness"
  creator: ":Self"
  memberCount: "cell:OneMember"
  subject: ":Paula_Walker"
  memberTopics: "topic-17"
  topics:
    - id: "http://www.example.org/mia/topics/topic-17"
      claimant: ":Self"
      subject: ":Paula_Walker"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
---

## Topics

<a id="topic-17"></a>
### Topic 17

#### Overview

This topic captures Paula Walker's physical body characteristics — properties that are intrinsic to her as a person and do not belong to any particular institutional or social topic — as recorded by Alice. Height is recorded as a CCO Height quality with a RatioMeasurementICE (68 inches). Eye color is modeled as Paula bearing a BlueEyeColor quality directly. Hair color is borne by her ScalpHair continuant part.

#### Topic Graph

```turtle
<!-- databook:id: paula-health-topic-graph -->
<!-- databook:graph: http://www.example.org/mia/topics/topic-17#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
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
            <https://purl.org/cco/ont00001765> "Grey" ;
            rdfs:comment "Hair color: Grey"@en
        ]
    ] .


:Paula_Height rdf:type owl:NamedIndividual ,
                       <https://purl.org/cco/ont00000967> ;  # Height (CCO Quality)
    rdfs:label "Paula Walker's height"@en .

:Paula_Height_Measurement rdf:type owl:NamedIndividual ,
                                   <https://purl.org/cco/ont00001022> ;  # Ratio Measurement ICE
    <https://purl.org/cco/ont00001983> :Paula_Height ;
    <https://purl.org/cco/ont00001863> <https://purl.org/cco/ont00001677> ;  # uses measurement unit: Inch
    <https://purl.org/cco/ont00001769> "68"^^xsd:decimal .  # has decimal value
```
