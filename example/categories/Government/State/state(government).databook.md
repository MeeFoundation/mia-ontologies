---
id: http://www.example.org/mia/categories/state(government)
title: "State"
type: category-databook
version: 1.0.1
created: 2026-06-24
description: >
  Example copy of the State cell DataBook, extended with Alice's user-defined state agency cells.
  
  Split in this version into a paired -cell DataBook (mia.forCell) that holds
  this cell's content facts (num-parties, sbs/obs/sbo/obo, graph, note, folder);
  this file now holds only its cat:Category tree-position facts.
mia:
  catType: "State"
  copiedFrom: "http://mee.foundation/ontologies/categories-person/state"
  child:
    - "http://www.example.org/mia/categories/texas-vital-records(state)"
    - "http://www.example.org/mia/categories/california-dmv(state)"
  forCell: "http://www.example.org/mia/categories/state(government)-cell"
---
