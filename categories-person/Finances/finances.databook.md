---
id: http://mee.foundation/ontologies/categories-person/finances
title: "Finances"
type: category-databook
version: 1.0.2
created: 2026-06-23
description: >
  Cell DataBook for the Finances cell. Groups context DataBooks about personal finances and relationships with financial institutions. Child of Cells.
  
  Split in this version into a paired -cell DataBook (mia.forCell) that holds
  this cell's content facts (num-parties, sbs/obs/sbo/obo, graph, note, folder);
  this file now holds only its cat:Category tree-position facts.
mia:
  catType: "Finances"
  child:
    - "http://mee.foundation/ontologies/categories-person/banking-payments"
    - "http://mee.foundation/ontologies/categories-person/investing"
    - "http://mee.foundation/ontologies/categories-person/lending-credit"
    - "http://mee.foundation/ontologies/categories-person/insurance"
    - "http://mee.foundation/ontologies/categories-person/advisory"
  forCell: "http://mee.foundation/ontologies/categories-person/finances-cell"
---
