---
id: http://www.example.org/mia/categories/categories
title: "Cells"
type: category-databook
version: 1.0.2
created: 2026-06-24
description: >
  Root cell DataBook for Alice's example instance. Parent of all top-level cells.
  
  Split in this version into a paired -cell DataBook (mia.forCell) that holds
  this cell's content facts (num-parties, sbs/obs/sbo/obo, graph, note, folder);
  this file now holds only its cat:Category tree-position facts.
mia:
  catType: "Cell"
  copiedFrom: "http://mee.foundation/ontologies/categories-person/categories-person"
  child:
    - "http://www.example.org/mia/categories/people"
    - "http://www.example.org/mia/categories/work"
    - "http://www.example.org/mia/categories/companies"
    - "http://www.example.org/mia/categories/finances"
    - "http://www.example.org/mia/categories/government"
    - "http://www.example.org/mia/categories/ownership"
    - "http://www.example.org/mia/categories/affiliations"
  forCell: "http://www.example.org/mia/categories/categories-cell"
---
