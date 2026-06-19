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
| `persona-shacl.ttl` | SHACL validation shapes — constraint rules for all `persona:Person` instances (SSN format, address cardinality, payment cards, wallet, social network, etc.) |
| `persona-templates.ttl` | Persona template labels — defines `p:PersonaTemplate` (abstract classification superclass) and concrete label subclasses `p:BirthCertificate`, `p:JSContactCard`, `p:DriversLicense`; also defines related designator classes (`persona:DriversLicenseNumber`, `persona:IssuingJurisdiction`, `persona:Credential`, `persona:WebURL`, `persona:OrganizationUnit`, `persona:JobTitle`), complex classes (`persona:Anniversary`, `persona:PersonalInfo`), and properties (`persona:hasAnniversary`, `persona:hasPhoto`, etc.) |
| `shacl/birthcertificate-shacl.ttl` | Per-template SHACL shapes for birth certificate context files — run against the individual context file, not merged data |
| `shacl/jscontactcard-shacl.ttl` | Per-template SHACL shapes for JSContactCard context files — run against the individual context file, not merged data |
| `shacl/driverslicense-shacl.ttl` | Per-template SHACL shapes for driver's license context files — run against the individual context file, not merged data |
| `project_files/` | Reference materials: imported domain ontologies (PersonOntology.ttl, AddressOntology.ttl, StagingOntology.ttl), BFO/CCO source files, PDFs, docs |

## Example Files

| File | Purpose |
|------|---------|
| `example/alice(self)alice.databook.md` | Alice Walker's selfness — central Person instance; physical characteristics |
| `example/paula(self)paula.databook.md` | Paula Walker's selfness — central Person instance for Paula |
| `example/bob(self)bob.databook.md` | Bob Johnson's selfness — central Person instance for Bob |
| `example/01-paula(acme)alice.databook.md` | Paula Walker as Alice's Acme colleague — asserted by Alice |
| `example/02-paula(familymember)alice.databook.md` | Paula Walker as Alice's family member — name and relationship; asserted by Alice |
| `example/03-paula(familymember)paula.databook.md` | Paula Walker in family context — self-asserted; dyad with 02 |
| `example/04-alice(bob)bob.databook.md` | Alice Walker in Bob context — Bob's view of Alice with personal notes |
| `example/05-bob(bob)alice.databook.md` | Bob Johnson in Bob context — Alice's view of Bob with personal notes; dyad with 06 |
| `example/06-bob(bob)bob.databook.md` | Bob Johnson in Bob context — self-asserted name; dyad with 05 |
| `example/07-alice(bhs)alice.databook.md` | Alice Walker's Boston Hub Society profile — address and phone |
| `example/08-bhs(bhs)members.databook.md` | Boston Hub Society — g:Group instance with Alice and Bob as members |
| `example/09-bob(bhs)bob.databook.md` | Bob Johnson's Boston Hub Society profile — name; self-asserted |
| `example/10-alice(citibank)citibank.databook.md` | Alice's Citibank Persona — payment card |
| `example/11-alice(google)alice.databook.md` | Alice's Google Persona — email address |
| `example/12-alice(att)alice.databook.md` | Alice's AT&T Persona — phone number |
| `example/13-alice(tx-birth-cert)alice.databook.md` | Alice's Texas Birth Certificate Persona — legal name record |
| `example/14-alice(paradise)alice.databook.md` | Alice's Paradise Persona — current residential address |
| `example/15-alice(boston)alice.databook.md` | Alice's Boston Persona — residential address 2020–2025 |
| `example/16-alice(ssa)alice.databook.md` | Alice's SSA Persona — Social Security Number |
| `example/17-alice(bob)alice.databook.md` | Alice Walker in Bob context — Alice's self-asserted persona shown to Bob; dyad with 04 |
| `example/18-alice(familymember)alice.databook.md` | Alice's Family Persona — family relationships and social network |
| `example/19-alice(possessions)alice.databook.md` | Alice's Possessions Persona — wallet, health insurance card, SSN card |
| `example/20-alice(acme)alice.databook.md` | Alice's Acme Persona — employee context; social network with Paula |
| `example/21-alice(business-card)alice.databook.md` | Alice's Business Card Persona — employer, job title, email, phone |
| `example/22-alice(driverslicense)alice.databook.md` | Alice's Driver's License Persona — legal name, DOB, license number, expiration date |
| `example/under-development/paula(fl-birth-cert)alice.ttl` | Paula Walker's Florida Birth Certificate Persona — legal name record (under development) |

## Architecture

### Three-Layer Design

```
Triplestore (Fuseki) — loads all DataBook files directly:
  ├─ persona.ttl              (application profile — imports domain ontologies)
  │   ├─ PersonOntology.ttl
  │   ├─ AddressOntology.ttl
  │   └─ StagingOntology.ttl → BFO terms
  ├─ example/alice(self)alice.databook.md
  ├─ example/bob(self)bob.databook.md
  ├─ example/paula(self)paula.databook.md
  ├─ example/01-paula(acme)alice.databook.md
  ├─ example/02-paula(familymember)alice.databook.md
  ├─ … (all numbered context DataBooks)
  └─ example/22-alice(driverslicense)alice.databook.md

persona-shacl.ttl — no owl:imports of data; validated against the loaded dataset
shacl/birthcertificate-shacl.ttl  — per-template shapes for birth certificate files
shacl/jscontactcard-shacl.ttl     — per-template shapes for JSContactCard files
shacl/driverslicense-shacl.ttl    — per-template shapes for driver's license files
```

1. **Foundation**: BFO (Basic Formal Ontology) — provides temporal modeling (`TemporalInterval`) and core relations
2. **Domain Ontologies** (in `project_files/`): PersonOntology, AddressOntology, StagingOntology
3. **Application Ontologies** (peer, not nested):
   - `persona.ttl`: aggregates domain ontologies; uses annotation properties (`usesRequiredClass`, `usesOptionalClass`, `usesCCOClass`, `usesCCOProperty`) to document Mee's usage
   - `context.ttl`: defines `contextType`, `assertionType`, and `subject` vocabularies; imported directly by each context file

### Context File Naming Convention

Context filenames follow a single flat pattern:

```
[NN-]<about>(<context-name>)<asserted-by>.ttl
```

| Segment | Meaning |
|---------|---------|
| `NN-` | Zero-padded two-digit diagram label number; omitted for files that have no diagram circle. Selfness files (`<X>(self)<X>.ttl`) never carry a prefix. |
| `<about>` | The entity the Persona is about (e.g. `alice`, `bob`, `paula`, `bhs`). |
| `(<context-name>)` | Lowercase name identifying the context or relationship. For named-entity contexts (a specific company, person, place, or group), use the entity's own name (e.g. `(citibank)`, `(bhs)`, `(bob)`). For categorical contexts, use the lowercase local name of the `c:contextCategory` (e.g. `(familymember)` for `context:FamilyMember`, `(employee)` for `context:Employee`). |
| `<asserted-by>` | Who asserted the data — a real entity identifier (e.g. `alice`, `bob`, `paula`) or the literal `members` for `c:Group` contexts where any permitted member may write. |

**Exception — `c:Group` contexts**: A group context (`contextCategory context:Group`) has no single asserter — any permitted member can write to it and changes replicate to all members. The `<asserted-by>` segment is the literal `members` rather than an individual name. Example: `08-bhs(bhs)members.ttl` — about BHS, context "bhs", asserted by the group's members collectively.

**`context:assertedBy` vocabulary**: The TTL annotation uses `identity:Self` (a singleton individual of `identity:Individual`) for self-asserted contexts (the Mia user entered the data), a named individual of `identity:Individual` (e.g. `:Bob_Johnson`) for peer-asserted contexts, and a named individual of `identity:Organization` only when the asserting organization is itself a PDN node. In the example data **only Citibank is a PDN node**, so only `10-alice(citibank)citibank.ttl` uses `assertedBy identity:Organization`. All other organization-related contexts (Google, AT&T, SSA, etc.) use `assertedBy identity:Self` because Alice self-enters that data — those organizations are not PDN-interoperable.

**"Other" asserters**: When the asserter is someone other than the current Mia user (`identity:Self`), the asserter is a named individual of one of:
- `identity:Individual` — another Mia user (a different person, e.g. Bob asserting data about Alice)
- `identity:Organization` — a company, nonprofit, or government agency that is a PDN node
- `identity:Group` — a group of Mia users

The parent-context hierarchy (which context is a child of which) is expressed via `persona:hasPersona` and `BFO_0000115` links in the TTL files, not in the filename.

**Examples:**

| Filename | About | Context | Asserted by |
|----------|-------|---------|-------------|
| `10-alice(citibank)citibank.ttl` | Alice | citibank | Citibank |
| `02-paula(familymember)alice.databook.md` | Paula | familymember | Alice |
| `04-alice(bob)bob.ttl` | Alice | bob | Bob |
| `09-bob(bhs)bob.ttl` | Bob | bhs | Bob |
| `08-bhs(bhs)members.ttl` | BHS | bhs | members (group) |

### Key Architectural Patterns

**Selfness and Personas**: A Person's selfness (`alice(self)alice.ttl`) is the central identity individual. It carries only properties intrinsic to the person (physical characteristics). All other data — names, identifiers, addresses, payment cards — belongs to context-specific Personas, each in its own file.

**`:Self` IRI convention**: The Mia user's own `persona:Person` individual always uses the IRI `:Self` across all of their context files. All other people, groups, and organizations are assigned locally-minted named IRIs (e.g. `:Bob_Johnson`, `:Paula_Walker`, `:BHS`). `:Self` is a local IRI and is never exposed externally over the PDN, so there are no collisions between Mia instances. All context files in the example live in Alice's Mia — some authored by Alice, others received from peers over PDN. In either case, `:Self` refers to Alice. When data arrives from a peer's Mia (where that peer was `:Self` in their own instance), Alice's Mia assigns them a locally-minted identifier; once a PDN connection is established, that identifier resolves to or is replaced by their PDN ID.

**DataBook IRI convention**: The document `id:` and `graph.named_graph:` always differ by the `#graph` fragment — `named_graph` is always `{id}#graph`. The `databook:id` on a block is a fragment identifier making that block independently addressable as `{id}#{block-id}`. Overview sections always begin with "This context captures...".

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

After any change to context files or the context map diagram, verify the following. **`example/images/context-map.png` is the authoritative source of truth.** When a discrepancy is found between the diagram and any `.ttl` file or `README.md` entry, the diagram wins — update the files to match the diagram, not the other way around.

**Check 1 — Diagram ↔ files ↔ README coverage**: Every labeled circle in `example/images/context-map.png` must have (a) a corresponding `.ttl` file in the appropriate directory and (b) a row in one of the tables in the **Alice's Personas and Contexts** section of `README.md`. Conversely, every row in those tables must correspond to a circle in the diagram and a file that actually exists. If a circle exists in the diagram but has no `.ttl` file or README row, create them to match the diagram.

**Check 2 — Filename convention**: Every context filename must follow `[NN-]<about>(<context-name>)<asserted-by>.ttl`, where the optional `NN-` is the zero-padded two-digit diagram label number for files that appear as labeled circles in `context-map.png`. The `<asserted-by>` segment must be a real entity identifier (e.g. `alice`, `bob`, `paula`) — except for `c:Group` contexts, where it must be the literal string `members`. If a filename does not match this pattern, rename it to conform.

**Check 3 — Orange arrows (hasMember)**: For every orange arrow from circle A to circle B in `context-map.png`, there must be a `BFO_0000115` (has member part) triple pointing to the `p:Persona` individual defined in the target context file (B), originating from one of two sources depending on context type:
- **`c:Persona`-type source (Person, Family, Employee, etc.)**: the source file's `p:Persona` individual must carry a `persona:hasSocialNetwork` link to a `cco:ont00001183` (Social Network) individual, and that Social Network individual must have the `BFO_0000115` triple.
- **`c:Group`-type source**: the source file's `g:Group` individual must have the `BFO_0000115` triple directly (no Social Network intermediate, since the group itself is the social entity).

**Check 4 — Dyad symmetry**: If context A contains a `p:Persona` with a `persona:dyad` link pointing to a `p:Persona` in context B, then context B must contain the reciprocal `persona:dyad` link pointing back to the persona in context A. Dyad links must always be bidirectional.

**Check 5 — Dyad cardinality**: A `p:Persona` must have at most one `persona:dyad` property. A persona can be paired with only one other persona.

**Check 6 — hasPersona tree structure**: The directed graph formed by `persona:hasPersona` links must be a tree (not a DAG). Every `p:Persona` must appear as the object of `persona:hasPersona` from at most one subject. A persona that is the target of two or more `hasPersona` links from different sources has two parents — a violation of tree structure.

**Check 7 — contextCategory label ↔ TTL agreement**: For every labeled circle in `example/images/context-map.png`, the light-blue label attached to that circle shows a `contextCategory` value (e.g. "Finance", "Federal", "Group"). That value must exactly match the local name of the `c:contextCategory` object in the corresponding `.ttl` file (e.g. `context:contextCategory context:Finance`). Read the diagram label independently before consulting the TTL — do not let the TTL value anchor your reading of the diagram. If the label and the TTL value differ, the diagram is authoritative — update the TTL to match the diagram.

**Check 8 — No orphan Personas**: Every `p:Persona` individual must be reachable via at least one of the following two link types from a `cco:ont00001262` (Person) individual or another `p:Persona` individual:

- **`persona:hasPersona`** — valid only when all contexts along the chain share the same `c:subject` value (i.e. the entire branch describes the same person). A `hasPersona` link that would cross a subject boundary is not a valid parent link.
- **`BFO_0000115`** (has member part) — a `hasMember` link from a Person or Persona to a Persona. This is the correct parent link for cross-person contexts where the `c:subject` differs from the asserting person's tree (e.g. Bob's Self linking to Alice's persona asserted by Bob via an orange `hasMember` arrow in the diagram).

A Persona that is not reachable by either mechanism is an orphan. Note: `persona:dyad` does not satisfy this requirement — it is a lateral peer link, not a parent link.

**Check 9 — Validation command completeness**: The `## Validation` section of `README.md` must document two tiers. Tier 1 uses four steps: (1) a `find example -name "*.databook.md"` loop using `databook extract` to produce a merged turtle file of all context data (excluding `under-development/`); (2) a `riot` merge of that data with all application ontology TTL files and the foundation ontologies listed explicitly from `project_files/`; (3) a `grep -v owl:imports` on `persona-shacl.ttl` to collect shapes (the `shacl/` per-template files are excluded here — they target `persona:Person` and would fire incorrectly on all individuals when applied to merged data); (4) a `shacl validate` call. Tier 2 lists explicit per-file `databook extract` + `riot` + `shacl validate` commands for each template context file paired with its `shacl/*-shacl.ttl` file. If the commands change, update the README to match.

**Check 10 — PNG file location**: The diagram PNG for every context file and selfness file must be stored directly in `example/images/` (flat, no subfolders — not `images/example/`). Files in `under-development/` are excluded.

**Check 11 — PNG filename convention**: Every diagram PNG in `example/images/` must use the same base filename as the corresponding `.ttl` file in `example/`, with `.png` substituted for `.ttl` (including the `NN-` numeric prefix where present). For example, `07-alice(bhs)alice.ttl` → `07-alice(bhs)alice.png`; `alice(self)alice.ttl` → `alice(self)alice.png`. If the PNG does not yet exist, the README Diagram cell must be marked `*(todo)*` rather than left blank.

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

`README.md` must be written in US English. Use American spellings throughout — e.g. "organization" not "organisation", "color" not "colour".

All classes and properties defined in `persona.ttl` and `context.ttl` must be mentioned in `README.md` in the sections before the **Illustrative Example: Alice Walker** section. The only intentional exceptions are the internal ontology documentation annotation properties (`usesRequiredClass`, `usesOptionalClass`, `usesCCOClass`, `usesCCOProperty`, `usagePattern`), which are infrastructure for self-documenting the ontology, not user-facing terms.

In `README.md`, every mention of a class defined in `persona.ttl` must appear in backticks with the `p:` prefix (e.g. `p:Persona`, `p:Wallet`), and every mention of a class or property defined in `context.ttl` must appear in backticks with the `c:` prefix (e.g. `c:contextType`, `c:SelfAsserted`). Every capitalized mention of `Person` (the CCO class) must also appear in backticks. These formatting rules do **not** apply inside headings or subheadings.

## Catalog Files

Two `catalog-v001.xml` files map ontology IRIs to local file paths so Protégé can resolve `owl:imports` without hitting the network:

- **`catalog-v001.xml`** (repo root) — used when opening root-level files (`persona.ttl`, `persona-shacl.ttl`, etc.) directly. Uses **relative** paths from the repo root.
- **`example/catalog-v001.xml`** — used when opening a context file from the `example/` directory directly. Uses **absolute** `file://` paths.

**Whenever a `.ttl` file is created, deleted, renamed, or moved**, update both catalog files to match:
- **Create**: add a `<uri>` entry in both catalogs with the new file's ontology IRI (from its `rdf:type owl:Ontology` declaration) and its path.
- **Delete**: remove the corresponding `<uri>` entry from both catalogs.
- **Rename or move**: update the `uri=` path attribute in both catalogs.

The `id` attribute is a human-readable label (no functional significance); keep it consistent with the file's short name or diagram number.

## Gitignore Notes

`/project_files` is gitignored. The `project_files/` directory exists locally but is not tracked — it contains source domain ontologies and reference documents.
