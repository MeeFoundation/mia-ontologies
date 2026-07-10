# Mia Ontologies

This document describes the ontologies used by the Mee Identity Agent (Mia) software application. Each Mia interoperates with the Personal Data Network (PDN). The PDN is a data-sharing network with three kinds of participants: individual Mia users, groups of Mia users and/or organizations, and organizations (government agencies, companies, and nonprofits).

Mia's ontologies import and profile existing ontologies — documenting which of their classes and properties Mia requires or uses — and extending them with Mia-specific classes and properties. 

The **Context** and **Cell** ontologies are the organizing framework. The context ontology defines *contexts* - containers of claims (attributes) about a given subject and claimed by some entity. The cell ontology defines *cells* that may reference one or more contexts. 

The three **domain ontologies** model claims about people, organizations and groups contained in contexts:
- **Persona ontology** — models a person: names, addresses, phone numbers, relationships, payment cards, and more. It is built on BFO (Basic Formal Ontology) and CCO (Common Core Ontologies) as the upper ontological foundation, and on domain ontologies that extend CCO:
  - **PersonOntology** — person, name types, parent-child relationships
  - **AddressOntology** — postal address structure
  - **StagingOntology** — staging area for terms pending promotion (phone numbers, email addresses, user accounts, etc.)
  - **AgentOntology** — agents and their properties (imported transitively via PersonOntology)
- **Organization ontology** — models organizations (companies, government agencies, non-profits, etc.) 
- **Group ontology** — a group made up of individuals and/or organizations.

An additional ontology provides PDN ids for persons, organizations and groups:
- **Identity ontology** — types of PDN network identifiers used by people, organizations or groups. 

Throughout, we use these shorthands:

- `c:` for the `context:` namespace (`http://mee.foundation/ontologies/context#`)
- `cell:` for the `cell:` namespace (`http://mee.foundation/ontologies/cell#`)
- `p:` for the `persona:` namespace (`http://mee.foundation/ontologies/persona#`)
- `o:` for the `organization:` namespace (`http://mee.foundation/ontologies/organization#`).
- `g:` for the `group:` namespace (`http://mee.foundation/ontologies/group#`)
- `i:` for the `identity:` namespace (`http://mee.foundation/ontologies/pdn-identity#`)
- `ako` for `rdfs:subClassOf` ("a kind of")
- `isa` for 'rdf:type` ("is a")

We first present an overview of the ontologies and then illustrate their use through a sample dataset for a hypothetical user, Alice Walker.

## Context Ontology

The context ontology defines *contexts* which are named graphs containing sets of claims (attributes) about a person. 

### Contexts

A *context* is a container of information about a person related to their interactions with, or relationship to, another person, group or organization. This information is expressed as triples using the Persona, Organization, Group and Identity ontologies and stored in a **[DataBook](https://github.com/w3c-cg/holon/tree/main/architectures/databook)** (`.databook.md`) file. 

Each context is a named graph of claims describing one facet of a person or organization (called the `subject` of the context). It is a self-contained set of claim data about that subject, although these claims may have originated from other contexts about the same subject. 

<p align="center"><img src="images/context-ontology/context.png" alt="context ontology"></p>

Two properties apply to every `c:Context`:

**`c:cell`** — containing cell. Its value is the IRI of the cell DataBook (e.g. `"http://www.example.org/mia/cells/bob-johnson(others)"`) that references it via `cell:sbs`, `cell:obs`, `cell:sbo`, or `cell:obo` links of the cell.

**`c:template`** — present only on context files that contain instances of a template; its value is the name of a `p:PersonaTemplate` subclass (e.g. `"persona:BirthCertificate"`, `"persona:JSContactCard"`, `"persona:DriversLicense"`, `"persona:Passport"`, `"persona:MedicalAppointment"`).

Three more properties apply only to contexts classified into one of the four self-vs-other subtypes (`c:XBXcontext` and below) — a context linked via `cell:graph` rather than `sbs`/`obs`/`sbo`/`obo` is a plain `c:Context` and does not carry these:

**`c:about-by`** — classifies a context DataBook by the combination of `subject` and `claimant`. One of `context:SBScontext` (subject=Self, claimant=Self), `context:OBScontext` (subject=Other, claimant=Self), `context:OBOcontext` (subject=Other, claimant=Other), or `context:SBOcontext` (subject=Self, claimant=Other).

**`c:subject`** — The identity the context file is about. Values are IRIs of `p:Person`, `g:Group`, or `o:Organization` individuals:
- `:Self` — the context is about the Mia user.
- a named individual of `p:Person` — the context is about another human Mia user.
- a named individual of `g:Group` — the context is about a group of Mia users.
- a named individual of `o:Organization` — the context is about an organization (legal corporation or government agency).

**`c:claimant`** — Who is making the claim. Values are local IRIs of `p:Person`, `g:Group`, or `o:Organization` individuals:
- `:Self` — the Mia user that is entering the data, even if the underlying information originates from some other party such as a company, government agency, or another person.
- a named individual of class `p:Person` — another Mia user is claiming the data directly.
- a named individual of class `g:Group` — a group of Mia users is claiming the data.
- a named individual of class `o:Organization` — an organization is claiming the data.

The diagram below shows four kinds of contexts related to a hypothetical Mia user, Alice, and her interactions with a Department of Motor Vehicles (DMV) agency. Across the top are two contexts where the DMV itself is the subject, and at the bottom where Alice is the subject. At the left are contexts where Alice has made the claims (e.g. Alice's Mia has written the claims into the context) and at the right are contexts where the DMV as the "other" has written the claims. 

<p align="center"><img src="images/context-ontology/quadrants.png" alt="a quadrant of context types"></p>

The lower left shows a context that Alice might share with other people or companies. In it, she claims that her driver's license number is S43228943, having copied that number from her physical driver's license. The context in the lower right carries the same information as the lower left, but because it is being claimed by the DMV it is more likely to be trusted by a recipient (especially if this information is conveyed via secure channel and the claims are cryptographically bound to the identity of the DMV).

### Context DataBooks

The description of the context container itself is carried in the DataBook's YAML front matter under the `mia:` key. The context ontology (`context.ttl`) defines the controlled vocabularies that those YAML fields reference:

- `mia.cell` = `c:cell`
- `mia:template` = `c:template`
- `mia.about-by` = `c:about-by`
- `mia.subject` = `c:subject`
- `mia.claimant` = `c:claimant`


### Context Ontology File

**`context.ttl`** — the Context ontology, defines:
  - *Classes*: `c:Context`, `c:XBXcontext` (abstract intermediate superclass of the four classified subtypes below — carries the `c:about-by`/`c:subject`/`c:claimant` annotations, since a `cell:graph`-linked plain `c:Context` doesn't carry them), `c:SBScontext`, `c:OBScontext`, `c:OBOcontext`, `c:SBOcontext` (each a subclass of `c:XBXcontext`).
  - *Annotation properties*: `c:cell` (containing cell — range `cell:Cell`; domain `c:Context`), `c:template` (domain `c:Context`), `c:claimant`, `c:subject`, `c:about-by` (domain `c:XBXcontext`).
  These terms are referenced by name in the YAML frontmatter of each DataBook file. `context.ttl` imports `cell.ttl` (for `c:cell`'s range, `cell:Cell`, and to reuse `cell:abstract` on `c:Context`/`c:XBXcontext`).

### Context Ontology Validation

Context file metadata (cell, claimant, subject, about-by) is declared in YAML frontmatter and validated at authoring time by convention. `context.ttl` has no SHACL shapes of its own — the classification fields that carry validation constraints (`cellType`, `num-parties`, `sbs`/`obs`/`sbo`/`obo`) live on cell DataBooks and are validated by `cell-shacl.ttl` (see [Cell Ontology Validation](#cell-ontology-validation)).

## Cell Ontology

The cell ontology defines *cells* — containers of information about some aspect of a person's personal or work life. 

### Cells 

The cell may contain a reference to folder on in the local file system. It may contain reference to a markdown note in the local file system. And it and may contain within itself a graph structure. It may also contain a set of references *contexts* (also graphs) as described in the previous section; the number and kinds varies by the type of cell. The number and type of contexts varies depending on if this cell is shared or not and with how many parties it is shared. 

Cells vary in scope from a few broad categories of information to narrower ones. In the social domain, a cell might be about "People", or more narrowly about "Immediate Family", or to information about just a single family member. The user can choose at what level in this broader to narrower structure to put what kind of information. For example if the user has a nickname used only by this one family member, they can add that "claim" (attribute) at the individual relationship level. 

### CellType and parties

Every cell is a `cell:Cell` (or a subtype of `cell:Personal`, `cell:Organizational` or `cell:UserDefined`), as well as being a subtype of `cell:Parties` shown in the diagram below. 

<p align="center"><img src="images/cell-ontology/cell.png" alt="Cell hierarchy"></p>

**CellType — `mia.cellType`.** Its value is the local name of the `cell:Cell` subclass this cell canonically is — for a canonical cell, e.g. `ImmediateFamily` or `Employees(org)` — or, for a user's instance copy of a canonical cell, the name of the class it was copied from (the same value as its canonical source). A cell with no canonical counterpart at all (e.g. a specific person, company, or group Alice created herself) uses `Cell` itself, the root class. Canonical cells are direct subclasses of `cell:Cell`: either `cell:Personal` (generally useful cells for organizing a person's personal, non-work, life) or `cell:Organizational` (cells tuned to a person's working life) — `mia.cellType` names the specific leaf subclass rather than this broader family, so new canonical subclasses can be added without changing the property itself.

**Parties — `mia.num-parties`.** `cell:Parties` is an abstract class classifying every cell by how many total parties (the user plus zero or more others) are involved in the relationship it represents. Unlike `cellType`, this isn't just a descriptive string: `cell:Parties` and `cell:Cell` are orthogonal facets of the same instance (`cell:Parties` is not `rdfs:subClassOf cell:Cell`, and vice versa), so every cell is formally typed as *both* a `cell:Cell` subclass and a concrete `cell:Parties` subclass. There are three concrete types: `cell:OneParty` (the user alone — display label "Cell"), `cell:TwoParty` (the user plus exactly one other party — display label "Two-Party Cell"), and `cell:ThreePlusParty` (the user plus two or more other parties, e.g. a group — display label "Multi-Party Cell"). `cell:TwoParty` and `cell:ThreePlusParty` are both subclasses of the abstract `cell:MultiParty`, which exists only to group "more than one total party" cells for the purpose of properties that need another party to make sense (see `obs`/`sbo`/`obo` below).



Cardinality of each property by concrete `cell:Parties` subtype:

| Property | OneParty | TwoParty | ThreePlusParty |
|----------|----------|----------|-----------------|
| `cell:graph` | 0..1 | 0..1 | 0..1 |
| `cell:folder` | 0..1 | 0..1 | 0..1 |
| `cell:note` | 0..1 | 0..1 | 0..1 |
| `cell:sbs` | 0..1 | 0..1 | 0..1 |
| `cell:sbo` | 0 | 0..1 | 0..N |
| `cell:obs` | 0 | 0..1 | 0..N |
| `cell:obo` | 0 | 0..1 | 0..N |

### Properties

- **`cell:label`** — user-editable display name of the cell. Defaults to cell's class name.
- **`cell:note`** — path to a markdown note in the *notes* folder/file hierarchy for this cell.
- **`cell:folder`** — path to a folder in the *files* folder/file hierarchy for this cell.
- **`cell:child`** — organizes cells into a tree structure.
- **`cell:sbs`** - link to a context that is about the self as claimed by the self (user).
- **`cell:obs`** - a context about the other party as claimed by the self.
- **`cell:sbo`** - a context about the self as claimed by the other party.
- **`cell:obo`** - a context about the other party as claimed by the other party.
- **`cell:graph`** - link to a plain `c:Context` that doesn't fit the self-vs-other classification `cell:sbs`/`cell:obs`/`cell:sbo`/`cell:obo` assume — e.g. claims jointly maintained by multiple parties about a third party, or, on a `OneParty` cell, simply a context that doesn't need self-vs-other framing at all.

### Representative cell types

The diagram below shows five kinds of cells along with referenced contexts (the white and green circles). The first is a `cell:Personal` canonical cell. Next is an`cell:Organizational` cell. The third is a `cell:UserDefined` cell. The fourth is a `cell:TwoParty` cell between the user and another Mia user, Bob. The last is a `cell:ThreePlusParty`--the Boston Hub Society (BHS) professional social network.

<p align="center"><img src="images/cell-ontology/cells+contexts.png" alt="Cells and contexts"></p>

Each of these five example cells contains contexts shown as circles. White circles are contexts whose triples are claimed by the self (the user). Green circles are contexts whose triples are claimed by a person other than the self (i:Individual), by an organization (i:Organization) or by a group (i:Group), and synchronized with the user's Mia instance over the PDN. For example the BHS cell at the bottom has three contexts: Self (the user)'s BHS profile, Carol's BHS profile (claimed by Carol) and information about the BHS itself (as claimed by the BHS) in the last green circle.

### Cells are organized into trees

To organize the user's information, canonical cells are copied into the user's cell tree. 

Both personal life (family, health, finances cells) and work life (employment, colleagues cells) are organized within this same tree, since `Work` is itself a `cell:Personal` subclass alongside `People` and `Health & Wellness`, not a separate branch. The `cells-org/` tree, rooted in `cell:Organizational`, exists so a person can copy pieces of it into their own `Work` branch to model the organizations they work for or with — e.g. Alice's `Work > Organization-Acme > Employees` cell is a copy of `cell:Organizational`'s `Employees`, since Acme's own structure is what her employment relationship is actually about.

The top-to-bottom ordering of the two canonical cell trees is preserved when copied to the user's tree, although the user is always free to insert any number of user-defined cells at any level in the resulting tree. 

#### A few details about cell:note and cell:folder
`cell:note` and `cell:folder` point into two separate but parallel folder structures that mirror the structure of the cell tree. If the cell tree is `(People, (Immediate Family, Friends), Work)` then both hierarchies contain exactly the same folder names and nesting. Mia keeps both in sync with the cell tree — when a cell is created, renamed, or deleted, Mia updates both hierarchies automatically.

A canonical top-level or nested cell is not required to be copied into a user's tree just because it exists in the canonical template — Mia (or the user) copies a canonical cell into the tree, and creates its `cell:note`/`cell:folder` paths, only once the user actually has content for it. Empty cells are not pre-populated as placeholder folders.

- The **notes hierarchy** mirrors the cell tree as a folder structure, rooted at a top-level folder named **`Self`**. The invisible root cell's note is `Self.md`, stored directly inside `Self/`; every other cell's note is stored as `X.md` inside the X folder — for example, `Self/People/Immediate Family/Immediate Family.md`. Using the same name as the folder matches the convention used by PKM (Personal Knowledge Management) tools such as Obsidian (using the Folder Notes plugin), Logseq, Foam and others. Any file or folder in the notes root that is not `Self/` — app-managed folders (e.g. `Templates/`, `.obsidian/`), unrelated personal notes (e.g. a `Journal/`), or loose files — falls outside the cell tree entirely and is ignored by Mia.
- The **files hierarchy** mirrors the cell tree as a folder structure. It has no equivalent of a root note, so it has no `Self` wrapper folder — the files root itself plays that role, and each top-level cell (e.g. `People`, `Work`) is a folder directly inside it. Each folder may hold arbitrary files, and may also contain additional subfolders (to any depth) that are not part of the cell tree. Any file or folder directly inside the files root that is not a recognized top-level cell folder likewise falls outside the cell tree and is ignored by Mia.

The two roots are stored separately so the notes hierarchy can be opened as a standalone PKM vault without exposing the files hierarchy. Two user-configurable settings define where each root lives on disk:

- **Files root** — default on macOS: `~/Enclave`
- **Notes root** — default on macOS: `~/Enclave/ObsidianVault`

The files root defaults to a dedicated top-level folder (sibling of the Mac's built-in `Desktop`/`Downloads`/`Pictures`/`Movies`/`Music`/`Public`/`Documents` folders) so the cell tree doesn't mix with — or need to accommodate — those OS-managed conventions; native Mac folders are left alone entirely, outside the Enclave tree. The notes root's default location is nested inside the files root's default location on disk — that's a matter of default configuration convenience, not a statement that the notes hierarchy is part of the files hierarchy. When Mia walks the files hierarchy it excludes the notes-root subtree entirely, and vice versa. All `cell:note` values are relative paths from the notes root; all `cell:folder` values are relative paths from the files root.

In the normal case `cell:note` and `cell:folder` are technically redundant — both paths can be derived from the cell tree plus the two configured roots. They are retained for three reasons:

1. **Divergence detection** — if a stored path no longer matches the derived path, Mia knows the user has manually renamed or rearranged folders outside of Mia and can alert them or attempt reconciliation rather than failing silently.
2. **Graceful degradation** — Mia can continue to locate a cell's folder or note via the stored path even when the folder hierarchy has drifted out of sync with the cell tree.
3. **Intentional overrides** — a user may deliberately want a cell's folder to live somewhere other than the derived location (e.g. `~/Pictures/Immediate Family/` rather than the default `~/Enclave/People/Immediate Family/`). The explicit link records that intentional deviation without disrupting the cell tree.

### Personal Cells

`cell:Personal` cells (and sub-cells) organize a person's information:

1. **People** (`cell:People`) — people in your social or professional life. Use this cell for people not otherwise tied to a specific domain — a bookkeeper you know belongs under Finances (Advisory), and your primary care physician belongs under Health & Wellness (Medical > Providers > Primary Care Physician), rather than here.
    - **Immediate Family** (`cell:ImmediateFamily`) — your closest living relatives, which generally include parents, siblings, spouses/partners, and children.
    - **Extended Family** (`cell:ExtendedFamily`) — relatives outside the immediate nuclear group, such as grandparents, aunts, uncles, cousins, nieces and nephews.
    - **In-Laws / Step-Family** (`cell:InLawsStepFamily`) — relatives gained through marriage or legal guardianship, including a spouse's parents and siblings, or children from a previous relationship.
    - **Friends** (`cell:Friends`) — interactions with friends.
    - **Others** (`cell:Others`) — people you know socially or professionally who are not family or friends — acquaintances, neighbors, or other connections not yet more specifically categorized.
1. **Affiliations** (`cell:Affiliations`) — clubs, charities, faith groups, and other group affiliations not covered by a more specific cell — includes formal memberships and their social networks, some of which may be `cell:ThreePlusParty` ("Multi-Party Cell") cells that exist as a `g:Group` on the PDN. See also Sports & Entertainment for personal sports and entertainment interests, like following a favorite team, that aren't tied to a formal membership.
1. **Health & Wellness** (`cell:HealthWellness`) — personal health and wellness information. Medical history, allergies, medications, vaccinations, prescriptions, eyeglasses.
    - **Medical** (`cell:Medical`) — medical (as opposed to dental or vision) care — diagnoses, treatments, providers, and insurance.
        - **History** (`cell:MedicalHistory`) — past diagnoses, conditions, surgeries, and treatments.
        - **Insurance** (`cell:MedicalInsurance`) — medical health insurance policies, providers, and coverage.
        - **Providers** (`cell:MedicalProviders`) — medical providers and practices you see for care.
            - **Primary Care Physician** (`cell:PrimaryCarePhysician`) — your primary care doctor, the physician you generally see first for checkups, referrals, and everyday health concerns.
            - **Medical Appointment Info** (`cell:MedicalAppointmentInfo`) — a medical appointment you're helping arrange on behalf of someone else.
    - **Dental** (`cell:Dental`) — dental care — diagnoses, treatments, providers, and insurance.
        - **History** (`cell:DentalHistory`) — past dental treatments, procedures, and conditions.
        - **Insurance** (`cell:DentalInsurance`) — dental insurance policies, providers, and coverage.
        - **Providers** (`cell:DentalProviders`) — dental providers and practices you see for care.
    - **Vision** (`cell:Vision`) — vision and eye care — diagnoses, treatments, providers, and insurance.
        - **History** (`cell:VisionHistory`) — past eye-care prescriptions, treatments, and conditions.
        - **Insurance** (`cell:VisionInsurance`) — vision insurance policies, providers, and coverage.
        - **Providers** (`cell:VisionProviders`) — vision care providers and practices you see for care.
    - **Fitness** (`cell:Fitness`) — general fitness and preventive physical health — exercise, gyms, trainers, and other non-clinical wellbeing information.
        - **Providers** (`cell:FitnessProviders`) — fitness providers and practices you see for care, e.g. gyms, trainers, and coaches.
    - **Nutrition** (`cell:Nutrition`) — nutritionists and dietitians.
        - **History** (`cell:NutritionHistory`) — past nutritional consultations, diet plans, and dietary conditions.
        - **Providers** (`cell:NutritionProviders`) — nutritionists and dietitians you see for care.
    - **Mental Health** (`cell:MentalHealth`) — mental and behavioral health care.
        - **History** (`cell:MentalHealthHistory`) — past diagnoses, treatments, and mental health conditions.
        - **Insurance** (`cell:MentalHealthInsurance`) — mental health insurance policies, providers, and coverage.
        - **Providers** (`cell:MentalHealthProviders`) — mental health providers and practices you see for care, e.g. therapists, counselors, and psychiatrists.
    - **Physical Therapy** (`cell:PhysicalTherapy`) — physical therapy and rehabilitative care.
        - **History** (`cell:PhysicalTherapyHistory`) — past physical therapy treatments, injuries, and rehabilitation plans.
        - **Providers** (`cell:PhysicalTherapyProviders`) — physical therapy providers and practices you see for care.
1. **Finances** (`cell:Finances`) — information about personal finances, bookkeeping, budgets, payment cards, bank accounts, brokerage accounts, insurance policies, financial advisors, etc.
    - **Banking & Payments** (`cell:BankingPayments`) — firms that help you store, access, and move your cash for daily living. These include Retail Banks & Credit Unions, which provide checking accounts, savings accounts, and debit cards. These also include Payment Processors like Visa, Mastercard, or PayPal that let you buy things online and in stores, and Remittance Firms like Western Union or Wise used to send money to family or friends, especially overseas.
    - **Investing** (`cell:Investing`) — firms that help you buy assets, so your money can grow over time for goals like buying a house or retiring. These include Brokerage Firms like Charles Schwab or Robinhood where you buy and sell stocks, bonds, and ETFs; Robo-Advisors, computer-run investing platforms like Betterment or Wealthfront that manage your portfolio for a low fee; and Mutual Fund companies like Vanguard or Fidelity that pool your money with other investors to buy a large bundle of stocks.
    - **Lending & Credit** (`cell:LendingCredit`) — firms that lend you money when you need to buy something expensive that you cannot pay for all at once. These include Mortgage Lenders, banks or specialized companies that give you loans specifically to buy a home; Consumer Finance Companies, that give out personal loans, auto loans, or student loans; and Credit Card Issuers, banks that give you a plastic card to borrow money on the spot for daily purchases.
    - **Insurance** (`cell:Insurance`) — firms that protect you and your family from financial ruin if something bad happens. These include Life & Health Insurance firms that cover medical bills or provide money to your family if you pass away, and Property & Casualty Insurance firms that insure your car, home, or apartment against accidents and theft.
    - **Advisory** (`cell:Advisory`) — firms and individuals who do not just hold your money, but tell you the best ways to use it. These include Financial Planners (Wealth Advisors), human experts who help you build a custom roadmap for taxes, retirement, and budgeting, and Estate Planners, specialized professionals who help you write wills and plan how to pass your money to your children. Also includes Accountants and Bookkeepers, who track your income and expenses and prepare your taxes.
1. **Pets** (`cell:Pets`) — care instructions, veterinarians, medicines, food providers.
1. **Home** (`cell:Home`) — owning or renting a home, apartment, or other dwelling. Leases, deeds, utility accounts, real estate brokers.
1. **Work** (`cell:Work`) — professional roles. Employment history, resume/CV.
1. **Ownership** (`cell:Ownership`) — owned assets, property, vehicles, and other possessions.
    - **Vehicles** (`cell:Vehicles`) — related to owning and maintaining a vehicle. Vehicle insurance, repairs, mechanics, garages. 
1. **Travel** (`cell:Travel`) — travel plans, trips, and related information. Loyalty programs, airlines, bus lines, trains.
1. **Food** (`cell:Food`) — food preferences, dietary restrictions, favorite restaurants, recipes, shopping lists, and other food-related interests
1. **Sports & Entertainment** (`cell:SportsEntertainment`) — sports, hobbies, entertainment, and media interests. Favorite teams, venues, streaming services, ticketing. See also `cell:Affiliations` for club or team memberships.
1. **Legal** (`cell:Legal`) — legal matters, contracts, agreements, trusts, wills, and professional legal relationships.
1. **Projects** (`cell:Projects`) — involvement in a specific project or initiative.
1. **Events** (`cell:Events`) — participation in or relationship to a specific event or gathering.
1. **Information** (`cell:Information`) — general knowledge selected by you, web links, documents, images.
    - **Learnings** (`cell:Learnings`) — knowledge gained through personal experience.
1. **Government** (`cell:Government`) — government-issued credentials, tax records, and civic relationships.
    - **Federal** (`cell:Federal`) — federal government context (e.g. passport, federal tax records).
        - **SSA** (`cell:SSA`) — the Social Security Administration.
        - **Passport** (`cell:Passport`) — a federal agency that issues and holds passport records.
    - **State** (`cell:State`) — state government context (e.g. driver's license, state tax records).
        - **Birth Certificate** (`cell:BirthCertificate`) — a state agency that issues and holds birth certificate records.
        - **Drivers License** (`cell:DriversLicense`) — a state agency that issues and holds driver's license records.
    - **Municipality** (`cell:Municipality`) — municipal government context (e.g. local permits, library card).
        - **Residence** (`cell:Residence`) — a place a person has lived, current or past.
1. **Companies** (`cell:Companies`) — miscellaneous companies and organizations that provide services or products to you. See also Finances, Health, Home, Food for companies and organizations related to those areas.

### Organizational Cells

`cell:Organizational` cells relate to a person's role within organization:

1. **Customers** (`cell:Customers`) — customer organizations. Rename to "Clients", etc.
1. **Marketing** (`cell:Marketing`) — marketing activities, campaigns, and related organizations.
    - **Prospects** (`cell:Prospects`) - customer prospects. Rename to "Client prospects", etc.
1. **Partners** (`cell:Partners`) — firms that provide goods and services.
1. **People (org)** (`cell:People(org)`) — people the organization interacts with in a working capacity.
    - **Employees** (`cell:Employees`) — related to employees.
        - **Employee** (`cell:Employee`) — detailed information about a specific employee.
    - **Consultants (org)** (`cell:Consultants(org)`) — engaged consultants.
    - **Other (org)** (`cell:Other(org)`) — people associated with the organization who don't fit Employees, Consultants, or Colleagues.
    - **Colleagues** (`cell:Colleagues`) — coworkers and peers within the organization not tracked as formal Employee records.
    - **Advisors (org)** (`cell:Advisors(org)`) — individuals who advise the organization in a non-employee capacity.
    - **Board of Directors (org)** (`cell:BoardOfDirectors(org)`) — the organization's board members.
1. **KB** (`cell:KB`) — corporate knowledge bases.
1. **Projects (org)** (`cell:Projects(org)`) — projects related to R&D, manufacturing, sales, marketing, operations, HR, etc.
1. **Meetings (org)** (`cell:Meetings(org)`) — events, meetings, workshops, webinars, and gatherings.
    - **Conferences** (`cell:Conferences`) — a conference or professional gathering.
1. **Suppliers** (`cell:Suppliers`) — companies that supply goods or services to this organization.
1. **Legal (org)** (`cell:Legal(org)`) — contracts and agreements.
1. **Government (org)** (`cell:Government(org)`) — interactions with government organizations.
1. **Finances (org)** (`cell:Finances(org)`) — corporate finance-related matters.
    - **Banking & Payments (org)** (`cell:BankingPayments(org)`) — firms that help you store, access, and move your cash for daily living. These include Retail Banks & Credit Unions, which provide checking accounts, savings accounts, and debit cards. These also include Payment Processors like Visa, Mastercard, or PayPal that let you buy things online and in stores, and Remittance Firms like Western Union or Wise used to send money to family or friends, especially overseas.
    - **Investing (org)** (`cell:Investing(org)`) — firms that help you buy assets, so your money can grow over time for goals like buying a house or retiring. These include Brokerage Firms like Charles Schwab or Robinhood where you buy and sell stocks, bonds, and ETFs; Robo-Advisors, computer-run investing platforms like Betterment or Wealthfront that manage your portfolio for a low fee; and Mutual Fund companies like Vanguard or Fidelity that pool your money with other investors to buy a large bundle of stocks.
    - **Lending & Credit (org)** (`cell:LendingCredit(org)`) — firms that lend you money when you need to buy something expensive that you cannot pay for all at once. These include Mortgage Lenders, banks or specialized companies that give you loans specifically to buy a home; Consumer Finance Companies, that give out personal loans, auto loans, or student loans; and Credit Card Issuers, banks that give you a plastic card to borrow money on the spot for daily purchases.
    - **Insurance (org)** (`cell:Insurance(org)`) — firms that protect you and your family from financial ruin if something bad happens. These include Life & Health Insurance firms that cover medical bills or provide money to your family if you pass away, and Property & Casualty Insurance firms that insure your car, home, or apartment against accidents and theft.
    - **Advisory (org)** (`cell:Advisory(org)`) — firms and individuals who do not just hold your money, but tell you the best ways to use it. These include Financial Planners (Wealth Advisors), human experts who help you build a custom roadmap for taxes, retirement, and budgeting, and Estate Planners, specialized professionals who help you write wills and plan how to pass your money to your children. Also includes Accountants and Bookkeepers, who track your income and expenses and prepare your taxes.

### Cell DataBooks

Each node in the `cell:Cell` tree is represented by a **cell DataBook** (`.databook.md` file with `type: cell-databook`) linked to other nodes by the parent node's `cell:child` property (IRI) to its child. This tree contains a mixture of user-minted user-defined cells and copies of canonical cells. These copies contain a `copiedFrom:` IRI property pointing back to the corresponding canonical cell.

#### Canonical Cell DataBooks

`cell:Personal` cell DataBooks live in `cells-person/`, rooted at `cells-person/cells-person.databook.md`. `cell:Organizational` cell DataBooks live in `cells-org/`, rooted at `cells-org/cells-org.databook.md`.

#### Properties

The following properties are defined in `cell.ttl` and represented as `mia.` YAML fields in cell DataBooks, following the same pattern as `mia.cell` → `context:cell`:

| YAML field | Ontology property | Cardinality | Meaning |
|------------|-------------------|-------------|---------|
| `mia.cellType` | `cell:cellType` | 1 | The local name of the `cell:Cell` subclass this DataBook is or was copied from (e.g. `ImmediateFamily`, `Employees(org)`), or `Cell` itself if there is no canonical counterpart |
| `mia.num-parties` | `cell:num-parties` | 1 | The concrete `cell:Parties` subclass this DataBook instantiates: one of `OneParty`, `TwoParty`, `ThreePlusParty` |
| `mia.label` | `cell:label` | 1 | User-editable display name — defaults to the DataBook `title` but can be changed independently, leaving `title` and `id` immutable |
| `mia.note` | `cell:note` | 0..1 | Relative path to a markdown notes file for this cell (e.g. `People/Paula Walker/Paula Walker.md`) |
| `mia.folder` | `cell:folder` | 0..1 | Relative path to a folder of arbitrary files for this cell (e.g. `People/Paula Walker`) |
| `mia.copiedFrom` | `cell:copiedFrom` | 0..1 | IRI of the canonical cell this DataBook was copied from. Present only on copies of canonical cells |

Note files live in a folder hierarchy whose structure mirrors the cell hierarchy; associated file folders live in a parallel hierarchy whose names match the cell names.

#### Context link properties

Each cell DataBook in the user's tree may carry up to four optional links to context DataBook IRIs, corresponding to the four `c:XBXcontext` subtypes:

| Property | Value (`c:Context` subtype) | Cardinality | Applies to | Meaning |
|----------|---------------------|-------------|------------|---------|
| `cell:sbs` | `c:SBScontext` | 0..1 | `cell:Parties` cells (`OneParty` or `MultiParty`) | The user's own context in this cell |
| `cell:obs` | `c:OBScontext` | 0..1 on `TwoParty`; 0..N on `ThreePlusParty` | `cell:MultiParty` cells (`TwoParty` or `ThreePlusParty`) | The user's record of the other party |
| `cell:obo` | `c:OBOcontext` | 0..1 on `TwoParty`; 0..N on `ThreePlusParty` | `cell:MultiParty` cells (`TwoParty` or `ThreePlusParty`) | A context the other party presents |
| `cell:sbo` | `c:SBOcontext` | 0..1 on `TwoParty`; 0..N on `ThreePlusParty` | `cell:MultiParty` cells (`TwoParty` or `ThreePlusParty`) | A context the other party holds about the user |
| `cell:graph` | `c:Context` | 0..1 | All cells | A context that doesn't fit the self-vs-other classification — e.g. claims jointly maintained by multiple parties about a third party, or, on a `OneParty` cell, a context that simply doesn't need self-vs-other framing |

`cell:sbs`, `cell:obs`, `cell:obo`, `cell:sbo`, `cell:graph` links appear only in cells in the user's tree, not in canonical cells. `obs`/`obo`/`sbo` require another party to make sense, so their domain is `cell:MultiParty` rather than the broader `cell:Parties` or `cell:Cell` — a `OneParty` cell (just the user, no external party) can have `sbs` but not `obs`/`sbo`/`obo`. Their cardinality is capped at 1 for `TwoParty` cells (only one other party exists to have a record about) but unconstrained for `ThreePlusParty` cells (a group can have any number of other-party contexts). `cell:graph`'s domain deliberately stays the broader `cell:Cell` rather than `cell:MultiParty`, since it's also useful on a `OneParty` cell for a context that doesn't need self-vs-other classification at all — unlike `obs`/`sbo`/`obo`, it doesn't require another party to make sense.

### Cell Ontology File

- **`cell.ttl`** — The Cell ontology, defining:
  - *Classes*: `cell:Cell`, `cell:Personal`, `cell:Organizational`, `cell:UserDefined`, `cell:Parties`, `cell:OneParty`, `cell:MultiParty` (abstract), `cell:TwoParty`, `cell:ThreePlusParty`, and all leaf cell subclasses. `cell:Parties` is not `rdfs:subClassOf cell:Cell` (and vice versa) — every cell instance is formally typed as both, since the two hierarchies classify orthogonal facets of the same instance.
  - *Annotation properties*: `cell:cellType` (the `cell:Cell` subclass this DataBook is or was copied from, or `Cell` itself), `cell:num-parties` (concrete `cell:Parties` subclass — domain `cell:Parties`), `cell:label` (user-editable display name), `cell:note` (path to markdown notes file), `cell:folder` (path to associated file folder), `cell:copiedFrom` (IRI of the canonical cell this DataBook was copied from), `cell:abstract` (marks a class as not directly instantiated in DataBooks).
  - *Object properties*: `cell:sbs` (domain `cell:Parties`), `cell:obs`/`cell:obo`/`cell:sbo` (domain `cell:MultiParty`), `cell:graph`/`cell:child` (domain `cell:Cell`).
  These terms are referenced by name in the YAML frontmatter of each cell DataBook file. `cell.ttl` imports `context.ttl` (for the `c:SBScontext`/`c:OBScontext`/`c:OBOcontext`/`c:SBOcontext` ranges of `cell:sbs`/`cell:obs`/`cell:obo`/`cell:sbo`, and the plain `c:Context` range of `cell:graph`); `context.ttl` in turn imports `cell.ttl` (for `c:cell`'s range, `cell:Cell`, and to reuse `cell:abstract` on `c:Context`).

- **`cell-shacl.ttl`** — SHACL shapes for cell DataBook instances, split across the five classes that carry cell properties: `:CellShape` (target `cell:Cell`) constrains `cell:graph`, `cell:note`, and `cell:folder` to at most one value each, and `cell:cellType` to exactly one (open-ended — no enum, since new canonical subclasses can be added freely); `:PartiesShape` (target `cell:Parties`) constrains `cell:sbs` to at most one value and `cell:num-parties` to at most one value which, if present, must be one of `OneParty`, `TwoParty`, `ThreePlusParty`; `:OnePartyShape` (target `cell:OneParty`) forbids `cell:obs`/`cell:sbo`/`cell:obo` entirely, since a `OneParty` cell has no other party; `:TwoPartyShape` (target `cell:TwoParty`) constrains `cell:obs`, `cell:sbo`, and `cell:obo` to at most one value each, since a 1:1 cell has only one other party; `:ThreePlusPartyShape` (target `cell:ThreePlusParty`) leaves `cell:obs`/`cell:sbo`/`cell:obo` unconstrained (0..N), since a group cell can have any number of other-party contexts.

### Cell Ontology Validation

Cell DataBook instances are validated by `cell-shacl.ttl`.

## Persona Ontology

The Persona ontology defines a formal, machine-readable model of a person. It is used by Mia to represent the user as well as information about other people. Mia can bi-directionally synchronize information with other Mia users on a Personal Data Network (PDN).  

We represent a person with the `p:Person` class — a Mia-specific subclass of CCO `Person` (`cco:ont00001262`). Each context file contains exactly one `p:Person` individual. The Mia user's own `p:Person` individual always uses the IRI `:Self` across all of their context files; other people, groups, and organizations are assigned locally-minted named IRIs (e.g. `:Bob_Johnson`). These context files function as *named-graph slices* — each is an independent snapshot of an identity in a specific relationship or institutional context, carrying the claims relevant to that context: names, addresses, phone numbers, SSNs, physical characteristics, parent-child relationships, social connections, payment cards, and more. The Persona ontology reuses existing well-known ontologies wherever possible and defines new terms only where no suitable existing term exists.

<p align="center"><img src="images/persona-ontology/persona.png" alt="Persona model"></p>

### Key properties and classes

This section describes the most fundamental properties and classes in the Persona ontology. A person's identity data is spread across multiple named-graph slice files, each containing one `p:Person` individual. The Mia user's slices share the IRI `:Self`; each other person's slices share their locally-assigned named IRI.

**Classes**

* `p:Person` — a Mia-specific subclass of CCO `Person` (`cco:ont00001262`). Each context file (named-graph slice) contains exactly one `p:Person` individual. The Mia user's own `p:Person` always uses the IRI `:Self`, shared across all of their context files. Other people, groups, and organizations are assigned locally-minted named IRIs (e.g. `:Bob_Johnson`, `:Paula_Walker`). `:Self` is a local IRI and is never exposed externally over the PDN, so there are no collisions between Mia instances. All identity data — names, identifiers, addresses, social networks, payment cards, and more — attaches to this individual.

**Properties**

* `i:hasPDNidentifier` — links a `p:Person` to a `i:PDNidentifier` — the identifier used to communicate with this `Person` over the Personal Data Network. Sub-property of CCO `designated by`.


### Social classes and properties 

This section describes classes and properties related to a person's social network.

**Classes**

* `cco:ont00001183` - Social Network

**Properties**

* `p:hasSocialNetwork` - a social network — other people known by the `p:Person` carrying the social network. The holder is not included as a member part of the social network object, but *is* considered to be a part of it by virtue of holding the network entity.
* `BFO_0000115` - has member part. Links to `p:Person` members of this network.

### Possession-related classes and properties

This section describes properties and classes related to things a person has, holds, possesses, purchased, or rents. 

 - Physical plastic/paper cards are `MaterialArtifact` subclasses that include driver's license, health insurance card, payment card, etc.
 - Physical wallets - Cards may be placed in a wallet (via BFO `continuant part of`) or held directly by the `p:Person` (via `p:hasPhysicalCard`).

<p align="center"><img src="images/persona-ontology/persona-card.png" alt="Card possessions model"></p>

**Classes**

* `p:PhysicalCard` — a physical plastic or paper card (held in a wallet or carried directly).
* `p:PhysicalHealthInsuranceCard` (subclass of `p:PhysicalCard`) — a physical health insurance membership card.
* `p:PhysicalDriversLicense` (subclass of `p:PhysicalCard`) — a state-issued driver's license card.
* `p:PhysicalPaymentCard` (subclass of `p:PhysicalCard`) — a physical credit or debit card.
* `p:PhysicalSocialSecurityCard` (subclass of `p:PhysicalCard`) — a paper or plastic card issued by the Social Security Administration.
* `p:Wallet` — a physical wallet that can hold cash as well as various kinds of paper or plastic identity or payment cards.

**Properties**

* `is carrier of` (from BFO) — used to link a physical card to its corresponding `p:Person` in another context.
* `p:hasWallet` — links a `p:Person` to a physical wallet (see Possessions below).
* `p:hasImageScan` — a link to a scanned image of this card.
* `p:hasPhysicalCard` — links a `p:Person` to a `p:PhysicalCard` carried outside of a wallet (see Possessions below).

### Accounts

This section describes properties and classes related to a person's relationship with an online service provider. An online service account (`OnlineServiceAccount`, CCO `ont00000033`) records a person's credentials and identity with an online service provider such as Google or AT&T.

**Properties**

* `holds user account` (CCO) — links a `p:Person` to an `OnlineServiceAccount`.
* `has service name` (CCO) — the name of the online service (e.g. "Google").
* `has service URI` (CCO) — the URI of the online service.
* `has user handle` (CCO) — the user's handle or username on the service.
* `p:hasPassword` — the password credential for an `OnlineServiceAccount` (Persona ontology extension).

### Finance-related classes and properties

This section describes properties and classes related to a person's interactions with financial institutions.

**Classes**

* `p:CheckingAccount` — a bank checking account held by a person, linked to a debit card.
* `p:CheckingAccountNumber` — an identifier designating a bank checking account, connected via `designated by` (`ont00001879`).
* `p:RoutingNumber` — an ABA routing transit number identifying the financial institution, connected via `designated by`.

**Properties**

* `p:hasBankAccount` — links a `p:Person` to a `p:CheckingAccount` it records.
* `p:accessesBankAccount` — links a DebitCard to the `p:CheckingAccount` it draws funds from.

### Modeling details

This section describes a few details related to modeling names and addresses.

**Peer name pattern**: All name types (FullName, GivenName, FamilyName, AlternateName) connect directly to a `p:Person` via `designated by` (`ont00001879`). They are siblings, not nested under a PersonName parent. Legal names belong to the birth certificate context file (annotated `c:template p:BirthCertificate`); a preferred/goes-by name (AlternateName) belongs to each social or professional context where it applies.

**Address history**: Each address context file carries a `p:Person` with a USPostalAddress and an `AddressDesignation` with a `TemporalInterval` (start date required; no end date = current address).

### Persona Templates

`p:PersonaTemplate` is an abstract classification class that serves as the common superclass for all reusable, context-type-specific template labels. These labels are defined in `persona-templates.ttl`. A context file declares its template in the YAML frontmatter as `mia.template` rather than by typing its `p:Person` individual. Per-template SHACL files live in the `shacl/` subdirectory.

<p align="center"><img src="images/persona-ontology/persona-templates.png" alt="persona templates model"></p>

**Government-issued identity documents** — `p:BirthCertificate`, `p:DriversLicense`, and `p:Passport` are subclasses of both `p:PersonaTemplate` (template label use) and `p:IdentityDocument` (artifact instance use). `p:IdentityDocument` is the class for government-issued documents that formally identify a person. The property `p:hasIdentityDocument` (domain: `p:Person`, range: `p:IdentityDocument`) links a person to the government document they hold. Each government-ID context file declares one named individual of the document type and links it from `:Self`. `p:JSContactCard` is a format label only — not a government-issued document — and is a subclass of `p:PersonaTemplate` only.

The four currently defined subclasses of `p:PersonaTemplate` are:

* `p:BirthCertificate` — label for context files that carry a person's legal birth name record as issued by a state agency. Also a subclass of `p:IdentityDocument`. Declared in the YAML frontmatter as `mia.template: "persona:BirthCertificate"`. SHACL shape `:BirthCertificateDocumentShape` (in `shacl/birthcertificate-shacl.ttl`) targets the `p:BirthCertificate` document individual and validates the holding `p:Person` via `^persona:hasIdentityDocument`:
  - **Required**: either a `FullName` designator **or** both a `GivenName` and a `FamilyName` designator (via `designated by`, `ont00001879`) — expressed with `sh:or`.
  - **Optional**: `AdditionalName` (middle name), `AlternateName` (e.g. maiden name), `Nickname`, and `Legal Name` designators.

* `p:JSContactCard` — label for context files that carry professional contact details in the JSContact (RFC 9553) format. A digital contact format (RFC 9553) — not a government-issued identity document, and therefore not a subclass of `p:IdentityDocument`. Declared in the YAML frontmatter as `mia.template: "persona:JSContactCard"`. SHACL shape `:JSContactCardPersonShape` (in `shacl/jscontactcard-shacl.ttl`) enforces:
  - **Required**: exactly one `OrganizationName` designator; at least one `Email` or `TelephoneNumber` designator.
  - **Optional**: all name components, `OrganizationUnit`, `JobTitle`, addresses, online services, anniversaries, personal info, photo.
  - **Max 1** on all single-valued name and organization components.
  See the [JSContact field coverage table](#jscontact-field-coverage) below for the complete mapping.

* `p:DriversLicense` — label for context files that carry the identity claims on a state-issued driver's license. Also a subclass of `p:IdentityDocument`. Declared in the YAML frontmatter as `mia.template: "persona:DriversLicense"`. SHACL shape `:DriversLicenseDocumentShape` (in `shacl/driverslicense-shacl.ttl`) targets the `p:DriversLicense` document individual and validates the holding `p:Person` via `^persona:hasIdentityDocument`:
  - **Required**: `FullName` **or** (`GivenName` + `FamilyName`); exactly one `Birthdate` (`cco:ent00000046`); exactly one `p:DriversLicenseNumber`; exactly one `ExpirationDateIdentifier` (`cco:ent00000054`).
  - **Optional**: `AdditionalName`; `p:IssuingJurisdiction` (USPS 2-letter state code, validated by `USStateNameShape`); `PostalAddress`; `p:hasPhoto`.
  Note: `p:PhysicalDriversLicense` (in `persona.ttl`) models the physical card object held in a wallet — `p:DriversLicense` is the template label that marks a context file as carrying driver's license identity data.

* `p:Passport` — label for context files that carry the identity claims on a government-issued passport. Also a subclass of `p:IdentityDocument`. Declared in the YAML frontmatter as `mia.template: "persona:Passport"`. SHACL shape `:PassportDocumentShape` (in `shacl/passport-shacl.ttl`) targets the `p:Passport` document individual and validates the holding `p:Person` via `^persona:hasIdentityDocument`:
  - **Required**: `FullName` **or** (`GivenName` + `FamilyName`); exactly one `Birthdate` (`cco:ent00000046`); exactly one `p:PassportNumber`; exactly one `ExpirationDateIdentifier` (`cco:ent00000054`).
  - **Optional**: `AdditionalName`; `p:IssueDate`; `p:IssuingCountry`; `p:PlaceOfBirth`; `p:GenderMarker`; `p:hasPhoto`.

#### JSContact field coverage

The table below maps every JSContact (RFC 9553) property to its representation in the Persona ontology. Properties defined in `persona-templates.ttl` for JSContact alignment are marked **JSC**.

| JSContact Property | Card. | Ontology Representation | Via | SHACL constraint |
|---|:---:|---|---|:---:|
| `name.full` | 0..1 | `cco:ent00000001` FullName | `designated by` | max 1 |
| `name.given` | 0..1 | `cco:ent00000002` GivenName | `designated by` | max 1 |
| `name.surname` | 0..1 | `cco:ent00000004` FamilyName | `designated by` | max 1 |
| `name.given2` | 0..1 | `cco:ent00000003` AdditionalName | `designated by` | max 1 |
| `name.surname2` | 0..1 | `cco:ent00000058` Surname2 | `designated by` | max 1 |
| `name.prefix` | 0..1 | `cco:ent00000057` Title/HonorificPrefix | `designated by` | max 1 |
| `name.suffix` | 0..1 | `cco:ent00000005` Suffix (Jr., Sr., III) | `designated by` | max 1 |
| `name.credential` | 0..1 | **JSC** `p:Credential` (MD, PhD, Esq.) | `designated by` | max 1 |
| `nicknames` | 0..1 | `cco:ont00000990` Nickname | `designated by` | max 1 |
| `name.altName` | 0..1 | `cco:ent00000006` AlternateName | `designated by` | max 1 |
| `emails` | 0..N | `cco:ent00000024` EmailAddress | `designated by` | — |
| ↳ `contexts` | 0..N | **JSC** `p:contactContext` annotation | annotation property | — |
| `phones` | 0..N | `cco:ent00000023` TelephoneNumber | `designated by` | — |
| ↳ `contexts` | 0..N | **JSC** `p:contactContext` annotation | annotation property | — |
| ↳ `features` | 0..N | **JSC** `p:phoneFeature` annotation | annotation property | — |
| `addresses` | 0..N | `cco:ent00000010` USPostalAddress | (address pattern) | — |
| ↳ `contexts` | 0..N | **JSC** `p:contactContext` annotation | annotation property | — |
| `anniversaries` (birth) | 0..1 | `cco:ent00000046` Birthdate | `designated by` | max 1 |
| `anniversaries` (other) | 0..N | **JSC** `p:Anniversary` | `p:hasAnniversary` | — |
| ↳ `kind` | — | **JSC** `p:anniversaryKind` | datatype property | — |
| ↳ `date` | — | **JSC** `p:anniversaryDate` | datatype property | — |
| ↳ `label` | — | **JSC** `p:anniversaryLabel` | datatype property | — |
| `organizations[].name` | 0..1 | `cco:ent00000047` OrganizationName | `designated by` | max 1 |
| `organizations[].units` | 0..1 | **JSC** `p:OrganizationUnit` | `designated by` | max 1 |
| `titles[].name` | 0..1 | **JSC** `p:JobTitle` | `designated by` | max 1 |
| `onlineServices` (account) | 0..N | `cco:ont00000033` OnlineServiceAccount | `holds user account` | — |
| `onlineServices` (URL) | 0..N | **JSC** `p:WebURL` | `designated by` | — |
| ↳ `service` | 0..N | **JSC** `p:serviceLabel` annotation | annotation property | — |
| `personalInfo` | 0..N | **JSC** `p:PersonalInfo` | `p:hasPersonalInfo` | — |
| ↳ `kind` | — | **JSC** `p:personalInfoKind` | datatype property | — |
| ↳ `value` | — | **JSC** `p:personalInfoValue` | datatype property | — |
| ↳ `level` | — | **JSC** `p:personalInfoLevel` | datatype property | — |
| `photos[].uri` | 0..N | **JSC** `p:hasPhoto` (xsd:anyURI) | datatype property | — |
| `legalName` | 0..1 | `cco:ont00001331` Legal Name | `designated by` | — |
| `uid` | 1 | IRI of the `p:Person` individual | — | — |
| `notes` | 0..N | `Person` Note via `has text value` | `designated by` | — |
| `relatedTo` | 0..N | `BFO_0000115` (member) | object property | — |
| `updated` | 0..1 | `version:` in the DataBook YAML frontmatter | YAML field | — |
| `language` | 0..1 | *(not yet mapped)* | — | — |
| `cells` | 0..N | *(not yet mapped)* | — | — |
| `preferredLanguages` | 0..N | *(not yet mapped)* | — | — |


### Persona Ontology Files

- **`persona.ttl`** — The Persona ontology. Imports the domain ontologies above and documents which classes and properties Mia uses (required vs. optional). Defines `p:Person` (Mee-specific subclass of CCO `Person`), Mia-specific extension properties (`p:hasSocialNetwork`, `p:hasPaymentCard`, `p:hasBankAccount`, etc.), and the core data model classes (physical card classes, banking classes, and others).
- **`persona-templates.ttl`** — Defines `p:PersonaTemplate` (abstract classification superclass) and the five concrete subtypes `p:BirthCertificate`, `p:JSContactCard`, `p:DriversLicense`, `p:Passport`, and `p:MedicalAppointment`. These are used as values of `mia.template` in the DataBook YAML frontmatter — they classify the context file, not the `p:Person` individual inside it. Also defines `p:IdentityDocument` (superclass for government-issued identity document artifacts) and `p:hasIdentityDocument` (links a `p:Person` to a `p:IdentityDocument` individual they hold); `p:BirthCertificate`, `p:DriversLicense`, and `p:Passport` are subclasses of both `p:PersonaTemplate` and `p:IdentityDocument`. Also defines related designator classes (`p:DriversLicenseNumber`, `p:IssuingJurisdiction`, `p:PassportNumber`, `p:IssuingCountry`, `p:PlaceOfBirth`, `p:GenderMarker`, `p:IssueDate`, `p:Credential`, `p:WebURL`, `p:OrganizationUnit`, `p:JobTitle`), complex information classes (`p:Anniversary`, `p:PersonalInfo`), annotation properties for JSContact channel labels (`p:contactContext`, `p:phoneFeature`, `p:serviceLabel`), `p:hasPhoto`, and the `p:MedicalAppointment` claim properties (`p:forPatient`, `p:hasPrimaryCarePhysician`, `p:currentMedication`, `p:allergy`, `p:medicalHistoryNote`, `p:insuranceProvider`, `p:insurancePolicyNumber`, `p:insuranceGroupNumber`, `p:preferredPharmacy`). Imported by `persona.ttl` so all context files inherit these classes transitively.

- **`shacl/birthcertificate-shacl.ttl`** — SHACL shapes for birth certificate context files (`c:template p:BirthCertificate`). `:BirthCertificateDocumentShape` targets `p:BirthCertificate` document individuals directly — all identity claims (names) are properties of the document individual, not the `p:Person`. Enforces: FullName OR (GivenName + FamilyName) required; optional AdditionalName, AlternateName, Nickname, Legal Name.

- **`shacl/jscontactcard-shacl.ttl`** — SHACL shapes for JSContactCard context files (`c:template p:JSContactCard`). Validates `p:Person` instances:
  - OrganizationName required (1..1); at least one Email or TelephoneNumber required; all name components and OrganizationUnit/JobTitle optional (0..1 each).

- **`shacl/driverslicense-shacl.ttl`** — SHACL shapes for driver's license context files (`c:template p:DriversLicense`). `:DriversLicenseDocumentShape` targets `p:DriversLicense` document individuals directly — all identity claims are properties of the document individual, not the `p:Person`. Enforces: FullName OR (GivenName + FamilyName) required; Birthdate, DriversLicenseNumber, ExpirationDateIdentifier required (1..1 each); IssuingJurisdiction, PostalAddress, and hasPhoto optional.

- **`shacl/passport-shacl.ttl`** — SHACL shapes for passport context files (`c:template p:Passport`). `:PassportDocumentShape` targets `p:Passport` document individuals directly — all identity claims are properties of the document individual, not the `p:Person`. Enforces: FullName OR (GivenName + FamilyName) required; Birthdate, PassportNumber, ExpirationDateIdentifier required (1..1 each); IssueDate, IssuingCountry, PlaceOfBirth, GenderMarker, and hasPhoto optional.

- **`persona-shacl.ttl`** — SHACL constraint rules for all `p:Person` individuals across all context files. Validates properties including:
  - *All `p:Person` instances*: SSN format (`NNN-NN-NNNN`), email format, phone (E.164), address cardinality, payment cards, wallet, social network, bank account
  - *US Postal Address*: required street, city, state (USPS 2-letter), ZIP; optional country
  - *`p:Person`*: scalp hair (0..1); `has mother` / `is mother of` range must be a `p:Person`
  - *Social Network*: sub-groups (via `has part`) must be Social Networks; members (via `has member part`) must be `p:Person` instances
  - *Debit Card*: card number and expiration date required; CVV optional
  - *`p:Wallet`*: items declaring themselves `continuant part of` this wallet must be `p:PhysicalCard` instances
  - *`p:PhysicalCard`*: image scan, if present, must be `xsd:anyURI` (max 1); `continuant part of` target, if present, must be a `p:Wallet` (max 1)

### Persona Ontology Validation

`persona-shacl.ttl` runs against merged data from all context files (Tier 1 validation). Per-template SHACL files in `shacl/` run against individual context files (Tier 2): birth certificate, JSContactCard, driver's license, passport, and medical appointment each have their own shape file and are validated separately to avoid their `sh:targetClass` constraints firing on every relevant slice in the merged dataset. See the [Validation](#validation) section for commands.

## Organization Ontology

The Organization ontology models organizations — companies, government agencies, nonprofits, and other institutions — that participate in the Personal Data Network. An organization has a PDN identity — an `i:Organization` identifier — that allows Mia to communicate with it as with any other node on the network.

<p align="center"><img src="images/organization-ontology/organization.png" alt="Organization model"></p>

**Classes**

* `o:Organization` — an organization (company, government agency, corporation, nonprofit, etc.) on the Personal Data Network.

### Organization Ontology File

- **`organization.ttl`** — The Organization ontology. Imports `pdn-identity.ttl`.

### Organization Ontology Validation

`organization-shacl.ttl` validates `o:Organization` instances. Key constraint: each `o:Organization` must have exactly one `i:hasPDNidentifier` value of type `i:Organization`.

## Group Ontology

The Group ontology introduces the concept of a *shared* group (`g:Group`) whose members are individuals and/or organizations. The group entity *itself* as well as any attached properties are shared with all of its members. Like individuals and organizations, `g:Groups` have their own PDN identifiers and can be communicated with as with any other node on the PDN.

<p align="center"><img src="images/group-ontology/group.png" alt="Group model"></p>

**Classes**

* `g:Group` — a group of people and/or organizations on the Personal Data Network.

### Group Ontology File

- **`group.ttl`** — The Group ontology. Imports `pdn-identity.ttl`.

### Group Ontology Validation

`group-shacl.ttl` validates `g:Group` instances. Key constraint: each `g:Group` must have exactly one `i:hasPDNidentifier` value of type `i:Group`.

## PDN Identity Ontology

The Identity ontology is used to describe the kinds of identities that Mia can communicate with over the internet using Personal Data Network protocols. The root class, `i:PDNidentifier`, has three subclasses:

<p align="center"><img src="images/identity-ontology/identity.png" alt="types of MeeIdentities"></p>

**Classes**

* `i:Individual` - an identifier of a human Mia user.
* `i:Group` - an identifier of a `g:Group` of Mia users and/or `o:Organizations`.
* `i:Organization` - an identifier of an `o:Organization`.

**Well-known individual**

* `i:Self` — a singleton individual of `i:Individual` representing the current Mia user's PDN identity. The corresponding `p:Person` individual `:Self` is what appears in `mia.claimant` and `mia.subject` fields. Every other Mia user is represented by a locally-assigned named individual of `i:Individual`.

### PDN Identity Ontology File

- **`pdn-identity.ttl`** — The PDN Identity ontology. 

### PDN Identity Ontology Validation

`pdn-identity-shacl.ttl` validates `i:PDNidentifier` instances. Key constraint: each instance must be typed as exactly one of `i:Individual`, `i:Group`, or `i:Organization`.

## Illustrative Example: Alice 

This section describes the local Mia dataset for a hypothetical user, Alice Walker. Alice's data lives in multiple context DataBooks linked to by a tree structure of cell DataBooks. 

### Alice's Cells and Contexts

Alice interacts with other people, organizations and groups in contexts of different types, with each context file holding a named-graph. 

Alice's context DataBooks are in `example/contexts.` Some are authored by Alice (self-claimed data--data she entered herself into her Mia app); others contain data received from peer Mia users or organizational peers over PDN and stored locally. In either case, Alice is the Mia user, so the `p:Person` that represents her uses the IRI `:Self` across all of her context files. Other people — Bob Johnson, Paula Walker — and groups such as BHS use locally-assigned named IRIs (e.g. `:Bob_Johnson`, `:Paula_Walker`, `:BHS`). When data arrives from a peer's Mia (where that peer was `:Self` in their own instance), Alice's Mia assigns them a locally-minted identifier; once a PDN connection is established, that identifier resolves to their PDN id.

Alice's cell DataBooks are in `example/cells/`. The full tree can be walked starting from `example/cells/cells.databook.md`. It contains two kinds of entries:

- **Copies of canonical cells** (`mia.cellType` set to the specific class it was copied from, e.g. `People`, `Employees`) — one for each of the 16 top-level cells and their child cells. Each copy carries a `copiedFrom:` property pointing to the corresponding canonical IRI (e.g. `copiedFrom: "http://mee.foundation/ontologies/cells-person/people"`). Context links (`cell:sbs`, `cell:obs`, `cell:obo`, `cell:sbo`) to Alice's contexts are attached here, not in the canonical tree.
- **User-defined cells** (`mia.cellType: Cell`) — one per specific person, company, government agency, or group Alice interacts with (e.g. `bob-johnson(others)`, `acme(work)`, `citibank(banking-payments)`).

#### Cell and Context Diagrams

The following sequence of diagrams maps out the cells and contexts of our Alice example. We start with the People cell--Alice's relationship with someone she knows named Bob Johnson. Bob is someone Alice knows but who isn't family or a close friend, so she has filed him under the Others cell rather than Friends. 

Contexts with dotted outlines are placeholders for contexts in cell — Alice could fill a context in any of these placeholders if she wishes, and the claims in the context. 

<p align="center"><img src="example/images/people.png" alt="People cells"></p>

Alice's mother, Paula Walker, is filed under Immediate Family. Alice's own Health & Wellness cell — Medical, Dental, Vision, and Wellness — is nested within Paula's own cell, since caring for Paula's health is central to why Alice tracks health information at all. Under Medical > Providers, Alice keeps a record of Dr. Jane Kopakolva, Paula's primary care physician (context #25). Alice and her sister, Carol, are also taking care of their mother Paula Walker and need to arrange medical appointments for her. To do so, they need to share and synchronize medical information about Paula including her list of medications, medical history, health insurance policy, contact information and so on. Alice creates a two-party Medical Appointment Info cell with Carol, also filed under Medical > Providers, that they use to share information about Paula. The medical information claims are captured in triples shown in the filled grey circle. Of the many claims, one of them will be the name of Paula's doctor (primary care physician), copied from the Dr. Jane Kopakolva cell shown in the same diagram. The resulting tree, from People down through both provider cells, is shown below:

<p align="center"><img src="example/images/people2.png" alt="People cells, continued — Immediate Family, Paula Walker, and her Health & Wellness, Medical, and Providers cells"></p>

*(This diagram is a work in progress and will be expanded to show the Health & Wellness cell in more detail.)*

<p align="center"><img src="example/images/health.png" alt="Health & Wellness cell (work in progress)"></p>

Alice is an employee of Acme, so under her Work cell she has created a user-defined cell called Acme to represent her employer. Since Acme is an organization, Alice has under her Acme cell switched from adding `cell:Personal` cells to `cell:Organizational` cells (light blue color) and added an Employees cell which acts as a parent holding an Employee cell for each person there she tracks, including herself. Her own "Alice Walker" cell holds her Business Card claims — job title at Acme, work telephone number, work email, etc. One of the employees she works with is Paula Walker, so she adds a Paula Walker cell too.
<p align="center"><img src="example/images/work.png" alt="Work cells"></p>

Alice has relationships with two companies, Google and AT&T:
<p align="center"><img src="example/images/companies.png" alt="Companies cells"></p>

Alice has a relationship with Citibank. In our example Citibank exists as a node on the PDN and directly claims information about their customer, Alice in context #9.
<p align="center"><img src="example/images/finances.png" alt="Financial cells"></p>


Here are the cells related to Alice's interactions with various state governments:
<p align="center"><img src="example/images/gov-state.png" alt="Government — State cells"></p>
Here are the cells related to Alice's interactions with the federal government:
<p align="center"><img src="example/images/gov-federal.png" alt="Government — Federal cells"></p>

Here are the cells related to Alice's interactions with two municipal governments:

<p align="center"><img src="example/images/gov-municipality.png" alt="Government — Municipality cells"></p>

Here are Alice's cells related to her personal health and her possessions:
<p align="center"><img src="example/images/misc.png" alt="Miscellaneous cells"></p>

The last diagram shows Alice's membership in the Boston Hub Society, an informal professional social network that exists as a `i:Group` node on the PDN:
<p align="center"><img src="example/images/affiliations.png" alt="Affiliations cells"></p>

The contexts in the table below are *about* Alice and claimed *by* Alice. All `.databook.md` files are in the `example/contexts/` folder.

| #  | DataBook file                                                                          | Context type | Key data                                                         | Diagram |
|--- |:--------------------------------------------------------------------------------------|:-------------|:-----------------------------------------------------------------|:--------|
| 10 | [self.self(alice-walker)(acme)(10)](example/contexts/self.self(alice-walker)(acme)(10).databook.md) | Employee     | Business card — given name, family name, email, phone, employer  | [view](example/contexts/images/self.self(alice-walker)(acme)(10).png) |
| 11 | [self.self(att)(companies)(11)](example/contexts/self.self(att)(companies)(11).databook.md)                     | Companies    | Phone number                                                     | [view](example/contexts/images/self.self(att)(companies)(11).png) |
| 12 | [self.self(bob-johnson)(others)(12)](example/contexts/self.self(bob-johnson)(others)(12).databook.md)                     | Others       | Alice's 1:1 context with Bob; social network with Bob as member  | [view](example/contexts/images/self.self(bob-johnson)(others)(12).png)|
| 13 | [self.self(boston)(municipality)(13)](example/contexts/self.self(boston)(municipality)(13).databook.md)               | Municipality | Previous address — Boston, MA (2020–2025) with temporal interval | [view](example/contexts/images/self.self(boston)(municipality)(13).png) |
| 14  | [self.self(boston-hub-society)(affiliations)(14)](example/contexts/self.self(boston-hub-society)(affiliations)(14).databook.md)                     | Affiliations | BHS profile: email, phone and current address                    | [view](example/contexts/images/self.self(boston-hub-society)(affiliations)(14).png)|
| 15 | [self.self(california-dmv)(state)(15)](example/contexts/self.self(california-dmv)(state)(15).databook.md) | State      | California driver's license — legal name, DOB, DL#, expiry, photo | [view](example/contexts/images/self.self(california-dmv)(state)(15).png) |
| 16 | [self.self(google)(companies)(16)](example/contexts/self.self(google)(companies)(16).databook.md)               | Companies    | Gmail address                                                    | [view](example/contexts/images/self.self(google)(companies)(16).png) |
| 17 | [self.self(health-wellness)(17)](example/contexts/self.self(health-wellness)(17).databook.md)                 | Health & Wellness     | Physical body — height (68 in.), blue eyes, grey hair            | [view](example/contexts/images/self.self(health-wellness)(17).png) |
| 18 | [self.self(paradise)(municipality)(18)](example/contexts/self.self(paradise)(municipality)(18).databook.md)           | Municipality | Current address — Paradise, CA (2025–present)                    | [view](example/contexts/images/self.self(paradise)(municipality)(18).png) |
| 19 | [self.self(passport)(federal)(19)](example/contexts/self.self(passport)(federal)(19).databook.md)             | Federal    | US passport — legal name, DOB, passport#, issue/expiry, place of birth, gender marker, photo | [view](example/contexts/images/self.self(passport)(federal)(19).png) |
| 20 | [self.self(paula-walker)(acme)(20)](example/contexts/self.self(paula-walker)(acme)(20).databook.md)                   | Employee     | Acme employee context; company email; works with Paula           | [view](example/contexts/images/self.self(paula-walker)(acme)(20).png)|
| 21 | [self.self(paula-walker)(immediate-family)(21)](example/contexts/self.self(paula-walker)(immediate-family)(21).databook.md)   | Immediate Family       | Alice as a family member                       | [view](example/contexts/images/self.self(paula-walker)(immediate-family)(21).png) |
| 22 | [self.self(ownership)(22)](example/contexts/self.self(ownership)(22).databook.md)     | Ownership  | Wallet (driver's license + payment card); health ins., SSN card  | [view](example/contexts/images/self.self(ownership)(22).png) |
| 23 | [self.self(social-security-administration)(federal)(23)](example/contexts/self.self(social-security-administration)(federal)(23).databook.md)                     | Federal      | Social security number (SSN)                                     | [view](example/contexts/images/self.self(social-security-administration)(federal)(23).png) |
| 24 | [self.self(texas-vital-records)(state)(24)](example/contexts/self.self(texas-vital-records)(state)(24).databook.md) | State        | Legal names, maiden name                                         | [view](example/contexts/images/self.self(texas-vital-records)(state)(24).png) |

The following table lists contexts that are *about* Alice but claimed by others.

| #  | DataBook file                                                                         | Context type | Key data                             | Diagram |
|--- |:-------------------------------------------------------------------------------------|:-------------|:-------------------------------------|:--------|
| 8  | [self.bob-johnson(bob-johnson)(others)(08)](example/contexts/self.bob-johnson(bob-johnson)(others)(08).databook.md)                         | Others            | Alice as seen by Bob                 | [view](example/contexts/images/self.bob-johnson(bob-johnson)(others)(08).png)|
| 9 | [self.citibank(citibank)(banking-payments)(09)](example/contexts/self.citibank(citibank)(banking-payments)(09).databook.md)     | Banking & Payments | Debit card                           | [view](example/contexts/images/self.citibank(citibank)(banking-payments)(09).png) |

The following table lists contexts about other people (Paula and Bob) or groups (Boston Hub Society) in Alice's Mia. All files are in `example/contexts/`.

| #  | DataBook file                                                                                     | Context type | Key data                                                         | Diagram |
|--- |:-------------------------------------------------------------------------------------------------|:-------------|:-----------------------------------------------------------------|:--------|
| 1  | [bhs-group.members(boston-hub-society)(affiliations)(01)](example/contexts/bhs-group.members(boston-hub-society)(affiliations)(01).databook.md)             | Affiliations | BHS group instance with Alice and Bob as members                | [view](example/contexts/images/bhs-group.members(boston-hub-society)(affiliations)(01).png) |
| 2  | [bob-johnson.bob-johnson(bob-johnson)(others)(02)](example/contexts/bob-johnson.bob-johnson(bob-johnson)(others)(02).databook.md)                     | Others       | Bob's self-claimed Bob persona                                 | [view](example/contexts/images/bob-johnson.bob-johnson(bob-johnson)(others)(02).png)|
| 3  | [bob-johnson.bob-johnson(boston-hub-society)(affiliations)(03)](example/contexts/bob-johnson.bob-johnson(boston-hub-society)(affiliations)(03).databook.md)                     | Affiliations | Bob's BHS member persona (name, email, phone, address)          | [view](example/contexts/images/bob-johnson.bob-johnson(boston-hub-society)(affiliations)(03).png) |
| 4  | [bob-johnson.self(bob-johnson)(others)(04)](example/contexts/bob-johnson.self(bob-johnson)(others)(04).databook.md)                 | Others       | Alice's notes about Bob; fav drink: oat milk cappuccino         | [view](example/contexts/images/bob-johnson.self(bob-johnson)(others)(04).png) |
| 5  | [paula-walker.paula-walker(paula-walker)(immediate-family)(05)](example/contexts/paula-walker.paula-walker(paula-walker)(immediate-family)(05).databook.md) | Immediate Family       | Paula's own family persona; social network with Alice       | [view](example/contexts/images/paula-walker.paula-walker(paula-walker)(immediate-family)(05).png)|
| 6  | [paula-walker.self(paula-walker)(acme)(06)](example/contexts/paula-walker.self(paula-walker)(acme)(06).databook.md)           | Employee     | Paula as Alice's Acme colleague (Alice-claimed)                | [view](example/contexts/images/paula-walker.self(paula-walker)(acme)(06).png)|
| 7  | [paula-walker.self(paula-walker)(immediate-family)(07)](example/contexts/paula-walker.self(paula-walker)(immediate-family)(07).databook.md) | Immediate Family       | Paula as Alice's family member (Alice-claimed)           | [view](example/contexts/images/paula-walker.self(paula-walker)(immediate-family)(07).png)|
| 25 | [jane-kopakolva.self(jane-kopakolva)(25)](example/contexts/jane-kopakolva.self(jane-kopakolva)(25).databook.md) | Primary Care Physician       | Alice's record of Dr. Jane Kopakolva, Paula Walker's primary care physician           | [view](example/contexts/images/jane-kopakolva.self(jane-kopakolva)(25).png)|
| 26 | [context(alice-carol-about-mom)(health)(26)](example/contexts/context(alice-carol-about-mom)(health)(26).databook.md) | Medical Appointment       | Alice and Carol's shared claims for Paula's medical appointment — medications, allergies, insurance, PCP reference           | [view](example/contexts/images/context(alice-carol-about-mom)(health)(26).png)|



### Named graph scoping and context-specific membership

A `BFO_0000115` (has member part) triple on a Social Network individual — for example, `:Alice_Family_Network BFO_0000115 :Paula_Walker` in context 21 — targets `:Paula_Walker` as a person entity, not as a context-specific slice of her data. The named graph architecture provides the isolation: that triple lives inside context 21's named graph, and when an application needs "Paula Walker's family context data" it queries context 21's graph together with context 5's graph, rather than the full merged dataset.

This is the correct design for three reasons:

- **BFO semantics**: changing the range of `BFO_0000115` to a DataBook document IRI (e.g. `<https://www.example.org/mia/contexts/paula-walker.self(paula-walker)(immediate-family)(07)>`) would be a semantic error — the range of `has member part` must be a continuant (a person or group), not a document.
- **Model simplicity**: introducing context-specific "view" individuals (e.g. `:Paula_Walker_Family`) would reintroduce the layered complexity that the removal of `p:Persona` was designed to eliminate.
- **Tooling maturity**: annotating the triple with RDF-star (`<< :Alice_Family_Network BFO_0000115 :Paula_Walker >> mia:inContext <...>`) is a valid future option, but is not yet supported by Protégé and remains non-standard.

The practical implication is that **Tier 1 validation** (which merges all graphs) correctly finds all reachability links across the full dataset, while **application queries** that display a social network's members should join against specific context named graphs rather than the full triplestore merge.

## Diagrams

`draw.py` generates a Mermaid (`.mmd`) and PNG diagram from any context DataBook file:

```bash
python3 draw.py example/contexts/self.citibank(citibank)(banking-payments)(09).databook.md
python3 draw.py example/contexts/self.self(paradise)(municipality)(18).databook.md
```

Both output files are written to the same `images/` directory as the existing PNG diagrams.

**Dependencies** (one-time setup):
```bash
pip install rdflib pyyaml
npm install -g @mermaid-js/mermaid-cli
```

Each diagram shows the `p:Person` individual (yellow), supporting named individuals (white boxes), class labels (plain text), blank-node designator chains, and literal values (green).

## Validation

Validation requires [Apache Jena](https://jena.apache.org/) (`riot`, `shacl`) and the [DataBook CLI](https://github.com/w3c-cg/holon/tree/main/architectures/databook/implementations/js) (`databook`; install: `cd /tmp/holon/architectures/databook/implementations/js && npm install && npm install -g .`). SHACL shapes remain plain Turtle (`.ttl`).

### Quick check — DataBook syntax

Verify that every DataBook file has valid YAML frontmatter and well-formed block annotations:

```bash
for f in $(find example -name "*.databook.md" \
             -not -path "*/under-development/*" | sort); do
  databook head "$f" -q > /dev/null || echo "FAIL: $f"
done
```

A file that fails here will also fail silently in `databook extract`, producing no Turtle output and causing downstream `riot` or SHACL errors that are harder to trace.

### Tier 1 — general validation (all context files)

`persona-shacl.ttl` applies to every `p:Person` individual across all context files.

```bash
# Step 1 — extract turtle from every DataBook file (excluding under-development)
for f in $(find example -name "*.databook.md" \
             -not -path "*/under-development/*" | sort); do
  databook extract "$f" 2>/dev/null
done > /tmp/mia-data.ttl

# Step 2 — merge data with all ontology files and foundation ontologies
riot --output=turtle \
  project_files/bfo-core.ttl \
  project_files/PersonOntology.ttl \
  project_files/AddressOntology.ttl \
  project_files/StagingOntology.ttl \
  persona.ttl persona-templates.ttl context.ttl cell.ttl \
  pdn-identity.ttl group.ttl organization.ttl \
  /tmp/mia-data.ttl \
  2>/dev/null > /tmp/mia-merged.ttl

# Step 3 — collect shapes (shacl/ per-template files excluded — see Tier 2)
grep -v 'owl:imports' persona-shacl.ttl > /tmp/mia-shapes.ttl

# Step 4 — validate
shacl validate --shapes /tmp/mia-shapes.ttl --data /tmp/mia-merged.ttl --text
```

Expected output: `Conforms`

### Tier 2 — per-template validation (individual context files)

The `shacl/` shapes target document classes (`p:BirthCertificate`, `p:DriversLicense`, `p:Passport`, `p:MedicalAppointment`) or `p:Person` (JSContactCard). Each template SHACL file is run against only the relevant context file merged with the foundation ontologies.

```bash
# Shared base: foundation ontologies + application ontologies
riot --output=turtle \
  project_files/bfo-core.ttl \
  project_files/PersonOntology.ttl \
  project_files/AddressOntology.ttl \
  project_files/StagingOntology.ttl \
  persona.ttl persona-templates.ttl context.ttl cell.ttl \
  pdn-identity.ttl group.ttl organization.ttl \
  2>/dev/null > /tmp/mia-base.ttl

# BirthCertificate — self.self(texas-vital-records)(state)(24).databook.md
databook extract "example/contexts/self.self(texas-vital-records)(state)(24).databook.md" 2>/dev/null > /tmp/data-birth-cert-raw.ttl
riot --output=turtle /tmp/mia-base.ttl /tmp/data-birth-cert-raw.ttl 2>/dev/null > /tmp/data-birth-cert.ttl
grep -v 'owl:imports' shacl/birthcertificate-shacl.ttl > /tmp/shapes-birth-cert.ttl
shacl validate --shapes /tmp/shapes-birth-cert.ttl --data /tmp/data-birth-cert.ttl --text

# JSContactCard — self.self(alice-walker)(acme)(10).databook.md
databook extract "example/contexts/self.self(alice-walker)(acme)(10).databook.md" 2>/dev/null > /tmp/data-jscontact-raw.ttl
riot --output=turtle /tmp/mia-base.ttl /tmp/data-jscontact-raw.ttl 2>/dev/null > /tmp/data-jscontact.ttl
grep -v 'owl:imports' shacl/jscontactcard-shacl.ttl > /tmp/shapes-jscontact.ttl
shacl validate --shapes /tmp/shapes-jscontact.ttl --data /tmp/data-jscontact.ttl --text

# DriversLicense — self.self(california-dmv)(state)(15).databook.md
databook extract "example/contexts/self.self(california-dmv)(state)(15).databook.md" 2>/dev/null > /tmp/data-dl-raw.ttl
riot --output=turtle /tmp/mia-base.ttl /tmp/data-dl-raw.ttl 2>/dev/null > /tmp/data-dl.ttl
grep -v 'owl:imports' shacl/driverslicense-shacl.ttl > /tmp/shapes-dl.ttl
shacl validate --shapes /tmp/shapes-dl.ttl --data /tmp/data-dl.ttl --text

# Passport — self.self(passport)(federal)(19).databook.md
databook extract "example/contexts/self.self(passport)(federal)(19).databook.md" 2>/dev/null > /tmp/data-passport-raw.ttl
riot --output=turtle /tmp/mia-base.ttl /tmp/data-passport-raw.ttl 2>/dev/null > /tmp/data-passport.ttl
grep -v 'owl:imports' shacl/passport-shacl.ttl > /tmp/shapes-passport.ttl
shacl validate --shapes /tmp/shapes-passport.ttl --data /tmp/data-passport.ttl --text

# MedicalAppointment — context(alice-carol-about-mom)(health)(26).databook.md
databook extract "example/contexts/context(alice-carol-about-mom)(health)(26).databook.md" 2>/dev/null > /tmp/data-medical-appt-raw.ttl
riot --output=turtle /tmp/mia-base.ttl /tmp/data-medical-appt-raw.ttl 2>/dev/null > /tmp/data-medical-appt.ttl
grep -v 'owl:imports' shacl/medical-appointment-shacl.ttl > /tmp/shapes-medical-appt.ttl
shacl validate --shapes /tmp/shapes-medical-appt.ttl --data /tmp/data-medical-appt.ttl --text
```

Expected output for each: `Conforms`
