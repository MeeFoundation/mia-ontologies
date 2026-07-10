---
id: http://www.example.org/mia/categories/municipality(government)
title: "Municipality"
type: category-databook
version: 1.0.1
created: 2026-06-24
description: >
  Example copy of the Municipality cell DataBook, extended with Alice's user-defined municipal cells.
  
  Split in this version into a paired -cell DataBook (mia.forCell) that holds
  this cell's content facts (num-parties, sbs/obs/sbo/obo, graph, note, folder);
  this file now holds only its cat:Category tree-position facts.
mia:
  catType: "Municipality"
  copiedFrom: "http://mee.foundation/ontologies/categories-person/municipality"
  child:
    - "http://www.example.org/mia/categories/boston(municipality)"
    - "http://www.example.org/mia/categories/paradise(municipality)"
  forCell: "http://www.example.org/mia/categories/municipality(government)-cell"
---
