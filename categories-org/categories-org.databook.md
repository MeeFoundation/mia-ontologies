---
id: http://mee.foundation/ontologies/categories-org/categories-org
title: "Cells (org)"
type: category-databook
version: 1.0.4
created: 2026-07-03
description: >
  Root cell DataBook for Organization cells. Parent of all top-level canonical organization cells.
  
  Split in this version into a paired -cell DataBook (mia.forCell) that holds
  this cell's content facts (num-parties, sbs/obs/sbo/obo, graph, note, folder);
  this file now holds only its cat:Category tree-position facts.
mia:
  catType: "Cell"
  child:
    - "http://mee.foundation/ontologies/categories-org/customers"
    - "http://mee.foundation/ontologies/categories-org/marketing"
    - "http://mee.foundation/ontologies/categories-org/partners"
    - "http://mee.foundation/ontologies/categories-org/people-org"
    - "http://mee.foundation/ontologies/categories-org/kb"
    - "http://mee.foundation/ontologies/categories-org/projects-org"
    - "http://mee.foundation/ontologies/categories-org/meetings-org"
    - "http://mee.foundation/ontologies/categories-org/suppliers"
    - "http://mee.foundation/ontologies/categories-org/legal-org"
    - "http://mee.foundation/ontologies/categories-org/government-org"
    - "http://mee.foundation/ontologies/categories-org/finances-org"
  forCell: "http://mee.foundation/ontologies/categories-org/categories-org-cell"
---
