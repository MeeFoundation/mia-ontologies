---
id: http://www.example.org/mia/categories/med-app-info(medical-appointment-info)-cell
title: "Med. App. Info (Cell)"
type: cell-databook
version: 1.0.14
created: 2026-07-10
description: >
  Cell DataBook of category "Med. App. Info" (mia.catType: MedicalAppointmentInfo). Content may include topics/folder/note links, and may carry one or two required subject values. Since this cell has a single subject (Paula), her own topic is linked via otherTopics rather than memberTopics — the two memberTopics values belong to the two active members (Carol and Self), per CLAUDE.md Check 18.
mia:
  creator: ":Self"
  memberCount: "cell:TwoMember"
  subject: ":Paula_Walker"
  memberTopics:
    - "https://www.example.org/mia/topics/carol-walker.carol-walker(med-app-info)(medical-appointment-info)(28)"
    - "https://www.example.org/mia/topics/self.self(med-app-info)(medical-appointment-info)(30)"
  otherTopics:
    - "https://www.example.org/mia/topics/paula-walker.self(med-app-info)(medical-appointment-info)(26)"
  folder: "People/Immediate Family/Paula Walker/Health & Wellness/Medical/Providers/Med. App. Info"
  shape: "pshapes:MedicalAppointmentRecordShape"
---
