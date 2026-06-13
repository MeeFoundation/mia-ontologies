# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an **RDF/OWL ontology project** — a formal semantic knowledge model for representing natural people's identity data in the Mee Identity Agent (MIA). It comprises two peer application ontologies:

- **Persona ontology** (`persona.ttl`): models identity data — names, addresses, identifiers, relationships, payment cards, and more — structured around context-specific `Persona` instances linked to a central `Person` entity. Imports and profiles existing domain ontologies, documenting which of their classes and properties Mee uses, and extends them with Mia-specific terms.
- **Context ontology** (`context.ttl`): defines controlled vocabularies for classifying context files — what broad category of interaction is involved (`contextType`), who asserted the data (`assertionType`), and whose identity the file describes (`subject`).

There are no build, compile, test, or lint commands. The files are Turtle (`.ttl`) loaded into semantic web tools (Protégé).

## Core Files

| File | Purpose |
|------|---------|
| `persona.ttl` | Persona ontology — imports domain ontologies, annotates which classes/properties are required vs. optional for Mee, defines Mia-specific classes and properties |
| `context.ttl` | Context ontology — controlled vocabularies for classifying context files (`contextType`, `assertionType`, `subject`) |
| `persona-shacl.ttl` | SHACL validation shapes — constraint rules for valid instance data (e.g., a BirthCertificate Persona must have FullName OR GivenName+FamilyName) |
| `example/alice/alice(self)alice.ttl` | Alice Walker's selfness — the central Person instance; imports all context files |
| `example/paula/paula(self)paula.ttl` | Paula Walker's selfness — the central Person instance for Paula |
| `example/bob/bob(self)bob.ttl` | Bob Johnson's selfness — the central Person instance for Bob |
| `example/alice-contexts/10-alice(citibank)alice.ttl` | Alice's Citibank Persona — payment card |
| `example/alice-contexts/15-alice(boston)alice.ttl` | Alice's Boston Persona — residential address 2020–2025 |
| `example/alice-contexts/14-alice(paradise)alice.ttl` | Alice's Paradise Persona — current residential address |
| `example/alice-contexts/18-alice(family)alice.ttl` | Alice's Family Persona — family relationships and social network |
| `example/alice-contexts/12-alice(att)alice.ttl` | Alice's AT&T Persona — phone number |
| `example/alice-contexts/16-alice(ssa)alice.ttl` | Alice's SSA Persona — Social Security Number |
| `example/alice-contexts/11-alice(google)alice.ttl` | Alice's Google Persona — email address |
| `example/alice-contexts/13-alice(tx-birth-cert)alice.ttl` | Alice's Texas Birth Certificate Persona — legal name record |
| `example/paula-contexts/under-development/paula(fl-birth-cert)alice.ttl` | Paula Walker's Florida Birth Certificate Persona — legal name record (under development) |
| `project_files/` | Reference materials: imported domain ontologies (PersonOntology.ttl, AddressOntology.ttl, StagingOntology.ttl), BFO/CCO source files, PDFs, docs |

## Architecture

### Three-Layer Design

```
example/alice/alice(self)alice.ttl (selfness)
  ├─ imports → persona.ttl (application profile)
  │             ├─ imports → PersonOntology.ttl
  │             ├─ imports → AddressOntology.ttl
  │             └─ imports → StagingOntology.ttl
  │                           └─ imports → BFO terms
  ├─ imports → example/alice-contexts/10-alice(citibank)alice.ttl
  ├─ imports → example/alice-contexts/15-alice(boston)alice.ttl
  ├─ imports → example/alice-contexts/14-alice(paradise)alice.ttl
  ├─ imports → example/alice-contexts/18-alice(family)alice.ttl
  ├─ imports → example/alice-contexts/12-alice(att)alice.ttl
  ├─ imports → example/alice-contexts/16-alice(ssa)alice.ttl
  ├─ imports → example/alice-contexts/11-alice(google)alice.ttl
  ├─ imports → example/alice-contexts/13-alice(tx-birth-cert)alice.ttl
  └─ imports → (plus bob-contexts, paula-contexts, bhs-contexts — see alice(self)alice.ttl)

persona-shacl.ttl
  └─ imports → example/alice/alice(self)alice.ttl (which transitively imports everything above)
```

1. **Foundation**: BFO (Basic Formal Ontology) — provides temporal modeling (`TemporalInterval`) and core relations
2. **Domain Ontologies** (in `project_files/`): PersonOntology, AddressOntology, StagingOntology
3. **Application Ontologies** (peer, not nested):
   - `persona.ttl`: aggregates domain ontologies; uses annotation properties (`usesRequiredClass`, `usesOptionalClass`, `usesCCOClass`, `usesCCOProperty`) to document Mee's usage
   - `context.ttl`: defines `contextType`, `assertionType`, and `subject` vocabularies; imported directly by each context file

### Context File Naming Convention

Context filenames encode a **right-to-left hierarchy** of contexts, reading from the outermost context inward toward the central "Self".

**Full unabbreviated structure** (one segment per hierarchy level, separated by `.`):
```
<about>(<context-name>)<asserted-by>.<about>(<context-name>)<asserted-by>. … .<about>(self)<asserted-by>.ttl
```

**Abbreviation rules applied in practice:**
1. The trailing `.(self)` segment (the central Self level) is always omitted.
2. In the second and subsequent segments, only `(<context-name>)` is kept — the `<about>` and `<asserted-by>` strings are omitted.

**Numeric prefix**: Context files that appear as labeled circles in `context-map.png` carry a zero-padded two-digit prefix matching their diagram label number: `NN-<about>(<context-name>)<asserted-by>[.(<parent-context>)].ttl` (e.g. `10-alice(citibank)alice.ttl`). Context files without a diagram label number have no prefix. Selfness files (`<X>(self)<X>.ttl`) never carry a prefix.

**Exception — `c:Group` contexts**: A group context (`contextCategory context:Group`) has no single asserter — any permitted member can write to it and changes replicate to all members. For group contexts, the `<asserted-by>` segment is replaced with the literal string `members` rather than an individual entity name. Example: `bhs(bhs)members.ttl` — about BHS, context "bhs", assertedBy the group's members collectively.

**Examples:**

| Filename | Full (unabbreviated) form | Meaning |
|----------|--------------------------|---------|
| `10-alice(citibank)alice.ttl` | `alice(citibank)alice.alice(self)alice.ttl` | About Alice, context "citibank", asserted by Alice; child of Alice's Self |
| `02-paula(paula)alice.(family).ttl` | `paula(paula)alice.alice(family)alice.alice(self)alice.ttl` | About Paula, context "paula", asserted by Alice; child of Alice's Family context |
| `05-bob(bob)alice.(bob).ttl` | `bob(bob)alice.alice(bob)alice.alice(self)alice.ttl` | About Bob, context "bob", asserted by Alice; child of Alice's Bob (1:1) context |
| `09-bob(bob)bob.(bhs).ttl` | `bob(bob)bob.alice(bhs)alice.alice(self)alice.ttl` | About Bob, context "bob", asserted by Bob; child of Alice's BHS context |
| `08-bhs(bhs)members.ttl` | `bhs(bhs)members.alice(self)alice.ttl` | About BHS, context "bhs", asserted by group members collectively (`c:Group` exception) |

### Key Architectural Patterns

**Selfness and Personas**: A Person's selfness (`alice(self)alice.ttl`) is the central identity individual. It carries only properties intrinsic to the person (physical characteristics. All other data — names, identifiers, addresses, payment cards — belongs to context-specific Personas, each in its own file.

**Peer name pattern** (not hierarchical): All name types (FullName, GivenName, FamilyName, AlternateName) connect directly to a Persona via `ont00001879` (designated by). They are siblings, not nested. Names belong to Personas not to Persons. 

**Address history pattern**: `AddressDesignation` links Person → Address → `TemporalInterval`. Open-ended intervals (no `hasEndDate`) indicate current address.

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

Before committing any change to `alice(self)alice.ttl`, any context file, `persona.ttl`, `context.ttl`, or `persona-shacl.ttl`, increment the **minor version number** in that file's `owl:versionInfo` annotation and update the description to summarise the change. For example:

```
owl:versionInfo "Version 3.0.3 - added social network"@en
```
becomes:
```
owl:versionInfo "Version 3.0.4 - added birth date"@en
```

## Integrity Checks

Files inside any directory named `under-development/` (at any depth) are works-in-progress and must be **excluded from all integrity checks** below.

After any change to context files or the context map diagram, verify the following. **`images/example/context-map.png` is the authoritative source of truth.** When a discrepancy is found between the diagram and any `.ttl` file or `README.md` entry, the diagram wins — update the files to match the diagram, not the other way around.

**Check 1 — Diagram ↔ files ↔ README coverage**: Every labeled circle in `images/example/context-map.png` must have (a) a corresponding `.ttl` file in the appropriate directory and (b) a row in one of the tables in the **Alice's Personas and Contexts** section of `README.md`. Conversely, every row in those tables must correspond to a circle in the diagram and a file that actually exists. If a circle exists in the diagram but has no `.ttl` file or README row, create them to match the diagram.

**Check 2 — Filename convention**: Every context filename must follow `[NN-]<about>(<context-name>)<asserted-by>[.(<parent-context>)]`, where the optional `NN-` is the zero-padded two-digit diagram label number for files that appear as labeled circles in `context-map.png`. The `<asserted-by>` segment must be a real entity identifier (e.g. `alice`, `bob`, `paula`) — except for `c:Group` contexts, where it must be the literal string `members`. Where a parent segment `.(X)` is present, the parent context file must exist. The hierarchy implied by the segments must match the radial structure in `context-map.png`. If a filename conflicts with the diagram's hierarchy, rename the file to match the diagram.

**Check 3 — Orange arrows (hasMember)**: For every orange arrow from circle A to circle B in `context-map.png`, the source context file (A) must contain a `persona:hasSocialNetwork` individual of type `cco:ont00001183` (Social Network), and that network must have a `BFO_0000115` (has member part) triple pointing to the `p:Persona` individual defined in the target context file (B).

**Check 4 — Dyad symmetry**: If context A contains a `p:Persona` with a `persona:dyad` link pointing to a `p:Persona` in context B, then context B must contain the reciprocal `persona:dyad` link pointing back to the persona in context A. Dyad links must always be bidirectional.

**Check 5 — Dyad cardinality**: A `p:Persona` must have at most one `persona:dyad` property. A persona can be paired with only one other persona.

**Check 6 — hasPersona tree structure**: The directed graph formed by `persona:hasPersona` links must be a tree (not a DAG). Every `p:Persona` must appear as the object of `persona:hasPersona` from at most one subject. A persona that is the target of two or more `hasPersona` links from different sources has two parents — a violation of tree structure.

**Check 7 — contextCategory label ↔ TTL agreement**: For every labeled circle in `images/example/context-map.png`, the light-blue label attached to that circle shows a `contextCategory` value (e.g. "Finance", "Federal", "Group"). That value must exactly match the local name of the `c:contextCategory` object in the corresponding `.ttl` file (e.g. `context:contextCategory context:Finance`). Read the diagram label independently before consulting the TTL — do not let the TTL value anchor your reading of the diagram. If the label and the TTL value differ, the diagram is authoritative — update the TTL to match the diagram.

**Check 8 — No orphan Personas**: Every `p:Persona` individual must be reachable via at least one of the following two link types from a `cco:ont00001262` (Person) individual or another `p:Persona` individual:

- **`persona:hasPersona`** — valid only when all contexts along the chain share the same `c:subject` value (i.e. the entire branch describes the same person). A `hasPersona` link that would cross a subject boundary is not a valid parent link.
- **`BFO_0000115`** (has member part) — a `hasMember` link from a Person or Persona to a Persona. This is the correct parent link for cross-person contexts where the `c:subject` differs from the asserting person's tree (e.g. Bob's Self linking to Alice's persona asserted by Bob via an orange `hasMember` arrow in the diagram).

A Persona that is not reachable by either mechanism is an orphan. Note: `persona:dyad` does not satisfy this requirement — it is a lateral peer link, not a parent link.

**Check 9 — Validation command completeness**: The `riot` merge command in the `## Validation` section of `README.md` must include every `.ttl` file in the project except: (a) files in `project_files/` (listed explicitly as foundation ontologies at the head of the command), (b) files in any `under-development/` directory, and (c) `persona-shacl.ttl` (used separately as the shapes file). The preferred implementation uses `find` with `-not -path "*/under-development/*"` so that newly added files are included automatically without a manual README update. If the `find` pattern changes (e.g. a new exclusion is added), update the README command to match.

**Check 10 — PNG file location**: The diagram PNG for a context file must be stored in `images/example/<about>-contexts/`, where `<about>` is the first segment of the context filename (e.g. `alice(bhs)alice.ttl` → `images/example/alice-contexts/`). Selfness files (`<X>(self)<X>.ttl`) are an exception — their PNGs live in `images/example/<X>/`. Files in `under-development/` are excluded.

**Check 11 — PNG filename convention**: Within `images/example/<about>-contexts/`, every diagram PNG must use the same base filename as the corresponding `.ttl` file, with `.png` substituted for `.ttl` (including the `NN-` numeric prefix where present). For example, `07-alice(bhs)alice.ttl` → `07-alice(bhs)alice.png`; `09-bob(bob)bob.(bhs).ttl` → `09-bob(bob)bob.(bhs).png`. If the PNG does not yet exist, the README Diagram cell must be marked `*(todo)*` rather than left blank.

## Keeping Files in Sync

Whenever changes are made to `alice(self)alice.ttl`, any context file, `persona.ttl`, or `context.ttl`, `persona-shacl.ttl` must be updated to match:

- **New property usage in a context file or `alice(self)alice.ttl`** (e.g., a new physical characteristic, relationship, or identifier added to a Person or Persona instance) → add or extend a SHACL shape to validate that property on the relevant target class.
- **New class or property defined in `persona.ttl`** (e.g., `persona:hasSocialNetwork`) → add a SHACL shape that constrains how instances of the domain class may or must use it.

Always update `persona-shacl.ttl` in the same edit session as the change that triggers it.

## Validation

**SHACL validation** (e.g., using Apache Jena's `shaclvalidate`):
```bash
shaclvalidate -datafile example/alice/alice(self)alice.ttl -shapesfile persona-shacl.ttl
```

**Protégé**: Load `persona.ttl`; Protégé will import the domain ontologies via IRI resolution. Use the reasoner (HermiT/Pellet) to check consistency.

## README Coverage

All classes and properties defined in `persona.ttl` and `context.ttl` must be mentioned in `README.md` in the sections before the **Illustrative Example: Alice Walker** section. The only intentional exceptions are the internal ontology documentation annotation properties (`usesRequiredClass`, `usesOptionalClass`, `usesCCOClass`, `usesCCOProperty`, `usagePattern`), which are infrastructure for self-documenting the ontology, not user-facing terms.

In `README.md`, every mention of a class defined in `persona.ttl` must appear in backticks with the `p:` prefix (e.g. `p:Persona`, `p:Wallet`), and every mention of a class or property defined in `context.ttl` must appear in backticks with the `c:` prefix (e.g. `c:contextType`, `c:SelfAsserted`). Every capitalized mention of `Person` (the CCO class) must also appear in backticks. These formatting rules do **not** apply inside headings or subheadings.

## Gitignore Notes

`catalog-v001.xml` and `/project_files` are gitignored (Protégé IDE artifacts). The `project_files/` directory exists locally but is not tracked — it contains source domain ontologies and reference documents.
