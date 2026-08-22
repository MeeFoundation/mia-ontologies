---
id: http://www.example.org/mia/cells/cell-40
title: "Medications"
type: cell-databook
version: 1.2.0
created: 2026-08-21
description: >
  Cell DataBook for folder "Medications" (cell:origin: cat:PetsMedications). It is a one-member cell with one memberTopic about :Self and one otherTopic about :Ginger, Alice's cat (the cell's subject).
mia:
  origin: "cat:PetsMedications"
  creator: ":Self"
  memberCount: "cell:OneMember"
  subject: ":Ginger"
  memberTopics: "topic-33"
  otherTopics: "topic-32"
  topics:
    - id: "http://www.example.org/mia/topics/topic-33"
      claimant: ":Self"
      subject: ":Self"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/topic/shapes
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

<a id="topic-33"></a>
### Topic 33

#### Overview

This topic is the cell's one required `memberTopics` entry, satisfying `cell:OneMember`'s per-member baseline. Alice is both the claimant and the subject. Deliberately empty: the `memberTopics` requirement is about `t:subject`/`t:claimant` (asserted at the `mia.topics[]` YAML level, not in this Turtle body), not about carrying any particular content.

#### Topic Graph

```turtle
<!-- databook:id: alice-ginger-medications-member-topic-graph -->
<!-- databook:graph: http://www.example.org/mia/topics/topic-33#graph -->
```

<a id="topic-32"></a>
### Topic 32

#### Overview

This topic captures Alice's record of her cat Ginger's medications — an amoxicillin/clavulanate course prescribed after a minor infection, and an ongoing daily joint supplement. Validated by the `PetMedications` per-template SHACL shapes. Alice is the claimant; Ginger is the cell's `subject` but, since she has no `p:Person` individual of her own, her topic is linked as an `otherTopic` rather than the required `memberTopics` entry (topic 33, above, fills that slot instead). Each medication's active ingredient(s) are cited by real ChEBI class IRIs, its tablet/liquid dosage form and amount by DrOn/CCO terms, and its schedule by a DrOn drug-administration individual carrying a BFO temporal interval — see `persona:Medication`'s `rdfs:comment` (persona-templates.ttl) for the full reuse rationale.

#### Topic Graph

```turtle
<!-- databook:id: ginger-medications-topic-graph -->
<!-- databook:graph: http://www.example.org/mia/topics/topic-32#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
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

    persona:hasActiveIngredient <http://purl.obolibrary.org/obo/CHEBI_2676> ,   # amoxicillin
                                 <http://purl.obolibrary.org/obo/CHEBI_48947> ; # clavulanic acid

    persona:hasDoseForm <http://purl.obolibrary.org/obo/DRON_00000022> ;  # drug tablet

    persona:medicationBrandName "Clavamox" ;
    persona:medicationManufacturer "Zoetis" ;

    persona:hasDosageAmount :Ginger_Medication_Clavamox_Dosage ;
    persona:hasAdministration :Ginger_Medication_Clavamox_Administration .

:Ginger_Medication_Clavamox_Dosage rdf:type owl:NamedIndividual ,
               persona:DosageAmount ;
    rdfs:comment "1 tablet — a count of discrete dose-form units (see hasDoseForm above), not a measured quantity, so no 'uses measurement unit' link (per UCUM's own stance that 'tablet' is not a real unit)."@en ;
    cco:ont00001773 1 .  # has integer value

:Ginger_Medication_Clavamox_Administration rdf:type owl:NamedIndividual ,
               persona:MedicationAdministration ;
    persona:medicationFrequencyPerDay "2" ;
    <http://purl.obolibrary.org/obo/BFO_0000199> :Ginger_Medication_Clavamox_Interval .  # occupies temporal region

:Ginger_Medication_Clavamox_Interval rdf:type owl:NamedIndividual ,
               <http://purl.obolibrary.org/obo/BFO_0000038> ;  # one-dimensional temporal region
    cco:ent00000017 "2026-08-10"^^xsd:date ;   # has start date
    cco:ent00000018 "2026-08-20"^^xsd:date .   # has end date — a completed short course

:Ginger_Medication_Glucosamine rdf:type owl:NamedIndividual ,
               persona:Medication ;
    rdfs:label "Glucosamine/Chondroitin"@en ;

    persona:hasActiveIngredient <http://purl.obolibrary.org/obo/CHEBI_5417> ,   # glucosamine
                                 <http://purl.obolibrary.org/obo/CHEBI_37397> ; # chondroitin sulfate

    persona:hasDosageAmount :Ginger_Medication_Glucosamine_Dosage ;
    persona:hasAdministration :Ginger_Medication_Glucosamine_Administration .

:Ginger_Medication_Glucosamine_Dosage rdf:type owl:NamedIndividual ,
               persona:DosageAmount ;
    rdfs:comment "1 teaspoon — a true measured liquid quantity, so it carries a real CCO measurement unit (unlike the tablet count above)."@en ;
    cco:ont00001769 "1.0"^^xsd:decimal ;         # has decimal value
    cco:ont00001863 cco:ont00001573 .            # uses measurement unit → Teaspoon Measurement Unit

:Ginger_Medication_Glucosamine_Administration rdf:type owl:NamedIndividual ,
               persona:MedicationAdministration ;
    persona:medicationFrequencyPerDay "1" ;
    <http://purl.obolibrary.org/obo/BFO_0000199> :Ginger_Medication_Glucosamine_Interval .  # occupies temporal region

:Ginger_Medication_Glucosamine_Interval rdf:type owl:NamedIndividual ,
               <http://purl.obolibrary.org/obo/BFO_0000038> ;  # one-dimensional temporal region
    cco:ent00000017 "2026-01-15"^^xsd:date .   # has start date — no end date: ongoing/current
```
