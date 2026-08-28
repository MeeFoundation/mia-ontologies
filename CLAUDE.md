# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an **RDF/OWL ontology project** — a formal semantic knowledge model for representing natural people's identity data in Cellula, an identity agent application from Mee. It comprises four peer application ontologies:

- **Persona ontology** (`persona.ttl`): models identity data — names, addresses, identifiers, relationships, payment cards, and more — structured around graph-specific `Person` instances. Imports and profiles existing domain ontologies, documenting which of their classes and properties Mee uses, and extends them with app-specific terms.
- **Graph ontology** (`graph.ttl`): defines controlled vocabularies for classifying graph files — who claimed the data (`claimant`), and what or whom the file is about (`subject` — any resource IRI; the ontology does not require it to be a person's identity, though in the example data every `subject` value happens to be a `p:Person`/`o:Organization`, a convention of the example, not an ontology requirement). The four self-vs-other combinations these two values distinguish (self-by-self, other-by-self, other-by-other, self-by-other) are derived directly from `subject`/`claimant`, not a separate property or class hierarchy — `SCGraph` has no subclasses.
- **Cell ontology** (`cell.ttl`): defines `cell:Cell` — the self-contained *content* facet of a cell, carrying only what's common to every cell: `origin` (range `cat:Category`, at most one value, absent/nil exactly when the cell is of the UserDefined category — identified precisely by its cell-databook filename's `(custom)` disambiguator, not a vague judgment call — otherwise the concrete leaf class the cell was originally instantiated as, fixed at creation and not re-derived from the folder's current name, so a folder can be freely renamed or moved without needing to update it), letting a recipient's app use it as a hint for where to file a shared cell in its own tree; referenced by name without `owl:imports category.ttl`. `cell:origin` does not contradict `cell:Cell`'s "no link to a tree position" design, since its range is the classificatory `cat:Category`, not a tree position — a folder is purely a filesystem concept with no RDF individual at all. The folder ownership boundary rule: a subfolder belongs to a different, nested cell, not this one, iff it directly contains a `*.databook.md` file (the only DataBook type in a user's instance tree is `cell-databook`), checkable one folder at a time with no category-tree traversal. `cell:Cell` splits into two disjoint kinds (`owl:disjointWith` — a cell is always exactly one, never both): `cell:TemplateCell` (a reusable, class-level template, carrying `templateShape` and `isTopicCell` — a boolean flagging whether Lazy Instantiation's clone should be typed `cell:TopicCell`) and `cell:MemberCell` (abstract — an actual cell instantiated in a user's own tree is never directly typed `cell:MemberCell` alone, only one of its concrete member-count subclasses `OneMember`/`MultiMember`(abstract)/`TwoMember`/`ThreePlusMember`, hanging off `MemberCell` rather than `Cell` directly — carrying `memberCount`, `creator`, `members`, and `shape`). `cell:TopicCell` is a further subclass of `MemberCell` — a mixin that combines with whichever concrete member-count class a cell already has (e.g. a real cell is typed `MemberCell, TwoMember, TopicCell` together), for a cell that also carries at least one `topic` value. `members` (an `owl:ObjectProperty`, range `g:SCGraph`, domain `MemberCell`) links to the required baseline of graph DataBooks backing the cell's content, one or more per member required, cardinality enforced per member count; `topic` (same range, domain `TopicCell`) links to one or more additional graphs beyond that baseline — required (at least one, no upper bound) exactly when a cell is typed `TopicCell`, absent otherwise. There is no `cell:subject` property — who or what a cell's relationship is about is derived from `members`/`topic` instead (see Check 18). A `cell:Cell` carries no tree position of its own. Every cell in a user's own tree is typed `cell:MemberCell`, never `cell:TemplateCell`, which is reserved for the reusable class-level templates in `cell-templates.ttl` — a purely organizational cell with nothing substantive to say still carries a minimal stub `members` entry (claimed by and about `:Self`) rather than omitting member content altogether, and (having no third party to link) stays a bare `MemberCell`, never also `TopicCell`. In app/user terminology, a **cell** is the atomic tree unit — a filesystem folder holding this cell-databook file, folder and file together forming one tree node, with cells nesting inside cells to form the tree; `cell:Cell` itself models only the content facet and stores no property for that tree position, which is simply wherever the folder currently sits (see [Key Architectural Patterns](#key-architectural-patterns)'s Cell/Category split note).
- **Category ontology** (`category.ttl`): defines the *classificatory* facet of a category — which kind of thing it is (e.g. `cat:Work`, `cat:Affiliations`; the `Person`/`Organization` hierarchy and all leaf categories) — the canonical tree IS this class hierarchy (`rdfs:subClassOf`), not a separate set of instances. `category.ttl` defines no tree-position facet at all: a user's own instance-tree position is purely a filesystem fact (a cell is simply the folder its cell-databook physically lives in, with no RDF individual representing the folder at all), and `cell:origin` (`cell.ttl`) is the sole remaining RDF-level record of a cell's matched classification, asserted as a class value directly on the cell. A `cat:Category` subclass with reusable starter content carries `cat:templateCell` (an `owl:AnnotationProperty`) pointing directly at a `cell:Cell` template — mirroring `cell:abstract`'s precedent for asserting metadata directly on a class IRI. The `cat:templateCell` pointer triples for the 5 templated classes are asserted directly in `category.ttl`, right alongside each class's own declaration; the target `cell:Cell` individuals themselves are defined in the companion file `cell-templates.ttl` (which `category.ttl` `owl:imports`). That template cell may in turn carry `cell:templateShape` (an `owl:ObjectProperty`, defined in `cell.ttl` — not `category.ttl`, since its domain/range, `cell:Cell`/`sh:NodeShape`, never actually reference a `cat:` term) to the `sh:NodeShape`(s), in `cell-templates-shacl.ttl`, describing the content expected of a graph file filed under that category — making a class's shape reachable by pure RDF traversal (`cat:Category` → `cat:templateCell` → `cell:templateShape`), not merely by file co-location or naming convention. Because `cell:templateShape` lives in `cell.ttl`, `cell-templates.ttl` only needs to import `cell.ttl` directly, not `category.ttl` — so unlike `graph.ttl`/`cell.ttl`, `category.ttl`/`cell-templates.ttl` is a one-directional import, not mutual. `cell.ttl` imports `graph.ttl` (a separate mutual import), but not `category.ttl` — nothing in `cell.ttl` references `cat:` terms except by name in `cell:origin`'s range.

There are no build, compile, test, or lint commands. The files are Turtle (`.ttl`) loaded into semantic web tools (Protégé).

## Core Files

| File | Purpose |
|------|---------|
| `persona.ttl` | Persona ontology — imports domain ontologies, annotates which classes/properties are required vs. optional for Mee, defines app-specific classes and properties |
| `graph.ttl` | Graph ontology — controlled vocabularies for classifying graph files (`claimant`, `subject`) and the `Graph` class hierarchy. Mutually imports `cell.ttl` |
| `cell.ttl` | Cell ontology — `cell:Cell`, the content facet of a cell, carrying only what's common regardless of facet: `origin` — range `cat:Category`, at most one value (0..1; absent/nil exactly when the cell is of the UserDefined category, identified precisely by its cell-databook filename's `(custom)` disambiguator), else the concrete leaf subclass (class-value punning, like `memberCount`) it was originally instantiated as, fixed at creation rather than re-derived from the folder's current name, letting a recipient's app use it as a filing hint, referenced by name without `owl:imports category.ttl` (mirroring `creator`'s identical pattern below); does not contradict `cell:Cell`'s "no link to a tree position" design (see Check 12), since `cat:Category` is the classificatory hierarchy — a folder is purely a filesystem concept with no RDF individual at all. The folder ownership boundary rule: a subfolder belongs to a different, nested cell rather than this one iff it directly contains a `*.databook.md` file (the only DataBook type in a user's instance tree is `cell-databook`), resolvable one folder at a time with no category-tree traversal and no dependency on any recorded path. Splits into two disjoint kinds (`owl:disjointWith` — a cell is always exactly one, never both): `cell:TemplateCell` (abstract, a reusable class-level template — carries `templateShape`) and `cell:MemberCell` (abstract, an actual cell instantiated in a user's own tree — carries `memberCount`, `creator`, `members`, and `shape`). The `Cell`/`MultiMember`(abstract)/`OneMember`/`TwoMember`/`ThreePlusMember` member-count hierarchy hangs off `cell:MemberCell` rather than `cell:Cell` directly; `cell:TopicCell` is a further subclass of `MemberCell`, a mixin combining with whichever concrete member-count class a cell already has, for a cell that also carries at least one `topic` value — a real cell is never typed bare `MemberCell` alone, only one of `OneMember`/`TwoMember`/`ThreePlusMember`, optionally together with `TopicCell`. `memberCount`'s range is `cell:MemberCell` itself — its value is the concrete subclass (e.g. `cell:OneMember`), not a string, the same class-value-punning pattern `cell:origin` uses for its own range, `cat:Category`. `creator`'s range is a union of `p:Person`/`o:Organization`, referenced by name without importing those ontologies (mirroring `g:claimant`), required exactly one value, since every actual cell's content is authored by someone. `members` is an `owl:ObjectProperty` (range `g:SCGraph`, domain `MemberCell`) — the required per-member baseline, cardinality enforced per member count by `cell-shacl.ttl`'s per-member shapes; `topic` (same range, domain `TopicCell`) is one or more additional graphs beyond that baseline — required (at least one, no upper bound) exactly when a cell is typed `TopicCell`, absent otherwise. `templateShape` (domain `cell:TemplateCell`, range `sh:NodeShape`) links a template cell to its SHACL shape(s) describing what a graph filed under its category should look like. `shape` (domain `cell:MemberCell`, range `sh:NodeShape`) links an actual cell directly to the shape(s) validating its own content — distinct from `templateShape`. Every individual in `cell-templates.ttl` is typed solely `cell:TemplateCell` — never also `cell:MemberCell` or a `cell:MemberCell`-lineage class (including `TopicCell`), since the two kinds are disjoint. Carries no link back to a folder at all — a folder is purely a filesystem concept with no RDF individual; `origin` is the sole remaining record of a cell's original classification. Mutually imports `graph.ttl` |
| `category.ttl` | Category ontology — `cat:Category` (abstract, classificatory facet: the `Person`/`Organization` hierarchy and all leaf categories, plus `templateCell`). No tree-position facet at all: a user's own instance-tree position is purely a filesystem fact, with `cell:origin` (cell.ttl) the sole remaining RDF-level record of a cell's matched classification. No separate canonical folder class either — the canonical tree is the `cat:Category` class hierarchy itself. Imports `cell.ttl` and `cell-templates.ttl` |
| `cell-templates.ttl` | Class-level `cell:Cell` templates — one individual per templated class (`cat:Passport`, `cat:BirthCertificate`, `cat:DriversLicense`, `cat:MedicalAppointment`, `cat:PetsMedications`), each pointed at by its class's own `cat:templateCell` value (asserted in `category.ttl`, not here). Each is typed solely `cell:Cell, cell:TemplateCell` — `cell:TemplateCell` and `cell:MemberCell` are disjoint, so a template cell carries no member composition of its own, just `cell:templateShape` pointing to its SHACL shape in `cell-templates-shacl.ttl`, and the required `cell:isTopicCell` — `true` on `ctpl:MedicalAppointmentTemplateCell`/`ctpl:PetMedicationsTemplateCell`, `false` on the other three — flagging whether Lazy Instantiation's clone of the template is expected to be typed `cell:TopicCell`, since a real Medical Appointment or Medications cell always ends up carrying a `cell:topic` value. Imports `cell.ttl` directly — no mutual import with `category.ttl` |
| `cell-shacl.ttl` | SHACL validation shapes for `cell:Cell` DataBook instances, split across shapes matching `cell.ttl`'s two-kind split: `:CellShape` (target `cell:Cell`) — `origin` cardinality (at most one — 0..1 — not constrained via `sh:class cat:Category` since a legal value is the concrete leaf subclass itself, never `rdf:type cat:Category`, mirroring `cell:memberCount`'s own identical unconstrained, class-value-punning treatment above), plus an `sh:xone` requiring `rdf:type` to be exactly one of `cell:TemplateCell`/`cell:MemberCell` (mirroring `cell.ttl`'s `owl:disjointWith`); `:TemplateCellShape` (target `cell:TemplateCell`) — `templateShape` cardinality (at most one; deliberately not constrained to `sh:class sh:NodeShape` since its value is only typed as such in `cell-templates-shacl.ttl`, which Tier 1 excludes from its merged-data run) and `isTopicCell` cardinality (required, exactly one value, must be a boolean); `:MemberCellShape` (target `cell:MemberCell`) — `memberCount` required and constrained to be the class `cell:OneMember`/`cell:TwoMember`/`cell:ThreePlusMember`, `creator` (required, exactly one value) constrained to be a `p:Person` or `o:Organization`, and `shape` cardinality (at most one, same reasoning as `templateShape`); `:TopicCellShape` (target `cell:TopicCell`, the mixin subclass for a cell that carries at least one `topic` value) — `topic` required, at least one value, no upper bound, each constrained to be a `g:SCGraph`; plus three per-member shapes — `:OneMemberShape`/`:TwoMemberShape`/`:ThreePlusMemberShape` (target `cell:OneMember`/`cell:TwoMember`/`cell:ThreePlusMember` directly) — enforcing `members` (each constrained to `g:SCGraph`) as exactly 1/2..4/at least 3 respectively. There is no `subject` property/shape at all — a cell's subject is derived, never stored (see Check 18) |
| `persona-shacl.ttl` | SHACL validation shapes — constraint rules for all `persona:Person` instances (SSN format, address cardinality, payment cards, wallet, social network, etc.) |
| `graph-shacl.ttl` | SHACL validation shapes for graph DataBook instances — `:SCGraphShape` (`g:SCGraph`'s `subject`/`claimant`; `claimant` required exactly once and constrained to a `p:Person`/`o:Organization`, `subject` required exactly once and constrained to be an IRI — its range is `xsd:anyURI`, so a graph's subject need not be a person's identity); split out of `persona-shacl.ttl` since it validates a `graph.ttl` class, not `persona:Person`. A graph DataBook does not carry `cell:creator` (or any creator property) — that stays a `cell:Cell`-only property |
| `persona-templates.ttl` | Persona template labels — defines `p:PersonaTemplate` (abstract classification superclass) and concrete label subclasses `p:BirthCertificateDocument`, `p:JSContactCard`, `p:DriversLicenseDocument`, `p:PassportDocument`, `p:MedicalAppointmentRecord`, `p:PetMedicationRecord`; also defines related designator classes (`persona:DriversLicenseNumber`, `persona:IssuingJurisdiction`, `persona:PassportNumber`, `persona:IssuingCountry`, `persona:PlaceOfBirth`, `persona:GenderMarker`, `persona:IssueDate`, `persona:Credential`, `persona:WebURL`, `persona:OrganizationUnit`, `persona:JobTitle`), complex classes (`persona:Anniversary`, `persona:PersonalInfo`, `persona:PersonalityAssessment` with `persona:hasPersonalityAssessment`/`persona:personalityFramework`/`persona:personalityResult`/`persona:personalityAssessmentDate`), the `p:MedicalAppointmentRecord` claim properties (`persona:forPatient`, `persona:hasPrimaryCarePhysician`, `persona:currentMedication`, `persona:allergy`, `persona:medicalHistoryNote`, `persona:insuranceProvider`, `persona:insurancePolicyNumber`, `persona:insuranceGroupNumber`, `persona:preferredPharmacy`), and the `p:PetMedicationRecord`/`p:Medication` classes and properties (`persona:hasMedication`, `persona:Medication`, `persona:hasActiveIngredient` (ChEBI class IRIs), `persona:hasDoseForm` (DrOn dose-form class IRIs), `persona:DosageAmount`/`persona:hasDosageAmount` (CCO Measurement-Unit/Information-Bearing-Entity machinery), `persona:MedicationAdministration`/`persona:hasAdministration` (DrOn drug-administration process + BFO TemporalInterval), `persona:medicationFrequencyPerDay`, `persona:medicationBrandName`, `persona:medicationManufacturer`, `persona:medicationDuration` — see README's "Reused External Vocabulary"), and other properties (`persona:hasAnniversary`, `persona:hasPhoto`, etc.). `owl:imports` the new `project_files/dron-upper.ttl` (below) |
| `project_files/dron-upper.ttl` | A hand-curated subset of DrOn (the Drug Ontology)'s upper module — five classes ("drug product", "active ingredient", "drug tablet", "drug capsule", "drug administration") cited by their real upstream IRIs, not a full mirror (DrOn's full distribution is ~300MB of RxNorm-derived per-product classes not relevant here). `owl:import`ed by `persona-templates.ttl`. The first non-CCO/non-`mee.foundation` external ontology this project has ever vendored |
| `cell-templates-shacl.ttl` | Per-template SHACL shapes for birth certificate, driver's license, passport, medical appointment, and pet medication graph files — `:BirthCertificateDocumentShape`, `:DriversLicenseDocumentShape`, `:PassportDocumentShape`, `:MedicalAppointmentRecordShape`, `:PetMedicationRecordShape`, `:MedicationShape`, `:DosageAmountShape`, `:MedicationAdministrationShape` — each directly linked from its `cell-templates.ttl` template cell via `cell:templateShape`; run against the individual graph file, not merged data |
| `shacl/jscontactcard-shacl.ttl` | Per-template SHACL shapes for JSContactCard graph files — run against the individual graph file, not merged data (JSContactCard is reused across many unrelated tree positions with no single `cat:Category` class of its own, so its shape stays standalone) |
| `yaml-to-rdf.py` | Synthesizes `cell:`/`graph:` triples from each cell-databook's `mia.` YAML frontmatter (including its embedded `mia.graphs` list), used as Tier 1 validation Step 1b (see EXAMPLE.md's Validation section) — `databook extract` only pulls fenced Turtle blocks, which cell-databooks mostly don't carry, so without this script `cell:Cell` individuals and `g:SCGraph`'s subject/claimant never reach the merged validation graph. No category-side synthesis at all — a folder's tree position is purely a filesystem fact with no RDF individual to synthesize |
| `project_files/` | Reference materials: imported domain ontologies (PersonOntology.ttl, AddressOntology.ttl, StagingOntology.ttl), BFO/CCO source files, PDFs, docs |
| `APP-BEHAVIOR.md` | App-behavior documentation — how the app uses the ontologies above: cell lifecycle (Lazy Instantiation), storage and sync, sharing/permissions (Number of Members, Write Permissions), cell naming/renaming/collision handling, how a cell is persisted as a filesystem folder (naming and fill/text-color conventions), and the auto-filing heuristic used when a shared cell is received. Not itself an RDF file — no `owl:versionInfo`. Linked from `README.md` and `EXAMPLE.md` |

## Example Files

Every graph below is an embedded section (`mia.graphs` entry + `### Graph NN` body) inside its owning cell-databook file under `example/Cells/` — there are no standalone graph files (see [Graph ID Naming Convention](#graph-id-naming-convention)).

| Graph — File | Purpose |
|------|---------|
| Graph 06 — `example/Cells/Work/Acme/Employees/Paula Walker/Paula Walker(employee).databook.md` | Paula Walker as Alice's Acme colleague — claimed by Alice |
| Graph 07 — `example/Cells/People/Immediate Family/Paula Walker/Paula Walker(immediate-family).databook.md` | Paula Walker as Alice's family member — claimed by Alice |
| Graph 05 — `example/Cells/People/Immediate Family/Paula Walker/Paula Walker(immediate-family).databook.md` | Paula Walker's own family persona; social network with Alice |
| Graph 08 — `example/Cells/People/Others/Bob Johnson/Bob Johnson(others).databook.md` | Alice Walker as seen by Bob Johnson — claimed by Bob |
| Graph 04 — `example/Cells/People/Others/Bob Johnson/Bob Johnson(others).databook.md` | Alice's notes about Bob Johnson; favorite drink: oat milk cappuccino |
| Graph 02 — `example/Cells/People/Others/Bob Johnson/Bob Johnson(others).databook.md` | Bob Johnson's self-claimed persona; social network with Alice |
| Graph 14 — `example/Cells/Affiliations/Boston Hub Society/Boston Hub Society(affiliations).databook.md` | Alice's Boston Hub Society profile — email, phone, and current address |
| Graph 01 — `example/Cells/Affiliations/Boston Hub Society/Boston Hub Society(affiliations).databook.md` | BHS — o:Organization instance; BHS's own claimed profile |
| Graph 03 — `example/Cells/Affiliations/Boston Hub Society/Boston Hub Society(affiliations).databook.md` | Bob Johnson's BHS member persona — name, email, phone, address |
| Graph 09 — `example/Cells/Finances/Banking & Payments Firms/Citibank/Citibank(banking-payments).databook.md` | Alice's Citibank graph — debit card; claimed by Citibank |
| Graph 27 — `example/Cells/Finances/Banking & Payments Firms/Citibank/Citibank(banking-payments).databook.md` | Alice's own self-claimed notes about Citibank as an institution, alongside Citibank's own claimed record about her (graph 09) |
| Graph 16 — `example/Cells/Companies/Google/Google(companies).databook.md` | Alice's Google graph — Gmail address |
| Graph 11 — `example/Cells/Companies/ATT/ATT(companies).databook.md` | Alice's AT&T graph — phone number |
| Graph 24 — `example/Cells/Government/State/Texas Vital Records/Texas Vital Records(birth-certificate).databook.md` | Alice's Texas birth certificate — legal names, maiden name |
| Graph 18 — `example/Cells/Government/Municipality/Paradise/Paradise(residence).databook.md` | Alice's Paradise, CA address — current residence (2025–present) |
| Graph 13 — `example/Cells/Government/Municipality/Boston/Boston(residence).databook.md` | Alice's Boston, MA address — previous residence (2020–2025) |
| Graph 23 — `example/Cells/Government/Federal/Social Security Administration/Social Security Administration(ssn).databook.md` | Alice's Social Security Number |
| Graph 12 — `example/Cells/People/Others/Bob Johnson/Bob Johnson(others).databook.md` | Alice's 1:1 graph with Bob; social network with Bob as member |
| Graph 21 — `example/Cells/People/Immediate Family/Paula Walker/Paula Walker(immediate-family).databook.md` | Alice's family graph — social network with Paula Walker as member |
| Graph 22 — `example/Cells/Things/Things.databook.md` | Alice's possessions — wallet, health insurance card, SSN card |
| Graph 20 — `example/Cells/Work/Acme/Employees/Paula Walker/Paula Walker(employee).databook.md` | Alice's Acme employee graph; social network with Paula Walker |
| Graph 10 — `example/Cells/Work/Acme/Employees/Alice Walker/Alice Walker(employee).databook.md` | Alice's business card (JSContactCard) — name, email, phone, employer, job title |
| Graph 15 — `example/Cells/Government/State/California DMV/California DMV(drivers-license).databook.md` | Alice's California driver's license — legal name, DOB, DL#, expiry, photo |
| Graph 19 — `example/Cells/Government/Federal/Department of State/Department of State(passport).databook.md` | Alice's US passport — legal name, DOB, passport#, issue/expiry, place of birth, gender marker, photo |
| Graph 17 — `example/Cells/People/Immediate Family/Paula Walker/Health & Wellness/Health & Wellness.databook.md` | Paula's physical characteristics — height, eye color, hair color — as recorded by Alice; linked via `cell:topic` (Paula is the cell's subject, not its member) |
| Graph 35 — `example/Cells/People/Immediate Family/Paula Walker/Health & Wellness/Health & Wellness.databook.md` | Alice's bare given-name claim — the cell's required `members` entry, claimed by Alice |
| Graph 36 — `example/Cells/Pets/Ginger/Ginger(pets).databook.md` | Deliberately empty — the `cat:Pets`-origin Ginger cell's required `members` entry, claimed by Alice; `members`' requirement is about `g:subject`/`g:claimant`, not content |
| Graph 37 — `example/Cells/Pets/Ginger/Ginger(pets).databook.md` | Alice's basic claim identifying Ginger — as the Ginger cell's sole `topic`, its own `subject: ":Ginger"` is what the cell's derived subject resolves to (see Check 18) |
| Graph 25 — `example/Cells/People/Immediate Family/Paula Walker/Health & Wellness/Medical/Provider/Jane Starostina/Jane Starostina(primary-care-physician).databook.md` | Alice's record of Dr. Jane Starostina, Paula Walker's primary care physician — claimed by Alice; linked via `cell:topic` (Jane is the cell's subject, not its member) |
| Graph 34 — `example/Cells/People/Immediate Family/Paula Walker/Health & Wellness/Medical/Provider/Jane Starostina/Jane Starostina(primary-care-physician).databook.md` | Alice's bare given-name claim — the cell's required `members` entry, claimed by Alice |
| Graph 26 — `example/Cells/People/Immediate Family/Paula Walker/Health & Wellness/Medical/Provider/Medical Appointment/Medical Appointment.databook.md` | Alice and Carol's shared claims for Paula's medical appointment — medications, allergies, insurance, PCP reference — claimed by Alice |
| Graph 28 — `example/Cells/People/Immediate Family/Paula Walker/Health & Wellness/Medical/Provider/Medical Appointment/Medical Appointment.databook.md` | Carol's own self-claimed persona and contact info — one of this cell's two members, alongside Alice (graph 30) |
| Graph 30 — `example/Cells/People/Immediate Family/Paula Walker/Health & Wellness/Medical/Provider/Medical Appointment/Medical Appointment.databook.md` | Alice's own self-claimed contact info — the other of this cell's two members, alongside Carol (graph 28) |
| Graph 29 — `example/Cells/People/Others/Fred Flintstone/Fred Flintstone(others).databook.md` | Alice's 1:1 graph with Fred; social network with Fred as member — claimed by Alice |
| Graph 31 — `example/Cells/People/Others/Fred Flintstone/Fred Flintstone(others).databook.md` | Fred's self-claimed Fred persona |
| Graph 32 — `example/Cells/Pets/Ginger/Health/Medications/Medications.databook.md` | Alice's record of her cat Ginger's medications — amoxicillin/clavulanate course, ongoing glucosamine/chondroitin supplement — claimed by Alice; linked via `cell:topic` (Ginger has no `p:Person` individual) |
| Graph 33 — `example/Cells/Pets/Ginger/Health/Medications/Medications.databook.md` | Deliberately empty — one of the cell's two required `members` entries, claimed by Alice |
| Graph 57 — `example/Cells/Pets/Ginger/Health/Medications/Medications.databook.md` | Deliberately empty — the other required `members` entry, claimed by Paula, after the cell (created by Self) was shared with Paula and became a `cell:TwoMember` cell |
| `example/graphs/self.ttl` | `:Self`'s sole type declaration (`rdf:type owl:NamedIndividual, persona:Person`); not `owl:imports`ed anywhere, merged in only for validation |

## Architecture

### Three-Layer Design

```
Triplestore (Fuseki) — loads all DataBook files directly:
  ├─ persona.ttl              (application profile — imports domain ontologies)
  │   ├─ PersonOntology.ttl
  │   ├─ AddressOntology.ttl
  │   └─ StagingOntology.ttl → BFO terms
  ├─ example/Cells/Work/Acme/Employees/Paula Walker/Paula Walker(employee).databook.md      (embeds graphs 06, 20)
  ├─ example/Cells/People/Immediate Family/Paula Walker/Paula Walker(immediate-family).databook.md  (embeds graphs 05, 07, 21)
  ├─ … (all other cell-databooks, each embedding one or more numbered graphs via mia.graphs)
  ├─ example/Cells/People/Immediate Family/Paula Walker/Health & Wellness/Health & Wellness.databook.md  (embeds graph 17)
  └─ example/graphs/self.ttl        (:Self's bare type declaration — merged in for validation, never owl:imports'd)

persona-shacl.ttl — no owl:imports of data; validated against the loaded dataset
shacl/jscontactcard-shacl.ttl — per-template shapes for JSContactCard files (only template with no cat:Category class of its own)
cell-templates-shacl.ttl — per-template shapes for birth certificate, driver's license, passport, and medical appointment files
```

1. **Foundation**: BFO (Basic Formal Ontology) — provides temporal modeling (`TemporalInterval`) and core relations
2. **Domain Ontologies** (in `project_files/`): PersonOntology, AddressOntology, StagingOntology
3. **Application Ontologies** (peer, not nested):
   - `persona.ttl`: aggregates domain ontologies; uses annotation properties (`usesRequiredClass`, `usesOptionalClass`, `usesCCOClass`, `usesCCOProperty`) to document Mee's usage
   - `graph.ttl`: defines `claimant` and `subject` vocabularies; imported directly by each graph file
   - `cell.ttl`: defines `cell:Cell`, the content facet of a cell (graph links common to all cells), split into two disjoint kinds — `cell:TemplateCell` (a reusable class-level template) and `cell:MemberCell` (an actual cell instantiated in a user's own tree, carrying member composition); mutually imports `graph.ttl`
   - `category.ttl`: defines `cat:Category` (classificatory facet only: `templateCell`) — no tree-position facet at all; a folder is purely a filesystem concept with no RDF individual, and `cell:origin` (cell.ttl) is the sole remaining RDF-level record of a cell's matched classification; no separate canonical folder class either — the canonical tree is the class hierarchy itself; imports `cell.ttl` and `cell-templates.ttl`

### Cell DataBook Filename Convention

Cell-databook filenames follow (there is no separate category-databook file — a folder's sole DataBook is its cell-databook, see [Key Architectural Patterns](#key-architectural-patterns)'s Cell/Category split note):

```
<local>(<catType>).databook.md  — cell-databook
```

`<local>` is an **exact copy of the folder's own name** — verbatim, no kebab-casing, no lowercasing, whatever case/spacing/punctuation the folder itself has (e.g. `Acme`, `Paula Walker`, `ATT`). There is no more `-cell` token: cell-databook is the sole DataBook type in a user's instance tree, so nothing needs to be disambiguated by it. There is also no numeric disambiguator of any kind (no `-2`, `-N`, etc.): a folder holds **at most one** cell-databook, ever — a folder is a **cell** only when it holds exactly one such matching file, and a folder with no matching cell-databook is simply a plain filesystem folder, not a cell at all (see [Cell/Category split](#key-architectural-patterns) below for why two cells can never share one folder). `<catType>` is the folder's own category classification, kebab-cased as before (e.g. `Employee` → `employee`, `ImmediateFamily` → `immediate-family`, `SSN` → `ssn` — kebab-casing is acronym-aware: a hyphen is inserted only at a lowercase→uppercase boundary or an uppercase-run→lowercase boundary, so consecutive capitals stay together). If the matched `cat:Category` class's own local name carries a literal `(org)` disambiguator (used only to distinguish it from a same-named Person-side sibling class, e.g. `cat:BankingPayments` vs. `cat:BankingPayments(org)`), that suffix is dropped before kebab-casing — `<catType>` only ever needs to disambiguate a *recurring folder name* by role (e.g. Paula Walker's `Employee` folder vs. her `ImmediateFamily` folder, both Person-side), never the Person/Organization split itself, which is already carried by the folder's own tree position and by `cell:origin`'s actual asserted value, never by the filename. So Citibank's cell — `cell:origin: cat:BankingPayments` (Person-side, since it's the person's own relationship with the bank, not company business filed under `Work`) — is `Citibank(banking-payments).databook.md` with no `-org` marker, and the same bare `banking-payments` `<catType>` would apply identically if a cell's `cell:origin` were instead the org-side `cat:BankingPayments(org)`, since nothing in the filename needs to tell the two apart. A cell-databook's `<catType>` parenthetical is purely a filename-level disambiguator — `cat:catType` does not exist in RDF at all, so nothing in RDF records it, and nothing reverse-matches the filename to derive it. The one RDF-level echo of a folder's classification is `cell:origin`, read directly from the cell-databook's own explicit `mia.origin` YAML field, not derived from the filename at all. Unlike the filename, a cell-databook's `id:` is deliberately *not* derived from the folder name at all — it's a flat, opaque `http://www.example.org/mia/cells/cell-<NN>` (see [Check 9](#integrity-checks)), the same reasoning as the [Graph ID Naming Convention](#graph-id-naming-convention)'s `graph-<NN>`.

**UserDefined folders — `<catType>` is the literal `custom`**: a cell may legally carry no `cell:origin` at all — this is the UserDefined category, for a cell the user created without picking any existing `cat:Category` class. Since there is no origin class to kebab-case into `<catType>`, the filename uses the fixed literal string `custom` in its place, e.g. a folder named `Friends` with no origin is `Friends(custom).databook.md`. The compression rule below still applies verbatim on top of this (a folder literally named "Custom" would compress to `Custom.databook.md`, though no real example does this) — `custom` is just an ordinary `<catType>` value from the filename's point of view, it just happens to never come from kebab-casing an `rdfs:label`.

**Compression rule**: if `<local>`, normalized the same acronym-aware way `<catType>` already is, is identical to the kebab-cased `<catType>`, the parenthetical is dropped entirely, since it's pure redundancy — `<local>.databook.md` — rather than `<local>(<local>).databook.md`. For example `cat:Work`'s folder is named `Work`, and its own `catType` (`Work`) also kebab-cases to `work` — the same string — so its file is `Work.databook.md`, not `Work(work).databook.md`. This applies on a normalized-equal match, not raw string identity (since `<local>` itself is never kebab-cased): folder `Health & Wellness`'s catType `HealthWellness` both normalize to `health-wellness`, so it compresses too, to `Health & Wellness.databook.md`. `Acme(organization).databook.md` keeps its parenthetical since normalized `Acme` (`acme`) ≠ `organization`. Most of the top-level tree scaffold compresses this way (`Work`, `People`, `Others`, `Companies`, `Finances`, `Government`, `State`, `Municipality`, `Federal`, `Things`, `Affiliations`, `Employees`, `Immediate Family`, `Health & Wellness`, `Medical`), since these folders' own name simply *is* their category (there's no more-specific person/organization/thing filed there directly — that's one level further down, e.g. `Boston Hub Society(affiliations)` or `Acme(organization)`, which don't compress). `Banking & Payments Firms(banking-payments).databook.md` is a further example of the non-compressing case: normalized `Banking & Payments Firms` (`banking-payments-firms`) ≠ `banking-payments`, since the folder's own name matches `cat:BankingPayments`'s full `rdfs:label` ("Banking & Payments Firms") rather than a shortened form. The same rule applies identically to a graph's `(<containing-cell>)` segment (see [Graph ID Naming Convention](#graph-id-naming-convention) below), since that segment is always derived directly from the (possibly-compressed) cell filename's `id:` form (space-hyphenated, not the raw filename — graph ids are IRIs too).

Folder naming is standardized as the category's own display label (the OS folder name is used verbatim, with no override field anywhere — the cell-databook's own `title:` field mirrors this name exactly rather than overriding it, see Check 19), but a folder's own name alone can't disambiguate a repeated name's *role* — e.g. Paula Walker's Immediate Family folder vs. her Acme Employee folder are both literally named "Paula Walker" — so `catType` carries that role encoding in the filename instead, not derived from folder position. This is exactly what disambiguates a name that legitimately recurs in two different roles — e.g. Paula Walker is both her own Immediate Family folder (`catType: ImmediateFamily` → `Paula Walker(immediate-family).databook.md`) and her Acme employee record (`catType: Employee` → `Paula Walker(employee).databook.md`); the same folder name, but never colliding, since a repeated name always means a *different* role and therefore a different `catType`.

### Graph ID Naming Convention

A graph lives physically inside its owning cell-databook's `mia.graphs` list and body (see [Key Architectural Patterns](#key-architectural-patterns)'s Cell/Category split note) — it has no file or filename of its own. Its `mia.graphs[].id` (which doubles as the graph's own named-graph identity, `{id}#graph`) does not re-encode `claimant`/`subject`/the containing cell into the id string, since those facts are already carried by that same entry's own sibling `claimant:`/`subject:` fields, and the containing cell is simply wherever the entry physically lives — encoding them a second time would be pure redundancy. It follows a single flat pattern instead:

```
http://www.example.org/mia/graphs/graph-<NN>
```

`<NN>` is the same zero-padded two-digit graph number used everywhere else for this graph — the diagram label, the `### Graph NN` body heading, and its `<a id="graph-NN">` anchor. `mia.members`/`mia.topic` entries reference a graph by its bare local name (`graph-<NN>`) rather than the full IRI (see [Check 3](#integrity-checks)).

**`claimant` vocabulary** (a `mia.graphs[]` entry's own field): takes the local IRI of a `p:Person` or `o:Organization` individual — NOT an `i:PDNidentifier`. Specifically: `:Self` (the user's `p:Person`) for self-claimed graphs; a named `p:Person` individual (e.g. `:Bob_Johnson`) when another user claims the data; and a named `o:Organization` individual (e.g. `:Citibank`) only when the claiming organization is itself PDN-interoperable. In the example data **only Citibank is treated as PDN-interoperable**, so only the graph embedded in `Citibank(banking-payments).databook.md` (id `graph-09`) uses `claimant: ":Citibank"`. All other organization-related graphs (Google, AT&T, SSA, etc.) use `claimant: ":Self"` because Alice self-enters that data — those organizations aren't PDN-interoperable. (This distinction is currently just a data-modeling convention in the example, not formally enforced by any property — `pdn-identity.ttl` defines no property for it.)

**"Other" claimants**: When the claimant is someone other than the current user (`:Self`), the claimant is a named individual of one of:
- `p:Person` — another user (a different person, e.g. `:Bob_Johnson` claiming data about Alice)
- `o:Organization` — a company, nonprofit, or government agency that is a PDN node (e.g. `:Citibank`)

**Examples** (id local-name and the corresponding `claimant`/`subject` field values, found in that same `mia.graphs[]` entry; the owning cell-databook file is found via [Check 3](#integrity-checks)):

| Id local-name | Subject | Claimed by | Containing cell |
|----------|---------|-------------|---------------------|
| `graph-09` | Self (Alice) | Citibank | Citibank(banking-payments) |
| `graph-07` | Paula Walker | Self (Alice) | Paula-Walker(immediate-family) |
| `graph-08` | Self (Alice) | Bob Johnson | Bob-Johnson(others) |
| `graph-03` | Bob Johnson | Bob Johnson | Boston-Hub-Society(affiliations) |
| `graph-01` | BHS | BHS | Boston-Hub-Society(affiliations) |

### Key Architectural Patterns

**All data belongs to graphs**: There is no separate selfness file holding a user's identity data. Every piece of identity data — names, identifiers, addresses, payment cards, physical characteristics — belongs to a graph-specific Persona file, asserted directly on the shared `:Self` individual. The one exception is `:Self`'s bare type declaration (`:Self rdf:type owl:NamedIndividual, persona:Person`), which lives once in `example/graphs/self.ttl` instead of being repeated with an `rdfs:label` in every graph file as it once was; `self.ttl` carries no other claims about `:Self` and is never `owl:imports`ed — it is merged in alongside the graph files only when validating (see the Tier 1/Tier 2 commands in EXAMPLE.md's Validation section). Every substantive fact about a user still lives exactly where it always has: in the graph file(s) it belongs to.

**`:Self` IRI convention**: The user's own `persona:Person` individual always uses the IRI `:Self` across all of their graph files. All other people, groups, and organizations are assigned locally-minted named IRIs (e.g. `:Bob_Johnson`, `:Paula_Walker`, `:BHS`). `:Self` is a local IRI and is never exposed externally over the PDN, so there are no collisions between instances of the app. All graph files in the example live in Alice's own instance — some authored by Alice, others received from peers over PDN. In either case, `:Self` refers to Alice. When data arrives from a peer's instance (where that peer was `:Self` in their own instance), Alice's own instance assigns them a locally-minted identifier; once a PDN connection is established, that identifier resolves to or is replaced by their PDN ID.

**Cell/Category split**: A **cell** is the atomic unit of a user's own instance tree: a filesystem folder holding exactly one cell-databook file, folder and file together forming one tree node — cells nest inside cells, forming the tree, with no RDF individual representing the folder as something separate from the cell. A cell's sole DataBook is its `cell-databook` (content: `memberCount`/`subject`/`members`/`topic`/`origin`); there is no sibling `category-databook` file. A cell's **content** — its **attachments**, shown in the app's Attachments tab — is every plain file found directly inside its own folder; attachments are flat, like email attachments, with no subfolder nesting. Any subfolder found there is never itself an attachment — it's either a **descendant cell** (holds its own cell-databook) — a separate tree node, never counted as part of its ancestor's content even though it physically sits inside the ancestor's folder — or a bare pass-through directory with no databook of its own, existing purely to reach a descendant cell nested deeper still (see Check 11), and likewise never shown in the Attachments tab. The one remaining RDF-level trace of a cell's classification is `cell:origin`, asserted directly on the cell as a class value (e.g. `cat:Passport`) recording the `cat:Category` subclass the cell was originally instantiated as — at most one value (0..1), absent exactly when the cell is of the UserDefined category (identified precisely by its cell-databook filename's `(custom)` disambiguator) — read straight from the cell-databook's own explicit `mia.origin` YAML field when present, fixed at creation and never re-derived from the folder's current name, filename, or position (so a folder can be freely renamed or moved without touching it). `cell:Cell` carries no link back to its own folder at all — `cell.ttl` has no such property, since there is no folder individual distinct from the cell to hold one. **A folder holds at most one cell-databook, never more** — a folder is a cell exactly when it holds one such matching file (its filename an exact copy of the folder's own name), and a folder with none is just a plain filesystem folder, not a cell at all. Two cells can never share a folder: a `cell:Cell` is self-contained, and letting two cells share a folder would risk a single file in that folder becoming ambiguously part of both. A graph DataBook still carries no field pointing back at its cell at all — the cell is the one that asserts the `members`/`topic` link, and the graph id's `(<containing-cell>)` segment names the cell (the human-readable position) that cell-databook lives in directly, not via any RDF lookup. This keeps a cell's content self-contained (aside from the graph files it references) and independent of tree position, for PDN sync robustness: when a cell is shared between peers (e.g. a `TwoMember` cell between Alice and Bob), each peer can independently rearrange their own tree of cells — moving or renesting their cell under a different parent however they like — without ever touching the shared cell's content or identity, since moving a folder in the tree is a pure filesystem operation with no frontmatter field to edit on either side. The cell's own name, by contrast, is part of that shared content, not a per-peer-independent choice — see APP-BEHAVIOR.md's [Naming, Renaming, and Sharing](APP-BEHAVIOR.md#naming-renaming-and-sharing) section for how a shared name is kept unique within each peer's own tree (renaming, receipt-collision suffixing, and first-receipt auto-naming for two-member cells). The *canonical* side of the split (which classes have reusable starter content) lives entirely at the class level — see `category.ttl`'s `cat:templateCell` and the `cell-templates.ttl` file — there is no separate canonical-instance tree.

**Terminology going forward**: the `cat:Category` class hierarchy (`category.ttl`) is a completely separate tree from a user's own instance tree — it's a recommended pattern (`cell:origin`, `cat:templateCell`) that a cell's tree position may optionally follow, not the tree itself. Describe the user's own instance tree only in terms of **cells** and their **descendant cells** — never "folders" or "categories" — except in `APP-BEHAVIOR.md`'s own section on persisting a cell in the filesystem, where "folder" is the correct literal term for the on-disk implementation detail. A heading, check, or script comment that names a filename/tree-position convention after "Category" (e.g. the retired "Category/Cell DataBook Filename Convention" name) is stale leftover from when a separate `category-databook` file type existed (see the Cell/Category split note above) — fix it to name the cell-level concept it actually describes.

**DataBook IRI convention**: The document `id:` and `graph.named_graph:` always differ by the `#graph` fragment — `named_graph` is always `{id}#graph`. The `databook:id` on a block is a fragment identifier making that block independently addressable as `{id}#{block-id}`. Overview sections always begin with "This graph captures...".

**Peer name pattern** (not hierarchical): All name types (FullName, GivenName, FamilyName, AlternateName) connect directly to a Persona via `ont00001879` (designated by). They are siblings, not nested. Names belong to Personas not to Persons.

**Address history pattern**: `AddressDesignation` links Person → Address → `TemporalInterval`. Open-ended intervals (no `hasEndDate`) indicate current address.

**Named graph scoping of `BFO_0000115`**: When a Social Network individual carries `BFO_0000115 :Paula_Walker`, the triple is intentionally scoped to the enclosing named graph — it refers to Paula Walker *as a person entity*, with graph-specific isolation provided by the DataBook named graph architecture, not by the triple itself. Queries needing graph-specific member data must target the relevant named graphs (e.g. graph 21 + graph 5) rather than querying the full merged dataset. Do NOT change the range of `BFO_0000115` to a document IRI (breaks BFO semantics — range must be a continuant, not a document), and do NOT introduce graph-specific person individuals (reintroduces the complexity that removing the layered Persona model eliminated). RDF-star annotation is a valid future option if tooling matures.

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

Before committing any change to `persona.ttl`, increment the **minor version number** in that file's `owl:versionInfo` annotation and update the description to summarise the change. For example:

```
owl:versionInfo "Version 3.0.3 - added social network"@en
```
becomes:
```
owl:versionInfo "Version 3.0.4 - added birth date"@en
```

`graph.ttl`, `cell.ttl`, and `category.ttl` do not carry `owl:versionInfo` at all — these three files are evolving too rapidly right now for a change-log annotation to be worth maintaining. Do not add it to any of the three. They still carry `owl:versionIRI` and `dc:date`; bump those on a real change if convenient, but there's no change-history text to update alongside them. `organization.ttl`, `pdn-identity.ttl`, `cell-templates.ttl`, and `persona-templates.ttl` are unaffected by this — they still carry `owl:versionInfo` and should keep it updated on a real change, the same way `persona.ttl` does.

**`owl:versionInfo` describes only the current version — no embedded history, ever**: `persona.ttl`, `organization.ttl`, `pdn-identity.ttl`, `cell-templates.ttl`, and `persona-templates.ttl` each keep `owl:versionInfo` as a single bare `"Version X.Y.Z - <description of this change only>"@en` string. **Never embed history in it** — replace the whole string with the new version and its own description on each bump; never append the outgoing description in parentheses. Git carries the changelog now — the same reasoning that governs `rdfs:comment`/block-comment text in every `.ttl` file (describe current semantics only, never narrate how it got that way) applies to `owl:versionInfo` too.

**No `owl:versionInfo` in any `*-shacl.ttl` file, ever**: `cell-shacl.ttl`, `graph-shacl.ttl`, `persona-shacl.ttl`, `organization-shacl.ttl`, `pdn-identity-shacl.ttl`, `cell-templates-shacl.ttl`, and `shacl/jscontactcard-shacl.ttl` carry no `owl:versionInfo` — this applies uniformly to every SHACL shapes file regardless of whether its paired main ontology file still carries `owl:versionInfo` (`persona-shacl.ttl` does not, even though `persona.ttl` itself does). Every one of these files still carries `owl:versionIRI` and `dc:date`; bump those on a real change, but do not add `owl:versionInfo` to any of them — their `rdfs:comment`s describe only current semantics, same as the main ontology files.

## Integrity Checks

Files inside any directory named `under-development/` (at any depth) are works-in-progress and must be **excluded from all integrity checks** below.

After any change to a graph (its `mia.graphs` entry or `### Graph NN` body section) or a cell DataBook, verify the following.

**Check 1 — Diagram ↔ files ↔ EXAMPLE.md coverage**: Every numbered graph circle in any of the 11 cell diagrams (`example/images/`) must have (a) a corresponding embedded graph section — a `mia.graphs` entry plus its `### Graph NN` body section — inside a cell-databook file under `example/Cells/`, and (b) a row in one of the tables in the **Graphs** section of `EXAMPLE.md`. Conversely, every row in those tables must correspond to a numbered circle in a diagram and an embedded graph that actually exists. If a circle exists in a diagram but has no embedded graph or `EXAMPLE.md` row, create them to match the diagram.

**Check 2 — Graph id naming convention**: Every `mia.graphs[].id` value's local-name (the string after the final `/`) — across all cell-databooks in `example/Cells/` — must follow the flat pattern `graph-<NN>`, where `<NN>` is a zero-padded two-digit number matching the graph's own diagram label, `### Graph NN` body heading, and `<a id="graph-NN">` anchor. If an id does not match this pattern, flag it rather than silently renaming — `mia.graphs[].id` also doubles as the graph's own named-graph identity (`{id}#graph`), so changing it is a bigger operation than a file rename ever was.

**Check 3 — `mia.graphs` ↔ `members`/`topic` consistency**: Since a graph lives physically inside its owning cell-databook file, containment is structural rather than a cross-file reverse lookup — but the two lists that record it independently (`mia.members`/`mia.topic`, and `mia.graphs`) must still agree exactly. For every cell-databook under `example/Cells/`, the set of ids across `mia.members`+`mia.topic` and the set of `mia.graphs[].id` values must be identical — every linked id has a matching `graphs` entry supplying its metadata, and every `graphs` entry is linked from one of the two lists. `mia.members`/`mia.topic` entries are written as the graph id's bare local name (e.g. `"graph-22"`) rather than the full `http://www.example.org/mia/graphs/...` IRI — that base is constant across every graph id in the dataset and repeating it on every list entry is pure redundancy, since a graph only ever lives inside the one cell-databook file whose own `members`/`topic` reference it (see [Graph ID Naming Convention](#graph-id-naming-convention)); `mia.graphs[].id` itself keeps the full IRI, since that value also doubles as the graph's own named-graph identity (`{id}#graph`). This check normalizes both sides to the bare local name before comparing, so it still catches a real mismatch and isn't fooled by that form difference. Run:

```python
import glob, re, yaml

GRAPHS_BASE_RE = re.compile(r'^https?://www\.example\.org/mia/graphs/')

def frontmatter(path):
    text = open(path, encoding='utf-8').read()
    m = re.match(r'^---\n(.*?)\n---', text, re.DOTALL)
    return yaml.safe_load(m.group(1)) if m else None

def local_name(v):
    return GRAPHS_BASE_RE.sub('', v)

errors = 0
for path in sorted(glob.glob('example/Cells/**/*.databook.md', recursive=True)):
    if 'under-development' in path.split('/'):
        continue
    fm = frontmatter(path)
    if not fm or fm.get('type') != 'cell-databook':
        continue
    mia = fm.get('mia', {}) or {}
    linked_ids = set()
    for field in ('members', 'topic'):
        val = mia.get(field)
        if val:
            linked_ids.update(local_name(v) for v in (val if isinstance(val, list) else [val]))
    graph_ids = {local_name(t['id']) for t in (mia.get('graphs') or []) if isinstance(t, dict) and t.get('id')}
    missing = linked_ids - graph_ids
    unlinked = graph_ids - linked_ids
    if missing:
        print(f'{path}: members/topic reference(s) with no matching mia.graphs entry: {sorted(missing)}')
        errors += 1
    if unlinked:
        print(f'{path}: mia.graphs entry/entries with no members/topic link: {sorted(unlinked)}')
        errors += 1
if not errors:
    print('All cell-databooks: mia.graphs entries and members/topic links are in 1:1 correspondence.')
```

If a mismatch appears, add the missing `mia.graphs` entry (or `### Graph NN` body section) or the missing `members`/`topic` reference — whichever side is incomplete.

**Check 4 — No orphan Persons**: Every `persona:Person` individual other than `:Self` must be reachable via `BFO_0000115` (has member part) from a Social Network individual linked to another `persona:Person` via `persona:hasSocialNetwork`. `:Self` is always the root and needs no incoming link. Since graphs are embedded graph sections across every cell-databook under `example/Cells/**`, this check's scope is the merged Tier 1 data graph, which spans every embedded graph. **Exception**: a `persona:Person` referenced only via a professional/service-designation property (e.g. `persona:hasPrimaryCarePhysician`) rather than social-network membership is exempt — it represents a service relationship (e.g. a physician), not a social connection, so it has no social network to be reachable from. Example: `:Jane_Starostina` (graph #25), Paula Walker's primary care physician.

**Check 5 — Validation command completeness**: The `## Validation` section of `EXAMPLE.md` must document two tiers. Tier 1 uses five steps: (1) a `find example -name "*.databook.md"` loop using `databook extract` to extract turtle content and produce a merged turtle file of all graph data (excluding `under-development/`) — directory-agnostic, so it naturally concatenates every embedded graph within a cell-databook, which is exactly what Tier 1 wants; (1b) `python3 yaml-to-rdf.py` to synthesize `cell:`/`graph:` triples from each cell-databook's own `mia.` YAML frontmatter (including its `mia.graphs` list; a graph's `claimant`/`subject` live there, not in a separate graph-databook file) — there is no `cat:` synthesis at all, since a folder's tree position is purely a filesystem fact with no RDF individual to synthesize; the only surviving classification fact, `cell:origin`, is read directly from each cell-databook's own explicit `mia.origin` field, no reverse-matching involved. `databook extract` only pulls fenced Turtle blocks, which cell DataBooks don't carry, so without this step `cell:Cell` individuals and `g:SCGraph`'s subject/claimant never reach the merged graph and `cell-shacl.ttl`/`graph-shacl.ttl`'s `:SCGraphShape` never fire against real instance data; (2) a `riot` merge of both extracted files with all application ontology TTL files and the foundation ontologies listed explicitly from `project_files/` — `cell-templates.ttl` is deliberately excluded from this merge (unlike Tier 2's per-file base merge, below): its 5 template individuals are generic, reusable content bound to no real person, so they can't sensibly carry `cell-shacl.ttl`'s required `cell:members`/`cell:creator`, and are instead validated only via `cell-templates-shacl.ttl` in Tier 2; (3) a `grep -v owl:imports` on `persona-shacl.ttl`, `graph-shacl.ttl`, `cell-shacl.ttl`, and `organization-shacl.ttl` to collect shapes (`shacl/jscontactcard-shacl.ttl` and `cell-templates-shacl.ttl` are excluded here — they target document classes and would fire incorrectly on all individuals when applied to merged data; `pdn-identity-shacl.ttl` is also excluded — its ontology, `pdn-identity.ttl`, isn't part of the Step 2 merge, since nothing in the active ontology stack references an `identity:` term); (4) a `shacl validate` call. Tier 2 lists explicit per-graph `extract-graph.py` + `riot` + `shacl validate` commands for each template graph paired with its owning cell-databook file and its shapes source — `cell-templates-shacl.ttl` directly for BirthCertificate/DriversLicense/Passport/MedicalAppointment/PetMedications, or `shacl/jscontactcard-shacl.ttl` directly for JSContactCard (both are plain `.ttl` files, not DataBook fragments). `extract-graph.py` (not `databook extract`) is required here because a cell-databook may embed more than one graph — e.g. the MedicalAppointment case lives in a three-graph cell, so a whole-file extraction would wrongly pull in its two sibling graphs' data. Tier 2 does not need `yaml-to-rdf.py` since it validates one graph's isolated Turtle directly, not category/cell YAML frontmatter. If the commands change, update `EXAMPLE.md` to match.

**Check 6 — PNG file location**: The diagram PNG for every embedded graph (each `mia.graphs` entry across every cell-databook under `example/Cells/`) must be stored directly in `example/graphs/images/` (flat, no subfolders — not `images/example/`) — this location is unchanged by the graph/cell merge; only the graphs' own `.databook.md` files were removed, not this images directory. Files in `under-development/` are excluded. **Exempt**: the minimal `:Self`-stub `members` graph Check 21 requires on a purely organizational scaffold cell — one with no rendered diagram box at all, per Check 10h/Check 1's scope — needs no diagram PNG and no `EXAMPLE.md` row of any kind, not even `*(todo)*` (Check 7); it was never intended to be visualized, unlike every other embedded graph. `example/Cells/Cells(person).databook.md`'s `graph-38` and the other scaffold-cell stub graphs (e.g. `graph-52` on `Work`) fall under this exemption.

**Check 7 — PNG filename convention**: Every diagram PNG in `example/graphs/images/` must use the same base filename as the graph's own `mia.graphs[].id` local-name (the string after the final `/`), with `.png` appended. For example, id local-name `graph-14` → `graph-14.png`. If the PNG does not yet exist, the `EXAMPLE.md` Diagram cell must be marked `*(todo)*` rather than left blank — except for a scaffold-cell stub graph covered by Check 6's exemption, which gets no `EXAMPLE.md` row at all, not even `*(todo)*`.

**Check 8 — No broken image links in `README.md`/`EXAMPLE.md`/`APP-BEHAVIOR.md`**: Every PNG path referenced in `README.md`, `EXAMPLE.md`, or `APP-BEHAVIOR.md` (both `<img src="...">` tags and `[view](...)` table links) must resolve to an actual file on disk. Run:

```bash
python3 -c "
import re, os
content = open('README.md').read() + open('EXAMPLE.md').read() + open('APP-BEHAVIOR.md').read()
pngs = [m.group(1) for m in re.finditer(r'src=[\"\\'](.*?\.png)[\"\\']', content)]
pngs += [m.group(1) for m in re.finditer(r'\]\((example/[^\s\"\']+\.png)\)', content)]
missing = [p for p in sorted(set(pngs)) if not os.path.exists(p)]
[print('MISSING:', p) for p in missing] or print('All PNG refs OK')
"
```

If any `MISSING:` lines appear, either add the file or update the link.

**Check 9 — Cell id naming convention**: This check applies only to `example/Cells/` — the user's own instance tree — since there is no separate canonical-instance file tree: the canonical tree is the `cat:Category` class hierarchy in `category.ttl` itself, with class-level templates in `cell-templates.ttl`. A cell-databook's `id:` is deliberately independent of its filename — the filename stays the folder's own verbatim name per the Cell DataBook Filename Convention, but the `id:` value is a flat, opaque, globally-unique identifier, following the same reasoning and pattern as the [Graph ID Naming Convention](#graph-id-naming-convention)'s `graph-<NN>`: encoding the folder's name and catType into the id would risk a collision the moment two different folders elsewhere in the tree shared both a name and a catType, and nothing in the repo actually depends on the id's string *structure* — it's purely a self-contained RDF subject identifier for that one cell, never cross-referenced by another cell, a graph, or a catalog file. Every `id:` value — across all cell-databooks in `example/Cells/` — must follow the flat pattern `http://www.example.org/mia/cells/cell-<NN>`, where `<NN>` is a zero-padded two-digit number, assigned once at creation and never reused or renumbered. Every `<NN>` must be globally unique across the whole tree. Run:

```python
import glob, re

pattern = re.compile(r'^http://www\.example\.org/mia/cells/cell-(\d{2})$')
seen = {}
errors = 0
for path in sorted(glob.glob('example/Cells/**/*.databook.md', recursive=True)):
    if 'under-development' in path.split('/'):
        continue
    text = open(path).read()
    m = re.search(r'^id:\s*(\S+)', text, re.MULTILINE)
    fid = m.group(1).strip() if m else ''
    pm = pattern.match(fid)
    if not pm:
        print(f'MALFORMED  {path}  id={fid!r} does not match http://www.example.org/mia/cells/cell-<NN>')
        errors += 1
        continue
    nn = pm.group(1)
    if nn in seen:
        print(f'DUPLICATE  cell-{nn}  used by both {seen[nn]!r} and {path!r}')
        errors += 1
    else:
        seen[nn] = path
print('Check 9: OK' if errors == 0 else f'Check 9: {errors} issue(s) found')
```

If a malformed id is found, fix it to match the pattern. If a duplicate `<NN>` is found, assign the newer cell the next unused number — never renumber an existing cell's id, since (like a graph id) it may already be referenced by an external peer over the PDN. This rule has no exceptions for `example/Cells/`, fictional as its data is — treat every id there exactly as if a real external PDN peer might already hold a reference to it.

Note: this check's `^id:\s*(\S+)` regex is anchored at true line-start with no leading whitespace, so it only ever matches a file's own top-level `id:` line — a nested, indented `mia.graphs[].id` value never matches this anchor and is intentionally out of scope here (a graph's `id` is not expected to relate to its owning cell file's name at all; see Check 2 for that). This imposes a requirement on any script that writes `mia.graphs`: never emit an unindented `id:` at column 0.

**Check 10 — Example cell diagrams are authoritative**: The 11 cell diagrams in `example/images/` are the authoritative source of truth for the example cell tree. When any discrepancy is found between a diagram and the DataBook files, the diagram wins — update the DataBooks to match, not the other way around. Each diagram box corresponds to a cell in `example/Cells/` (a folder holding its one `cell-databook` directly inside it, box label = the cell's own folder name, mirrored in its cell-databook's `title:`). After any change to `example/Cells/` DataBooks or to the 11 diagrams, verify all of the following:

- **10a — Every cell box has a cell DataBook**: Every cell box shown in any of the 11 diagrams must have a corresponding cell in `example/Cells/` whose cell-databook's `title:` matches the box label. If a box has no DataBook, create the cell (folder + cell DataBook).

- **10b — Every cell DataBook has a diagram box**: Every cell's cell-databook in `example/Cells/` (except the top-level `example/Cells/` folder's own cell-databook, `Cells(person).databook.md`, which is the invisible root) must appear as a visible box in at least one of the 11 diagrams. If a DataBook has no corresponding box, either add it to the appropriate diagram or delete that cell's DataBook.

- **10c — Solid graph circles match DataBook links**: Every solid (filled) graph circle attached to a cell box indicates a real graph link. The cell-databook co-located in that box's own folder must carry a corresponding `members` or `topic` value pointing to the graph DataBook IRI. A dashed (empty) circle indicates an unfilled slot — the cell DataBook must NOT have a link for that slot.

- **10d — Numbered graph circles have matching embedded graphs**: Every numbered graph circle (e.g. `[10]`, `[17]`) shown in a diagram must correspond to a `mia.graphs` entry (equivalently, a `### Graph NN` body section) in some cell-databook under `example/Cells/` whose id contains that number (e.g. `(10)`, `(17)`).

- **10e — Child arrows match folder nesting**: Every downward child arrow from cell box A to cell box B in a diagram must correspond to B's folder being a direct filesystem subfolder of A's folder (i.e. B is a descendant cell of A) — child links are derived purely from folder nesting, not any `child:` YAML field. Conversely, every direct-subfolder relationship between two cells must be reflected by a visible child arrow in the diagram.

- **10f — Cell box border style matches `mia.memberCount`**: Per the Key legend, a cell box is drawn with one of three border styles — square corners with a single border ("1 Member Cell"), rounded corners with a single border ("2 Member Cell"), or rounded corners with a double/bold border ("3+ Member Cell") — corresponding to `cell:OneMember`, `cell:TwoMember`, and `cell:ThreePlusMember` respectively (these display strings are `cell:label` values, matching the diagrams' wording). The distinguishing feature between a One- and a Two-Member cell is corner rounding, not border doubling — only the 3+-Member style doubles the border. The border style shown for a cell box must match the actual `mia.memberCount` value of the cell-databook co-located in that box's own folder. This is a visual check (no script) — e.g. `people2.png`'s "Jane Starostina" box is drawn with square corners and a single border ("1 Member Cell"), which must match `Jane-Starostina(primary-care-physician).databook.md`'s `mia.memberCount: "cell:OneMember"`; `pets.png`'s "Medications" box is drawn with rounded corners and a single border ("2 Member Cell"), matching its `mia.memberCount: "cell:TwoMember"`.

- **10g — Black parenthetical origin-label text matches `cell:origin`'s class label**: As the second line of a cell box's content (there is no blue Subject text above it any more — cell diagrams don't render a cell's subject at all, since it's derivable from the graph circles already drawn rather than an independently stored fact; see README's Representative Cells section), a cell box may carry a black parenthetical giving its `cell:origin` class's `rdfs:label` (from `category.ttl`) in human-readable form. It follows the exact same compression rule as the Cell DataBook Filename Convention's `<local>(<catType>)` filename form: shown only when that label differs from the box's own folder-name label, and omitted entirely when the two are identical. This text must match the co-located cell-databook's actual `mia.origin` class's `rdfs:label`, verbatim — no more and no fewer words, never invented or abbreviated further. This is a visual check (no script) — e.g. `companies.png`'s "Google" and "ATT" boxes both show `(Companies)`, matching their shared `mia.origin: "cat:Companies"` (label "Companies"); `gov-state.png`'s "Texas Vital Records" and "California DMV" boxes show `(Birth Certificate)` and `(Drivers License)`, matching `cat:BirthCertificate`'s and `cat:DriversLicense`'s labels; `misc.png`'s "Things" box shows no parenthetical at all, correctly compressed since `cat:Things`'s label already equals the folder name "Things".

- **10h — Black curly-brace `{NN}` label matches the cell's own `cell-<NN>` id**: As the last line of a cell box's content (immediately below the Origin text, or combined with it on one line, e.g. `(SSN) {6}`), a cell box carries a small black `{NN}` label in curly braces — the cell's own number (a bare scaffolding folder with no rendered content box, e.g. `Work`/`Acme`/`Employees`, carries none — deliberately: even though every one of these scaffolding cells carries real (stub) member content, that stub is intentionally not visualized as a content box, so the box still shows no border style, Origin text, `{NN}`, or graph circles — a visual simplification, not a sign the cell lacks content). Wherever `{NN}` appears, it must equal the zero-padded two-digit `<NN>` from the co-located cell-databook's own `id: http://www.example.org/mia/cells/cell-<NN>` (see Check 9). Don't confuse this with the numbered graph circles' `[NN]` labels (Check 10d) — those are graph numbers in square brackets attached to a circle; this is the cell's own number in curly braces attached to the box itself. This is a visual check (no automated OCR), but the script below prints every folder's actual `cell-<NN>` for quick cross-reference against whichever diagram is being checked — e.g. `people.png`'s "Bob Johnson" box shows `{16}` and its "Fred Flintstone" box shows `{17}`; `people2.png`'s "Paula Walker" (Immediate Family) box shows `{12}`, "Health & Wellness" shows `{13}`, "Jane Starostina" shows `{14}`, and "Medical Appointment" shows `{15}`; `companies.png`'s "Google"/"ATT" boxes show `{3}`/`{2}`; `finances.png`'s "Citibank" box shows `{4}`; `gov-state.png`'s "Texas Vital Records"/"California DMV" boxes show `{10}`/`{9}`; `gov-federal.png`'s "Social Security Administration"/"Department of State" boxes show `{6}`/`{5}`; `gov-municipality.png`'s "Boston"/"Paradise" boxes show `{7}`/`{8}`; `misc.png`'s "Things" box shows `{11}`; `affiliations.png`'s "Boston Hub Society" box shows `{1}`; `work.png`'s "Paula"/"Alice Walker" boxes show `{19}`/`{18}`; `pets.png`'s "Ginger" box shows `{41}` and its "Medications" box shows `{40}`. Run:

```python
import glob, re

for path in sorted(glob.glob('example/Cells/**/*.databook.md', recursive=True)):
    if 'under-development' in path.split('/'):
        continue
    text = open(path).read()
    m = re.search(r'^id:\s*http://www\.example\.org/mia/cells/(cell-\d{2})', text, re.MULTILINE)
    if m:
        print(f'{m.group(1)}  {path}')
```

- **10i — Fill color and folder-name-text color match real data**: Every cell across all 11 diagrams carries exactly two independent, mechanically-checkable colors, matching Check 10a's Person/Organization/Custom fill-swatch legend (see Check 15's identical rule for `cat-cell-graph.png`): a **fill** color, applied to the cell's own DataBook box (a separately-drawn folder icon, where a diagram draws one, stays plain white and never carries fill — see Check 20's `folder-mapping.png`) — tan if the folder's `mia.origin` resolves to `cat:Person`, light blue if `cat:Organization`, purple/Custom if the cell has no origin at all — and a folder-**name-text** color (green/"Predefined" if the folder's `title:` equals the origin class's own `rdfs:label` verbatim, plain black/"User-defined" otherwise — always black for a no-origin/Custom cell). This is a visual check (no automated pixel/OCR comparison) — use Check 20's script (identical rule, just applied to a different set of diagrams) to compute the correct fill/text color for every real folder and cross-reference against whichever diagram is being checked — e.g. `people.png`: "People"/"Others" tan fill + green text; "Bob Johnson"/"Fred Flintstone" tan fill + black text; `work.png`: "Paula"/"Alice Walker" light-blue fill + black text; `people2.png`: "Paula Walker"/"Jane Starostina" tan fill + black text; "Medical Appointment" tan fill + green text (folder name "Medical Appointment" now matches origin `cat:MedicalAppointment`'s own label verbatim); `pets.png`: "Pets"/"Health"/"Medications" tan fill + green text (folder name matches origin label), "Ginger" tan fill + black text (origin `cat:Pets` label "Pets" ≠ folder name "Ginger"). No real example cell currently uses the Custom (no-origin, `(custom)` filename) case — every current cell has an origin — so no example diagram box is expected to show purple fill yet.

The 11 diagrams are: `example/images/people.png`, `example/images/people2.png`, `example/images/work.png`, `example/images/companies.png`, `example/images/finances.png`, `example/images/gov-state.png`, `example/images/gov-federal.png`, `example/images/gov-municipality.png`, `example/images/misc.png`, `example/images/affiliations.png`, `example/images/pets.png`. There is no `health.png` — its content, e.g. Health & Wellness/Medical/Provider, lives in `people2.png` instead. `pets.png` shows both the "Ginger" cell (cell-41, `{41}`, graphs `[36]`/`[37]`) and the "Medications" cell (cell-40, `{40}`, graphs `[32]`/`[33]`/`[57]`) as separate content boxes under the `Pets → Ginger → Health → Medications` folder nesting.

**Check 11 — Physical folder structure IS the tree of cells in `example/Cells/`**: This check applies only to `example/Cells/` — the user's own instance tree — since there is no separate canonical-instance file tree to mirror. There is no `mia.child`/`mia.cell` YAML list to cross-check the tree against either, so this check has no independently-asserted list to "mirror" at all; it collapses to a pure filesystem sanity check with no YAML frontmatter parsing at all. A folder is a **cell** ("marker dir") iff it directly contains exactly one `*.databook.md` file (the only DataBook type in a user's instance tree is `cell-databook`, so no `-cell` marker is needed to identify one) — that file is simultaneously the cell's real (or placeholder) content and its tree-node marker (cell.ttl's folder ownership boundary rule). A folder can never legally hold more than one cell-databook: a `cell:Cell` is self-contained, and letting two cells share a folder would risk a single file in that folder becoming ambiguously part of both — this check flags any such folder as an error. A plain filesystem folder with no cell-databook of its own is not a cell at all — that word stays reserved for a folder that does have one. Cell naming is not standardized — a cell's own folder name may be the category's display label, a role-based label, or anything else — but a cell-databook's own filename is always the folder's exact verbatim name (see the Cell DataBook Filename Convention), so this check's per-folder marker test and its filename root are one and the same string. A bare, marker-less pass-through directory between two marker dirs is legal, matching README.md's own definition of a "regular filesystem folder" ("A folder without a matching cell DataBook is simply a regular file system folder, not a cell — **even if it contains nested cells of its own**"): such a folder is legal anywhere in the tree, including between two marker dirs, as long as it isn't otherwise empty (i.e. something beneath it eventually has a cell-databook). Run:

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

    # (A bare, marker-less pass-through directory between two marker dirs is
    #  legal — README.md's own definition of a "regular filesystem folder"
    #  explicitly allows this ("even if it contains nested cells of its
    #  own") — so no ancestor-chain check is needed here.
    #  Rule 1 below (empty/placeholder detection) already covers the only
    #  real failure mode: a bare folder with nothing but other bare folders
    #  under it, all the way down.)

    # 1. Any subfolder with no cell-databook anywhere under it at all is
    #    either an empty/placeholder folder (flag, don't delete) or plain
    #    non-cell content living inside a cell's own folder (fine,
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

    # 2. A cell's folder holds exactly one cell-databook — a cell is
    #    self-contained, so more than one sharing a folder is always an
    #    error (it risks a single file ambiguously belonging to both).
    for d, cells in sorted(cell_counts.items()):
        if len(cells) > 1:
            errors.append(f'TOO MANY CELLS: {d!r} has {len(cells)} cell-databooks (expected exactly 1): {sorted(cells)}')

    return errors

for root in ['example/Cells']:
    errors = check_tree(root)
    print(f'{root}: ' + (f'{len(errors)} issue(s) found:' if errors else 'OK — folder structure IS the tree of cells, no gaps.'))
    for e in errors:
        print(' -', e)
```

If a `TOO MANY CELLS` issue is found, move the extra file(s) out to their own new folder — a folder may hold only one cell-databook, so a second cell belongs in its own new folder, not alongside the first. An empty/placeholder folder is not necessarily an error — flag it to the user rather than deleting it, since it may be a deliberate placeholder for content not yet added. Cell-databook files routinely carry substantial body content (one `### Graph NN` section per embedded graph) — this is expected and not itself a violation of this check, which only validates folder nesting, not file size or content.

**Check 12 — `cell.ttl` matches `images/cell-ontology/cell.png`**: `Cell` shows only `origin` (to a `cat:Category` box, drawn **0..1**, matching `cell:origin`'s actual cardinality). `cell:origin`'s range is the classificatory `cat:Category` — there is no tree-position class for it to be confused with, so it does not conflict with `cell:Cell`'s "no link to a tree position" design (see `cell:Cell`'s own `rdfs:comment`) — it records what kind of thing a cell is, not where it lives, and needs no `owl:imports category.ttl` (referenced by name only, mirroring `cell:creator`'s identical pattern). The diagram shows three arrows off `Cell` with no counterpart in `cell.ttl` — `note` (to a placeholder box, `(markdown file) 1..1`), `attachment` (to a placeholder box, `(file) 0..N`), and `chat` (to a placeholder box, `(a chat stream) 0..1`) — this is a deliberate, accepted exception to 12a/12b below: README.md already describes all three properties' intended semantics (see the Cell Details section) as planned, but `cell.ttl` itself has no `cell:note`/`cell:attachment`/`cell:chat` declaration yet — none of the three is ever reified as a triple in any real graph. `Cell` (abstract, blue) carries `origin` only (plus the still-open `note`/`attachment`/`chat` arrows above). `Cell` splits into two disjoint kinds (`owl:disjointWith` — a cell is always exactly one, never both): `TemplateCell` (abstract, blue, a reusable class-level template) carries `isTopicCell` (to an `xsd:boolean` box) and `templateShape` (to a `sh:NodeShape` box, 0..1); `MemberCell` (abstract, blue, an actual cell instantiated in a user's own tree) carries `members` (to a `g:SCGraph` box, 1..N, cardinality varying by member count — see Check 17), `shape` (to a `sh:NodeShape` box, 0..1), `creator` (to a union of `p:Person`/`o:Organization`, 1..1), and `memberCount` (to `OneMember`/`TwoMember`/`ThreePlusMember`, 1..1). There is no `subject` arrow off `MemberCell` — `cell:subject` was removed (a cell's subject is now derived from `members`/`topic` rather than stored). Three classes hang directly off `MemberCell` as its children: `OneMember` (concrete, black, no arrows of its own), `MultiMember` (abstract, blue, no arrows of its own — further splitting into `TwoMember`/`ThreePlusMember`, neither of which carries arrows either), and `TopicCell` (concrete, black — a mixin that combines with whichever of `OneMember`/`TwoMember`/`ThreePlusMember` a real cell already has, not a fourth alternative to them), which alone carries `topic` (to a `g:SCGraph` box, 1..N — required, at least one, no upper bound, once a cell is typed `TopicCell` at all). `TemplateCell` has no subclasses of its own, and no individual is ever typed both `TemplateCell` and `MemberCell` (or any `MemberCell`-lineage class, including `TopicCell`) — every template individual in `cell-templates.ttl` is typed solely `TemplateCell`. No arrow points from `Cell`, `TemplateCell`, or `MemberCell` to any tree-position box at all — `cell:origin`'s arrow points to `cat:Category` instead, the classificatory hierarchy. This diagram is the ontology-level (not example-tree) picture of `cell:Cell`'s structure — the member-composition hierarchy and its content-linking properties. Unlike Check 10 (example diagrams, where the diagram always wins), this check does not presume which side is authoritative when the two disagree — surface the discrepancy and ask:

- **12a** — every property arrow shown off `Cell` (`origin`) has a corresponding `cell:` property in `cell.ttl` with `rdfs:domain cell:Cell` (the diagram's `note`, `attachment`, and `chat` arrows are the three accepted exceptions — see above: all three are planned properties, not yet added to `cell.ttl`). Every arrow off `TemplateCell` (`isTopicCell`, `templateShape`) has `rdfs:domain cell:TemplateCell`; every arrow off `MemberCell` (`shape`, `creator`, `memberCount`, `members`) has `rdfs:domain cell:MemberCell`; the one arrow off `TopicCell` (`topic`) has `rdfs:domain cell:TopicCell`. No `subject` arrow should appear off `MemberCell` at all — `cell:subject` doesn't exist (see Check 12's own note above). `OneMember` and `MultiMember` should show no arrows of their own — neither carries a property. Each arrow's target type in the diagram must match the property's `rdfs:range` — `members`'s and `topic`'s are both `g:SCGraph`, `isTopicCell`'s is `xsd:boolean`, `creator`'s is the union of `p:Person`/`o:Organization`, `memberCount`'s is `cell:MemberCell` itself (value is the concrete subclass, not `xsd:string`), `origin`'s is `cat:Category` itself (value is the concrete leaf subclass, e.g. `cat:Others`, not `xsd:string` — the same class-value-punning pattern as `memberCount`), `templateShape`'s and `shape`'s are both `sh:NodeShape` — two separate arrows from two different boxes (`TemplateCell` vs `MemberCell`) to what may be drawn as the same target, since they're two distinct properties, not one property under two names. No `note` arrow should appear off `Cell` at all.
- **12b** — every `cell:` property defined in `cell.ttl` appears as an arrow in the diagram, under the box matching its domain — `Cell`, `TemplateCell`, `MemberCell`, or `TopicCell` (catches new properties added to the ttl but never drawn, or drawn under the wrong box).
- **12c** — the class hierarchy `Cell` → `TemplateCell`/`MemberCell` (both abstract, `owl:disjointWith` one another), and separately `MemberCell` → `OneMember`, `MemberCell` → `MultiMember` (abstract) → `TwoMember`/`ThreePlusMember`, and `MemberCell` → `TopicCell`, shown in the diagram matches `cell.ttl`'s actual `rdfs:subClassOf` relationships (by class local name, not just position). `OneMember`, `MultiMember`, and `TopicCell` must all be drawn as direct children of `MemberCell`, not of `Cell` — `TopicCell` in particular is a mixin sibling of `OneMember`/`MultiMember`, not a fourth member-count alternative folded into that same branch.
- **12d** — `cell.png` draws only the bare class local names (`OneMember`, `TwoMember`, `ThreePlusMember`, `TopicCell`) as box labels; no `cell:label` display string appears anywhere in this diagram. `cell:label` wording is instead verified where it's actually drawn — in the 11 example diagrams (Check 10f) and in `cat-cell-graph.png`/`images/folder-mapping.png`'s border-style legend entries (Checks 15/20). `cell:label` itself is a real class-level default display name defined in `cell.ttl` — `Cell`, `TemplateCell`, `MemberCell`, and `MultiMember` are all abstract and carry no `cell:label` of their own; `TopicCell`, though concrete, carries no `cell:label` either, since it's never solely responsible for a cell box's border style (Check 10f) — that's still driven entirely by the cell's member-count class.

**Check 13 — `graph.ttl` matches `images/graph-ontology/graph.png`**: The diagram shows `Graph`/`SCGraph`. `Graph` shows only `template` (targeting `p:PersonaTemplate`, matching `g:template`'s actual `rdfs:range`); `SCGraph` (subClassOf `Graph`) shows `subject` (targeting `xsd:anyURI` — any resource IRI, not necessarily `p:Person`/`o:Organization`) and `claimant` (targeting `p:Person`/`o:Organization`, not `i:PDNidentifier`) — no `about-by` arrow. No leaf subtype boxes appear below `SCGraph` — `SCGraph` has no subclasses. This diagram is the ontology-level picture of `g:Graph`'s structure. After any change to `graph.ttl` or to this diagram, verify:

- **13a** — every property arrow shown off `Graph` in the diagram (`template`) has a corresponding `g:` property in `graph.ttl` with `rdfs:domain g:Graph`, and its target type matches the property's `rdfs:range`.
- **13b** — every property arrow shown off `SCGraph` in the diagram (`subject`, `claimant`) has a corresponding `g:` property with `rdfs:domain g:SCGraph`; `claimant`'s target in the diagram must match its actual `rdfs:range` — a union of `p:Person`/`o:Organization`, not `i:PDNidentifier`; `subject`'s target must match its actual `rdfs:range` — any resource IRI (`xsd:anyURI`), not a Person/Organization union. No `about-by` arrow should appear — `graph.ttl` defines no such property.
- **13c** — every `g:` property with domain `g:Graph` or `g:SCGraph` defined in `graph.ttl` appears in the diagram under the correct box (catches new properties added to the ttl but never drawn, or drawn under the wrong box).
- **13d** — no subclasses appear below `SCGraph` — `graph.ttl` defines none. If any appear here or in `graph.ttl`, reconcile them.

**Check 14 — `category.ttl` matches `images/category-ontology/category.png`**: This diagram is the ontology-level picture of `cat:Category`'s structure alone: `cat:Category` (abstract, blue) carries only `templateCell` (to a `cell:TemplateCell` box) — an annotation asserted directly on the class, not an instance; `cat:Person`/`cat:Organization` (abstract, blue) are its direct subclasses, each with representative leaf examples (Affiliations/People/Work under Person; Suppliers/People (org) under Organization). No `Folder`/`CategoryDefined`/`UserDefined` boxes and no `child`/`cell`/`category`/`catType`/`label` arrows should appear anywhere. This diagram does not presume which side is authoritative when the two disagree — surface the discrepancy and ask. After any change to `category.ttl` or to this diagram, verify:

- **14a** — the only property arrow in the diagram is `templateCell`, off `Category`, matching `category.ttl`'s `cat:templateCell` (`rdfs:domain owl:Class` — an annotation asserted on the class itself, not scoped to `cat:Category` specifically at the OWL level; `rdfs:range cell:TemplateCell`). No `catType`, `child`, `cell`, `category`, or `label` arrow should appear anywhere — `category.ttl` defines none of these properties, nor the `Folder`/`CategoryDefined`/`UserDefined` classes they would live on. No `templateShape` arrow should appear either — that's a `cell.ttl` property (see Check 12), never a `category.ttl` one. There must be no `Canonical` box and no `copiedFrom` arrow anywhere — `category.ttl` defines neither.
- **14b** — every `cat:` property defined in `category.ttl` appears as an arrow in the diagram, under the box matching its domain (catches new properties added to the ttl but never drawn, or drawn under the wrong box). This means just `templateCell`.
- **14c** — the class hierarchy `Category` → `Person`/`Organization` (both abstract) and their leaf subclasses, shown in the diagram matches `category.ttl`'s actual `rdfs:subClassOf` and `cell:abstract` values. There is no second tree to check — `category.ttl` defines no `Folder` hierarchy at all.

**Check 15 — `images/cat-cell-graph.png` matches example usage**: The legend is a single box (title "Cell") — there is no longer a separate "Category" legend box. It holds, in order: three fill-color swatches — Person (tan), Organization (light blue), None (Custom) (purple/lavender); a compact two-line folder-name-text formula, "Name = Category or" (blue "Name =", green "Category") / "User-defined + (Category)" (bold black) — green text means the folder's name is copied verbatim from its origin's own `rdfs:label`, black means the user gave it a different name (shown alongside its `(Category)` parenthetical), and a Custom (no-origin) folder's name is always black, never green, since it has no label to match; a green-filled swatch labeled "Claimed by Other" and a dashed/outlined swatch labeled "Claimed by Self"; a circle labeled "Member" and a square labeled "Topic" — **shape**, not fill, is what distinguishes `c:members` from `c:topic` in this diagram, a change from the older circles-only design; fill/outline (green vs dashed-outline) is then layered on independently to show who claimed that graph, so a `c:topic` square can be either color just as a `c:members` circle can; and three cell-box border-style entries — "3+-Member Cell" (rounded corners, bold/double border), "2 Member Cell" (rounded corners, single border), "1 Member Cell" (square corners, single border) — the One-vs-Two distinction is corner rounding, not border doubling; only 3+ doubles the border — matching `cell:ThreePlusMember`/`cell:TwoMember`/`cell:OneMember`'s current `cell:label` values (Check 12d does not cover this, since `cell.png` itself never draws this text; it's verified here and in the 11 example diagrams' own legends, Check 10f, instead). None of the legend's names are OWL classes — `category.ttl` defines no `Folder`/`CategoryDefined`/`UserDefined` class; Custom stays a pure filename/display convention. Every circle/square carries an explicit subject-name label (e.g. "Bob", "Self", "BHS") baked directly into the shape — this is how a viewer still learns who is involved, without a separate Subject annotation. There is no "Subject" heading grouping these any more, and no blue per-box Subject text — a cell box no longer displays its subject at all, since it's derivable from the circles/squares already drawn rather than an independently stored fact (see README's Representative Cells section). This diagram illustrates representative cell/category associations generically, not tied to a specific example instance — six boxes, each with a single-line folder-name header (no separate `catType`/`label` split), fill color on the cell's own box (this diagram draws no separate folder icon at all, unlike `folder-mapping.png` — see Check 20):
  - `Medical Appointment` (tan/`Person` fill, green text — folder name matches origin `(Medical Appointment)`'s own label exactly, two squares "Med. Appt mt." — one green/other-claimed, one white/self-claimed, demonstrating `cell:topic`'s unbounded-above cardinality (Check 18) — plus two circles "Self" (white) and "Bob" (green))
  - `Friends` (purple/Custom fill, black text, no origin at all, shown as `()`, rounded corners/single border (`cell:TwoMember`), two circles: a white "Self" member — the cell's required `members` entry, per Check 21 — and a green "Fred", since Fred is the derived subject but not a member; no squares)
  - `Employee` (light-blue/`Organization` fill, green text — folder name matches origin `(Employee)`'s own label exactly, square corners/single border (`cell:OneMember`), one white "Self" circle, no squares)
  - `Bob Johnson` (tan/`Person` fill, black text — origin `(Others)` ≠ folder name, rounded corners/single border (`cell:TwoMember`), four circles — two white/self-claimed, two green/other-claimed, all four `c:members` link types filled; no squares)
  - `BHS` (tan/`Person` fill, black text — origin `(Affiliations)` ≠ folder name, rounded corners/double border (`cell:ThreePlusMember`), three circles (Self white, Bob green, BHS green — its three `c:members`) plus one green square (BHS's own organization profile, linked via `cell:topic`) — illustrative only, not tied to real cell-01 data (which has no `cell:topic` value at all, see Check 18)
  - `People` (tan/`Person` fill, green text — no origin parenthetical shown, correctly compressed since the origin's label already equals the folder name, square corners/single border (`cell:OneMember`), one white "Self" circle, no squares)

  Each cell box shows no icon of any kind — no folder icon and no separate "note", "attachment", or "chat" icon (see Check 12's `cell:note`/`cell:attachment`/`cell:chat` planned-property note, which concerns `cell.png` only, not this diagram) — just the filled box itself. Re-verify each box's circles/squares remain a valid illustration of the properties and cardinalities described in the Cell and Graph Ontology sections of `README.md` after any change to those properties.

**Check 16 — IRI roots: `mee.foundation/ontologies` for foundational files, `www.example.org` for example data**: Every foundational ontology and SHACL shapes file — `persona.ttl`, `graph.ttl`, `cell.ttl`, `category.ttl`, `cell-templates.ttl`, `pdn-identity.ttl`, `organization.ttl`, `persona-templates.ttl`, their `*-shacl.ttl` companions (including `cell-templates-shacl.ttl`), and the per-template files in `shacl/` — must declare its `owl:Ontology` IRI under `http://mee.foundation/ontologies/`. There is no separate canonical category/cell DataBook tree to check — the canonical tree's IRI roots are covered by `category.ttl`/`cell-templates.ttl` themselves. Every DataBook under `example/Cells/` (excluding `under-development/`) represents Alice's own example instance data, so both its own `id:` and every `mia.graphs[].id` value it carries must be grounded under `http://www.example.org/` — `https://` is deliberately rejected here, not just accepted alongside it, since every identifier in the example tree (cell ids and graph ids alike) was standardized on the plain `http://` scheme for consistency; a stray `https://` is exactly the kind of drift this check exists to catch. Run:

```python
import os, re, glob, yaml

FOUNDATIONAL_TTL = [
    'persona.ttl', 'graph.ttl', 'cell.ttl', 'category.ttl', 'cell-templates.ttl',
    'pdn-identity.ttl', 'organization.ttl', 'persona-templates.ttl',
    'persona-shacl.ttl', 'cell-shacl.ttl', 'graph-shacl.ttl',
    'organization-shacl.ttl', 'pdn-identity-shacl.ttl',
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
        for graph in (fm.get('mia', {}) or {}).get('graphs') or []:
            tid = graph.get('id') if isinstance(graph, dict) else None
            if tid and not any(tid.startswith(p) for p in expected_prefixes):
                print(f'WRONG GRAPH ID ROOT: {path} -> {tid}')
                errors += 1

check_cell_tree_id_roots('example/Cells/**/*.databook.md', ['http://www.example.org/'])

print('OK — no IRI-root violations found.' if errors == 0 else f'{errors} violation(s) found.')
```

If a violation is found, rename the offending file's `owl:Ontology`/`id:` IRI to the correct root, and update every DataBook `shapes:` YAML reference, catalog entry, and cross-reference that pointed at the old IRI to match (see Check 5's Tier 1/Tier 2 validation commands, which also hardcode these IRIs via the `shapes:` mechanism).

**Check 17 — `members` distinct-subject count matches member class**: `cell:members`'s cardinality (cell-shacl.ttl's `:OneMemberShape`/`:TwoMemberShape`/`:ThreePlusMemberShape`) guarantees *enough* graphs per member count, but not that they're graphs *about* the right number of distinct members — a cell could satisfy the count while every graph repeats the same `g:subject` (e.g. two `members` both with `subject: ":Self"` on a `TwoMember` cell). The additional invariant: across all of a cell's `members` (found via the graph's own `subject`, not `claimant`, in that same cell's own `mia.graphs` list, not a separate graph-databook file), the number of **distinct** `g:subject` values must be at least 1 for `cell:OneMember`, 2 for `cell:TwoMember`, and 3 for `cell:ThreePlusMember` — one per member in the relationship. This is not itself an OWL/SHACL-expressible constraint (it requires dereferencing each `members` value's own `subject`, not just counting `members` values), so it's checked here instead. This invariant is also the direct backbone of a cell's derived subject (see Check 18): the distinct `members` subjects this check validates are exactly what a cell with no `topic` derives its subject to be. Run:

```python
import re, yaml, glob

GRAPHS_BASE_RE = re.compile(r'^https?://www\.example\.org/mia/graphs/')

def frontmatter(path):
    text = open(path, encoding='utf-8').read()
    m = re.match(r'^---\n(.*?)\n---', text, re.DOTALL)
    return yaml.safe_load(m.group(1)) if m else None

def local_name(v):
    return GRAPHS_BASE_RE.sub('', v)

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
    # mia.members/topic hold bare graph-id local names; mia.graphs[].id
    # keeps the full IRI (it doubles as the graph's named-graph identity) — normalize
    # both to the local name before looking up.
    graph_subject = {local_name(t['id']): t.get('subject') for t in (mia.get('graphs') or []) if isinstance(t, dict)}
    pt = mia.get('members')
    pt = pt if isinstance(pt, list) else [pt]
    subs = set()
    for tid in pt:
        s = graph_subject.get(local_name(tid))
        if s is None:
            print(f'{f}: graph {tid} not found in mia.graphs, or has no subject')
            continue
        subs.add(s if isinstance(s, str) else tuple(s))
    need = expected[member_count]
    if len(subs) < need:
        violations += 1
        print(f'VIOLATION {member_count} distinct_subjects={len(subs)} need>={need} subs={subs} {f}')
print('All cells satisfy the distinct-subject-count rule.' if violations == 0 else f'{violations} violation(s) found.')
```

If a violation is found, add a `members` entry whose `subject` is a member not yet represented (real content, not a placeholder), or reconsider whether the cell's `mia.memberCount` value is correct (e.g. a service-provider relationship with no true second member may belong as `cell:OneMember` instead of `cell:TwoMember`).

**Check 18 — `topic`'s presence is what types a cell `cell:TopicCell`, and a cell's subject is derived from it plus `members`**: There is no independently-asserted `cell:subject`/`mia.subject` — who or what a cell's relationship is about is computed, not stored, by a simple two-branch rule: **if the cell has any `topic` entries** (i.e. it's typed `cell:TopicCell`), the full set of distinct `g:subject` values among them is the cell's subject (e.g. `Paula-Walker(employee).databook.md`: `memberCount: "cell:OneMember"`, `members` holds Self's own graph (the member), `topic` holds Paula's graph — subject is `:Paula_Walker`; similarly `Med.-App.-Info(medical-appointment).databook.md`, a `cell:TwoMember` cell: `members` holds Carol's and Self's graphs, `topic` holds Paula's graph — subject is `:Paula_Walker`); **otherwise** the subject is the full set of distinct `g:subject` values among `members` — the cell's own active members (e.g. `Bob-Johnson(others).databook.md`, a `cell:TwoMember` cell with no `topic`: subject is `:Self` and `:Bob_Johnson` together; `Boston-Hub-Society(affiliations).databook.md`, a `cell:ThreePlusMember` cell with no `topic`: subject is `:BHS`, `:Bob_Johnson`, and `:Self` together). `cell:topic` is required (at least one value) but unbounded above once a cell is typed `cell:TopicCell` at all (`cell-shacl.ttl`'s `:TopicCellShape`) — every real example cell today happens to carry exactly one `topic` value, but the rule and this check both generalize to any number. One invariant follows that isn't itself OWL/SHACL-expressible (dereferencing each linked graph's own `subject`, not just counting links), so it's checked here instead: none of a cell's `topic` subjects may already be one of that cell's `members` subjects — otherwise that duplicate would silently mask a real member from the derived subject, since the presence of any `topic` value switches the derivation to the `topic` set entirely, ignoring `members` (e.g. `Jane-Starostina(primary-care-physician).databook.md`, `Health & Wellness.databook.md`, and `Medications.databook.md` under `Pets/Ginger/` each keep a real `:Self`-subject graph in `members`, distinct from their own `topic` entry's subject, for exactly this reason). Run:

```python
import re, yaml, glob

GRAPHS_BASE_RE = re.compile(r'^https?://www\.example\.org/mia/graphs/')

def frontmatter(path):
    text = open(path, encoding='utf-8').read()
    m = re.match(r'^---\n(.*?)\n---', text, re.DOTALL)
    return yaml.safe_load(m.group(1)) if m else None

def local_name(v):
    return GRAPHS_BASE_RE.sub('', v)

violations = 0
for f in glob.glob('example/Cells/**/*.databook.md', recursive=True):
    fm = frontmatter(f)
    if not fm:
        continue
    mia = fm.get('mia', {}) or {}
    member_count = mia.get('memberCount')
    if not member_count:
        continue
    # mia.members/topic hold bare graph-id local names; mia.graphs[].id
    # keeps the full IRI (it doubles as the graph's named-graph identity) — normalize
    # both to the local name before looking up.
    graph_subject = {local_name(t['id']): t.get('subject') for t in (mia.get('graphs') or []) if isinstance(t, dict)}
    pt = mia.get('members') or []
    pt = pt if isinstance(pt, list) else [pt]
    ot = mia.get('topic') or []
    ot = ot if isinstance(ot, list) else [ot]
    pt_subs = {graph_subject.get(local_name(t)) for t in pt}
    ot_subs = {graph_subject.get(local_name(t)) for t in ot}
    dup = ot_subs & pt_subs
    if dup:
        violations += 1
        print(f'VIOLATION {f}: topic subject(s) {sorted(s for s in dup if s)} duplicate a members subject {sorted(s for s in pt_subs if s)} — masks a real member from the derived subject')
    derived = ot_subs if ot else pt_subs
    print(f'derived subject={sorted(s for s in derived if s)} {f}')
print()
print('All cells satisfy the subject-derivation rule.' if violations == 0 else f'{violations} violation(s) found.')
```

If a violation is found: for a duplicated subject, either move the redundant `topic` graph's content into the matching `members` graph instead, or reconsider whether that graph really belongs in `topic` at all.

**Check 19 — Cell-databook `title:` is the cell's name and matches its own folder's OS name**: `title:` is defined as the cell's own name — it is always exactly the name of the filesystem folder that holds the cell-databook, and the two are kept in sync (a folder rename means updating `title:` to match, never the reverse); `title:` is never an independent display-name override of the folder's name. The Cell DataBook Filename Convention already requires a cell-databook's *filename root* to be an exact copy of its folder's own name, but that convention is about the filename — not the separate `title:` YAML field, which several other checks (notably Check 10a's box-label match) treat as authoritative for what a cell "is called." The invariant: for every cell-databook under `example/Cells/`, `title:` must equal `os.path.basename` of the folder it directly lives in, verbatim (same case/spacing/punctuation rule as the filename convention — no kebab-casing, no paraphrasing). Run:

```python
import os, re, yaml

def frontmatter(path):
    text = open(path, encoding='utf-8').read()
    m = re.match(r'^---\n(.*?)\n---', text, re.DOTALL)
    return yaml.safe_load(m.group(1)) if m else None

errors = 0
for dirpath, _, filenames in os.walk('example/Cells'):
    if 'under-development' in dirpath.split(os.sep):
        continue
    cells = [f for f in filenames if f.endswith('.databook.md')]
    for fname in cells:
        path = os.path.join(dirpath, fname)
        fm = frontmatter(path)
        if not fm:
            continue
        title = fm.get('title')
        folder_name = os.path.basename(dirpath)
        if title != folder_name:
            print(f'MISMATCH  {path}  folder={folder_name!r}  title={title!r}')
            errors += 1
print('OK — title: matches its own folder name for every cell-databook.' if errors == 0 else f'{errors} mismatch(es) found.')
```

If a mismatch is found, the folder name is authoritative — update `title:` to match it exactly, even when the existing `title:` reads more naturally (e.g. an honorific like `Dr. Jane Starostina` vs. folder `Jane Starostina`, or an expansion like `AT&T` vs. folder `ATT`): `title:` is not an independent display-name override, so it cannot legitimately diverge from the folder's own name — the mismatch is drift, not a deliberate choice, since the folder name is also what Check 10a's diagram-box match keys off. If the *folder's* name is what's actually wrong (e.g. it should have been named `AT&T` all along), rename the folder itself instead, then update the cell-databook's filename and `title:` together to match the new folder name.

**Check 20 — `images/folder-mapping.png` folder colors match real data**: This diagram has no dedicated check of its own until now (unlike `cat-cell-graph.png`'s Check 15). Every cell shown in this diagram (and in `cat-cell-graph.png`, and in all 11 example diagrams — Check 10i) carries exactly two independent, mechanically-checkable colors: a **fill** color, applied to the cell's own Cell DataBook box — since `c:origin` is a fact asserted in the DataBook's own YAML frontmatter, not on some separate notion of "the folder," the DataBook box is what carries the fill; the folder icon drawn alongside it is always plain white and never carries fill — (tan if the cell's `mia.origin` resolves to `cat:Person`, light blue if `cat:Organization`, purple/Custom if the cell has no origin at all) and a folder-**name-text** color (green/"Predefined" if the cell's `title:` equals the origin class's own `rdfs:label` verbatim, plain black/"User-defined" otherwise — and always black for a no-origin/Custom cell, since there's no label to match). A cell with no origin is only legal if its cell-databook's filename carries the literal `(custom)` disambiguator (see the Cell DataBook Filename Convention) — the two facts (no `mia.origin` and a `(custom)` filename) must always agree; either alone without the other is an error. This is a visual check (no automated pixel/OCR comparison), but the script below computes the correct fill and text color for every real cell, for direct cross-reference against whichever diagram box is being checked — e.g. this diagram's "Fred Flintstone" box (origin `cat:Others`, folder name "Fred Flintstone") should be tan fill + black text; "People" (origin `cat:People`, folder name "People") should be tan fill + green text; the "Friends" box (no origin, filename `Friends(custom).databook.md`) should be purple fill + black text. Run:

```python
import glob, re, yaml

text = open('category.ttl').read()
classes, labels = {}, {}
pattern = re.compile(
    r'cat:([A-Za-z]+(?:\\\(org\\\))?) rdf:type owl:Class\s*;\s*'
    r'(?:cell:abstract \w+ ;\s*)?rdfs:subClassOf cat:([A-Za-z]+(?:\\\(org\\\))?)\s*;\s*'
    r'rdfs:label "([^"]+)"'
)
for m in pattern.finditer(text):
    child = m.group(1).replace('\\(', '(').replace('\\)', ')')
    parent = m.group(2).replace('\\(', '(').replace('\\)', ')')
    classes[child] = parent
    labels[child] = m.group(3)

def ancestry_root(cls):
    if cls in ('Person', 'Organization'):
        return cls
    seen = set()
    while cls in classes and cls not in seen:
        seen.add(cls)
        parent = classes[cls]
        if parent in ('Person', 'Organization'):
            return parent
        cls = parent
    return classes.get(cls, cls)

for path in sorted(glob.glob('example/Cells/**/*.databook.md', recursive=True)):
    if 'under-development' in path.split('/'):
        continue
    text2 = open(path, encoding='utf-8').read()
    m = re.match(r'^---\n(.*?)\n---', text2, re.DOTALL)
    fm = yaml.safe_load(m.group(1)) if m else None
    if not fm:
        continue
    mia = fm.get('mia', {}) or {}
    origin = mia.get('origin')
    title = fm.get('title')
    is_custom_filename = path.endswith('(custom).databook.md')
    if not origin:
        if not is_custom_filename:
            print(f'INCONSISTENT: {path} has no mia.origin but its filename does not carry (custom)')
            continue
        print(f'{title:35s} origin={"(none)":28s} label={"":24s} fill={"purple/Custom":24s} text=black/UserDefined')
        continue
    if is_custom_filename:
        print(f'INCONSISTENT: {path} carries a (custom) filename but has mia.origin={origin!r}')
        continue
    local = origin.split(':', 1)[1]
    root = ancestry_root(local)
    fill = 'tan/Person' if root == 'Person' else ('light-blue/Organization' if root == 'Organization' else f'UNKNOWN ROOT ({root})')
    label = labels.get(local, '???')
    text_color = 'green/Predefined' if title == label else 'black/UserDefined'
    print(f'{title:35s} origin={origin:28s} label={label:24s} fill={fill:24s} text={text_color}')
```

**Check 21 — `:Self` must be a member of every cell in the user's own tree**: A cell-databook under `example/Cells/` — the user's own instance tree — can only ever have gotten there one of two ways: (1) the user created it themselves, in which case they (`:Self`) are trivially a member, or (2) someone else shared it with the user, in which case the share necessarily made `:Self` a member (a cell can't be "shared with" someone without them becoming a member of it). Either way, `:Self` must be one of the cell's active members — i.e. `:Self` must be the `g:subject` of at least one of that cell's `members` — for **every** cell in `example/Cells/`, regardless of `cell:memberCount` or what the cell's derived subject (Check 18) is. This is strictest for `cell:OneMember` cells, where there is only one `members` slot at all: that slot's subject must be `:Self`, full stop — never the cell's `topic` subject (see Check 18's placement rule above), even when the cell's derived-from-`topic` subject is a third party (e.g. `Jane_Starostina`, `Paula_Walker`, `Ginger`) and no other graph happens to exist yet. `cell:TwoMember`/`cell:ThreePlusMember` cells have more room, so `:Self` just needs to be one of the members alongside whichever other real members the cell has (already satisfied by every existing example, e.g. Bob Johnson, Fred Flintstone, Medical Appointment, Boston Hub Society). This is not itself an OWL/SHACL-expressible constraint (same reasoning as Checks 17/18 — it requires dereferencing each `members` value's own `subject`, not just counting or matching cardinalities), so it's checked here instead. Run:

```python
import re, yaml, glob

GRAPHS_BASE_RE = re.compile(r'^https?://www\.example\.org/mia/graphs/')

def frontmatter(path):
    text = open(path, encoding='utf-8').read()
    m = re.match(r'^---\n(.*?)\n---', text, re.DOTALL)
    return yaml.safe_load(m.group(1)) if m else None

def local_name(v):
    return GRAPHS_BASE_RE.sub('', v)

violations = 0
for f in glob.glob('example/Cells/**/*.databook.md', recursive=True):
    if 'under-development' in f.split('/'):
        continue
    fm = frontmatter(f)
    if not fm:
        continue
    mia = fm.get('mia', {}) or {}
    member_count = mia.get('memberCount')
    if not member_count:
        continue
    graph_subject = {local_name(t['id']): t.get('subject') for t in (mia.get('graphs') or []) if isinstance(t, dict)}
    pt = mia.get('members') or []
    pt = pt if isinstance(pt, list) else [pt]
    subs = [graph_subject.get(local_name(t)) for t in pt]
    if not any(s == ':Self' for s in subs):
        violations += 1
        print(f'VIOLATION {member_count} members-subjects={subs} (no :Self) {f}')
print('All cells have :Self as a member.' if violations == 0 else f'{violations} violation(s) found.')
```

If a violation is found, add a new minimal graph claimed by and about `:Self` (following the pattern in `Medications.databook.md` under `Pets/Ginger/`, `Jane-Starostina(primary-care-physician).databook.md`, or `Health & Wellness.databook.md` — a single `designated by` → `GivenName` triple is enough), assign it the next free `graph-<NN>`, put it in `members`, and move whatever was in that slot to `topic` instead.

If a diagram box's fill or text color doesn't match this script's output for the corresponding real folder, the diagram wins (per Check 10's own rule) — update `mia.origin`/`title:`/filename only if the *data* is actually wrong, otherwise redraw the box.

**Check 22 — `persona-templates.ttl` matches `images/persona-ontology/persona-templates.png`**: This diagram is a pure classification tree — every box label is a class's exact *local name* (with the `p:` prefix), not its `rdfs:label` display string (e.g. `p:PetMedicationRecord`, not "Pet Medications"), and it shows no property arrows at all. `persona-templates.ttl` defines many properties (`persona:hasIdentityDocument`, `persona:forPatient`, `persona:hasPrimaryCarePhysician`, `persona:hasMedication`, `persona:hasActiveIngredient`, `persona:hasDoseForm`, `persona:hasDosageAmount`, `persona:hasAdministration`, etc.) — none of these are missing from the diagram by omission; they're simply out of scope for it, unlike `cell.png`/`graph.png`/`category.png`, which do show property arrows. Two `ako` (a-kind-of) arrows each connect a bracket of boxes to a superclass box, arrow always pointing from subclass(es) to superclass regardless of whether that superclass is drawn above or below the bracket: `p:PersonaTemplate` (above, connects to all six boxes — `p:BirthCertificateDocument`, `p:DriversLicenseDocument`, `p:PassportDocument`, `p:JSContactCard`, `p:MedicalAppointmentRecord`, `p:PetMedicationRecord`) and `p:IdentityDocument` (below, connects to only the first three of those same six boxes). Like Checks 12–14, this check does not presume which side is authoritative when the two disagree — surface the discrepancy and ask. Verify:

- **22a** — every box in the top bracket (pointing at `p:PersonaTemplate`) matches a class in `persona-templates.ttl` actually declared `rdfs:subClassOf persona:PersonaTemplate`, by exact local name.
- **22b** — every box in the bottom bracket (pointing at `p:IdentityDocument`) matches a class actually declared `rdfs:subClassOf persona:IdentityDocument`, by exact local name — and every such class must already be in the top bracket too, since `persona-templates.ttl`'s three `IdentityDocument` subclasses (`p:BirthCertificateDocument`, `p:DriversLicenseDocument`, `p:PassportDocument`) are always also `PersonaTemplate` subclasses (see `persona-templates.ttl`'s own class-hierarchy doc comment).
- **22c** — conversely, every class in `persona-templates.ttl` declared `rdfs:subClassOf persona:PersonaTemplate` or `rdfs:subClassOf persona:IdentityDocument` appears as a box in the diagram (catches a new template/identity-document class added to the ttl but never drawn).

This is a visual check (no automated OCR), but the script below prints the ttl's actual current subclass structure for direct cross-reference against the diagram:

```python
import re

text = open('persona-templates.ttl').read()
blocks = re.split(r'\n\n+', text)
for block in blocks:
    m = re.search(r'persona:(\w+) rdf:type owl:Class', block)
    if not m:
        continue
    cls = m.group(1)
    subs = re.findall(r'rdfs:subClassOf persona:(\w+)', block)
    if 'PersonaTemplate' in subs or 'IdentityDocument' in subs:
        print(f'{cls:30} subClassOf {subs}')
```

## Keeping Files in Sync

Whenever changes are made to any graph file, `persona.ttl`, or `graph.ttl`, `persona-shacl.ttl` must be updated to match:

- **New property usage in a graph** (e.g., a new physical characteristic, relationship, or identifier added to a Person or Persona instance) → add or extend a SHACL shape to validate that property on the relevant target class.
- **New class or property defined in `persona.ttl`** (e.g., `persona:hasSocialNetwork`) → add a SHACL shape that constrains how instances of the domain class may or must use it.

Always update `persona-shacl.ttl` in the same edit session as the change that triggers it.

## Validation

**SHACL validation** (e.g., using Apache Jena's `shaclvalidate`) — run against turtle extracted from a cell-databook (see EXAMPLE.md's Validation section for the full extraction pipeline; graph 14 is embedded in this cell):
```bash
databook extract "example/Cells/Affiliations/Boston Hub Society/Boston Hub Society(affiliations).databook.md" > /tmp/data.ttl
shaclvalidate -datafile /tmp/data.ttl -shapesfile persona-shacl.ttl
```

**Protégé**: Load `persona.ttl`; Protégé will import the domain ontologies via IRI resolution. Use the reasoner (HermiT/Pellet) to check consistency.

## README Coverage

Documentation is split across three files: `README.md` documents the ontologies themselves (Category, Cell, Graph, Persona, Organization); `EXAMPLE.md` holds the worked Alice Walker example, diagram-generation instructions, and the full validation pipeline (linked from the bottom of `README.md`); `APP-BEHAVIOR.md` documents app-level behavior built on top of the ontologies — cell lifecycle, storage/sync, sharing/permissions, naming/renaming, filesystem persistence, and the auto-filing heuristic (linked from both `README.md` and `EXAMPLE.md`). All three files must be written in US English. Use American spellings throughout — e.g. "organization" not "organisation", "color" not "colour".

All classes and properties defined in `persona.ttl`, `graph.ttl`, `cell.ttl`, and `category.ttl` must be mentioned in `README.md`. The only intentional exceptions are the internal ontology documentation annotation properties (`usesRequiredClass`, `usesOptionalClass`, `usesCCOClass`, `usesCCOProperty`, `usagePattern`), which are infrastructure for self-documenting the ontology, not user-facing terms.

In `README.md`, `EXAMPLE.md`, and `APP-BEHAVIOR.md`, every mention of a class defined in `persona.ttl` must appear in backticks with the `p:` prefix (e.g. `p:Persona`, `p:Wallet`), every mention of a class or property defined in `graph.ttl` must appear in backticks with the `t:` prefix (e.g. `g:template`, `g:subject`), every mention of a class or property defined in `cell.ttl` must appear in backticks with the `c:` prefix (e.g. `c:Cell`, `c:memberCount`), and every mention of a class or property defined in `category.ttl` must appear in backticks with the `cat:` prefix (e.g. `cat:Category`, `cat:templateCell`). Every capitalized mention of `Person` (the CCO class) must also appear in backticks. These formatting rules do **not** apply inside headings or subheadings.

## Catalog Files

Two `catalog-v001.xml` files map ontology IRIs to local file paths so Protégé can resolve `owl:imports` without hitting the network:

- **`catalog-v001.xml`** (repo root) — used when opening root-level files (`persona.ttl`, `persona-shacl.ttl`, etc.) directly. Uses **relative** paths from the repo root.
- **`example/catalog-v001.xml`** — used when opening a graph file from the `example/` directory directly. Uses **absolute** `file://` paths.

**Whenever a `.ttl` file is created, deleted, renamed, or moved**, update both catalog files to match:
- **Create**: add a `<uri>` entry in both catalogs with the new file's ontology IRI (from its `rdf:type owl:Ontology` declaration) and its path.
- **Delete**: remove the corresponding `<uri>` entry from both catalogs.
- **Rename or move**: update the `uri=` path attribute in both catalogs.

The `id` attribute is a human-readable label (no functional significance); keep it consistent with the file's short name or diagram number.

## Gitignore Notes

`/project_files` is gitignored. The `project_files/` directory exists locally but is not tracked — it contains source domain ontologies and reference documents.
