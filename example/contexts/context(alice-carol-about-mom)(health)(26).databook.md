---
id: https://www.example.org/mia/contexts/context(alice-carol-about-mom)(health)(26)
title: "Medical appointment claims for Paula Walker, shared between Alice and Carol"
type: context-databook
version: 1.0.11
created: 2026-07-08
description: >
  Alice's shared record of the claims needed to arrange a medical appointment
  for their mother, Paula Walker, synced to Carol's Mia via PDN. Linked from
  its cell via cell:graph rather than cell:sc-context, since this data is
  jointly maintained by Alice and Carol about a third party (Paula) and does
  not fit the self-vs-other classification that property assumes.
mia:
  template: "persona:MedicalAppointmentRecord"
graph:
  named_graph: https://www.example.org/mia/contexts/context(alice-carol-about-mom)(health)(26)#graph
  rdf_version: "1.1"
shapes:
  - http://mee.foundation/ontologies/persona/shapes
  - http://mee.foundation/ontologies/persona/shapes/medical-appointment
process:
  transformer: human
  timestamp: 2026-07-08T00:00:00Z
  agent:
    name: Paul Trevithick
    role: author
---

## Overview

This context captures Alice's shared record of the claims needed to arrange a medical appointment on behalf of their mother, Paula Walker. Alice maintains this record on her own Mia and syncs it to Carol's Mia over the PDN so both sisters can coordinate Paula's care. It is linked from its cell via `cell:graph` rather than `cell:sc-context`, since the data is jointly maintained by Alice and Carol about a third party (Paula) rather than claimable as simply self-vs-other. Because each context's named graph must be self-contained for p2p sync to work, the claims about Paula and about her primary care physician, Dr. Jane Kopakolva, are copied directly into this context rather than merely linked — Alice already holds Dr. Jane's information in her own Mia, so it is Alice's Mia that copies it over. Validated by the `MedicalAppointment` per-template SHACL shapes.

## Identity Data

```turtle
<!-- databook:id: alice-paula-medical-appointment-identity -->
<!-- databook:graph: https://www.example.org/mia/contexts/context(alice-carol-about-mom)(health)(26)#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

# ── Copied third-party individuals (self-containment for p2p sync) ──────────

:Paula_Walker rdf:type owl:NamedIndividual ,
               persona:Person ;
    rdfs:label "Paula Walker"@en ;

    <https://purl.org/cco/ont00001879> [  # designated by → GivenName
        rdf:type cco:ent00000002 ;  # GivenName
        <https://purl.org/cco/ont00001765> "Paula"
    ] ;

    <https://purl.org/cco/ont00001879> [  # designated by → FamilyName
        rdf:type cco:ent00000004 ;  # FamilyName
        <https://purl.org/cco/ont00001765> "Walker"
    ] .

:Jane_Kopakolva rdf:type owl:NamedIndividual ,
               persona:Person ;
    rdfs:label "Jane Kopakolva (Primary Care Physician)"@en ;

    <https://purl.org/cco/ont00001879> [  # designated by → GivenName
        rdf:type cco:ent00000002 ;  # GivenName
        <https://purl.org/cco/ont00001765> "Jane"
    ] ;

    <https://purl.org/cco/ont00001879> [  # designated by → FamilyName
        rdf:type cco:ent00000004 ;  # FamilyName
        <https://purl.org/cco/ont00001765> "Kopakolva"
    ] ;

    <https://purl.org/cco/ont00001917> [  # described by → Person Note
        rdf:type cco:ent00000048 ;
        <https://purl.org/cco/ont00001765> "Paula Walker's primary care physician"
    ] .

# ── The shared Medical Appointment claims record ─────────────────────────────

:Paula_Medical_Appointment rdf:type owl:NamedIndividual ,
               persona:MedicalAppointmentRecord ;
    rdfs:label "Paula Walker's Medical Appointment Claims"@en ;
    rdfs:comment "Claims Alice and Carol share to arrange and manage medical appointments for Paula."@en ;

    persona:forPatient :Paula_Walker ;
    persona:hasPrimaryCarePhysician :Jane_Kopakolva ;

    persona:currentMedication "Lisinopril 10mg daily" ,
                               "Metformin 500mg twice daily" ;

    persona:allergy "Penicillin" ;

    persona:medicalHistoryNote "Type 2 diabetes; hypertension." ;

    persona:insuranceProvider "Medicare" ;
    persona:insurancePolicyNumber "1EG4-TE5-MK72" ;

    persona:preferredPharmacy "CVS Pharmacy, 123 Main St, Paradise, CA" .
```
