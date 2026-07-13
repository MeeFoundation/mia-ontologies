---
id: http://mee.foundation/ontologies/categories-person/birth-certificate-cell
title: "Birth Certificate (Cell)"
type: cell-databook
version: 1.0.5
created: 2026-07-10
description: >
  Cell DataBook of category "Birth Certificate" (mia.catType: BirthCertificate). Content may include sc-context/folder/note links, and may contain a named graph. Also embeds this canonical cell's per-template SHACL shape (persona:BirthCertificate, fragment #shapes) as validation metadata — never cloned into user copies.
mia:
  parties: "cell:OneParty"
---

## SHACL Shapes

This canonical cell embeds the per-template SHACL shape applied to context files carrying `mia.template: "persona:BirthCertificate"` (Tier 2 validation — see README `## Validation`). This block is validation metadata attached to the canonical cell only — it is never cloned when this category is copied into a user's tree (see [Lazy Copying](../../../../README.md#lazy-copying)).

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

<http://mee.foundation/ontologies/persona/shapes/birthcertificate> rdf:type owl:Ontology ;
    owl:imports <http://mee.foundation/ontologies/persona> ;
    dc:date "2026-07-13"^^xsd:date ;
    owl:versionInfo "Version 1.0.5 - moved out of standalone shacl/birthcertificate-shacl.ttl into an embedded turtle block (fragment #shapes) inside the canonical cell-databook categories-person/Government/State/Birth Certificate/birth-certificate-cell.databook.md; IRI unchanged."@en ;
    rdfs:label "Birth Certificate Template SHACL Shapes"@en ;
    rdfs:comment """SHACL shapes for validating context files carrying context:template persona:BirthCertificate.
                    Apply in addition to persona-shacl.ttl when validating a birth certificate context file.
                    Targets persona:BirthCertificate document individuals directly — identity claims
                    (names, designators) are properties of the document, not the Person."""@en .


#################################################################
#  Birth Certificate Document Shape
#  Targets persona:BirthCertificate individuals.
#  All identity claims are properties of the document individual.
#  Required: FullName (1..1) OR (GivenName (1..1) AND FamilyName (1..1))
#  Optional: AdditionalName (ent00000003), AlternateName (ent00000006),
#            Nickname, Legal Name
#################################################################

:BirthCertificateDocumentShape
    a sh:NodeShape ;
    sh:targetClass persona:BirthCertificate ;
    sh:message "Birth certificate document must record either FullName OR (GivenName + FamilyName)."@en ;

    # Name requirement: EITHER FullName OR (GivenName AND FamilyName)
    sh:or (
        [
            sh:property [
                sh:path <https://purl.org/cco/ont00001879> ;  # designated by
                sh:qualifiedValueShape [ sh:class cco:ent00000001 ] ;
                sh:qualifiedMinCount 1 ;
                sh:message "Birth certificate must record at least one FullName, OR provide GivenName + FamilyName."@en
            ]
        ]
        [
            sh:and (
                [
                    sh:property [
                        sh:path <https://purl.org/cco/ont00001879> ;  # designated by
                        sh:qualifiedValueShape [ sh:class cco:ent00000002 ] ;
                        sh:qualifiedMinCount 1 ;
                        sh:message "If no FullName is recorded, birth certificate must include at least one GivenName."@en
                    ]
                ]
                [
                    sh:property [
                        sh:path <https://purl.org/cco/ont00001879> ;  # designated by
                        sh:qualifiedValueShape [ sh:class cco:ent00000004 ] ;
                        sh:qualifiedMinCount 1 ;
                        sh:message "If no FullName is recorded, birth certificate must include at least one FamilyName."@en
                    ]
                ]
            )
        ]
    ) ;

    # Optional name components
    sh:property [
        sh:path <https://purl.org/cco/ont00001879> ;  # designated by
        sh:qualifiedValueShape [
            sh:or (
                [ sh:class cco:ent00000003 ]
                [ sh:class cco:ent00000005 ]
                [ sh:class cco:ent00000006 ]
                [ sh:class <https://purl.org/cco/ont00000990> ]  # Nickname
                [ sh:class <https://purl.org/cco/ont00001331> ]  # Legal Name
            )
        ] ;
        sh:qualifiedMaxCount 50 ;
        sh:message "Optional name designators are allowed (up to 50 total across these types)."@en
    ] .
```
