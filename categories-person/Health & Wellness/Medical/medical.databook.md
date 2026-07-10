---
id: http://mee.foundation/ontologies/categories-person/medical
title: "Medical"
type: category-databook
version: 1.0.1
created: 2026-07-09
description: >
  Cell DataBook for the Medical cell. Groups context DataBooks about medical (as opposed to dental or vision) care. Child of Health & Wellness.
  
  Split in this version into a paired -cell DataBook (mia.forCell) that holds
  this cell's content facts (num-parties, sbs/obs/sbo/obo, graph, note, folder);
  this file now holds only its cat:Category tree-position facts.
mia:
  catType: "Medical"
  child:
    - "http://mee.foundation/ontologies/categories-person/medical-history"
    - "http://mee.foundation/ontologies/categories-person/medical-insurance"
    - "http://mee.foundation/ontologies/categories-person/medical-providers"
  forCell: "http://mee.foundation/ontologies/categories-person/medical-cell"
---
