# Apple Contacts Integration Notes

## Overview

Mia is a strict superset of Apple Contacts in every dimension. This means importing from Apple Contacts into Mia is straightforward, but exporting from Mia back to Apple Contacts requires explicit design decisions. Round-tripping losslessly is achievable but requires an anchor strategy (see below).

There are two levels to address:

---

## Level 1: Contacts ↔ Contexts

Apple Contacts' core design assumption is **one card per person**, with all contexts flattened into it. vCard accommodates multiple contexts by allowing optional labels on repeatable fields — a person can have two email addresses, one labeled `work` and one labeled `home`. This is vCard's mechanism for expressing context.

Mia follows the same design assumption. When exporting a person to Apple Contacts, **all N Mia contexts for that person are merged into a single vCard**. Each field value carries the label from the context it came from (e.g. a phone number from a work context gets the `work` label). If two different work contexts both contribute a phone number, the vCard will have two `work` phone numbers — this is correct and consistent with how vCard works.

**Import (Apple Contacts → Mia):** each contact record becomes a context DataBook. All standard vCard fields have direct counterparts in the persona ontology: names, phone numbers, email addresses, postal addresses, organization, job title, birthday, anniversary, photo, notes, social profiles, URLs, related names.

**Export (Mia → Apple Contacts):** merge all contexts for the person into a single vCard. Map each field's Mia context (work, personal, family, etc.) to the corresponding vCard label. Multiple values under the same label are permitted and expected.

### vCard label constraints

**Number of values:** the vCard spec (RFC 6350) imposes no maximum on repeatable properties — `TEL`, `EMAIL`, `ADR` etc. can appear as many times as needed. Apple Contacts also imposes no hard cap in its data model. A person with phone numbers across many Mia contexts will export cleanly regardless of count.

**Label string length:** vCard's `TYPE` parameter supports predefined types (`work`, `home`, `cell`, etc.) and custom types, stored with an `X-` prefix in vCard 3.0 (e.g. `TYPE=X-Acme-Corp`) or as free strings in vCard 4.0. The vCard spec sets no maximum length for `TYPE` values. However, Apple Contacts has an undocumented practical limit on how much of a custom label it displays in the UI — long labels (e.g. `"Boston Hub Society"`, `"California DMV"`) may be truncated visually even though the full string is preserved in the underlying vCard data. Round-trip fidelity of the data is unaffected; this is purely a display concern.

This display truncation limit is not publicly documented by Apple and likely varies by OS version. It should be verified empirically once an early implementation exists.

---

## Level 2: Groups ↔ c:UserDefined Categories

Apple Contacts groups are **flat** (one level only) and untyped. Mia's category tree is hierarchical and typed (`c:TwoParty`, `c:MultiParty`, `c:UserDefined`, etc.).

**Import (Apple Contacts → Mia):** each Apple group becomes a leaf-level `c:TwoParty` or `c:UserDefined` category. No hierarchy is lost since Apple groups have none.

**Export (Mia → Apple Contacts):** the hierarchy must be flattened. Two options:

1. **Path encoding**: encode the hierarchy in the Apple group name using a separator, e.g. Mia category `People > Family` becomes Apple group `"People/Family"`. Survives the round-trip — on re-import, parse the separator to restore the tree.
2. **Leaf-only sync**: export only leaf-level categories and discard the hierarchy. Simpler but lossy — the hierarchy cannot be restored on re-import.

Path encoding is recommended if lossless round-tripping is required.

---

## Anchor Strategy (Key to Losslessness)

vCard supports custom extension fields (`X-` prefix). Storing Mia IRIs in these fields lets Mia re-identify records on re-import without duplication or drift:

- `X-MIA-PERSON-IRI` on a contact record — points to the Mia `p:Person` individual IRI
- `X-MIA-CATEGORY-IRI` on a group — points to the Mia category DataBook IRI

These fields are ignored by Apple Contacts and other vCard consumers but survive export/import cycles, making true lossless round-tripping achievable.

---

## Summary

| Dimension | Import | Export | Lossless? |
|-----------|--------|--------|-----------|
| Contact fields | Direct field mapping | Merge all contexts into one vCard | Yes, with `X-MIA-PERSON-IRI` anchor |
| Multiple contexts per person | Each → separate DataBook | Flatten to single vCard; multiple values per label are correct | Yes |
| Group hierarchy | Flat → leaf categories | Encode as path in group name | Yes, with path encoding |
| Mia-specific metadata | Stored in context DataBook | Store IRI in `X-MIA-*` vCard field | Yes, with anchor fields |
