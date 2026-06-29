---
id: https://www.example.org/mia/contexts/bhs-group.members(boston-hub-society)(affiliations)(01)
title: "About Boston Hub Society in the Groups context as asserted by Boston Hub Society"
type: context-databook
version: 2.0.4
created: 2026-06-12
description: >
  The Boston Hub Society group instance, with Alice and Bob as members.
  A g:Group context assertable by any permitted member.
mia:
  category: "http://www.example.org/mia/categories/boston-hub-society(affiliations)"
  assertedBy: ":BHS_Group"
  subject: ":BHS_Group"
  about-by: "context:OBOcontext"
graph:
  named_graph: https://www.example.org/mia/contexts/bhs-group.members(boston-hub-society)(affiliations)(01)#graph
  rdf_version: "1.1"
shapes:
  - http://www.example.org/shapes
process:
  transformer: human
  timestamp: 2026-06-19T00:00:00Z
  agent:
    name: Paul Trevithick
    role: author
---

## Overview

This context captures the Boston Hub Society as a `g:Group` entity. It records the group's membership: Alice Walker (`:Self`) and Bob Johnson (`:Bob_Johnson`). Any permitted member may assert or update this context.

## Identity Data

```turtle
<!-- databook:id: bhs-group-identity -->
<!-- databook:graph: https://www.example.org/mia/contexts/bhs-group.members(boston-hub-society)(affiliations)(01)#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix g: <http://mee.foundation/ontologies/group#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:BHS_Group rdf:type owl:NamedIndividual ,
                    g:Group ;
    rdfs:label "Boston Hub Society"@en ;
    rdfs:comment "The Boston Hub Society group instance."@en ;
    <http://purl.obolibrary.org/obo/BFO_0000115> :Self ;        # has member part → Alice
    <http://purl.obolibrary.org/obo/BFO_0000115> :Bob_Johnson . # has member part → Bob
```
