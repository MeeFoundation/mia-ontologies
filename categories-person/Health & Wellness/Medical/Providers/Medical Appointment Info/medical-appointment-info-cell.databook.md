---
id: http://mee.foundation/ontologies/categories-person/medical-appointment-info-cell
title: "Medical Appointment Info (Cell)"
type: cell-databook
version: 1.0.5
created: 2026-07-10
description: >
  Cell DataBook of category "Medical Appointment Info" (mia.catType: MedicalAppointmentInfo). Content may include sc-context/folder/note links, and may contain a named graph. Also embeds this canonical cell's per-template SHACL shape (persona:MedicalAppointment, fragment #shapes) as validation metadata — never cloned into user copies.
mia:
  parties: "cell:OneParty"
---

## SHACL Shapes

This canonical cell embeds the per-template SHACL shape applied to context files carrying `mia.template: "persona:MedicalAppointment"` (Tier 2 validation — see README `## Validation`). This block is validation metadata attached to the canonical cell only — it is never cloned when this category is copied into a user's tree (see [Lazy Copying](../../../../../README.md#lazy-copying)).

<!-- databook:id: shapes -->
```turtle
@prefix : <http://mee.foundation/ontologies/persona/shapes#> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix cco: <https://purl.org/cco/> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix dc: <http://purl.org/dc/elements/1.1/> .

<http://mee.foundation/ontologies/persona/shapes/medical-appointment> rdf:type owl:Ontology ;
    owl:imports <http://mee.foundation/ontologies/persona> ;
    dc:date "2026-07-13"^^xsd:date ;
    owl:versionInfo "Version 1.0.3 - moved out of standalone shacl/medical-appointment-shacl.ttl into an embedded turtle block (fragment #shapes) inside the canonical cell-databook categories-person/Health & Wellness/Medical/Providers/Medical Appointment Info/medical-appointment-info-cell.databook.md; IRI unchanged."@en ;
    rdfs:label "Medical Appointment Template SHACL Shapes"@en ;
    rdfs:comment """SHACL shapes for validating context files carrying context:template persona:MedicalAppointment.
                    Apply in addition to persona-shacl.ttl when validating a medical appointment context file.
                    Targets persona:MedicalAppointment individuals directly — the claims needed to arrange
                    the appointment are properties of the record, not of the patient's Person individual."""@en .


#################################################################
#  Medical Appointment Record Shape
#  Targets persona:MedicalAppointment individuals.
#  Required: forPatient (persona:forPatient, 1..1)
#            InsuranceProvider (persona:insuranceProvider, 1..1)
#            InsurancePolicyNumber (persona:insurancePolicyNumber, 1..1)
#  Optional: PrimaryCarePhysician (persona:hasPrimaryCarePhysician, 0..1)
#            CurrentMedication (persona:currentMedication, 0..n)
#            Allergy (persona:allergy, 0..n)
#            MedicalHistoryNote (persona:medicalHistoryNote, 0..1)
#            InsuranceGroupNumber (persona:insuranceGroupNumber, 0..1)
#            PreferredPharmacy (persona:preferredPharmacy, 0..1)
#################################################################

:MedicalAppointmentRecordShape
    a sh:NodeShape ;
    sh:targetClass persona:MedicalAppointment ;
    sh:message "Medical Appointment record validation: patient, insurance provider, and policy number are required."@en ;

    # ── Required: patient, insurance provider, insurance policy number ──────
    sh:property [
        sh:path persona:forPatient ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:class persona:Person ;
        sh:message "A Medical Appointment record must link to exactly one patient via forPatient."@en
    ] ;

    sh:property [
        sh:path persona:insuranceProvider ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:datatype xsd:string ;
        sh:message "A Medical Appointment record must record exactly one insurance provider."@en
    ] ;

    sh:property [
        sh:path persona:insurancePolicyNumber ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:datatype xsd:string ;
        sh:message "A Medical Appointment record must record exactly one insurance policy number."@en
    ] ;

    # ── Optional fields ──────────────────────────────────────────────────────
    sh:property [
        sh:path persona:hasPrimaryCarePhysician ;
        sh:maxCount 1 ;
        sh:class persona:Person ;
        sh:message "A Medical Appointment record may link to at most one primary care physician."@en
    ] ;

    sh:property [
        sh:path persona:medicalHistoryNote ;
        sh:maxCount 1 ;
        sh:datatype xsd:string ;
        sh:message "A Medical Appointment record may have at most one medical history note."@en
    ] ;

    sh:property [
        sh:path persona:insuranceGroupNumber ;
        sh:maxCount 1 ;
        sh:datatype xsd:string ;
        sh:message "A Medical Appointment record may have at most one insurance group number."@en
    ] ;

    sh:property [
        sh:path persona:preferredPharmacy ;
        sh:maxCount 1 ;
        sh:datatype xsd:string ;
        sh:message "A Medical Appointment record may have at most one preferred pharmacy."@en
    ] .
    # ── Multi-valued claims (no upper bound) ─────────────────────────────────
    # currentMedication, allergy — no sh:maxCount constraint; repeatable.
```
