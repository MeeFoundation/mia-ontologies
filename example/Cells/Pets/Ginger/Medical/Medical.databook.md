---
id: http://www.example.org/mia/cells/cell-40
title: "Medical"
type: cell-databook
version: 2.0.0
created: 2026-08-21
description: >
  Cell DataBook for folder "Medical" (cell:origin: cat:PetsMedical). Formerly two nested cells — an organizational "Medical" scaffold (cell-38, retired) wrapping a "Medications" content cell (this cell, cell-40) — now flattened into one, since cat:PetsMedications was merged into cat:PetsMedical and the extra nesting no longer served a purpose. It is a two-member cell, shared by Alice with Paula, with two members (about :Self and :Paula_Walker) and one graph about :Ginger, Alice's cat (the cell's subject).
mia:
  origin: "cat:PetsMedical"
  creator: ":Self"
  memberCount: "cell:TwoMember"
  members:
    - "graph-33"
    - "graph-57"
  topic: "graph-32"
  graphs:
    - id: "http://www.example.org/mia/graphs/graph-33"
      claimant: ":Self"
      subject: ":Self"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/graph/shapes
    - id: "http://www.example.org/mia/graphs/graph-57"
      claimant: ":Paula_Walker"
      subject: ":Paula_Walker"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/graph/shapes
    - id: "http://www.example.org/mia/graphs/graph-32"
      claimant: ":Self"
      subject: ":Ginger"
      template: "persona:PetMedicationRecord"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/persona/shapes/pet-medications
  shape: "pshapes:PetMedicationRecordShape"
---

## Graphs

<a id="graph-33"></a>
### Graph 33

#### Overview

This graph is one of the cell's two `members` entries, satisfying `cell:TwoMember`'s per-member baseline alongside graph 57 (Paula's own claim, below). Alice is both the claimant and the subject. Deliberately empty: the `members` requirement is about `g:subject`/`g:claimant` (asserted at the `mia.graphs[]` YAML level, not in this Turtle body), not about carrying any particular content.

#### Graph

```turtle
<!-- databook:id: alice-ginger-medications-member-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-33#graph -->
```

<a id="graph-57"></a>
### Graph 57

#### Overview

This cell was created by Alice and later shared with Paula, making the cell a `cell:TwoMember` cell. This graph is Paula's own bare identity claim (just her given name) — the cell's second `members` entry, satisfying `cell:TwoMember`'s per-member baseline alongside graph 33 (Alice's own claim, above). Paula is both the claimant and the subject.

#### Graph

```turtle
<!-- databook:id: paula-ginger-medications-member-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-57#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

:Paula_Walker rdf:type owl:NamedIndividual ,
               persona:Person ;
    cco:ont00001879 [  # designated by → GivenName
        rdf:type cco:ent00000002 ;  # GivenName
        cco:ont00001765 "Paula"  # has text value
    ] .
```

<a id="graph-32"></a>
### Graph 32

#### Overview

This graph captures Alice's record of her cat Ginger's medications — an amoxicillin/clavulanate course prescribed after a minor infection, and an ongoing daily joint supplement. Validated by the `PetMedications` per-template SHACL shapes. Alice is the claimant; Ginger is the cell's `subject` but, since she has no `p:Person` individual of her own, her graph is linked via `cell:topic` rather than as one of the required `members` entries (graphs 33 and 57, above, fill those slots instead). Each medication's active ingredient(s) are cited by real ChEBI class IRIs, its tablet/liquid dosage form and amount by DrOn/CCO terms, and its schedule by a DrOn drug-administration individual carrying a BFO temporal interval — see `persona:Medication`'s `rdfs:comment` (persona-templates.ttl) for the full reuse rationale.

#### Graph

```turtle
<!-- databook:id: ginger-medications-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-32#graph -->
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
