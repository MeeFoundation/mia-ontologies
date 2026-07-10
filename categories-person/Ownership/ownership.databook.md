---
id: http://mee.foundation/ontologies/categories-person/ownership
title: "Ownership"
type: category-databook
version: 1.0.3
created: 2026-06-22
description: >
  Cell DataBook for the Ownership cell. Groups context DataBooks about owned assets, property, vehicles, and other possessions. Child of Cells.
  
  Split in this version into a paired -cell DataBook (mia.forCell) that holds
  this cell's content facts (num-parties, sbs/obs/sbo/obo, graph, note, folder);
  this file now holds only its cat:Category tree-position facts.
mia:
  catType: "Ownership"
  child:
    - "http://mee.foundation/ontologies/categories-person/vehicles"
  forCell: "http://mee.foundation/ontologies/categories-person/ownership-cell"
---
