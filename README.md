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

## Ontology Files

- **`persona.ttl`** — The application ontology. Imports the domain ontologies above and documents which classes and properties Mee uses (required vs. optional). Also defines Mee-specific extension properties (`persona:hasSocialNetwork`, `persona:holdsPaymentCard`, `persona:hasPersona`) and the Persona context hierarchy.

- **`persona-shacl.ttl`** — SHACL constraint rules defining how instance data must be structured. Validates:
  - *BirthCertificate Personas*: FullName OR (GivenName + FamilyName) required; optional AdditionalName, AlternateName, Nickname, Legal Name
  - *All Personas*: SSN format (`NNN-NN-NNNN`), email format, phone (E.164), address cardinality, payment cards, wallet
  - *US Postal Address*: required street, city, state (USPS 2-letter), ZIP; optional country
  - *Person (selfness)*: scalp hair (0..1); `has mother` / `is mother of` range must be a Person
  - *Social Network*: sub-groups (via `has part`) must be Social Networks; members (via `has member part`) must be Personas
  - *Debit Card*: card number and expiration date required; CVV optional
  - *Wallet*: `has continuant part` items must be PhysicalCards
  - *PhysicalCard*: image scan, if present, must be `xsd:anyURI` (max 1)

## Illustrative Example: Alice Walker

The repository includes a worked example for a hypothetical person, Alice Walker, to demonstrate the ontology in use. Each context file is an independent `owl:Ontology` linked to her Person entity in `self.ttl` via `persona:hasPersona`.

| Context file | Context type | Key data |
|:-------------|:-------------|:---------|
| `att.ttl` | Company (ATT) | Phone number |
| `belongings.ttl` | Possession | Wallet containing driver's license and health insurance card (with image scans) |
| `boston.ttl` | Municipality (Boston) | Previous address — Boston, MA (2020–2025) with temporal interval |
| `citibank.ttl` | Company (Citibank) | Debit card |
| `colleagues.ttl` | People/Professionals | Colleagues social network with Bob Johnston |
| `family.ttl` | People/Family | Family social network with Paula Walker |
| `florida-birth-certificate.ttl` | State (FL) | Paula Walker's legal names |
| `google.ttl` | Company (Google) | Email address |
| `paradise.ttl` | Municipality (Paradise)| Current address — Paradise, CA (2025–present) |
| `ssa.ttl` | Federal (SSA.gov) | SSN |
| `texas-birth-certificate.ttl` | State (texas.gov) | Legal names: Margery Alice Walker; maiden name Margery Alice Arnold |

## Design Patterns

**Physical cards**: When a future context file creates a Persona for a credential issuer (e.g. DMV), the corresponding physical card in `belongings.ttl` links back using BFO `is carrier of` (`BFO_0000101`): the PhysicalCard individual is the carrier of the Persona (ICE).

**Peer name pattern**: All name types (FullName, GivenName, FamilyName, AlternateName) connect directly to a Person or Persona via `designated by` (`ont00001879`). They are siblings, not nested under a PersonName parent. Legal names belong to BirthCertificate Personas; a preferred/goes-by name lives in `self.ttl` since it applies across all contexts.

**Address history**: Each address Persona carries a USPostalAddress and an `AddressDesignation` with a `TemporalInterval` (start date required; no end date = current address).

## Diagrams

`draw.py` generates a Graphviz diagram from any context `.ttl` file:

```bash
python3 draw.py example/contexts/citibank.ttl      # → example/contexts/citibank.png
python3 draw.py example/contexts/paradise.ttl      # → example/contexts/paradise.png
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
  persona.ttl example/self/self.ttl \
  example/contexts/citibank.ttl example/contexts/boston.ttl \
  example/contexts/paradise.ttl example/contexts/family.ttl \
  example/contexts/colleagues.ttl example/contexts/att.ttl \
  example/contexts/ssa.ttl example/contexts/google.ttl \
  example/contexts/texas-birth-certificate.ttl \
  example/contexts/florida-birth-certificate.ttl \
  example/contexts/belongings.ttl \
  2>/dev/null > /tmp/mia-merged.ttl

grep -v 'owl:imports' persona-shacl.ttl > /tmp/mia-shapes.ttl

shacl validate --shapes /tmp/mia-shapes.ttl --data /tmp/mia-merged.ttl --text
```

Expected output: `Conforms`
