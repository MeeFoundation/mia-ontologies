# DataBook Migration Analysis: Mia Context Files

**Date:** 2026-06-18  
**Spec:** [DataBook Handbook](https://github.com/w3c-cg/holon/blob/main/architectures/databook/databook-handbook.databook.md)  
**CLI:** [DataBook CLI v1.4.4](https://github.com/w3c-cg/holon/tree/main/architectures/databook)  
**Status:** Exploratory — no changes made to the repository

---

## 1. Background

Each Mia context file is currently a `.ttl` (Turtle RDF) file that acts as a "poor man's named graph." Because plain Turtle has no native support for named graphs or graph-level metadata, we work around this limitation by declaring an `owl:Ontology` and hanging annotation properties off its IRI:

```turtle
<http://www.example.org/mia/alice(citibank)citibank> rdf:type owl:Ontology ;
    owl:imports <http://mee.foundation/ontologies/persona> ;
    owl:imports <http://mee.foundation/ontologies/context> ;
    context:contextCategory context:FinancialServices ;
    context:assertedBy identity:Organization ;
    context:subject identity:Self ;
    context:name "Citibank" ;
    owl:versionInfo "Version 2.0.1"@en ;
    rdfs:label "Alice Walker - Citibank Persona"@en .

:Self rdf:type persona:Person ;
    persona:hasPaymentCard :Alice_Debit_Card .
```

This works, but it conflates two distinct concerns: the ontology import mechanism (`owl:Ontology`, `owl:imports`) with what is really just a data container with some metadata. The result is structural boilerplate that every context file must carry, metadata that is only machine-readable if you know our custom `context:` annotation properties, and no human-readable documentation beyond code comments.

[DataBook](https://github.com/w3c-cg/holon/blob/main/architectures/databook/databook-handbook.databook.md) is a W3C Community Group format designed to solve exactly this problem.

---

## 2. What a DataBook Is

A `.databook.md` file is a double-extension Markdown file that is simultaneously three things:

- A **human-readable document** (standard Markdown, renders in any viewer)
- A **named-graph RDF container** (fenced turtle/sparql/shacl blocks carry the data)
- A **self-describing provenance record** (structured PROV-O authorship in frontmatter)

### Structure

```
--- YAML frontmatter (required, comes first) ---
Markdown prose and fenced RDF/SPARQL/SHACL blocks (freely interleaved)
```

### Frontmatter

```yaml
---
id: https://example.org/databooks/my-book-v1   # stable absolute IRI
title: "Human-readable title"
type: databook
version: 1.0.0
created: 2026-06-18
description: >
  Multi-line prose description.
graph:
  named_graph: https://example.org/databooks/my-book-v1#graph  # real named graph IRI
  rdf_version: "1.1"
shapes:
  - https://example.org/shapes/MyShape   # SHACL shapes pointer
process:                                 # PROV-O authorship stamp
  transformer: human
  timestamp: 2026-06-18T00:00:00Z
  agent:
    name: Paul Trevithick
    role: author
---
```

### Fenced Blocks

Each fenced block is preceded by HTML comment directives:

```markdown
<!-- databook:id: identity-data -->
<!-- databook:graph: https://example.org/databooks/my-book-v1#graph -->
```turtle
@prefix : <https://example.org/data#> .
:Alice a <http://mee.foundation/ontologies/persona#Person> .
` ``
```

`databook:id` makes the block independently addressable as `{doc-id}#{block-id}`.

**Block `mode` values:**

| Mode | Behaviour |
|---|---|
| `executed` | Run against a SPARQL endpoint |
| `rendered` | Pass to a rendering engine |
| `printed` | Syntax highlight only (default) |
| `hidden` | Invisible in rendered view; present for parsers and LLMs |
| `reference` | Surfaceable on demand |

**Supported fence languages:** `turtle`, `turtle12`, `sparql`, `sparql-update`, `shacl`, `json-ld`, `trig`, `n-triples`, `n-quads`, `prompt`, `manifest`, `encrypted-turtle`.

---

## 3. How Our Properties Map to DataBook

| Our `owl:Ontology` property | DataBook destination | Notes |
|---|---|---|
| Ontology IRI | `id:` | 1:1 |
| `rdfs:label` | `title:` | 1:1 |
| `rdfs:comment` | `description:` + prose sections | Richer in DataBook |
| `dc:date` | `created:` | 1:1 |
| `owl:versionInfo "Version X.Y.Z - ..."` | `version:` + intro prose | Number → `version:`, description → prose |
| `context:name "Citibank"` | `mia.name:` in YAML | No standard equivalent |
| `context:contextCategory` | `mia.contextCategory:` in YAML | Human-readable string |
| `context:assertedBy` | `mia.assertedBy:` in YAML | Human-readable string |
| `context:subject` | `mia.subject:` in YAML | Human-readable string |
| `context:template` | `mia.template:` in YAML | Human-readable string |
| `context:dyad` | `mia.dyad:` in YAML | Human-readable string |
| `owl:imports` | Not needed | Ontologies pre-loaded into triplestore; no file-level import chain |
| *(absent today)* | `graph.named_graph: {id}#graph` | Real named-graph IRI |
| *(absent today)* | `shapes:` | Formal SHACL pointer |
| *(absent today)* | `process:` | PROV-O provenance stamp |

### Note on `context:` annotation properties

`context:contextCategory`, `context:assertedBy`, `context:subject`, `context:template`, and `context:dyad` are RDF annotation properties defined in `context.ttl`. Moving them to YAML frontmatter means they are stored as human-readable strings rather than RDF triples, so they are not directly SPARQL-queryable from the file. In a triplestore-centric workflow this is not a concern — the DataBook CLI loads the named graph into Fuseki where all metadata is queryable. For file-only workflows it is a trade-off worth noting.

### No `owl:Ontology` needed

The `owl:Ontology` declaration exists in our current `.ttl` files solely as a vehicle for graph-level metadata and import declarations. In a DataBook, the frontmatter covers the metadata and the triplestore model replaces `owl:imports`. The `owl:Ontology` boilerplate disappears entirely.

---

## 4. Concrete Example: Citibank File Converted

**Current `.ttl` (abbreviated):**

```turtle
<http://www.example.org/mia/alice(citibank)citibank> rdf:type owl:Ontology ;
    owl:imports <http://mee.foundation/ontologies/persona> ;
    owl:imports <http://mee.foundation/ontologies/context> ;
    context:contextCategory context:FinancialServices ;
    context:assertedBy identity:Organization ;
    context:subject identity:Self ;
    context:name "Citibank" ;
    rdfs:label "Alice Walker - Citibank Persona"@en .

:Self rdf:type owl:NamedIndividual , persona:Person ;
    persona:hasPaymentCard :Alice_Debit_Card ;
    persona:hasBankAccount :Alice_Checking_Account .
```

**Proposed `.databook.md`:**

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
node and directly asserts this context. It records a debit card linked to a checking
account, plus an online service account for `online.citi.com`.

## Identity Data

<!-- databook:id: alice-citibank -->
<!-- databook:graph: http://www.example.org/mia/alice(citibank)citibank#graph -->
```turtle
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://purl.org/cco/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Self rdf:type rdf:NamedIndividual , persona:Person ;
    rdfs:label "Alice Walker (Citibank)"@en ;
    persona:hasPaymentCard :Alice_Debit_Card ;
    persona:hasBankAccount :Alice_Checking_Account ;
    cco:ent00000045 :Alice_Citibank_Online .

:Alice_Debit_Card rdf:type rdf:NamedIndividual , cco:ent00000051 ;
    rdfs:label "Alice Walker's VISA Debit Card"@en ;
    <https://purl.org/cco/ont00001879> [
        rdf:type cco:ent00000052 ;
        <https://purl.org/cco/ont00001765> "4111-1111-1111-1111"
    ] ;
    persona:accessesBankAccount :Alice_Checking_Account .

:Alice_Checking_Account rdf:type rdf:NamedIndividual , persona:CheckingAccount ;
    rdfs:label "Alice Walker's Citibank Checking Account"@en ;
    <https://purl.org/cco/ont00001879> [
        rdf:type persona:CheckingAccountNumber ;
        <https://purl.org/cco/ont00001765> "9876543210"
    ] ;
    <https://purl.org/cco/ont00001879> [
        rdf:type persona:RoutingNumber ;
        <https://purl.org/cco/ont00001765> "021000089"
    ] .

:Alice_Citibank_Online rdf:type rdf:NamedIndividual , cco:ent00000033 ;
    rdfs:label "Alice Walker's Citibank Online Account"@en ;
    cco:ent00000034 "Citibank" ;
    cco:ent00000035 "awalker@gmail.com" ;
    cco:ent00000036 "https://online.citi.com" ;
    persona:hasPassword "C1t1b@nk#2024!" .
` ``
```

### SHACL shapes pointers for template context files

`http://www.example.org/shapes` is the ontology IRI declared inside `persona-shacl.ttl`. It is the Tier 1 shapes file that applies to every context file. Context files that carry a `mia.template` annotation (birth certificate, JSContactCard, driver's license) list both Tier 1 and their per-template Tier 2 shapes file:

```yaml
# Birth certificate
shapes:
  - http://www.example.org/shapes                        # persona-shacl.ttl (Tier 1)
  - http://www.example.org/shapes/birthcertificate       # shacl/birthcertificate-shacl.ttl (Tier 2)

# JSContactCard
shapes:
  - http://www.example.org/shapes
  - http://www.example.org/shapes/jscontactcard

# Driver's license
shapes:
  - http://www.example.org/shapes
  - http://www.example.org/shapes/driverslicense
```

---

## 5. DataBook CLI (v1.4.4)

The CLI has 20 commands in three groups: **Document Structure** (`create`, `head`, `insert`, `drop`, `extract`, `convert`, `ingest`), **Triplestore** (`push`, `pull`, `sparql`, `sparql-update`, `validate`, `describe`, `clear`, `list`), and **Pipeline** (`process`, `transform`, `prompt`, `fetch`, `shacl2sparql`).

### Commands relevant to our workflow

**Extracting turtle for Protégé**

Protégé cannot load `.databook.md` files directly. A `databook extract` pre-processing script run before each Protégé session produces the `.ttl` files it needs:

```bash
databook extract alice\(citibank\)citibank.databook.md#alice-citibank -o alice-citibank.ttl
```

**SHACL validation**

`databook validate` replaces `shaclvalidate` outright — it runs SHACL natively via Jena, and `--shapes` accepts either a DataBook block reference or a plain `.ttl` path, so our existing `persona-shacl.ttl` and `shacl/*.ttl` files work without conversion:

```bash
# Tier 1 — all contexts
databook validate 10-alice\(citibank\)citibank.databook.md \
    --shapes persona-shacl.ttl --fail-on-violation

# Tier 2 — template-specific
databook validate 13-alice\(tx-birth-cert\)alice.databook.md \
    --shapes shacl/birthcertificate-shacl.ttl --fail-on-violation
```

**Triplestore loading**

`databook push` loads all RDF blocks to Apache Jena Fuseki via the Graph Store Protocol. Foundation ontologies are pre-loaded once; each context DataBook pushes its named-graph slice alongside them. `databook pull` retrieves RDF back out by IRI.

**SPARQL queries**

`databook sparql` runs SELECT/CONSTRUCT/ASK against embedded blocks or a Fuseki endpoint. `databook shacl2sparql` compiles SHACL NodeShapes to SPARQL retrieval queries, useful for generating views over identity data.

**LLM integration**

`databook prompt` sends the full file — prose, metadata, and RDF — to an LLM endpoint with provenance tracking baked in.

---

## 6. Pros and Cons

### Pros

| | |
|---|---|
| **True named graphs** | `graph.named_graph` gives each context a real RDF 1.1 named-graph IRI rather than borrowing the ontology IRI for double duty. |
| **No `owl:Ontology` boilerplate** | The structural workaround disappears; a DataBook is a data container by design. |
| **Human-readable** | Markdown prose sections make each context file self-documenting without code comments. |
| **Standard metadata** | `id`, `title`, `version`, `description`, `created` are readable by any developer without knowledge of OWL. |
| **Structured provenance** | PROV-O `process:` stamps replace ad-hoc `owl:versionInfo` strings. |
| **Formal SHACL pointer** | `shapes:` links data to its validation constraints explicitly, not by convention. |
| **Fragment addressing** | Individual blocks are independently retrievable by IRI (`{doc-id}#{block-id}`). |
| **Native validation** | `databook validate` uses Jena under the hood — same engine, simpler commands. |
| **SPARQL queries** | Per-context queries can live alongside the data; `shacl2sparql` generates identity views. |
| **LLM integration** | `databook prompt` enables AI-assisted identity management with provenance tracking. |
| **Encryption** | Sensitive blocks (SSN, card numbers) can be encrypted at rest while structural metadata stays readable. |
| **Authoring** | Claude authors `.databook.md` as naturally as `.ttl` — markdown with YAML frontmatter and fenced code blocks is a comfortable format. |

### Cons

| | |
|---|---|
| **Fuseki required** | The triplestore-centric composition model requires Apache Jena Fuseki to be running for full union queries. The current workflow is filesystem-only. |
| **`context:` properties lose RDF semantics in YAML** | `contextCategory`, `assertedBy`, `subject`, `template`, `dyad` stored as YAML strings are not directly SPARQL-queryable from the file. Mitigated by the triplestore model. |
| **Protégé pre-processing** | Protégé sessions require a `databook extract` script to produce temp `.ttl` files. Minor friction since Protégé is used for inspection, not authoring. |
| **Ecosystem immaturity** | DataBook is a W3C Community Group draft (spec v1.2, CLI v1.4.4). Smaller ecosystem than the Jena/Protégé/SHACL stack. |
| **File-reference churn** | 22 context files plus all references in `README.md`, `CLAUDE.md`, `alice(self)alice.ttl` imports, and both catalog files would need updating. |

---

## 7. Recommendation

**Migrate.** DataBook solves the structural problem we work around today — using `owl:Ontology` as a metadata vehicle for what is really just a named-graph data container — and does so in a format that is more readable, more self-documenting, and better supported by purpose-built tooling.

The practical concerns are manageable:

- **Fuseki** is a well-established, free Apache project; running it locally is straightforward and unlocks SPARQL queries over the full dataset as a bonus.
- **Protégé pre-processing** is a small script, not a workflow change.
- **File-reference churn** is mechanical work well-suited to a single migration session.
- **Ecosystem immaturity** is real but the CLI already uses Jena under the hood, so the validation results are identical to our current stack.

A full migration is a well-scoped project: convert 22 context files to `.databook.md`, update catalog and import references, write the Protégé extraction script, and replace the README validation commands with `databook validate` equivalents.
