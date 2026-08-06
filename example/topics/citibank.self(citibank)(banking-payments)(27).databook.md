---
id: https://www.example.org/mia/topics/citibank.self(citibank)(banking-payments)(27)
title: "About Citibank in the BankingPayments cell as claimed by Alice Walker"
type: topic-databook
version: 1.0.0
created: 2026-08-02
description: >
  Alice Walker's own self-claimed notes about Citibank as an institution, alongside
  Citibank's own claimed record about Alice (topic 09) — the two distinct subjects
  (`:Self`, `:Citibank`) this `cell:TwoMember` cell's `memberTopics` must cover.
mia:
  claimant: ":Self"
  subject: ":Citibank"
graph:
  named_graph: https://www.example.org/mia/topics/citibank.self(citibank)(banking-payments)(27)#graph
  rdf_version: "1.1"
shapes:
  - http://mee.foundation/ontologies/persona/shapes
  - http://mee.foundation/ontologies/topic/shapes
process:
  transformer: human
  timestamp: 2026-08-02T00:00:00Z
  agent:
    name: Paul Trevithick
    role: author
---

## Overview

This topic captures Alice Walker's own self-claimed notes about Citibank as an institution — her own record of the organization, distinct from Citibank's own claimed record about her (topic 09). Together the two topics give this cell's `memberTopics` the two distinct subjects (`:Self`, `:Citibank`) required for a `cell:TwoMember` cell.

## Topic Graph

```turtle
<!-- databook:id: alice-citibank-org-topic-graph -->
<!-- databook:graph: https://www.example.org/mia/topics/citibank.self(citibank)(banking-payments)(27)#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix o: <http://mee.foundation/ontologies/organization#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Citibank rdf:type owl:NamedIndividual ,
                   o:Organization ;
    rdfs:label "Citibank"@en ;

    <https://purl.org/cco/ont00001917> [  # described by → Organization Note
        rdf:type cco:ent00000048 ;
        <https://purl.org/cco/ont00001765> "My primary checking account is here — used for rent and bill-pay autopay. Opened 2019."
    ] .
```
