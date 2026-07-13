---
id: http://mee.foundation/ontologies/categories-person/drivers-license-cell
title: "Drivers License (Cell)"
type: cell-databook
version: 1.0.5
created: 2026-07-10
description: >
  Cell DataBook of category "Drivers License" (mia.catType: DriversLicense). Content may include sc-context/folder/note links, and may contain a named graph. Also embeds this canonical cell's per-template SHACL shape (persona:DriversLicense, fragment #shapes) as validation metadata — never cloned into user copies.
mia:
  parties: "cell:OneParty"
---

## SHACL Shapes

This canonical cell embeds the per-template SHACL shape applied to context files carrying `mia.template: "persona:DriversLicense"` (Tier 2 validation — see README `## Validation`). This block is validation metadata attached to the canonical cell only — it is never cloned when this category is copied into a user's tree (see [Lazy Copying](../../../../README.md#lazy-copying)).

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

<http://mee.foundation/ontologies/persona/shapes/driverslicense> rdf:type owl:Ontology ;
    owl:imports <http://mee.foundation/ontologies/persona> ;
    dc:date "2026-07-13"^^xsd:date ;
    owl:versionInfo "Version 1.0.5 - moved out of standalone shacl/driverslicense-shacl.ttl into an embedded turtle block (fragment #shapes) inside the canonical cell-databook categories-person/Government/State/Drivers License/drivers-license-cell.databook.md; IRI unchanged."@en ;
    rdfs:label "Driver's License Template SHACL Shapes"@en ;
    rdfs:comment """SHACL shapes for validating context files carrying context:template persona:DriversLicense.
                    Apply in addition to persona-shacl.ttl when validating a driver's license context file.
                    Targets persona:DriversLicense document individuals directly — identity claims
                    (names, dates, license number) are properties of the document, not the Person."""@en .


#################################################################
#  DriversLicense Document Shape
#  Targets persona:DriversLicense individuals.
#  All identity claims are properties of the document individual.
#  Required: FullName (1..1) OR (GivenName (1..1) AND FamilyName (1..1))
#            DateOfBirth (ent00000046, 1..1)
#            DriversLicenseNumber (persona:DriversLicenseNumber, 1..1)
#            ExpirationDateIdentifier (ent00000054, 1..1)
#  Optional: AdditionalName (ent00000003, 0..1), PostalAddress (ent00000010, 0..1)
#            IssuingJurisdiction (persona:IssuingJurisdiction, 0..1)
#            Photo (persona:hasPhoto, 0..1)
#################################################################

:DriversLicenseDocumentShape
    a sh:NodeShape ;
    sh:targetClass persona:DriversLicense ;
    sh:message "Driver's license document validation: name, date of birth, license number, and expiration date are required."@en ;

    # ── Name: FullName OR (GivenName + FamilyName) ───────────────────────────
    sh:or (
        [
            sh:property [
                sh:path <https://purl.org/cco/ont00001879> ;
                sh:qualifiedValueShape [ sh:class cco:ent00000001 ] ;
                sh:qualifiedMinCount 1 ;
                sh:message "A DriversLicense must record a FullName, OR provide GivenName + FamilyName."@en
            ]
        ]
        [
            sh:and (
                [
                    sh:property [
                        sh:path <https://purl.org/cco/ont00001879> ;
                        sh:qualifiedValueShape [ sh:class cco:ent00000002 ] ;
                        sh:qualifiedMinCount 1 ;
                        sh:message "If no FullName is recorded, a DriversLicense must include at least one GivenName."@en
                    ]
                ]
                [
                    sh:property [
                        sh:path <https://purl.org/cco/ont00001879> ;
                        sh:qualifiedValueShape [ sh:class cco:ent00000004 ] ;
                        sh:qualifiedMinCount 1 ;
                        sh:message "If no FullName is recorded, a DriversLicense must include at least one FamilyName."@en
                    ]
                ]
            )
        ]
    ) ;

    # ── Required: DateOfBirth, LicenseNumber, ExpirationDate ─────────────────
    sh:property [
        sh:path <https://purl.org/cco/ont00001879> ;
        sh:qualifiedValueShape [ sh:class cco:ent00000046 ] ;  # Birthdate
        sh:qualifiedMinCount 1 ;
        sh:qualifiedMaxCount 1 ;
        sh:message "A DriversLicense must record exactly one DateOfBirth."@en
    ] ;

    sh:property [
        sh:path <https://purl.org/cco/ont00001879> ;
        sh:qualifiedValueShape [ sh:class persona:DriversLicenseNumber ] ;
        sh:qualifiedMinCount 1 ;
        sh:qualifiedMaxCount 1 ;
        sh:message "A DriversLicense must record exactly one DriversLicenseNumber."@en
    ] ;

    sh:property [
        sh:path <https://purl.org/cco/ont00001879> ;
        sh:qualifiedValueShape [ sh:class cco:ent00000054 ] ;  # ExpirationDateIdentifier
        sh:qualifiedMinCount 1 ;
        sh:qualifiedMaxCount 1 ;
        sh:message "A DriversLicense must record exactly one ExpirationDateIdentifier."@en
    ] ;

    # ── Optional fields ──────────────────────────────────────────────────────
    sh:property [
        sh:path <https://purl.org/cco/ont00001879> ;
        sh:qualifiedValueShape [ sh:class cco:ent00000003 ] ;  # AdditionalName
        sh:qualifiedMaxCount 1 ;
        sh:message "A DriversLicense may record at most one AdditionalName."@en
    ] ;

    sh:property [
        sh:path <https://purl.org/cco/ont00001879> ;
        sh:qualifiedValueShape [ sh:class cco:ent00000010 ] ;  # USPostalAddress
        sh:qualifiedMaxCount 1 ;
        sh:message "A DriversLicense may record at most one residential address."@en
    ] ;

    sh:property [
        sh:path <https://purl.org/cco/ont00001879> ;
        sh:qualifiedValueShape [ sh:class persona:IssuingJurisdiction ] ;
        sh:qualifiedMaxCount 1 ;
        sh:message "A DriversLicense may record at most one IssuingJurisdiction."@en
    ] ;

    sh:property [
        sh:path persona:hasPhoto ;
        sh:maxCount 1 ;
        sh:datatype xsd:anyURI ;
        sh:message "A DriversLicense may record at most one photo."@en
    ] .
```
