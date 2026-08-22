---
id: http://www.example.org/mia/cells/cell-40
title: "Medications"
type: cell-databook
version: 1.0.0
created: 2026-08-21
description: >
  Cell DataBook for folder "Medications" (cell:origin: cat:PetsMedications). It is a one-member cell with one memberTopic about :Ginger, Alice's cat.
mia:
  origin: "cat:PetsMedications"
  creator: ":Self"
  memberCount: "cell:OneMember"
  subject: ":Ginger"
  memberTopics: "topic-32"
  topics:
    - id: "http://www.example.org/mia/topics/topic-32"
      claimant: ":Self"
      subject: ":Ginger"
      template: "persona:PetMedicationRecord"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/persona/shapes/pet-medications
  shape: "pshapes:PetMedicationRecordShape"
---

## Topics

<a id="topic-32"></a>
### Topic 32

#### Overview

This topic captures Alice's record of her cat Ginger's medications — an amoxicillin/clavulanate course prescribed after a minor infection, and an ongoing daily joint supplement. Validated by the `PetMedications` per-template SHACL shapes. Alice is the claimant, and since Ginger has no `p:Person` individual of her own, this topic's sole topic occupies the cell's required `memberTopics` slot directly (there is no separate "member" topic to fill it instead).

#### Topic Graph

```turtle
<!-- databook:id: ginger-medications-topic-graph -->
<!-- databook:graph: http://www.example.org/mia/topics/topic-32#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

:Ginger rdf:type owl:NamedIndividual ;
    rdfs:label "Ginger (Alice's cat)"@en .

:Ginger_Medications rdf:type owl:NamedIndividual ,
               persona:PetMedicationRecord ;
    rdfs:label "Ginger's Medications"@en ;
    rdfs:comment "Alice's record of medications for her cat, Ginger."@en ;

    persona:hasMedication :Ginger_Medication_Clavamox ,
                           :Ginger_Medication_Glucosamine .

:Ginger_Medication_Clavamox rdf:type owl:NamedIndividual ,
               persona:Medication ;
    rdfs:label "Amoxicillin/Clavulanate (Clavamox)"@en ;
    persona:medicationChemicalName "Amoxicillin/Clavulanate" ;
    persona:medicationBrandName "Clavamox" ;
    persona:medicationManufacturer "Zoetis" ;
    persona:medicationDosageValue "1" ;
    persona:medicationDosageUnit "tablet" ;
    persona:medicationFrequencyPerDay "2" ;
    persona:medicationStartDate "2026-08-10"^^xsd:date ;
    persona:medicationEndDate "2026-08-20"^^xsd:date .

:Ginger_Medication_Glucosamine rdf:type owl:NamedIndividual ,
               persona:Medication ;
    rdfs:label "Glucosamine/Chondroitin"@en ;
    persona:medicationChemicalName "Glucosamine/Chondroitin" ;
    persona:medicationDosageValue "1" ;
    persona:medicationDosageUnit "teaspoon" ;
    persona:medicationFrequencyPerDay "1" ;
    persona:medicationStartDate "2026-01-15"^^xsd:date .
```
