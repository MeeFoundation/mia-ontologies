---
id: http://www.example.org/mia/categories/employees(acme)
title: "Employees"
type: category-databook
version: 1.0.3
created: 2026-06-24
description: >
  Canonical Employees cell scoped to Alice's Acme work context. Groups the Acme colleagues Alice tracks.
  
  Split in this version into a paired -cell DataBook (mia.forCell) that holds
  this cell's content facts (num-parties, sbs/obs/sbo/obo, graph, note, folder);
  this file now holds only its cat:Category tree-position facts.
mia:
  catType: "Employees"
  copiedFrom: "http://mee.foundation/ontologies/categories-org/employees"
  child:
    - "http://www.example.org/mia/categories/paula-walker(acme)"
    - "http://www.example.org/mia/categories/alice-walker(acme)"
  forCell: "http://www.example.org/mia/categories/employees(acme)-cell"
---
