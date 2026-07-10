---
id: http://www.example.org/mia/categories/people
title: "People"
type: category-databook
version: 1.0.4
created: 2026-06-24
description: >
  Example copy of the People cell DataBook, extended with Alice's user-defined person cells.
  
  Split in this version into a paired -cell DataBook (mia.forCell) that holds
  this cell's content facts (num-parties, sbs/obs/sbo/obo, graph, note, folder);
  this file now holds only its cat:Category tree-position facts.
mia:
  catType: "People"
  copiedFrom: "http://mee.foundation/ontologies/categories-person/people"
  child:
    - "http://www.example.org/mia/categories/immediate-family(people)"
    - "http://www.example.org/mia/categories/friends(people)"
    - "http://www.example.org/mia/categories/others(people)"
  forCell: "http://www.example.org/mia/categories/people-cell"
---
