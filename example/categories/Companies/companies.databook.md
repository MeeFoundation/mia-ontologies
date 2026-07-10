---
id: http://www.example.org/mia/categories/companies
title: "Companies"
type: category-databook
version: 1.0.1
created: 2026-06-24
description: >
  Example copy of the Companies cell DataBook, extended with Alice's user-defined company cells.
  
  Split in this version into a paired -cell DataBook (mia.forCell) that holds
  this cell's content facts (num-parties, sbs/obs/sbo/obo, graph, note, folder);
  this file now holds only its cat:Category tree-position facts.
mia:
  catType: "Companies"
  copiedFrom: "http://mee.foundation/ontologies/categories-person/companies"
  child:
    - "http://www.example.org/mia/categories/google(companies)"
    - "http://www.example.org/mia/categories/att(companies)"
  forCell: "http://www.example.org/mia/categories/companies-cell"
---
