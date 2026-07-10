---
id: http://www.example.org/mia/categories/medical-providers
title: "Providers"
type: category-databook
version: 1.0.1
created: 2026-07-09
description: >
  Example copy of the Medical Providers cell DataBook. Child of Alice's Medical cell.
  
  Split in this version into a paired -cell DataBook (mia.forCell) that holds
  this cell's content facts (num-parties, sbs/obs/sbo/obo, graph, note, folder);
  this file now holds only its cat:Category tree-position facts.
mia:
  catType: "MedicalProviders"
  copiedFrom: "http://mee.foundation/ontologies/categories-person/medical-providers"
  child:
    - "http://www.example.org/mia/categories/jane-kopakolva"
    - "http://www.example.org/mia/categories/alice-carol-about-mom(health)"
  forCell: "http://www.example.org/mia/categories/medical-providers-cell"
---
