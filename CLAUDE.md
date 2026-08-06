# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an **RDF/OWL ontology project** — a formal semantic knowledge model for representing natural people's identity data in the Mee Identity Agent (MIA). It comprises four peer application ontologies:

- **Persona ontology** (`persona.ttl`): models identity data — names, addresses, identifiers, relationships, payment cards, and more — structured around topic-specific `Person` instances. Imports and profiles existing domain ontologies, documenting which of their classes and properties Mee uses, and extends them with Mia-specific terms.
- **Topic ontology** (`topic.ttl`): defines controlled vocabularies for classifying topic files — who claimed the data (`claimant`), and what or whom the file is about (`subject` — any resource IRI; the ontology does not require it to be a person's identity, though in the example data every `subject` value happens to be a `p:Person`/`g:Group`/`o:Organization`, a convention of the example, not an ontology requirement). The four self-vs-other combinations these two values distinguish (self-by-self, other-by-self, other-by-other, self-by-other) are derived directly from `subject`/`claimant`, not a separate property or class hierarchy — `SCTopicGraph` has no subclasses.
- **Cell ontology** (`cell.ttl`): defines `cell:Cell` — the self-contained *content* facet of a cell, carrying only what's common to every cell (`origin`, range `cat:Category`, at most one value (0..1, absent/nil when a cell's containing folder's own name matches no real `cat:Category` subclass) — for a cell whose folder does match one, that class itself, letting a recipient's Mia app use it as a hint for where to file a shared cell in its own tree; referenced by name without `owl:imports category.ttl`, added in cell.ttl 3.20.0 to close the previously open `cell.png` `origin`-arrow discrepancy without contradicting `cell:Cell`'s "no link to a tree position" design, since its range is the classificatory `cat:Category`, not a tree position (category.ttl 1.31.0 deleted `cat:Folder` and its subclasses outright — a folder is now purely a filesystem concept with no RDF individual at all)) — `cell:folder`, which formerly stored a path to a cell's own folder (carrying `note` too until cell.ttl 3.15.0 merged the separate notes/files folder hierarchies into one), was removed outright in cell.ttl 3.23.0, since a folder holds at most one cell-databook (cell.ttl 3.22.0) and so a cell's folder is now always unambiguously wherever its own cell-databook physically lives, with no path left to store; cell.ttl 3.16.0 documented the folder ownership boundary rule — a subfolder belongs to a different, nested cell, not this one, iff it directly contains a `*.databook.md` file (the only DataBook type in a user's instance tree is now `cell-databook`; cell.ttl 3.19.0 reworded this rule once the separate `category-databook` type it originally keyed on was retired), checkable one folder at a time with no category-tree traversal — plus two further orthogonal facets: `cell:TCell` (template content, carrying `templateShape`) and `cell:ACell` (actual/instantiated content, carrying `memberCount`, `creator`, `subject`/`memberTopics`/`otherTopics`, and `shape` — its member composition is the `OneMember`/`MultiMember`(abstract)/`TwoMember`/`ThreePlusMember` hierarchy, hanging off `ACell` rather than `Cell` directly; renamed from `OneParty`/`MultiParty`/`TwoParty`/`ThreePlusParty` in cell.ttl 3.17.0, alongside `parties`→`memberCount` and `partyTopics`→`memberTopics`). `subject` (an `owl:AnnotationProperty`, range `xsd:anyURI`) identifies the one or two resource(s) — e.g. a `p:Person`/`g:Group`/`o:Organization` — the cell's relationship is about; `memberTopics` (an `owl:ObjectProperty`, range `topic:SCTopicGraph`) links to the required baseline of topic DataBooks backing the cell's content, one or more per member required, cardinality enforced per member count; `otherTopics` (same range) links to any number of additional topics beyond that baseline, optional and unbounded regardless of member count (cell.ttl 3.14.0 split of the former single `topics` property). A cell needing both facets (e.g. a template cell that also carries real member data) is simply multi-typed with both. A `cell:Cell` carries no tree position of its own, and isn't typed `cell:ACell` (so carries none of the above) until it has real content.
- **Category ontology** (`category.ttl`): defines the *classificatory* facet of a category — which kind of thing it is (e.g. `cat:Work`, `cat:Affiliations`; the `Person`/`Organization` hierarchy and all leaf categories) — the canonical tree IS this class hierarchy (`rdfs:subClassOf`), not a separate set of instances. A `cat:Category` subclass with reusable starter content carries `cat:templateCell` (an `owl:AnnotationProperty`) pointing directly at a `cell:Cell` template — mirroring `cell:abstract`'s precedent for asserting metadata directly on a class IRI. The `cat:templateCell` pointer triples for the 4 templated classes are asserted directly in `category.ttl`, right alongside each class's own declaration; the target `cell:Cell` individuals themselves are defined in the companion file `cell-templates.ttl` (which `category.ttl` `owl:imports`). That template cell may in turn carry `cell:templateShape` (an `owl:ObjectProperty`, defined in `cell.ttl` — not `category.ttl`, since its domain/range, `cell:Cell`/`sh:NodeShape`, never actually reference a `cat:` term) to the `sh:NodeShape`(s), in `cell-templates-shacl.ttl`, describing the content expected of a topic file filed under that category — making a class's shape reachable by pure RDF traversal (`cat:Category` → `cat:templateCell` → `cell:templateShape`), not merely by file co-location or naming convention. Because `cell:templateShape` lives in `cell.ttl`, `cell-templates.ttl` only needs to import `cell.ttl` directly, not `category.ttl` — so unlike `topic.ttl`/`cell.ttl`, `category.ttl`/`cell-templates.ttl` is a one-directional import, not mutual. category.ttl 1.31.0 deleted the *tree-position* facet that used to sit alongside this one entirely — `cat:Folder` and its subclasses `cat:CategoryDefined`/`cat:UserDefined`, along with `cat:child`/`cat:cell`/`cat:category`/`cat:catType`/`cat:label` — since none of it had any remaining purpose: a user's own instance-tree position is now purely a filesystem fact (a category is simply the folder its cell-databook physically lives in, with no RDF individual representing the folder at all), and `cell:origin` (cell.ttl 3.20.0) already carries every classification fact `cat:category` used to, as a class value directly on the cell rather than a separate folder individual. `cell.ttl` imports `topic.ttl` (a separate mutual import), but not `category.ttl` — nothing in `cell.ttl` references `cat:` terms except by name in `cell:origin`'s range.

There are no build, compile, test, or lint commands. The files are Turtle (`.ttl`) loaded into semantic web tools (Protégé).

## Core Files

| File | Purpose |
|------|---------|
| `persona.ttl` | Persona ontology — imports domain ontologies, annotates which classes/properties are required vs. optional for Mee, defines Mia-specific classes and properties |
| `topic.ttl` | Topic ontology — controlled vocabularies for classifying topic files (`claimant`, `subject`) and the `Topic` class hierarchy. Mutually imports `cell.ttl` |
| `cell.ttl` | Cell ontology — `cell:Cell` (formerly `cell:Parties`), the content facet of a cell, carrying only what's common regardless of facet: `origin` (added cell.ttl 3.20.0) — range `cat:Category`, at most one value (0..1; absent/nil when the cell's containing folder's own name matches no real `cat:Category` subclass), else the concrete leaf subclass (class-value punning, like `memberCount`) matching the folder's own name, letting a recipient's app use it as a filing hint, referenced by name without `owl:imports category.ttl` (mirroring `creator`'s identical pattern below); resolves `cell.png`'s previously open `origin`-arrow discrepancy (see Check 12) without contradicting `cell:Cell`'s "no link to a tree position" design, since `cat:Category` is the classificatory hierarchy, and category.ttl 1.31.0 deleted the tree-position side (`cat:Folder` and its subclasses) outright — a folder is now purely a filesystem concept with no RDF individual at all. `folder` — which stored a path to a cell's own folder — was removed outright in cell.ttl 3.23.0: a folder holds at most one cell-databook (cell.ttl 3.22.0), so a cell's folder is now always unambiguously wherever its own cell-databook physically lives, with nothing left to store or keep in sync. The folder ownership boundary rule `folder`'s design comment used to document (cell.ttl 3.16.0) survives independently of any property — a subfolder belongs to a different, nested cell rather than this one iff it directly contains a `*.databook.md` file (the only DataBook type in a user's instance tree is now `cell-databook`; cell.ttl 3.19.0 reworded this rule once the separate `category-databook` type it originally keyed on was retired), resolvable one folder at a time with no category-tree traversal and no dependency on any recorded path. cell.ttl 3.15.0 had earlier removed `note`, merging the separate notes/files hierarchies into the single folder hierarchy that `folder` itself pointed at, before `folder`'s own later removal. Splits into two orthogonal facets (cell.ttl 3.7.0): `cell:TCell` (abstract, template facet — carries `templateShape`) and `cell:ACell` (abstract, actual/instantiated facet — carries `memberCount`, `creator`, `subject`/`memberTopics`/`otherTopics` (cell.ttl 3.14.0 split `partyTopics`/`otherTopics` out of a single `topics` property, itself renamed from `primary`/`secondary` in 3.12.0, themselves renamed from `graph`/`sc-context`, and moved here from `cell:Cell`; `partyTopics` itself renamed to `memberTopics` in cell.ttl 3.17.0), and `shape`). The `Cell`/`MultiMember`(abstract)/`OneMember`/`TwoMember`/`ThreePlusMember` member-count hierarchy now hangs off `cell:ACell` rather than `cell:Cell` directly (renamed from `MultiParty`/`OneParty`/`TwoParty`/`ThreePlusParty` in cell.ttl 3.17.0, alongside `parties`→`memberCount`). `memberCount`'s range is `cell:ACell` itself — its value is the concrete subclass (e.g. `cell:OneMember`), not a string, the same class-value-punning pattern `cell:origin` uses for its own range, `cat:Category`. `creator`'s range is a union of `p:Person`/`g:Group`/`o:Organization`, referenced by name without importing those ontologies (mirroring `topic:subject`/`topic:claimant`). `subject` is an `owl:AnnotationProperty` (range `xsd:anyURI`, mirroring `topic:subject`'s identical pattern — not a topic link, but the resource(s) the cell is about) required one or two values, cardinality enforced per member count; `memberTopics` is an `owl:ObjectProperty` (range `topic:SCTopicGraph`) — the required per-member baseline, cardinality enforced per member count by `cell-shacl.ttl`'s per-member shapes; `otherTopics` (same range) is any number of additional topics beyond that baseline, optional and unbounded regardless of member count — the old plain-`topic:TopicGraph`, no-claimant use case `graph` supported remains retired. `templateShape` (domain `cell:TCell`, range `sh:NodeShape`) links a template cell to its SHACL shape(s) describing what a topic filed under its category should look like; moved here from `category.ttl`'s `cat:templateShape` since its domain/range never referenced a `cat:` term. `shape` (domain `cell:ACell`, range `sh:NodeShape`) links an actual cell directly to the shape(s) validating its own content — distinct from `templateShape`. A cell needing both facets (e.g. every individual in `cell-templates.ttl`) is simply multi-typed with both `cell:TCell` and its `cell:ACell`-lineage class. Carries no link back to a folder at all — a folder is purely a filesystem concept with no RDF individual (category.ttl 1.31.0 deleted `cat:Folder` and its subclasses outright); `origin` is the sole remaining record of a cell's matched classification. Mutually imports `topic.ttl` |
| `category.ttl` | Category ontology — `cat:Category` (abstract, classificatory facet: the `Person`/`Organization` hierarchy and all leaf categories, plus `templateCell`). No tree-position facet at all — category.ttl 1.31.0 deleted `cat:Folder` and its subclasses `cat:CategoryDefined`/`cat:UserDefined`, along with `cat:child`/`cat:cell`/`cat:category`/`cat:catType`/`cat:label`, outright: a user's own instance-tree position is now purely a filesystem fact, with `cell:origin` (cell.ttl) the sole remaining RDF-level record of a cell's matched classification. No separate canonical folder class either — the canonical tree is the `cat:Category` class hierarchy itself. Imports `cell.ttl` and `cell-templates.ttl` |
| `cell-templates.ttl` | Class-level `cell:Cell` templates — one individual per templated class (`cat:Passport`, `cat:BirthCertificate`, `cat:DriversLicense`, `cat:MedicalAppointmentInfo`), each pointed at by its class's own `cat:templateCell` value (asserted in `category.ttl`, not here). Each is multi-typed `cell:Cell, cell:TCell, cell:ACell, cell:OneMember` (cell.ttl 3.7.0's facet split), since a template cell is simultaneously the template facet (carrying `cell:templateShape` to its SHACL shape in `cell-templates-shacl.ttl`) and the actual/instantiated facet (carrying `cell:memberCount`). Imports `cell.ttl` directly — no mutual import with `category.ttl` |
| `cell-shacl.ttl` | SHACL validation shapes for `cell:Cell` DataBook instances, split across shapes matching cell.ttl 3.7.0's facet split: `:CellShape` (target `cell:Cell`) — `folder` cardinality (dropped its `note` cardinality check in cell-shacl.ttl 3.13.0, alongside cell.ttl 3.15.0's removal of `cell:note`) and `origin` cardinality (at most one — 0..1, added cell-shacl.ttl 3.15.0 alongside cell.ttl 3.20.0's new `cell:origin` — not constrained via `sh:class cat:Category` since a legal value is the concrete leaf subclass itself, never `rdf:type cat:Category`, mirroring `cell:memberCount`'s own identical unconstrained, class-value-punning treatment above); `:TCellShape` (target `cell:TCell`) — `templateShape` cardinality (at most one; deliberately not constrained to `sh:class sh:NodeShape` since its value is only typed as such in `cell-templates-shacl.ttl`, which Tier 1 excludes from its merged-data run); `:ACellShape` (target `cell:ACell`) — `memberCount` required and constrained to be the class `cell:OneMember`/`cell:TwoMember`/`cell:ThreePlusMember`, `subject` values each constrained via `sh:nodeKind sh:IRI` (not `sh:class`, since its range is `xsd:anyURI` not a topic class; cardinality no longer set here), `otherTopics` values (if any) constrained to be a `topic:SCTopicGraph` (uniformly optional/unbounded regardless of member count), `creator` (if present) constrained to be a `p:Person`, `g:Group`, or `o:Organization`, and `shape` cardinality (at most one, same reasoning as `templateShape`); plus three new per-member shapes (cell.ttl/cell-shacl.ttl 3.14.0/3.12.0, shapes themselves renamed in 3.17.0 alongside their target classes) — `:OneMemberShape`/`:TwoMemberShape`/`:ThreePlusMemberShape` (target `cell:OneMember`/`cell:TwoMember`/`cell:ThreePlusMember` directly) — enforcing `subject` as exactly 1/1..2/exactly 1 and `memberTopics` (each constrained to `topic:SCTopicGraph`) as exactly 1/2..4/at least 3 respectively, replacing the old single `topics` property's uniform "at least one, no upper bound" rule |
| `persona-shacl.ttl` | SHACL validation shapes — constraint rules for all `persona:Person` instances (SSN format, address cardinality, payment cards, wallet, social network, etc.) |
| `topic-shacl.ttl` | SHACL validation shapes for topic DataBook instances — `:SCTopicGraphShape` (`topic:SCTopicGraph`'s `subject`/`claimant`; `claimant` required exactly once and constrained to a `p:Person`/`g:Group`/`o:Organization`, `subject` required exactly once and constrained to be an IRI — topic.ttl 1.13.0 broadened `subject`'s range to `xsd:anyURI`, so a topic's subject need not be a person's identity); split out of `persona-shacl.ttl` since it validates a `topic.ttl` class, not `persona:Person`. A topic DataBook does not carry `cell:creator` (or any creator property) — that stays a `cell:Cell`-only property |
| `persona-templates.ttl` | Persona template labels — defines `p:PersonaTemplate` (abstract classification superclass) and concrete label subclasses `p:BirthCertificateDocument`, `p:JSContactCard`, `p:DriversLicenseDocument`, `p:PassportDocument`, `p:MedicalAppointmentRecord`; also defines related designator classes (`persona:DriversLicenseNumber`, `persona:IssuingJurisdiction`, `persona:PassportNumber`, `persona:IssuingCountry`, `persona:PlaceOfBirth`, `persona:GenderMarker`, `persona:IssueDate`, `persona:Credential`, `persona:WebURL`, `persona:OrganizationUnit`, `persona:JobTitle`), complex classes (`persona:Anniversary`, `persona:PersonalInfo`), the `p:MedicalAppointmentRecord` claim properties (`persona:forPatient`, `persona:hasPrimaryCarePhysician`, `persona:currentMedication`, `persona:allergy`, `persona:medicalHistoryNote`, `persona:insuranceProvider`, `persona:insurancePolicyNumber`, `persona:insuranceGroupNumber`, `persona:preferredPharmacy`), and other properties (`persona:hasAnniversary`, `persona:hasPhoto`, etc.) |
| `cell-templates-shacl.ttl` | Per-template SHACL shapes for birth certificate, driver's license, passport, and medical appointment topic files — `:BirthCertificateDocumentShape`, `:DriversLicenseDocumentShape`, `:PassportDocumentShape`, `:MedicalAppointmentRecordShape` — each directly linked from its `cell-templates.ttl` template cell via `cell:templateShape`; run against the individual topic file, not merged data |
| `shacl/jscontactcard-shacl.ttl` | Per-template SHACL shapes for JSContactCard topic files — run against the individual topic file, not merged data (JSContactCard is reused across many unrelated tree positions with no single `cat:Category` class of its own, so its shape stays standalone) |
| `yaml-to-rdf.py` | Synthesizes `cell:`/`topic:` triples from each cell-databook's `mia.` YAML frontmatter (including its embedded `mia.topics` list), used as Tier 1 validation Step 1b (see README.md's Validation section) — `databook extract` only pulls fenced Turtle blocks, which cell-databooks mostly don't carry, so without this script `cell:Cell` individuals and `topic:SCTopicGraph`'s subject/claimant never reach the merged validation graph. No category-side synthesis at all — a folder's tree position is purely a filesystem fact with no RDF individual to synthesize |
| `project_files/` | Reference materials: imported domain ontologies (PersonOntology.ttl, AddressOntology.ttl, StagingOntology.ttl), BFO/CCO source files, PDFs, docs |

## Example Files

Every topic below is now an embedded section (`mia.topics` entry + `### Topic NN` body) inside its owning cell-databook file under `example/Cells/` — there are no more standalone topic files (see [Topic ID Naming Convention](#topic-id-naming-convention)).

| Topic — File | Purpose |
|------|---------|
| Topic 06 — `example/Cells/Work/Acme/Employees/Paula Walker/Paula Walker(employee).databook.md` | Paula Walker as Alice's Acme colleague — claimed by Alice |
| Topic 07 — `example/Cells/People/Immediate Family/Paula Walker/Paula Walker(immediate-family).databook.md` | Paula Walker as Alice's family member — claimed by Alice |
| Topic 05 — `example/Cells/People/Immediate Family/Paula Walker/Paula Walker(immediate-family).databook.md` | Paula Walker's own family persona; social network with Alice |
| Topic 08 — `example/Cells/People/Others/Bob Johnson/Bob Johnson(others).databook.md` | Alice Walker as seen by Bob Johnson — claimed by Bob |
| Topic 04 — `example/Cells/People/Others/Bob Johnson/Bob Johnson(others).databook.md` | Alice's notes about Bob Johnson; favorite drink: oat milk cappuccino |
| Topic 02 — `example/Cells/People/Others/Bob Johnson/Bob Johnson(others).databook.md` | Bob Johnson's self-claimed persona; social network with Alice |
| Topic 14 — `example/Cells/Affiliations/Boston Hub Society/Boston Hub Society(affiliations).databook.md` | Alice's Boston Hub Society profile — email, phone, and current address |
| Topic 01 — `example/Cells/Affiliations/Boston Hub Society/Boston Hub Society(affiliations).databook.md` | BHS Group — g:Group instance with Alice and Bob as members |
| Topic 03 — `example/Cells/Affiliations/Boston Hub Society/Boston Hub Society(affiliations).databook.md` | Bob Johnson's BHS member persona — name, email, phone, address |
| Topic 09 — `example/Cells/Finances/Banking & Payments/Citibank/Citibank(banking-payments).databook.md` | Alice's Citibank topic — debit card; claimed by Citibank |
| Topic 16 — `example/Cells/Companies/Google/Google(companies).databook.md` | Alice's Google topic — Gmail address |
| Topic 11 — `example/Cells/Companies/ATT/ATT(companies).databook.md` | Alice's AT&T topic — phone number |
| Topic 24 — `example/Cells/Government/State/Texas Vital Records/Texas Vital Records(birth-certificate).databook.md` | Alice's Texas birth certificate — legal names, maiden name |
| Topic 18 — `example/Cells/Government/Municipality/Paradise/Paradise(residence).databook.md` | Alice's Paradise, CA address — current residence (2025–present) |
| Topic 13 — `example/Cells/Government/Municipality/Boston/Boston(residence).databook.md` | Alice's Boston, MA address — previous residence (2020–2025) |
| Topic 23 — `example/Cells/Government/Federal/Social Security Administration/Social Security Administration(ssa).databook.md` | Alice's Social Security Number |
| Topic 12 — `example/Cells/People/Others/Bob Johnson/Bob Johnson(others).databook.md` | Alice's 1:1 topic with Bob; social network with Bob as member |
| Topic 21 — `example/Cells/People/Immediate Family/Paula Walker/Paula Walker(immediate-family).databook.md` | Alice's family topic — social network with Paula Walker as member |
| Topic 22 — `example/Cells/Ownership/Ownership.databook.md` | Alice's possessions — wallet, health insurance card, SSN card |
| Topic 20 — `example/Cells/Work/Acme/Employees/Paula Walker/Paula Walker(employee).databook.md` | Alice's Acme employee topic; social network with Paula Walker |
| Topic 10 — `example/Cells/Work/Acme/Employees/Alice Walker/Alice Walker(employee).databook.md` | Alice's business card (JSContactCard) — name, email, phone, employer, job title |
| Topic 15 — `example/Cells/Government/State/California DMV/California DMV(drivers-license).databook.md` | Alice's California driver's license — legal name, DOB, DL#, expiry, photo |
| Topic 19 — `example/Cells/Government/Federal/Passport/Passport.databook.md` | Alice's US passport — legal name, DOB, passport#, issue/expiry, place of birth, gender marker, photo |
| Topic 17 — `example/Cells/People/Immediate Family/Paula Walker/Health & Wellness/Health & Wellness.databook.md` | Paula's physical characteristics — height, eye color, hair color — as recorded by Alice |
| `example/topics/under-development/paula(fl-birth-cert)alice.ttl` | Paula Walker's Florida Birth Certificate Persona — legal name record (under development) |
| `example/topics/self.ttl` | `:Self`'s sole type declaration (`rdf:type owl:NamedIndividual, persona:Person`); not `owl:imports`ed anywhere, merged in only for validation |

## Architecture

### Three-Layer Design

```
Triplestore (Fuseki) — loads all DataBook files directly:
  ├─ persona.ttl              (application profile — imports domain ontologies)
  │   ├─ PersonOntology.ttl
  │   ├─ AddressOntology.ttl
  │   └─ StagingOntology.ttl → BFO terms
  ├─ example/Cells/Work/Acme/Employees/Paula Walker/Paula Walker(employee).databook.md      (embeds topics 06, 20)
  ├─ example/Cells/People/Immediate Family/Paula Walker/Paula Walker(immediate-family).databook.md  (embeds topics 05, 07, 21)
  ├─ … (all other cell-databooks, each embedding one or more numbered topics via mia.topics)
  ├─ example/Cells/People/Immediate Family/Paula Walker/Health & Wellness/Health & Wellness.databook.md  (embeds topic 17)
  └─ example/topics/self.ttl        (:Self's bare type declaration — merged in for validation, never owl:imports'd)

persona-shacl.ttl — no owl:imports of data; validated against the loaded dataset
shacl/jscontactcard-shacl.ttl — per-template shapes for JSContactCard files (only template with no cat:Category class of its own)
cell-templates-shacl.ttl — per-template shapes for birth certificate, driver's license, passport, and medical appointment files
```

1. **Foundation**: BFO (Basic Formal Ontology) — provides temporal modeling (`TemporalInterval`) and core relations
2. **Domain Ontologies** (in `project_files/`): PersonOntology, AddressOntology, StagingOntology
3. **Application Ontologies** (peer, not nested):
   - `persona.ttl`: aggregates domain ontologies; uses annotation properties (`usesRequiredClass`, `usesOptionalClass`, `usesCCOClass`, `usesCCOProperty`) to document Mee's usage
   - `topic.ttl`: defines `claimant` and `subject` vocabularies; imported directly by each topic file
   - `cell.ttl`: defines `cell:Cell`, the content facet of a cell (topic links common to all cells), split into `cell:TCell` (template facet) and `cell:ACell` (actual facet, carrying member composition); mutually imports `topic.ttl`
   - `category.ttl`: defines `cat:Category` (classificatory facet only: `templateCell`) — no tree-position facet at all, since category.ttl 1.31.0 deleted `cat:Folder` and its subclasses outright; a folder is now purely a filesystem concept with no RDF individual, and `cell:origin` (cell.ttl) is the sole remaining RDF-level record of a cell's matched classification; no separate canonical folder class either — the canonical tree is the class hierarchy itself; imports `cell.ttl` and `cell-templates.ttl`

### Category/Cell DataBook Filename Convention

Cell-databook filenames follow (there is no separate category-databook file any more — a folder's sole DataBook is its cell-databook, see [Key Architectural Patterns](#key-architectural-patterns)'s Cell/Category split note):

```
<local>(<catType>).databook.md  — cell-databook
```

`<local>` is an **exact copy of the folder's own name** — verbatim, no kebab-casing, no lowercasing, whatever case/spacing/punctuation the folder itself has (e.g. `Acme`, `Paula Walker`, `ATT`). There is no more `-cell` token: cell-databook is the sole DataBook type in a user's instance tree, so nothing needs to be disambiguated by it. There is also no numeric disambiguator of any kind (no `-2`, `-N`, etc.): a folder holds **at most one** cell-databook, ever — a folder counts as a category folder only when it holds exactly one such matching file, and a folder with no matching cell-databook is simply a plain filesystem folder, not a category folder at all (see [Cell/Category split](#key-architectural-patterns) below for why two cells can never share one folder). `<catType>` is the folder's own category classification, kebab-cased as before (e.g. `Employee` → `employee`, `ImmediateFamily` → `immediate-family`, `SSA` → `ssa` — kebab-casing is acronym-aware: a hyphen is inserted only at a lowercase→uppercase boundary or an uppercase-run→lowercase boundary, so consecutive capitals stay together). If the matched `cat:Category` class's own local name carries a literal `(org)` disambiguator (used only to distinguish it from a same-named Person-side sibling class, e.g. `cat:BankingPayments` vs. `cat:BankingPayments(org)`), that suffix is dropped before kebab-casing — `<catType>` only ever needs to disambiguate a *recurring folder name* by role (e.g. Paula Walker's `Employee` folder vs. her `ImmediateFamily` folder, both Person-side), never the Person/Organization split itself, which is already carried by the folder's own tree position and by `cell:origin`'s actual asserted value, never by the filename. So Citibank's cell — `cell:origin: cat:BankingPayments` (Person-side, since it's the person's own relationship with the bank, not company business filed under `Work`) — is `Citibank(banking-payments).databook.md` with no `-org` marker, and the same bare `banking-payments` `<catType>` would apply identically if a cell's `cell:origin` were instead the org-side `cat:BankingPayments(org)`, since nothing in the filename needs to tell the two apart. A cell-databook's `<catType>` parenthetical is purely a filename-level disambiguator now — category.ttl 1.31.0 deleted `cat:catType` outright (it was only ever asserted on a now-vanished `cat:Folder` individual), so nothing in RDF records it, and nothing reverse-matches the filename to derive it. The one RDF-level echo of a folder's classification is `cell:origin`, read directly from the cell-databook's own explicit `mia.origin` YAML field, not derived from the filename at all. The `id:` local name matches the filename root **once every space is replaced with a hyphen** — spaces are illegal inside a raw Turtle IRI, so e.g. filename `Paula Walker(employee).databook.md` has `id:` local name `Paula-Walker(employee)`; every other character (case, `&`, `.`, etc.) passes through unchanged (Check 9).

**Compression rule**: if `<local>`, normalized the same acronym-aware way `<catType>` already is, is identical to the kebab-cased `<catType>`, the parenthetical is dropped entirely, since it's pure redundancy — `<local>.databook.md` — rather than `<local>(<local>).databook.md`. For example `cat:Work`'s folder is named `Work`, and its own `catType` (`Work`) also kebab-cases to `work` — the same string — so its file is `Work.databook.md`, not `Work(work).databook.md`. This applies on a normalized-equal match, not raw string identity (since `<local>` is no longer pre-kebab-cased): folder `Health & Wellness`'s catType `HealthWellness` both normalize to `health-wellness`, so it compresses too, to `Health & Wellness.databook.md`. `Acme(organization).databook.md` keeps its parenthetical since normalized `Acme` (`acme`) ≠ `organization`. Most of the top-level tree scaffold compresses this way (`Work`, `People`, `Others`, `Companies`, `Finances`, `Government`, `State`, `Municipality`, `Federal`, `Ownership`, `Affiliations`, `Employees`, `Immediate Family`, `Health & Wellness`, `Medical`, `Banking & Payments`), since these folders' own name simply *is* their category (there's no more-specific person/organization/thing filed there directly — that's one level further down, e.g. `Boston Hub Society(affiliations)` or `Acme(organization)`, which don't compress). The same rule applies identically to a topic's `(<containing-cell>)` segment (see [Topic ID Naming Convention](#topic-id-naming-convention) below), since that segment is always derived directly from the (possibly-compressed) cell filename's `id:` form (space-hyphenated, not the raw filename — topic ids are IRIs too).

This replaced an earlier convention that disambiguated using the folder's *parent's* local name instead (e.g. `Acme(Work).databook.md`) — redundant with the folder position that already encodes it, and inconsistently chosen in practice. Folder naming is now standardized as the category's own display label (the OS folder name is used verbatim, with no override field anywhere), but a folder's own name still can't disambiguate a repeated name's *role* — e.g. Paula Walker's Immediate Family folder vs. her Acme Employee folder are both literally named "Paula Walker" — so `catType` still needs its own encoding in the filename, not derived from folder position. Using the folder's own `catType` instead has a useful side effect: it's exactly what disambiguates a name that legitimately recurs in two different roles — e.g. Paula Walker is both her own Immediate Family folder (`catType: ImmediateFamily` → `Paula Walker(immediate-family).databook.md`) and her Acme employee record (`catType: Employee` → `Paula Walker(employee).databook.md`); the same folder name, but never colliding, since a repeated name always means a *different* role and therefore a different `catType`.

### Topic ID Naming Convention

**Historical note**: this convention originally governed topic *filenames*. Topic content was later merged into its owning cell-databook's `mia.topics` list and body (see [Key Architectural Patterns](#key-architectural-patterns)'s Cell/Category split note) — a topic no longer has a file or filename of its own. This convention now governs only the string shape of each `mia.topics[].id` value (which doubles as the topic's own named-graph identity, `{id}#graph` — unchanged by the merge), not any file on disk. A topic's id local-name follows a single flat pattern:

```
<subject>.<claimant>(<containing-cell>)(<NN>)
```

| Segment | Meaning |
|---------|---------|
| `<subject>` | The entity the Persona is about. Use `self` when the subject is the Mia user's own `p:Person` (`:Self`); otherwise use the full hyphenated lowercase name (e.g. `paula-walker`, `bob-johnson`, `bhs-group`). (In the ontology, `topic:subject`'s range is any resource IRI — every subject value in this example happens to be a `p:Person`/`g:Group`/`o:Organization`, but that's a convention of the example, not an ontology requirement.) |
| `<claimant>` | Who claimed the data. Use `self` when the claimant is `:Self`; use the full hyphenated lowercase name for other claimants (e.g. `bob-johnson`, `citibank`); use the literal `members` for `cell:ThreePlusMember` topics where any permitted member may write. |
| `(<containing-cell>)` | The readable local name of the cell-databook this `mia.topics` entry lives inside — i.e., the folder (category) that cell-databook physically lives in, since a folder's tree position is purely a filesystem fact with no RDF individual of its own (category.ttl 1.31.0 deleted `cat:Folder` and its subclasses outright). Ordinarily this is two parenthetical segments — the category's local name, then its own `catType` (kebab-cased) — but per the [Category/Cell DataBook Filename Convention](#categorycell-databook-filename-convention) below's compression rule, when the cell's own local name is identical to its `catType` kebab-cased, the cell's filename (and so this segment) collapses to a single bare parenthetical instead of the doubled-up form. Two-segment examples: `(Bob-Johnson)(others)`, `(Boston-Hub-Society)(affiliations)`, `(Paula-Walker)(immediate-family)`, `(Citibank)(banking-payments)`, `(Paula-Walker)(employee)` (Paula's *Acme employee* cell — same local name as her Immediate Family cell above, disambiguated only by the differing `catType`). Compressed, single-segment examples: `(Ownership)` (topic #22 — a top-level category whose local name and `catType` happen to coincide), `(Passport)` (topic #19), `(Health-&-Wellness)` (topic #17). |
| `(<NN>)` | Zero-padded two-digit topic number in parentheses, matching the diagram label. |

**Exception — `cell:ThreePlusMember` topics**: A group topic (`memberCount: ThreePlusMember`) has no single claimant — any permitted member can write to it and changes replicate to all members. The `<claimant>` segment is the literal `members` rather than an individual name. Example id local-name: `bhs-group.members(Boston-Hub-Society)(affiliations)(01)` — about BHS Group, containing cell "Boston-Hub-Society(affiliations)", claimed by the group's members collectively.

**`claimant` vocabulary** (a `mia.topics[]` entry's own field): takes the local IRI of a `p:Person`, `g:Group`, or `o:Organization` individual — NOT an `i:PDNidentifier`. Specifically: `:Self` (the Mia user's `p:Person`) for self-claimed topics; a named `p:Person` individual (e.g. `:Bob_Johnson`) when another Mia user claims the data; a named `g:Group` individual (e.g. `:BHS_Group`) for group topics; and a named `o:Organization` individual (e.g. `:Citibank`) only when the claiming organization is itself PDN-interoperable. In the example data **only Citibank is treated as PDN-interoperable**, so only the topic embedded in `Citibank(banking-payments).databook.md` with id local-name `self.citibank(Citibank)(banking-payments)(09)` uses `claimant: ":Citibank"`. All other organization-related topics (Google, AT&T, SSA, etc.) use `claimant: ":Self"` because Alice self-enters that data — those organizations aren't PDN-interoperable. (This distinction is currently just a data-modeling convention in the example, not formally enforced by any property — `identity:hasPDNidentifier`, which would have modeled it, was removed as unused; see pdn-identity.ttl 1.3.0.)

**"Other" claimants**: When the claimant is someone other than the current Mia user (`:Self`), the claimant is a named individual of one of:
- `p:Person` — another Mia user (a different person, e.g. `:Bob_Johnson` claiming data about Alice)
- `o:Organization` — a company, nonprofit, or government agency that is a PDN node (e.g. `:Citibank`)
- `g:Group` — a group of Mia users (e.g. `:BHS_Group`)

**Examples** (id local-name; the owning cell-databook file is found via [Check 3](#integrity-checks)):

| Id local-name | Subject | Claimed by | Containing cell |
|----------|---------|-------------|---------------------|
| `self.citibank(Citibank)(banking-payments)(09)` | Self (Alice) | Citibank | Citibank(banking-payments) |
| `paula-walker.self(Paula-Walker)(immediate-family)(07)` | Paula Walker | Self (Alice) | Paula-Walker(immediate-family) |
| `self.bob-johnson(Bob-Johnson)(others)(08)` | Self (Alice) | Bob Johnson | Bob-Johnson(others) |
| `bob-johnson.bob-johnson(Boston-Hub-Society)(affiliations)(03)` | Bob Johnson | Bob Johnson | Boston-Hub-Society(affiliations) |
| `bhs-group.members(Boston-Hub-Society)(affiliations)(01)` | BHS Group | members (group) | Boston-Hub-Society(affiliations) |

### Key Architectural Patterns

**All data belongs to topics**: There is no separate selfness file holding a Mia user's identity data. Every piece of identity data — names, identifiers, addresses, payment cards, physical characteristics — belongs to a topic-specific Persona file, asserted directly on the shared `:Self` individual. The one exception is `:Self`'s bare type declaration (`:Self rdf:type owl:NamedIndividual, persona:Person`), which lives once in `example/topics/self.ttl` instead of being repeated with an `rdfs:label` in every topic file as it once was; `self.ttl` carries no other claims about `:Self` and is never `owl:imports`ed — it is merged in alongside the topic files only when validating (see the Tier 1/Tier 2 commands in README.md's Validation section). Every substantive fact about a Mia user still lives exactly where it always has: in the topic file(s) it belongs to.

**`:Self` IRI convention**: The Mia user's own `persona:Person` individual always uses the IRI `:Self` across all of their topic files. All other people, groups, and organizations are assigned locally-minted named IRIs (e.g. `:Bob_Johnson`, `:Paula_Walker`, `:BHS`). `:Self` is a local IRI and is never exposed externally over the PDN, so there are no collisions between Mia instances. All topic files in the example live in Alice's Mia — some authored by Alice, others received from peers over PDN. In either case, `:Self` refers to Alice. When data arrives from a peer's Mia (where that peer was `:Self` in their own instance), Alice's Mia assigns them a locally-minted identifier; once a PDN connection is established, that identifier resolves to or is replaced by their PDN ID.

**Cell/Category split**: In a user's own instance tree, a category is now purely a filesystem folder — its tree position (nesting, name) is a plain OS fact, with no RDF individual representing it at all (category.ttl 1.31.0 deleted `cat:Folder` and its subclasses `cat:CategoryDefined`/`cat:UserDefined`, along with `cat:child`/`cat:cell`/`cat:category`/`cat:catType`/`cat:label`, outright). A folder's sole DataBook is its `cell-databook` (content: `memberCount`/`subject`/`memberTopics`/`otherTopics`/`folder`/`origin`); there is no sibling `category-databook` file, and never was one in this simplified picture (category.ttl 1.30.0 / cell.ttl 3.19.0 already removed it). The one remaining RDF-level trace of a folder's classification is `cell:origin` (cell.ttl 3.20.0), asserted directly on the cell as a class value (e.g. `cat:Passport`) whenever the folder's own name matches a real `cat:Category` subclass, and absent otherwise — read straight from the cell-databook's own explicit `mia.origin` YAML field, never derived from filename-parsing or folder position. `cell:Cell` carries no link back to a folder at all — `cell.ttl` has no such property, and there is no folder-side property to hold one either any more. **A folder holds at most one cell-databook, never more** — a folder counts as a category folder exactly when it holds one such matching file (its filename an exact copy of the folder's own name), and a folder with none is just a plain filesystem folder, not a category folder at all. Two cells can never share a folder: a `cell:Cell` is self-contained, and letting two cells share a folder would risk a single file in that folder becoming ambiguously part of both. A topic DataBook still carries no field pointing back at its cell at all — the cell is the one that asserts the `memberTopics`/`otherTopics` link, and the topic id's `(<containing-cell>)` segment names the folder (the human-readable position) that cell-databook lives in directly, not via any RDF lookup. This still keeps a cell's content self-contained (aside from the topic files it references) and independent of tree position, for PDN sync robustness: when a cell is shared between peers (e.g. a `TwoMember` cell between Alice and Bob), each peer can independently rearrange their own category tree — moving, renaming, or renesting their category folder however they like — without ever touching the shared cell's content or identity, since moving a folder in the tree is now a pure filesystem operation with no frontmatter field to edit on either side. The *canonical* side of the split (which classes have reusable starter content) lives entirely at the class level — see `category.ttl`'s `cat:templateCell` and the `cell-templates.ttl` file — there is no separate canonical-instance tree (`categories-person/`/`categories-org/` folders, removed in category.ttl 1.8.0).

**DataBook IRI convention**: The document `id:` and `graph.named_graph:` always differ by the `#graph` fragment — `named_graph` is always `{id}#graph`. The `databook:id` on a block is a fragment identifier making that block independently addressable as `{id}#{block-id}`. Overview sections always begin with "This topic captures...".

**Peer name pattern** (not hierarchical): All name types (FullName, GivenName, FamilyName, AlternateName) connect directly to a Persona via `ont00001879` (designated by). They are siblings, not nested. Names belong to Personas not to Persons.

**Address history pattern**: `AddressDesignation` links Person → Address → `TemporalInterval`. Open-ended intervals (no `hasEndDate`) indicate current address.

**Named graph scoping of `BFO_0000115`**: When a Social Network individual carries `BFO_0000115 :Paula_Walker`, the triple is intentionally scoped to the enclosing named graph — it refers to Paula Walker *as a person entity*, with topic-specific isolation provided by the DataBook named graph architecture, not by the triple itself. Queries needing topic-specific member data must target the relevant named graphs (e.g. topic 21 + topic 5) rather than querying the full merged dataset. Do NOT change the range of `BFO_0000115` to a document IRI (breaks BFO semantics — range must be a continuant, not a document), and do NOT introduce topic-specific person individuals (reintroduces the complexity that removing the layered Persona model eliminated). RDF-star annotation is a valid future option if tooling matures.

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

Before committing any change to `persona.ttl`, `topic.ttl`, `cell.ttl`, `category.ttl`, or `persona-shacl.ttl`, increment the **minor version number** in that file's `owl:versionInfo` annotation and update the description to summarise the change. For example:

```
owl:versionInfo "Version 3.0.3 - added social network"@en
```
becomes:
```
owl:versionInfo "Version 3.0.4 - added birth date"@en
```

## Integrity Checks

Files inside any directory named `under-development/` (at any depth) are works-in-progress and must be **excluded from all integrity checks** below.

After any change to a topic (its `mia.topics` entry or `### Topic NN` body section) or a cell DataBook, verify the following.

**Check 1 — Diagram ↔ files ↔ README coverage**: Every numbered topic circle in any of the 11 cell diagrams (`example/images/`) must have (a) a corresponding embedded topic section — a `mia.topics` entry plus its `### Topic NN` body section — inside a cell-databook file under `example/Cells/`, and (b) a row in one of the tables in the **Alice's Personas and Topics** section of `README.md`. Conversely, every row in those tables must correspond to a numbered circle in a diagram and an embedded topic that actually exists. If a circle exists in a diagram but has no embedded topic or README row, create them to match the diagram.

**Check 2 — Topic id naming convention**: Every `mia.topics[].id` value's local-name (the string after the final `/`) — across all cell-databooks in `example/Cells/` — must follow `<subject>.<claimant>(<containing-cell>)(<NN>)`. `<subject>` must be `self` when the subject is `:Self`, or the full hyphenated lowercase name otherwise. `<claimant>` must be `self` when the claimant is `:Self`, or the full hyphenated lowercase name otherwise — except for `cell:ThreePlusMember` topics, where it must be the literal string `members`. `(<containing-cell>)` encodes the local name of the *owning* cell-databook itself (the file this `mia.topics` entry lives in, minus its trailing `-cell` suffix) — two segments ordinarily, e.g. `(Bob-Johnson)(others)`, or a single compressed segment when the cell's local name and `catType` kebab-case to the same string, e.g. `(Ownership)` (see [Category/Cell DataBook Filename Convention](#categorycell-databook-filename-convention)). `(<NN>)` is the zero-padded two-digit topic number. If an id does not match this pattern, flag it rather than silently renaming — unlike the old topic-filename convention, `mia.topics[].id` also doubles as the topic's own named-graph identity (`{id}#graph`), so changing it is a bigger operation than a file rename ever was.

**Check 3 — `mia.topics` ↔ `memberTopics`/`otherTopics` consistency**: Since a topic now lives physically inside its owning cell-databook file, containment is structural rather than a cross-file reverse lookup — but the two lists that record it independently (`mia.memberTopics`/`mia.otherTopics`, and the newer `mia.topics`) must still agree exactly. For every cell-databook under `example/Cells/`, the set of ids across `mia.memberTopics`+`mia.otherTopics` and the set of `mia.topics[].id` values must be identical — every linked id has a matching `topics` entry supplying its metadata, and every `topics` entry is linked from one of the two lists. Run:

```python
import glob, re, yaml

def frontmatter(path):
    text = open(path, encoding='utf-8').read()
    m = re.match(r'^---\n(.*?)\n---', text, re.DOTALL)
    return yaml.safe_load(m.group(1)) if m else None

errors = 0
for path in sorted(glob.glob('example/Cells/**/*.databook.md', recursive=True)):
    if 'under-development' in path.split('/'):
        continue
    fm = frontmatter(path)
    if not fm or fm.get('type') != 'cell-databook':
        continue
    mia = fm.get('mia', {}) or {}
    linked_ids = set()
    for field in ('memberTopics', 'otherTopics'):
        val = mia.get(field)
        if val:
            linked_ids.update(val if isinstance(val, list) else [val])
    topic_ids = {t['id'] for t in (mia.get('topics') or []) if isinstance(t, dict) and t.get('id')}
    missing = linked_ids - topic_ids
    unlinked = topic_ids - linked_ids
    if missing:
        print(f'{path}: memberTopics/otherTopics reference(s) with no matching mia.topics entry: {sorted(missing)}')
        errors += 1
    if unlinked:
        print(f'{path}: mia.topics entry/entries with no memberTopics/otherTopics link: {sorted(unlinked)}')
        errors += 1
if not errors:
    print('All cell-databooks: mia.topics entries and memberTopics/otherTopics links are in 1:1 correspondence.')
```

If a mismatch appears, add the missing `mia.topics` entry (or `### Topic NN` body section) or the missing `memberTopics`/`otherTopics` reference — whichever side is incomplete.

**Check 4 — No orphan Persons**: Every `persona:Person` individual other than `:Self` must be reachable via `BFO_0000115` (has member part) from a `g:Group` or from a Social Network individual linked to another `persona:Person` via `persona:hasSocialNetwork`. `:Self` is always the root and needs no incoming link. Since topics are now embedded topic sections across every cell-databook under `example/Cells/**` (rather than standalone files in `example/topics/`), this check's scope is the merged Tier 1 data graph, which already spans every embedded topic. **Exception**: a `persona:Person` referenced only via a professional/service-designation property (e.g. `persona:hasPrimaryCarePhysician`) rather than social-network membership is exempt — it represents a service relationship (e.g. a physician), not a social connection, so it has no social network to be reachable from. Example: `:Jane_Kolpakova` (topic #25), Paula Walker's primary care physician.

**Check 5 — Validation command completeness**: The `## Validation` section of `README.md` must document two tiers. Tier 1 uses five steps: (1) a `find example -name "*.databook.md"` loop using `databook extract` to extract turtle content and produce a merged turtle file of all topic data (excluding `under-development/`) — directory-agnostic, so it naturally concatenates every embedded topic within a cell-databook, which is exactly what Tier 1 wants; (1b) `python3 yaml-to-rdf.py` to synthesize `cell:`/`topic:` triples from each cell-databook's own `mia.` YAML frontmatter (including its `mia.topics` list; a topic's `claimant`/`subject` live there, not in a separate topic-databook file) — there is no `cat:` synthesis at all any more, since category.ttl 1.31.0 deleted `cat:Folder` and its subclasses outright and a folder's tree position is now purely a filesystem fact with no RDF individual to synthesize; the only surviving classification fact, `cell:origin`, is read directly from each cell-databook's own explicit `mia.origin` field, no reverse-matching involved. `databook extract` only pulls fenced Turtle blocks, which cell DataBooks don't carry, so without this step `cell:Cell` individuals and `topic:SCTopicGraph`'s subject/claimant never reach the merged graph and `cell-shacl.ttl`/`topic-shacl.ttl`'s `:SCTopicGraphShape` never fire against real instance data; (2) a `riot` merge of both extracted files with all application ontology TTL files and the foundation ontologies listed explicitly from `project_files/` — `cell-templates.ttl` is deliberately excluded from this merge (unlike Tier 2's per-file base merge, below): its 4 template individuals are generic, reusable content bound to no real person, so they can't sensibly carry `cell-shacl.ttl`'s required `cell:subject`/`cell:memberTopics`, and are instead validated only via `cell-templates-shacl.ttl` in Tier 2; (3) a `grep -v owl:imports` on `persona-shacl.ttl`, `topic-shacl.ttl`, `cell-shacl.ttl`, `group-shacl.ttl`, and `organization-shacl.ttl` to collect shapes (`shacl/jscontactcard-shacl.ttl` and `cell-templates-shacl.ttl` are excluded here — they target document classes and would fire incorrectly on all individuals when applied to merged data; `pdn-identity-shacl.ttl` is also excluded — its ontology, `pdn-identity.ttl`, isn't part of the Step 2 merge, since nothing in the active ontology stack references an `identity:` term any more); (4) a `shacl validate` call. Tier 2 lists explicit per-topic `extract-topic.py` + `riot` + `shacl validate` commands for each template topic paired with its owning cell-databook file and its shapes source — `cell-templates-shacl.ttl` directly for BirthCertificate/DriversLicense/Passport/MedicalAppointment, or `shacl/jscontactcard-shacl.ttl` directly for JSContactCard (both are plain `.ttl` files, not DataBook fragments). `extract-topic.py` (not `databook extract`) is required here because a cell-databook may embed more than one topic — e.g. the MedicalAppointment case lives in a three-topic cell, so a whole-file extraction would wrongly pull in its two sibling topics' data. Tier 2 does not need `yaml-to-rdf.py` since it validates one topic's isolated Turtle directly, not category/cell YAML frontmatter. If the commands change, update the README to match.

**Check 6 — PNG file location**: The diagram PNG for every embedded topic (each `mia.topics` entry across every cell-databook under `example/Cells/`) must be stored directly in `example/topics/images/` (flat, no subfolders — not `images/example/`) — this location is unchanged by the topic/cell merge; only the topics' own `.databook.md` files were removed, not this images directory. Files in `under-development/` are excluded.

**Check 7 — PNG filename convention**: Every diagram PNG in `example/topics/images/` must use the same base filename as the topic's own `mia.topics[].id` local-name (the string after the final `/`), with `.png` appended. For example, id local-name `self.self(Boston-Hub-Society)(affiliations)(14)` → `self.self(Boston-Hub-Society)(affiliations)(14).png`. If the PNG does not yet exist, the README Diagram cell must be marked `*(todo)*` rather than left blank.

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

**Check 9 — Cell/Category filename ↔ id consistency**: This check applies only to `example/Cells/` — the user's own instance tree — since there is no longer a separate canonical-instance file tree (`categories-person/`/`categories-org/` were removed in category.ttl 1.8.0; the canonical tree is now the `cat:Category` class hierarchy in `category.ttl` itself, with class-level templates in `cell-templates.ttl`). Each category folder holds exactly one `cell-databook` DataBook directly inside it — never more than one, since a cell is self-contained and two cells sharing a folder would risk a file becoming ambiguously part of both; a folder with no such matching file is not a category folder at all (see [Key Architectural Patterns](#key-architectural-patterns)'s Cell/Category split note). So this check validates every cell-databook file individually: for every `*.databook.md` in `example/Cells/` (the only DataBook type there is now cell-databook, so no `-cell` marker is needed to identify them), the filename root (the filename with `.databook.md` stripped) — the folder's own name verbatim, no kebab-casing or lowercasing (per the Category/Cell DataBook Filename Convention) — must match the local name portion of the file's `id:` IRI (the string after the IRI base, `http://www.example.org/mia/categories/`) **once every space in the filename root is replaced with a hyphen** — spaces are illegal inside a raw Turtle IRI, so the `id:` value hyphenates them while every other character (case, `&`, `.`, etc.) passes through unchanged. `example/Cells/` is nested into folders mirroring its category tree (see Check 11), so it must be walked recursively. Run:

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
    ('example/Cells', 'http://www.example.org/mia/categories/', True),
]
for directory, base, recursive in checks:
    for path, fname in iter_databooks(directory, recursive):
        root = fname[:-len('.databook.md')]
        expected_local = root.replace(' ', '-')
        text = open(path).read()
        m = re.search(r'^id:\s*(\S+)', text, re.MULTILINE)
        fid = m.group(1).strip() if m else ''
        local = fid[len(base):] if fid.startswith(base) else None
        if local != expected_local:
            print(f'MISMATCH  {path}  root={root!r}  expected_id_local={expected_local!r}  actual_id_local={local!r}')
```

If a mismatch is found, rename the file so its root (once space-hyphenated) matches the id local name (preferred) or update the `id:` to match the filename — whichever is consistent with the broader naming conventions. A category folder's cell-databook is, by construction, whatever single `*.databook.md` file sits directly in that folder — there is no separate `mia.cell` field to cross-check against any more.

Note: this check's `^id:\s*(\S+)` regex is anchored at true line-start with no leading whitespace, so it only ever matches a file's own top-level `id:` line — a nested, indented `mia.topics[].id` value never matches this anchor and is intentionally out of scope here (a topic's `id` is not expected to relate to its owning cell file's name at all; see Check 2 for that). This imposes a requirement on any script that writes `mia.topics`: never emit an unindented `id:` at column 0.

**Check 10 — Example cell diagrams are authoritative**: The 11 cell diagrams in `example/images/` are the authoritative source of truth for the example cell tree. When any discrepancy is found between a diagram and the DataBook files, the diagram wins — update the DataBooks to match, not the other way around. Each diagram box now corresponds to a category folder in `example/Cells/` (tree position, box label = the folder's own name, mirrored in its cell-databook's `title:`) holding its one `cell-databook` (content) directly inside it. After any change to `example/Cells/` DataBooks or to the 11 diagrams, verify all of the following:

- **10a — Every cell box has a category DataBook**: Every cell box (blue/tan canonical or white user-defined) shown in any of the 11 diagrams must have a corresponding folder in `example/Cells/` whose cell-databook's `title:` matches the box label. If a box has no DataBook, create the category folder and its cell DataBook.

- **10b — Every category DataBook has a diagram box**: Every category folder's cell-databook in `example/Cells/` (except the top-level `example/Cells/` folder's own cell-databook, `Cells(person).databook.md`, which is the invisible root) must appear as a visible box in at least one of the 11 diagrams. If a DataBook has no corresponding box, either add it to the appropriate diagram or delete the category folder's cell DataBook.

- **10c — Solid topic circles match DataBook links**: Every solid (filled) topic circle attached to a cell box indicates a real topic link. The cell-databook co-located in that box's own folder must carry a corresponding `memberTopics` or `otherTopics` value pointing to the topic DataBook IRI. A dashed (empty) circle indicates an unfilled slot — the cell DataBook must NOT have a link for that slot.

- **10d — Numbered topic circles have matching embedded topics**: Every numbered topic circle (e.g. `[10]`, `[17]`) shown in a diagram must correspond to a `mia.topics` entry (equivalently, a `### Topic NN` body section) in some cell-databook under `example/Cells/` whose id contains that number (e.g. `(10)`, `(17)`).

- **10e — Child arrows match folder nesting**: Every downward child arrow from cell box A to cell box B in a diagram must correspond to B's folder being a direct filesystem subfolder of A's folder (both folders containing their own cell-databook file) — child links are now derived purely from folder nesting, not any `child:` YAML field. Conversely, every direct-subfolder relationship between two category folders (each holding its own cell-databook) must be reflected by a visible child arrow in the diagram.

- **10f — Cell box border style matches `mia.memberCount`**: Per the Key legend, a cell box is drawn with one of three border styles — a single border ("Single-Member Cell"), a double border ("Two-Member Cell"), or a bold/double border ("Multi-Member Cell") — corresponding to `cell:OneMember`, `cell:TwoMember`, and `cell:ThreePlusMember` respectively (these display strings are `cell:label` values, updated in cell.ttl 3.17.0 from "Cell"/"Two-Party Cell"/"Multi-Party Cell" to match the redrawn diagrams). The border style shown for a cell box must match the actual `mia.memberCount` value of the cell-databook co-located in that box's own folder. This is a visual check (no script) — e.g. `people2.png`'s "Dr. Jane" box is drawn with a single border ("Single-Member Cell"), which must match `Jane-Kolpakova(primary-care-physician).databook.md`'s `mia.memberCount: "cell:OneMember"`.

- **10g — Blue "Subject" annotation matches `cell:subject`**: Per the Key legend's "Subject" entry, a cell box carries a blue "Subject" text annotation listing the name(s) of the resource(s) the cell's relationship is about, comma-separated when there are two. This text must list exactly the same value(s) — by name, not IRI — as the actual `mia.subject` value(s) of the cell-databook co-located in that box's own folder, no more and no fewer. This is a visual check (no script) — e.g. `finances.png`'s "Banking & Payments / Citibank" box's Subject annotation reads "Self, Citibank", matching `Citibank(banking-payments).databook.md`'s `mia.subject: [":Self", ":Citibank"]`.

The 11 diagrams are: `example/images/people.png`, `example/images/people2.png`, `example/images/health.png`, `example/images/work.png`, `example/images/companies.png`, `example/images/finances.png`, `example/images/gov-state.png`, `example/images/gov-federal.png`, `example/images/gov-municipality.png`, `example/images/misc.png`, `example/images/affiliations.png`.

**Check 11 — Physical folder structure IS the category tree in `example/Cells/`**: This check applies only to `example/Cells/` — the user's own instance tree — since there is no longer a separate canonical-instance file tree to mirror (`categories-person/`/`categories-org/` were removed in category.ttl 1.8.0). There is no longer a `mia.child`/`mia.cell` YAML list to cross-check the tree against either — category.ttl 1.31.0 deleted `cat:child`/`cat:cell` (and `cat:Folder` itself) outright, so this check has no independently-asserted list to "mirror" at all; it collapses to a pure filesystem sanity check with no YAML frontmatter parsing at all. A folder counts as a category-tree node ("marker dir") iff it directly contains exactly one `*.databook.md` file (the only DataBook type in a user's instance tree is now cell-databook, so no `-cell` marker is needed to identify one) — that file is simultaneously the folder's real (or placeholder) content and its tree-node marker (cell.ttl's folder ownership boundary rule, 3.16.0/3.19.0). A folder can never legally hold more than one cell-databook (cell.ttl 3.22.0): a `cell:Cell` is self-contained, and letting two cells share a folder would risk a single file in that folder becoming ambiguously part of both — this check flags any such folder as an error. Folder naming is not standardized — it may be the category's display label, a role-based label, or anything else — but a cell-databook's own filename is now always the folder's exact verbatim name (see the Category/Cell DataBook Filename Convention), so this check's per-folder marker test and its filename root are one and the same string. No bare, marker-less pass-through directories are permitted between two marker dirs. Run:

```python
import os

def check_tree(root):
    marker_dirs = set()
    cell_counts = {}
    for dirpath, _, filenames in os.walk(root):
        cells = [f for f in filenames if f.endswith('.databook.md')]
        if cells:
            rel = os.path.relpath(dirpath, root)
            marker_dirs.add(rel)
            cell_counts[rel] = cells

    def parent_of(reldir):
        if reldir == '.':
            return None
        p = os.path.dirname(reldir)
        return p if p != '' else '.'

    errors = []

    # 1. Every marker dir's full ancestor chain back to root must also be
    #    marker dirs — no skip-level (bare, marker-less) nesting allowed.
    for d in sorted(marker_dirs):
        cur = parent_of(d)
        while cur is not None:
            if cur not in marker_dirs:
                errors.append(f'SKIP-LEVEL NESTING: {d!r} has non-marker ancestor {cur!r} (missing its own cell-databook)')
                break
            cur = parent_of(cur)

    # 2. Any subfolder with no cell-databook anywhere under it at all is
    #    either an empty/placeholder folder (flag, don't delete) or plain
    #    non-category content living inside a cell's own folder (fine,
    #    not an error) — only flag when it's otherwise empty.
    for dirpath, dirnames, filenames in os.walk(root):
        rel = os.path.relpath(dirpath, root)
        for entry in sorted(dirnames):
            full = os.path.join(dirpath, entry)
            sub_rel = os.path.join(rel, entry) if rel != '.' else entry
            if sub_rel not in marker_dirs and not any(
                fn.endswith('.databook.md') for _, _, fns in os.walk(full) for fn in fns
            ):
                errors.append(f'EMPTY/PLACEHOLDER FOLDER (no databook.md anywhere under it): {sub_rel!r} under {rel!r}')

    # 3. A category folder holds exactly one cell-databook — a cell is
    #    self-contained, so more than one sharing a folder is always an
    #    error (it risks a single file ambiguously belonging to both).
    for d, cells in sorted(cell_counts.items()):
        if len(cells) > 1:
            errors.append(f'TOO MANY CELLS: {d!r} has {len(cells)} cell-databooks (expected exactly 1): {sorted(cells)}')

    return errors

for root in ['example/Cells']:
    errors = check_tree(root)
    print(f'{root}: ' + (f'{len(errors)} issue(s) found:' if errors else 'OK — folder structure IS the category tree, no gaps.'))
    for e in errors:
        print(' -', e)
```

If a `SKIP-LEVEL NESTING` issue is found, give the intervening folder its own cell-databook. If a `TOO MANY CELLS` issue is found, move the extra file(s) out to their own new folder — a category folder may hold only one cell-databook, so a second cell belongs in its own new folder, not alongside the first. An empty/placeholder folder is not necessarily an error — flag it to the user rather than deleting it, since it may be a deliberate placeholder for content not yet added. Cell-databook files now routinely carry substantial body content (one `### Topic NN` section per embedded topic) — this is expected and not itself a violation of this check, which only validates folder nesting, not file size or content.

**Check 12 — `cell.ttl` matches `images/cell-ontology/cell.png`**: Current as of the diagram's 5-aug-2026 redraw, which dropped the `folder` arrow off `Cell` entirely, matching cell.ttl 3.23.0's outright removal of `cell:folder` (a cell's folder is now purely the folder its cell-databook physically lives in, never a stored path, since a folder holds at most one cell-databook — cell.ttl 3.22.0 — so the folder<->cell mapping needs nothing recorded). `Cell` now shows only `origin` (to a `cat:Category` box, correctly drawn **0..1**, matching `cell:origin`'s actual cardinality — this was already correct before today's redraw too, contrary to an earlier revision of this check that had (incorrectly) flagged it as a 1..1 mismatch). `cell:origin`'s range is the classificatory `cat:Category` — category.ttl 1.31.0 deleted the tree-position facet (`cat:Folder` and its subclasses) outright, so there is no longer any tree-position class this could be confused with — so it does not conflict with `cell:Cell`'s "no link to a tree position" design (see `cell:Cell`'s own `rdfs:comment`) — it records what kind of thing a cell is, not where it lives, and needs no `owl:imports category.ttl` (referenced by name only, mirroring `cell:creator`'s identical pattern). ⚠️ **Still-open discrepancy**: the diagram still shows a `chat` arrow off `Cell` (to a box literally labeled "TBD") with no counterpart in `cell.ttl` — README.md already describes intended semantics for this too ("optional path to chat stream") but it has not been implemented in `cell.ttl`. Per this check's own rule below, don't silently resolve this either direction — surface it and ask whether `chat` is a planned property not yet added to `cell.ttl`, a stale leftover from an earlier design, or something else. Otherwise current as of cell.ttl 3.15.0: the diagram no longer shows a `note` arrow off `Cell`, matching `cell.ttl` 3.15.0's removal of `cell:note` (the separate notes/files folder hierarchies merged into one single hierarchy under `cell:folder`, itself later removed outright — see above); also correctly shows the `memberTopics`/`otherTopics` split (cell.ttl 3.14.0, renamed from `partyTopics` in 3.17.0) and the `t:SCTopicGraph` label (topic.ttl 1.15.0), both drawn as two separate arrows off `ACell` to a `t:SCTopicGraph` box. `Cell` (abstract, blue) carries `origin` only (plus the still-open `chat` arrow above). `Cell` splits into two orthogonal facets: `TCell` (abstract, blue, the template facet) carries `templateShape` (to a `sh:NodeShape` box); `ACell` (abstract, blue, the actual/instantiated facet) carries `subject` (to an `xsd:anyURI` box, 1..2 — renamed from `primary` in cell.ttl 3.12.0, range widened from `topic:SCTopicGraph`), `memberTopics` (to a `t:SCTopicGraph` box, cardinality varying by member count — split from `topics`/`secondary`, cell.ttl 3.14.0), `otherTopics` (to a `t:SCTopicGraph` box, 0..N uniformly — the other half of that same split), `shape` (to a `sh:NodeShape` box), `creator` (to a union of `p:Person`/`o:Organization`/`g:Group`), and `memberCount` (to `OneMember`/`TwoMember`/`ThreePlusMember` 1..1). The member-composition hierarchy — `OneMember` and `MultiMember` (abstract) → `TwoMember`/`ThreePlusMember` — hangs off `ACell`, not `Cell` directly; `TCell` has no subclasses of its own, since a template cell individual is instead multi-typed with both `TCell` and its `ACell`-lineage class (e.g. `OneMember`) — see `cell-templates.ttl`. `MultiMember` shows no arrows of its own, matching `cell:subject`/`cell:memberTopics`/`cell:otherTopics`'s domain being the broader `cell:ACell` rather than `cell:MultiMember`. No arrow points from `Cell`, `TCell`, or `ACell` to any tree-position box at all — category.ttl 1.31.0 deleted `cat:Folder` and its subclasses outright, so no such box exists any more — `cell:origin`'s arrow points to `cat:Category` instead, the classificatory hierarchy. This diagram is the ontology-level (not example-tree) picture of `cell:Cell`'s structure (redrawn for the 3.0.0/1.0.0 Cell/Category split, again for the 3.7.0 TCell/ACell split, again for the 3.10.0 graph/sc-context → primary/secondary rename, again for the 3.12.0 primary/secondary → subject/topics rename, again for the topic.ttl 1.15.0 SCtopic → SCTopicGraph label fix and the cell.ttl 3.14.0 topics → partyTopics/otherTopics arrow split, again for the cell.ttl 3.15.0 removal of the `note` arrow, again for the cell.ttl 3.17.0 party→member rename, again for the cell.ttl 3.20.0 addition of `cell:origin`, and again for the cell.ttl 3.23.0 removal of `cell:folder`) — the member-composition hierarchy and its content-linking properties. Unlike Check 10 (example diagrams, where the diagram always wins), this check does not presume which side is authoritative when the two disagree — surface the discrepancy and ask:

- **12a** — every property arrow shown off `Cell` (`origin`) has a corresponding `cell:` property in `cell.ttl` with `rdfs:domain cell:Cell` (the diagram's `chat` arrow currently fails this — see the still-open discrepancy above). Every arrow off `TCell` (`templateShape`) has `rdfs:domain cell:TCell`; every arrow off `ACell` (`shape`, `creator`, `memberCount`, `subject`, `memberTopics`, `otherTopics`) has `rdfs:domain cell:ACell` — `creator` and `memberCount` were narrowed here from `cell:Cell` in cell.ttl 3.7.0 (`memberCount` itself renamed from `parties` in 3.17.0), `subject`/`topics` (renamed from `primary`/`secondary`, themselves renamed from `graph`/`sc-context`) in 3.10.0/3.12.0, and `topics` itself split into `partyTopics`/`otherTopics` in 3.14.0 (`partyTopics` itself renamed to `memberTopics` in 3.17.0). `MultiMember` should show no arrows of its own — it carries no property, since `cell:subject`/`cell:memberTopics`/`cell:otherTopics`'s domain is the broader `cell:ACell`. Each arrow's target type in the diagram must match the property's `rdfs:range` — `subject`'s is `xsd:anyURI` (widened from `topic:SCTopicGraph` in cell.ttl 3.12.0, since its value is the resource(s) the cell is about, not a topic container; `subject` is an `owl:AnnotationProperty`, unlike the other `ACell` arrows, though the diagram doesn't visually distinguish annotation from object properties by arrow style anywhere), `memberTopics`'s and `otherTopics`'s are both `topic:SCTopicGraph` (unchanged range from `topics`; narrowed from plain `topic:TopicGraph` for `primary`/`graph` in 3.10.0; renamed from `context:SCcontext`/`context:Context` in cell.ttl 3.11.0; the diagram's box for this target correctly reads `t:SCTopicGraph`, not the retired `t:SCtopic` label), `creator`'s is the union of `p:Person`/`g:Group`/`o:Organization`, `memberCount`'s is `cell:ACell` itself (value is the concrete subclass, not `xsd:string`; range narrowed from `cell:Cell` in 3.7.0), `origin`'s is `cat:Category` itself (value is the concrete leaf subclass, e.g. `cat:Others`, not `xsd:string` — the same class-value-punning pattern as `memberCount`), `templateShape`'s and `shape`'s are both `sh:NodeShape` — two separate arrows from two different boxes (`TCell` vs `ACell`) to what may be drawn as the same target, since they're two distinct properties, not one property under two names. No `note` arrow should appear off `Cell` at all — `cell:note` was removed in cell.ttl 3.15.0.
- **12b** — every `cell:` property defined in `cell.ttl` appears as an arrow in the diagram, under the box matching its domain — `Cell`, `TCell`, or `ACell` (catches new properties added to the ttl but never drawn, or drawn under the wrong box). `cell:origin` satisfies this as of cell.ttl 3.20.0.
- **12c** — the class hierarchy `Cell` → `TCell`/`ACell` (both abstract), and separately `ACell` → `MultiMember` (abstract) → `TwoMember`/`ThreePlusMember`, plus `ACell` → `OneMember`, shown in the diagram matches `cell.ttl`'s actual `rdfs:subClassOf` relationships (by class local name, not just position). `OneMember` and `MultiMember` must not be drawn as direct children of `Cell` — both moved under `ACell` in cell.ttl 3.7.0.
- **12d** — each concrete `Cell` subtype's example `cell:label` value shown in the diagram (`"Single-Member Cell"`, `"Two-Member Cell"`, `"Multi-Member Cell"`) matches that subtype's actual `cell:label` value in `cell.ttl` — these display strings were updated in cell.ttl 3.17.0 (from `"Cell"`/`"Two-Party Cell"`/`"Multi-Party Cell"`) to match the redrawn diagrams. `cell:label` here is a class-level default display name — category.ttl 1.31.0 deleted `cat:label` (the per-instance display name it used to be distinguished from) outright, since it lived on the now-deleted `cat:Folder` — `Cell`, `TCell`, `ACell`, and `MultiMember` are all abstract and carry no `cell:label` of their own.

**Check 13 — `topic.ttl` matches `images/topic-ontology/topic.png`**: ⚠️ **Stale as of topic.ttl 1.15.0** — the diagram still shows boxes labeled `Topic` and `SCtopic`, the retired pre-1.15.0 class names; it needs manual redrawing to `TopicGraph`/`SCTopicGraph` and is described below in its pre-1.15.0 form for reference. Redrawn for the context→topic rename and the `subject` range broadening: `Topic` shows only `template`; `SCtopic` (subClassOf `Topic`) shows `subject` (targeting `xsd:anyURI` — any resource IRI, not necessarily `p:Person`/`g:Group`/`o:Organization`) and `claimant` (targeting `p:Person`/`g:Group`/`o:Organization`, not `i:PDNidentifier`) — no `about-by` arrow, matching the earlier deletion of `context:about-by`. No leaf subtype boxes below `SCtopic`, matching the earlier deletion of `SBScontext`/`OBScontext`/`OBOcontext`/`SBOcontext` — `SCTopicGraph` has no subclasses. Once redrawn for topic.ttl 1.15.0, the two boxes should simply read `TopicGraph` and `SCTopicGraph` — no change to which arrows they carry or those arrows' targets/cardinalities, this is a pure rename with no domain/range/cardinality changes. This diagram is the ontology-level picture of `topic:TopicGraph`'s structure. After any change to `topic.ttl` or to this diagram, verify:

- **13a** — every property arrow shown off `TopicGraph` in the diagram (`template`) has a corresponding `topic:` property in `topic.ttl` with `rdfs:domain topic:TopicGraph`, and its target type matches the property's `rdfs:range`.
- **13b** — every property arrow shown off `SCTopicGraph` in the diagram (`subject`, `claimant`) has a corresponding `topic:` property with `rdfs:domain topic:SCTopicGraph`; `claimant`'s target in the diagram must match its actual `rdfs:range` — a union of `p:Person`/`g:Group`/`o:Organization`, not `i:PDNidentifier`; `subject`'s target must match its actual `rdfs:range` — any resource IRI (`xsd:anyURI`), not a Person/Group/Organization union. No `about-by` arrow should appear — `context:about-by` was deleted (context.ttl 1.9.0).
- **13c** — every `topic:` property with domain `topic:TopicGraph` or `topic:SCTopicGraph` defined in `topic.ttl` appears in the diagram under the correct box (catches new properties added to the ttl but never drawn, or drawn under the wrong box).
- **13d** — no subclasses appear below `SCTopicGraph` — `topic.ttl` defines none (`SBScontext`/`OBScontext`/`OBOcontext`/`SBOcontext` were deleted in context.ttl 1.8.0). If any reappear here or in `topic.ttl`, reconcile them.

**Check 14 — `category.ttl` matches `images/category-ontology/category.png`**: Current as of category.ttl 1.31.0, pending the user's redraw — category.ttl 1.31.0 deleted the entire tree-position facet (`cat:Folder` and its subclasses `cat:CategoryDefined`/`cat:UserDefined`, plus `cat:child`/`cat:cell`/`cat:category`/`cat:catType`/`cat:label`) outright, so `category.png` should be redrawn to drop the `Folder` side entirely. This diagram is now the ontology-level picture of `cat:Category`'s structure alone: `cat:Category` (abstract, blue) carries only `templateCell` (to a `cell:TCell` box — narrowed from `cell:Cell` in category.ttl 1.18.0, once cell.ttl 3.7.0 split `cell:Cell` into its `TCell`/`ACell` facets) — an annotation asserted directly on the class, not an instance; `cat:Person`/`cat:Organization` (abstract, blue) are its direct subclasses, each with representative leaf examples (Affiliations/People/Work under Person; Suppliers/People (org) under Organization). No `Folder`/`CategoryDefined`/`UserDefined` boxes and no `child`/`cell`/`category`/`catType`/`label` arrows should appear anywhere. This diagram does not presume which side is authoritative when the two disagree — surface the discrepancy and ask. After any change to `category.ttl` or to this diagram, verify:

- **14a** — the only property arrow in the diagram is `templateCell`, off `Category`, matching `category.ttl`'s `cat:templateCell` (`rdfs:domain owl:Class` — an annotation asserted on the class itself, not scoped to `cat:Category` specifically at the OWL level; `rdfs:range cell:TCell`). No `catType`, `child`, `cell`, `category`, or `label` arrow should appear anywhere — all five properties, along with the `Folder`/`CategoryDefined`/`UserDefined` classes they lived on, were deleted in category.ttl 1.31.0. No `templateShape` arrow should appear either — that's a `cell.ttl` property (see Check 12), never a `category.ttl` one. There must be no `Canonical` box and no `copiedFrom` arrow anywhere — both were removed in category.ttl 1.8.0, well before the 1.31.0 Folder deletion.
- **14b** — every `cat:` property defined in `category.ttl` appears as an arrow in the diagram, under the box matching its domain (catches new properties added to the ttl but never drawn, or drawn under the wrong box). As of category.ttl 1.31.0 this means just `templateCell`.
- **14c** — the class hierarchy `Category` → `Person`/`Organization` (both abstract) and their leaf subclasses, shown in the diagram matches `category.ttl`'s actual `rdfs:subClassOf` and `cell:abstract` values. There is no second tree to check any more — `category.ttl` defines no `Folder` hierarchy at all as of 1.31.0.

**Check 15 — `images/cat-cell-topic.png` matches example usage**: Current as of cell.ttl 3.17.0 — redrawn with a substantially reworked Key legend, now split into two separate boxes on the right rather than one combined Key: a **Category** legend (title "Class"/"Label") giving the three `cat:Category`-family swatches — Person (tan), UserDefined (purple), Organization (light blue), matching Check 14's `cat:Person`/`cat:Organization` naming — and a **Cell** legend giving: a blue **Subject** heading over a green-filled circle labeled "Claimed by Other", a white/outlined circle labeled "Claimed by Self", and a gray swatch labeled "Shared"; two more circle entries labeled "Member Topic" and "Other Topic" (mapping to `c:memberTopics`/`c:otherTopics` respectively — visually similar at normal viewing size, so lean on the legend's text labels rather than trying to eyeball a ring-style difference); and three cell-box border-style entries — "Multi-Member Cell" (bold/double border), "Two-Member Cell" (double border), "Single-Member Cell" (single border) — these are exactly the `cell:label` strings cell.ttl 3.17.0 updated `cell:ThreePlusMember`/`cell:TwoMember`/`cell:OneMember` to (see Check 12d). Every topic circle in the diagram body now also carries an explicit subject-name label (e.g. "Bob", "Self", "Carol", "BHS") baked directly into the circle, not just a bare ring — a strictly more informative rendering than the diagram's earlier unlabeled-circle form. This diagram illustrates representative cell/category associations, generically rather than tied to a specific example instance: "Work" (a `cat:CategoryDefined` representing `cat:Work`, no override label), "Organization / Acme" (a `cat:CategoryDefined` representing `cat:Organization`, `cat:label`-renamed "Acme"), "Favorites" (a hypothetical `cat:UserDefined` category with no canonical counterpart, not tied to any real example data — there is currently no real `cat:UserDefined` example in the tree), "Others / Bob Johnson" (a `cat:CategoryDefined` representing `cat:Others`, `cat:label`-renamed "Bob Johnson" — a `cell:TwoMember` cell, all four topic link types filled), and "Affiliations / Boston Hub Society" (a `cell:ThreePlusMember` cell with two other members, Carol and BHS) — it replaces the earlier `images/cell-ontology/cells+contexts.png`. Each box's header shows `cat:catType` (green) over `cat:label` (bold) when a label is set, or just `catType` alone otherwise (e.g. "Work", which has no override label). Every cell box also shows a folder icon and a second icon next to it (chat, per the label used in `images/cell-ontology/cell.png` — see Check 12's open `cell:chat` discrepancy there, which applies equally here since this diagram draws the same two-icon pair on every cell box). Re-verify each box's `Member Topic`/`Other Topic` circles and blue `Subject` text remain a valid illustration of the properties and cardinalities described in the Cell and Category Ontology sections of `README.md` after any change to those properties.

**Check 16 — IRI roots: `mee.foundation/ontologies` for foundational files, `www.example.org` for example data**: Every foundational ontology and SHACL shapes file — `persona.ttl`, `topic.ttl`, `cell.ttl`, `category.ttl`, `cell-templates.ttl`, `pdn-identity.ttl`, `group.ttl`, `organization.ttl`, `persona-templates.ttl`, their `*-shacl.ttl` companions (including `cell-templates-shacl.ttl`), and the per-template files in `shacl/` — must declare its `owl:Ontology` IRI under `http://mee.foundation/ontologies/`. There is no longer a separate canonical category/cell DataBook tree to check (`categories-person/`/`categories-org/` were removed in category.ttl 1.8.0) — the canonical tree's IRI roots are covered by `category.ttl`/`cell-templates.ttl` themselves. Every DataBook under `example/Cells/` (excluding `under-development/`) represents Alice's own example instance data, so both its own `id:` and every `mia.topics[].id` value it carries must be grounded under `http://www.example.org/` (or `https://www.example.org/`). Run:

```python
import os, re, glob, yaml

FOUNDATIONAL_TTL = [
    'persona.ttl', 'topic.ttl', 'cell.ttl', 'category.ttl', 'cell-templates.ttl',
    'pdn-identity.ttl', 'group.ttl', 'organization.ttl', 'persona-templates.ttl',
    'persona-shacl.ttl', 'cell-shacl.ttl', 'topic-shacl.ttl',
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

def frontmatter(path):
    text = open(path, encoding='utf-8').read()
    m = re.match(r'^---\n(.*?)\n---', text, re.DOTALL)
    return yaml.safe_load(m.group(1)) if m else None

def check_cell_tree_id_roots(pattern, expected_prefixes):
    global errors
    for path in sorted(glob.glob(pattern, recursive=True)):
        if 'under-development' in path.split(os.sep):
            continue
        fm = frontmatter(path)
        if not fm:
            continue
        iri = fm.get('id')
        if iri and not any(str(iri).startswith(p) for p in expected_prefixes):
            print(f'WRONG ID ROOT: {path} -> {iri}')
            errors += 1
        for topic in (fm.get('mia', {}) or {}).get('topics') or []:
            tid = topic.get('id') if isinstance(topic, dict) else None
            if tid and not any(tid.startswith(p) for p in expected_prefixes):
                print(f'WRONG TOPIC ID ROOT: {path} -> {tid}')
                errors += 1

check_cell_tree_id_roots('example/Cells/**/*.databook.md', ['http://www.example.org/', 'https://www.example.org/'])

print('OK — no IRI-root violations found.' if errors == 0 else f'{errors} violation(s) found.')
```

If a violation is found, rename the offending file's `owl:Ontology`/`id:` IRI to the correct root, and update every DataBook `shapes:` YAML reference, catalog entry, and cross-reference that pointed at the old IRI to match (see Check 5's Tier 1/Tier 2 validation commands, which also hardcode these IRIs via the `shapes:` mechanism).

**Check 17 — `memberTopics` distinct-subject count matches member class**: `cell:memberTopics`'s cardinality (cell-shacl.ttl's `:OneMemberShape`/`:TwoMemberShape`/`:ThreePlusMemberShape`) guarantees *enough* topics per member count, but not that they're topics *about* the right number of distinct members — a cell could satisfy the count while every topic repeats the same `t:subject` (e.g. two `memberTopics` both with `subject: ":Self"` on a `TwoMember` cell). The additional invariant: across all of a cell's `memberTopics` (found via the topic's own `subject`, not `claimant`, in that same cell's own `mia.topics` list — no longer a separate topic-databook file), the number of **distinct** `t:subject` values must be at least 1 for `cell:OneMember`, 2 for `cell:TwoMember`, and 3 for `cell:ThreePlusMember` — one per member in the relationship. This is not itself an OWL/SHACL-expressible constraint (it requires dereferencing each `memberTopics` value's own `subject`, not just counting `memberTopics` values), so it's checked here instead. Run:

```python
import re, yaml, glob

def frontmatter(path):
    text = open(path, encoding='utf-8').read()
    m = re.match(r'^---\n(.*?)\n---', text, re.DOTALL)
    return yaml.safe_load(m.group(1)) if m else None

expected = {'cell:OneMember': 1, 'cell:TwoMember': 2, 'cell:ThreePlusMember': 3}
violations = 0
for f in glob.glob('example/Cells/**/*.databook.md', recursive=True):
    fm = frontmatter(f)
    if not fm:
        continue
    mia = fm.get('mia', {}) or {}
    member_count = mia.get('memberCount')
    if not member_count:
        continue
    topic_subject = {t['id']: t.get('subject') for t in (mia.get('topics') or []) if isinstance(t, dict)}
    pt = mia.get('memberTopics')
    pt = pt if isinstance(pt, list) else [pt]
    subs = set()
    for tid in pt:
        s = topic_subject.get(tid)
        if s is None:
            print(f'{f}: topic {tid} not found in mia.topics, or has no subject')
            continue
        subs.add(s if isinstance(s, str) else tuple(s))
    need = expected[member_count]
    if len(subs) < need:
        violations += 1
        print(f'VIOLATION {member_count} distinct_subjects={len(subs)} need>={need} subs={subs} {f}')
print('All cells satisfy the distinct-subject-count rule.' if violations == 0 else f'{violations} violation(s) found.')
```

If a violation is found, add a `memberTopics` entry whose `subject` is a member not yet represented (real content, not a placeholder — see the `cell:topics` → `partyTopics`/`otherTopics` split history, and the later `partyTopics`→`memberTopics` rename in cell.ttl 3.17.0, for worked examples), or reconsider whether the cell's `mia.memberCount` value is correct (e.g. a service-provider relationship with no true second member may belong as `cell:OneMember` instead of `cell:TwoMember`).

**Check 18 — `cell:subject` cardinality governs whether a subject's topic sits in `memberTopics` or `otherTopics`**: Check 17 confirms *enough* distinct subjects appear somewhere among `memberTopics`, but not *which* list (`memberTopics` vs `otherTopics`) a given subject's topic belongs in — that placement depends on how many `cell:subject` values the cell itself carries (`:OneMemberShape` and `:ThreePlusMemberShape` require exactly 1; `:TwoMemberShape` allows 1 or 2). The additional invariant: **if a `cell:OneMember` or `cell:TwoMember` cell has a single `subject` value**, that subject is the entity the relationship is *about* — it is not automatically one of the cell's active members (whose own topics fill the required `memberTopics` baseline: exactly 1 for `OneMember`, 2..4 for `TwoMember`) — so a topic whose `t:subject` matches the cell's `subject` must be linked via `otherTopics`, not `memberTopics` (e.g. `Paula-Walker(employee).databook.md`: `memberCount: "cell:OneMember"`, `subject: ":Paula_Walker"`; `memberTopics` holds Self's own topic (the member), `otherTopics` holds Paula's — the subject's — topic; similarly `Med.-App.-Info(medical-appointment-info).databook.md`, a `cell:TwoMember` with `subject: ":Paula_Walker"`: `memberTopics` holds Carol's and Self's topics, `otherTopics` holds Paula's own topic). **Exception**: if there aren't enough *other* topics (whose subject differs from the cell's subject) to fill the required `memberTopics` minimum, the subject's own topic may fill the shortfall instead — e.g. `Jane-Kolpakova(primary-care-physician).databook.md` (`cell:OneMember`, `subject: ":Jane_Kolpakova"`) has only one topic total, about Jane herself, and no alternative exists, so it necessarily occupies the required `memberTopics` slot. **If a `TwoMember` cell has two `subject` values**, those two values are the cell's active members, and each must be the `t:subject` of at least one topic among that cell's `memberTopics` (already covered by Check 17's count, but here checked by actual value match, not just count). This is not itself an OWL/SHACL-expressible constraint (same reasoning as Check 17), so it's checked here instead. Run:

```python
import re, yaml, glob

def frontmatter(path):
    text = open(path, encoding='utf-8').read()
    m = re.match(r'^---\n(.*?)\n---', text, re.DOTALL)
    return yaml.safe_load(m.group(1)) if m else None

REQUIRED_MIN = {'cell:OneMember': 1, 'cell:TwoMember': 2}
violations = 0
for f in glob.glob('example/Cells/**/*.databook.md', recursive=True):
    fm = frontmatter(f)
    if not fm:
        continue
    mia = fm.get('mia', {}) or {}
    member_count = mia.get('memberCount')
    if member_count not in REQUIRED_MIN:
        continue
    topic_subject = {t['id']: t.get('subject') for t in (mia.get('topics') or []) if isinstance(t, dict)}
    subj = mia.get('subject')
    subj = subj if isinstance(subj, list) else [subj]
    pt = mia.get('memberTopics') or []
    pt = pt if isinstance(pt, list) else [pt]
    ot = mia.get('otherTopics') or []
    ot = ot if isinstance(ot, list) else [ot]
    pt_subs = {t: topic_subject.get(t) for t in pt}
    ot_subs = {t: topic_subject.get(t) for t in ot}
    if len(subj) == 1:
        s = subj[0]
        all_linked = {**pt_subs, **ot_subs}
        other_topics_available = [t for t, sub in all_linked.items() if sub != s]
        required_min = REQUIRED_MIN[member_count]
        if len(other_topics_available) >= required_min:
            bad = [t for t, sub in pt_subs.items() if sub == s]
            if bad:
                violations += 1
                print(f'VIOLATION single-subject {s!r} topic(s) {bad} found in memberTopics (belong in otherTopics) in {f}')
    elif len(subj) == 2 and member_count == 'cell:TwoMember':
        missing = [s for s in subj if s not in pt_subs.values()]
        if missing:
            violations += 1
            print(f'VIOLATION two-subject cell missing {missing} from memberTopics subjects {set(pt_subs.values())} in {f}')
    else:
        violations += 1
        print(f'VIOLATION {f}: cell:subject has {len(subj)} values, expected 1 for cell:OneMember or 1-2 for cell:TwoMember')
print('All cell:OneMember/TwoMember cells satisfy the subject/otherTopics-memberTopics placement rule.' if violations == 0 else f'{violations} violation(s) found.')
```

If a violation is found, either relink the offending topic to the correct list (`memberTopics` for an active member's own topic, `otherTopics` for the single named subject's own topic when the cell has only one `cell:subject` value and enough other topics exist to fill `memberTopics` without it), or reconsider whether `cell:subject`'s value(s) or `cell:memberCount`'s value are correct for the relationship being modeled.

## Keeping Files in Sync

Whenever changes are made to any topic file, `persona.ttl`, or `topic.ttl`, `persona-shacl.ttl` must be updated to match:

- **New property usage in a topic** (e.g., a new physical characteristic, relationship, or identifier added to a Person or Persona instance) → add or extend a SHACL shape to validate that property on the relevant target class.
- **New class or property defined in `persona.ttl`** (e.g., `persona:hasSocialNetwork`) → add a SHACL shape that constrains how instances of the domain class may or must use it.

Always update `persona-shacl.ttl` in the same edit session as the change that triggers it.

## Validation

**SHACL validation** (e.g., using Apache Jena's `shaclvalidate`) — run against turtle extracted from a cell-databook (see README.md's Validation section for the full extraction pipeline; topic 14 is embedded in this cell):
```bash
databook extract "example/Cells/Affiliations/Boston Hub Society/Boston Hub Society(affiliations).databook.md" > /tmp/data.ttl
shaclvalidate -datafile /tmp/data.ttl -shapesfile persona-shacl.ttl
```

**Protégé**: Load `persona.ttl`; Protégé will import the domain ontologies via IRI resolution. Use the reasoner (HermiT/Pellet) to check consistency.

## README Coverage

`README.md` must be written in US English. Use American spellings throughout — e.g. "organization" not "organisation", "color" not "colour".

All classes and properties defined in `persona.ttl`, `topic.ttl`, `cell.ttl`, and `category.ttl` must be mentioned in `README.md` in the sections before the **Illustrative Example: Alice Walker** section. The only intentional exceptions are the internal ontology documentation annotation properties (`usesRequiredClass`, `usesOptionalClass`, `usesCCOClass`, `usesCCOProperty`, `usagePattern`), which are infrastructure for self-documenting the ontology, not user-facing terms.

In `README.md`, every mention of a class defined in `persona.ttl` must appear in backticks with the `p:` prefix (e.g. `p:Persona`, `p:Wallet`), every mention of a class or property defined in `topic.ttl` must appear in backticks with the `t:` prefix (e.g. `t:template`, `t:subject`), every mention of a class or property defined in `cell.ttl` must appear in backticks with the `c:` prefix (e.g. `c:Cell`, `c:memberCount`), and every mention of a class or property defined in `category.ttl` must appear in backticks with the `cat:` prefix (e.g. `cat:Category`, `cat:templateCell`). Every capitalized mention of `Person` (the CCO class) must also appear in backticks. These formatting rules do **not** apply inside headings or subheadings.

## Catalog Files

Two `catalog-v001.xml` files map ontology IRIs to local file paths so Protégé can resolve `owl:imports` without hitting the network:

- **`catalog-v001.xml`** (repo root) — used when opening root-level files (`persona.ttl`, `persona-shacl.ttl`, etc.) directly. Uses **relative** paths from the repo root.
- **`example/catalog-v001.xml`** — used when opening a topic file from the `example/` directory directly. Uses **absolute** `file://` paths.

**Whenever a `.ttl` file is created, deleted, renamed, or moved**, update both catalog files to match:
- **Create**: add a `<uri>` entry in both catalogs with the new file's ontology IRI (from its `rdf:type owl:Ontology` declaration) and its path.
- **Delete**: remove the corresponding `<uri>` entry from both catalogs.
- **Rename or move**: update the `uri=` path attribute in both catalogs.

The `id` attribute is a human-readable label (no functional significance); keep it consistent with the file's short name or diagram number.

## Gitignore Notes

`/project_files` is gitignored. The `project_files/` directory exists locally but is not tracked — it contains source domain ontologies and reference documents.
