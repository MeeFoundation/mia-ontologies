---
id: http://www.example.org/mia/categories/finances
title: "Finances"
type: category-databook
version: 1.0.2
created: 2026-06-24
description: >
  Example copy of the Finances cell DataBook, extended with Alice's user-defined financial institution cells.
  
  Split in this version into a paired -cell DataBook (mia.forCell) that holds
  this cell's content facts (num-parties, sbs/obs/sbo/obo, graph, note, folder);
  this file now holds only its cat:Category tree-position facts.
mia:
  catType: "Finances"
  copiedFrom: "http://mee.foundation/ontologies/categories-person/finances"
  child:
    - "http://www.example.org/mia/categories/banking-payments(finances)"
  forCell: "http://www.example.org/mia/categories/finances-cell"
---
