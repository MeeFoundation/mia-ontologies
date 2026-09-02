---
id: http://www.example.org/mia/cells/cell-15
title: "Medical Appointment"
type: cell-databook
version: 1.1.0
created: 2026-07-10
description: >
  Cell DataBook for folder "Medical Appointment" (cell:category: cat:MedicalAppointment). It is a two-member cell with two members about :Carol_Walker and :Self and one graph about :Paula_Walker.
mia:
  category: "cat:MedicalAppointment"
  creator: ":Self"
  owner: ":Self"
  member:
    - "graph-28"
    - "graph-30"
  topic:
    - "graph-26"
  graphs:
    - id: "http://www.example.org/mia/graphs/graph-26"
      claimant: ":Self"
      subject: ":Paula_Walker"
      template: "persona:MedicalAppointmentRecord"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/persona/shapes/medical-appointment
    - id: "http://www.example.org/mia/graphs/graph-28"
      claimant: ":Carol_Walker"
      subject: ":Carol_Walker"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/graph/shapes
    - id: "http://www.example.org/mia/graphs/graph-30"
      claimant: ":Self"
      subject: ":Self"
      shapes:
        - http://mee.foundation/ontologies/persona/shapes
        - http://mee.foundation/ontologies/graph/shapes
---

## Graphs

<a id="graph-26"></a>
### Graph 26

#### Overview

This graph captures Alice's shared record of the claims needed to arrange a medical appointment on behalf of their mother, Paula Walker. Alice maintains this record on her own instance of the app and syncs it to Carol's over the PDN so both sisters can coordinate Paula's care. Because each graph's named graph must be self-contained for p2p sync to work, the claims about Paula and about her primary care physician, Dr. Jane Starostina, are copied directly into this graph rather than merely linked — Alice already holds Dr. Jane's information in her own instance, so it is Alice's own app that copies it over. Validated by the `MedicalAppointment` per-template SHACL shapes. Alice is the claimant.

#### Graph

```turtle
<!-- databook:id: alice-paula-medical-appointment-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-26#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

# ── Copied third-party individuals (self-containment for p2p sync) ──────────

:Paula_Walker rdf:type owl:NamedIndividual ,
               persona:Person ;
    rdfs:label "Paula Walker"@en ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → GivenName
        rdf:type cco:ent00000002 ;  # GivenName
        <https://w3id.org/cco-domains/cco/ont00001765> "Paula"
    ] ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → FamilyName
        rdf:type cco:ent00000004 ;  # FamilyName
        <https://w3id.org/cco-domains/cco/ont00001765> "Walker"
    ] .

:Jane_Starostina rdf:type owl:NamedIndividual ,
               persona:Person ;
    rdfs:label "Jane Starostina (Primary Care Physician)"@en ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → GivenName
        rdf:type cco:ent00000002 ;  # GivenName
        <https://w3id.org/cco-domains/cco/ont00001765> "Jane"
    ] ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → FamilyName
        rdf:type cco:ent00000004 ;  # FamilyName
        <https://w3id.org/cco-domains/cco/ont00001765> "Starostina"
    ] ;

    <https://w3id.org/cco-domains/cco/ont00001917> [  # described by → Person Note
        rdf:type cco:ent00000048 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "Paula Walker's primary care physician"
    ] .

# ── The shared Medical Appointment claims record ─────────────────────────────

:Paula_Medical_Appointment rdf:type owl:NamedIndividual ,
               persona:MedicalAppointmentRecord ;
    rdfs:label "Paula Walker's Medical Appointment Claims"@en ;
    rdfs:comment "Claims Alice and Carol share to arrange and manage medical appointments for Paula."@en ;

    persona:forPatient :Paula_Walker ;
    persona:hasPrimaryCarePhysician :Jane_Starostina ;

    persona:currentMedication "Lisinopril 10mg daily" ,
                               "Metformin 500mg twice daily" ;

    persona:allergy "Penicillin" ;

    persona:medicalHistoryNote "Type 2 diabetes; hypertension." ;

    persona:insuranceProvider "Medicare" ;
    persona:insurancePolicyNumber "1EG4-TE5-MK72" ;

    persona:preferredPharmacy "CVS Pharmacy, 123 Main St, Paradise, CA" .
```

<a id="graph-28"></a>
### Graph 28

#### Overview

This graph captures Carol Walker's own self-claimed persona and contact info, shared directly from her own instance of the app to Alice's over the PDN. This cell's two members are Alice and Carol (its derived subject, `:Paula_Walker` (from its sole `graph` entry), is a third party the cell is *about*, not one of its members) — this graph and its counterpart (graph 30, Alice's own self-claimed contact info) together represent those two members, alongside graph 26 (Alice's claims about Paula's medical appointment). Carol is the claimant.

#### Graph

```turtle
<!-- databook:id: carol-self-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-28#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Carol_Walker rdf:type owl:NamedIndividual ,
               persona:Person ;
    rdfs:label "Carol Walker"@en ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → GivenName
        rdf:type cco:ent00000002 ;  # GivenName
        <https://w3id.org/cco-domains/cco/ont00001765> "Carol"
    ] ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → FamilyName
        rdf:type cco:ent00000004 ;  # FamilyName
        <https://w3id.org/cco-domains/cco/ont00001765> "Walker"
    ] ;

    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → Phone
        rdf:type cco:ent00000023 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "+19165550198"
    ] ;

    <https://w3id.org/cco-domains/cco/ont00001917> [  # described by → Person Note
        rdf:type cco:ent00000048 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "Usually available weekday evenings and weekends for Mom's appointments."
    ] .
```

<a id="graph-30"></a>
### Graph 30

#### Overview

This graph captures Alice Walker's own self-claimed contact info, kept in this cell so Carol can reach her while coordinating Paula's medical appointments. This cell's two members are Alice and Carol (its derived subject, `:Paula_Walker` (from its sole `graph` entry), is a third party the cell is *about*, not one of its members) — this graph and its counterpart (graph 28, Carol's own self-claimed persona) together represent those two members, alongside graph 26 (Alice's claims about Paula's medical appointment). Alice is the claimant.

#### Graph

```turtle
<!-- databook:id: alice-self-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-30#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Self <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → Phone
        rdf:type cco:ent00000023 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "+15108149999"
    ] ;

    <https://w3id.org/cco-domains/cco/ont00001917> [  # described by → Person Note
        rdf:type cco:ent00000048 ;
        <https://w3id.org/cco-domains/cco/ont00001765> "Best reached by text for scheduling Mom's appointments."
    ] .
```
