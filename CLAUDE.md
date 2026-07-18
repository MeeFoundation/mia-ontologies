# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an **RDF/OWL ontology project** — a formal semantic knowledge model for representing natural people's identity data in the Mee Identity Agent (MIA). It comprises four peer application ontologies:

- **Persona ontology** (`persona.ttl`): models identity data — names, addresses, identifiers, relationships, payment cards, and more — structured around context-specific `Person` instances. Imports and profiles existing domain ontologies, documenting which of their classes and properties Mee uses, and extends them with Mia-specific terms.
- **Context ontology** (`context.ttl`): defines controlled vocabularies for classifying context files — who claimed the data (`claimant`), and whose identity the file describes (`subject`). The four self-vs-other combinations these two values distinguish (self-by-self, other-by-self, other-by-other, self-by-other) are derived directly from `subject`/`claimant`, not a separate property or class hierarchy — `SCcontext` has no subclasses.
- **Cell ontology** (`cell.ttl`): defines `cell:Cell` — the self-contained *content* facet of a cell, carrying only what's common to every cell (`sc-context`, `graph`, `note`, `folder`), plus two further orthogonal facets: `cell:TCell` (template content, carrying `templateShape`) and `cell:ACell` (actual/instantiated content, carrying `parties`, `creator`, and `shape` — its party composition is the `OneParty`/`MultiParty`(abstract)/`TwoParty`/`ThreePlusParty` hierarchy, hanging off `ACell` rather than `Cell` directly). A cell needing both facets (e.g. a template cell that also carries real party data) is simply multi-typed with both. A `cell:Cell` carries no tree position of its own.
- **Category ontology** (`category.ttl`): defines two orthogonal facets of a category. `cat:Category` (abstract) is the *classificatory* facet — which kind of thing it is (e.g. `cat:Work`, `cat:Affiliations`; the `Person`/`Organization` hierarchy and all leaf categories) — the canonical tree IS this class hierarchy (`rdfs:subClassOf`), not a separate set of instances. A `cat:Category` subclass with reusable starter content carries `cat:templateCell` (an `owl:AnnotationProperty`) pointing directly at a `cell:Cell` template — mirroring `cell:abstract`'s precedent for asserting metadata directly on a class IRI. The `cat:templateCell` pointer triples for the 4 templated classes are asserted directly in `category.ttl`, right alongside each class's own declaration; the target `cell:Cell` individuals themselves are defined in the companion file `cell-templates.ttl` (which `category.ttl` `owl:imports`). That template cell may in turn carry `cell:templateShape` (an `owl:ObjectProperty`, defined in `cell.ttl` — not `category.ttl`, since its domain/range, `cell:Cell`/`sh:NodeShape`, never actually reference a `cat:` term) to the `sh:NodeShape`(s), in `cell-templates-shacl.ttl`, describing the content expected of a context file filed under that category — making a class's shape reachable by pure RDF traversal (`cat:Category` → `cat:templateCell` → `cell:templateShape`), not merely by file co-location or naming convention. Because `cell:templateShape` lives in `cell.ttl`, `cell-templates.ttl` only needs to import `cell.ttl` directly, not `category.ttl` — so unlike `context.ttl`/`cell.ttl`, `category.ttl`/`cell-templates.ttl` is a one-directional import, not mutual. `cat:Node` (abstract) is the *tree-position* facet, used only within a user's own instance tree, split into two kinds: `cat:CategoryDefined` (a node instantiated from a canonical class, carrying `category` naming the `cat:Category` subclass it represents — this single value also records what it was instantiated from, since there is no separate canonical individual; formerly named `cat:Copy`, renamed in category.ttl 1.13.0 alongside a broader 'copy'→'instantiate' terminology shift) and `cat:UserDefined` (a node created directly, with no canonical counterpart, so no `category`) — `cat:CategoryDefined` and `cat:UserDefined` both carry an optional `label` override (`cat:label`'s domain is their union). Both kinds carry a forward link to their own real-content cell(s), `cat:cell` (domain the union of `cat:CategoryDefined`/`cat:UserDefined`) — `cell:Cell` has no property pointing back at all. Splitting tree position from cell content this way (the 3.0.0/1.0.0 rewrite, refined to Node/Canonical/Copy in a later revision, then simplified again in 1.8.0 when `cat:Canonical`/`cat:copiedFrom` were deleted once empirically confirmed redundant with the class hierarchy) makes a cell's content self-contained and independent of tree position, so it's robust under PDN sync: two peers (e.g. Alice and Bob) can each freely reorganize their own category tree without ever needing to touch a cell they share — moving a node in the tree is done entirely through its parent's `child` list, never through the node's own `cat:cell` value(s). Every category DataBook in a user's instance tree is associated with one or more `cell-databook` files. `cell.ttl` imports `context.ttl` (a separate mutual import), but not `category.ttl` — nothing in `cell.ttl` references `cat:` terms.

There are no build, compile, test, or lint commands. The files are Turtle (`.ttl`) loaded into semantic web tools (Protégé).

## Core Files

| File | Purpose |
|------|---------|
| `persona.ttl` | Persona ontology — imports domain ontologies, annotates which classes/properties are required vs. optional for Mee, defines Mia-specific classes and properties |
| `context.ttl` | Context ontology — controlled vocabularies for classifying context files (`claimant`, `subject`) and the `Context` class hierarchy. Mutually imports `cell.ttl` |
| `cell.ttl` | Cell ontology — `cell:Cell` (formerly `cell:Parties`), the content facet of a cell, carrying only what's common regardless of facet (`sc-context`, `graph`, `note`, `folder`). Splits into two orthogonal facets (cell.ttl 3.7.0): `cell:TCell` (abstract, template facet — carries `templateShape`) and `cell:ACell` (abstract, actual/instantiated facet — carries `parties`, `creator`, and the new `shape` property). The `Cell`/`MultiParty`(abstract)/`OneParty`/`TwoParty`/`ThreePlusParty` party-count hierarchy now hangs off `cell:ACell` rather than `cell:Cell` directly. `parties`'s range is `cell:ACell` itself — its value is the concrete subclass (e.g. `cell:OneParty`), not a string, mirroring `cat:category`'s class-value punning (category.ttl). `creator`'s range is a union of `p:Person`/`g:Group`/`o:Organization`, referenced by name without importing those ontologies (mirroring `context:subject`/`context:claimant`). `templateShape` (domain `cell:TCell`, range `sh:NodeShape`) links a template cell to its SHACL shape(s) describing what a context filed under its category should look like; moved here from `category.ttl`'s `cat:templateShape` since its domain/range never referenced a `cat:` term. `shape` (domain `cell:ACell`, range `sh:NodeShape`) links an actual cell directly to the shape(s) validating its own content — distinct from `templateShape`. A cell needing both facets (e.g. every individual in `cell-templates.ttl`) is simply multi-typed with both `cell:TCell` and its `cell:ACell`-lineage class. Carries no link back to a node — that's asserted only on the category side, as `cat:cell`. Mutually imports `context.ttl` |
| `category.ttl` | Category ontology — `cat:Category` (abstract, classificatory facet: the `Person`/`Organization` hierarchy and all leaf categories, plus `catType` and `templateCell`) and `cat:Node` (abstract, tree-position facet used only in a user's own instance tree, split into `cat:CategoryDefined` — `category` — and `cat:UserDefined`; `cat:label`'s domain is the union of `cat:CategoryDefined`/`cat:UserDefined`; both kinds carry `cat:cell` — the sole link to a node's `cell:Cell`(s), since `cell.ttl` has no forward-pointing equivalent); `child` domain/range `cat:Node`. No separate canonical node class — the canonical tree is the `cat:Category` class hierarchy itself. Imports `cell.ttl` and `cell-templates.ttl` |
| `cell-templates.ttl` | Class-level `cell:Cell` templates — one individual per templated class (`cat:Passport`, `cat:BirthCertificate`, `cat:DriversLicense`, `cat:MedicalAppointmentInfo`), each pointed at by its class's own `cat:templateCell` value (asserted in `category.ttl`, not here). Each is multi-typed `cell:Cell, cell:TCell, cell:ACell, cell:OneParty` (cell.ttl 3.7.0's facet split), since a template cell is simultaneously the template facet (carrying `cell:templateShape` to its SHACL shape in `cell-templates-shacl.ttl`) and the actual/instantiated facet (carrying `cell:parties`). Imports `cell.ttl` directly — no mutual import with `category.ttl` |
| `cell-shacl.ttl` | SHACL validation shapes for `cell:Cell` DataBook instances, split across three shapes matching cell.ttl 3.7.0's facet split: `:CellShape` (target `cell:Cell`) — `sc-context`/`graph`/`note`/`folder` cardinality, with `sc-context` values (if any) constrained to be a `context:SCcontext` (uniformly regardless of party count); `:TCellShape` (target `cell:TCell`) — `templateShape` cardinality (at most one; deliberately not constrained to `sh:class sh:NodeShape` since its value is only typed as such in `cell-templates-shacl.ttl`, which Tier 1 excludes from its merged-data run); `:ACellShape` (target `cell:ACell`) — `parties` required and constrained to be the class `cell:OneParty`/`cell:TwoParty`/`cell:ThreePlusParty`, `creator` (if present) constrained to be a `p:Person`, `g:Group`, or `o:Organization`, and `shape` cardinality (at most one, same reasoning as `templateShape`) |
| `category-shacl.ttl` | SHACL validation shapes for `cat:Category`/`cat:Node` DataBook instances — `catType` required exactly once on `cat:Category`; `child` (values must be `cat:Node`) and `cell` (values must be `cell:Cell`) on `cat:Node`; `category` cardinality on `cat:CategoryDefined`; `label` cardinality shared by `cat:CategoryDefined` and `cat:UserDefined` |
| `persona-shacl.ttl` | SHACL validation shapes — constraint rules for all `persona:Person` instances (SSN format, address cardinality, payment cards, wallet, social network, etc.) |
| `context-shacl.ttl` | SHACL validation shapes for context DataBook instances — `:SCcontextShape` (`context:SCcontext`'s `subject`/`claimant`, each required exactly once); split out of `persona-shacl.ttl` since it validates a `context.ttl` class, not `persona:Person`. A context DataBook does not carry `cell:creator` (or any creator property) — that stays a `cell:Cell`-only property |
| `persona-templates.ttl` | Persona template labels — defines `p:PersonaTemplate` (abstract classification superclass) and concrete label subclasses `p:BirthCertificateDocument`, `p:JSContactCard`, `p:DriversLicenseDocument`, `p:PassportDocument`, `p:MedicalAppointmentRecord`; also defines related designator classes (`persona:DriversLicenseNumber`, `persona:IssuingJurisdiction`, `persona:PassportNumber`, `persona:IssuingCountry`, `persona:PlaceOfBirth`, `persona:GenderMarker`, `persona:IssueDate`, `persona:Credential`, `persona:WebURL`, `persona:OrganizationUnit`, `persona:JobTitle`), complex classes (`persona:Anniversary`, `persona:PersonalInfo`), the `p:MedicalAppointmentRecord` claim properties (`persona:forPatient`, `persona:hasPrimaryCarePhysician`, `persona:currentMedication`, `persona:allergy`, `persona:medicalHistoryNote`, `persona:insuranceProvider`, `persona:insurancePolicyNumber`, `persona:insuranceGroupNumber`, `persona:preferredPharmacy`), and other properties (`persona:hasAnniversary`, `persona:hasPhoto`, etc.) |
| `cell-templates-shacl.ttl` | Per-template SHACL shapes for birth certificate, driver's license, passport, and medical appointment context files — `:BirthCertificateDocumentShape`, `:DriversLicenseDocumentShape`, `:PassportDocumentShape`, `:MedicalAppointmentRecordShape` — each directly linked from its `cell-templates.ttl` template cell via `cell:templateShape`; run against the individual context file, not merged data |
| `shacl/jscontactcard-shacl.ttl` | Per-template SHACL shapes for JSContactCard context files — run against the individual context file, not merged data (JSContactCard is reused across many unrelated tree positions with no single `cat:Category` class of its own, so its shape stays standalone) |
| `yaml-to-rdf.py` | Synthesizes `cat:`/`cell:`/`context:` triples from category, cell, and context DataBook `mia.` YAML frontmatter, used as Tier 1 validation Step 1b (see README.md's Validation section) — `databook extract` only pulls fenced Turtle blocks, which category/cell DataBooks never carry, so without this script `cat:Node`/`cell:Cell` individuals and `context:SCcontext`'s subject/claimant never reach the merged validation graph |
| `project_files/` | Reference materials: imported domain ontologies (PersonOntology.ttl, AddressOntology.ttl, StagingOntology.ttl), BFO/CCO source files, PDFs, docs |

## Example Files

| File | Purpose |
|------|---------|
| `example/contexts/paula-walker.self(paula-walker)(acme)(06).databook.md` | Paula Walker as Alice's Acme colleague — claimed by Alice |
| `example/contexts/paula-walker.self(paula-walker)(immediate-family)(07).databook.md` | Paula Walker as Alice's family member — claimed by Alice |
| `example/contexts/paula-walker.paula-walker(paula-walker)(immediate-family)(05).databook.md` | Paula Walker's own family persona; social network with Alice |
| `example/contexts/self.bob-johnson(bob-johnson)(others)(08).databook.md` | Alice Walker as seen by Bob Johnson — claimed by Bob |
| `example/contexts/bob-johnson.self(bob-johnson)(others)(04).databook.md` | Alice's notes about Bob Johnson; favorite drink: oat milk cappuccino |
| `example/contexts/bob-johnson.bob-johnson(bob-johnson)(others)(02).databook.md` | Bob Johnson's self-claimed persona; social network with Alice |
| `example/contexts/self.self(boston-hub-society)(affiliations)(14).databook.md` | Alice's Boston Hub Society profile — email, phone, and current address |
| `example/contexts/bhs-group.members(boston-hub-society)(affiliations)(01).databook.md` | BHS Group — g:Group instance with Alice and Bob as members |
| `example/contexts/bob-johnson.bob-johnson(boston-hub-society)(affiliations)(03).databook.md` | Bob Johnson's BHS member persona — name, email, phone, address |
| `example/contexts/self.citibank(citibank)(banking-payments)(09).databook.md` | Alice's Citibank context — debit card; claimed by Citibank |
| `example/contexts/self.self(google)(companies)(16).databook.md` | Alice's Google context — Gmail address |
| `example/contexts/self.self(att)(companies)(11).databook.md` | Alice's AT&T context — phone number |
| `example/contexts/self.self(texas-vital-records)(state)(24).databook.md` | Alice's Texas birth certificate — legal names, maiden name |
| `example/contexts/self.self(paradise)(municipality)(18).databook.md` | Alice's Paradise, CA address — current residence (2025–present) |
| `example/contexts/self.self(boston)(municipality)(13).databook.md` | Alice's Boston, MA address — previous residence (2020–2025) |
| `example/contexts/self.self(social-security-administration)(federal)(23).databook.md` | Alice's Social Security Number |
| `example/contexts/self.self(bob-johnson)(others)(12).databook.md` | Alice's 1:1 context with Bob; social network with Bob as member |
| `example/contexts/self.self(paula-walker)(immediate-family)(21).databook.md` | Alice's family context — social network with Paula Walker as member |
| `example/contexts/self.self(ownership)(22).databook.md` | Alice's possessions — wallet, health insurance card, SSN card |
| `example/contexts/self.self(paula-walker)(acme)(20).databook.md` | Alice's Acme employee context; social network with Paula Walker |
| `example/contexts/self.self(alice-walker)(acme)(10).databook.md` | Alice's business card (JSContactCard) — name, email, phone, employer, job title |
| `example/contexts/self.self(california-dmv)(state)(15).databook.md` | Alice's California driver's license — legal name, DOB, DL#, expiry, photo |
| `example/contexts/self.self(passport)(federal)(19).databook.md` | Alice's US passport — legal name, DOB, passport#, issue/expiry, place of birth, gender marker, photo |
| `example/contexts/self.self(health-wellness)(17).databook.md` | Alice's physical characteristics — height, eye color, hair color |
| `example/contexts/under-development/paula(fl-birth-cert)alice.ttl` | Paula Walker's Florida Birth Certificate Persona — legal name record (under development) |
| `example/contexts/self.ttl` | `:Self`'s sole type declaration (`rdf:type owl:NamedIndividual, persona:Person`); not `owl:imports`ed anywhere, merged in only for validation |

## Architecture

### Three-Layer Design

```
Triplestore (Fuseki) — loads all DataBook files directly:
  ├─ persona.ttl              (application profile — imports domain ontologies)
  │   ├─ PersonOntology.ttl
  │   ├─ AddressOntology.ttl
  │   └─ StagingOntology.ttl → BFO terms
  ├─ example/contexts/paula-walker.self(paula-walker)(acme)(06).databook.md
  ├─ example/contexts/paula-walker.self(paula-walker)(immediate-family)(07).databook.md
  ├─ … (all numbered context DataBooks)
  ├─ example/contexts/self.self(health-wellness)(17).databook.md
  └─ example/contexts/self.ttl        (:Self's bare type declaration — merged in for validation, never owl:imports'd)

persona-shacl.ttl — no owl:imports of data; validated against the loaded dataset
shacl/jscontactcard-shacl.ttl — per-template shapes for JSContactCard files (only template with no cat:Category class of its own)
cell-templates-shacl.ttl — per-template shapes for birth certificate, driver's license, passport, and medical appointment files
```

1. **Foundation**: BFO (Basic Formal Ontology) — provides temporal modeling (`TemporalInterval`) and core relations
2. **Domain Ontologies** (in `project_files/`): PersonOntology, AddressOntology, StagingOntology
3. **Application Ontologies** (peer, not nested):
   - `persona.ttl`: aggregates domain ontologies; uses annotation properties (`usesRequiredClass`, `usesOptionalClass`, `usesCCOClass`, `usesCCOProperty`) to document Mee's usage
   - `context.ttl`: defines `claimant` and `subject` vocabularies; imported directly by each context file
   - `cell.ttl`: defines `cell:Cell`, the content facet of a cell (context links common to all cells), split into `cell:TCell` (template facet) and `cell:ACell` (actual facet, carrying party composition); mutually imports `context.ttl`
   - `category.ttl`: defines `cat:Category` (classificatory facet: `catType`, `templateCell`) and `cat:Node` (tree-position facet used only in a user's own instance tree, split into `cat:CategoryDefined` — `category` — and `cat:UserDefined`; `cat:label` shared by `cat:CategoryDefined`/`cat:UserDefined`; `child` domain/range `cat:Node`; both kinds carry a link to their own cell(s) — `cat:cell`); no separate canonical node class — the canonical tree is the class hierarchy itself; imports `cell.ttl` and `cell-templates.ttl`

### Context File Naming Convention

Context filenames follow a single flat pattern:

```
<subject>.<claimant>(<containing-cell>)(<NN>).databook.md
```

| Segment | Meaning |
|---------|---------|
| `<subject>` | The entity the Persona is about. Use `self` when the subject is the Mia user's own `p:Person` (`:Self`); otherwise use the full hyphenated lowercase name (e.g. `paula-walker`, `bob-johnson`, `bhs-group`). |
| `<claimant>` | Who claimed the data. Use `self` when the claimant is `:Self`; use the full hyphenated lowercase name for other claimants (e.g. `bob-johnson`, `citibank`); use the literal `members` for `cell:ThreePlusParty` contexts where any permitted member may write. |
| `(<containing-cell>)` | A context DataBook carries no field pointing back at its cell — the containing cell is found by reverse lookup: the one `cell:Cell` DataBook whose `sc-context` or `graph` field references this context's `id`. This segment is that cell's filename, **minus its trailing `-cell` suffix** — i.e., the readable name of the `cat:CategoryDefined`/`cat:UserDefined` category associated with that cell (the association is recorded as `mia.cell` on the category — the only place any category/cell association is recorded, for any `cat:Node`). When the category's local name includes a `(parent)` qualifier (e.g. `bob-johnson(others)`), the filename uses two separate parenthetical segments before the number: `(bob-johnson)(others)`. Examples: `(bob-johnson)(others)`, `(boston-hub-society)(affiliations)`, `(paula-walker)(immediate-family)`, `(citibank)(banking-payments)`. For categories without a `(parent)` qualifier (e.g. `health`, `ownership`), a single segment suffices. |
| `(<NN>)` | Zero-padded two-digit context number in parentheses, matching the diagram label. |

**Exception — `cell:ThreePlusParty` contexts**: A group context (`parties: ThreePlusParty`) has no single claimant — any permitted member can write to it and changes replicate to all members. The `<claimant>` segment is the literal `members` rather than an individual name. Example: `bhs-group.members(boston-hub-society)(affiliations)(01).databook.md` — about BHS Group, containing cell "boston-hub-society(affiliations)", claimed by the group's members collectively.

**Exception — `cell:graph`-linked contexts**: A context linked from its cell via `cell:graph` (rather than `cell:sc-context`) has no single subject/claimant — it is data jointly maintained by multiple parties about a third party. Such contexts drop the `<subject>.<claimant>` prefix entirely and use the literal `context` in its place: `context(<containing-cell>)(<NN>).databook.md`. These files also omit `mia.claimant` and `mia.subject` from the YAML frontmatter (those fields describe a single-claimant relationship that doesn't apply here). Example: `context(alice-carol-about-mom)(health)(26).databook.md` — jointly maintained by Alice and Carol about their mother Paula, containing cell `alice-carol-about-mom(health)`.

**`mia.claimant` vocabulary**: The YAML field takes the local IRI of a `p:Person`, `g:Group`, or `o:Organization` individual — NOT an `i:PDNidentifier`. Specifically: `:Self` (the Mia user's `p:Person`) for self-claimed contexts; a named `p:Person` individual (e.g. `:Bob_Johnson`) when another Mia user claims the data; a named `g:Group` individual (e.g. `:BHS_Group`) for group contexts; and a named `o:Organization` individual (e.g. `:Citibank`) only when the claiming organization is itself PDN-interoperable. In the example data **only Citibank is treated as PDN-interoperable**, so only `self.citibank(citibank)(banking-payments)(09).databook.md` uses `claimant: ":Citibank"`. All other organization-related contexts (Google, AT&T, SSA, etc.) use `claimant: ":Self"` because Alice self-enters that data — those organizations aren't PDN-interoperable. (This distinction is currently just a data-modeling convention in the example, not formally enforced by any property — `identity:hasPDNidentifier`, which would have modeled it, was removed as unused; see pdn-identity.ttl 1.3.0.)

**"Other" claimants**: When the claimant is someone other than the current Mia user (`:Self`), the claimant is a named individual of one of:
- `p:Person` — another Mia user (a different person, e.g. `:Bob_Johnson` claiming data about Alice)
- `o:Organization` — a company, nonprofit, or government agency that is a PDN node (e.g. `:Citibank`)
- `g:Group` — a group of Mia users (e.g. `:BHS_Group`)

**Examples:**

| Filename | Subject | Claimed by | Containing cell |
|----------|---------|-------------|---------------------|
| `self.citibank(citibank)(banking-payments)(09).databook.md` | Self (Alice) | Citibank | citibank(banking-payments) |
| `paula-walker.self(paula-walker)(immediate-family)(07).databook.md` | Paula Walker | Self (Alice) | paula-walker(immediate-family) |
| `self.bob-johnson(bob-johnson)(others)(08).databook.md` | Self (Alice) | Bob Johnson | bob-johnson(others) |
| `bob-johnson.bob-johnson(boston-hub-society)(affiliations)(03).databook.md` | Bob Johnson | Bob Johnson | boston-hub-society(affiliations) |
| `bhs-group.members(boston-hub-society)(affiliations)(01).databook.md` | BHS Group | members (group) | boston-hub-society(affiliations) |

### Key Architectural Patterns

**All data belongs to contexts**: There is no separate selfness file holding a Mia user's identity data. Every piece of identity data — names, identifiers, addresses, payment cards, physical characteristics — belongs to a context-specific Persona file, asserted directly on the shared `:Self` individual. The one exception is `:Self`'s bare type declaration (`:Self rdf:type owl:NamedIndividual, persona:Person`), which lives once in `example/contexts/self.ttl` instead of being repeated with an `rdfs:label` in every context file as it once was; `self.ttl` carries no other claims about `:Self` and is never `owl:imports`ed — it is merged in alongside the context files only when validating (see the Tier 1/Tier 2 commands in README.md's Validation section). Every substantive fact about a Mia user still lives exactly where it always has: in the context file(s) it belongs to.

**`:Self` IRI convention**: The Mia user's own `persona:Person` individual always uses the IRI `:Self` across all of their context files. All other people, groups, and organizations are assigned locally-minted named IRIs (e.g. `:Bob_Johnson`, `:Paula_Walker`, `:BHS`). `:Self` is a local IRI and is never exposed externally over the PDN, so there are no collisions between Mia instances. All context files in the example live in Alice's Mia — some authored by Alice, others received from peers over PDN. In either case, `:Self` refers to Alice. When data arrives from a peer's Mia (where that peer was `:Self` in their own instance), Alice's Mia assigns them a locally-minted identifier; once a PDN connection is established, that identifier resolves to or is replaced by their PDN ID.

**Cell/Category split**: In a user's own instance tree, what was originally one `.databook.md` file per cell is now a category-databook associated with one or more cell-databooks — a `category-databook` (tree position: `child`/`catType`, plus `category` if `cat:CategoryDefined` — naming the `cat:Category` subclass it represents, which also records what it was instantiated from — `label` if `cat:CategoryDefined` or `cat:UserDefined`, and `cell` linking to its cell(s), keeping the original `id`/filename) and a `cell-databook` (content: `parties`/`sc-context`/`graph`/`note`/`folder`, minted alongside it with a matching `-cell`-suffixed `id`/filename in the same folder). `cell:Cell` carries no link back to a node at all — `cell.ttl` has no such property. Instead, every category node links forward to its cell(s) via `mia.cell`; this is the only place the association is recorded, in either direction. **The category/cell relationship is many-to-one, not 1:1** — a category may have more than one `mia.cell` value, each an independent piece of content filed at that one tree position; the example tree currently only shows one cell per category, but that's incidental, not a constraint (a second cell sharing a category would need its own distinguishing filename, e.g. `-cell-2`, alongside the conventional `-cell`). A context DataBook carries no field pointing back at its cell at all — the cell is the one that asserts the `sc-context`/`graph` link, and the context filename's `(<containing-cell>)` segment names the **category** (the human-readable position) associated with that cell, found by reverse lookup rather than by any field on the context itself. The split exists to make a cell's content self-contained (aside from the context files it references) and independent of tree position, for PDN sync robustness: when a cell is shared between peers (e.g. a `TwoParty` cell between Alice and Bob), each peer can independently rearrange their own category tree — moving, renaming, or renesting their category node however they like — without ever touching the shared cell's content or identity, since moving a node in the tree only ever means editing its parent's `child` list, never the node's own `cell` value(s). The *canonical* side of the split (which classes have reusable starter content) lives entirely at the class level now — see `category.ttl`'s `cat:templateCell` and the new `cell-templates.ttl` file — there is no longer a separate canonical-instance tree (`categories-person/`/`categories-org/` folders, removed in category.ttl 1.8.0).

**DataBook IRI convention**: The document `id:` and `graph.named_graph:` always differ by the `#graph` fragment — `named_graph` is always `{id}#graph`. The `databook:id` on a block is a fragment identifier making that block independently addressable as `{id}#{block-id}`. Overview sections always begin with "This context captures...".

**Peer name pattern** (not hierarchical): All name types (FullName, GivenName, FamilyName, AlternateName) connect directly to a Persona via `ont00001879` (designated by). They are siblings, not nested. Names belong to Personas not to Persons.

**Address history pattern**: `AddressDesignation` links Person → Address → `TemporalInterval`. Open-ended intervals (no `hasEndDate`) indicate current address.

**Named graph scoping of `BFO_0000115`**: When a Social Network individual carries `BFO_0000115 :Paula_Walker`, the triple is intentionally scoped to the enclosing named graph — it refers to Paula Walker *as a person entity*, with context-specific isolation provided by the DataBook named graph architecture, not by the triple itself. Queries needing context-specific member data must target the relevant named graphs (e.g. context 21 + context 5) rather than querying the full merged dataset. Do NOT change the range of `BFO_0000115` to a document IRI (breaks BFO semantics — range must be a continuant, not a document), and do NOT introduce context-specific person individuals (reintroduces the complexity that removing the layered Persona model eliminated). RDF-star annotation is a valid future option if tooling matures.

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

Before committing any change to any context file, `persona.ttl`, `context.ttl`, `cell.ttl`, `category.ttl`, or `persona-shacl.ttl`, increment the **minor version number** in that file's `owl:versionInfo` annotation and update the description to summarise the change. For example:

```
owl:versionInfo "Version 3.0.3 - added social network"@en
```
becomes:
```
owl:versionInfo "Version 3.0.4 - added birth date"@en
```

## Integrity Checks

Files inside any directory named `under-development/` (at any depth) are works-in-progress and must be **excluded from all integrity checks** below.

After any change to context files or cell DataBooks, verify the following.

**Check 1 — Diagram ↔ files ↔ README coverage**: Every numbered context circle in any of the 11 cell diagrams (`example/images/`) must have (a) a corresponding `.databook.md` file in `example/contexts/` and (b) a row in one of the tables in the **Alice's Personas and Contexts** section of `README.md`. Conversely, every row in those tables must correspond to a numbered circle in a diagram and a file that actually exists. If a circle exists in a diagram but has no `.databook.md` file or README row, create them to match the diagram.

**Check 2 — Filename convention**: Every context filename must follow `<subject>.<claimant>(<containing-cell>)(<NN>).databook.md`. `<subject>` must be `self` when the subject is `:Self`, or the full hyphenated lowercase name otherwise. `<claimant>` must be `self` when the claimant is `:Self`, or the full hyphenated lowercase name otherwise — except for `c:Group` contexts, where it must be the literal string `members`. `(<containing-cell>)` encodes the local name of the one `cell:Cell` DataBook whose `sc-context`/`graph` field references this context (found by reverse lookup — a context carries no field pointing back at its cell): when that cell's local name includes a `(parent)` qualifier (e.g. `bob-johnson(others)`), it appears as two separate segments `(bob-johnson)(others)`; when there is no qualifier (e.g. `health`), a single segment suffices. `(<NN>)` is the zero-padded two-digit context number. Exception: a context linked via `cell:graph` rather than `cell:sc-context` drops the `<subject>.<claimant>` prefix and uses the literal `context` instead — `context(<containing-cell>)(<NN>).databook.md`. If a filename does not match one of these two patterns, rename it to conform.

**Check 3 — containing-cell ↔ filename consistency**: For every context DataBook in `example/contexts/` (excluding `under-development/`), find the one cell DataBook (in `example/categories/`, the only remaining per-node instance tree — canonical templates have no cells of their own since category.ttl 1.8.0) whose `sc-context`/`graph` field references this context's `id` — a context carries no field pointing back at its cell, so this is always a reverse lookup, never a direct read. That cell's filename, **minus a trailing `-cell` suffix**, must equal the `(<containing-cell>)` segment extracted from the context's filename. When the filename uses two separate parenthetical segments before the number (e.g. `(bob-johnson)(others)`), concatenate them as `bob-johnson(others)` to form the expected local name. A context that resolves to zero or more than one referencing cell is also an error. Run:

```python
import os, re, yaml

ctx_dir = 'example/contexts'
cell_dirs = ['example/categories']
link_fields = ('sc-context', 'graph')

def fn_cell_local(fname):
    base = fname[:-len('.databook.md')]
    m = re.match(r'^context((?:\([^)]+\))+)\(\d{2}\)$', base)
    if not m:
        m = re.match(r'^[^.]+\.[^(]+((?:\([^)]+\))+)\(\d{2}\)$', base)
    if not m:
        return None
    segs = re.findall(r'\(([^)]+)\)', m.group(1))
    return segs[0] if len(segs) == 1 else f'{segs[0]}({segs[1]})'

def frontmatter(path):
    text = open(path).read()
    m = re.match(r'^---\n(.*?)\n---', text, re.DOTALL)
    return yaml.safe_load(m.group(1)) if m else None

# context id -> list of cell filenames that reference it
context_to_cells = {}
for cell_dir in cell_dirs:
    for dirpath, _, filenames in os.walk(cell_dir):
        if 'under-development' in dirpath.split(os.sep):
            continue
        for fname in filenames:
            if not fname.endswith('.databook.md'):
                continue
            fm = frontmatter(os.path.join(dirpath, fname))
            if not fm or fm.get('type') != 'cell-databook':
                continue
            mia = fm.get('mia', {}) or {}
            for field in link_fields:
                val = mia.get(field)
                if not val:
                    continue
                for ctx_id in (val if isinstance(val, list) else [val]):
                    context_to_cells.setdefault(ctx_id, []).append(fname)

errors = 0
for fname in sorted(os.listdir(ctx_dir)):
    if not fname.endswith('.databook.md'):
        continue
    path = f'{ctx_dir}/{fname}'
    fm = frontmatter(path)
    ctx_id = fm.get('id')
    cells = context_to_cells.get(ctx_id, [])
    if len(cells) != 1:
        print(f'{fname}: expected exactly 1 referencing cell, found {len(cells)}: {cells}')
        errors += 1
        continue
    cell_local = cells[0][:-len('.databook.md')]
    if cell_local.endswith('-cell'):
        cell_local = cell_local[:-len('-cell')]
    expected = fn_cell_local(fname)
    if cell_local != expected:
        print(f'MISMATCH {fname}:')
        print(f'  filename implies: {expected!r}')
        print(f'  referencing cell (–cell stripped): {cell_local!r}')
        errors += 1
if not errors:
    print('All contexts resolve to exactly one referencing cell, matching their filenames.')
```

If mismatches appear, the filename `(<containing-cell>)` segments are authoritative — update the cell DataBook's `sc-context`/`graph` value to reference the correct context (or rename the context file if it was misnamed).

**Check 4 — No orphan Persons**: Every `persona:Person` individual other than `:Self` must be reachable via `BFO_0000115` (has member part) from a `g:Group` or from a Social Network individual linked to another `persona:Person` via `persona:hasSocialNetwork`. `:Self` is always the root and needs no incoming link. **Exception**: a `persona:Person` referenced only via a professional/service-designation property (e.g. `persona:hasPrimaryCarePhysician`) rather than social-network membership is exempt — it represents a service relationship (e.g. a physician), not a social connection, so it has no social network to be reachable from. Example: `:Jane_Kopakolva` (context #25), Paula Walker's primary care physician.

**Check 5 — Validation command completeness**: The `## Validation` section of `README.md` must document two tiers. Tier 1 uses five steps: (1) a `find example -name "*.databook.md"` loop using `databook extract` to extract turtle content and produce a merged turtle file of all context data (excluding `under-development/`); (1b) `python3 yaml-to-rdf.py` to synthesize `cat:`/`cell:`/`context:` triples from category, cell, and context DataBook `mia.` YAML frontmatter — `databook extract` only pulls fenced Turtle blocks, which category/cell DataBooks never carry, so without this step `cat:Node`/`cell:Cell` individuals and `context:SCcontext`'s subject/claimant never reach the merged graph and `category-shacl.ttl`/`cell-shacl.ttl`/`context-shacl.ttl`'s `:SCcontextShape` never fire against real instance data; (2) a `riot` merge of both extracted files with all application ontology TTL files (including `cell-templates.ttl`) and the foundation ontologies listed explicitly from `project_files/`; (3) a `grep -v owl:imports` on `persona-shacl.ttl`, `context-shacl.ttl`, `category-shacl.ttl`, `cell-shacl.ttl`, `group-shacl.ttl`, and `organization-shacl.ttl` to collect shapes (`shacl/jscontactcard-shacl.ttl` and `cell-templates-shacl.ttl` are excluded here — they target document classes and would fire incorrectly on all individuals when applied to merged data; `pdn-identity-shacl.ttl` is also excluded — its ontology, `pdn-identity.ttl`, isn't part of the Step 2 merge, since nothing in the active ontology stack references an `identity:` term any more); (4) a `shacl validate` call. Tier 2 lists explicit per-file `databook extract` + `riot` + `shacl validate` commands for each template context file paired with its shapes source — `cell-templates-shacl.ttl` directly for BirthCertificate/DriversLicense/Passport/MedicalAppointment, or `shacl/jscontactcard-shacl.ttl` directly for JSContactCard (both are plain `.ttl` files, not DataBook fragments); Tier 2 does not need `yaml-to-rdf.py` since it validates individual context files directly, not category/cell DataBooks. If the commands change, update the README to match.

**Check 6 — PNG file location**: The diagram PNG for every context file must be stored directly in `example/contexts/images/` (flat, no subfolders — not `images/example/`). Files in `under-development/` are excluded.

**Check 7 — PNG filename convention**: Every diagram PNG in `example/contexts/images/` must use the same base filename as the corresponding `.databook.md` file in `example/contexts/`, with `.png` substituted for `.databook.md`. For example, `self.self(boston-hub-society)(affiliations)(14).databook.md` → `self.self(boston-hub-society)(affiliations)(14).png`. If the PNG does not yet exist, the README Diagram cell must be marked `*(todo)*` rather than left blank.

**Check 8 — No broken image links in README**: Every PNG path referenced in `README.md` (both `<img src="...">` tags and `[view](...)` table links) must resolve to an actual file on disk. Run:

```bash
python3 -c "
import re, os
content = open('README.md').read()
pngs = [m.group(1) for m in re.finditer(r'src=[\"\\'](.*?\.png)[\"\\']', content)]
pngs += [m.group(1) for m in re.finditer(r'\]\((example/[^\s\"\']+\.png)\)', content)]
missing = [p for p in sorted(set(pngs)) if not os.path.exists(p)]
[print('MISSING:', p) for p in missing] or print('All PNG refs OK')
"
```

If any `MISSING:` lines appear, either add the file or update the link.

**Check 9 — Cell/Category filename ↔ id consistency**: This check applies only to `example/categories/` — the user's own instance tree — since there is no longer a separate canonical-instance file tree (`categories-person/`/`categories-org/` were removed in category.ttl 1.8.0; the canonical tree is now the `cat:Category` class hierarchy in `category.ttl` itself, with class-level templates in `cell-templates.ttl`). Each category is associated with one or more `cell-databook` DataBooks — the relationship between a category and its cells is many-to-one (many cells may share the same `cat:Node`), not 1:1; the example tree simply happens to show only one cell per category so far. A `category-databook`'s own filename/id is unchanged; each of its cell DataBooks conventionally uses the category's filename/id with a `-cell` suffix (with a further distinguishing suffix, e.g. `-cell-2`, if more than one cell shares the category). For every `.databook.md` in `example/categories/` (both types), the filename root (the filename with `.databook.md` stripped) must exactly match the local name portion of the file's `id:` IRI (the string after the IRI base, `http://www.example.org/mia/categories/`). `example/categories/` is nested into folders mirroring its category tree (see Check 11), so it must be walked recursively. Run:

```python
import os, re

def iter_databooks(directory, recursive):
    if recursive:
        for dirpath, _, filenames in os.walk(directory):
            for fname in sorted(filenames):
                if fname.endswith('.databook.md'):
                    yield os.path.join(dirpath, fname), fname
    else:
        for fname in sorted(os.listdir(directory)):
            if fname.endswith('.databook.md'):
                yield os.path.join(directory, fname), fname

checks = [
    ('example/categories', 'http://www.example.org/mia/categories/', True),
]
for directory, base, recursive in checks:
    for path, fname in iter_databooks(directory, recursive):
        root = fname[:-len('.databook.md')]
        text = open(path).read()
        m = re.search(r'^id:\s*(\S+)', text, re.MULTILINE)
        fid = m.group(1).strip() if m else ''
        local = fid[len(base):] if fid.startswith(base) else None
        if local != root:
            print(f'MISMATCH  {path}  root={root!r}  id={local!r}')
```

If a mismatch is found, rename the file so its root matches the id local name (preferred) or update the `id:` to match the filename — whichever is consistent with the broader naming conventions. Additionally, every category's associated cell(s) must resolve to `cell-databook` file(s) that exist in the **same directory** (see Check 11) — found via `mia.cell` on the category, pointing forward at its cell(s) (`cell:Cell` has no property pointing back at all, regardless of the node's kind). A category may have more than one such cell.

**Check 10 — Example cell diagrams are authoritative**: The 11 cell diagrams in `example/images/` are the authoritative source of truth for the example cell tree. When any discrepancy is found between a diagram and the DataBook files, the diagram wins — update the DataBooks to match, not the other way around. Each diagram box now corresponds to a `category-databook` (tree position, box label = its `title:`) in `example/categories/` associated with one or more `cell-databook`s (content) in the same folder, via the category's own `mia.cell` value(s). After any change to `example/categories/` DataBooks or to the 11 diagrams, verify all of the following:

- **10a — Every cell box has a category DataBook**: Every cell box (blue/tan canonical or white user-defined) shown in any of the 11 diagrams must have a corresponding `category-databook` `.databook.md` file in `example/categories/` whose `title:` matches the box label. If a box has no DataBook, create the category DataBook and its associated cell DataBook.

- **10b — Every category DataBook has a diagram box**: Every `category-databook` file in `example/categories/` (except `categories.databook.md` itself, which is the invisible root) must appear as a visible box in at least one of the 11 diagrams. If a DataBook has no corresponding box, either add it to the appropriate diagram or delete the category DataBook and its associated cell DataBook(s).

- **10c — Solid context circles match DataBook links**: Every solid (filled) context circle attached to a cell box indicates a real context link. The **cell DataBook** associated with that box's category (via the category's own `mia.cell` value(s)) must carry a corresponding `sc-context` or `graph` value pointing to the context DataBook IRI. A dashed (empty) circle indicates an unfilled slot — the cell DataBook must NOT have a link for that slot.

- **10d — Numbered context circles have matching files**: Every numbered context circle (e.g. `[10]`, `[17]`) shown in a diagram must correspond to an actual `.databook.md` file in `example/contexts/` whose filename contains that number (e.g. `(10)`, `(17)`).

- **10e — Child arrows match DataBook child links**: Every downward child arrow from cell box A to cell box B in a diagram must correspond to a `child:` entry in A's **category** DataBook pointing to B's category IRI. Conversely, every `child:` entry in a category DataBook must be reflected by a visible child arrow in the diagram.

The 11 diagrams are: `example/images/people.png`, `example/images/people2.png`, `example/images/health.png`, `example/images/work.png`, `example/images/companies.png`, `example/images/finances.png`, `example/images/gov-state.png`, `example/images/gov-federal.png`, `example/images/gov-municipality.png`, `example/images/misc.png`, `example/images/affiliations.png`.

**Check 11 — Physical folder structure mirrors the `child:` tree in `example/categories/`**: This check applies only to `example/categories/` — the user's own instance tree — since there is no longer a separate canonical-instance file tree to mirror (`categories-person/`/`categories-org/` were removed in category.ttl 1.8.0). The tree is organized as nested filesystem folders that mirror the category hierarchy, rather than one flat directory. Each category's own `category-databook` `.databook.md` file lives in a folder together with its associated cell DataBook(s) (folder naming is not standardized — it may be the category's `title`, a `catType`-prefixed disambiguator, or a role-based label; this check does not validate folder names, only nesting). The rule: for every `mia.child` link from category A to category B, B's `.databook.md` file must live in a folder that is a **direct subfolder** of the folder containing A's `.databook.md` file — not deeper, not a sibling, not the same folder. The tree's root DataBook (`categories.databook.md`) sits directly in the tree's top-level directory, alongside its associated `-cell` DataBook. A category's association with its cell(s) is recorded directly on the category, via its own `mia.cell` value(s) — `cell:Cell` has no property pointing back at all, so this is the only place the association is recorded. **The relationship is many-to-one (many cells may share one category), not 1:1** — the example tree currently shows only one cell per category, but that's incidental to the data, not a constraint; a category with two or more `mia.cell` values, each pointing at its own `-cell`-suffixed DataBook, is valid. Run:

```python
import os, re, yaml

def check_tree(root):
    id_to_dir, id_to_children, dir_to_ids, id_to_type, id_to_cells = {}, {}, {}, {}, {}

    for dirpath, _, filenames in os.walk(root):
        for fname in filenames:
            if not fname.endswith('.databook.md'):
                continue
            path = os.path.join(dirpath, fname)
            fm = yaml.safe_load(re.match(r'^---\n(.*?)\n---', open(path).read(), re.DOTALL).group(1))
            cid = fm['id']
            rel_dir = os.path.relpath(dirpath, root)
            id_to_dir[cid] = rel_dir
            id_to_type[cid] = fm.get('type')
            dir_to_ids.setdefault(rel_dir, []).append(cid)
            mia = fm.get('mia', {}) or {}
            child = mia.get('child')
            if child:
                id_to_children[cid] = child if isinstance(child, list) else [child]
            cell = mia.get('cell')
            if cell:
                id_to_cells[cid] = cell if isinstance(cell, list) else [cell]  # category id -> list of its cells' ids

    # Only category-databook files define the tree; each dir must have
    # exactly one, plus one or more associated cell-databooks.
    cat_ids_by_dir = {d: [i for i in ids if id_to_type.get(i) == 'category-databook'] for d, ids in dir_to_ids.items()}

    def parent_of(reldir):
        if reldir == '.':
            return None
        p = os.path.dirname(reldir)
        return p if p != '' else '.'

    errors = []
    for d, ids in dir_to_ids.items():
        cats = cat_ids_by_dir[d]
        if len(cats) != 1:
            errors.append(f'Expected exactly one category-databook in {d!r}, found {len(cats)}: {cats}')
            continue
        cat_id = cats[0]
        cell_ids = id_to_cells.get(cat_id, [])
        cell_ids_here = [c for c in cell_ids if id_to_dir.get(c) == d]
        if not cell_ids_here:
            errors.append(f'Category {cat_id!r} in {d!r} has no associated cell-databook (via mia.cell) in the same folder')

    id_to_cat_dir = {i: d for d, ids in cat_ids_by_dir.items() for i in ids}

    for parent_id, children in id_to_children.items():
        if id_to_type.get(parent_id) != 'category-databook':
            continue
        parent_dir = id_to_cat_dir.get(parent_id)
        for child_id in children:
            child_dir = id_to_cat_dir.get(child_id)
            if child_dir is None:
                errors.append(f'Child id {child_id!r} (child of {parent_id}) not found on disk')
            elif parent_of(child_dir) != parent_dir:
                errors.append(f'NESTING MISMATCH: child {child_id!r} dir={child_dir!r} is not a direct subfolder of parent {parent_id!r} dir={parent_dir!r}')

    id_by_dir = {d: ids[0] for d, ids in cat_ids_by_dir.items() if len(ids) == 1}
    for this_dir, this_id in id_by_dir.items():
        this_path = os.path.join(root, this_dir) if this_dir != '.' else root
        declared = set(id_to_children.get(this_id, []))
        for entry in sorted(os.listdir(this_path)):
            full = os.path.join(this_path, entry)
            if not os.path.isdir(full):
                continue
            sub_rel = os.path.join(this_dir, entry) if this_dir != '.' else entry
            if sub_rel in id_by_dir:
                if id_by_dir[sub_rel] not in declared:
                    errors.append(f'ORPHAN NESTING: {sub_rel!r} (id={id_by_dir[sub_rel]}) is nested under {this_dir!r} (id={this_id}) but not declared as its child')
            elif not any(fn.endswith('.databook.md') for _, _, fns in os.walk(full) for fn in fns):
                errors.append(f'EMPTY/PLACEHOLDER FOLDER (no databook.md anywhere under it): {sub_rel!r} under {this_dir!r}')

    return errors

for root in ['example/categories']:
    errors = check_tree(root)
    print(f'{root}: ' + (f'{len(errors)} issue(s) found:' if errors else 'OK — folder structure matches the child-link tree.'))
    for e in errors:
        print(' -', e)
```

If a nesting mismatch or orphan is found, move the file to the correct folder (preferred) or fix the `mia.child` link — whichever reflects the intended tree. An empty/placeholder folder is not necessarily an error — flag it to the user rather than deleting it, since it may be a deliberate placeholder for content not yet added.

**Check 12 — `cell.ttl` matches `images/cell-ontology/cell.png`**: Current as of cell.ttl 3.7.0 — verified aligned. `Cell` (abstract, blue) carries only what's common to every cell regardless of facet: `note`, `folder`, `graph`, `sc-context`. `Cell` splits into two orthogonal facets, mirroring `category.ttl`'s Category/Node split (see Check 14): `TCell` (abstract, blue, the template facet) carries `templateShape` (to a `sh:NodeShape` box); `ACell` (abstract, blue, the actual/instantiated facet) carries the new `shape` property (drawn in red in the diagram to flag it as newly added, also to a `sh:NodeShape` box), `creator` (to a union of `p:Person`/`o:Organization`/`g:Group`), and `parties` (to `OneParty`/`TwoParty`/`ThreePlusParty` 1..1). The party-composition hierarchy — `OneParty` and `MultiParty` (abstract) → `TwoParty`/`ThreePlusParty` — hangs off `ACell` now, not `Cell` directly; `TCell` has no subclasses of its own, since a template cell individual is instead multi-typed with both `TCell` and its `ACell`-lineage class (e.g. `OneParty`) — see `cell-templates.ttl`. `MultiParty` shows no arrows of its own, matching `cell:sc-context`'s domain being the broader `cell:Cell` rather than `cell:MultiParty`. No arrow points from `Cell`, `TCell`, or `ACell` to any `cat:Node` box, matching that link now being asserted only on the category side (see Check 14). This diagram is the ontology-level (not example-tree) picture of `cell:Cell`'s structure (redrawn for the 3.0.0/1.0.0 Cell/Category split, then again for the 3.7.0 TCell/ACell split) — the party-composition hierarchy and its content-linking properties. Unlike Check 10 (example diagrams, where the diagram always wins), this check does not presume which side is authoritative when the two disagree — surface the discrepancy and ask. After any change to `cell.ttl` or to this diagram, verify:

- **12a** — every property arrow shown off `Cell` (`note`, `folder`, `graph`, `sc-context`) has a corresponding `cell:` property in `cell.ttl` with `rdfs:domain cell:Cell`. Every arrow off `TCell` (`templateShape`) has `rdfs:domain cell:TCell`; every arrow off `ACell` (`shape`, `creator`, `parties`) has `rdfs:domain cell:ACell` — `creator` and `parties` were narrowed here from `cell:Cell` in cell.ttl 3.7.0, and `shape` is new as of that version. `MultiParty` should show no arrows of its own — it carries no property, since `cell:sc-context`'s domain is the broader `cell:Cell`. Each arrow's target type in the diagram must match the property's `rdfs:range` — `sc-context`'s is `context:SCcontext`, `creator`'s is the union of `p:Person`/`g:Group`/`o:Organization`, `parties`'s is `cell:ACell` itself (value is the concrete subclass, not `xsd:string`; range narrowed from `cell:Cell` in 3.7.0), `templateShape`'s and `shape`'s are both `sh:NodeShape` — two separate arrows from two different boxes (`TCell` vs `ACell`) to what may be drawn as the same target, since they're two distinct properties, not one property under two names. No arrow should point from `Cell`, `TCell`, or `ACell` to any `cat:Node` box — that link is now asserted only on the category side (see Check 14).
- **12b** — every `cell:` property defined in `cell.ttl` appears as an arrow in the diagram, under the box matching its domain — `Cell`, `TCell`, or `ACell` (catches new properties added to the ttl but never drawn, or drawn under the wrong box).
- **12c** — the class hierarchy `Cell` → `TCell`/`ACell` (both abstract), and separately `ACell` → `MultiParty` (abstract) → `TwoParty`/`ThreePlusParty`, plus `ACell` → `OneParty`, shown in the diagram matches `cell.ttl`'s actual `rdfs:subClassOf` relationships (by class local name, not just position). `OneParty` and `MultiParty` must not be drawn as direct children of `Cell` — both moved under `ACell` in cell.ttl 3.7.0.
- **12d** — each concrete `Cell` subtype's example `cell:label` value shown in the diagram (`"Cell"`, `"Two-Party Cell"`, `"Multi-Party Cell"`) matches that subtype's actual `cell:label` value in `cell.ttl`. `cell:label` here is a class-level default display name, distinct from `cat:label` (category.ttl's per-instance display name) — `Cell`, `TCell`, `ACell`, and `MultiParty` are all abstract and carry no `cell:label` of their own.

**Check 13 — `context.ttl` matches `images/context-ontology/context.png`**: Current as of context.ttl 1.9.0 — verified aligned. `Context` shows only `template`; `SCcontext` (renamed from `XBXcontext`, subClassOf `Context`) shows `subject` and `claimant` (both correctly targeting `p:Person, g:Group or o:Organization`, not `i:PDNidentifier`) — no `about-by` arrow, matching context.ttl 1.9.0's deletion of `context:about-by` (the four self-vs-other cases it used to distinguish are now derived directly from the `subject`/`claimant` combination, not a separate property). No leaf subtype boxes are shown below `SCcontext`, correctly matching the earlier deletion of `SBScontext`/`OBScontext`/`OBOcontext`/`SBOcontext` — `SCcontext` has no subclasses now. This diagram is the ontology-level picture of `context:Context`'s structure. After any change to `context.ttl` or to this diagram, verify:

- **13a** — every property arrow shown off `Context` in the diagram (`template`) has a corresponding `context:` property in `context.ttl` with `rdfs:domain context:Context`, and its target type matches the property's `rdfs:range`.
- **13b** — every property arrow shown off `SCcontext` in the diagram (`subject`, `claimant`) has a corresponding `context:` property with `rdfs:domain context:SCcontext`; both targets in the diagram must match their actual `rdfs:range` — a union of `p:Person`/`g:Group`/`o:Organization`, not `i:PDNidentifier`. No `about-by` arrow should appear — `context:about-by` was deleted (1.9.0).
- **13c** — every `context:` property with domain `context:Context` or `context:SCcontext` defined in `context.ttl` appears in the diagram under the correct box (catches new properties added to the ttl but never drawn, or drawn under the wrong box).
- **13d** — no subclasses appear below `SCcontext` — `context.ttl` defines none (`SBScontext`/`OBScontext`/`OBOcontext`/`SBOcontext` were deleted in 1.8.0). If any reappear here or in `context.ttl`, reconcile them.

**Check 14 — `category.ttl` matches `images/category-ontology/category.png`**: Current as of category.ttl 1.14.0 — verified aligned. `cat:templateShape` was briefly added in category.ttl 1.9.0 then moved out entirely to `cell.ttl` (as `cell:templateShape`) in 1.12.0, since its domain/range never referenced a `cat:` term — so the diagram correctly shows no `templateShape` arrow under `Category` at any point (see Check 12 for that property's diagram, verified aligned as of cell.ttl 3.7.0). This diagram is the ontology-level picture of `cat:Category`'s and `cat:Node`'s structure: `cat:Category` (abstract, blue) carries `catType` (to `xsd:string`) and `templateCell` (to a `cell:Cell` box) — an annotation asserted directly on the class, not an instance; `cat:Person`/`cat:Organization` (abstract, blue) are its direct subclasses, each with representative leaf examples (Affiliations/People/Work under Person; Suppliers/People (org) under Organization); separately, `cat:Node` (abstract, blue) carries `child` (self-loop) and `cell` (to a `cell:Cell` box — domain simplified from `unionOf(CategoryDefined, UserDefined)` to `cat:Node` itself in category.ttl 1.14.0, since `cat:Canonical`'s deletion in 1.8.0 left `CategoryDefined`/`UserDefined` as `cat:Node`'s only subclasses, making the narrower union redundant with `cat:Node`), and splits into only `cat:CategoryDefined`/`cat:UserDefined` (both concrete, black, correctly showing the class's current name — renamed from `Copy` in category.ttl 1.13.0) — `category` arrows from `CategoryDefined` to `Category` (recording which class a node represents, and by extension what it was instantiated from — there is no separate canonical individual any more), and both `CategoryDefined` and `UserDefined` have their own `label` arrow to `xsd:string`. This diagram does not presume which side is authoritative when the two disagree — surface the discrepancy and ask. After any change to `category.ttl` or to this diagram, verify:

- **14a** — every property arrow shown off `Category` (`catType`, `templateCell`) has a corresponding `cat:` property in `category.ttl` with `rdfs:domain cat:Category` (`catType`) or `owl:Class` (`templateCell`, an annotation property asserted on the class itself, not scoped to `cat:Category` specifically at the OWL level); every arrow off `Node` (`child`, `cell`) has `rdfs:domain cat:Node`; the `category` arrow off `CategoryDefined` has `rdfs:domain cat:CategoryDefined`; the `label` arrows off `CategoryDefined` and `UserDefined` have `rdfs:domain` the union class `[ owl:unionOf ( cat:CategoryDefined cat:UserDefined ) ]` — shown as two separate arrows to the same `label` target, not two separate properties. No `templateShape` arrow should appear anywhere in this diagram — it's a `cell.ttl` property now (see Check 12), not a `category.ttl` one. Each arrow's target type must match the property's `rdfs:range` — `category`'s is `cat:Category`, `templateCell`'s is `cell:Cell`, `cell`'s is `cell:Cell` (a distinct box from `templateCell`'s target, even though both point at `cell:Cell` — one is a class-level annotation, the other an instance-level link off `Node`). There must be no `Canonical` box and no `copiedFrom` arrow anywhere — both were removed in category.ttl 1.8.0. The concrete `Node` subclass box must read `CategoryDefined`, not `Copy` — renamed in category.ttl 1.13.0.
- **14b** — every `cat:` property defined in `category.ttl` appears as an arrow in the diagram, under the box matching its domain (catches new properties added to the ttl but never drawn, or drawn under the wrong box).
- **14c** — the class hierarchy `Category` → `Person`/`Organization` (both abstract) and their leaf subclasses, and separately `Node` (abstract) → `Copy`/`UserDefined`, shown in the diagram matches `category.ttl`'s actual `rdfs:subClassOf` and `cell:abstract` values. `Category` and `Node` are two separate trees, not one — like `cell:Cell`/`cat:Category` before it (Check 12), `cat:Category` is not `rdfs:subClassOf cat:Node` and vice versa.

**Check 15 — `images/category-ontology/cat-cell-context.png` matches example usage**: Current as of category.ttl 1.5.0 and cell.ttl 3.4.1 — verified aligned as of that version; category.ttl 1.8.0's removal of `cat:Canonical` may require a re-check of the box descriptions below. The four context circles per cell (self-by-self, other-by-self, self-by-other, other-by-other) remain a valid illustration under the consolidated `cell:sc-context`, since the diagram was never tied to the four now-retired property names in the first place. This diagram illustrates representative cell/category associations, generically rather than tied to a specific example instance: "Work" (a `cat:CategoryDefined` representing `cat:Work`, no override label), "Organization / Acme" (a `cat:CategoryDefined` representing `cat:Organization`, `cat:label`-renamed "Acme"), "Favorites" (a hypothetical `cat:UserDefined` category with no canonical counterpart, not tied to any real example data — there is currently no real `cat:UserDefined` example in the tree), "Person / Bob Johnson" (a `cell:TwoParty` cell, all four context link types filled), and "Affiliations / Boston Hub Society" (a `cell:ThreePlusParty` cell with two other-party members, Carol and BHS) — it replaces the earlier `images/cell-ontology/cells+contexts.png`. Each box's header shows `cat:catType` (green) over `cat:label` (bold) when a label is set, or just `catType` alone otherwise (e.g. "Work", which has no override label). ⚠️ The Key legend still labels two color swatches "Organizational" and "Personal" — leftover from before category.ttl's `cat:Organizational`→`cat:Organization`/`cat:Personal`→`cat:Person` rename; the box headers themselves already say "Organization" correctly, only the legend text needs updating. Re-verify each box's filled/dashed context circles remain a valid illustration of the properties and cardinalities described in the Cell and Category Ontology sections of `README.md` after any change to those properties.

**Check 16 — IRI roots: `mee.foundation/ontologies` for foundational files, `www.example.org` for example data**: Every foundational ontology and SHACL shapes file — `persona.ttl`, `context.ttl`, `cell.ttl`, `category.ttl`, `cell-templates.ttl`, `pdn-identity.ttl`, `group.ttl`, `organization.ttl`, `persona-templates.ttl`, their `*-shacl.ttl` companions (including `cell-templates-shacl.ttl`), and the per-template files in `shacl/` — must declare its `owl:Ontology` IRI under `http://mee.foundation/ontologies/`. There is no longer a separate canonical category/cell DataBook tree to check (`categories-person/`/`categories-org/` were removed in category.ttl 1.8.0) — the canonical tree's IRI roots are covered by `category.ttl`/`cell-templates.ttl` themselves. Every DataBook under `example/categories/` and `example/contexts/` (excluding `under-development/`) represents Alice's own example instance data, so its `id:` must be grounded under `http://www.example.org/` (or `https://www.example.org/`). Run:

```python
import os, re, glob

FOUNDATIONAL_TTL = [
    'persona.ttl', 'context.ttl', 'cell.ttl', 'category.ttl', 'cell-templates.ttl',
    'pdn-identity.ttl', 'group.ttl', 'organization.ttl', 'persona-templates.ttl',
    'persona-shacl.ttl', 'cell-shacl.ttl', 'category-shacl.ttl', 'context-shacl.ttl',
    'group-shacl.ttl', 'organization-shacl.ttl', 'pdn-identity-shacl.ttl',
    'cell-templates-shacl.ttl',
] + sorted(glob.glob('shacl/*.ttl'))

errors = 0
for path in FOUNDATIONAL_TTL:
    if not os.path.exists(path):
        continue
    text = open(path).read()
    m = re.search(r'^<(http[^>]+)>\s+rdf:type\s+owl:Ontology', text, re.MULTILINE)
    if not m:
        print(f'NO owl:Ontology IRI FOUND: {path}')
        errors += 1
        continue
    if not m.group(1).startswith('http://mee.foundation/ontologies/'):
        print(f'WRONG ROOT (expected mee.foundation): {path} -> {m.group(1)}')
        errors += 1

def check_id_root(pattern, expected_prefixes, recursive):
    global errors
    paths = glob.glob(pattern, recursive=recursive)
    for path in sorted(paths):
        if 'under-development' in path.split(os.sep):
            continue
        text = open(path).read()
        m = re.search(r'^id:\s*(\S+)', text, re.MULTILINE)
        if not m:
            continue
        iri = m.group(1).strip()
        if not any(iri.startswith(p) for p in expected_prefixes):
            print(f'WRONG ID ROOT: {path} -> {iri}')
            errors += 1

check_id_root('example/categories/**/*.databook.md', ['http://www.example.org/', 'https://www.example.org/'], True)
check_id_root('example/contexts/*.databook.md', ['http://www.example.org/', 'https://www.example.org/'], False)

print('OK — no IRI-root violations found.' if errors == 0 else f'{errors} violation(s) found.')
```

If a violation is found, rename the offending file's `owl:Ontology`/`id:` IRI to the correct root, and update every DataBook `shapes:` YAML reference, catalog entry, and cross-reference that pointed at the old IRI to match (see Check 5's Tier 1/Tier 2 validation commands, which also hardcode these IRIs via the `shapes:` mechanism).

## Keeping Files in Sync

Whenever changes are made to any context file, `persona.ttl`, or `context.ttl`, `persona-shacl.ttl` must be updated to match:

- **New property usage in a context file** (e.g., a new physical characteristic, relationship, or identifier added to a Person or Persona instance) → add or extend a SHACL shape to validate that property on the relevant target class.
- **New class or property defined in `persona.ttl`** (e.g., `persona:hasSocialNetwork`) → add a SHACL shape that constrains how instances of the domain class may or must use it.

Always update `persona-shacl.ttl` in the same edit session as the change that triggers it.

## Validation

**SHACL validation** (e.g., using Apache Jena's `shaclvalidate`):
```bash
shaclvalidate -datafile example/contexts/self.self(boston-hub-society)(affiliations)(14).databook.md -shapesfile persona-shacl.ttl
```

**Protégé**: Load `persona.ttl`; Protégé will import the domain ontologies via IRI resolution. Use the reasoner (HermiT/Pellet) to check consistency.

## README Coverage

`README.md` must be written in US English. Use American spellings throughout — e.g. "organization" not "organisation", "color" not "colour".

All classes and properties defined in `persona.ttl`, `context.ttl`, `cell.ttl`, and `category.ttl` must be mentioned in `README.md` in the sections before the **Illustrative Example: Alice Walker** section. The only intentional exceptions are the internal ontology documentation annotation properties (`usesRequiredClass`, `usesOptionalClass`, `usesCCOClass`, `usesCCOProperty`, `usagePattern`), which are infrastructure for self-documenting the ontology, not user-facing terms.

In `README.md`, every mention of a class defined in `persona.ttl` must appear in backticks with the `p:` prefix (e.g. `p:Persona`, `p:Wallet`), every mention of a class or property defined in `context.ttl` must appear in backticks with the `c:` prefix (e.g. `c:contextType`, `c:SelfClaimed`), every mention of a class or property defined in `cell.ttl` must appear in backticks with the `cell:` prefix (e.g. `cell:Cell`, `cell:parties`), and every mention of a class or property defined in `category.ttl` must appear in backticks with the `cat:` prefix (e.g. `cat:Category`, `cat:catType`). Every capitalized mention of `Person` (the CCO class) must also appear in backticks. These formatting rules do **not** apply inside headings or subheadings.

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
