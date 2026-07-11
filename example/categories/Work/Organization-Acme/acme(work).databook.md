---
id: http://www.example.org/mia/categories/acme(work)
title: "Acme"
type: category-databook
version: 1.0.7
created: 2026-06-23
description: >
  Cell DataBook for Alice's employer, Acme, a cat:Copy of the canonical
  Organization root. Child of the Work cell.
  
  Split in this version into a paired -cell DataBook that holds this cell's
  content facts (num-parties, sbs/obs/sbo/obo, graph, note, folder); this file
  now holds only its cat:Copy tree-position facts. The pairing is recorded
  on this side as mia.cell, the sole link between a node and its cell(s).
mia:
  catType: "Organization"
  cell: "http://www.example.org/mia/categories/acme(work)-cell"
  copiedFrom: "http://mee.foundation/ontologies/categories-org/categories-org"
  label: "Acme"
  child: "http://www.example.org/mia/categories/employees(acme)"
---
