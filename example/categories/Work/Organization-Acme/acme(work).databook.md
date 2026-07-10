---
id: http://www.example.org/mia/categories/acme(work)
title: "Acme"
type: category-databook
version: 1.0.4
created: 2026-06-23
description: >
  UserDefined cell DataBook for Alice's employer, Acme. Child of the Work cell.
  
  Split in this version into a paired -cell DataBook (mia.forCell) that holds
  this cell's content facts (num-parties, sbs/obs/sbo/obo, graph, note, folder);
  this file now holds only its cat:Category tree-position facts.
mia:
  catType: "Organization"
  child: "http://www.example.org/mia/categories/employees(acme)"
  forCell: "http://www.example.org/mia/categories/acme(work)-cell"
---
