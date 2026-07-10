---
id: http://mee.foundation/ontologies/categories-person/state
title: "State"
type: category-databook
version: 1.0.3
created: 2026-06-22
description: >
  Cell DataBook for the State cell. Groups context DataBooks about state government credentials and records. Child of Government.
  
  Split in this version into a paired -cell DataBook (mia.forCell) that holds
  this cell's content facts (num-parties, sbs/obs/sbo/obo, graph, note, folder);
  this file now holds only its cat:Category tree-position facts.
mia:
  catType: "State"
  child:
    - "http://mee.foundation/ontologies/categories-person/birth-certificate"
    - "http://mee.foundation/ontologies/categories-person/drivers-license"
  forCell: "http://mee.foundation/ontologies/categories-person/state-cell"
---
