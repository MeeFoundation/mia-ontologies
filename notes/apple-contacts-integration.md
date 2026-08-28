# Apple Contacts Integration Notes

## Overview

Cellula is a strict superset of Apple Contacts in every dimension. This means importing from Apple Contacts into the app is straightforward, but exporting from the app back to Apple Contacts requires explicit design decisions. Round-tripping losslessly is achievable but requires an anchor strategy (see below).

There are two levels to address:

---

## Level 1: Contacts ↔ Graphs

Apple Contacts' core design assumption is **one card per person**, with all graphs flattened into it. vCard accommodates multiple graphs by allowing optional labels on repeatable fields — a person can have two email addresses, one labeled `work` and one labeled `home`. This is vCard's mechanism for expressing graph.

The app follows the same design assumption. When exporting a person to Apple Contacts, **all N of that person's graphs are merged into a single vCard**. Each field value carries the label from the graph it came from (e.g. a phone number from a work graph gets the `work` label). If two different work graphs both contribute a phone number, the vCard will have two `work` phone numbers — this is correct and consistent with how vCard works.

**Import (Apple Contacts → the app):** each contact record becomes a graph DataBook. All standard vCard fields have direct counterparts in the persona ontology: names, phone numbers, email addresses, postal addresses, organization, job title, birthday, anniversary, photo, notes, social profiles, URLs, related names.

**Export (the app → Apple Contacts):** merge all graphs for the person into a single vCard. Map each field's graph (work, personal, family, etc.) to the corresponding vCard label. Multiple values under the same label are permitted and expected.

### vCard label constraints

**Number of values:** the vCard spec (RFC 6350) imposes no maximum on repeatable properties — `TEL`, `EMAIL`, `ADR` etc. can appear as many times as needed. Apple Contacts also imposes no hard cap in its data model. A person with phone numbers across many graphs will export cleanly regardless of count.

**Label string length:** vCard's `TYPE` parameter supports predefined types (`work`, `home`, `cell`, etc.) and custom types, stored with an `X-` prefix in vCard 3.0 (e.g. `TYPE=X-Acme-Corp`) or as free strings in vCard 4.0. The vCard spec sets no maximum length for `TYPE` values. However, Apple Contacts has an undocumented practical limit on how much of a custom label it displays in the UI — long labels (e.g. `"Boston Hub Society"`, `"California DMV"`) may be truncated visually even though the full string is preserved in the underlying vCard data. Round-trip fidelity of the data is unaffected; this is purely a display concern.

This display truncation limit is not publicly documented by Apple and likely varies by OS version. It should be verified empirically once an early implementation exists.

---

## Level 2: Groups ↔ c:UserDefined Categories

Apple Contacts groups are **flat** (one level only) and untyped. The app's category tree is hierarchical and typed (`c:TwoMember`, `c:MultiMember`, `c:UserDefined`, etc.).

**Import (Apple Contacts → the app):** each Apple group becomes a leaf-level `c:TwoMember` or `c:UserDefined` category. No hierarchy is lost since Apple groups have none.

**Export (the app → Apple Contacts):** the hierarchy must be flattened. Two options:

1. **Path encoding**: encode the hierarchy in the Apple group name using a separator, e.g. category `People > Family` becomes Apple group `"People/Family"`. Survives the round-trip — on re-import, parse the separator to restore the tree.
2. **Leaf-only sync**: export only leaf-level categories and discard the hierarchy. Simpler but lossy — the hierarchy cannot be restored on re-import.

Path encoding is recommended if lossless round-tripping is required.

---

## Anchor Strategy (Key to Losslessness)

vCard supports custom extension fields (`X-` prefix). Storing app IRIs in these fields lets the app re-identify records on re-import without duplication or drift:

- `X-CELLULA-PERSON-IRI` on a contact record — points to the `p:Person` individual IRI
- `X-CELLULA-CATEGORY-IRI` on a group — points to the category DataBook IRI

These fields are ignored by Apple Contacts and other vCard consumers but survive export/import cycles, making true lossless round-tripping achievable.

---

## Summary

| Dimension | Import | Export | Lossless? |
|-----------|--------|--------|-----------|
| Contact fields | Direct field mapping | Merge all graphs into one vCard | Yes, with `X-CELLULA-PERSON-IRI` anchor |
| Multiple graphs per person | Each → separate DataBook | Flatten to single vCard; multiple values per label are correct | Yes |
| Group hierarchy | Flat → leaf categories | Encode as path in group name | Yes, with path encoding |
| App-specific metadata | Stored in graph DataBook | Store IRI in `X-CELLULA-*` vCard field | Yes, with anchor fields |
