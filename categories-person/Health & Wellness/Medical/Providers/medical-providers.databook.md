---
id: http://mee.foundation/ontologies/categories-person/medical-providers
title: "Providers"
type: category-databook
version: 1.0.1
created: 2026-07-09
description: >
  Cell DataBook for the Medical Providers cell. Groups context DataBooks about medical providers and practices you see for care, including your primary care physician and any medical appointments you help arrange. Child of Medical.
  
  Split in this version into a paired -cell DataBook (mia.forCell) that holds
  this cell's content facts (num-parties, sbs/obs/sbo/obo, graph, note, folder);
  this file now holds only its cat:Category tree-position facts.
mia:
  catType: "MedicalProviders"
  child:
    - "http://mee.foundation/ontologies/categories-person/primary-care-physician"
    - "http://mee.foundation/ontologies/categories-person/medical-appointment-info"
  forCell: "http://mee.foundation/ontologies/categories-person/medical-providers-cell"
---
