# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an **RDF/OWL ontology project** — a formal semantic knowledge model for representing natural people's identity data in the Mee Identity Agent (MIA). It comprises three peer application ontologies:

- **Persona ontology** (`persona.ttl`): models identity data — names, addresses, identifiers, relationships, payment cards, and more — structured around context-specific `Person` instances. Imports and profiles existing domain ontologies, documenting which of their classes and properties Mee uses, and extends them with Mia-specific terms.
- **Context ontology** (`context.ttl`): defines controlled vocabularies for classifying context files — what asserted the data (`assertedBy`), and whose identity the file describes (`subject`), plus the `Context` class hierarchy (`SBScontext`/`OBScontext`/`OBOcontext`/`SBOcontext`).
- **Category ontology** (`category.ttl`): defines the category class hierarchy (`Person`/`Organization`/`UserDefined` as direct subclasses of `Category`, `Parties`/`OneParty`/`TwoParty`/`MultiParty`, and all leaf categories) and the properties that classify and link category DataBooks (`classname`, `num-parties`, `sbs`/`obs`/`sbo`/`obo`, `child`, `label`, `note`, `folder`, `copiedFrom`). Mutually imports `context.ttl`.

There are no build, compile, test, or lint commands. The files are Turtle (`.ttl`) loaded into semantic web tools (Protégé).

## Core Files

| File | Purpose |
|------|---------|
| `persona.ttl` | Persona ontology — imports domain ontologies, annotates which classes/properties are required vs. optional for Mee, defines Mia-specific classes and properties |
| `context.ttl` | Context ontology — controlled vocabularies for classifying context files (`category`, `assertedBy`, `subject`, `about-by`) and the `Context` class hierarchy. Mutually imports `category.ttl` |
| `category.ttl` | Category ontology — the category class hierarchy and its classification/link properties (`classname`, `num-parties`, `sbs`/`obs`/`sbo`/`obo`, `child`, `label`, `note`, `folder`, `copiedFrom`). Mutually imports `context.ttl` |
| `category-shacl.ttl` | SHACL validation shapes for category DataBook instances — `classname`/`num-parties` cardinality and enum, `sbs`/`obs`/`sbo` cardinality |
| `persona-shacl.ttl` | SHACL validation shapes — constraint rules for all `persona:Person` instances (SSN format, address cardinality, payment cards, wallet, social network, etc.) |
| `persona-templates.ttl` | Persona template labels — defines `p:PersonaTemplate` (abstract classification superclass) and concrete label subclasses `p:BirthCertificate`, `p:JSContactCard`, `p:DriversLicense`, `p:Passport`; also defines related designator classes (`persona:DriversLicenseNumber`, `persona:IssuingJurisdiction`, `persona:PassportNumber`, `persona:IssuingCountry`, `persona:PlaceOfBirth`, `persona:GenderMarker`, `persona:IssueDate`, `persona:Credential`, `persona:WebURL`, `persona:OrganizationUnit`, `persona:JobTitle`), complex classes (`persona:Anniversary`, `persona:PersonalInfo`), and properties (`persona:hasAnniversary`, `persona:hasPhoto`, etc.) |
| `shacl/birthcertificate-shacl.ttl` | Per-template SHACL shapes for birth certificate context files — run against the individual context file, not merged data |
| `shacl/jscontactcard-shacl.ttl` | Per-template SHACL shapes for JSContactCard context files — run against the individual context file, not merged data |
| `shacl/driverslicense-shacl.ttl` | Per-template SHACL shapes for driver's license context files — run against the individual context file, not merged data |
| `shacl/passport-shacl.ttl` | Per-template SHACL shapes for passport context files — run against the individual context file, not merged data |
| `project_files/` | Reference materials: imported domain ontologies (PersonOntology.ttl, AddressOntology.ttl, StagingOntology.ttl), BFO/CCO source files, PDFs, docs |

## Example Files

| File | Purpose |
|------|---------|
| `example/contexts/paula-walker.self(paula-walker)(acme)(06).databook.md` | Paula Walker as Alice's Acme colleague — asserted by Alice |
| `example/contexts/paula-walker.self(paula-walker)(family)(07).databook.md` | Paula Walker as Alice's family member — asserted by Alice |
| `example/contexts/paula-walker.paula-walker(paula-walker)(family)(05).databook.md` | Paula Walker's own family persona; social network with Alice |
| `example/contexts/self.bob-johnson(bob-johnson)(people)(08).databook.md` | Alice Walker as seen by Bob Johnson — asserted by Bob |
| `example/contexts/bob-johnson.self(bob-johnson)(people)(04).databook.md` | Alice's notes about Bob Johnson; favorite drink: oat milk cappuccino |
| `example/contexts/bob-johnson.bob-johnson(bob-johnson)(people)(02).databook.md` | Bob Johnson's self-asserted persona; social network with Alice |
| `example/contexts/self.self(boston-hub-society)(affiliations)(14).databook.md` | Alice's Boston Hub Society profile — email, phone, and current address |
| `example/contexts/bhs-group.members(boston-hub-society)(affiliations)(01).databook.md` | BHS Group — g:Group instance with Alice and Bob as members |
| `example/contexts/bob-johnson.bob-johnson(boston-hub-society)(affiliations)(03).databook.md` | Bob Johnson's BHS member persona — name, email, phone, address |
| `example/contexts/self.citibank(citibank)(financial-services)(09).databook.md` | Alice's Citibank context — debit card; asserted by Citibank |
| `example/contexts/self.self(google)(companies)(16).databook.md` | Alice's Google context — Gmail address |
| `example/contexts/self.self(att)(companies)(11).databook.md` | Alice's AT&T context — phone number |
| `example/contexts/self.self(texas-vital-records)(state)(24).databook.md` | Alice's Texas birth certificate — legal names, maiden name |
| `example/contexts/self.self(paradise)(municipality)(18).databook.md` | Alice's Paradise, CA address — current residence (2025–present) |
| `example/contexts/self.self(boston)(municipality)(13).databook.md` | Alice's Boston, MA address — previous residence (2020–2025) |
| `example/contexts/self.self(social-security-administration)(federal)(23).databook.md` | Alice's Social Security Number |
| `example/contexts/self.self(bob-johnson)(people)(12).databook.md` | Alice's 1:1 context with Bob; social network with Bob as member |
| `example/contexts/self.self(paula-walker)(family)(21).databook.md` | Alice's family context — social network with Paula Walker as member |
| `example/contexts/self.self(ownership)(22).databook.md` | Alice's possessions — wallet, health insurance card, SSN card |
| `example/contexts/self.self(paula-walker)(acme)(20).databook.md` | Alice's Acme employee context; social network with Paula Walker |
| `example/contexts/self.self(alice-walker)(acme)(10).databook.md` | Alice's business card (JSContactCard) — name, email, phone, employer, job title |
| `example/contexts/self.self(california-dmv)(state)(15).databook.md` | Alice's California driver's license — legal name, DOB, DL#, expiry, photo |
| `example/contexts/self.self(passport)(federal)(19).databook.md` | Alice's US passport — legal name, DOB, passport#, issue/expiry, place of birth, gender marker, photo |
| `example/contexts/self.self(health)(17).databook.md` | Alice's physical characteristics — height, eye color, hair color |
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
  ├─ example/contexts/paula-walker.self(paula-walker)(family)(07).databook.md
  ├─ … (all numbered context DataBooks)
  └─ example/contexts/self.self(health)(17).databook.md

persona-shacl.ttl — no owl:imports of data; validated against the loaded dataset
shacl/birthcertificate-shacl.ttl  — per-template shapes for birth certificate files
shacl/jscontactcard-shacl.ttl     — per-template shapes for JSContactCard files
shacl/driverslicense-shacl.ttl    — per-template shapes for driver's license files
shacl/passport-shacl.ttl          — per-template shapes for passport files
```

1. **Foundation**: BFO (Basic Formal Ontology) — provides temporal modeling (`TemporalInterval`) and core relations
2. **Domain Ontologies** (in `project_files/`): PersonOntology, AddressOntology, StagingOntology
3. **Application Ontologies** (peer, not nested):
   - `persona.ttl`: aggregates domain ontologies; uses annotation properties (`usesRequiredClass`, `usesOptionalClass`, `usesCCOClass`, `usesCCOProperty`) to document Mee's usage
   - `context.ttl`: defines `category`, `assertedBy`, `subject`, and `about-by` vocabularies; imported directly by each context file
   - `category.ttl`: defines the category class hierarchy and classification/link properties; mutually imports `context.ttl`

### Context File Naming Convention

Context filenames follow a single flat pattern:

```
<subject>.<asserted-by>(<containing-category>)(<NN>).databook.md
```

| Segment | Meaning |
|---------|---------|
| `<subject>` | The entity the Persona is about. Use `self` when the subject is the Mia user's own `p:Person` (`:Self`); otherwise use the full hyphenated lowercase name (e.g. `paula-walker`, `bob-johnson`, `bhs-group`). |
| `<asserted-by>` | Who asserted the data. Use `self` when the asserter is `:Self`; use the full hyphenated lowercase name for other asserters (e.g. `bob-johnson`, `citibank`); use the literal `members` for `c:MultiParty` contexts where any permitted member may write. |
| `(<containing-category>)` | The local-name portion of this context's `mia.category` IRI — i.e., the IRI of the category DataBook that directly holds the `sbs`, `obs`, `sbo`, or `obo` link to this context. When the category DataBook local name includes a `(parent)` qualifier (e.g. `bob-johnson(people)`), the filename uses two separate parenthetical segments before the number: `(bob-johnson)(people)`. Examples: `(bob-johnson)(people)`, `(boston-hub-society)(affiliations)`, `(paula-walker)(family)`, `(citibank)(financial-services)`. For categories without a `(parent)` qualifier (e.g. `health`, `ownership`), a single segment suffices. |
| `(<NN>)` | Zero-padded two-digit context number in parentheses, matching the diagram label. |

**Exception — `c:MultiParty` contexts**: A group context (`category context:MultiParty`) has no single asserter — any permitted member can write to it and changes replicate to all members. The `<asserted-by>` segment is the literal `members` rather than an individual name. Example: `bhs-group.members(boston-hub-society)(affiliations)(01).databook.md` — about BHS Group, containing category "boston-hub-society(affiliations)", asserted by the group's members collectively.

**`mia.assertedBy` vocabulary**: The YAML field takes the local IRI of a `p:Person`, `g:Group`, or `o:Organization` individual — NOT an `i:PDNidentifier`. Those individuals carry their own PDN identity via `identity:hasPDNidentifier`. Specifically: `:Self` (the Mia user's `p:Person`) for self-asserted contexts; a named `p:Person` individual (e.g. `:Bob_Johnson`) when another Mia user asserts the data; a named `g:Group` individual (e.g. `:BHS_Group`) for group contexts; and a named `o:Organization` individual (e.g. `:Citibank`) only when the asserting organization is itself a PDN node. In the example data **only Citibank is a PDN node**, so only `self.citibank(citibank)(financial-services)(09).databook.md` uses `assertedBy: ":Citibank"`. All other organization-related contexts (Google, AT&T, SSA, etc.) use `assertedBy: ":Self"` because Alice self-enters that data — those organizations are not PDN-interoperable.

**"Other" asserters**: When the asserter is someone other than the current Mia user (`:Self`), the asserter is a named individual of one of:
- `p:Person` — another Mia user (a different person, e.g. `:Bob_Johnson` asserting data about Alice)
- `o:Organization` — a company, nonprofit, or government agency that is a PDN node (e.g. `:Citibank`)
- `g:Group` — a group of Mia users (e.g. `:BHS_Group`)

**Examples:**

| Filename | Subject | Asserted by | Containing category |
|----------|---------|-------------|---------------------|
| `self.citibank(citibank)(financial-services)(09).databook.md` | Self (Alice) | Citibank | citibank(financial-services) |
| `paula-walker.self(paula-walker)(family)(07).databook.md` | Paula Walker | Self (Alice) | paula-walker(family) |
| `self.bob-johnson(bob-johnson)(people)(08).databook.md` | Self (Alice) | Bob Johnson | bob-johnson(people) |
| `bob-johnson.bob-johnson(boston-hub-society)(affiliations)(03).databook.md` | Bob Johnson | Bob Johnson | boston-hub-society(affiliations) |
| `bhs-group.members(boston-hub-society)(affiliations)(01).databook.md` | BHS Group | members (group) | boston-hub-society(affiliations) |

### Key Architectural Patterns

**All data belongs to contexts**: There is no separate selfness file. Every piece of identity data — names, identifiers, addresses, payment cards, physical characteristics — belongs to a context-specific Persona file. The Mia user's `persona:Person` individual (IRI `:Self`) is declared in each context file; there is no single root file that owns the declaration.

**`:Self` IRI convention**: The Mia user's own `persona:Person` individual always uses the IRI `:Self` across all of their context files. All other people, groups, and organizations are assigned locally-minted named IRIs (e.g. `:Bob_Johnson`, `:Paula_Walker`, `:BHS`). `:Self` is a local IRI and is never exposed externally over the PDN, so there are no collisions between Mia instances. All context files in the example live in Alice's Mia — some authored by Alice, others received from peers over PDN. In either case, `:Self` refers to Alice. When data arrives from a peer's Mia (where that peer was `:Self` in their own instance), Alice's Mia assigns them a locally-minted identifier; once a PDN connection is established, that identifier resolves to or is replaced by their PDN ID.

**DataBook IRI convention**: The document `id:` and `graph.named_graph:` always differ by the `#graph` fragment — `named_graph` is always `{id}#graph`. The `databook:id` on a block is a fragment identifier making that block independently addressable as `{id}#{block-id}`. Overview sections always begin with "This context captures...".

**Peer name pattern** (not hierarchical): All name types (FullName, GivenName, FamilyName, AlternateName) connect directly to a Persona via `ont00001879` (designated by). They are siblings, not nested. Names belong to Personas not to Persons.

**Address history pattern**: `AddressDesignation` links Person → Address → `TemporalInterval`. Open-ended intervals (no `hasEndDate`) indicate current address.

**Named graph scoping of `BFO_0000115`**: When a Social Network individual carries `BFO_0000115 :Paula_Walker`, the triple is intentionally scoped to the enclosing named graph — it refers to Paula Walker *as a person entity*, with context-specific isolation provided by the DataBook named graph architecture, not by the triple itself. Queries needing context-specific member data must target the relevant named graphs (e.g. context 18 + context 02) rather than querying the full merged dataset. Do NOT change the range of `BFO_0000115` to a document IRI (breaks BFO semantics — range must be a continuant, not a document), and do NOT introduce context-specific person individuals (reintroduces the complexity that removing the layered Persona model eliminated). RDF-star annotation is a valid future option if tooling matures.

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

Before committing any change to any context file, `persona.ttl`, `context.ttl`, `category.ttl`, or `persona-shacl.ttl`, increment the **minor version number** in that file's `owl:versionInfo` annotation and update the description to summarise the change. For example:

```
owl:versionInfo "Version 3.0.3 - added social network"@en
```
becomes:
```
owl:versionInfo "Version 3.0.4 - added birth date"@en
```

## Integrity Checks

Files inside any directory named `under-development/` (at any depth) are works-in-progress and must be **excluded from all integrity checks** below.

After any change to context files or category DataBooks, verify the following.

**Check 1 — Diagram ↔ files ↔ README coverage**: Every numbered context circle in any of the 9 category diagrams (`example/images/`) must have (a) a corresponding `.databook.md` file in `example/contexts/` and (b) a row in one of the tables in the **Alice's Personas and Contexts** section of `README.md`. Conversely, every row in those tables must correspond to a numbered circle in a diagram and a file that actually exists. If a circle exists in a diagram but has no `.databook.md` file or README row, create them to match the diagram.

**Check 2 — Filename convention**: Every context filename must follow `<subject>.<asserted-by>(<containing-category>)(<NN>).databook.md`. `<subject>` must be `self` when the subject is `:Self`, or the full hyphenated lowercase name otherwise. `<asserted-by>` must be `self` when the asserter is `:Self`, or the full hyphenated lowercase name otherwise — except for `c:Group` contexts, where it must be the literal string `members`. `(<containing-category>)` encodes the local name of the `mia.category` IRI: when the category DataBook local name includes a `(parent)` qualifier (e.g. `bob-johnson(people)`), it appears as two separate segments `(bob-johnson)(people)`; when there is no qualifier (e.g. `health`), a single segment suffices. `(<NN>)` is the zero-padded two-digit context number. If a filename does not match this pattern, rename it to conform.

**Check 3 — `mia.category` ↔ filename consistency**: For every context DataBook in `example/contexts/` (excluding `under-development/`), the local-name portion of its `mia.category` IRI must equal the `(<containing-category>)` segment extracted from the filename. When the filename uses two separate parenthetical segments before the number (e.g. `(bob-johnson)(people)`), concatenate them as `bob-johnson(people)` to form the expected local name. Run:

```python
import os, re

cat_dir = 'example/categories'
ctx_dir = 'example/contexts'
base_cat = 'http://www.example.org/mia/categories/'

def fn_cat_local(fname):
    base = fname[:-len('.databook.md')]
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
    cat_m = re.search(r'^\s+category:\s+"([^"]+)"', text, re.MULTILINE)
    if not cat_m:
        print(f'NO mia.category: {fname}'); errors += 1; continue
    cat_local = cat_m.group(1)
    if cat_local.startswith(base_cat):
        cat_local = cat_local[len(base_cat):]
    expected = fn_cat_local(fname)
    if cat_local != expected:
        print(f'MISMATCH {fname}:')
        print(f'  filename implies: {expected!r}')
        print(f'  mia.category has: {cat_local!r}')
        errors += 1
if not errors:
    print('All mia.category values match filenames.')
```

If mismatches appear, the filename `(<containing-category>)` segments are authoritative — update the `mia.category` IRI in the DataBook to match (or vice versa if the filename was misnamed).

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

**Check 9 — `about-by` ↔ `subject`/`assertedBy` consistency**: Every DataBook's `mia.about-by` value must be consistent with its `mia.subject` and `mia.assertedBy` values according to these rules:

| `about-by` | `subject` | `assertedBy` |
|---|---|---|
| `context:SBScontext` | `:Self` | `:Self` |
| `context:OBScontext` | not `:Self` | `:Self` |
| `context:OBOcontext` | not `:Self` | not `:Self` |
| `context:SBOcontext` | `:Self` | not `:Self` |

For each DataBook in `example/` (excluding `under-development/`), extract the three YAML values and verify they match the table. If they conflict, `about-by` is the authoritative value — update `subject` and/or `assertedBy` to match it.

**Check 10 — Category filename ↔ id consistency**: For every category DataBook in `categories-person/`, `categories-org/`, and `example/categories/`, the filename root (the filename with `.databook.md` stripped) must exactly match the local name portion of the file's `id:` IRI (the string after the IRI base). The IRI base for canonical Person files is `http://mee.foundation/ontologies/categories-person/`; for canonical Organization files it is `http://mee.foundation/ontologies/categories-org/`; for example files it is `http://www.example.org/mia/categories/`. Run:

```python
import os, re
checks = [
    ('categories-person', 'http://mee.foundation/ontologies/categories-person/'),
    ('categories-org',     'http://mee.foundation/ontologies/categories-org/'),
    ('example/categories', 'http://www.example.org/mia/categories/'),
]
for directory, base in checks:
    for fname in sorted(os.listdir(directory)):
        if not fname.endswith('.databook.md'):
            continue
        root = fname[:-len('.databook.md')]
        text = open(f'{directory}/{fname}').read()
        m = re.search(r'^id:\s*(\S+)', text, re.MULTILINE)
        fid = m.group(1).strip() if m else ''
        local = fid[len(base):] if fid.startswith(base) else None
        if local != root:
            print(f'MISMATCH  {directory}/{fname}  root={root!r}  id={local!r}')
```

If a mismatch is found, rename the file so its root matches the id local name (preferred) or update the `id:` to match the filename — whichever is consistent with the broader naming conventions.

**Check 11 — Example category diagrams are authoritative**: The 9 category diagrams in `example/images/` are the authoritative source of truth for the example category tree. When any discrepancy is found between a diagram and the DataBook files, the diagram wins — update the DataBooks to match, not the other way around. After any change to `example/categories/` DataBooks or to the 9 diagrams, verify all of the following:

- **11a — Every category box has a DataBook**: Every category box (blue predefined or white user-defined) shown in any of the 9 diagrams must have a corresponding `.databook.md` file in `example/categories/` whose `title:` matches the box label. If a box has no DataBook, create one.

- **11b — Every DataBook has a diagram box**: Every `.databook.md` file in `example/categories/` (except `categories.databook.md` itself, which is the invisible root) must appear as a visible box in at least one of the 9 diagrams. If a DataBook has no corresponding box, either add it to the appropriate diagram or delete the DataBook.

- **11c — Solid context circles match DataBook links**: Every solid (filled) context circle attached to a category box indicates a real context link. The category DataBook for that box must carry the corresponding `sbs`, `obs`, `obo`, or `sbo` field pointing to the context DataBook IRI. A dashed (empty) circle indicates an unfilled slot — the DataBook must NOT have a link for that slot.

- **11d — Numbered context circles have matching files**: Every numbered context circle (e.g. `[10]`, `[17]`) shown in a diagram must correspond to an actual `.databook.md` file in `example/contexts/` whose filename contains that number (e.g. `(10)`, `(17)`).

- **11e — Child arrows match DataBook child links**: Every downward child arrow from category box A to category box B in a diagram must correspond to a `child:` entry in A's DataBook pointing to B's IRI. Conversely, every `child:` entry in a DataBook must be reflected by a visible child arrow in the diagram.

The 9 diagrams are: `example/images/people.png`, `example/images/work.png`, `example/images/companies.png`, `example/images/finances.png`, `example/images/gov-state.png`, `example/images/gov-federal.png`, `example/images/gov-municipality.png`, `example/images/misc.png`, `example/images/affiliations.png`.

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

All classes and properties defined in `persona.ttl`, `context.ttl`, and `category.ttl` must be mentioned in `README.md` in the sections before the **Illustrative Example: Alice Walker** section. The only intentional exceptions are the internal ontology documentation annotation properties (`usesRequiredClass`, `usesOptionalClass`, `usesCCOClass`, `usesCCOProperty`, `usagePattern`), which are infrastructure for self-documenting the ontology, not user-facing terms.

In `README.md`, every mention of a class defined in `persona.ttl` must appear in backticks with the `p:` prefix (e.g. `p:Persona`, `p:Wallet`), every mention of a class or property defined in `context.ttl` must appear in backticks with the `c:` prefix (e.g. `c:contextType`, `c:SelfAsserted`), and every mention of a class or property defined in `category.ttl` must appear in backticks with the `cat:` prefix (e.g. `cat:Category`, `cat:classname`). Every capitalized mention of `Person` (the CCO class) must also appear in backticks. These formatting rules do **not** apply inside headings or subheadings.

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
