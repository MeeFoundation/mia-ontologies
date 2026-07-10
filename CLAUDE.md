# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an **RDF/OWL ontology project** — a formal semantic knowledge model for representing natural people's identity data in the Mee Identity Agent (MIA). It comprises three peer application ontologies:

- **Persona ontology** (`persona.ttl`): models identity data — names, addresses, identifiers, relationships, payment cards, and more — structured around context-specific `Person` instances. Imports and profiles existing domain ontologies, documenting which of their classes and properties Mee uses, and extends them with Mia-specific terms.
- **Context ontology** (`context.ttl`): defines controlled vocabularies for classifying context files — who claimed the data (`claimant`), and whose identity the file describes (`subject`), plus the `Context` class hierarchy (`SBScontext`/`OBScontext`/`OBOcontext`/`SBOcontext`).
- **Cell ontology** (`cell.ttl`): defines the cell class hierarchy (`Personal`/`Organizational`/`UserDefined` as direct subclasses of `Cell`, and the orthogonal `Parties`/`OneParty`/`MultiParty`(abstract)/`TwoParty`/`ThreePlusParty` hierarchy every cell instance is also typed under, plus all leaf cells) and the properties that classify and link cell DataBooks (`cellType`, `num-parties`, `sbs`/`obs`/`sbo`/`obo`, `child`, `label`, `note`, `folder`, `copiedFrom`). Mutually imports `context.ttl`.

There are no build, compile, test, or lint commands. The files are Turtle (`.ttl`) loaded into semantic web tools (Protégé).

## Core Files

| File | Purpose |
|------|---------|
| `persona.ttl` | Persona ontology — imports domain ontologies, annotates which classes/properties are required vs. optional for Mee, defines Mia-specific classes and properties |
| `context.ttl` | Context ontology — controlled vocabularies for classifying context files (`cell`, `claimant`, `subject`, `about-by`) and the `Context` class hierarchy. Mutually imports `cell.ttl` |
| `cell.ttl` | Cell ontology — the cell class hierarchy and its classification/link properties (`cellType`, `num-parties`, `sbs`/`obs`/`sbo`/`obo`, `child`, `label`, `note`, `folder`, `copiedFrom`). Mutually imports `context.ttl` |
| `cell-shacl.ttl` | SHACL validation shapes for cell DataBook instances — `cellType`/`num-parties` cardinality and enum, `note`/`folder`/`sbs` cardinality, and `obs`/`sbo`/`obo` cardinality (forbidden on `OneParty` cells, capped at 1 on `TwoParty` cells, unconstrained on `ThreePlusParty` cells) |
| `persona-shacl.ttl` | SHACL validation shapes — constraint rules for all `persona:Person` instances (SSN format, address cardinality, payment cards, wallet, social network, etc.) |
| `persona-templates.ttl` | Persona template labels — defines `p:PersonaTemplate` (abstract classification superclass) and concrete label subclasses `p:BirthCertificate`, `p:JSContactCard`, `p:DriversLicense`, `p:Passport`, `p:MedicalAppointment`; also defines related designator classes (`persona:DriversLicenseNumber`, `persona:IssuingJurisdiction`, `persona:PassportNumber`, `persona:IssuingCountry`, `persona:PlaceOfBirth`, `persona:GenderMarker`, `persona:IssueDate`, `persona:Credential`, `persona:WebURL`, `persona:OrganizationUnit`, `persona:JobTitle`), complex classes (`persona:Anniversary`, `persona:PersonalInfo`), the `p:MedicalAppointment` claim properties (`persona:forPatient`, `persona:hasPrimaryCarePhysician`, `persona:currentMedication`, `persona:allergy`, `persona:medicalHistoryNote`, `persona:insuranceProvider`, `persona:insurancePolicyNumber`, `persona:insuranceGroupNumber`, `persona:preferredPharmacy`), and other properties (`persona:hasAnniversary`, `persona:hasPhoto`, etc.) |
| `shacl/birthcertificate-shacl.ttl` | Per-template SHACL shapes for birth certificate context files — run against the individual context file, not merged data |
| `shacl/jscontactcard-shacl.ttl` | Per-template SHACL shapes for JSContactCard context files — run against the individual context file, not merged data |
| `shacl/driverslicense-shacl.ttl` | Per-template SHACL shapes for driver's license context files — run against the individual context file, not merged data |
| `shacl/passport-shacl.ttl` | Per-template SHACL shapes for passport context files — run against the individual context file, not merged data |
| `shacl/medical-appointment-shacl.ttl` | Per-template SHACL shapes for medical appointment context files — run against the individual context file, not merged data |
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
  └─ example/contexts/self.self(health-wellness)(17).databook.md

persona-shacl.ttl — no owl:imports of data; validated against the loaded dataset
shacl/birthcertificate-shacl.ttl  — per-template shapes for birth certificate files
shacl/jscontactcard-shacl.ttl     — per-template shapes for JSContactCard files
shacl/driverslicense-shacl.ttl    — per-template shapes for driver's license files
shacl/passport-shacl.ttl          — per-template shapes for passport files
shacl/medical-appointment-shacl.ttl — per-template shapes for medical appointment files
```

1. **Foundation**: BFO (Basic Formal Ontology) — provides temporal modeling (`TemporalInterval`) and core relations
2. **Domain Ontologies** (in `project_files/`): PersonOntology, AddressOntology, StagingOntology
3. **Application Ontologies** (peer, not nested):
   - `persona.ttl`: aggregates domain ontologies; uses annotation properties (`usesRequiredClass`, `usesOptionalClass`, `usesCCOClass`, `usesCCOProperty`) to document Mee's usage
   - `context.ttl`: defines `cell`, `claimant`, `subject`, and `about-by` vocabularies; imported directly by each context file
   - `cell.ttl`: defines the cell class hierarchy and classification/link properties; mutually imports `context.ttl`

### Context File Naming Convention

Context filenames follow a single flat pattern:

```
<subject>.<claimant>(<containing-cell>)(<NN>).databook.md
```

| Segment | Meaning |
|---------|---------|
| `<subject>` | The entity the Persona is about. Use `self` when the subject is the Mia user's own `p:Person` (`:Self`); otherwise use the full hyphenated lowercase name (e.g. `paula-walker`, `bob-johnson`, `bhs-group`). |
| `<claimant>` | Who claimed the data. Use `self` when the claimant is `:Self`; use the full hyphenated lowercase name for other claimants (e.g. `bob-johnson`, `citibank`); use the literal `members` for `cell:ThreePlusParty` contexts where any permitted member may write. |
| `(<containing-cell>)` | The local-name portion of this context's `mia.cell` IRI — i.e., the IRI of the cell DataBook that directly holds the `sbs`, `obs`, `sbo`, or `obo` link to this context. When the cell DataBook local name includes a `(parent)` qualifier (e.g. `bob-johnson(others)`), the filename uses two separate parenthetical segments before the number: `(bob-johnson)(others)`. Examples: `(bob-johnson)(others)`, `(boston-hub-society)(affiliations)`, `(paula-walker)(immediate-family)`, `(citibank)(banking-payments)`. For cells without a `(parent)` qualifier (e.g. `health`, `ownership`), a single segment suffices. |
| `(<NN>)` | Zero-padded two-digit context number in parentheses, matching the diagram label. |

**Exception — `cell:ThreePlusParty` contexts**: A group context (`num-parties: ThreePlusParty`) has no single claimant — any permitted member can write to it and changes replicate to all members. The `<claimant>` segment is the literal `members` rather than an individual name. Example: `bhs-group.members(boston-hub-society)(affiliations)(01).databook.md` — about BHS Group, containing cell "boston-hub-society(affiliations)", claimed by the group's members collectively.

**Exception — `cell:graph`-linked contexts**: A context linked from its cell via `cell:graph` (rather than `sbs`/`obs`/`sbo`/`obo`) has no `about-by` classification and no single subject/claimant — it is data jointly maintained by multiple parties about a third party. Such contexts drop the `<subject>.<claimant>` prefix entirely and use the literal `context` in its place: `context(<containing-cell>)(<NN>).databook.md`. These files also omit `mia.claimant` and `mia.subject` from the YAML frontmatter (those fields describe a single-claimant relationship that doesn't apply here). Example: `context(alice-carol-about-mom)(health)(26).databook.md` — jointly maintained by Alice and Carol about their mother Paula, containing cell `alice-carol-about-mom(health)`.

**`mia.claimant` vocabulary**: The YAML field takes the local IRI of a `p:Person`, `g:Group`, or `o:Organization` individual — NOT an `i:PDNidentifier`. Those individuals carry their own PDN identity via `identity:hasPDNidentifier`. Specifically: `:Self` (the Mia user's `p:Person`) for self-claimed contexts; a named `p:Person` individual (e.g. `:Bob_Johnson`) when another Mia user claims the data; a named `g:Group` individual (e.g. `:BHS_Group`) for group contexts; and a named `o:Organization` individual (e.g. `:Citibank`) only when the claiming organization is itself a PDN node. In the example data **only Citibank is a PDN node**, so only `self.citibank(citibank)(banking-payments)(09).databook.md` uses `claimant: ":Citibank"`. All other organization-related contexts (Google, AT&T, SSA, etc.) use `claimant: ":Self"` because Alice self-enters that data — those organizations are not PDN-interoperable.

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

**All data belongs to contexts**: There is no separate selfness file. Every piece of identity data — names, identifiers, addresses, payment cards, physical characteristics — belongs to a context-specific Persona file. The Mia user's `persona:Person` individual (IRI `:Self`) is declared in each context file; there is no single root file that owns the declaration.

**`:Self` IRI convention**: The Mia user's own `persona:Person` individual always uses the IRI `:Self` across all of their context files. All other people, groups, and organizations are assigned locally-minted named IRIs (e.g. `:Bob_Johnson`, `:Paula_Walker`, `:BHS`). `:Self` is a local IRI and is never exposed externally over the PDN, so there are no collisions between Mia instances. All context files in the example live in Alice's Mia — some authored by Alice, others received from peers over PDN. In either case, `:Self` refers to Alice. When data arrives from a peer's Mia (where that peer was `:Self` in their own instance), Alice's Mia assigns them a locally-minted identifier; once a PDN connection is established, that identifier resolves to or is replaced by their PDN ID.

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

Before committing any change to any context file, `persona.ttl`, `context.ttl`, `cell.ttl`, or `persona-shacl.ttl`, increment the **minor version number** in that file's `owl:versionInfo` annotation and update the description to summarise the change. For example:

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

**Check 2 — Filename convention**: Every context filename must follow `<subject>.<claimant>(<containing-cell>)(<NN>).databook.md`. `<subject>` must be `self` when the subject is `:Self`, or the full hyphenated lowercase name otherwise. `<claimant>` must be `self` when the claimant is `:Self`, or the full hyphenated lowercase name otherwise — except for `c:Group` contexts, where it must be the literal string `members`. `(<containing-cell>)` encodes the local name of the `mia.cell` IRI: when the cell DataBook local name includes a `(parent)` qualifier (e.g. `bob-johnson(others)`), it appears as two separate segments `(bob-johnson)(others)`; when there is no qualifier (e.g. `health`), a single segment suffices. `(<NN>)` is the zero-padded two-digit context number. Exception: a context linked via `cell:graph` rather than `sbs`/`obs`/`sbo`/`obo` drops the `<subject>.<claimant>` prefix and uses the literal `context` instead — `context(<containing-cell>)(<NN>).databook.md`. If a filename does not match one of these two patterns, rename it to conform.

**Check 3 — `mia.cell` ↔ filename consistency**: For every context DataBook in `example/contexts/` (excluding `under-development/`), the local-name portion of its `mia.cell` IRI must equal the `(<containing-cell>)` segment extracted from the filename. When the filename uses two separate parenthetical segments before the number (e.g. `(bob-johnson)(others)`), concatenate them as `bob-johnson(others)` to form the expected local name. Run:

```python
import os, re

cell_dir = 'example/cells'
ctx_dir = 'example/contexts'
base_cell = 'http://www.example.org/mia/cells/'

def fn_cell_local(fname):
    base = fname[:-len('.databook.md')]
    m = re.match(r'^context((?:\([^)]+\))+)\(\d{2}\)$', base)
    if not m:
        m = re.match(r'^[^.]+\.[^(]+((?:\([^)]+\))+)\(\d{2}\)$', base)
    if not m:
        return None
    segs = re.findall(r'\(([^)]+)\)', m.group(1))
    return segs[0] if len(segs) == 1 else f'{segs[0]}({segs[1]})'

errors = 0
for fname in sorted(os.listdir(ctx_dir)):
    if not fname.endswith('.databook.md'):
        continue
    path = f'{ctx_dir}/{fname}'
    text = open(path).read()
    cell_m = re.search(r'^\s+cell:\s+"([^"]+)"', text, re.MULTILINE)
    if not cell_m:
        print(f'NO mia.cell: {fname}'); errors += 1; continue
    cell_local = cell_m.group(1)
    if cell_local.startswith(base_cell):
        cell_local = cell_local[len(base_cell):]
    expected = fn_cell_local(fname)
    if cell_local != expected:
        print(f'MISMATCH {fname}:')
        print(f'  filename implies: {expected!r}')
        print(f'  mia.cell has: {cell_local!r}')
        errors += 1
if not errors:
    print('All mia.cell values match filenames.')
```

If mismatches appear, the filename `(<containing-cell>)` segments are authoritative — update the `mia.cell` IRI in the DataBook to match (or vice versa if the filename was misnamed).

**Check 4 — No orphan Persons**: Every `persona:Person` individual other than `:Self` must be reachable via `BFO_0000115` (has member part) from a `g:Group` or from a Social Network individual linked to another `persona:Person` via `persona:hasSocialNetwork`. `:Self` is always the root and needs no incoming link.

**Check 5 — Validation command completeness**: The `## Validation` section of `README.md` must document two tiers. Tier 1 uses four steps: (1) a `find example -name "*.databook.md"` loop using `databook extract` to extract turtle content and produce a merged turtle file of all context data (excluding `under-development/`); (2) a `riot` merge of that data with all application ontology TTL files and the foundation ontologies listed explicitly from `project_files/`; (3) a `grep -v owl:imports` on `persona-shacl.ttl` to collect shapes (the `shacl/` per-template files are excluded here — they target `persona:Person` and would fire incorrectly on all individuals when applied to merged data); (4) a `shacl validate` call. Tier 2 lists explicit per-file `databook extract` + `riot` + `shacl validate` commands for each template context file paired with its `shacl/*-shacl.ttl` file. If the commands change, update the README to match.

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

**Check 9 — `about-by` ↔ `subject`/`claimant` consistency**: Every DataBook's `mia.about-by` value must be consistent with its `mia.subject` and `mia.claimant` values according to these rules:

| `about-by` | `subject` | `claimant` |
|---|---|---|
| `context:SBScontext` | `:Self` | `:Self` |
| `context:OBScontext` | not `:Self` | `:Self` |
| `context:OBOcontext` | not `:Self` | not `:Self` |
| `context:SBOcontext` | `:Self` | not `:Self` |

For each DataBook in `example/` (excluding `under-development/`), extract the three YAML values and verify they match the table. If they conflict, `about-by` is the authoritative value — update `subject` and/or `claimant` to match it. Exception: a context linked from its cell via `cell:graph` (rather than `sbs`/`obs`/`sbo`/`obo`) has no `about-by` value at all — it is not classified into one of the four subtypes, since its data is jointly maintained by multiple parties about a third party rather than claimable as self-vs-other. Such a context may still set `subject`/`claimant` as descriptive metadata; this check simply does not apply to it.

**Check 10 — Cell filename ↔ id consistency**: For every cell DataBook in `cells-person/`, `cells-org/`, and `example/cells/`, the filename root (the filename with `.databook.md` stripped) must exactly match the local name portion of the file's `id:` IRI (the string after the IRI base). The IRI base for canonical Person files is `http://mee.foundation/ontologies/cells-person/`; for canonical Organization files it is `http://mee.foundation/ontologies/cells-org/`; for example files it is `http://www.example.org/mia/cells/`. `cells-person/`, `cells-org/`, and `example/cells/` are all nested into folders mirroring their cell tree (see Check 12), so they must be walked recursively. Run:

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
    ('cells-person', 'http://mee.foundation/ontologies/cells-person/', True),
    ('cells-org',     'http://mee.foundation/ontologies/cells-org/', True),
    ('example/cells', 'http://www.example.org/mia/cells/', True),
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

If a mismatch is found, rename the file so its root matches the id local name (preferred) or update the `id:` to match the filename — whichever is consistent with the broader naming conventions.

**Check 11 — Example cell diagrams are authoritative**: The 11 cell diagrams in `example/images/` are the authoritative source of truth for the example cell tree. When any discrepancy is found between a diagram and the DataBook files, the diagram wins — update the DataBooks to match, not the other way around. After any change to `example/cells/` DataBooks or to the 11 diagrams, verify all of the following:

- **11a — Every cell box has a DataBook**: Every cell box (blue/tan canonical or white user-defined) shown in any of the 11 diagrams must have a corresponding `.databook.md` file in `example/cells/` whose `title:` matches the box label. If a box has no DataBook, create one.

- **11b — Every DataBook has a diagram box**: Every `.databook.md` file in `example/cells/` (except `cells.databook.md` itself, which is the invisible root) must appear as a visible box in at least one of the 11 diagrams. If a DataBook has no corresponding box, either add it to the appropriate diagram or delete the DataBook.

- **11c — Solid context circles match DataBook links**: Every solid (filled) context circle attached to a cell box indicates a real context link. The cell DataBook for that box must carry the corresponding `sbs`, `obs`, `obo`, `sbo`, or `graph` field pointing to the context DataBook IRI. A dashed (empty) circle indicates an unfilled slot — the DataBook must NOT have a link for that slot.

- **11d — Numbered context circles have matching files**: Every numbered context circle (e.g. `[10]`, `[17]`) shown in a diagram must correspond to an actual `.databook.md` file in `example/contexts/` whose filename contains that number (e.g. `(10)`, `(17)`).

- **11e — Child arrows match DataBook child links**: Every downward child arrow from cell box A to cell box B in a diagram must correspond to a `child:` entry in A's DataBook pointing to B's IRI. Conversely, every `child:` entry in a DataBook must be reflected by a visible child arrow in the diagram.

The 11 diagrams are: `example/images/people.png`, `example/images/people2.png`, `example/images/health.png`, `example/images/work.png`, `example/images/companies.png`, `example/images/finances.png`, `example/images/gov-state.png`, `example/images/gov-federal.png`, `example/images/gov-municipality.png`, `example/images/misc.png`, `example/images/affiliations.png`.

**Check 12 — Physical folder structure mirrors the `child:` tree in `cells-person/`, `cells-org/`, and `example/cells/`**: All three cell trees are organized as nested filesystem folders that mirror their cell hierarchy, rather than one flat directory. Each cell's own `.databook.md` file lives in a folder (folder naming is not standardized — it may be the cell's `title`, a `cellType`-prefixed disambiguator, or a role-based label; this check does not validate folder names, only nesting). The rule: for every `mia.child` link from cell A to cell B, B's `.databook.md` file must live in a folder that is a **direct subfolder** of the folder containing A's `.databook.md` file — not deeper, not a sibling, not the same folder. Each tree's root DataBook (`cells-person.databook.md` / `cells-org.databook.md` / `cells.databook.md`) sits directly in the tree's top-level directory. Run:

```python
import os, re, yaml

def check_tree(root):
    id_to_dir, id_to_children, dir_to_ids = {}, {}, {}

    for dirpath, _, filenames in os.walk(root):
        for fname in filenames:
            if not fname.endswith('.databook.md'):
                continue
            path = os.path.join(dirpath, fname)
            fm = yaml.safe_load(re.match(r'^---\n(.*?)\n---', open(path).read(), re.DOTALL).group(1))
            cid = fm['id']
            rel_dir = os.path.relpath(dirpath, root)
            id_to_dir[cid] = rel_dir
            dir_to_ids.setdefault(rel_dir, []).append(cid)
            child = fm.get('mia', {}).get('child')
            if child:
                id_to_children[cid] = child if isinstance(child, list) else [child]

    def parent_of(reldir):
        if reldir == '.':
            return None
        p = os.path.dirname(reldir)
        return p if p != '' else '.'

    errors = []
    for d, ids in dir_to_ids.items():
        if len(ids) > 1:
            errors.append(f'MULTIPLE DATABOOKS in same dir {d!r}: {ids}')

    for parent_id, children in id_to_children.items():
        parent_dir = id_to_dir.get(parent_id)
        for child_id in children:
            child_dir = id_to_dir.get(child_id)
            if child_dir is None:
                errors.append(f'Child id {child_id!r} (child of {parent_id}) not found on disk')
            elif parent_of(child_dir) != parent_dir:
                errors.append(f'NESTING MISMATCH: child {child_id!r} dir={child_dir!r} is not a direct subfolder of parent {parent_id!r} dir={parent_dir!r}')

    id_by_dir = {d: ids[0] for d, ids in dir_to_ids.items() if len(ids) == 1}
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

for root in ['cells-person', 'cells-org', 'example/cells']:
    errors = check_tree(root)
    print(f'{root}: ' + (f'{len(errors)} issue(s) found:' if errors else 'OK — folder structure matches the child-link tree.'))
    for e in errors:
        print(' -', e)
```

If a nesting mismatch or orphan is found, move the file to the correct folder (preferred) or fix the `mia.child` link — whichever reflects the intended tree. An empty/placeholder folder is not necessarily an error — flag it to the user rather than deleting it, since it may be a deliberate placeholder for content not yet added.

**Check 13 — `cell.ttl` matches `images/cell-ontology/cell.png`**: This diagram is the ontology-level (not example-tree) picture of `cell:Cell`'s structure — its properties, the `child` self-relationship, the `Cell` → `Personal`/`Organizational`/`UserDefined` class hierarchy, and the `Parties` → `OneParty`/`MultiParty` (abstract) → `TwoParty`/`ThreePlusParty` hierarchy with each concrete subtype's `cell:label` display value. `cell:Parties` is not `rdfs:subClassOf cell:Cell` (and vice versa) — the diagram accordingly draws them as two separate trees, not one. Unlike Check 11 (example diagrams, where the diagram always wins), this check does not presume which side is authoritative when the two disagree — surface the discrepancy and ask, since fixing it might mean updating `cell.ttl` (e.g. adding a missing property, as `cell:graph` was) or might mean the diagram is simply stale and needs redrawing. After any change to `cell.ttl`'s `cell:Cell`/`cell:Parties` sections or to this diagram, verify:

- **13a** — every property arrow shown off `Cell` (`label`, `note`, `folder`, `graph`, `cellType`) has a corresponding `cell:` property in `cell.ttl` with `rdfs:domain cell:Cell`; every arrow shown off `Parties` (`num-parties`, `sbs`) has `rdfs:domain cell:Parties`; every arrow shown off `MultiParty` (`obs`, `sbo`, `obo`) has `rdfs:domain cell:MultiParty`. Each arrow's target type in the diagram must match the property's `rdfs:range`.
- **13b** — every `cell:` property with `rdfs:domain cell:Cell`, `cell:Parties`, or `cell:MultiParty` defined in `cell.ttl` appears as an arrow in the diagram, under the box matching its domain (catches new properties added to the ttl but never drawn, or drawn under the wrong box).
- **13c** — the class hierarchy under `Cell` (→ `Personal`/`Organizational`/`UserDefined`) and under `Parties` (→ `OneParty`/`MultiParty` → `TwoParty`/`ThreePlusParty`) shown in the diagram matches `cell.ttl`'s actual `rdfs:subClassOf` relationships (by class local name, not just position).
- **13d** — each concrete `Parties` subtype's example `cell:label` value shown in the diagram (`"Cell"`, `"Two-Party Cell"`, `"Multi-Party Cell"`) matches that subtype's actual `cell:label` value in `cell.ttl`. `Parties` and `MultiParty` are abstract and carry no `cell:label` of their own.

**Check 14 — `context.ttl` matches `images/context-ontology/context.png`**: This diagram is the ontology-level picture of `context:Context`'s structure — its `cell`/`template` properties, the intermediate `context:XBXcontext` class (carrying `about-by`/`subject`/`claimant`), and the four classified subtypes (`SBScontext`/`OBScontext`/`OBOcontext`/`SBOcontext`) below it. Like Check 13, this does not presume which side is authoritative when the two disagree — surface the discrepancy and ask. After any change to `context.ttl` or to this diagram, verify:

- **14a** — every property arrow shown off `Context` in the diagram (`cell`, `template`) has a corresponding `context:` property in `context.ttl` with `rdfs:domain context:Context`, and its target type matches the property's `rdfs:range`.
- **14b** — every property arrow shown off `XBXcontext` in the diagram (`about-by`, `subject`, `claimant`) has a corresponding `context:` property with `rdfs:domain context:XBXcontext`.
- **14c** — every `context:` property with domain `context:Context` or `context:XBXcontext` defined in `context.ttl` appears in the diagram under the correct box (catches new properties added to the ttl but never drawn, or drawn under the wrong box).
- **14d** — the class hierarchy shown (`Context` → `XBXcontext` → `SBScontext`/`OBScontext`/`OBOcontext`/`SBOcontext`) matches `context.ttl`'s actual `rdfs:subClassOf` relationships.

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

All classes and properties defined in `persona.ttl`, `context.ttl`, and `cell.ttl` must be mentioned in `README.md` in the sections before the **Illustrative Example: Alice Walker** section. The only intentional exceptions are the internal ontology documentation annotation properties (`usesRequiredClass`, `usesOptionalClass`, `usesCCOClass`, `usesCCOProperty`, `usagePattern`), which are infrastructure for self-documenting the ontology, not user-facing terms.

In `README.md`, every mention of a class defined in `persona.ttl` must appear in backticks with the `p:` prefix (e.g. `p:Persona`, `p:Wallet`), every mention of a class or property defined in `context.ttl` must appear in backticks with the `c:` prefix (e.g. `c:contextType`, `c:SelfClaimed`), and every mention of a class or property defined in `cell.ttl` must appear in backticks with the `cell:` prefix (e.g. `cell:Cell`, `cell:cellType`). Every capitalized mention of `Person` (the CCO class) must also appear in backticks. These formatting rules do **not** apply inside headings or subheadings.

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
