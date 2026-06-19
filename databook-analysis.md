<title>DataBook Migration Analysis — MIA Context Files</title>

# DataBook Migration Analysis: MIA Context Files

**Date:** 2026-06-18  
**Spec:** [DataBook Handbook](https://github.com/w3c-cg/holon/blob/main/architectures/databook/databook-handbook.databook.md)  
**CLI:** [DataBook CLI v1.4.4](https://github.com/w3c-cg/holon/tree/main/architectures/databook)  
**Status:** Exploratory — no changes made to the repository

---

## 1. What a DataBook Is

A `.databook.md` file is a double-extension Markdown file that is simultaneously three things:

- A **human-readable document** (standard Markdown, renders in any viewer)
- A **named-graph RDF container** (fenced turtle/sparql/shacl blocks carry the data)
- A **self-describing provenance record** (structured PROV-O authorship in frontmatter)

### Structure

```
--- YAML frontmatter (required first) ---
Markdown prose + fenced RDF/SPARQL/SHACL blocks (freely interleaved)
```

### Frontmatter

Required fields:

```yaml
---
id: https://example.org/databooks/my-book-v1   # stable absolute IRI
title: "Human-readable title"
type: databook
version: 1.0.0
created: 2026-06-18
---
```

Important optional fields:

```yaml
description: >
  Multi-line prose description.
graph:
  namespace: https://example.org/data/
  named_graph: https://example.org/databooks/my-book-v1#graph  # real named graph IRI
  rdf_version: "1.1"
shapes:
  - https://example.org/shapes/MyShape          # formal SHACL pointer
process:                                         # PROV-O activity stamp
  transformer: human
  timestamp: 2026-06-18T00:00:00Z
  agent:
    name: Paul Trevithick
    role: author
```

### Fenced Blocks

Each block is preceded by HTML comments that configure how parsers and renderers handle it:

```markdown
<!-- databook:id: identity-data -->
<!-- databook:graph: https://example.org/databooks/my-book-v1#graph -->
<!-- mode=hidden -->
```turtle
@prefix : <https://example.org/data#> .
:Alice a <http://mee.foundation/ontologies/persona#Person> .
` ``
```

The `databook:id` comment makes the block independently addressable as `{doc-id}#{block-id}`.

**`mode` values:**

| Mode | Behaviour |
|---|---|
| `executed` | Run against a SPARQL endpoint |
| `rendered` | Pass to a rendering engine |
| `printed` | Syntax highlight only (default display) |
| `hidden` | Invisible in rendered view; present for parsers and LLMs |
| `reference` | Surfaceable on demand |

**Supported fence languages:** `turtle`, `turtle12`, `sparql`, `sparql-update`, `shacl`, `json-ld`, `trig`, `n-triples`, `n-quads`, `prompt`, `manifest`, `encrypted-turtle`.

---

## 2. Our Current Model vs. DataBook

Each MIA context file is a `.ttl` file acting as a "poor man's named graph": an `owl:Ontology` IRI borrowed as a de-facto graph name, with annotation properties on that IRI serving as graph-level metadata.

| Dimension | Our `.ttl` approach | DataBook |
|---|---|---|
| Graph IRI | `owl:Ontology` IRI used as de-facto graph name | `graph.named_graph: {id}#graph` — a real named-graph IRI |
| Graph-level metadata | Annotation properties on the ontology node | Frontmatter YAML + optional hidden RDF block |
| Human readability | Code comments only | Full Markdown prose between blocks |
| Provenance | `dc:date` + `owl:versionInfo` string | Structured PROV-O `process:` stamp |
| SHACL pointer | External convention only | `shapes:` frontmatter field |
| Block addressing | Whole-file only | Fragment IRIs: `{doc-id}#{block-id}` |
| SPARQL queries | Separate files | Embedded `sparql` blocks alongside the data |
| Authoring | Claude (writes `.ttl`) | Claude (writes `.databook.md`) — equally natural |
| Tooling | Protégé (inspection), Apache Jena, `shaclvalidate` | DataBook CLI + standard Markdown renderers |

---

## 3. Property Mapping

| Our `owl:Ontology` property | DataBook destination | Notes |
|---|---|---|
| Ontology IRI | `id:` | 1:1 |
| `rdfs:label` | `title:` | 1:1 |
| `rdfs:comment` | `description:` + prose sections | Richer in databook |
| `dc:date` | `created:` | 1:1 |
| `owl:versionInfo "Version X.Y.Z - ..."` | `version:` + intro prose | Split: number → `version:`, description → prose |
| `context:name "Citibank"` | `mia.name:` in YAML | No standard equivalent |
| `context:contextCategory` | `mia.contextCategory:` in YAML **and** hidden turtle block | See design decision below |
| `context:assertedBy` | `mia.assertedBy:` in YAML **and** hidden turtle block | |
| `context:subject` | `mia.subject:` in YAML **and** hidden turtle block | |
| `context:template` | `mia.template:` in YAML **and** hidden turtle block | |
| `context:dyad` | `mia.dyad:` in YAML **and** hidden turtle block | |
| `owl:imports` | Not needed | Ontologies pre-loaded into triplestore; no file-level import chain |
| *(absent today)* | `graph.named_graph: {id}#graph` | New — real named-graph IRI |
| *(absent today)* | `shapes:` | Formal SHACL pointer |
| *(absent today)* | `process:` | PROV-O provenance stamp |

### Design decision: `context:` annotation properties

These are proper RDF terms defined in `context.ttl` and are part of the ontological model. Two options:

- **Option A — YAML only:** Move to `mia:` namespace in frontmatter. Clean and scannable, but they lose RDF semantics and SPARQL queryability unless a processor maps them back.
- **Option B — Hidden RDF block:** Keep as RDF triples in a `mode=hidden` turtle block. Preserves full semantics; the block is invisible in rendered views but present for parsers and LLMs.
- **Option C — Hybrid (recommended):** Put human-readable keys in `mia:` YAML for scannability; keep the authoritative triples in a hidden block. Redundant, but both audiences are served.

---

## 4. Concrete Example: Citibank File Converted

Current `.ttl` (abbreviated):

```turtle
<http://www.example.org/mia/alice(citibank)citibank> rdf:type owl:Ontology ;
    owl:imports <http://mee.foundation/ontologies/persona> ;
    owl:imports <http://mee.foundation/ontologies/context> ;
    context:contextCategory context:FinancialServices ;
    context:assertedBy identity:Organization ;
    context:subject identity:Self ;
    context:name "Citibank" ;
    rdfs:label "Alice Walker - Citibank Persona"@en .

:Alice_Walker rdf:type owl:NamedIndividual , persona:Person ;
    rdfs:label "Alice Walker (Citibank)"@en ;
    persona:hasPaymentCard :Alice_Debit_Card ;
    persona:hasBankAccount :Alice_Checking_Account .
```

Proposed `.databook.md`:

```markdown
---
id: http://www.example.org/mia/alice(citibank)citibank
title: "Alice Walker — Citibank"
type: databook
version: 2.0.1
created: 2026-06-15
description: >
  Alice Walker's Citibank context. Records her debit card, checking account,
  and online banking credentials. Asserted by Citibank (a PDN Organization node).
mia:
  name: "Citibank"
  contextCategory: "context:FinancialServices"
  assertedBy: "identity:Organization"
  subject: "identity:Self"
graph:
  namespace: http://www.example.org/mia#
  named_graph: http://www.example.org/mia/alice(citibank)citibank#graph
  rdf_version: "1.1"
shapes:
  - http://www.example.org/shapes          # IRI of persona-shacl.ttl (Tier 1 — all contexts)
process:
  transformer: human
  timestamp: 2026-06-15T00:00:00Z
  agent:
    name: Paul Trevithick
    role: author
---

## Overview

Alice Walker's financial relationship with Citibank. Citibank is a PDN Organization
node and directly asserts this context. It holds a debit card linked to a checking
account, plus an online service account for `online.citi.com`.

## Identity Data

<!-- databook:id: alice-citibank -->
<!-- databook:graph: http://www.example.org/mia/alice(citibank)citibank#graph -->
```turtle
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Alice_Walker rdf:type owl:NamedIndividual , persona:Person ;
    rdfs:label "Alice Walker (Citibank)"@en ;
    persona:hasPaymentCard :Alice_Debit_Card ;
    persona:hasBankAccount :Alice_Checking_Account ;
    cco:ent00000045 :Alice_Citibank_Online .

:Alice_Debit_Card rdf:type owl:NamedIndividual , cco:ent00000051 ;
    rdfs:label "Alice Walker's VISA Debit Card"@en ;
    <https://purl.org/cco/ont00001879> [
        rdf:type cco:ent00000052 ;
        <https://purl.org/cco/ont00001765> "4111-1111-1111-1111"
    ] ;
    persona:accessesBankAccount :Alice_Checking_Account .

:Alice_Checking_Account rdf:type owl:NamedIndividual , persona:CheckingAccount ;
    rdfs:label "Alice Walker's Citibank Checking Account"@en ;
    <https://purl.org/cco/ont00001879> [
        rdf:type persona:CheckingAccountNumber ;
        <https://purl.org/cco/ont00001765> "9876543210"
    ] ;
    <https://purl.org/cco/ont00001879> [
        rdf:type persona:RoutingNumber ;
        <https://purl.org/cco/ont00001765> "021000089"
    ] .

:Alice_Citibank_Online rdf:type owl:NamedIndividual , cco:ent00000033 ;
    rdfs:label "Alice Walker's Citibank Online Account"@en ;
    cco:ent00000034 "Citibank" ;
    cco:ent00000035 "awalker@gmail.com" ;
    cco:ent00000036 "https://online.citi.com" ;
    persona:hasPassword "C1t1b@nk#2024!" .
` ``
```

### Note: two-tier shapes for template context files

`http://www.example.org/shapes` is the ontology IRI declared inside `persona-shacl.ttl`
(its `owl:Ontology` declaration reads `<http://www.example.org/shapes> rdf:type owl:Ontology`).
It is the Tier 1 shapes file that applies to **every** context file.

Context files that carry a `context:template` annotation (birth certificate, JSContactCard,
driver's license) need a second entry for their per-template Tier 2 shapes file:

```yaml
# Birth certificate — Tier 1 + Tier 2
shapes:
  - http://www.example.org/shapes                        # persona-shacl.ttl
  - http://www.example.org/shapes/birthcertificate       # shacl/birthcertificate-shacl.ttl

# JSContactCard — Tier 1 + Tier 2
shapes:
  - http://www.example.org/shapes                        # persona-shacl.ttl
  - http://www.example.org/shapes/jscontactcard          # shacl/jscontactcard-shacl.ttl

# Driver's license — Tier 1 + Tier 2
shapes:
  - http://www.example.org/shapes                        # persona-shacl.ttl
  - http://www.example.org/shapes/driverslicense         # shacl/driverslicense-shacl.ttl
```

---

## 5. DataBook CLI (v1.4.4) — 20 commands

The CLI is grouped into three families: **Document Structure** (`create`, `head`, `insert`, `drop`, `extract`, `convert`, `ingest`), **Triplestore** (`push`, `pull`, `sparql`, `sparql-update`, `validate`, `describe`, `clear`, `list`), and **Pipeline** (`process`, `transform`, `prompt`, `fetch`, `shacl2sparql`).

### Blocker-by-blocker assessment

**✅ `riot`/`shaclvalidate` need `.ttl` — solved**

`databook extract` and `databook convert` both emit plain Turtle from a named block:

```bash
databook extract 10-alice(citibank)citibank.databook.md#alice-citibank -o graph.ttl
databook convert 10-alice(citibank)citibank.databook.md#alice-citibank --to turtle -o graph.ttl
```

`databook validate` replaces `shaclvalidate` outright — it runs SHACL natively via Jena, and `--shapes` accepts either a databook block reference or a plain `.ttl` path, so our existing `persona-shacl.ttl` and `shacl/*.ttl` files work without conversion:

```bash
# Tier 1
databook validate 10-alice(citibank)citibank.databook.md \
    --shapes persona-shacl.ttl --fail-on-violation

# Tier 2 (template file)
databook validate 13-alice(tx-birth-cert)alice.databook.md \
    --shapes shacl/birthcertificate-shacl.ttl --fail-on-violation
```

**✅ `owl:imports` composition — addressed via triplestore**

No file-level `owl:imports` equivalent exists, but the intended pattern is clean: **pre-load foundation ontologies into a Jena Fuseki triplestore once**, then each context databook pushes its slice alongside them via `databook push`. The triplestore handles the union — no file-level import chain needed. `databook insert`, `databook process`, and `databook fetch` handle DataBook-to-DataBook composition in pipeline workflows.

**✅ SPARQL, LLM, triplestore — new capabilities**

`databook sparql` runs SELECT/CONSTRUCT/ASK against embedded blocks or a Fuseki endpoint. `databook shacl2sparql` compiles SHACL NodeShapes to SPARQL retrieval queries — useful for generating identity views. `databook push`/`pull` loads data to Fuseki via Graph Store Protocol. `databook prompt` sends the whole file to an LLM with full provenance tracking.

**⚠️ Protégé — minor friction, not a blocker**

The CLI has no native Protégé integration. However, since Claude is the primary authoring tool (not Protégé), this is acceptable: a small `databook extract` pre-processing script run before each Protégé inspection session produces the temp `.ttl` files Protégé needs. One script, run on demand.

### CLI blocker table

| Blocker | CLI command | Status |
|---|---|---|
| `riot`/`shaclvalidate` need `.ttl` | `extract`, `convert` | ✅ Solved |
| SHACL validation workflow | `validate` (Jena-native) | ✅ Replaces current workflow |
| `owl:imports` chain composition | `push` + Fuseki triplestore | ⚠️ Requires Fuseki running |
| Triplestore loading | `push` / `pull` | ✅ New capability |
| SPARQL queries over data | `sparql`, `shacl2sparql` | ✅ New capability |
| LLM integration | `prompt` | ✅ New capability |
| Protégé compatibility | `extract` pre-processing script | ⚠️ Minor friction — acceptable |

---

## 6. What We Gain

1. **True named graphs** — `graph.named_graph` gives each context a real RDF 1.1 named-graph IRI rather than borrowing the ontology IRI for double duty.
2. **Natural authoring** — Claude authors `.databook.md` as easily as `.ttl`; markdown with YAML frontmatter and fenced code blocks is if anything a more comfortable format to write and review.
3. **Human-readable prose** — Markdown sections make each context file self-documenting in plain English, without code comments.
4. **Cleaner header metadata** — `id`, `title`, `version`, `description`, `created` are standard fields any reader can understand without knowing OWL.
5. **Built-in provenance** — structured PROV-O `process:` stamps replace ad-hoc `owl:versionInfo` strings.
6. **Formal SHACL pointer** — `shapes:` frontmatter field links data to its validation constraints explicitly rather than by convention.
7. **Fragment IRI addressing** — `…citibank#alice-citibank` lets tooling retrieve just the identity block independently.
8. **Embedded SPARQL** — per-context queries can live alongside the data.
9. **Encryption profile** — sensitive blocks (SSN, payment card numbers) can be encrypted at rest while structural metadata stays readable.
10. **No `owl:Ontology` boilerplate** — the `owl:Ontology` header with its annotation-property workarounds disappears entirely; frontmatter handles everything it did.

---

## 7. Remaining Concerns

1. **Fuseki dependency for `owl:imports` composition** — the triplestore-centric model requires Fuseki to be running for full union queries. File-system-only workflows (current) would need a running triplestore.

2. **`context:` annotation properties have no standard home** — `context:contextCategory`, `context:assertedBy`, `context:subject`, `context:template`, `context:dyad` are our own RDF terms. The recommended hybrid approach (readable strings in `mia:` YAML + authoritative triples in a hidden block) works but is slightly redundant.

3. **Ecosystem immaturity** — DataBook is a W3C Community Group draft at v1.2/CLI v1.4.4. Smaller ecosystem than the Jena/SHACL stack, though the CLI already uses Jena under the hood.

4. **File-reference churn** — 22 context files, plus references in `README.md`, `CLAUDE.md`, `alice(self)alice.ttl` imports, and both catalog files, would all need updating.

---

## 8. Recommendation

The case for full migration is now strong. The primary blockers have been resolved:

- **Authoring** is unchanged — Claude writes databooks as naturally as Turtle.
- **SHACL validation** is replaced by `databook validate` (same Jena engine, simpler commands).
- **Protégé** is an inspection tool, not an authoring tool — a `databook extract` script before each session is acceptable.
- **The `owl:Ontology` workaround disappears** — the core architectural problem is solved cleanly.

The remaining concerns (Fuseki dependency, `context:` property placement, ecosystem maturity, file churn) are real but manageable. A full migration would be a well-scoped project: convert 22 context files, update catalog and import references, write the Protégé extraction script, and replace the README validation commands with `databook validate` equivalents.
