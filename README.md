# Mia Ontologies

This document describes the ontologies used by the Mee Identity Agent (Mia) software application. The application lets the user create *cells* – private, secure collaboration spaces which can be joined by other Mia users and/or nodes on the Personal Data Network (PDN) hosted by organizations. 

The following **domain ontologies** model claims about people, organizations, and other subjects — these claims live in `t:SCTopicGraph` instances. They import and profile existing ontologies — documenting which of their classes and properties Mia requires or uses — and extending them with Mia-specific classes and properties

- **Persona ontology** — models a person: names, addresses, phone numbers, relationships, payment cards, and more. It is built on BFO (Basic Formal Ontology) and CCO (Common Core Ontologies) as the upper ontological foundation, and on domain ontologies that extend CCO:
  - **PersonOntology** — person, name types, parent-child relationships
  - **AddressOntology** — postal address structure
  - **StagingOntology** — staging area for terms pending promotion (phone numbers, email addresses, user accounts, etc.)
  - **AgentOntology** — agents and their properties (imported transitively via PersonOntology)
- **Organization ontology** — models organizations (companies, government agencies, non-profits, etc.) 

Also included are the Category, Cell and Topic **metadata ontologies**. A *cell* is the atomic unit of information. A cell is implemented as a filesystem folder holding exactly one cell DataBook file and potentially other (non-cell) files and folders. The parent folder and databook file together forming one atomic tree node. Cells nest inside cells, forming a tree. Cells have different types, called *Categories* described in the category ontology. A cell contains various kinds of content including markdown notes, chat streams, and other file attachments. It also contains structured information blocks (called *topics*) whose schemas differ based on the cell's category. 

Throughout this document we use these short-hands:

- `cat:` for the `category:` namespace (`http://mee.foundation/ontologies/category#`)
- `c:` for the `cell:` namespace (`http://mee.foundation/ontologies/cell#`)
- `t:` for the `topic:` namespace (`http://mee.foundation/ontologies/topic#`)
- `p:` for the `persona:` namespace (`http://mee.foundation/ontologies/persona#`)
- `o:` for the `organization:` namespace (`http://mee.foundation/ontologies/organization#`).

See [**EXAMPLE.md**](EXAMPLE.md) for an illustration of the use of these ontologies by a hypothetical Mia user, Alice, along with diagram-generation and validation instructions for the example dataset.

## Category Ontology

To help the Mia user organize their information, the app comes with a pre-defined tree structure of categories. Although the user is free to organize their cells however they like, we think many users will choose to create their own tree of cells based on the pattern of the tree of `cat:Category` classes and subclasses. Cells that are created based on a pre-defined category have a `c:origin` property whose value is that category. 

<p align="center"><img src="images/category-ontology/category.png" alt="Category hierarchy"></p>

These categories vary in scope from broad groupings of information to narrower ones. In the social domain, for example, a category might be about "People", or more narrowly about "Immediate Family", and ultimately about just one family member. All predefined categories are *symmetric*. For example, "Extended Family" is symmetric because if Alice is a member of Bob's extended family, the reverse is also always true.

Mia includes two predefined `cat:Category` class hierarchies rooted in the `cat:Person` and `cat:Organization`. Some classes in this hierarchy have "starter" content pointed to via `cat:templateCell` and asserted directly in `category.ttl` alongside the class's own declaration, pointing at a `c:TCell` individual defined in the companion file `cell-templates.ttl` — the *cell template* for that class.

When a new cell is created, Mia clones its class's `cat:templateCell`, if it exists, into that cell's DataBook — this is how a **cell template** becomes the starter content for a newly-created cell (see [Lazy Instantiation](#lazy-instantiation)).

As we've mentioned, the user is free to create cells not included in the predefined categories. These, by the way, need not be symmetric, and simply carry no `c:origin` value. The user is also free to rearrange their cells as they wish, adding new cells and moving others around. They can do this using the Mia app or entirely as a file system operation.

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
    - **Health** (`cat:PetsHealth`) — a pet's medical care — veterinarians, medications, devices, diagnoses, and treatments.
        - **Veterinarians** (`cat:PetsVeterinarians`) — veterinary practices and providers a pet sees for care.
        - **Medications** (`cat:PetsMedications`) — a pet's prescriptions, medications, and dosing instructions.
        - **Devices** (`cat:PetsDevices`) — medical devices and supplies used in a pet's care, e.g. syringes, nebulizers, and injection solutions.
    - **Food** (`cat:PetsFood`) — a pet's diet, food providers, feeding instructions, and dietary restrictions.
1. **Home** (`cat:Home`) — owning or renting a home, apartment, or other dwelling. Leases, deeds, utility accounts, real estate brokers.
1. **Work** (`cat:Work`) — professional roles. Employment history, resume/CV.
1. **Ownership** (`cat:Ownership`) — owned assets, property, vehicles, and other possessions.
    - **Vehicles** (`cat:Vehicles`) — related to owning and maintaining a vehicle. Vehicle insurance, repairs, mechanics, garages. 
1. **Travel** (`cat:Travel`) — travel plans, trips, and related information. Loyalty programs, airlines, bus lines, trains.
1. **Food** (`cat:Food`) — food preferences, dietary restrictions, favorite restaurants, recipes, shopping lists, and other food-related interests
1. **Sports & Entertainment** (`cat:SportsEntertainment`) — sports events (watching or participating) and entertainment (movies, plays, jazz clubs). Favorite teams/groups, venues, streaming services, ticketing. See `cat:Information` for other interests.
1. **Education** (`cat:Education`) — educational history and ongoing learning — schools, degrees, certifications, transcripts, and enrolled courses.
1. **Legal** (`cat:Legal`) — legal matters, contracts, agreements, trusts, wills, and professional legal relationships. Includes durable power of attorney and healthcare proxy agreements.
1. **Projects** (`cat:Projects`) — involvement in a specific project or initiative.
1. **Events** (`cat:Events`) — participation in or relationship to a specific event or gathering.
1. **Information** (`cat:Information`) — information about anything; articles, web links, documents, images. Includes topics that interest and inspire you (e.g. drawing, painting, dancing, religion, gaming, music). See `cat:SportsEntertainment` for sports and entertainment, and `cat:Affiliations` for formal memberships tied to a hobby or interest.
1. **Government** (`cat:Government`) — government-issued credentials, tax records, and civic relationships.
    - **Federal** (`cat:Federal`) — federal government topic (e.g. passport, federal tax records).
        - **SSN** (`cat:SSN`) — social security number issued by the federal Social Security Administration.
        - **Passport** (`cat:Passport`) — passport issued by the Department of State.
    - **State** (`cat:State`) — state government topic (e.g. driver's license, state tax records).
        - **Birth Certificate** (`cat:BirthCertificate`) — a birth certificate issued by a state agency that issues and holds these records.
        - **Drivers License** (`cat:DriversLicense`) — a driver's license issued by a state agency that issues and holds these records.
    - **Municipality** (`cat:Municipality`) — municipal government topic (e.g. local permits, library card).
        - **Residence** (`cat:Residence`) — a place a person has lived, current or past.
1. **Companies** (`cat:Companies`) — a catch-all for your relationships with companies and organizations that provide services and/or products to you that are not included in more specific categories such as `cat:Finances`, `cat:HealthWellness`, `cat:Home`, `cat:Food`, etc.

### Organizational Categories

`cat:Organization` categories organize a person's professional and organizational-role information:

1. **Customers** (`cat:Customers`) — customer organizations. Rename to "Clients", etc.
1. **Marketing** (`cat:Marketing`) — marketing activities, campaigns, and related organizations.
    - **Prospects** (`cat:Prospects`) — customer prospects. Rename to "Client prospects", etc.
1. **Partners** (`cat:Partners`) — firms that provide goods and services.
1. **People (org)** (`cat:People(org)`) — people the organization interacts with in a working capacity.
    - **Employees** (`cat:Employees`) — related to employees.
        - **Employee** (`cat:Employee`) — detailed information about a specific employee.
    - **Consultants** (`cat:Consultants`) — engaged consultants.
    - **Others (org)** (`cat:Others(org)`) — people associated with the organization who don't fit Employees, Consultants, or Colleagues.
    - **Colleagues** (`cat:Colleagues`) — coworkers and peers within the organization not tracked as formal Employee records.
    - **Advisors** (`cat:Advisors`) — individuals who advise the organization in a non-employee capacity.
    - **Board of Directors** (`cat:BoardOfDirectors`) — the organization's board members.
    - **Direct Reports** (`cat:DirectReports`) — employees who report directly to a specific manager or role within the organization.
    - **Manager(s)** (`cat:Managers`) — the manager or managers a specific employee or role reports to within the organization.
1. **KB** (`cat:KB`) — corporate knowledge bases.
1. **Projects (org)** (`cat:Projects(org)`) — projects related to R&D, manufacturing, sales, marketing, operations, HR, etc.
1. **Meetings** (`cat:Meetings`) — face-to-face or online meetings, whether internal or with clients/customers. See also Events (org) for external, travel-to or larger-scale gatherings.
1. **Events (org)** (`cat:Events(org)`) — external events that people travel to, or larger-scale gatherings — conferences, webinars, town halls, and similar events. See also Meetings for ordinary internal or client/customer meetings.
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

### Category Ontology File

**`category.ttl`** — The Category ontology, defining:
  - *Classes*: `cat:Category`, `cat:Person`, `cat:Organization`, and all leaf category subclasses.
  - *Annotation properties*: `cat:templateCell` (domain `owl:Class`, range `c:TCell`) — links a `cat:Category` subclass directly to its reusable template cell.

#### Lazy Instantiation

Cells for most `cat:Category` subclasses are not pre-created ahead of time. A cell is not created until the user wants one. When a cell matching a templated class (one carrying a `cat:templateCell` value) is first created, Mia clones that class's `c:TCell` template into the new cell: whatever `c:templateShape` value the template carried is copied into the new cell's `c:shape`, and the clone is given real member-classified content — typed with a concrete `c:ACell` subclass (e.g. `c:OneMember`) — rather than staying purely a template. 

## Cell Ontology

The cell ontology defines the concept of a cell (`c:Cell`). 

### Introduction to Cells

A cell is a secure **container of information** that can remain private to the user or be shared with other users and/or organizations.

A cell may be empty or hold various kinds of information, organized into a set of tabs:

* **Info** tab:
  * Structured information organized into one or more **topics**.
  * Some topics are about a member of the cell. When created a cell starts off with one member, the creator.
  * A cell may also have one other topic which can be about anything else (e.g. medications for a cat that the cell members are taking care of).
  * Each topic has a *subject* and a *claimant*. The subject is typically a person or organization, but it could be any other entity the Persona ontology can describe. The claimant is the person or organization that is asserting the values of the claims in the topic.
* **Notes** tab:
  * A Markdown document about the cell. It may be blank. It may be linked to any number of other Markdown notes anywhere in the user's own tree of cells, not just within the same cell.
* **Files** tab:
  * An arbitrary number of files and sub-folders.
* **Chat** tab:
  * A chat stream shared with all members.

The app contains two pre-defined, non-user-editable tree structures of **categories**. One is focused on helping organize a person's personal life (Family, Home, Pets, etc.) and the other their work life (Employer, Employees, etc.). Each category has a *template cell* which may contain some starter content (or may be empty) and may have a schema for the structured fields and values that a cell of this category might contain. Most cells are instantiated from a template cell, although the user may also create category-less cells if desired.

A cell has a **name**. Often this name is just a copy of the name of the category. For example if the category was "People", the cell might be called "People". However, the user can give the cell a name of their own choosing. This name is shared like the rest of a cell's content — every member's copy carries the same name. What is *not* shared is each member's own tree position for the cell — which parent cell they happen to file it under, and so that parent's own name — since a cell carries no property recording its own tree position at all (see [Cell Naming, Renaming, and Sharing](#cell-naming-renaming-and-sharing)).

A cell has a **`c:origin`**. The origin identifies the category (e.g. "People") the cell represents. For categories with a template cell, this is usually the category whose template was cloned to create the cell; a cell can also be assigned an origin directly, with no template involved.

A cell has a **`c:creator`**, which is the identity of the user who created it.

A cell can be **shared**. The creator of a cell can invite people (or organizations compatible with the Mee Personal Data Network protocols) to join the cell. When they do, they get a complete copy of the cell that is "alive" — any changes made to its contents, including its own name, are continuously shared with all members. The one thing that stays independent per member is where each of them files the cell in their own tree — plus, for a `c:TwoMember` cell specifically, the name itself, which is also independent per member rather than shared (see [Cell Naming, Renaming, and Sharing](#cell-naming-renaming-and-sharing)).

#### Storage

Cells are stored on the user's device(s) or, for organizations, on Personal Data Network (PDN) nodes hosted by that organization. No cell is ever stored by any cloud provider, or any third party of any kind, including The Mee Foundation.

#### Number of Members

A cell can have just one member (the user) or several. We don't yet know how many members a cell can support, but the number is almost surely well under 100.

#### Write Permissions

Notes, files, and chat are all freely readable and editable by anyone in the cell. The permissions on who can write/edit which info fields vary.

### Cell Details

The Cell class splits into two disjoint kinds: `c:TCell`, a reusable, class-level *template* cell, and `c:ACell`, an *actual* cell instantiated in a user's own tree. 

A cell is an atomic unit of information that the app manages for the user. This unit consists of a filesystem folder holding exactly one cell DataBook file, folder and file together forming one node — cells nest inside cells, forming the tree.

`c:Cell` (below) still models only the content *facet* carried by the cell DataBook file's own triples, and stores no property recording the cell's own tree position: the folder<->cell-databook pairing is always one-to-one (see [How Cells Are Persisted in the Filesystem](#how-cells-are-persisted-in-the-filesystem)), so a cell's position in the tree is simply wherever its folder currently sits — moving or renaming that folder is a pure filesystem operation that never requires updating anything asserted on the cell itself.

<p align="center"><img src="images/cell-ontology/cell.png" alt="Cell hierarchy"></p>

A cell's **files content** — everything shown in the app's **Files tab** for that cell — is every file and plain subfolder found under its own folder, to any depth, except (1) a nested folder that is itself a cell. Such a nested folder is a **descendant cell**: a separate node in the tree of cells, never counted as part of its ancestor's content even though it physically sits inside the ancestor's folder, and (2) Markdown folder notes (and other notes); these are displayed in the **Notes tab** for that cell (not the Files tab).

#### Cell Properties

- **`c:origin`** — The `cat:Category` subclass this cell was originally instantiated as, else nil. For one of the four templated classes (`cat:Passport`, `cat:BirthCertificate`, `cat:DriversLicense`, `cat:MedicalAppointmentInfo`), this is literally the class whose `c:TCell` template was cloned into this cell via [Lazy Instantiation](#lazy-instantiation); for any other cell, it's simply the category the cell was created to represent, asserted directly with no template involved. Either way the value is fixed at that point — it is not re-derived from the folder's current name, so it needs no update if the folder is later renamed or moved elsewhere in the tree. When a cell is shared with another member, the recipient's app can look at this value (if not nil) and use it as a hint as to which folder in the recipient's own tree it should be filed under. Domain `c:Cell`, range `cat:Category` (referenced by name, no `owl:imports`), at most one value (0..1) — see [Cell Ontology File](#cell-ontology-file) below.

- **`c:chat`** — optional path to chat stream. Aspirational: shown in `images/cell-ontology/cell.png`'s diagram and described here for intended semantics, but not yet defined as an actual property in `cell.ttl` (see `CLAUDE.md`'s Check 12 for this open discrepancy).

### TCell (Template Cell)

A cell pointed to by a `cat:Category` subclass (via `cat:templateCell`) serves as a **cell template** — a reusable, typically empty shape that the application clones into a new cell whenever a category of that class is first instantiated into a user's tree (see [Lazy Instantiation](#lazy-instantiation)). Such a cell is typed `c:TCell` only. An ordinary, already-instantiated cell is typed `c:ACell` instead, carrying real member composition, creator, and content. `c:TCell` and `c:ACell` are disjoint: a template cell is never also typed `c:ACell` or any of `c:OneMember`/`c:TwoMember`/`c:ThreePlusMember` — see [Cell Ontology File](#cell-ontology-file) below.

#### Properties

If a `c:TCell` has a `c:templateShape` value, then when the category pointing to it is instantiated (see [Lazy Instantiation](#lazy-instantiation)), whatever value this property has is copied into the new `c:ACell`'s `c:shape`.

- **`c:templateShape`** — links a `c:TCell` individual directly to the `sh:NodeShape`(s) describing the content expected of a topic filed under its category — e.g. `ctpl:PassportTemplateCell` carries `pshapes:PassportDocumentShape`. An `owl:ObjectProperty`, domain `c:TCell`, range `sh:NodeShape`. Makes the shape reachable by pure RDF traversal (`cat:Category` → `cat:templateCell` → `c:templateShape` → `sh:NodeShape`), not just by file co-location or naming convention. 

### ACell (Asserted Cell)

A `c:ACell` is an actual cell instantiated in a user's own tree — one of the two disjoint kinds of an abstract `c:Cell`, the other being `c:TCell`. It carries `c:memberCount`, `c:creator`, `c:memberTopics`, `c:otherTopics`, and `c:shape`. Every cell in a user's own tree is typed `c:ACell`, never `c:TCell` — there is no bare tree-position-only cell with no member content; a purely organizational cell with nothing substantive to say still carries a minimal stub `c:memberTopics` entry (claimed by and about `:Self`) rather than omitting member content altogether.

Reusable class-level templates (`cell-templates.ttl`) are the exception: each is typed solely `c:TCell`, never `c:ACell` or any `c:ACell`-lineage class like `c:OneMember` — `c:TCell` and `c:ACell` are disjoint, so a template cell carries no member composition of its own.

#### Properties

- **Subject** — not a stored property; who or what a cell's relationship is about is derived from its topic links instead. If the cell has one `c:otherTopics` value, that topic's own `t:subject` is the answer; otherwise the answer is the full set of distinct `t:subject` values found among the cell's `c:memberTopics` (its active members). See [Members](#members) below for the worked-out cases.

- **`c:memberTopics`** — one or more values, required; It's a link to the required baseline of subject-claimant topic graphs (`t:SCTopicGraph`) that hold the structured content of the cell related to the members with which the cell has been shared. Its cardinality varies by member count — see [Members](#members). Each SCTopicGraph has a *subject* and a *claimant*. The subject is typically a person, organization, or group, but it could be any other entity the Persona ontology can describe. The claimant is the person, group or organization that is asserting the values of the claims in the container. See [Topic Ontology](#topic-ontology) for details.

- **`c:otherTopics`** — optional, at most one value (0..1), uniformly regardless of member count. Link to one additional subject-claimant topic graph beyond those referenced by `c:memberTopics`. This cap is what makes deriving a cell's subject (above) unambiguous.

- **`c:shape`** — a `owl:ObjectProperty`, domain `c:ACell`, range `sh:NodeShape`. Optional; most actual cells carry no `c:shape` value. Links a `c:ACell` individual directly to the `sh:NodeShape`(s) validating that specific cell's own content, as opposed to `c:templateShape`, which describes what a topic filed under some other, template category should look like. Populated by copy-on-clone: when Lazy Instantiation clones a `c:TCell` into a new `c:ACell` — whatever `c:templateShape` value the `TCell` carried is copied into the clone's `c:shape` with the same validation expectation.

- **`c:creator`** — required, exactly one value. Identifies who created this cell's content: a single `p:Person` or `o:Organization`. 

- **`c:memberCount`** — the concrete `c:ACell` subtype this DataBook instantiates: `c:OneMember`, `c:TwoMember`, or `c:ThreePlusMember`. Value is the class itself (e.g. `mia.memberCount: "c:OneMember"`). See [Members](#members) above.

#### Members

Every `c:ACell` has a `c:memberCount`, which is a tally of the number of members of the cell. There are three concrete types: `c:OneMember` (a cell created by the user and not shared with any other member), `c:TwoMember` (the user plus exactly one other member), and `c:ThreePlusMember` (the user plus two or more other members).

Every `c:ACell` carries one or more `c:memberTopics` links (the required baseline of topic containers backing its content, one or more per member), and at most one `c:otherTopics` link (a topic beyond that baseline), regardless of member count. The cardinality of each is shown in the table below:

| Property         | OneMember | TwoMember | ThreePlusMember |
|------------------|-----------|-----------|-----------------|
| `c:memberTopics` | 1         | 2..4      | 3..N            |
| `c:otherTopics`  | 0..1      | 0..1      | 0..1            |

The `c:memberTopics` and `c:otherTopics` are lists of `t:TopicGraphs`. See the [Topic Ontology](#topic-ontology) for details.

#### Representative Cells

The diagram below shows five representative cells.

<p align="center"><img src="images/cat-cell-topic.png" alt="Cells, categories, and topics"></p>

Each cell's fill color and cell name text color follow the same convention described under [How Cells Are Persisted in the Filesystem](#how-cells-are-persisted-in-the-filesystem) below — e.g. tan fill for `People`/`Bob Johnson`/`BHS` (Person-rooted origin), light blue for `Employee` (Organization-rooted origin), purple for `Friends` (no origin at all, Custom); `Bob Johnson`'s origin is `cat:Others`, so its name doesn't match the label and is shown in black text, while `People`'s name matches its own origin's label and is shown in green. The cell DataBook's own content box is always plain white — fill color lives on the folder icon, not the box. This is purely a display choice about the cell's folder icon and name, not a separate RDF property.

Diagrams don't render a cell's subject directly — there's no stored `c:subject` to draw, and drawing the derived value would just repeat what the topic circles already show. A cell's subject can still be computed from what *is* drawn: if the cell has a `c:otherTopics` value, that topic's own subject is the answer (e.g. `Employee`, `Friends`); otherwise the answer is every distinct subject among the topic graphs pointed to by `c:memberTopics` — i.e. the cell's own active members (e.g. `People`, and `Bob Johnson`'s "Self, Bob"). A `TwoMember`/`ThreePlusMember` cell with no `c:otherTopics` is essentially about the connection between all of its members — this is why the `BHS` cell at the bottom (`ThreePlusMember`, no `c:otherTopics`) is understood as being about `:BHS`, `:Bob_Johnson`, and `:Self` together, not `:BHS` alone, even though only "BHS" appears drawn on its topic circle.

Within each cell, topic graphs shown as circles. White circles are topic graphs whose triples are claimed by the self (the user). Green circles are topic graphs whose triples are claimed by a person other than the self, or by an organization (`o:Organization`), and synchronized with the user's Mia instance over the PDN. For example the BHS cell at the bottom has three topics: Self (the user)'s BHS profile, BHS's own organization profile, and Bob Johnson's BHS member profile as claimed by Bob.

A class's template cell (`cell-templates.ttl`) may also carry validation metadata declared in the paired `cell-templates-shacl.ttl`. This metadata lives on the class-level template only.

#### Properties

The following properties are defined in `cell.ttl` and represented as `mia.` YAML fields in cell DataBooks:

| YAML field | Ontology property | Cardinality | Meaning |
|------------|-------------------|-------------|---------|
| `mia.origin` | `c:origin` | 0..1 | The `cat:Category` subclass this cell was originally instantiated as, as a class value (e.g. `"cat:Others"`); absent otherwise. Fixed at creation, not re-derived from the folder's current name. A hint for a recipient's app when this cell is shared over PDN |
| `mia.memberCount` | `c:memberCount` | 1 | The concrete `c:ACell` subclass this DataBook instantiates, as a class value (e.g. `"c:OneMember"`) |
| `mia.creator` | `c:creator` | 1 | Who created this cell's content — a `p:Person` or `o:Organization` |
| `mia.shape` | `c:shape` | 0..1 | Optional `sh:NodeShape` validating this specific cell's own content directly |

There is no `mia.subject` field — who or what a cell's content is about is derived from `mia.memberTopics`/`mia.otherTopics` rather than asserted independently (see [Topic Link Properties](#topic-link-properties) below).

#### Topic Link Properties

Each cell DataBook carries one or more `c:memberTopics` links (the required per-member baseline) and at most one `c:otherTopics` link (a topic beyond that baseline) to the actual topic DataBook container(s) backing its content:

| Property | Value | Cardinality | Meaning |
|----------|-------|-------------|---------|
| `c:memberTopics` | `t:SCTopicGraph` | 1 on `OneMember`; 2..4 on `TwoMember`; 3..N on `ThreePlusMember` (required) | The required baseline of self-vs-other classified topics backing this cell's content — at least one per member in the relationship (up to all four self-vs-other combinations for `TwoMember`) — distinguished by each linked topic's own `subject`/`claimant` combination rather than by separate properties or classes |
| `c:otherTopics` | `t:SCTopicGraph` | 0..1 (optional), uniformly regardless of member count | At most one additional topic beyond the `c:memberTopics` baseline |

Together, these two properties are also the sole basis for deriving a cell's subject (who or what its relationship is about), now that there is no independently-asserted `c:subject` property: if the cell has a `c:otherTopics` value, that topic's own `t:subject` is the answer; otherwise the answer is the full set of distinct `t:subject` values among `c:memberTopics` (the cell's active members). `c:otherTopics` is capped at one value precisely so this derivation is always unambiguous — see [Representative Cells](#representative-cells) above for worked examples.

`c:memberTopics` and `c:otherTopics`'s domain is the broader `c:ACell` rather than `c:MultiMember`, unlike the four properties `c:topics` (via its predecessor `c:secondary`) replaced (`c:sbs`/`c:obs`/`c:sbo`/`c:obo`) — a `OneMember` cell can hold a self-by-self topic through `c:memberTopics`, not just a `TwoMember`/`ThreePlusMember` cell. `c:memberTopics`'s per-member-count cardinality *is* enforced by `cell-shacl.ttl`, via three shapes targeting `cell:OneMember`/`cell:TwoMember`/`cell:ThreePlusMember` directly (`:OneMemberShape`, `:TwoMemberShape`, `:ThreePlusMemberShape`) — this replaced the single `c:topics` property's old blanket "at least one, no upper bound" rule, which didn't vary by member count. `c:otherTopics` stays uniform across all member counts, enforced only by the general `:ACellShape` (each value must be a `t:SCTopicGraph`, `sh:maxCount 1`).

### How Cells Are Persisted in the Filesystem

A folder is a **cell** exactly when it holds one **cell DataBook** (see [Representative Cells](#representative-cells) above) directly inside it, whose filename's `<local>` segment is an exact copy of the folder's own name — that single file alone marks the folder as a cell. A folder without a matching cell DataBook is simply a **regular filesystem folder**, not a cell — even if it contains nested cells of its own further down. A folder can never hold more than one cell DataBook, because a `c:Cell` is, by definition, self-contained, and letting two cells share a folder would risk a single file in that folder becoming ambiguously part of both.

A cell's DataBook may carry a `c:origin` value, asserted as `mia.origin` in its own YAML front matter. When present, it records the `cat:Category` subclass — always ultimately reachable from `cat:Person` or `cat:Organization` — the cell was originally instantiated from; this value is fixed at that point, not re-derived from the cell's folder's current name, so the folder can be freely renamed or moved without needing to update it. There are accordingly **three category types**, and the diagram below colors each cell's folder icon fill by which one it is: **Person** (tan, origin reachable from `cat:Person`), **Organization** (light blue, origin reachable from `cat:Organization`), and **Custom** (purple, no `c:origin` at all — a cell the user created without picking any existing `cat:Category` class). Custom is identified precisely, not by judgment call: the cell's DataBook filename carries the literal `(custom)` disambiguator in place of an origin-derived `<catType>` (e.g. `Friends(custom).databook.md` — see the [Cell DataBook Filename Convention](CLAUDE.md#cell-databook-filename-convention) in CLAUDE.md).

A cell's own **name** — its filesystem folder's own name — is a separate, purely display-level choice, independent of the above: when the cell does have an origin, the name may be copied verbatim from that origin category's own `rdfs:label` (e.g. a cell named "Others" whose origin is `cat:Others`), or the user may give it a different name entirely (e.g. a cell named "Bob Johnson" whose origin is still `cat:Others`). This name is recorded in the cell DataBook's own `title:` YAML field, which always equals the folder's own name verbatim (same case, spacing, and punctuation) and is kept in sync with it — renaming the folder means updating `title:` to match, not the other way around; `title:` is never an independent override of the folder's name. For a `c:OneMember` or `c:ThreePlusMember` cell, this name is part of the cell's own shared content: it is kept in sync and identical across every member's copy, exactly like its topics, files, notes (a note's own text, including any links it contains, but not necessarily the resolvability of a link pointing outside the cell — see the folder note description below), chat, `c:origin`, and every other field in its DataBook (see [Introduction to Cells](#introduction-to-cells)). What stays independent per member is only their own tree *position* for the cell — the parent it's nested under, and so that parent's own name — since a cell carries no property recording its own tree position at all. A `c:TwoMember` cell is the one exception: there, the name itself is also independent per member, alongside tree position, rather than shared — see [Cell Naming, Renaming, and Sharing](#cell-naming-renaming-and-sharing) below for both this exception and how the app keeps a shared name unique within each member's own tree. The diagram renders this in the folder-name text color — **green** ("Predefined folder name") when the name matches the origin's label verbatim, plain **black** ("User-defined folder name") when the user has customized it. This text color is unrelated to the icon fill color above — a cell can be tan-filled (Person) with black text (e.g. "Bob Johnson"), light-blue-filled (Organization) with black text, or purple-filled (Custom, no origin at all) with black text — a Custom cell's name has no label to possibly match, so it is always black text too, never green.

The diagram below shows how a three level snippet of the user's tree of cells is represented concretely in filesystem folders and files.

<p align="center"><img src="images/folder-mapping.png" alt="Cells, categories, and topics"></p>

- Every file and non-cell subfolder found inside a cell's folder — to any depth — that is not itself a descendant cell (see below) is that cell's own content, shown in the app's Files tab, and travels with the cell when it's shared. A nested folder that is itself a cell (i.e. holds its own cell DataBook) is a **descendant cell** — a separate node in the tree — and is never counted as part of its ancestor's content, even though it physically sits inside the ancestor's folder.
- One special file is the cell's **cell DataBook** (a `.databook.md` file with `type: cell-databook`) — see [How Cells Are Persisted in the Filesystem](#how-cells-are-persisted-in-the-filesystem) above for why a folder can never hold more than one. A cell DataBook's *filename* matches its own folder's name verbatim, with each space replaced by a hyphen (spaces are illegal inside a raw Turtle IRI), and its `title:` field is exactly the folder's own name — the cell's name — updated whenever the folder is renamed. Its `id`, by contrast, is a flat, opaque `cell-<NN>` value independent of the folder name (see CLAUDE.md's Check 9), the same pattern topic ids already use.
- Another special file acts as a note about the cell. This so-called *folder note* is stored as a file named `X.md` inside the `X` folder. Using the same name as the folder matches the convention used by PKM (Personal Knowledge Management) tools such as Obsidian (using the Folder Notes plugin), Logseq, Foam and others — including the same freeform, vault-wide linking these tools support: a folder note may link to any other note anywhere in the user's tree of cells, not just within its own cell. A link's own text travels with the cell's note when the cell is shared, but the linked-to note itself does not: if the target lies outside this cell's own boundary (i.e. it isn't part of this cell's own Files-tab content or its own folder note), the recipient may not have that other cell at all, or may organize their tree completely differently, so the link simply won't resolve on their side. This is an accepted limitation of cross-cell linking, not a defect.

### Cell Naming, Renaming, and Sharing

This section describes app-level behavior, not an ontology rule — nothing here changes `cell.ttl` or any DataBook triple.

For a `c:OneMember` or `c:ThreePlusMember` cell, any member of the cell — not just its creator — can rename it, and the new name propagates to every member. Mia's cell model has no creator/admin-only privilege tier for this or any other content action, matching [Write Permissions](#write-permissions) above, where notes, files, and chat are already freely editable by anyone in the cell. This mirrors how **Slack** and **Notion** handle renaming by default: any member/editor can rename a channel or page, and the new name propagates to everyone. It's a deliberate contrast with **Microsoft Teams** (channel owners only, by default), **Discord**, and **GitHub**, which restrict renaming to a privileged admin/Manage-Channels/owner role — a distinction Mia's cell model doesn't have to begin with. A `c:TwoMember` cell does *not* follow this rule — see the exception below.

A cell's name must be unique among its sibling cells — the cells directly nested under the same parent. When a user renames a cell — e.g. to give it a name of its own choosing, different from its origin category's label, the same convention followed by other PKM tools — to a name that already belongs to one of its siblings, the app doesn't prompt or reject the input: it silently appends the next available integer suffix (`"1"`, `"2"`, ...) to make the name unique. The same rule applies when creating a brand-new cell whose default name (e.g. copied verbatim from its origin category's own label) would otherwise collide with an existing sibling.

This same uniqueness rule applies on **receipt** of a shared cell — for both `c:TwoMember` and `c:ThreePlusMember` cells alike — and, once a `c:TwoMember` cell's name goes independent per member (see the exception below), on every later rename by either member too: if the incoming or renamed name collides with a cell the recipient already has at that position in their own tree, the app appends the next available suffix to it rather than overwriting the existing cell or rejecting the incoming/renamed one.

**Exception: `c:TwoMember` cells.** A two-member cell's name is never shared, synced content between its two members, in contradiction to the general rule above — each member is independently responsible for the name on their own side. This is because, unlike a `c:ThreePlusMember` cell (a genuine group identity with no single "other side" to name from), a two-member cell is an asymmetric dyad: each member's name for it naturally reflects their own perspective on the *other* party, and there's no single name that fits both. The creator's name for their own copy is simply whatever they set it to — chosen and renamed exactly as for any other cell, subject only to the sibling-uniqueness rule below, but never propagated to the recipient's copy.

At **first-time receipt** of a `c:TwoMember` cell — the recipient self-evidently did not create it, they're joining one already created — the app does not just adopt the creator's name as shared content. Instead, once, at that first receipt, it analyzes the `c:memberTopics` graph(s) belonging to the cell's creator/sender member and auto-generates a name for the cell from that analysis. (The sender's own choice of name for their copy is naturally centered on their own perspective, so blindly reusing it verbatim on the recipient's side would be a poor fit; analyzing the sender's own member topics lets the recipient's app derive a name that makes sense from its own side instead.) This auto-generated name is subject to the same sibling-uniqueness suffixing described above.

For example, Alice creates a `c:TwoMember` cell about her relationship with Bob and names it "Bob" on her own side, then shares it with Bob. On first receipt, Bob's app doesn't just copy "Bob" — that's Alice's name for *him*, not a name that makes sense in Bob's own tree. Instead it scans the cell's `c:memberTopics` graph(s) belonging to Alice, finds a topic graph about Alice herself, extracts her given name, and names the cell "Alice" on Bob's side instead.

From that point on, both the creator's and the recipient's names for their own copies may be freely renamed at any time, exactly like a `c:OneMember` cell's name — but such a rename stays purely local to the renaming member's own tree and is never propagated to the other member's copy, in either direction. This is what keeps the first-receipt divergence meaningful: if a later rename on either side rippled to the other, it would silently overwrite a name chosen to fit that member's own perspective, defeating the reason the divergence exists in the first place.

### Cell Ontology File

**`cell.ttl`** — The Cell ontology, defining:
  - *Classes*: `c:Cell` (formerly `c:Parties`), splitting into two disjoint kinds, `c:TCell` (abstract, reusable class-level template) and `c:ACell` (abstract, actual cell instantiated in a user's own tree) — a cell is always exactly one, never both (`owl:disjointWith`); `c:OneMember`, `c:MultiMember` (abstract), `c:TwoMember`, `c:ThreePlusMember` — all now subclasses of `c:ACell` rather than `c:Cell` directly (cell.ttl 3.7.0).
  - *Annotation properties*: `c:label` (default display name for a concrete `c:Cell` subtype, asserted on the class), `c:abstract` (marks a class as not directly instantiated in DataBooks). There is no `c:subject` annotation property — who or what a cell's relationship is about is derived from `c:memberTopics`/`c:otherTopics` rather than independently asserted (see [Topic Link Properties](#topic-link-properties)).
  - *Object properties*: `c:origin` (domain `c:Cell`, range `cat:Category` — added cell.ttl 3.20.0; the `cat:Category` subclass this cell was originally instantiated as, else nil; fixed at creation, not re-derived from the folder's current name; at most one value); `c:templateShape` (domain `c:TCell`); `c:memberCount`/`c:creator`/`c:memberTopics`/`c:otherTopics`/`c:shape` (domain `c:ACell` — every cell in a user's own tree is typed `c:ACell`, never `c:TCell`, so every such cell carries all of these; the reusable class-level templates in `cell-templates.ttl` are typed `c:TCell` instead and carry none of them). `c:creator`'s range is a union of `p:Person` and `o:Organization` — the same union-range pattern used by `topic:claimant` (see [Topic Ontology File](#topic-ontology-file)). `c:memberCount`'s range is `c:ACell` itself: its value is the concrete subclass (`c:OneMember`/`c:TwoMember`/`c:ThreePlusMember`), not a string — class-value punning; `c:origin`'s range `cat:Category` uses this same punning — its value is the concrete leaf subclass (e.g. `cat:Others`), not a string. `c:templateShape`'s and `c:shape`'s ranges are both `sh:NodeShape` — see [Cell Ontology](#cell-ontology) above — but on different domains: `templateShape` describes what a topic filed under a *template* category should look like, while `shape` validates an *actual* cell's own content directly. `c:memberTopics`/`c:otherTopics`'s range is `t:SCTopicGraph` — the former is the required per-member baseline (split from the single `c:topics` property, cell.ttl 3.14.0), the latter any number of additional topics beyond it. `c:Cell` carries no property pointing back to its own folder at all — a cell IS its folder together with this DataBook file, not two separately-associated things, so there is no distinct folder individual to point at (category.ttl 1.31.0 deleted `cat:Folder` and its subclasses outright); `c:origin`'s range is the classificatory `cat:Category`, not a tree position — it records what kind of thing a cell is, not where it lives, letting a recipient's app use it as a filing hint when a cell is shared over PDN.
  These terms are referenced by name in the YAML front matter of each cell DataBook file. `cell.ttl` imports `topic.ttl` (for `c:memberTopics`/`c:otherTopics`'s range, `t:SCTopicGraph`); `topic.ttl` in turn imports `cell.ttl` back, solely to reuse `c:abstract` — a mutual import. `category.ttl` also imports `cell.ttl` (to reuse `c:abstract`, and by name in `c:origin`'s doc comments), but `cell.ttl` does not import `category.ttl` back — `c:origin`'s range `cat:Category` is referenced by name only, exactly like `cell.ttl` already does for `p:Person`/`o:Organization` in `c:creator`'s range, without importing `persona.ttl` or `organization.ttl` — the same choice `topic.ttl` makes for `topic:claimant`.

**`cell-shacl.ttl`** — SHACL shapes for cell DataBook instances, split across shapes matching `cell.ttl`'s two-kind split: `:CellShape` (target `c:Cell`) constrains `c:origin` to at most one value (0..1, added cell-shacl.ttl 3.15.0 — not constrained via `sh:class cat:Category`, since a legal value is the concrete leaf subclass itself, never `rdf:type cat:Category`, mirroring `c:memberCount`'s own identical unconstrained, class-value-punning treatment above; its earlier `c:folder` cardinality constraint was removed outright in cell-shacl.ttl 3.17.0, once `c:folder` itself was removed from `cell.ttl`) and requires `rdf:type` to be exactly one of `c:TCell`/`c:ACell` (`sh:xone`, added cell-shacl.ttl 3.24.0, mirroring `cell.ttl`'s `owl:disjointWith` — never both, never neither); `:TCellShape` (target `c:TCell`) constrains `c:templateShape` to at most one value; `:ACellShape` (target `c:ACell`) constrains `c:creator` to exactly one value, which must be a `p:Person` or `o:Organization`, `c:memberCount` to exactly one value which must be the class `c:OneMember`, `c:TwoMember`, or `c:ThreePlusMember`, `c:otherTopics` to at most one value which must be a `t:SCTopicGraph` (`sh:maxCount 1`, added cell-shacl.ttl 3.23.0 — this cap is what makes deriving a cell's subject from its topic links unambiguous), and `c:shape` to at most one value. Cardinality for `c:memberTopics` is enforced instead by three shapes targeting `cell:OneMember`/`cell:TwoMember`/`cell:ThreePlusMember` directly (`:OneMemberShape`, `:TwoMemberShape`, `:ThreePlusMemberShape`, since `yaml-to-rdf.py` types every cell individual with its concrete member class) — exactly 1/2..4/at least 3 respectively, replacing the single `c:topics` property's old blanket "at least one, no upper bound" rule, which didn't vary by member count. `c:templateShape`/`c:shape` are deliberately not constrained to `sh:class sh:NodeShape`: the individuals they point at are only typed `sh:NodeShape` in `cell-templates-shacl.ttl`, which Tier 1 validation deliberately excludes from its merged-data run (see [Validation](EXAMPLE.md#validation)), so that constraint would spuriously fail there. There is no `c:subject` shape — that property no longer exists.

### Cell Ontology Validation

Cell DataBook instances are validated by `cell-shacl.ttl`: `origin`/`memberCount`/`memberTopics`/`otherTopics`/`creator`/`shape` exist solely as `mia.` YAML frontmatter fields on cell DataBooks, so `yaml-to-rdf.py` synthesizes the corresponding `c:` triples (`rdf:type c:Cell`, `c:origin` if present, plus `rdf:type c:ACell`/the concrete member class/`c:memberCount`/`c:creator`/`c:memberTopics`/`c:otherTopics`/`c:shape` once `memberCount` is set) directly from frontmatter, letting `:CellShape`/`:ACellShape`/the per-member-count shapes actually fire against real instance data — see [Tier 1](EXAMPLE.md#validation). `c:origin` is asserted on every `c:Cell` regardless of kind, since its domain is `c:Cell` itself, not `c:ACell`. Every cell-databook carries a `mia.memberCount` value, so `yaml-to-rdf.py` always types it `rdf:type c:ACell` — satisfying `:CellShape`'s `c:TCell`/`c:ACell` `sh:xone` requirement via the `c:ACell` branch — so `:ACellShape`'s and the per-member shapes' required `c:memberTopics` always apply; a category node with nothing substantive to say uses a minimal stub `c:memberTopics` entry rather than omitting member content. (`c:TCell` individuals live only in `cell-templates.ttl`, a plain `.ttl` file rather than a DataBook excluded from Tier 1's merge entirely — see [Validation](EXAMPLE.md#validation) — so they need no such synthesis either.) There is no `mia.subject`/`c:subject` to synthesize — a cell's subject is derived, not stored.

## Topic Ontology

The topic ontology defines *topics* (`t:TopicGraph`) — named graphs containing sets of claims about some resource; that resource need not be a person (see `t:subject` below). Topics are referenced by cells described in the Cell Ontology.

### Topics

A topic is a container of information related to an interaction with, or relationship to, another person, group, or organization. This information is expressed as a named graph of triples — typically using the Persona, Organization, and Group ontologies when the topic is about a person, group, or organization, though the ontology does not require this — and stored in a **[DataBook](https://github.com/w3c-cg/holon/tree/main/architectures/databook)** (`.databook.md`) file that describes one facet of its subject (called the `subject` of the topic). These claims may have originated from other topics about the same subject. 

<p align="center"><img src="images/topic-ontology/topic.png" alt="topic ontology"></p>

One property applies to every `t:TopicGraph`:

**`t:template`** — present only on topics that contain instances of a template; its value is the name of a `p:PersonaTemplate` subclass (e.g. `"persona:BirthCertificateDocument"`, `"persona:JSContactCard"`, `"persona:DriversLicenseDocument"`, `"persona:PassportDocument"`, `"persona:MedicalAppointmentRecord"`).

A topic carries no field pointing back at the cell that references it — that link is asserted only on the cell side, via `c:memberTopics`/`c:otherTopics` (see the Cell Ontology section above).

Two more properties apply to every topic linked from a cell, since every `c:memberTopics`/`c:otherTopics` value is classified as `t:SCTopicGraph`:

**`t:subject`** — The resource the topic is about. Value is any resource IRI — the ontology does not require it to be a `p:Person` or `o:Organization`, though in this example every `subject` value happens to be one of those two:
- `:Self` — the topic is about the Mia user.
- a named individual of `p:Person` — the topic is about another human Mia user.
- a named individual of `o:Organization` — the topic is about an organization (legal corporation or government agency).

**`t:claimant`** — Who is making the claim. Values are local IRIs of `p:Person` or `o:Organization` individuals:
- `:Self` — the Mia user that is entering the data, even if the underlying information originates from some other party such as a company, government agency, or another person.
- a named individual of class `p:Person` — another Mia user is claiming the data directly.
- a named individual of class `o:Organization` — an organization is claiming the data.

The diagram below shows four kinds of topics related to a hypothetical Mia user, Alice, and her interactions with a Department of Motor Vehicles (DMV) agency. Across the top are two topics where the DMV itself is the subject, and at the bottom where Alice is the subject. At the left are topics where Alice has made the claims (e.g. Alice's Mia has written the claims into the topic) and at the right are topics where the DMV as the "other" has written the claims. 

<p align="center"><img src="images/topic-ontology/quadrants.png" alt="a quadrant of topic types"></p>

The lower left shows a topic that Alice might share with other people or companies. In it, she claims that her driver's license number is S43228943, having copied that number from her physical driver's license. The topic in the lower right carries the same information as the lower left, but because it is being claimed by the DMV it is more likely to be trusted by a recipient (especially if this information is conveyed via secure channel and the claims are cryptographically bound to the identity of the DMV).


### Topic Ontology File

**`topic.ttl`** — the Topic ontology, defines:
  - *Classes*: `t:TopicGraph`, `t:SCTopicGraph` (Subject-Claimant topic graph; the concrete class every self-vs-other classified topic is typed as directly — it has no subclasses; carries the `t:subject`/`t:claimant` annotations — every topic reachable from a cell, via `c:memberTopics`/`c:otherTopics`, is a `t:SCTopicGraph`).
  - *Annotation properties*: `t:template` (domain `t:TopicGraph`), `t:claimant` (range a union of `p:Person`, `o:Organization`), `t:subject` (domain `t:SCTopicGraph`; range `xsd:anyURI` — any resource IRI, not necessarily a `p:Person`/`o:Organization`).
  These terms are referenced by name in each topic's `mia.topics[]` entry, inside its owning cell-databook file. `topic.ttl` imports `cell.ttl` to reuse `c:abstract` on `t:TopicGraph`/`t:SCTopicGraph`.

**`topic-shacl.ttl`** — SHACL shapes for topic instances: `:SCTopicGraphShape` (target `t:SCTopicGraph`) constrains `t:claimant` to exactly one value, which must be a `p:Person` or `o:Organization`, and `t:subject` to exactly one value, which must be an IRI.

### Topic Ontology Validation

`topic-shacl.ttl`'s `:SCTopicGraphShape` (see above) targets `topic:SCTopicGraph`, but that typing is itself only ever asserted via the `claimant`/`subject` fields of that entry, never as a literal `rdf:type topic:SCTopicGraph` triple in the topic's own extracted Turtle body. `yaml-to-rdf.py` synthesizes it directly from the cell-databook's frontmatter — `rdf:type topic:SCTopicGraph` plus `topic:claimant`/`topic:subject`, asserted on the topic's plain `id` (the `mia.topics[].id` value), not the `#graph`-suffixed `graph.named_graph` IRI (see `topic.ttl` 1.11.0) — so `:SCTopicGraphShape` actually fires against real instance data; see [Tier 1](EXAMPLE.md#validation). The remaining classification facts are synthesized the same way from the cell-databook's frontmatter: `origin`/`memberCount`/`memberTopics`/`otherTopics`/`creator`/`shape` (see [Cell Ontology Validation](#cell-ontology-validation)).

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

**Properties:**

- `p:hasBankAccount` — links a `p:Person` to a `p:CheckingAccount` it records.
- `p:accessesBankAccount` — links a DebitCard to the `p:CheckingAccount` it draws funds from.

### Contact-Related Classes and Properties

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

### Medication-Related Classes and Properties

This section describes the classes and properties, all defined in `persona-templates.ttl`, that model a single medication entry — what drug, how much, and how often — reusing external vocabulary wherever one fits rather than inventing flat strings.

**Classes:**

- `p:PetMedicationRecord` — subclass of `p:PersonaTemplate`; template label for a topic that carries a pet's list of medications, and also the class of the record individual itself (a pet has no `p:Person` individual of its own, so `p:hasMedication` links hang off this record rather than off a person).
- `p:Medication` — a single medication entry: what drug, how much, and how often.
- `p:DosageAmount` — how much of a `p:Medication` is given per dose; multi-typed as CCO's Information Bearing Entity (`cco:ont00000253`) and Ratio Measurement Information Content Entity (`cco:ont00001283`).
- `p:MedicationAdministration` — how often, and over what period, a `p:Medication` is given; subclass of DrOn's "drug administration" process class (`DRON:00000031`).

**Properties:**

- `p:hasMedication` — links a `p:PetMedicationRecord` to one of its `p:Medication` entries (domain `p:PetMedicationRecord`, range `p:Medication`); repeatable.
- `p:hasActiveIngredient` — links a `p:Medication` directly to a ChEBI chemical-substance class IRI (e.g. `CHEBI:2676` for amoxicillin); repeatable for combination drugs.
- `p:hasDoseForm` — links a `p:Medication` to a DrOn dose-form class IRI (e.g. `DRON:00000022` "drug tablet"); omitted for a true measured quantity (e.g. a teaspoon of liquid) rather than a count of discrete units.
- `p:hasDosageAmount` — links a `p:Medication` to its `p:DosageAmount` (domain `p:Medication`, range `p:DosageAmount`).
- `p:hasAdministration` — links a `p:Medication` to its `p:MedicationAdministration` (domain `p:Medication`, range `p:MedicationAdministration`).
- `p:medicationFrequencyPerDay` — free-text frequency, e.g. `"2"` or `"as needed"` (domain `p:MedicationAdministration`).
- `p:medicationBrandName` — free-text marketed brand name, e.g. `"Clavamox"` (domain `p:Medication`) — kept as a plain string since DrOn embeds brand names only inside auto-generated RxNorm product-class labels, not as a reusable property.
- `p:medicationManufacturer` — free-text manufacturer name, e.g. `"Zoetis"` (domain `p:Medication`) — kept as a plain string since DrOn has no manufacturer/labeler class.
- `p:medicationDuration` — free-text alternative to a fixed end date, e.g. `"10 days"` (domain `p:Medication`), for courses with no fixed calendar end date.

`p:DosageAmount` also carries exactly one of CCO's `cco:ont00001769` ("has decimal value") or `cco:ont00001773` ("has integer value"), and optionally `cco:ont00001863` ("uses measurement unit") pointing at a CCO Measurement Unit individual (e.g. "Teaspoon Measurement Unit", `cco:ont00001573`) — omitted for a count of discrete dose-form units. `p:MedicationAdministration` carries `p:medicationFrequencyPerDay` plus exactly one `BFO_0000199` ("occupies temporal region") link to a `BFO_0000038` temporal-interval individual carrying `cco:ent00000017`/`cco:ent00000018` ("has start/end date") — the same `AddressDesignation` temporal-interval pattern used for address history above; an absent end date means the medication is ongoing.

The external ontologies reused above, and one deliberately not used:

- **[DrOn](https://github.com/mcwdsi/dron) (the Drug Ontology)** — the only drug-domain ontology actually built on BFO, the same upper ontology CCO (and therefore this project) already uses. A small, hand-curated subset of its upper module — `p:hasDoseForm`'s target classes ("drug tablet", "drug capsule") and `p:MedicationAdministration`'s superclass ("drug administration") — is vendored at `project_files/dron-upper.ttl` and `owl:import`ed from `persona-templates.ttl`; DrOn's real per-product classes (auto-generated from RxNorm, hundreds of thousands of them, ~300MB) are not vendored, since nothing here needs them.
- **[ChEBI](https://www.ebi.ac.uk/chebi/)** (Chemical Entities of Biological Interest) — `p:hasActiveIngredient`'s values are real ChEBI class IRIs (e.g. `CHEBI:2676` for amoxicillin), cited directly, not imported (ChEBI is far larger than DrOn) — the same move DrOn itself makes for chemical-substance identity rather than modeling chemistry on its own.
- **CCO's already-vendored, already-transitively-imported `UnitsOfMeasureOntology.ttl`/`InformationEntityOntology.ttl`** (via `PersonOntology.ttl`'s own `owl:imports` chain, but never previously used by anything in this project) — supplies `p:DosageAmount`'s value/unit-linking properties and real unit individuals (Teaspoon/Tablespoon/Milliliter/Milligram Measurement Unit).
- **FHIR RDF was deliberately not used** — despite HL7 FHIR's `Quantity`/`Dosage` datatypes being a natural-looking fit on paper, FHIR RDF is not BFO-aligned (HL7's own documentation concedes the mismatch and describes FHIR RDF as record/transaction-oriented, "should not be directly interpreted as stating facts"), is ~6MB/1000+ classes, and validates natively via ShEx rather than SHACL — a poor fit for this project's architecture. Only its general shape (value+unit, frequency+period) served as informal inspiration for `p:DosageAmount`/`p:MedicationAdministration`'s design, with no RDF-level dependency.
- `p:usesDrOnClass`/`p:usesChEBIClass` (annotation properties, `persona.ttl`, mirroring `p:usesCCOClass`) document exactly which DrOn/ChEBI classes are actually referenced, asserted on `persona-templates.ttl`'s own ontology header.

### Modeling Details

This section describes a few details related to modeling names and addresses.

**Peer name pattern**: All name types (FullName, GivenName, FamilyName, AlternateName) connect directly to a `p:Person` via `designated by` (`ont00001879`). They are siblings, not nested under a PersonName parent. Legal names belong to the birth certificate topic (annotated `t:template p:BirthCertificateDocument`); a preferred/goes-by name (AlternateName) belongs to each social or professional topic where it applies.

**Address history**: Each address topic carries a `p:Person` with a USPostalAddress and an `AddressDesignation` with a `TemporalInterval` (start date required; no end date = current address).

### Persona Templates

`p:PersonaTemplate` is an abstract classification class that serves as the common superclass for all reusable, topic-type-specific template labels. These labels are defined in `persona-templates.ttl`. A topic declares its template as the `template` field of its `mia.topics[]` entry (inside its owning cell DataBook's front matter) rather than by typing its `p:Person` individual. 

Five of the six per-template SHACL shapes (`p:BirthCertificateDocument`, `p:DriversLicenseDocument`, `p:PassportDocument`, `p:MedicalAppointmentRecord`, `p:PetMedicationRecord`) live in `cell-templates-shacl.ttl`, each directly linked from its class-level `c:TCell` template (in `cell-templates.ttl`) via `c:templateShape` (`cell.ttl`) — so the shape is reachable by RDF traversal from the corresponding `cat:Category` class (`cat:BirthCertificate`, `cat:DriversLicense`, `cat:Passport`, `cat:MedicalAppointmentInfo`, `cat:PetsMedications`) via `cat:templateCell` — see [Lazy Instantiation](#lazy-instantiation); `p:JSContactCard`'s shape remains a standalone file in `shacl/`, since it's reused across many unrelated tree positions with no single `cat:Category` class of its own to attach to.

<p align="center"><img src="images/persona-ontology/persona-templates.png" alt="persona templates model"></p>

**Government-issued identity documents** — `p:BirthCertificateDocument`, `p:DriversLicenseDocument`, and `p:PassportDocument` are subclasses of both `p:PersonaTemplate` (template label use) and `p:IdentityDocument` (artifact instance use). `p:IdentityDocument` is the class for government-issued documents that formally identify a person. The property `p:hasIdentityDocument` (domain: `p:Person`, range: `p:IdentityDocument`) links a person to the government document they hold. Each government-ID topic declares one named individual of the document type and links it from `:Self`. `p:JSContactCard` is a format label only — not a government-issued document — and is a subclass of `p:PersonaTemplate` only.

The six currently defined subclasses of `p:PersonaTemplate` are:

- `p:BirthCertificateDocument` — label for topics that carry a person's legal birth name record as issued by a state agency. Also a subclass of `p:IdentityDocument`. Declared as `template: "persona:BirthCertificateDocument"` in the topic's `mia.topics[]` entry. SHACL shape `:BirthCertificateDocumentShape` (in `cell-templates-shacl.ttl`, alongside `cat:BirthCertificate`'s template cell in `cell-templates.ttl`) targets the `p:BirthCertificateDocument` document individual and validates the holding `p:Person` via `^persona:hasIdentityDocument`:
  - **Required**: either a `FullName` designator **or** both a `GivenName` and a `FamilyName` designator (via `designated by`, `ont00001879`) — expressed with `sh:or`.
  - **Optional**: `AdditionalName` (middle name), `AlternateName` (e.g. maiden name), `Nickname`, and `Legal Name` designators.

- `p:JSContactCard` — label for topics that carry professional contact details in the JSContact (RFC 9553) format. A digital contact format (RFC 9553) — not a government-issued identity document, and therefore not a subclass of `p:IdentityDocument`. Declared as `template: "persona:JSContactCard"` in the topic's `mia.topics[]` entry. SHACL shape `:JSContactCardPersonShape` (in `shacl/jscontactcard-shacl.ttl`) enforces:
  - **Required**: exactly one `OrganizationName` designator; at least one `Email` or `TelephoneNumber` designator.
  - **Optional**: all name components, `OrganizationUnit`, `JobTitle`, addresses, online services, anniversaries, personal info, photo.
  - **Max 1** on all single-valued name and organization components.
  See the [JSContact field coverage table](#contact-related-classes-and-properties) above for the complete mapping.

- `p:DriversLicenseDocument` — label for topics that carry the identity claims on a state-issued driver's license. Also a subclass of `p:IdentityDocument`. Declared as `template: "persona:DriversLicenseDocument"` in the topic's `mia.topics[]` entry. SHACL shape `:DriversLicenseDocumentShape` (in `cell-templates-shacl.ttl`, alongside `cat:DriversLicense`'s template cell in `cell-templates.ttl`) targets the `p:DriversLicenseDocument` document individual and validates the holding `p:Person` via `^persona:hasIdentityDocument`:
  - **Required**: `FullName` **or** (`GivenName` + `FamilyName`); exactly one `Birthdate` (`cco:ent00000046`); exactly one Driver's License Number (`cco:ent00000065`); exactly one expiration date (`cco:ent00000070` → Calendar Date Identifier `cco:ont00001340`).
  - **Optional**: `AdditionalName`; Issuing Jurisdiction (`cco:ent00000068`); `PostalAddress`; `p:hasPhoto`.
  Note: `p:PhysicalDriversLicense` (in `persona.ttl`) models the physical card object held in a wallet — `p:DriversLicenseDocument` is the template label that marks a topic as carrying driver's license identity data.

- `p:PassportDocument` — label for topics that carry the identity claims on a government-issued passport. Also a subclass of `p:IdentityDocument`. Declared as `template: "persona:PassportDocument"` in the topic's `mia.topics[]` entry. SHACL shape `:PassportDocumentShape` (in `cell-templates-shacl.ttl`, alongside `cat:Passport`'s template cell in `cell-templates.ttl`) targets the `p:PassportDocument` document individual and validates the holding `p:Person` via `^persona:hasIdentityDocument`:
  - **Required**: `FullName` **or** (`GivenName` + `FamilyName`); exactly one `Birthdate` (`cco:ent00000046`); exactly one Passport Number (`cco:ent00000066`); exactly one expiration date (`cco:ent00000070` → Calendar Date Identifier `cco:ont00001340`).
  - **Optional**: `AdditionalName`; issue date (`cco:ent00000069`); Issuing Jurisdiction (`cco:ent00000068`, collapsed from the former IssuingCountry); Place of Birth (`cco:ent00000067`); `p:GenderMarker`; `p:hasPhoto`.

- `p:MedicalAppointmentRecord` — label for topics that carry the claims needed to arrange a medical appointment on behalf of someone else, shared between the members coordinating that care. Not a subclass of `p:IdentityDocument`. Declared as `template: "persona:MedicalAppointmentRecord"` in the topic's `mia.topics[]` entry. SHACL shape `:MedicalAppointmentRecordShape` (in `cell-templates-shacl.ttl`, alongside `cat:MedicalAppointmentInfo`'s template cell in `cell-templates.ttl`) targets the `p:MedicalAppointmentRecord` record individual directly — the claims below are properties of the record, not of the patient's `p:Person`:
  - **Required**: exactly one `p:forPatient` link; exactly one `p:insuranceProvider`; exactly one `p:insurancePolicyNumber`.
  - **Optional**: `p:hasPrimaryCarePhysician`; `p:medicalHistoryNote`; `p:insuranceGroupNumber`; `p:preferredPharmacy`; repeatable `p:currentMedication` and `p:allergy`.

- `p:PetMedicationRecord` — label for topics that carry a pet's list of medications. Not a subclass of `p:IdentityDocument`. Declared as `template: "persona:PetMedicationRecord"` in the topic's `mia.topics[]` entry. SHACL shape `:PetMedicationRecordShape` (in `cell-templates-shacl.ttl`, alongside `cat:PetsMedications`' template cell in `cell-templates.ttl`) targets the `p:PetMedicationRecord` record individual directly — the pet has no `p:Person` individual of its own, so the medication list is a property of the record, not of a person:
  - **Required**: at least one `p:hasMedication` link, each pointing to a `p:Medication` individual.
  - Each `p:Medication` (validated by `:MedicationShape`) reuses external vocabulary wherever one fits, rather than inventing flat strings — see [Medication-Related Classes and Properties](#medication-related-classes-and-properties) below for the full rationale:
    - **Required**: at least one `p:hasActiveIngredient` (a ChEBI chemical-substance class IRI, repeatable for combination drugs); exactly one `p:hasDosageAmount` (a `p:DosageAmount` individual); exactly one `p:hasAdministration` (a `p:MedicationAdministration` individual).
    - **Optional**: `p:hasDoseForm` (a DrOn dose-form class IRI, e.g. "drug tablet" — omitted for measured liquid doses); `p:medicationBrandName`; `p:medicationManufacturer`; `p:medicationDuration` (these three stay plain strings — no reused ontology covers them).
  - `p:DosageAmount` (validated by `:DosageAmountShape`) requires exactly one of `cco:ont00001769` ("has decimal value") / `cco:ont00001773` ("has integer value"), and optionally `cco:ont00001863` ("uses measurement unit") pointing at a CCO Measurement Unit individual — omitted for a count of discrete dose-form units (tablets, capsules), since those aren't true measurement units.
  - `p:MedicationAdministration` (validated by `:MedicationAdministrationShape`, `rdfs:subClassOf` DrOn's "drug administration" class) carries optional `p:medicationFrequencyPerDay` and exactly one `BFO_0000199` ("occupies temporal region") link to a `BFO_0000038` interval carrying `cco:ent00000017`/`cco:ent00000018` ("has start/end date") — the same `AddressDesignation` temporal-interval pattern used elsewhere in this project; an absent end date means the medication is ongoing.

### Persona Ontology Files

- **`persona.ttl`** — The Persona ontology. Imports the domain ontologies above and documents which classes and properties Mia uses (required vs. optional). Defines `p:Person` (Mee-specific subclass of CCO `Person`), Mia-specific extension properties (`p:hasSocialNetwork`, `p:hasBankAccount`, etc.), and the core data model classes (physical card classes, banking classes, and others).
- **`persona-templates.ttl`** — Defines `p:PersonaTemplate` (abstract classification superclass) and the six concrete subtypes `p:BirthCertificateDocument`, `p:JSContactCard`, `p:DriversLicenseDocument`, `p:PassportDocument`, `p:MedicalAppointmentRecord`, and `p:PetMedicationRecord`. These are used as values of a topic's `mia.topics[].template` field — they classify the topic, not the `p:Person` individual inside it. Also defines `p:IdentityDocument` (superclass for government-issued identity document artifacts) and `p:hasIdentityDocument` (links a `p:Person` to a `p:IdentityDocument` individual they hold); `p:BirthCertificateDocument`, `p:DriversLicenseDocument`, and `p:PassportDocument` are subclasses of both `p:PersonaTemplate` and `p:IdentityDocument`. Also defines related designator classes (`p:DriversLicenseNumber`, `p:IssuingJurisdiction`, `p:PassportNumber`, `p:IssuingCountry`, `p:PlaceOfBirth`, `p:GenderMarker`, `p:IssueDate`, `p:Credential`, `p:WebURL`, `p:OrganizationUnit`, `p:JobTitle`), complex information classes (`p:Anniversary`, `p:PersonalInfo`), annotation properties for JSContact channel labels (`p:contactContext`, `p:phoneFeature`, `p:serviceLabel`), `p:hasPhoto`, the `p:MedicalAppointmentRecord` claim properties (`p:forPatient`, `p:hasPrimaryCarePhysician`, `p:currentMedication`, `p:allergy`, `p:medicalHistoryNote`, `p:insuranceProvider`, `p:insurancePolicyNumber`, `p:insuranceGroupNumber`, `p:preferredPharmacy`), and the `p:PetMedicationRecord`/`p:Medication` classes and properties (`p:hasMedication`, `p:Medication`, `p:hasActiveIngredient`, `p:hasDoseForm`, `p:DosageAmount`, `p:hasDosageAmount`, `p:MedicationAdministration`, `p:hasAdministration`, `p:medicationFrequencyPerDay`, `p:medicationBrandName`, `p:medicationManufacturer`, `p:medicationDuration` — see [Medication-Related Classes and Properties](#medication-related-classes-and-properties)). `owl:imports` `dron-upper.ttl` (below) in addition to being imported by `persona.ttl`, so all topics inherit these classes transitively.
- **`project_files/dron-upper.ttl`** — A hand-curated subset of [DrOn](https://github.com/mcwdsi/dron) (the Drug Ontology)'s upper module — five classes ("drug product", "active ingredient", "drug tablet", "drug capsule", "drug administration"), cited by their real upstream IRIs with real upstream labels/definitions, not a full mirror (DrOn's full distribution is ~300MB of RxNorm-derived per-product classes not relevant here). `owl:import`ed by `persona-templates.ttl`. The first non-CCO/non-`mee.foundation` external ontology this project has ever vendored.

- **`cell-templates.ttl`** — Class-level `c:Cell` templates for `cat:Category` subclasses. Holds one template cell individual per templated class: `cat:Passport`, `cat:BirthCertificate`, `cat:DriversLicense`, `cat:MedicalAppointmentInfo`, `cat:PetsMedications`. Each is pointed at by its class's own `cat:templateCell` value, which is asserted in `category.ttl` itself, alongside the class's declaration (not here) — the sole route to a template individual now, since category.ttl 1.31.0 deleted `cat:Folder` and its subclasses outright. Each individual is what Mia clones into a new cell when a cell matching that class is first created in a user's tree (Lazy Instantiation). Each is typed solely `c:TCell` — `c:TCell` and `c:ACell` are disjoint, so a template cell carries no member composition of its own, just `c:templateShape` pointing to its SHACL shape in `cell-templates-shacl.ttl`. Imports `cell.ttl` directly (not `category.ttl` — no mutual import here).

- **`cell-templates-shacl.ttl`** — SHACL shapes for birth certificate, driver's license, passport, medical appointment, and pet medication topics, each directly linked from its `cell-templates.ttl` template cell via `c:templateShape` (not merely co-located by naming convention):
  - `:BirthCertificateDocumentShape` (`t:template p:BirthCertificateDocument`) targets `p:BirthCertificateDocument` document individuals directly — all identity claims (names) are properties of the document individual, not the `p:Person`. Enforces: FullName OR (GivenName + FamilyName) required; optional AdditionalName, AlternateName, Nickname, Legal Name.
  - `:DriversLicenseDocumentShape` (`t:template p:DriversLicenseDocument`) targets `p:DriversLicenseDocument` document individuals directly. Enforces: FullName OR (GivenName + FamilyName) required; Birthdate, DriversLicenseNumber, ExpirationDateIdentifier required (1..1 each); IssuingJurisdiction, PostalAddress, and hasPhoto optional.
  - `:PassportDocumentShape` (`t:template p:PassportDocument`) targets `p:PassportDocument` document individuals directly. Enforces: FullName OR (GivenName + FamilyName) required; Birthdate, PassportNumber, ExpirationDateIdentifier required (1..1 each); IssueDate, IssuingCountry, PlaceOfBirth, GenderMarker, and hasPhoto optional.
  - `:MedicalAppointmentRecordShape` (`t:template p:MedicalAppointmentRecord`) targets `p:MedicalAppointmentRecord` record individuals directly — the claims needed to arrange the appointment are properties of the record, not of the patient's `p:Person`. Enforces: exactly one `forPatient`, `insuranceProvider`, and `insurancePolicyNumber` required; `hasPrimaryCarePhysician`, `medicalHistoryNote`, `insuranceGroupNumber`, `preferredPharmacy` optional; `currentMedication` and `allergy` repeatable.
  - `:PetMedicationRecordShape` (`t:template p:PetMedicationRecord`) targets `p:PetMedicationRecord` record individuals directly — the medication list is a property of the record, not of the pet (which has no `p:Person` individual). Enforces: at least one `hasMedication` link. `:MedicationShape` targets each linked `p:Medication` individual: at least one `hasActiveIngredient` (IRI); exactly one `hasDosageAmount` (`p:DosageAmount`) and `hasAdministration` (`p:MedicationAdministration`); optionally `hasDoseForm` (IRI), `medicationBrandName`, `medicationManufacturer`, `medicationDuration`. `:DosageAmountShape` targets `p:DosageAmount`: exactly one of "has decimal value"/"has integer value" (`sh:xone`), optionally "uses measurement unit". `:MedicationAdministrationShape` targets `p:MedicationAdministration`: optional `medicationFrequencyPerDay`; exactly one "occupies temporal region" link to a `BFO_0000038` interval.

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

`persona-shacl.ttl` runs against merged data from all topics (Tier 1 validation). Per-template SHACL files in `shacl/` run against individual topics, each isolated via `extract-topic.py` from its owning cell DataBook (Tier 2): birth certificate, JSContactCard, driver's license, passport, and medical appointment each have their own shape file and are validated separately to avoid their `sh:targetClass` constraints firing on every relevant slice in the merged dataset. See the [Validation](EXAMPLE.md#validation) section for commands.

## Organization Ontology

The Organization ontology models organizations — companies, government agencies, nonprofits, and other institutions — that participate in the Personal Data Network.

<p align="center"><img src="images/organization-ontology/organization.png" alt="Organization model"></p>

**Classes**

* `o:Organization` — an organization (company, government agency, corporation, nonprofit, etc.) on the Personal Data Network.

### Organization Ontology File

- **`organization.ttl`** — The Organization ontology.

### Organization Ontology Validation

`organization-shacl.ttl` targets `o:Organization` instances but currently has no property constraints of its own.

---

See [**EXAMPLE.md**](EXAMPLE.md) for a worked illustrative example (Alice Walker) showing how these ontologies are used together in practice, plus diagram-generation instructions and the full validation pipeline for the example dataset.
