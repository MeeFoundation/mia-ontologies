---
id: http://mee.foundation/ontologies/categories-person/people
title: "People"
type: category-databook
version: 1.0.5
created: 2026-06-22
description: >
  Cell DataBook for the People cell. Groups context DataBooks about interactions with individual people in the user's life.
  
  Split in this version into a paired -cell DataBook (mia.forCell) that holds
  this cell's content facts (num-parties, sbs/obs/sbo/obo, graph, note, folder);
  this file now holds only its cat:Category tree-position facts.
mia:
  catType: "People"
  child:
    - "http://mee.foundation/ontologies/categories-person/immediate-family"
    - "http://mee.foundation/ontologies/categories-person/extended-family"
    - "http://mee.foundation/ontologies/categories-person/in-laws-step-family"
    - "http://mee.foundation/ontologies/categories-person/friends"
    - "http://mee.foundation/ontologies/categories-person/others"
  forCell: "http://mee.foundation/ontologies/categories-person/people-cell"
---
