# Apple Contacts Integration Notes

## Overview

Mia is a strict superset of Apple Contacts in every dimension. This means importing from Apple Contacts into Mia is straightforward, but exporting from Mia back to Apple Contacts requires explicit design decisions. Round-tripping losslessly is achievable but requires an anchor strategy (see below).

There are two levels to address:

---

## Level 1: Contacts ↔ Contexts

A single Apple Contacts record (vCard / CNContact) maps cleanly to a single Mia context. All standard vCard fields have direct counterparts in the persona ontology: names, phone numbers, email addresses, postal addresses, organization, job title, birthday, anniversary, photo, notes, social profiles, URLs, related names.

**Import (Apple Contacts → Mia):** straightforward. Each contact record becomes a context DataBook. Field mapping is 1:1 for all standard vCard fields.

**Export (Mia → Apple Contacts):** more complex. Mia may hold multiple contexts for the same person (work, personal, family, etc.). Two possible policies:

1. **Primary context**: designate one context per person as the Apple Contacts source; export only that one. Simple and lossless in the other direction if the source context is tagged.
2. **Merge**: combine fields from all contexts into a single vCard. Risk of collisions (e.g. two "work" phone numbers from different contexts).

The primary-context policy is recommended for an initial integration.

---

## Level 2: Groups ↔ c:UserDefined Categories

Apple Contacts groups are **flat** (one level only) and untyped. Mia's category tree is hierarchical and typed (`c:TwoParty`, `c:MultiParty`, `c:UserDefined`, etc.).

**Import (Apple Contacts → Mia):** each Apple group becomes a leaf-level `c:TwoParty` or `c:UserDefined` category. No hierarchy is lost since Apple groups have none.

**Export (Mia → Apple Contacts):** the hierarchy must be flattened. Two options:

1. **Path encoding**: encode the hierarchy in the Apple group name using a separator, e.g. Mia category `People > Family` becomes Apple group `"People/Family"`. Ugly but survives the round-trip — on re-import, parse the separator to restore the tree.
2. **Leaf-only sync**: export only leaf-level categories and discard the hierarchy. Simpler but lossy — the hierarchy cannot be restored on re-import.

Path encoding is recommended if lossless round-tripping is required.

---

## Anchor Strategy (Key to Losslessness)

vCard supports custom extension fields (`X-` prefix). Storing Mia IRIs in these fields lets Mia re-identify records on re-import without duplication or drift:

- `X-MIA-CONTEXT-IRI` on a contact record — points to the Mia context DataBook IRI
- `X-MIA-CATEGORY-IRI` on a group — points to the Mia category DataBook IRI

These fields are ignored by Apple Contacts and other vCard consumers but survive export/import cycles, making true lossless round-tripping achievable.

---

## Summary

| Dimension | Import | Export | Lossless? |
|-----------|--------|--------|-----------|
| Contact fields | Direct field mapping | Map back from primary context | Yes, with primary-context tag |
| Multiple contexts per person | Each → separate DataBook | Requires primary-context policy | Yes, with policy |
| Group hierarchy | Flat → leaf categories | Encode as path in group name | Yes, with path encoding |
| Mia-specific metadata | Stored in context DataBook | Store IRI in `X-MIA-*` vCard field | Yes, with anchor fields |
