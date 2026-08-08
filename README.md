# Mia Ontologies

This document describes the ontologies used by the Mee Identity Agent (Mia) software application. The application lets the user create *cells* – private, secure collaboration spaces which can be joined by other Mia users and/or nodes on the Personal Data Network (PDN) hosted by groups, or organizations. 

The following **domain ontologies** model claims about people, organizations, groups, and other subjects — these claims live in `t:SCTopicGraph` instances. They import and profile existing ontologies — documenting which of their classes and properties Mia requires or uses — and extending them with Mia-specific classes and properties

- **Persona ontology** — models a person: names, addresses, phone numbers, relationships, payment cards, and more. It is built on BFO (Basic Formal Ontology) and CCO (Common Core Ontologies) as the upper ontological foundation, and on domain ontologies that extend CCO:
  - **PersonOntology** — person, name types, parent-child relationships
  - **AddressOntology** — postal address structure
  - **StagingOntology** — staging area for terms pending promotion (phone numbers, email addresses, user accounts, etc.)
  - **AgentOntology** — agents and their properties (imported transitively via PersonOntology)
- **Organization ontology** — models organizations (companies, government agencies, non-profits, etc.) 
- **Group ontology** — a group made up of individuals and/or organizations.

Also included are the Category, Cell and Topic **metadata ontologies**. *Categories* are used to organize *cells* into a tree structure of subject areas. *Cells* are data spaces that can be shared with other users and organizations. Cells contain content including files (including folder notes), folders, chat streams, as well as structure information blocks called *topics* that typically follow the Persona ontology.

Throughout this document we use these short-hands:

- `cat:` for the `category:` namespace (`http://mee.foundation/ontologies/category#`)
- `c:` for the `cell:` namespace (`http://mee.foundation/ontologies/cell#`)
- `t:` for the `topic:` namespace (`http://mee.foundation/ontologies/topic#`)
- `p:` for the `persona:` namespace (`http://mee.foundation/ontologies/persona#`)
- `o:` for the `organization:` namespace (`http://mee.foundation/ontologies/organization#`).
- `g:` for the `group:` namespace (`http://mee.foundation/ontologies/group#`)

See [**EXAMPLE.md**](EXAMPLE.md) for an illustration of the use of these ontologies by a hypothetical Mia user, Alice, along with diagram-generation and validation instructions for the example dataset.

## Category Ontology

Using Mia the user creates category trees (filesystem folders) to organize cells that they create themselves or are shared with them. Mia encourages the user to create these folders following the pattern of the tree of `cat:Category` classes and subclasses. A folder's display name is simply its own OS name, used verbatim.

<p align="center"><img src="images/category-ontology/category.png" alt="Category hierarchy"></p>

These categories vary in scope from broad groupings of information to narrower ones. In the social domain, for example, a category might be about "People", or more narrowly about "Immediate Family", and ultimately about just one family member. All predefined categories are *symmetric*. For example, "Extended Family" is symmetric because if Alice is a member of Bob's extended family, the reverse is also always true.

Mia includes two predefined `cat:Category` class hierarchies rooted in the `cat:Person` and `cat:Organization`. Some classes in this hierarchy have "starter" content pointed to via `cat:templateCell` and asserted directly in `category.ttl` alongside the class's own declaration, pointing at a `c:TCell` individual defined in the companion file `cell-templates.ttl` — the *cell template* for that class.

A category folder has no content of its own — its content lives entirely in the `c:ACell`(s) held by the cell-databook file(s) co-located in that same folder; `c:Cell` carries no property pointing back to a folder at all, since there's no folder individual to point at. When a category folder is created, Mia clones its class's `cat:templateCell`, if it exists, into a new `ACell`(DataBook file) for it — this is how a **cell template** becomes the starter content for an instantiated cell (see [Lazy Instantiation](#lazy-instantiation)).

The user is free to construct folders not included in the predefined categories. These, by the way, need not be symmetric, and simply carry no `c:origin` value on their cell. The user is also free to rearrange their folder tree as they wish, adding new folders and moving others around, within the Mia app or outside of it entirely as a filesystem operation.

### Category Properties

- **`cat:templateCell`** — links a `cat:Category` subclass directly to the `c:TCell` (template cell) individual serving as its reusable template content.

### Personal Categories

`cat:Person` categories organize a person's mostly non-employment-related information:

1. **People** (`cat:People`) — people in your social or professional life. Use this category for people not otherwise tied to a specific domain — a bookkeeper you know belongs under Finances (Advisory Firms), and your primary care physician belongs under Health & Wellness (Medical > Providers > Primary Care Physician), rather than here.
    - **Immediate Family** (`cat:ImmediateFamily`) — your closest living relatives, which generally include parents, siblings, spouses/partners, and children.
    - **Extended Family** (`cat:ExtendedFamily`) — relatives outside the immediate nuclear group, such as grandparents, aunts, uncles, cousins, nieces and nephews.
    - **In-Laws / Step-Family** (`cat:InLawsStepFamily`) — relatives gained through marriage or legal guardianship, including a spouse's parents and siblings, or children from a previous relationship.
    - **Others** (`cat:Others`) — people you know socially or professionally who are not part of your family — acquaintances, friends, neighbors, or other connections.
1. **Affiliations** (`cat:Affiliations`) — a catch-all for clubs, charities, faith groups, and other group affiliations that are not covered by a more specific category (e.g. `cat:SportsEntertainment`, `cat:Food`, etc.) 
1. **Health & Wellness** (`cat:HealthWellness`) — personal health and wellness information. Medical history, allergies, medications, vaccinations, prescriptions, eyeglasses.
    - **Medical** (`cat:Medical`) — medical (as opposed to dental or vision) care — diagnoses, treatments, providers, and insurance.
        - **History** (`cat:MedicalHistory`) — past diagnoses, conditions, surgeries, and treatments.
        - **Insurance** (`cat:MedicalInsurance`) — medical health insurance policies, providers, and coverage.
        - **Providers** (`cat:MedicalProviders`) — medical providers and practices you see for care.
            - **Primary Care Physician** (`cat:PrimaryCarePhysician`) — your primary care doctor, the physician you generally see first for checkups, referrals, and everyday health concerns.
            - **Medical Appointment Info** (`cat:MedicalAppointmentInfo`) — a medical appointment you're helping arrange on behalf of someone else.
    - **Dental** (`cat:Dental`) — dental care — diagnoses, treatments, providers, and insurance.
        - **History** (`cat:DentalHistory`) — past dental treatments, procedures, and conditions.
        - **Insurance** (`cat:DentalInsurance`) — dental insurance policies, providers, and coverage.
        - **Providers** (`cat:DentalProviders`) — dental providers and practices you see for care.
    - **Vision** (`cat:Vision`) — vision and eye care — diagnoses, treatments, providers, and insurance.
        - **History** (`cat:VisionHistory`) — past eye-care prescriptions, treatments, and conditions.
        - **Insurance** (`cat:VisionInsurance`) — vision insurance policies, providers, and coverage.
        - **Providers** (`cat:VisionProviders`) — vision care providers and practices you see for care.
    - **Fitness** (`cat:Fitness`) — general fitness and preventive physical health — exercise, gyms, trainers, and other non-clinical wellbeing information.
        - **Providers** (`cat:FitnessProviders`) — fitness providers and practices you see for care, e.g. gyms, trainers, and coaches.
    - **Nutrition** (`cat:Nutrition`) — nutritionists and dietitians.
        - **History** (`cat:NutritionHistory`) — past nutritional consultations, diet plans, and dietary conditions.
        - **Providers** (`cat:NutritionProviders`) — nutritionists and dietitians you see for care.
    - **Mental Health** (`cat:MentalHealth`) — mental and behavioral health care.
        - **History** (`cat:MentalHealthHistory`) — past diagnoses, treatments, and mental health conditions.
        - **Insurance** (`cat:MentalHealthInsurance`) — mental health insurance policies, providers, and coverage.
        - **Providers** (`cat:MentalHealthProviders`) — mental health providers and practices you see for care, e.g. therapists, counselors, and psychiatrists.
    - **Physical Therapy** (`cat:PhysicalTherapy`) — physical therapy and rehabilitative care.
        - **History** (`cat:PhysicalTherapyHistory`) — past physical therapy treatments, injuries, and rehabilitation plans.
        - **Providers** (`cat:PhysicalTherapyProviders`) — physical therapy providers and practices you see for care.
1. **Finances** (`cat:Finances`) — information about personal finances, bookkeeping, budgets, payment cards, bank accounts, brokerage accounts, insurance policies, financial advisors, etc.
    - **Bookkeeping** (`cat:Bookkeeping`) — budgeting, expense tracking, income, debts, IOUs, and savings goals.
    - **Banking & Payments Firms** (`cat:BankingPayments`) — firms that help you store, access, and move your cash for daily living. These include Retail Banks & Credit Unions, which provide checking accounts, savings accounts, and debit cards. These also include Payment Processors like Visa, Mastercard, or PayPal that let you buy things online and in stores, and Remittance Firms like Western Union or Wise used to send money to family or friends, especially overseas.
    - **Investment Firms** (`cat:Investing`) — firms that help you buy assets, so your money can grow over time for goals like buying a house or retiring. These include Brokerage Firms like Charles Schwab or Robinhood where you buy and sell stocks, bonds, and ETFs; Robo-Advisors, computer-run investing platforms like Betterment or Wealthfront that manage your portfolio for a low fee; and Mutual Fund companies like Vanguard or Fidelity that pool your money with other investors to buy a large bundle of stocks.
    - **Lending & Credit Firms** (`cat:LendingCredit`) — firms that lend you money when you need to buy something expensive that you cannot pay for all at once. These include Mortgage Lenders, banks or specialized companies that give you loans specifically to buy a home; Consumer Finance Companies, that give out personal loans, auto loans, or student loans; and Credit Card Issuers, banks that give you a plastic card to borrow money on the spot for daily purchases.
    - **Insurance Firms** (`cat:Insurance`) — firms that protect you and your family from financial ruin if something bad happens. These include Life & Health Insurance firms that cover medical bills or provide money to your family if you pass away, and Property & Casualty Insurance firms that insure your car, home, or apartment against accidents and theft.
    - **Advisory Firms** (`cat:Advisory`) — firms and individuals who do not just hold your money, but tell you the best ways to use it. These include Financial Planners (Wealth Advisors), human experts who help you build a custom roadmap for taxes, retirement, and budgeting, and Estate Planners, specialized professionals who help you write wills and plan how to pass your money to your children. Also includes Accountants and Bookkeepers, who track your income and expenses and prepare your taxes.
1. **Pets** (`cat:Pets`) — care instructions, veterinarians, medicines, food providers.
1. **Home** (`cat:Home`) — owning or renting a home, apartment, or other dwelling. Leases, deeds, utility accounts, real estate brokers.
1. **Work** (`cat:Work`) — professional roles. Employment history, resume/CV.
1. **Ownership** (`cat:Ownership`) — owned assets, property, vehicles, and other possessions.
    - **Vehicles** (`cat:Vehicles`) — related to owning and maintaining a vehicle. Vehicle insurance, repairs, mechanics, garages. 
1. **Travel** (`cat:Travel`) — travel plans, trips, and related information. Loyalty programs, airlines, bus lines, trains.
1. **Food** (`cat:Food`) — food preferences, dietary restrictions, favorite restaurants, recipes, shopping lists, and other food-related interests
1. **Sports & Entertainment** (`cat:SportsEntertainment`) — sports events (watching or participating) and entertainment (movies, plays, jazz clubs). Favorite teams/groups, venues, streaming services, ticketing. See `cat:Interests` for other interests.
1. **Education** (`cat:Education`) — educational history and ongoing learning — schools, degrees, certifications, transcripts, and enrolled courses.
1. **Interests** (`cat:Interests`) — things that interest, delight, and inspire — e.g. drawing, painting, dancing, religion, gaming, music. See `cat:SportsEntertainment` for sports and entertainment, and `cat:Affiliations` for formal memberships tied to a hobby or interest.
1. **Legal** (`cat:Legal`) — legal matters, contracts, agreements, trusts, wills, and professional legal relationships. Includes durable power of attorney and healthcare proxy agreements.
1. **Projects** (`cat:Projects`) — involvement in a specific project or initiative.
1. **Events** (`cat:Events`) — participation in or relationship to a specific event or gathering.
1. **Information** (`cat:Information`) — general knowledge selected by you, web links, documents, images.
1. **Government** (`cat:Government`) — government-issued credentials, tax records, and civic relationships.
    - **Federal** (`cat:Federal`) — federal government topic (e.g. passport, federal tax records).
        - **SSN** (`cat:SSN`) — social security number issued by the federal Social Security Administration.
        - **Passport** (`cat:Passport`) — passport issued by the Department of State.
    - **State** (`cat:State`) — state government topic (e.g. driver's license, state tax records).
        - **Birth Certificate** (`cat:BirthCertificate`) — a birth certificate issued by a state agency that issues and holds these records.
        - **Drivers License** (`cat:DriversLicense`) — a driver's license issued by a state agency that issues and holds these records.
    - **Municipality** (`cat:Municipality`) — municipal government topic (e.g. local permits, library card).
        - **Residence** (`cat:Residence`) — a place a person has lived, current or past.
1. **Companies** (`cat:Companies`) — a catch-all for your relationships with companies and organizations that provide services and/or products to you that are not included in more specific categories such `Cat:Finances`, `cat:HealthWellness`, `cat:Home`, `cat:Food`, etc.

### Organizational Categories

`cat:Organization` categories organize a person's professional and organizational-role information:

1. **Customers** (`cat:Customers`) — customer organizations. Rename to "Clients", etc.
1. **Marketing** (`cat:Marketing`) — marketing activities, campaigns, and related organizations.
    - **Prospects** (`cat:Prospects`) — customer prospects. Rename to "Client prospects", etc.
1. **Partners** (`cat:Partners`) — firms that provide goods and services.
1. **People (org)** (`cat:People(org)`) — people the organization interacts with in a working capacity.
    - **Employees** (`cat:Employees`) — related to employees.
        - **Employee** (`cat:Employee`) — detailed information about a specific employee.
    - **Consultants (org)** (`cat:Consultants(org)`) — engaged consultants.
    - **Other (org)** (`cat:Other(org)`) — people associated with the organization who don't fit Employees, Consultants, or Colleagues.
    - **Colleagues** (`cat:Colleagues`) — coworkers and peers within the organization not tracked as formal Employee records.
    - **Advisors (org)** (`cat:Advisors(org)`) — individuals who advise the organization in a non-employee capacity.
    - **Board of Directors (org)** (`cat:BoardOfDirectors(org)`) — the organization's board members.
1. **KB** (`cat:KB`) — corporate knowledge bases.
1. **Projects (org)** (`cat:Projects(org)`) — projects related to R&D, manufacturing, sales, marketing, operations, HR, etc.
1. **Meetings (org)** (`cat:Meetings(org)`) — face-to-face or online meetings, whether internal or with clients/customers. See also Events (org) for external, travel-to or larger-scale gatherings.
1. **Events (org)** (`cat:Events(org)`) — external events that people travel to, or larger-scale gatherings — conferences, webinars, town halls, and similar events. See also Meetings (org) for ordinary internal or client/customer meetings.
    - **Conferences** (`cat:Conferences`) — a conference or professional gathering.
1. **Suppliers** (`cat:Suppliers`) — companies that supply goods or services to this organization.
1. **Legal (org)** (`cat:Legal(org)`) — contracts and agreements.
1. **Government (org)** (`cat:Government(org)`) — interactions with government organizations.
1. **Finances (org)** (`cat:Finances(org)`) — corporate finance-related matters.
    - **Banking & Payments (org)** (`cat:BankingPayments(org)`) — firms that help organizations store, access, and move their cash. These include Retail Banks & Credit Unions, which provide checking accounts, savings accounts, and debit cards. These also include Payment Processors like Visa, Mastercard, or PayPal.
    - **Investing (org)** (`cat:Investing(org)`) — These include Investment firms, Private Equity firms, Venture Capitalists, Brokerage Firms like Charles Schwab and Mutual Fund companies like Vanguard or Fidelity.
    - **Lending & Credit (org)** (`cat:LendingCredit(org)`) — banks or specialized companies that give loans for specific purposes and Credit Card Issuers that give employees a card for travel and related expenses.
    - **Insurance (org)** (`cat:Insurance(org)`) — firms that protect organizations from risks. 
    - **Advisory (org)** (`cat:Advisory(org)`) — Financial Planners, outsourced CFO consultants, Accountants and Bookkeepers and Tax preparers.

### Category Folders

A folder qualifies as a **category folder** exactly when it holds one **cell DataBook** (see [Three Examples of Category Folders](#three-examples-of-category-folders) below) directly inside it, whose filename's `<local>` segment is an exact copy of the folder's own name. That single file both marks the folder as a *category* folder. A folder without a matching cell-databook is simply a plain filesystem folder, not a *category* folder — even if it contains nested category folders of its own. A category folder can never hold more than one cell because a `c:Cell` is, by definition, self-contained, and letting two cells share a folder would risk a single file in that folder becoming ambiguously part of both.

A category folder may be *user-defined* or *category-defined*. They can be distinguished purely by whether the folder's own cell-databook carries a `c:origin` value. User-defined category folders do not have an `c:origin` value. Category-defined category folders assert this value in `mia.origin` in its cell-databook's own YAML frontmatter. The value records the `cat:Category` subclass the cell was originally instantiated from. This value is fixed at that point, not re-derived from the folder's current name — a folder can be freely renamed or moved without needing to update it. 

#### Examples of Category Folders

In the center of the diagram below is a three level snippet of the user's category folders. 

<p align="center"><img src="images/folder-mapping.png" alt="Cells, categories, and topics"></p>

- Each folder may hold arbitrary files, and may also contain additional subfolders (to any depth) that are not part of the canonical category tree. These are all part of the cell content that is shared when the folder's cell is shared.
- One special file, acts as a note about the folder itself. These so-called *folder note* are stored as a file named `X.md` inside the `X` folder. Using the same name as the folder matches the convention used by PKM (Personal Knowledge Management) tools such as Obsidian (using the Folder Notes plugin), Logseq, Foam and others.
- Another special file, is the category folder's associated **cell DataBook** (a `.databook.md` file with `type: cell-databook`) — see [Category Folders](#category-folders) above for why a folder can never hold more than one. A cell DataBook's `id` matches its containing folder's own name verbatim, with each space replaced by a hyphen (spaces are illegal inside a raw Turtle IRI).

### Category Ontology File

**`category.ttl`** — The Category ontology, defining:
  - *Classes*: `cat:Category` (abstract; formerly `c:Cell`), `cat:Person`, `cat:Organization`, and all leaf category subclasses (the classificatory hierarchy — the only hierarchy this file defines; category.ttl 1.31.0 deleted the tree-position facet, `cat:Folder` and its subclasses `cat:CategoryDefined`/`cat:UserDefined`, outright, since a folder's tree position is now purely a filesystem fact).
  - *Annotation properties*: `cat:templateCell` (domain `owl:Class`, range `c:TCell` — links a `cat:Category` subclass directly to its reusable template cell; narrowed from `c:Cell` in category.ttl 1.18.0, once cell.ttl 3.7.0 split `c:Cell` into the `c:TCell`/`c:ACell` facets; see [cell-templates.ttl](#persona-ontology-files)).
  This is now `category.ttl`'s only property. `category.ttl` imports `cell.ttl` (to reuse `c:abstract` to mark non-instantiated classes, and by name in `c:origin`'s doc comments) and `cell-templates.ttl` (for the `ctpl:*TemplateCell` individuals its own `cat:templateCell` assertions point at). This import is one-directional only: `cell-templates.ttl` imports `cell.ttl` directly rather than importing `category.ttl` back, since the only `cat:` term it ever used, `cat:templateShape`, moved to `cell.ttl` as `c:templateShape` (its domain/range — `c:Cell`/`sh:NodeShape` at the time, narrowed to `c:TCell`/`sh:NodeShape` in cell.ttl 3.7.0's facet split — never actually referenced a `cat:` term) — so there is no mutual import here, unlike `topic.ttl`/`cell.ttl`.

#### Lazy Instantiation

Empty file system folders for most `cat:Category` subclasses are not pre-created ahead of time. A folder is not created until the user wishes to create a cell that needs that folder to hold it. When a folder matching a templated class (one carrying a `cat:templateCell` value) is first given content, Mia clones that class's `c:TCell` template into a new cell for that folder: whatever `c:templateShape` value the template carried is copied into the new cell's `c:shape`, and the clone is given real member-classified content — typed with a concrete `c:ACell` subclass (e.g. `c:OneMember`) — rather than staying purely a template. 

## Cell Ontology

The cell ontology defines the concept of a cell (`c:Cell`) — a self-contained unit of information that can be kept private or shared with others.

The Cell class has two facets: `c:TCell`, the *template* facet, and `c:ACell`, the *actual* (instantiated) facet. A cell always carries the `c:ACell` facet once it has real content; `c:TCell` is added on top of that when the cell also serves as a reusable template — a bare `c:TCell` with no `c:ACell` doesn't occur in practice.

### Cell

A cell is a private, secure collaboration space created and managed by the Mia software application. It is a self-contained unit of content that can be shared with one or more other members. These other members are usually other users, but may also be groups or organizations that are compatible with the Personal Data Network.

<p align="center"><img src="images/cell-ontology/cell.png" alt="Cell hierarchy"></p>

#### Cell Properties

- **`c:origin`** — The `cat:Category` subclass this cell was originally instantiated as, else nil. For one of the four templated classes (`cat:Passport`, `cat:BirthCertificate`, `cat:DriversLicense`, `cat:MedicalAppointmentInfo`), this is literally the class whose `c:TCell` template was cloned into this cell via [Lazy Instantiation](#lazy-instantiation); for any other cell, it's simply the category the cell was created to represent, asserted directly with no template involved. Either way the value is fixed at that point — it is not re-derived from the folder's current name, so it needs no update if the folder is later renamed or moved elsewhere in the tree. When a cell is shared with another member, the recipient's app can look at this value (if not nil) and use it as a hint as to which folder in the recipient's own tree it should be filed under. Domain `c:Cell`, range `cat:Category` (referenced by name, no `owl:imports`), at most one value (0..1) — see [Cell Ontology File](#cell-ontology-file) below.

- **`c:chat`** — optional path to chat stream. Aspirational: shown in `images/cell-ontology/cell.png`'s diagram and described here for intended semantics, but not yet defined as an actual property in `cell.ttl` (see `CLAUDE.md`'s Check 12 for this open discrepancy).

### TCell (Template Cell)

A cell pointed to by a `cat:Category` subclass (via `cat:templateCell`) serves as a **cell template** — a reusable, typically empty shape that the application clones into a new cell whenever a category of that class is first instantiated into a user's tree (see [Lazy Instantiation](#lazy-instantiation)). Such a cell is typed `c:TCell`, the template facet. An ordinary, already-instantiated cell is typed `c:ACell`, the actual facet, instead — carrying real member composition, creator, and content. A cell template is simultaneously both: it is reusable template content (`c:TCell`) that also carries real member-classified content of its own (`c:ACell`, via `c:OneMember`/`c:TwoMember`/`c:ThreePlusMember`) — see [Cell Ontology File](#cell-ontology-file) below.

#### Properties

If a `c:TCell` has a `c:templateShape` value, then when the category pointing to it is instantiated (see [Lazy Instantiation](#lazy-instantiation)), whatever value this property has is copied into the new `c:ACell`'s `c:shape`.

- **`c:templateShape`** — links a `c:TCell` individual directly to the `sh:NodeShape`(s) describing the content expected of a topic filed under its category — e.g. `ctpl:PassportTemplateCell` carries `pshapes:PassportDocumentShape`. An `owl:ObjectProperty`, domain `c:TCell`, range `sh:NodeShape`. Makes the shape reachable by pure RDF traversal (`cat:Category` → `cat:templateCell` → `c:templateShape` → `sh:NodeShape`), not just by file co-location or naming convention. 

### ACell (Asserted Cell)

A `c:ACell` is the instantiated facet of an abstract `c:Cell`. It carries `c:memberCount`, `c:creator`, `c:subject`, `c:memberTopics`, `c:otherTopics`, and `c:shape`. A cell isn't typed `c:ACell` until it has real content (`c:memberCount` set) — a pure tree-position placeholder with nothing filed under it yet stays a bare `c:Cell`, exempt from requiring `c:subject`/`c:memberTopics`.

A cell needing both facets at once — e.g. every individual in `cell-templates.ttl`, which is both reusable template content and real member-classified content — is simply multi-typed with both `c:TCell` and its `c:ACell`-lineage class (e.g. `c:OneMember`).

#### Properties

- **`c:subject`** — either exactly one or two values (`xsd:anyURI`s) are required. The subject indicates what this cell is about. Its values are the values of the `t:subject` properties of one or two of the topic graphs (`t:SCTopicGraph`s) pointed to by the cell's `c:memberTopics` or `c:otherTopics` links.

- **`c:memberTopics`** — one or more values, required; It is a link to the required baseline of subject-claimant topic graphs (`t:SCTopicGraph`) that hold the structured content of the cell related to the members with which the cell has been shared. Its cardinality varies by member count — see [Cell Members](#cell-members). Each SCTopicGraph has a *subject* and a *claimant*. The subject is typically a person, organization, or group, but it could be any other entity the Persona ontology can describe. The claimant is the person, group or organization that is asserting the values of the claims in the container. See [Topic Ontology](#topic-ontology) for details.

- **`c:otherTopics`** — optional, unbounded (0..N), uniformly regardless of member count. Link to any number of additional subject-claimant topic graphs beyond those referenced by `c:memberTopics`.

- **`c:shape`** — a `owl:ObjectProperty`, domain `c:ACell`, range `sh:NodeShape`. Optional; most actual cells carry no `c:shape` value. Links a `c:ACell` individual directly to the `sh:NodeShape`(s) validating that specific cell's own content, as opposed to `c:templateShape`, which describes what a topic filed under some other, template category should look like. Populated by copy-on-clone: when Lazy Instantiation clones a `c:TCell` into a new `c:ACell` — whatever `c:templateShape` value the `TCell` carried is copied into the clone's `c:shape` with the same validation expectation.

- **`c:creator`** — optional, at most one value. Identifies who created this cell's content: a single `p:Person`, `g:Group`, or `o:Organization`. 

- **`c:memberCount`** — the concrete `c:ACell` subtype this DataBook instantiates: `c:OneMember`, `c:TwoMember`, or `c:ThreePlusMember`. Value is the class itself (e.g. `mia.memberCount: "c:OneMember"`). See [Cell Members](#cell-members) above.

#### Cell Members

Every `c:ACell` has a `c:memberCount`, which is a tally of the number of members of the cell. There are three concrete types: `c:OneMember` (a cell created by the user and not shared with any other member), `c:TwoMember` (the user plus exactly one other member), and `c:ThreePlusMember` (the user plus two or more other members).

Every `c:ACell` carries either one or two `c:subject` values (the resource(s) or "content" the cell is primarily about), one or more `c:memberTopics` links (the required baseline of topic containers backing its content, one or more per member), and any number of `c:otherTopics` links (additional topics beyond that baseline), regardless of member count. The cardinality of each is shown in the table below:

| Property         | OneMember | TwoMember | ThreePlusMember |
|------------------|-----------|-----------|-----------------|
| `c:subject`      | 1         | 1..2      | 1               |
| `c:memberTopics` | 1         | 2..4      | 3..N            |
| `c:otherTopics`  | 0..N      | 0..N      | 0..N            |

The `c:memberTopics` and `c:otherTopics` are lists of `t:TopicGraphs`. See the [Topic Ontology](#topic-ontology) for details.

### Cells within Category folders

The diagram below shows a few representative category folders, each holding a cell. 

<p align="center"><img src="images/cat-cell-topic.png" alt="Cells, categories, and topics"></p>

The blue text in the upper left of the cell displays the 1-2 subject(s) of the cell. If a `c:TwoMember` cell has a single subject this subject must be the subject of a topic graph in the `c:otherTopics`. And if `c:TwoMember` cell has two subjects they must be two distinct subjects of the 2..4 topic graphs pointed to by `c:memberTopics`. A TwoMember cell with two subjects is essentially about the connection/relationship between the two members.

Within each cell, topic graphs shown as circles. White circles are topic graphs whose triples are claimed by the self (the user). Green circles are topic graphs whose triples are claimed by a person other than the self, by an organization (`o:Organization`), or by a group (`g:Group`), and synchronized with the user's Mia instance over the PDN. For example the BHS cell at the bottom has three topics: Self (the user)'s BHS profile, the BHS group's own profile and Bob Johnson's BHS member profile as claimed by Bob.

A class's template cell (`cell-templates.ttl`) may also carry validation metadata declared in the paired `cell-templates-shacl.ttl`. This metadata lives on the class-level template only.

#### Properties

The following properties are defined in `cell.ttl` and represented as `mia.` YAML fields in cell DataBooks:

| YAML field | Ontology property | Cardinality | Meaning |
|------------|-------------------|-------------|---------|
| `mia.origin` | `c:origin` | 0..1 | The `cat:Category` subclass this cell was originally instantiated as, as a class value (e.g. `"cat:Others"`); absent otherwise. Fixed at creation, not re-derived from the folder's current name. A hint for a recipient's app when this cell is shared over PDN |
| `mia.memberCount` | `c:memberCount` | 1 | The concrete `c:ACell` subclass this DataBook instantiates, as a class value (e.g. `"c:OneMember"`) |
| `mia.creator` | `c:creator` | 0..1 | Who created this cell's content — a `p:Person`, `g:Group`, or `o:Organization` |
| `mia.subject` | `c:subject` | 1..2 | The resource(s) (e.g. `:Self`, `:Bob_Johnson`) the cell's content is about |
| `mia.shape` | `c:shape` | 0..1 | Optional `sh:NodeShape` validating this specific cell's own content directly |

#### Subject and Topic Link Properties

Each cell DataBook carries one or two `c:subject` values identifying who or what the cell is about, plus one or more `c:memberTopics` links (the required per-member baseline) and any number of `c:otherTopics` links (additional topics beyond that baseline) to the actual topic DataBook container(s) backing its content:

| Property | Value | Cardinality | Applies to | Meaning |
|----------|-------|-------------|------------|---------|
| `c:subject` | `xsd:anyURI` | 1 on `OneMember`/`ThreePlusMember`; 1..2 on `TwoMember` (required) | Any `c:ACell` | The resource(s) (typically a `p:Person`/`g:Group`/`o:Organization`) the cell's relationship is about — not a topic container |
| `c:memberTopics` | `t:SCTopicGraph` | 1 on `OneMember`; 2..4 on `TwoMember`; 3..N on `ThreePlusMember` (required) | Any `c:ACell` | The required baseline of self-vs-other classified topics backing this cell's content — at least one per member in the relationship (up to all four self-vs-other combinations for `TwoMember`) — distinguished by each linked topic's own `subject`/`claimant` combination rather than by separate properties or classes |
| `c:otherTopics` | `t:SCTopicGraph` | 0..N (optional), uniformly regardless of member count | Any `c:ACell` | Any number of additional topics beyond the `c:memberTopics` baseline — e.g. extra notes or supplementary claims not tied to a specific self-vs-other combination |

`c:subject`, `c:memberTopics`, and `c:otherTopics`'s domain is the broader `c:ACell` rather than `c:MultiMember`, unlike the four properties `c:topics` (via its predecessor `c:secondary`) replaced (`c:sbs`/`c:obs`/`c:sbo`/`c:obo`) — a `OneMember` cell can hold a self-by-self topic through `c:memberTopics`, not just a `TwoMember`/`ThreePlusMember` cell. `c:memberTopics`'s and `c:subject`'s per-member-count cardinality *is* enforced by `cell-shacl.ttl`, via three shapes targeting `cell:OneMember`/`cell:TwoMember`/`cell:ThreePlusMember` directly (`:OneMemberShape`, `:TwoMemberShape`, `:ThreePlusMemberShape`) — this replaced the single `c:topics` property's old blanket "at least one, no upper bound" rule, which didn't vary by member count. `c:otherTopics` stays uniform and unbounded across all member counts, enforced only by the general `:ACellShape` (each value must be a `t:SCTopicGraph`, no cardinality restriction).

### Cell Ontology File

**`cell.ttl`** — The Cell ontology, defining:
  - *Classes*: `c:Cell` (formerly `c:Parties`), splitting into two orthogonal facets, `c:TCell` (abstract, template facet) and `c:ACell` (abstract, actual/instantiated facet); `c:OneMember`, `c:MultiMember` (abstract), `c:TwoMember`, `c:ThreePlusMember` — all now subclasses of `c:ACell` rather than `c:Cell` directly (cell.ttl 3.7.0).
  - *Annotation properties*: `c:label` (default display name for a concrete `c:Cell` subtype, asserted on the class), `c:abstract` (marks a class as not directly instantiated in DataBooks), `c:subject` (domain `c:ACell`; range `xsd:anyURI` — one or two resource IRIs identifying who or what the cell is about; not an object property since its range is a datatype, mirroring `topic:subject`'s identical pattern).
  - *Object properties*: `c:origin` (domain `c:Cell`, range `cat:Category` — added cell.ttl 3.20.0; the `cat:Category` subclass this cell was originally instantiated as, else nil; fixed at creation, not re-derived from the folder's current name; at most one value); `c:templateShape` (domain `c:TCell`); `c:memberCount`/`c:creator`/`c:memberTopics`/`c:otherTopics`/`c:shape` (domain `c:ACell` — a cell isn't typed `c:ACell`, and so carries none of these, until it has real content). `c:creator`'s range is a union of `p:Person`, `g:Group`, and `o:Organization` — the same union-range pattern used by `topic:claimant` (see [Topic Ontology File](#topic-ontology-file)). `c:memberCount`'s range is `c:ACell` itself: its value is the concrete subclass (`c:OneMember`/`c:TwoMember`/`c:ThreePlusMember`), not a string — class-value punning; `c:origin`'s range `cat:Category` uses this same punning — its value is the concrete leaf subclass (e.g. `cat:Others`), not a string. `c:templateShape`'s and `c:shape`'s ranges are both `sh:NodeShape` — see [Cell Ontology](#cell-ontology) above — but on different domains: `templateShape` describes what a topic filed under a *template* category should look like, while `shape` validates an *actual* cell's own content directly. `c:memberTopics`/`c:otherTopics`'s range is `t:SCTopicGraph` — the former is the required per-member baseline (split from the single `c:topics` property, cell.ttl 3.14.0), the latter any number of additional topics beyond it. `c:Cell` carries no property pointing back to a folder at all — a folder is now purely a filesystem concept with no RDF individual to point at (category.ttl 1.31.0 deleted `cat:Folder` and its subclasses outright); `c:origin`'s range is the classificatory `cat:Category`, not a tree position — it records what kind of thing a cell is, not where it lives, letting a recipient's app use it as a filing hint when a cell is shared over PDN.
  These terms are referenced by name in the YAML frontmatter of each cell DataBook file. `cell.ttl` imports `topic.ttl` (for `c:memberTopics`/`c:otherTopics`'s range, `t:SCTopicGraph`); `topic.ttl` in turn imports `cell.ttl` back, solely to reuse `c:abstract` — a mutual import. `category.ttl` also imports `cell.ttl` (to reuse `c:abstract`, and by name in `c:origin`'s doc comments), but `cell.ttl` does not import `category.ttl` back — `c:origin`'s range `cat:Category` is referenced by name only, exactly like `cell.ttl` already does for `p:Person`/`g:Group`/`o:Organization` in `c:creator`'s range, without importing `persona.ttl`, `group.ttl`, or `organization.ttl` — the same choice `topic.ttl` makes for `topic:claimant`.

**`cell-shacl.ttl`** — SHACL shapes for cell DataBook instances, split across shapes matching `cell.ttl`'s facet split: `:CellShape` (target `c:Cell`) constrains `c:origin` to at most one value (0..1, added cell-shacl.ttl 3.15.0 — not constrained via `sh:class cat:Category`, since a legal value is the concrete leaf subclass itself, never `rdf:type cat:Category`, mirroring `c:memberCount`'s own identical unconstrained, class-value-punning treatment above; its earlier `c:folder` cardinality constraint was removed outright in cell-shacl.ttl 3.17.0, once `c:folder` itself was removed from `cell.ttl`); `:TCellShape` (target `c:TCell`) constrains `c:templateShape` to at most one value; `:ACellShape` (target `c:ACell`) constrains `c:creator` to at most one value which, if present, must be a `p:Person`, `g:Group`, or `o:Organization`, `c:memberCount` to exactly one value which must be the class `c:OneMember`, `c:TwoMember`, or `c:ThreePlusMember`, `c:subject` values to each be an IRI (`sh:nodeKind sh:IRI`, not `sh:class`, since its range is `xsd:anyURI` not `t:SCTopicGraph`), `c:otherTopics` values (if any) to each be a `t:SCTopicGraph`, and `c:shape` to at most one value. Cardinality for `c:subject` and `c:memberTopics` is no longer enforced uniformly on `:ACellShape` — instead three new shapes, `:OneMemberShape`/`:TwoMemberShape`/`:ThreePlusMemberShape` (targeting `c:OneMember`/`c:TwoMember`/`c:ThreePlusMember` directly, since `yaml-to-rdf.py` types every cell individual with its concrete member class), enforce `c:subject` as exactly 1/1..2/exactly 1 and `c:memberTopics` as exactly 1/2..4/at least 3 respectively — replacing the single `c:topics` property's old blanket "at least one, no upper bound" rule, which didn't vary by member count. `c:templateShape`/`c:shape` are deliberately not constrained to `sh:class sh:NodeShape`: the individuals they point at are only typed `sh:NodeShape` in `cell-templates-shacl.ttl`, which Tier 1 validation deliberately excludes from its merged-data run (see [Validation](EXAMPLE.md#validation)), so that constraint would spuriously fail there.

### Cell Ontology Validation

Cell DataBook instances are validated by `cell-shacl.ttl`: `origin`/`memberCount`/`subject`/`memberTopics`/`otherTopics`/`creator`/`shape` exist solely as `mia.` YAML frontmatter fields on cell DataBooks, so `yaml-to-rdf.py` synthesizes the corresponding `c:` triples (`rdf:type c:Cell`, `c:origin` if present, plus `rdf:type c:ACell`/the concrete member class/`c:memberCount`/`c:creator`/`c:subject`/`c:memberTopics`/`c:otherTopics`/`c:shape` once `memberCount` is set) directly from frontmatter, letting `:CellShape`/`:ACellShape`/the per-member-count shapes actually fire against real instance data — see [Tier 1](EXAMPLE.md#validation). `c:origin` is asserted on every `c:Cell` regardless of facet, including a bare placeholder with no real content yet, since its domain is `c:Cell` itself, not `c:ACell`. A cell-databook with no `mia.memberCount` value (a pure tree-position placeholder with nothing filed under it yet) is synthesized as a bare `c:Cell` only, so it is not subject to `:ACellShape`'s or the per-member shapes' required `c:subject`/`c:memberTopics`. (`c:TCell` individuals live only in `cell-templates.ttl`, a plain `.ttl` file rather than a DataBook excluded from Tier 1's merge entirely — see [Validation](EXAMPLE.md#validation) — so they need no such synthesis either.)

## Topic Ontology

The topic ontology defines *topics* (`t:TopicGraph`) — named graphs containing sets of claims about some resource; that resource need not be a person (see `t:subject` below). Topics are referenced by cells described in the Cell Ontology.

### Topics

A topic is a container of information related to an interaction with, or relationship to, another person, group, or organization. This information is expressed as a named graph of triples — typically using the Persona, Organization, and Group ontologies when the topic is about a person, group, or organization, though the ontology does not require this — and stored in a **[DataBook](https://github.com/w3c-cg/holon/tree/main/architectures/databook)** (`.databook.md`) file that describes one facet of its subject (called the `subject` of the topic). These claims may have originated from other topics about the same subject. 

<p align="center"><img src="images/topic-ontology/topic.png" alt="topic ontology"></p>

One property applies to every `t:TopicGraph`:

**`t:template`** — present only on topics that contain instances of a template; its value is the name of a `p:PersonaTemplate` subclass (e.g. `"persona:BirthCertificateDocument"`, `"persona:JSContactCard"`, `"persona:DriversLicenseDocument"`, `"persona:PassportDocument"`, `"persona:MedicalAppointmentRecord"`).

A topic carries no field pointing back at the cell that references it — that link is asserted only on the cell side, via `c:memberTopics`/`c:otherTopics` (see the Cell Ontology section below).

Two more properties apply to every topic linked from a cell, since every `c:memberTopics`/`c:otherTopics` value is classified as `t:SCTopicGraph`:

**`t:subject`** — The resource the topic is about. Value is any resource IRI — the ontology does not require it to be a `p:Person`, `g:Group`, or `o:Organization`, though in this example every `subject` value happens to be one of those three:
- `:Self` — the topic is about the Mia user.
- a named individual of `p:Person` — the topic is about another human Mia user.
- a named individual of `g:Group` — the topic is about a group of Mia users.
- a named individual of `o:Organization` — the topic is about an organization (legal corporation or government agency).

**`t:claimant`** — Who is making the claim. Values are local IRIs of `p:Person`, `g:Group`, or `o:Organization` individuals:
- `:Self` — the Mia user that is entering the data, even if the underlying information originates from some other party such as a company, government agency, or another person.
- a named individual of class `p:Person` — another Mia user is claiming the data directly.
- a named individual of class `g:Group` — a group of Mia users is claiming the data.
- a named individual of class `o:Organization` — an organization is claiming the data.

The diagram below shows four kinds of topics related to a hypothetical Mia user, Alice, and her interactions with a Department of Motor Vehicles (DMV) agency. Across the top are two topics where the DMV itself is the subject, and at the bottom where Alice is the subject. At the left are topics where Alice has made the claims (e.g. Alice's Mia has written the claims into the topic) and at the right are topics where the DMV as the "other" has written the claims. 

<p align="center"><img src="images/topic-ontology/quadrants.png" alt="a quadrant of topic types"></p>

The lower left shows a topic that Alice might share with other people or companies. In it, she claims that her driver's license number is S43228943, having copied that number from her physical driver's license. The topic in the lower right carries the same information as the lower left, but because it is being claimed by the DMV it is more likely to be trusted by a recipient (especially if this information is conveyed via secure channel and the claims are cryptographically bound to the identity of the DMV).

### Topic DataBooks

A topic's own metadata is carried as an entry in its owning cell-databook's `mia.topics` list (see [Cell DataBooks](#cell-databooks) above), rather than in a separate DataBook file's YAML frontmatter — each topic no longer has a file of its own. The topic ontology (`topic.ttl`) defines the controlled vocabularies that those per-entry fields reference:

- `mia.topics[].template` = `t:template`
- `mia.topics[].subject` = `t:subject`
- `mia.topics[].claimant` = `t:claimant`

### Topic Ontology File

**`topic.ttl`** — the Topic ontology, defines:
  - *Classes*: `t:TopicGraph`, `t:SCTopicGraph` (Subject-Claimant topic graph; the concrete class every self-vs-other classified topic DataBook is typed as directly — it has no subclasses; carries the `t:subject`/`t:claimant` annotations — every topic reachable from a cell, via `c:memberTopics`/`c:otherTopics`, is a `t:SCTopicGraph`).
  - *Annotation properties*: `t:template` (domain `t:TopicGraph`), `t:claimant` (range a union of `p:Person`, `g:Group`, `o:Organization`), `t:subject` (domain `t:SCTopicGraph`; range `xsd:anyURI` — any resource IRI, not necessarily a `p:Person`/`g:Group`/`o:Organization`).
  These terms are referenced by name in each topic's `mia.topics[]` entry, inside its owning cell-databook file. `topic.ttl` imports `cell.ttl` to reuse `c:abstract` on `t:TopicGraph`/`t:SCTopicGraph`.

**`topic-shacl.ttl`** — SHACL shapes for topic instances: `:SCTopicGraphShape` (target `t:SCTopicGraph`) constrains `t:claimant` to exactly one value, which must be a `p:Person`, `g:Group`, or `o:Organization`, and `t:subject` to exactly one value, which must be an IRI.

### Topic Ontology Validation

A topic's own metadata (claimant, subject) is declared in its `mia.topics[]` entry, not a separate DataBook's YAML frontmatter. `topic-shacl.ttl`'s `:SCTopicGraphShape` (see above) targets `topic:SCTopicGraph`, but that typing is itself only ever asserted via the `claimant`/`subject` fields of that entry, never as a literal `rdf:type topic:SCTopicGraph` triple in the topic's own extracted Turtle body. `yaml-to-rdf.py` synthesizes it directly from the owning cell-databook's frontmatter — `rdf:type topic:SCTopicGraph` plus `topic:claimant`/`topic:subject`, asserted on the topic's plain `id` (the `mia.topics[].id` value), not the `#graph`-suffixed `graph.named_graph` IRI (see `topic.ttl` 1.11.0) — so `:SCTopicGraphShape` actually fires against real instance data; see [Tier 1](EXAMPLE.md#validation). The remaining classification facts are synthesized the same way from the cell-databook's own frontmatter: `origin`/`memberCount`/`subject`/`memberTopics`/`otherTopics`/`creator`/`shape` (see [Cell Ontology Validation](#cell-ontology-validation)) — there is no separate folder-level synthesis any more, since a folder's tree position is purely a filesystem fact with no RDF individual of its own.

## Persona Ontology

The Persona ontology defines a formal, machine-readable model of a person. It is used by triples stored in `t:TopicGraph` instances. 

We represent a person with the `p:Person` class — a Mia-specific subclass of CCO `Person` (`cco:ont00001262`).  The Mia user's own `p:Person` individual always uses the IRI `:Self` across all of their topics; other people, groups, and organizations are assigned locally-minted named IRIs (e.g. `:Bob_Johnson`). `:Self`'s type declaration (`rdf:type owl:NamedIndividual, persona:Person`) is asserted in `example/topics/self.ttl` (see the [Validation](EXAMPLE.md#validation) section for how `self.ttl` is merged in alongside every embedded topic).

<p align="center"><img src="images/persona-ontology/persona.png" alt="Persona model"></p>

The persona ontology is used to describe the contents of **topic graphs** of **cells** (see [Cell Ontology](#cell-ontology) and [Topic Ontology](#topic-ontology)). These topic graphs, when describing people, function as *named-graph slices* — each is an independent facet of an identity in a specific cell context, carrying the claims relevant to that topic: names, addresses, phone numbers, SSNs, physical characteristics, parent-child relationships, social connections, payment cards, and more. The Persona ontology reuses existing well-known ontologies wherever possible and defines new terms only where no suitable existing term exists.

### Key Properties and Classes

This section describes the most fundamental properties and classes in the Persona ontology. A person's identity data is spread across multiple named-graph slices — each a topic embedded in some cell-databook — each containing one `p:Person` individual. The Mia user's slices share the IRI `:Self`; each other person's slices share their locally-assigned named IRI.

**Classes:**

- `p:Person` — a Mia-specific subclass of CCO `Person` (`cco:ont00001262`). Each topic (named-graph slice) contains exactly one `p:Person` individual. The Mia user's own `p:Person` always uses the IRI `:Self`, shared across all of their topics. Other people, groups, and organizations are assigned locally-minted named IRIs (e.g. `:Bob_Johnson`, `:Paula_Walker`). `:Self` is a local IRI and is never exposed externally over the PDN, so there are no collisions between Mia instances. All identity data — names, identifiers, addresses, social networks, payment cards, and more — attaches to this individual.

### Social Classes and Properties

This section describes classes and properties related to a person's social network.

**Classes:**

- `cco:ont00001183` — Social Network

**Properties:**

- `p:hasSocialNetwork` — a social network — other people known by the `p:Person` carrying the social network. The holder is not included as a member part of the social network object, but *is* considered to be a part of it by virtue of holding the network entity.
- `BFO_0000115` — has member part. Links to `p:Person` members of this network.

#### Named Graph Scoping and Topic-Specific Membership

A `BFO_0000115` (has member part) triple on a Social Network individual — for example, `:Alice_Family_Network BFO_0000115 :Paula_Walker` in a topic about Alice's immediate family — targets `:Paula_Walker` as a person entity, not as a topic-specific slice of her data. The named graph architecture provides the isolation: that triple lives inside its own topic's named graph, and when an application needs "Paula Walker's family topic data" it queries that topic's graph together with Paula's own family-topic graph, rather than the full merged dataset. (See topics #21 and #5 in the [Illustrative Example](EXAMPLE.md#illustrative-example-alice) for the concrete instance of this pattern.)

This is the correct design for three reasons:

- **BFO semantics**: changing the range of `BFO_0000115` to a DataBook document IRI (e.g. `<http://www.example.org/mia/topics/topic-07>`) would be a semantic error — the range of `has member part` must be a continuant (a person or group), not a document.
- **Model simplicity**: introducing topic-specific "view" individuals (e.g. `:Paula_Walker_Family`) would reintroduce the layered complexity that the removal of `p:Persona` was designed to eliminate.
- **Tooling maturity**: annotating the triple with RDF-star (`<< :Alice_Family_Network BFO_0000115 :Paula_Walker >> mia:inContext <...>`) is a valid future option, but is not yet supported by Protégé and remains non-standard.

The practical implication is that **Tier 1 validation** (which merges all graphs) correctly finds all reachability links across the full dataset, while **application queries** that display a social network's members should join against specific topic named graphs rather than the full triplestore merge.

### Possession-Related Classes and Properties

This section describes properties and classes related to things a person has, holds, possesses, purchased, or rents.

- Physical plastic/paper cards are `MaterialArtifact` subclasses that include driver's license, health insurance card, payment card, etc.
- Physical wallets — `p:hasPhysicalCard` records that a `p:Person` possesses a card, wallet-contained or not; BFO `continuant part of` separately records that a specific card is currently inside a specific `p:Wallet`. These are independent, complementary facts, not alternatives — a wallet-contained card carries both.

<p align="center"><img src="images/persona-ontology/persona-card.png" alt="Card possessions model"></p>

**Classes:**

- `p:PhysicalCard` — a physical plastic or paper card (held in a wallet or carried directly).
- `p:PhysicalHealthInsuranceCard` (subclass of `p:PhysicalCard`) — a physical health insurance membership card.
- `p:PhysicalDriversLicense` (subclass of `p:PhysicalCard`) — a state-issued driver's license card.
- `p:PhysicalPaymentCard` (subclass of `p:PhysicalCard`) — a physical credit or debit card.
- `p:PhysicalSocialSecurityCard` (subclass of `p:PhysicalCard`) — a paper or plastic card issued by the Social Security Administration.
- `p:Wallet` — a physical wallet that can hold cash as well as various kinds of paper or plastic identity or payment cards.

**Properties:**

- `is carrier of` (from BFO) — used to link a physical card to its corresponding `p:Person` in another topic.
- `p:hasWallet` — links a `p:Person` to a physical wallet (see Possessions below).
- `p:hasImageScan` — a link to a scanned image of this card.
- `p:hasPhysicalCard` — links a `p:Person` to a `p:PhysicalCard` they possess, whether carried directly or held inside a wallet (see Possessions below).

### Accounts

This section describes properties and classes related to a person's relationship with an online service provider. An online service account (`OnlineServiceAccount`, CCO `ont00000033`) records a person's credentials and identity with an online service provider such as Google or AT&T.

**Properties:**

- `holds user account` (CCO) — links a `p:Person` to an `OnlineServiceAccount`.
- `has service name` (CCO) — the name of the online service (e.g. "Google").
- `has service URI` (CCO) — the URI of the online service.
- `has user handle` (CCO) — the user's handle or username on the service.
- `p:hasPassword` — the password credential for an `OnlineServiceAccount` (Persona ontology extension).

### Finance-Related Classes and Properties

This section describes properties and classes related to a person's interactions with financial institutions.

**Classes:**

- `p:CheckingAccount` — a bank checking account held by a person, linked to a debit card.
- `p:CheckingAccountNumber` — an identifier designating a bank checking account, connected via `designated by` (`ont00001879`).
- `p:RoutingNumber` — an ABA routing transit number identifying the financial institution, connected via `designated by`.

**Properties:**

- `p:hasBankAccount` — links a `p:Person` to a `p:CheckingAccount` it records.
- `p:accessesBankAccount` — links a DebitCard to the `p:CheckingAccount` it draws funds from.

### Modeling Details

This section describes a few details related to modeling names and addresses.

**Peer name pattern**: All name types (FullName, GivenName, FamilyName, AlternateName) connect directly to a `p:Person` via `designated by` (`ont00001879`). They are siblings, not nested under a PersonName parent. Legal names belong to the birth certificate topic (annotated `t:template p:BirthCertificateDocument`); a preferred/goes-by name (AlternateName) belongs to each social or professional topic where it applies.

**Address history**: Each address topic carries a `p:Person` with a USPostalAddress and an `AddressDesignation` with a `TemporalInterval` (start date required; no end date = current address).

### Persona Templates

`p:PersonaTemplate` is an abstract classification class that serves as the common superclass for all reusable, topic-type-specific template labels. These labels are defined in `persona-templates.ttl`. A topic declares its template as the `template` field of its `mia.topics[]` entry (inside its owning cell-databook's frontmatter) rather than by typing its `p:Person` individual. Four of the five per-template SHACL shapes (`p:BirthCertificateDocument`, `p:DriversLicenseDocument`, `p:PassportDocument`, `p:MedicalAppointmentRecord`) live in `cell-templates-shacl.ttl`, each directly linked from its class-level `c:TCell` template (in `cell-templates.ttl`) via `c:templateShape` (`cell.ttl`) — so the shape is reachable by RDF traversal from the corresponding `cat:Category` class (`cat:BirthCertificate`, `cat:DriversLicense`, `cat:Passport`, `cat:MedicalAppointmentInfo`) via `cat:templateCell` — see [Lazy Instantiation](#lazy-instantiation); `p:JSContactCard`'s shape remains a standalone file in `shacl/`, since it's reused across many unrelated tree positions with no single `cat:Category` class of its own to attach to.

<p align="center"><img src="images/persona-ontology/persona-templates.png" alt="persona templates model"></p>

**Government-issued identity documents** — `p:BirthCertificateDocument`, `p:DriversLicenseDocument`, and `p:PassportDocument` are subclasses of both `p:PersonaTemplate` (template label use) and `p:IdentityDocument` (artifact instance use). `p:IdentityDocument` is the class for government-issued documents that formally identify a person. The property `p:hasIdentityDocument` (domain: `p:Person`, range: `p:IdentityDocument`) links a person to the government document they hold. Each government-ID topic declares one named individual of the document type and links it from `:Self`. `p:JSContactCard` is a format label only — not a government-issued document — and is a subclass of `p:PersonaTemplate` only.

The five currently defined subclasses of `p:PersonaTemplate` are:

- `p:BirthCertificateDocument` — label for topics that carry a person's legal birth name record as issued by a state agency. Also a subclass of `p:IdentityDocument`. Declared as `template: "persona:BirthCertificateDocument"` in the topic's `mia.topics[]` entry. SHACL shape `:BirthCertificateDocumentShape` (in `cell-templates-shacl.ttl`, alongside `cat:BirthCertificate`'s template cell in `cell-templates.ttl`) targets the `p:BirthCertificateDocument` document individual and validates the holding `p:Person` via `^persona:hasIdentityDocument`:
  - **Required**: either a `FullName` designator **or** both a `GivenName` and a `FamilyName` designator (via `designated by`, `ont00001879`) — expressed with `sh:or`.
  - **Optional**: `AdditionalName` (middle name), `AlternateName` (e.g. maiden name), `Nickname`, and `Legal Name` designators.

- `p:JSContactCard` — label for topics that carry professional contact details in the JSContact (RFC 9553) format. A digital contact format (RFC 9553) — not a government-issued identity document, and therefore not a subclass of `p:IdentityDocument`. Declared as `template: "persona:JSContactCard"` in the topic's `mia.topics[]` entry. SHACL shape `:JSContactCardPersonShape` (in `shacl/jscontactcard-shacl.ttl`) enforces:
  - **Required**: exactly one `OrganizationName` designator; at least one `Email` or `TelephoneNumber` designator.
  - **Optional**: all name components, `OrganizationUnit`, `JobTitle`, addresses, online services, anniversaries, personal info, photo.
  - **Max 1** on all single-valued name and organization components.
  See the [JSContact field coverage table](#jscontact-field-coverage) below for the complete mapping.

- `p:DriversLicenseDocument` — label for topics that carry the identity claims on a state-issued driver's license. Also a subclass of `p:IdentityDocument`. Declared as `template: "persona:DriversLicenseDocument"` in the topic's `mia.topics[]` entry. SHACL shape `:DriversLicenseDocumentShape` (in `cell-templates-shacl.ttl`, alongside `cat:DriversLicense`'s template cell in `cell-templates.ttl`) targets the `p:DriversLicenseDocument` document individual and validates the holding `p:Person` via `^persona:hasIdentityDocument`:
  - **Required**: `FullName` **or** (`GivenName` + `FamilyName`); exactly one `Birthdate` (`cco:ent00000046`); exactly one Drivers License Number (`cco:ent00000065`); exactly one expiration date (`cco:ent00000070` → Calendar Date Identifier `cco:ont00001340`).
  - **Optional**: `AdditionalName`; Issuing Jurisdiction (`cco:ent00000068`); `PostalAddress`; `p:hasPhoto`.
  Note: `p:PhysicalDriversLicense` (in `persona.ttl`) models the physical card object held in a wallet — `p:DriversLicenseDocument` is the template label that marks a topic as carrying driver's license identity data.

- `p:PassportDocument` — label for topics that carry the identity claims on a government-issued passport. Also a subclass of `p:IdentityDocument`. Declared as `template: "persona:PassportDocument"` in the topic's `mia.topics[]` entry. SHACL shape `:PassportDocumentShape` (in `cell-templates-shacl.ttl`, alongside `cat:Passport`'s template cell in `cell-templates.ttl`) targets the `p:PassportDocument` document individual and validates the holding `p:Person` via `^persona:hasIdentityDocument`:
  - **Required**: `FullName` **or** (`GivenName` + `FamilyName`); exactly one `Birthdate` (`cco:ent00000046`); exactly one Passport Number (`cco:ent00000066`); exactly one expiration date (`cco:ent00000070` → Calendar Date Identifier `cco:ont00001340`).
  - **Optional**: `AdditionalName`; issue date (`cco:ent00000069`); Issuing Jurisdiction (`cco:ent00000068`, collapsed from the former IssuingCountry); Place of Birth (`cco:ent00000067`); `p:GenderMarker`; `p:hasPhoto`.

- `p:MedicalAppointmentRecord` — label for topics that carry the claims needed to arrange a medical appointment on behalf of someone else, shared between the members coordinating that care. Not a subclass of `p:IdentityDocument`. Declared as `template: "persona:MedicalAppointmentRecord"` in the topic's `mia.topics[]` entry. SHACL shape `:MedicalAppointmentRecordShape` (in `cell-templates-shacl.ttl`, alongside `cat:MedicalAppointmentInfo`'s template cell in `cell-templates.ttl`) targets the `p:MedicalAppointmentRecord` record individual directly — the claims below are properties of the record, not of the patient's `p:Person`:
  - **Required**: exactly one `p:forPatient` link; exactly one `p:insuranceProvider`; exactly one `p:insurancePolicyNumber`.
  - **Optional**: `p:hasPrimaryCarePhysician`; `p:medicalHistoryNote`; `p:insuranceGroupNumber`; `p:preferredPharmacy`; repeatable `p:currentMedication` and `p:allergy`.

#### JSContact Field Coverage

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
- **`persona-templates.ttl`** — Defines `p:PersonaTemplate` (abstract classification superclass) and the five concrete subtypes `p:BirthCertificateDocument`, `p:JSContactCard`, `p:DriversLicenseDocument`, `p:PassportDocument`, and `p:MedicalAppointmentRecord`. These are used as values of a topic's `mia.topics[].template` field — they classify the topic, not the `p:Person` individual inside it. Also defines `p:IdentityDocument` (superclass for government-issued identity document artifacts) and `p:hasIdentityDocument` (links a `p:Person` to a `p:IdentityDocument` individual they hold); `p:BirthCertificateDocument`, `p:DriversLicenseDocument`, and `p:PassportDocument` are subclasses of both `p:PersonaTemplate` and `p:IdentityDocument`. Also defines related designator classes (`p:DriversLicenseNumber`, `p:IssuingJurisdiction`, `p:PassportNumber`, `p:IssuingCountry`, `p:PlaceOfBirth`, `p:GenderMarker`, `p:IssueDate`, `p:Credential`, `p:WebURL`, `p:OrganizationUnit`, `p:JobTitle`), complex information classes (`p:Anniversary`, `p:PersonalInfo`), annotation properties for JSContact channel labels (`p:contactContext`, `p:phoneFeature`, `p:serviceLabel`), `p:hasPhoto`, and the `p:MedicalAppointmentRecord` claim properties (`p:forPatient`, `p:hasPrimaryCarePhysician`, `p:currentMedication`, `p:allergy`, `p:medicalHistoryNote`, `p:insuranceProvider`, `p:insurancePolicyNumber`, `p:insuranceGroupNumber`, `p:preferredPharmacy`). Imported by `persona.ttl` so all topics inherit these classes transitively.

- **`cell-templates.ttl`** — Class-level `c:Cell` templates for `cat:Category` subclasses. Holds one template cell individual per templated class: `cat:Passport`, `cat:BirthCertificate`, `cat:DriversLicense`, `cat:MedicalAppointmentInfo`. Each is pointed at by its class's own `cat:templateCell` value, which is asserted in `category.ttl` itself, alongside the class's declaration (not here) — the sole route to a template individual now, since category.ttl 1.31.0 deleted `cat:Folder` and its subclasses outright. Each individual is what Mia clones into a new cell when a folder matching that class is first instantiated into a user's tree (Lazy Instantiation). Each is multi-typed `c:TCell, c:ACell, c:OneMember` — simultaneously reusable template content (`c:TCell`, carrying `c:templateShape` to its SHACL shape in `cell-templates-shacl.ttl`) and real member-classified content (`c:OneMember`, a `c:ACell` subclass, carrying `c:memberCount`). Imports `cell.ttl` directly (not `category.ttl` — no mutual import here).

- **`cell-templates-shacl.ttl`** — SHACL shapes for birth certificate, driver's license, passport, and medical appointment topics, each directly linked from its `cell-templates.ttl` template cell via `c:templateShape` (not merely co-located by naming convention):
  - `:BirthCertificateDocumentShape` (`t:template p:BirthCertificateDocument`) targets `p:BirthCertificateDocument` document individuals directly — all identity claims (names) are properties of the document individual, not the `p:Person`. Enforces: FullName OR (GivenName + FamilyName) required; optional AdditionalName, AlternateName, Nickname, Legal Name.
  - `:DriversLicenseDocumentShape` (`t:template p:DriversLicenseDocument`) targets `p:DriversLicenseDocument` document individuals directly. Enforces: FullName OR (GivenName + FamilyName) required; Birthdate, DriversLicenseNumber, ExpirationDateIdentifier required (1..1 each); IssuingJurisdiction, PostalAddress, and hasPhoto optional.
  - `:PassportDocumentShape` (`t:template p:PassportDocument`) targets `p:PassportDocument` document individuals directly. Enforces: FullName OR (GivenName + FamilyName) required; Birthdate, PassportNumber, ExpirationDateIdentifier required (1..1 each); IssueDate, IssuingCountry, PlaceOfBirth, GenderMarker, and hasPhoto optional.
  - `:MedicalAppointmentRecordShape` (`t:template p:MedicalAppointmentRecord`) targets `p:MedicalAppointmentRecord` record individuals directly — the claims needed to arrange the appointment are properties of the record, not of the patient's `p:Person`. Enforces: exactly one `forPatient`, `insuranceProvider`, and `insurancePolicyNumber` required; `hasPrimaryCarePhysician`, `medicalHistoryNote`, `insuranceGroupNumber`, `preferredPharmacy` optional; `currentMedication` and `allergy` repeatable.

- **`shacl/jscontactcard-shacl.ttl`** — SHACL shapes for JSContactCard topics (`t:template p:JSContactCard`) — remains a standalone file, since JSContactCard is reused across many unrelated tree positions with no single `cat:Category` class of its own to attach a template cell to. Validates `p:Person` instances:
  - OrganizationName required (1..1); at least one Email or TelephoneNumber required; all name components and OrganizationUnit/JobTitle optional (0..1 each).

- **`persona-shacl.ttl`** — SHACL constraint rules for all `p:Person` individuals across all topics. Validates properties including:
  - *All `p:Person` instances*: SSN format (`NNN-NN-NNNN`), email format, phone (E.164), address cardinality, payment cards, wallet, social network, bank account
  - *US Postal Address*: required street, city, state (USPS 2-letter), ZIP; optional country
  - *`p:Person`*: scalp hair (0..1); `has mother` / `is mother of` range must be a `p:Person`
  - *Social Network*: sub-groups (via `has part`) must be Social Networks; members (via `has member part`) must be `p:Person` instances
  - *Debit Card*: card number and expiration date required; CVV optional
  - *`p:Wallet`*: items declaring themselves `continuant part of` this wallet must be `p:PhysicalCard` instances
  - *`p:PhysicalCard`*: image scan, if present, must be `xsd:anyURI` (max 1); `continuant part of` target, if present, must be a `p:Wallet` (max 1)

### Persona Ontology Validation

`persona-shacl.ttl` runs against merged data from all topics (Tier 1 validation). Per-template SHACL files in `shacl/` run against individual topics, each isolated via `extract-topic.py` from its owning cell-databook (Tier 2): birth certificate, JSContactCard, driver's license, passport, and medical appointment each have their own shape file and are validated separately to avoid their `sh:targetClass` constraints firing on every relevant slice in the merged dataset. See the [Validation](EXAMPLE.md#validation) section for commands.

## Organization Ontology

The Organization ontology models organizations — companies, government agencies, nonprofits, and other institutions — that participate in the Personal Data Network.

<p align="center"><img src="images/organization-ontology/organization.png" alt="Organization model"></p>

**Classes**

* `o:Organization` — an organization (company, government agency, corporation, nonprofit, etc.) on the Personal Data Network.

### Organization Ontology File

- **`organization.ttl`** — The Organization ontology.

### Organization Ontology Validation

`organization-shacl.ttl` targets `o:Organization` instances but currently has no property constraints of its own.

## Group Ontology

The Group ontology introduces the concept of a *shared* group (`g:Group`) whose members are individuals and/or organizations. The group entity *itself* as well as any attached properties are shared with all of its members.

<p align="center"><img src="images/group-ontology/group.png" alt="Group model"></p>

**Classes**

* `g:Group` — a group of people and/or organizations on the Personal Data Network.

### Group Ontology File

- **`group.ttl`** — The Group ontology.

### Group Ontology Validation

`group-shacl.ttl` validates `g:Group` instances. Key constraint: all members (via BFO `has member part`) must be `p:Person` or `o:Organization` instances.

---

See [**EXAMPLE.md**](EXAMPLE.md) for a worked illustrative example (Alice Walker) showing how these ontologies are used together in practice, plus diagram-generation instructions and the full validation pipeline for the example dataset.
