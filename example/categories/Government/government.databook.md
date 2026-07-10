---
id: http://www.example.org/mia/categories/government
title: "Government"
type: category-databook
version: 1.0.1
created: 2026-06-24
description: >
  Example copy of the Government cell DataBook, extended with Alice's user-defined government agency cells.
  
  Split in this version into a paired -cell DataBook (mia.forCell) that holds
  this cell's content facts (num-parties, sbs/obs/sbo/obo, graph, note, folder);
  this file now holds only its cat:Category tree-position facts.
mia:
  catType: "Government"
  copiedFrom: "http://mee.foundation/ontologies/categories-person/government"
  child:
    - "http://www.example.org/mia/categories/state(government)"
    - "http://www.example.org/mia/categories/federal(government)"
    - "http://www.example.org/mia/categories/municipality(government)"
  forCell: "http://www.example.org/mia/categories/government-cell"
---
