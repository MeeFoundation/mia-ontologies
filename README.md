# Persona Ontology

`persona.ttl` is an **application ontology** for the Mee Identity Agent (MIA). It imports and profiles existing domain ontologies — documenting which of their classes and properties Mee requires or uses — and extends them with Mee-specific classes and properties.

## Purpose

It defines a formal, machine-readable model of a real-world person's identity data — names, addresses, phone numbers, SSNs, physical characteristics, parent-child relationships, social connections, payment cards, and more — by reusing existing well-known ontologies wherever possible and defining new terms only where no suitable existing term exists.

## Ontological Foundation

Built on **BFO** (Basic Formal Ontology) and **CCO** (Common Core Ontologies) as the upper ontological foundation, and on domain ontologies that extend CCO:
- **PersonOntology** — person, name types, parent-child relationships
- **AddressOntology** — postal address structure
- **StagingOntology** — staging area for terms pending promotion (phone numbers, email addresses, user accounts, etc.)
- **AgentOntology** — agents and their properties (imported transitively via PersonOntology)

## One Person, multiple Personas

We represent a person as a combination of a single Person entity representing their **selfness** and multiple **context files**, one per relationship or institutional context.

A person's selfness is their essential individuality or unique selfhood represented by the Person entity in `self.ttl`. The selfness carries very few properties: only physical attributes and parent-child relationships. Most importantly, it carries `persona:hasPersona` links to context-specific Personas. Most names and all identifiers belong to those context-specific Personas; the one exception is a preferred/goes-by name, which lives in `self.ttl` as it applies across all contexts.

Rather than being a kind of Person, a `persona:Persona` is an **Information Content Entity** (CCO `ont00000958`) — a context-specific facet *of* a Person. Personas are linked to the Person entity in `self.ttl` via `persona:hasPersona`, a subproperty of CCO `is subject of` (`ont00001801`). Each Persona carries only the data relevant to its specific context.

## Contexts

Each context file carries a single Persona and is tagged with three orthogonal annotation properties that together classify its nature. All three are applied to the ontology IRI, not to the Persona individual.

**`persona:contextType`** — The kind of relationship the context represents. Values form a subclass hierarchy under `persona:Context`:
- `persona:Company` — a relationship with a company or institution (e.g. a bank, a phone carrier)
- `persona:Government` and subtypes `Federal`, `State`, `Municipality` — a government relationship
- `persona:People` and subtypes `Family`, `Colleagues`, etc. — a relationship with other people
- `persona:Possession` — personal belongings

**`persona:assertionType`** — Who is making the assertion:
- `persona:SelfAsserted` — the person themselves is recording the data, even if the underlying information originates from a third party such as a bank or government agency
- `persona:OtherAsserted` — a third party is asserting the data directly

**`persona:subject`** — Whose identity the context file describes:
- `persona:Self` — the file is about the identity owner
- `persona:Other` — the file is about another person or entity

For example, Alice's `texas-birth-certificate.ttl` is `contextType: State`, `assertionType: SelfAsserted`, `subject: Self` — a state government context recorded by Alice, about Alice. Her `florida-birth-certificate.ttl` is `contextType: State`, `assertionType: SelfAsserted`, `subject: Other` — also recorded by Alice, but describing her mother Paula.

## Ontology Files

- **`persona.ttl`** — The application ontology. Imports the domain ontologies above and documents which classes and properties Mee uses (required vs. optional). Also defines Mee-specific extension properties (`persona:hasSocialNetwork`, `persona:hasPaymentCard`, `persona:hasPersona`), the Persona context hierarchy, and three annotation properties for tagging context files: `persona:contextType`, `persona:assertionType`, and `persona:subject` (see **Contexts** above).

- **`persona-shacl.ttl`** — SHACL constraint rules defining how instance data must be structured. Validates:
  - *BirthCertificate Personas*: FullName OR (GivenName + FamilyName) required; optional AdditionalName, AlternateName, Nickname, Legal Name
  - *All Personas*: SSN format (`NNN-NN-NNNN`), email format, phone (E.164), address cardinality, payment cards, wallet
  - *US Postal Address*: required street, city, state (USPS 2-letter), ZIP; optional country
  - *Person (selfness)*: scalp hair (0..1); `has mother` / `is mother of` range must be a Person
  - *Social Network*: sub-groups (via `has part`) must be Social Networks; members (via `has member part`) must be Personas
  - *Debit Card*: card number and expiration date required; CVV optional
  - *Wallet*: items declaring themselves `continuant part of` this wallet must be PhysicalCards
  - *PhysicalCard*: image scan, if present, must be `xsd:anyURI` (max 1); `continuant part of` target, if present, must be a Wallet (max 1)

## Illustrative Example: Alice Walker

The repository includes a worked example for a hypothetical person, Alice Walker, to demonstrate the ontology in use. Each context file is an independent `owl:Ontology` linked to a Person entity in `example/alice/self.ttl` via `persona:hasPersona`. All context files are `persona:assertionType persona:SelfAsserted` — Alice is the one recording all of this data, even when the underlying information originates from a third party.

### Alice Walker (`persona:subject` = `Self`)

| Context file | Context type | Key data |
|:-------------|:-------------|:---------|
| `att.ttl` | Company (ATT) | Phone number |
| `belongings.ttl` | Possession | Wallet (driver's license + payment card); health insurance card and SSN card held directly (with image scans) |
| `boston.ttl` | Municipality (Boston) | Previous address — Boston, MA (2020–2025) with temporal interval |
| `citibank.ttl` | Company (Citibank) | Debit card |
| `colleagues.ttl` | People/Professionals | Colleagues social network with Bob Johnston |
| `family.ttl` | People/Family | Family social network with Paula Walker |
| `google.ttl` | Company (Google) | Email address |
| `paradise.ttl` | Municipality (Paradise) | Current address — Paradise, CA (2025–present) |
| `ssa.ttl` | Federal (SSA.gov) | SSN |
| `texas-birth-certificate.ttl` | State (texas.gov) | Legal names: Margery Alice Walker; maiden name Margery Alice Arnold |

### Paula Walker (`persona:subject` = `Other`)

| Context file | Context type | Key data |
|:-------------|:-------------|:---------|
| `florida-birth-certificate.ttl` | State (FL) | Legal names |

## Design Patterns

**Physical cards**: When a future context file creates a Persona for a credential issuer (e.g. DMV), the corresponding physical card in `belongings.ttl` links back using BFO `is carrier of` (`BFO_0000101`): the PhysicalCard individual is the carrier of the Persona (ICE).

**Peer name pattern**: All name types (FullName, GivenName, FamilyName, AlternateName) connect directly to a Person or Persona via `designated by` (`ont00001879`). They are siblings, not nested under a PersonName parent. Legal names belong to BirthCertificate Personas; a preferred/goes-by name lives in `self.ttl` since it applies across all contexts.

**Address history**: Each address Persona carries a USPostalAddress and an `AddressDesignation` with a `TemporalInterval` (start date required; no end date = current address).

## Diagrams

`draw.py` generates a Graphviz diagram from any context `.ttl` file:

```bash
python3 draw.py example/alice-contexts/citibank.ttl      # → example/alice-contexts/citibank.png
python3 draw.py example/alice-contexts/paradise.ttl      # → example/alice-contexts/paradise.png
```

**Dependencies** (one-time setup):
```bash
pip install rdflib graphviz
brew install graphviz
```

Each diagram shows the Persona individual (yellow), supporting named individuals (white boxes), class labels (plain text), blank-node designator chains, and literal values (green).

## Validation

Validation requires Apache Jena. The following validates Alice Walker's example instance data against the SHACL shapes. Merge all data files first, then validate:

```bash
riot --output=turtle \
  project_files/bfo-core.ttl project_files/PersonOntology.ttl \
  project_files/AddressOntology.ttl project_files/StagingOntology.ttl \
  persona.ttl example/alice/self.ttl \
  example/alice-contexts/citibank.ttl example/alice-contexts/boston.ttl \
  example/alice-contexts/paradise.ttl example/alice-contexts/family.ttl \
  example/alice-contexts/colleagues.ttl example/alice-contexts/att.ttl \
  example/alice-contexts/ssa.ttl example/alice-contexts/google.ttl \
  example/alice-contexts/texas-birth-certificate.ttl \
  example/paula-contexts/florida-birth-certificate.ttl \
  example/alice-contexts/belongings.ttl \
  2>/dev/null > /tmp/mia-merged.ttl

grep -v 'owl:imports' persona-shacl.ttl > /tmp/mia-shapes.ttl

shacl validate --shapes /tmp/mia-shapes.ttl --data /tmp/mia-merged.ttl --text
```

Expected output: `Conforms`
