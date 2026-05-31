# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an **RDF/OWL ontology project** — a formal semantic knowledge model for representing natural people's identity data in the Mee Identity Agent (MIA). It is an *application ontology*: it imports and profiles existing domain ontologies, documenting which classes and properties Mee uses, and extends them with Mee-specific terms.

There are no build, compile, test, or lint commands. The files are Turtle (`.ttl`) loaded into semantic web tools (Protégé).

## Core Files

| File | Purpose |
|------|---------|
| `persona.ttl` | Main application ontology — imports domain ontologies, annotates which classes/properties are required vs. optional for Mee |
| `persona-shacl.ttl` | SHACL validation shapes — constraint rules for valid instance data (e.g., a BirthCertificate Persona must have FullName OR GivenName+FamilyName) |
| `example/self/self.ttl` | Alice Walker's selfness — the central Person instance; imports all context files |
| `example/contexts/citibank.ttl` | Alice's Citibank Persona — payment card |
| `example/contexts/boston.ttl` | Alice's Boston Persona — residential address 2020–2025 |
| `example/contexts/paradise.ttl` | Alice's Paradise Persona — current residential address |
| `example/contexts/family.ttl` | Alice's Family Persona — family relationships and social network |
| `example/contexts/colleagues.ttl` | Alice's Colleagues Persona — professional relationships and social network |
| `example/contexts/att.ttl` | Alice's AT&T Persona — phone number |
| `example/contexts/ssa.ttl` | Alice's SSA Persona — Social Security Number |
| `example/contexts/google.ttl` | Alice's Google Persona — email address |
| `example/contexts/texas-birth-certificate.ttl` | Alice's Texas Birth Certificate Persona — legal name record |
| `example/contexts/florida-birth-certificate.ttl` | Paula Walker's Florida Birth Certificate Persona — legal name record |
| `project_files/` | Reference materials: imported domain ontologies (PersonOntology.ttl, AddressOntology.ttl, StagingOntology.ttl), BFO/CCO source files, PDFs, docs |

## Architecture

### Three-Layer Design

```
example/self/self.ttl (selfness)
  ├─ imports → persona.ttl (application profile)
  │             ├─ imports → PersonOntology.ttl
  │             ├─ imports → AddressOntology.ttl
  │             └─ imports → StagingOntology.ttl
  │                           └─ imports → BFO terms
  ├─ imports → example/contexts/citibank.ttl
  ├─ imports → example/contexts/boston.ttl
  ├─ imports → example/contexts/paradise.ttl
  ├─ imports → example/contexts/family.ttl
  ├─ imports → example/contexts/colleagues.ttl
  ├─ imports → example/contexts/att.ttl
  ├─ imports → example/contexts/ssa.ttl
  ├─ imports → example/contexts/google.ttl
  ├─ imports → example/contexts/texas-birth-certificate.ttl
  └─ imports → example/contexts/florida-birth-certificate.ttl

persona-shacl.ttl
  └─ imports → example/self/self.ttl (which transitively imports everything above)
```

1. **Foundation**: BFO (Basic Formal Ontology) — provides temporal modeling (`TemporalInterval`) and core relations
2. **Domain Ontologies** (in `project_files/`): PersonOntology, AddressOntology, StagingOntology
3. **Application Ontology** (`persona.ttl`): aggregates domain ontologies; uses annotation properties (`usesRequiredClass`, `usesOptionalClass`, `usesCCOClass`, `usesCCOProperty`) to document Mee's usage

### Key Architectural Patterns

**Selfness and Personas**: A Person's selfness (`self.ttl`) is the central identity individual. It carries only properties intrinsic to the person (physical characteristics, parent-child relationships). All other data — names, identifiers, addresses, payment cards — belongs to context-specific Personas, each in its own file.

**Peer name pattern** (not hierarchical): All name types (FullName, GivenName, FamilyName, AlternateName) connect directly to a Persona via `ont00001879` (designated by). They are siblings, not nested. Names belong to BirthCertificate Personas, not to the selfness.

**Address history pattern**: `AddressDesignation` links Person → Address → `TemporalInterval`. Open-ended intervals (no `hasEndDate`) indicate current address. See `TEMPORAL_TRACKING_SOLUTION.md` for details.

### Key Identifiers

Classes and properties use numeric IRIs. The most common:

- `ont00001262` = Person
- `ont00001879` = designated by (Person ← name/identifier)
- `ont00001765` = has text value (designator → literal string)
- `ent00000001`–`ent00000006` = name types (FullName, GivenName, AdditionalName, FamilyName, _, AlternateName)
- `ent00000008` = SSN; `ent00000023` = Phone; `ent00000024` = Email
- `ent00000010` = PostalAddress; `ent00000016` = AddressDesignation
- `BFO_0000038` = TemporalInterval; `ent00000017/18` = hasStartDate/hasEndDate

## Versioning

Before committing any change to `self.ttl`, any context file, `persona.ttl`, or `persona-shacl.ttl`, increment the **minor version number** in that file's `owl:versionInfo` annotation and update the description to summarise the change. For example:

```
owl:versionInfo "Version 3.0.3 - added social network"@en
```
becomes:
```
owl:versionInfo "Version 3.0.4 - added birth date"@en
```

## Keeping Files in Sync

Whenever changes are made to `self.ttl`, any context file, or `persona.ttl`, `persona-shacl.ttl` must be updated to match:

- **New property usage in a context file or `self.ttl`** (e.g., a new physical characteristic, relationship, or identifier added to a Person or Persona instance) → add or extend a SHACL shape to validate that property on the relevant target class.
- **New class or property defined in `persona.ttl`** (e.g., `persona:hasSocialNetwork`) → add a SHACL shape that constrains how instances of the domain class may or must use it.

Always update `persona-shacl.ttl` in the same edit session as the change that triggers it.

## Validation

**SHACL validation** (e.g., using Apache Jena's `shaclvalidate`):
```bash
shaclvalidate -datafile example/self/self.ttl -shapesfile persona-shacl.ttl
```

**Protégé**: Load `persona.ttl`; Protégé will import the domain ontologies via IRI resolution. Use the reasoner (HermiT/Pellet) to check consistency.

## Gitignore Notes

`catalog-v001.xml` and `/project_files` are gitignored (Protégé IDE artifacts). The `project_files/` directory exists locally but is not tracked — it contains source domain ontologies and reference documents.
