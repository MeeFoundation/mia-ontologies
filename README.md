# Persona Ontology

The persona ontology is an application profile over existing ontologies. It models the domain of natural people in the Mee Identity Agent (MIA). It documents in SHACL which classes and properties from other ontologies are used to describe a person.

## Purpose

It defines a formal, machine-readable model of a real-world person's identity data — names, addresses, phone numbers, SSNs, physical characteristics, parent-child relationships, social connections, payment cards, and more — by reusing and constraining existing well-known ontologies rather than inventing new ones.

## Ontological Foundation

Built on **BFO** (Basic Formal Ontology) and **CCO** (Common Core Ontologies), specifically:
- **PersonOntology** — person, name types, parent-child relationships
- **AddressOntology** — postal address structure
- **StagingOntology** — staging area for terms pending promotion (phone numbers, email addresses, user accounts, etc.)
- **AgentOntology** — agents and their properties (imported transitively via PersonOntology)

## Key Components

- **`persona.ttl`** — The application ontology. Imports the domain ontologies above and documents which classes and properties Mee uses (required vs. optional). Also defines Mee-specific extension properties (`persona:hasSocialNetwork`, `persona:holdsPaymentCard`, `persona:hasPersona`) and the Persona context hierarchy.

- **`persona-shacl.ttl`** — SHACL constraint rules defining how instance data must be structured. Validates:
  - *BirthCertificate Personas*: FullName OR (GivenName + FamilyName) required; optional AdditionalName, AlternateName, Nickname, Legal Name
  - *All Personas*: SSN format (`NNN-NN-NNNN`), email format, phone (E.164), address cardinality, payment cards, wallet
  - *US Postal Address*: required street, city, state (USPS 2-letter), ZIP; optional country
  - *Person (selfness)*: scalp hair (0..1); `has mother` / `is mother of` range must be a Person
  - *Social Network*: sub-groups (via `has part`) must be Social Networks; members (via `has member part`) must be Persons
  - *Debit Card*: card number and expiration date required; CVV optional
  - *Wallet*: `has continuant part` items must be PhysicalCards
  - *PhysicalCard*: image scan, if present, must be `xsd:anyURI` (max 1)

- **`self.ttl`** — Alice Walker's *selfness* — her essential individuality or unique selfhood. Carries only properties intrinsic to the person (physical characteristics, parent-child relationships) and `persona:hasPersona` links to all context-specific Personas. Imports all context files below.

## Instance Data Architecture

A person's data is split across a **selfness** file (`self.ttl`) and multiple **context files**, one per relationship or institutional context. Most names and all identifiers belong to context-specific Personas; the one exception is a preferred/goes-by name, which lives on the selfness as it applies across all contexts.

| File | Context type | Key data |
|------|-------------|----------|
| `att.ttl` | Company | Phone number |
| `belongings.ttl` | Possession | Wallet containing driver's license and health insurance card (with image scans) |
| `boston.ttl` | Municipality | Previous address — Boston, MA (2020–2025) with temporal interval |
| `citibank.ttl` | Company | Debit card |
| `colleagues.ttl` | People/Professionals | Colleagues social network with Bob Johnston |
| `family.ttl` | People/Family | Family social network with Paula Walker |
| `florida-birth-certificate.ttl` | State (FL) | Paula Walker's legal names |
| `google.ttl` | Company | Email address |
| `paradise.ttl` | Municipality | Current address — Paradise, CA (2025–present) |
| `ssa.ttl` | Federal | SSN |
| `texas-birth-certificate.ttl` | State (TX) | Legal names: Margery Alice Walker; maiden name Margery Alice Arnold |

## Architecture

**Selfness and Personas**: A person's selfness is their essential individuality or unique selfhood represented by the Person entity in self.ttl. A `persona:Persona` is an **Information Content Entity** (CCO `ont00000958`) — a context-specific profile *about* a Person, not itself a Person. Multiple Personas are linked to the selfness via `persona:hasPersona` (a subproperty of CCO `is subject of`). Each Persona carries only the data relevant to its interaction context.

**Physical cards**: When a future context file creates a Persona for a credential issuer (e.g. DMV), the corresponding physical card in `belongings.ttl` links back using BFO `is carrier of` (`BFO_0000101`): the PhysicalCard individual is the carrier of the Persona (ICE).

**Peer name pattern**: All name types (FullName, GivenName, FamilyName, AlternateName) connect directly to a Person or Persona via `designated by` (`ont00001879`). They are siblings, not nested under a PersonName parent. Legal names belong to BirthCertificate Personas; a preferred/goes-by name lives on the selfness since it applies across all contexts.

**Address history**: Each address Persona carries a USPostalAddress and an `AddressDesignation` with a `TemporalInterval` (start date required; no end date = current address).

## Diagrams

`draw.py` generates a Graphviz diagram from any context `.ttl` file:

```bash
python3 draw.py citibank.ttl      # → citibank.png
python3 draw.py paradise.ttl     # → paradise.png
```

**Dependencies** (one-time setup):
```bash
pip install rdflib graphviz
brew install graphviz
```

Each diagram shows the Persona individual (yellow), supporting named individuals (white boxes), class labels (plain text), blank-node designator chains, and literal values (green).

## Validation

Validation requires Apache Jena. Merge all data files first, then validate:

```bash
riot --output=turtle \
  project_files/bfo-core.ttl project_files/PersonOntology.ttl \
  project_files/AddressOntology.ttl project_files/StagingOntology.ttl \
  persona.ttl self.ttl citibank.ttl boston.ttl paradise.ttl family.ttl \
  colleagues.ttl att.ttl ssa.ttl google.ttl \
  texas-birth-certificate.ttl florida-birth-certificate.ttl belongings.ttl \
  2>/dev/null > /tmp/mia-merged.ttl

grep -v 'owl:imports' persona-shacl.ttl > /tmp/mia-shapes.ttl

shacl validate --shapes /tmp/mia-shapes.ttl --data /tmp/mia-merged.ttl --text
```

Expected output: `Conforms`
