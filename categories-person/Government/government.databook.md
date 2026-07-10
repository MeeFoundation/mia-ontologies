---
id: http://mee.foundation/ontologies/categories-person/government
title: "Government"
type: category-databook
version: 1.0.1
created: 2026-06-22
description: >
  Cell DataBook for the Government cell. Groups context DataBooks about government-issued credentials, tax records, and civic relationships. Child of Cells.
  
  Split in this version into a paired -cell DataBook (mia.forCell) that holds
  this cell's content facts (num-parties, sbs/obs/sbo/obo, graph, note, folder);
  this file now holds only its cat:Category tree-position facts.
mia:
  catType: "Government"
  child:
    - "http://mee.foundation/ontologies/categories-person/state"
    - "http://mee.foundation/ontologies/categories-person/federal"
    - "http://mee.foundation/ontologies/categories-person/municipality"
  forCell: "http://mee.foundation/ontologies/categories-person/government-cell"
---
