# Cellula Ontologies

This document describes the ontologies used by Cellula, a free, open-source application under development at The Mee Foundation. The app lets the user create *cells* – private, secure collaboration spaces which can be joined by other users and/or nodes on the Mee Personal Data Network (PDN) hosted by organizations. 

The following **domain ontologies** model claims about people, organizations, and other subjects — these claims live in `g:SCGraph` instances. They import and profile existing ontologies — documenting which of their classes and properties the app requires or uses — and extending them with app-specific classes and properties

- **Persona ontology** — models a person: names, addresses, phone numbers, relationships, payment cards, and more. It is built on BFO (Basic Formal Ontology) and CCO (Common Core Ontologies) as the upper ontological foundation, and on domain ontologies that extend CCO:
  - **PersonOntology** — person, name types, parent-child relationships
  - **AddressOntology** — postal address structure
  - **StagingOntology** — staging area for terms pending promotion (phone numbers, email addresses, user accounts, etc.)
  - **AgentOntology** — agents and their properties (imported transitively via PersonOntology)
- **Organization ontology** — models organizations (companies, government agencies, non-profits, etc.) 

Also included are the Category, Cell and Graph **metadata ontologies**. A *cell* is the atomic unit of information. A cell is implemented as a filesystem folder holding exactly one cell DataBook file and potentially other (non-cell) files and folders. The parent folder and databook file together forming one atomic tree node. Cells nest inside cells, forming a tree. Cells have different types, called *Categories* described in the category ontology. A cell contains various kinds of content including markdown notes, chat streams, and other file attachments. It also contains structured information blocks (called *graphs*) whose schemas differ based on the cell's category. 

Throughout this document we use these short-hands:

- `cat:` for the `category:` namespace (`http://mee.foundation/ontologies/category#`)
- `c:` for the `cell:` namespace (`http://mee.foundation/ontologies/cell#`)
- `g:` for the `graph:` namespace (`http://mee.foundation/ontologies/graph#`)
- `p:` for the `persona:` namespace (`http://mee.foundation/ontologies/persona#`)
- `o:` for the `organization:` namespace (`http://mee.foundation/ontologies/organization#`).

See [**EXAMPLE.md**](EXAMPLE.md) for an illustration of the use of these ontologies by a hypothetical user, Alice, along with diagram-generation and validation instructions for the example dataset, and [**APP-BEHAVIOR.md**](APP-BEHAVIOR.md) for how the app behaves on top of this data — cell naming/renaming/sharing, storage, permissions, and filing heuristics.

## Category Ontology

To help the user organize their information, the app comes with a pre-defined tree structure of categories. Although the user is free to organize their cells however they like, we think many users will choose to create their own tree of cells based on the pattern of the tree of `cat:Category` classes and subclasses. Cells that are created based on a pre-defined category have a `c:origin` property whose value is that category. 

<p align="center"><img src="images/category-ontology/category.png" alt="Category hierarchy"></p>

These categories vary in scope from broad groupings of information to narrower ones. In the social domain, for example, a category might be about "People", or more narrowly about "Immediate Family", and ultimately about just one family member. All predefined categories are *symmetric*. For example, "Extended Family" is symmetric because if Alice is a member of Bob's extended family, the reverse is also always true.

The app includes two predefined `cat:Category` class hierarchies rooted in the `cat:Person` and `cat:Organization`. Some classes in this hierarchy have "starter" content pointed to via `cat:templateCell` and asserted directly in `category.ttl` alongside the class's own declaration, pointing at a `c:TemplateCell` individual defined in the companion file `cell-templates.ttl` — the *cell template* for that class.

When a new cell is created, the app clones its class's `cat:templateCell`, if it exists, into that cell's DataBook — this is how a **cell template** becomes the starter content for a newly-created cell (see [Lazy Instantiation](APP-BEHAVIOR.md#lazy-instantiation) in APP-BEHAVIOR.md).

As we've mentioned, the user is free to create cells not included in the predefined categories. These, by the way, need not be symmetric, and simply carry no `c:origin` value. The user is also free to rearrange their cells as they wish, adding new cells and moving others around. They can do this using the app or entirely as a file system operation.

### Category Properties

- **`cat:templateCell`** — links a `cat:Category` subclass directly to the `c:TemplateCell` (template cell) individual serving as its reusable template content.

### Personal Categories

`cat:Person` categories organize a person's mostly non-employment-related information:

1. **People** (`cat:People`) — people in your social or professional life. Use this category for people not otherwise tied to a specific domain — a bookkeeper you know belongs under Finances (Advisory Firms), and your primary care physician belongs under Health & Wellness (Medical > Provider > Primary Care Physician), rather than here.
    - **Immediate Family** (`cat:ImmediateFamily`) — your closest living relatives, which generally include parents, siblings, spouses/partners, and children.
    - **Extended Family** (`cat:ExtendedFamily`) — relatives outside the immediate nuclear group, such as grandparents, aunts, uncles, cousins, nieces and nephews.
    - **In-Laws / Step-Family** (`cat:InLawsStepFamily`) — relatives gained through marriage or legal guardianship, including a spouse's parents and siblings, or children from a previous relationship.
    - **Others** (`cat:Others`) — people you know socially or professionally who are not part of your family — acquaintances, friends, neighbors, or other connections.
1. **Affiliations** (`cat:Affiliations`) — a catch-all for clubs, charities, faith groups, and other group affiliations that are not covered by a more specific category (e.g. `cat:SportsEntertainment`, `cat:Food`, etc.) 
1. **Health & Wellness** (`cat:HealthWellness`) — personal health and wellness information. Medical history, allergies, medications, vaccinations, prescriptions, eyeglasses, ethnicity, gender, age.
    - **Medical** (`cat:Medical`) — medical (as opposed to dental or vision) care — diagnoses, treatments, providers, and insurance.
        - **History** (`cat:MedicalHistory`) — past diagnoses, conditions, surgeries, and treatments.
        - **Insurance** (`cat:MedicalInsurance`) — medical health insurance policies, providers, and coverage.
        - **Provider** (`cat:MedicalProvider`) — medical providers and practices you see for care.
            - **Primary Care Physician** (`cat:PrimaryCarePhysician`) — your primary care doctor, the physician you generally see first for checkups, referrals, and everyday health concerns, including name, contact information, and the name of the provider they are associated with.
            - **Medical Appointment** (`cat:MedicalAppointment`) — a medical appointment and associated information required by the provider to arrange this appointment.
    - **Dental** (`cat:Dental`) — dental care — diagnoses, treatments, providers, and insurance.
        - **History** (`cat:DentalHistory`) — past dental treatments, procedures, and conditions.
        - **Insurance** (`cat:DentalInsurance`) — dental insurance policies, providers, and coverage.
        - **Provider** (`cat:DentalProvider`) — dental providers and practices you see for care.
            - **Dentist** (`cat:Dentist`) — a dentist you see for care, including name, contact information, and the name of the provider they are associated with.
            - **Dental Appointment** (`cat:DentalAppointment`) — a dental appointment and associated information required by the provider to arrange this appointment.
    - **Vision** (`cat:Vision`) — vision and eye care — diagnoses, treatments, providers, and insurance.
        - **History** (`cat:VisionHistory`) — past eye-care prescriptions, treatments, and conditions.
        - **Insurance** (`cat:VisionInsurance`) — vision insurance policies, providers, and coverage.
        - **Provider** (`cat:VisionProvider`) — vision care providers and practices you see for care.
            - **Eye Doctor** (`cat:EyeDoctor`) — an eye doctor you see for care, including name, contact information, and the name of the provider they are associated with.
            - **Vision Appointment** (`cat:VisionAppointment`) — a vision appointment and associated information required by the provider to arrange this appointment.
    - **Fitness** (`cat:Fitness`) — general fitness and preventive physical health — exercise, gyms, trainers, and other non-clinical wellbeing information.
        - **Provider** (`cat:FitnessProvider`) — fitness providers and practices you see for care, e.g. gyms, trainers, and coaches.
            - **Personal Trainer** (`cat:PersonalTrainer`) — a personal trainer you see for care, including name, contact information, and the name of the provider they are associated with.
    - **Nutrition** (`cat:Nutrition`) — nutritionists and dietitians.
        - **History** (`cat:NutritionHistory`) — past nutritional consultations, diet plans, and dietary conditions.
        - **Provider** (`cat:NutritionProvider`) — nutritionists and dietitians you see for care.
    - **Mental Health** (`cat:MentalHealth`) — mental and behavioral health care.
        - **History** (`cat:MentalHealthHistory`) — past diagnoses, treatments, and mental health conditions.
        - **Insurance** (`cat:MentalHealthInsurance`) — mental health insurance policies, providers, and coverage.
        - **Provider** (`cat:MentalHealthProvider`) — mental health providers and practices you see for care, e.g. therapists, counselors, and psychiatrists.
            - **Therapist** (`cat:Therapist`) — a therapist you see for care, including name, contact information, and the name of the provider they are associated with.
    - **Physical Therapy** (`cat:PhysicalTherapy`) — physical therapy and rehabilitative care.
        - **History** (`cat:PhysicalTherapyHistory`) — past physical therapy treatments, injuries, and rehabilitation plans.
        - **Provider** (`cat:PhysicalTherapyProvider`) — physical therapy providers and practices you see for care.
1. **Personality** (`cat:Personality`) — self-assessments of personality, temperament, or social style — e.g. Myers-Briggs (MBTI) type, Big Five, DISC, Enneagram, or similar self-assessment instruments.
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
1. **Work** (`cat:Work`) — professional roles. Employment history, resume/CV, job level, job function, industry.
1. **Things** (`cat:Things`) — owned assets, property, vehicles, and other possessions.
    - **Vehicles** (`cat:Vehicles`) — related to owning and maintaining a vehicle. Vehicle insurance, repairs, mechanics, garages. 
1. **Travel** (`cat:Travel`) — travel plans, trips, and related information. Loyalty programs, airlines, bus lines, trains.
1. **Food** (`cat:Food`) — food preferences, dietary restrictions, favorite restaurants, recipes, shopping lists, and other food-related interests
1. **Sports & Entertainment** (`cat:SportsEntertainment`) — sports events (watching or participating) and entertainment (movies, plays, jazz clubs). Favorite teams/groups, venues, streaming services, ticketing. See `cat:Information` for other interests.
1. **Education** (`cat:Education`) — educational history and ongoing learning — schools, degrees, certifications, transcripts, and enrolled courses.
1. **Legal** (`cat:Legal`) — legal matters, contracts, agreements, trusts, wills, and professional legal relationships. Includes durable power of attorney and healthcare proxy agreements.
1. **Projects** (`cat:Projects`) — involvement in a specific project or initiative.
1. **Events** (`cat:Events`) — participation in or relationship to a specific event or gathering.
1. **Information** (`cat:Information`) — information about anything; articles, web links, documents, images. Includes graphs that interest and inspire you (e.g. drawing, painting, dancing, religion, gaming, music). See `cat:SportsEntertainment` for sports and entertainment, and `cat:Affiliations` for formal memberships tied to a hobby or interest.
1. **Government** (`cat:Government`) — government-issued credentials, tax records, and civic relationships.
    - **Federal** (`cat:Federal`) — federal government graph (e.g. passport, federal tax records).
        - **SSN** (`cat:SSN`) — social security number issued by the federal Social Security Administration.
        - **Passport** (`cat:Passport`) — passport issued by the Department of State.
    - **State** (`cat:State`) — state government graph (e.g. driver's license, state tax records).
        - **Birth Certificate** (`cat:BirthCertificate`) — a birth certificate issued by a state agency that issues and holds these records.
        - **Drivers License** (`cat:DriversLicense`) — a driver's license issued by a state agency that issues and holds these records.
    - **Municipality** (`cat:Municipality`) — municipal government graph (e.g. local permits, library card).
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
  - *Annotation properties*: `cat:templateCell` (domain `owl:Class`, range `c:TemplateCell`) — links a `cat:Category` subclass directly to its reusable template cell.

## Cell Ontology


### Introduction to Cells

A cell is a secure **container of information** that can remain private to the user or be shared with other users and/or organizations.

A regular cell may be empty or hold various kinds of information, organized into a set of tabs:

* **Members** tab:
  * Structured information (fields and values) about the members of the cell.
* **Note** tab:
  * Exactly one Markdown document about the cell. It may be blank. It may be linked to any number of other Markdown notes anywhere in the user's own tree of cells.
* **Files** tab:
  * An arbitrary number of files and sub-folders.
* **Chat** tab:
  * A chat stream shared with all members.

A **Topic Cell** adds one more tab:

* **Topic** tab:
  * Structured information about topic that is the focus of the cell. This topic could be person who is not a member of the cell, or information about a project that the members of the cell are working on (e.g. organizing a medical appointment for someone who is not a member of the cell)

The app contains two pre-defined, non-user-editable tree structures of **categories**. One is focused on helping organize a person's personal life (Family, Home, Pets, etc.) and the other their work life (Employer, Employees, etc.). Each category has a *template cell* which may contain some starter content (or may be empty) and may have a schema for the structured fields and values that a cell of this category might contain. Most cells are instantiated from a template cell, although the user may also create category-less cells if desired.

A cell has a **name**. Often this name is just a copy of the name of the category. For example if the category was "People", the cell might be called "People". However, the user can give the cell a name of their own choosing. 

A cell has a **origin**. The origin identifies the category (e.g. "People") the cell represents. For categories with a template cell, this is usually the category whose template was cloned to create the cell; a cell can also be assigned an origin directly, with no template involved.

A cell has a **creator**, which is the identity of the user who created it.

A cell can be **shared**. The creator of a cell can invite people (or organizations compatible with the Mee PDN protocols) to join the cell. When they do, they get a complete copy of the cell that is "alive" — any changes made to its contents, are continuously shared with all members. The one thing that stays independent per member is where each of them files the cell in their own tree. 

### Diving Deeper

The Cell class splits into two disjoint kinds: `c:TemplateCell`, a reusable, class-level *template* cell, and `c:MemberCell`, an *actual* cell instantiated in a user's own tree. `c:MemberCell` further specializes into `c:TopicCell` for a member cell that actually carries a `c:topic` value.

A cell is an atomic unit of information that the app manages for the user. This unit consists of a filesystem folder holding exactly one cell DataBook file, folder and file together forming one node — cells nest inside cells, forming the tree.

`c:Cell` (below) still models only the content *facet* carried by the cell DataBook file's own triples, and stores no property recording the cell's own tree position: the folder<->cell-databook pairing is always one-to-one (see [Filesystem Persistence](APP-BEHAVIOR.md#filesystem-persistence) in APP-BEHAVIOR.md), so a cell's position in the tree is simply wherever its folder currently sits — moving or renaming that folder is a pure filesystem operation that never requires updating anything asserted on the cell itself.

<p align="center"><img src="images/cell-ontology/cell.png" alt="Cell hierarchy"></p>

A cell's **files content** — everything shown in the app's **Files tab** for that cell — is every file and plain subfolder found under its own folder, to any depth, except (1) a nested folder that is itself a cell. Such a nested folder is a **descendant cell**: a separate node in the tree of cells, never counted as part of its ancestor's content even though it physically sits inside the ancestor's folder, and (2) the cell's own Markdown folder note — exactly one per cell; it is displayed in the **Note tab** for that cell (not the Files tab). Clicking a link in that note to a note that doesn't exist yet creates a new, origin-less cell for it — see [Wikilink-Triggered Cell Creation](APP-BEHAVIOR.md#wikilink-triggered-cell-creation) in APP-BEHAVIOR.md.

#### Cell Properties

- **`c:origin`** — The `cat:Category` subclass this cell was originally instantiated as, else nil. For one of the four templated classes (`cat:Passport`, `cat:BirthCertificate`, `cat:DriversLicense`, `cat:MedicalAppointment`), this is literally the class whose `c:TemplateCell` template was cloned into this cell via [Lazy Instantiation](APP-BEHAVIOR.md#lazy-instantiation) (APP-BEHAVIOR.md); for any other cell, it's simply the category the cell was created to represent, asserted directly with no template involved. Either way the value is fixed at that point — it is not re-derived from the folder's current name, so it needs no update if the folder is later renamed or moved elsewhere in the tree. When a cell is shared with another member, the recipient's app can look at this value (if not nil) and use it as a hint as to which folder in the recipient's own tree it should be filed under. Domain `c:Cell`, range `cat:Category` (referenced by name, no `owl:imports`), at most one value (0..1) — see [Cell Ontology File](#cell-ontology-file) below.

- **`c:chat`** — optional path to chat stream. Aspirational: shown in `images/cell-ontology/cell.png`'s diagram and described here for intended semantics, but not yet defined as an actual property in `cell.ttl` (see `CLAUDE.md`'s Check 12 for this open discrepancy).

### TemplateCell (Template Cell)

A cell pointed to by a `cat:Category` subclass (via `cat:templateCell`) serves as a **cell template** — a reusable, typically empty shape that the application clones into a new cell whenever a category of that class is first instantiated into a user's tree (see [Lazy Instantiation](APP-BEHAVIOR.md#lazy-instantiation) in APP-BEHAVIOR.md). Such a cell is typed `c:TemplateCell` only. An ordinary, already-instantiated cell is typed `c:MemberCell` instead, carrying real member composition, creator, and content. `c:TemplateCell` and `c:MemberCell` are disjoint: a template cell is never also typed `c:MemberCell` or any of `c:OneMember`/`c:TwoMember`/`c:ThreePlusMember`/`c:TopicCell` — see [Cell Ontology File](#cell-ontology-file) below.

#### Properties

If a `c:TemplateCell` has a `c:templateShape` value, then when the category pointing to it is instantiated (see [Lazy Instantiation](APP-BEHAVIOR.md#lazy-instantiation) in APP-BEHAVIOR.md), whatever value this property has is copied into the new `c:MemberCell`'s `c:shape`. If its `c:isTopicCell` value is `true`, the new cell is also typed `c:TopicCell` from the start.

- **`c:templateShape`** — links a `c:TemplateCell` individual directly to the `sh:NodeShape`(s) describing the content expected of a graph filed under its category — e.g. `ctpl:PassportTemplateCell` carries `pshapes:PassportDocumentShape`. An `owl:ObjectProperty`, domain `c:TemplateCell`, range `sh:NodeShape`. Makes the shape reachable by pure RDF traversal (`cat:Category` → `cat:templateCell` → `c:templateShape` → `sh:NodeShape`), not just by file co-location or naming convention. 

- **`c:isTopicCell`** — a boolean flag telling Lazy Instantiation whether the cell it clones from this template is expected to end up typed `c:TopicCell` — i.e. to carry a `c:topic` value once real content is filed under it — as opposed to staying a bare concrete member-count cell with no `c:topic`. An `owl:DatatypeProperty`, domain `c:TemplateCell`, range `xsd:boolean`, required, exactly one value — every template cell must declare it explicitly: `ctpl:MedicalAppointmentTemplateCell` and `ctpl:PetMedicationsTemplateCell` carry `true`, since a real Medical Appointment or Medications cell always ends up about a third party (Paula, Ginger) beyond its own `c:members` baseline; the other three templates carry `false`.

### MemberCell (Member Cell)

A `c:MemberCell` is a cell instantiated in a user's own tree — one of the two disjoint kinds of an abstract `c:Cell`, the other being `c:TemplateCell`. It carries `c:memberCount`, `c:creator`, `c:members`, and `c:shape`. Every cell in a user's own tree is typed `c:MemberCell`, never `c:TemplateCell` — there is no bare tree-position-only cell with no member content; a purely organizational cell with nothing substantive to say still carries a minimal stub `c:members` entry (claimed by and about `:Self`) rather than omitting member content altogether.

Reusable class-level templates (`cell-templates.ttl`) are the exception: each is typed solely `c:TemplateCell`, never `c:MemberCell` or any `c:MemberCell`-lineage class like `c:OneMember`/`c:TopicCell` — `c:TemplateCell` and `c:MemberCell` are disjoint, so a template cell carries no member composition of its own.

#### Properties

- **Subject** — not a stored property; who or what a cell's relationship is about is derived from its graph links instead. If the cell has any `c:topic` values (i.e. it's also typed `c:TopicCell`), the full set of distinct `g:subject` values among them is the answer; otherwise the answer is the full set of distinct `g:subject` values found among the cell's `c:members` (its active members). See [Members](#members) below for the worked-out cases.

- **`c:members`** — one or more values, required; It's a link to the required baseline of subject-claimant graphs (`g:SCGraph`) that hold the structured content of the cell related to the members with which the cell has been shared. Its cardinality varies by member count — see [Members](#members). Each SCGraph has a *subject* and a *claimant*. The subject is typically a person, organization, or group, but it could be any other entity the Persona ontology can describe. The claimant is the person, group or organization that is asserting the values of the claims in the container. See [Graph Ontology](#graph-ontology) for details.

- **`c:shape`** — a `owl:ObjectProperty`, domain `c:MemberCell`, range `sh:NodeShape`. Optional; most actual cells carry no `c:shape` value. Links a `c:MemberCell` individual directly to the `sh:NodeShape`(s) validating that specific cell's own content, as opposed to `c:templateShape`, which describes what a graph filed under some other, template category should look like. Populated by copy-on-clone: when Lazy Instantiation clones a `c:TemplateCell` into a new `c:MemberCell` — whatever `c:templateShape` value the `TemplateCell` carried is copied into the clone's `c:shape` with the same validation expectation.

- **`c:creator`** — required, exactly one value. Identifies who created this cell's content: a single `p:Person` or `o:Organization`. 

- **`c:memberCount`** — the concrete `c:MemberCell` subtype this DataBook instantiates: `c:OneMember`, `c:TwoMember`, or `c:ThreePlusMember`. Value is the class itself (e.g. `mia.memberCount: "c:OneMember"`). See [Members](#members) above.

#### Members

Every `c:MemberCell` has a `c:memberCount`, which is a tally of the number of members of the cell. There are three concrete types: `c:OneMember` (a cell created by the user and not shared with any other member), `c:TwoMember` (the user plus exactly one other member), and `c:ThreePlusMember` (the user plus two or more other members).

Every `c:MemberCell` carries one or more `c:members` links (the required baseline of graph containers backing its content, one or more per member); a `c:MemberCell` that also carries one or more `c:topic` links (graphs beyond that baseline) is additionally typed `c:TopicCell` — see [TopicCell](#topiccell-topic-cell) below. The cardinality of each is shown in the table below:

| Property     | OneMember | TwoMember | ThreePlusMember |
|--------------|-----------|-----------|-----------------|
| `c:members`  | 1         | 2..4      | 3..N            |
| `c:topic`    | 0+        | 0+        | 0+              |

The `c:members` and `c:topic` are lists of `g:SCGraphs`. See the [Graph Ontology](#graph-ontology) for details.

### Topic Cell

A `c:TopicCell` is a subclass of `c:MemberCell` for a member cell that adds the concept of a *topic* focus for the cell carried by one or more `c:topic` values — additional `g:SCGraph` containers beyond the cell's `c:members` baseline. This focus is typically about a third party who is not a member of the cell, but may be about any topic that can be represented by the Persona Ontology.

#### Properties

- **`c:topic`** — one or more values, required once a cell is typed `c:TopicCell` at all (no upper bound). Link to one or more additional subject-claimant graphs beyond those referenced by `c:members`. Domain `c:TopicCell`.

### Representative Cells

The diagram below shows six representative cells.

<p align="center"><img src="images/cat-cell-graph.png" alt="Cells, categories, and graphs"></p>

Each cell's fill color and cell name text color follow a folder-icon display convention — see [Filesystem Persistence](APP-BEHAVIOR.md#filesystem-persistence) in APP-BEHAVIOR.md for the full rules. In short: tan fill for `People`/`Bob Johnson`/`BHS`/`Medical Appointment` (Person-rooted origin), light blue for `Employee` (Organization-rooted origin), purple for `Friends` (no origin at all, Custom); `Bob Johnson`'s origin is `cat:Others`, so its name doesn't match the label and is shown in black text, while `People`'s name matches its own origin's label and is shown in green. This is purely a display choice about the cell's folder icon and name, not a separate RDF property.

Regular cells contain one of more circle that represent structured information about the cell members. A Topic Cell also contains a square "topic" that contains structured information about a non-member person, organization or any other topic.

Both square topics and circular members, the fill color marks who claimed that graph: green fill for a graph claimed by someone other than the self (another person or an `o:Organization`); a dashed/outlined (unfilled) shape for a graph claimed by the self (the user). For example the `Bob Johnson` cell has four circles — two claimed by Bob, two claimed by Self. The `BHS` cell, a Topic Cell, has three circles (Self, Bob, and BHS's own member graphs) plus one square (BHS's organization profile, linked via `c:topic`). The `Medical Appointment` cell shows that `c:topic` isn't capped at one value: it has two squares (one claimed by each side) alongside its two member circles.

A class's template cell (`cell-templates.ttl`) may also carry validation metadata declared in the paired `cell-templates-shacl.ttl`. This metadata lives on the class-level template only.

#### Properties

The following properties are defined in `cell.ttl` and represented as `mia.` YAML fields in cell DataBooks:

| YAML field | Ontology property | Cardinality | Meaning |
|------------|-------------------|-------------|---------|
| `mia.origin` | `c:origin` | 0..1 | The `cat:Category` subclass this cell was originally instantiated as, as a class value (e.g. `"cat:Others"`); absent otherwise. Fixed at creation, not re-derived from the folder's current name. A hint for a recipient's app when this cell is shared with another member |
| `mia.memberCount` | `c:memberCount` | 1 | The concrete `c:MemberCell` subclass this DataBook instantiates, as a class value (e.g. `"c:OneMember"`) |
| `mia.creator` | `c:creator` | 1 | Who created this cell's content — a `p:Person` or `o:Organization` |
| `mia.shape` | `c:shape` | 0..1 | Optional `sh:NodeShape` validating this specific cell's own content directly |

There is no `mia.subject` field — who or what a cell's content is about is derived from `mia.members`/`mia.graph` rather than asserted independently (see [Graph Link Properties](#graph-link-properties) below).

#### Graph Link Properties

Each cell DataBook carries one or more `c:members` links (the required per-member baseline) and, on the minority of cells typed `c:TopicCell`, one or more `c:topic` links (graphs beyond that baseline) to the actual graph DataBook container(s) backing its content:

| Property | Value | Cardinality | Meaning |
|----------|-------|-------------|---------|
| `c:members` | `g:SCGraph` | 1 on `OneMember`; 2..4 on `TwoMember`; 3..N on `ThreePlusMember` (required) | The required baseline of self-vs-other classified graphs backing this cell's content — at least one per member in the relationship (up to all four self-vs-other combinations for `TwoMember`) — distinguished by each linked graph's own `subject`/`claimant` combination rather than by separate properties or classes |
| `c:topic` | `g:SCGraph` | 0 on a bare `MemberCell`; 1+ (required, no upper bound) once the cell is typed `c:TopicCell` | One or more additional graphs beyond the `c:members` baseline |

How a cell maps onto an actual filesystem folder — naming, origin-derived fill color, custom-cell identification, and the cell DataBook/folder-note file layout — plus how cell naming, renaming, and sharing work (who can rename a cell, sibling-uniqueness collision handling, and the bare-`c:TwoMember`-cell (not also `c:TopicCell`) per-member-name exception) are app/display-level behavior, not ontology rules; see [Filesystem Persistence](APP-BEHAVIOR.md#filesystem-persistence) and [Naming, Renaming, and Sharing](APP-BEHAVIOR.md#naming-renaming-and-sharing) in APP-BEHAVIOR.md.

### Cell Ontology File

**`cell.ttl`** — The Cell ontology, defining:
  - *Classes*: `c:Cell` (formerly `c:Parties`), splitting into two disjoint kinds, `c:TemplateCell` (abstract, reusable class-level template) and `c:MemberCell` (abstract, actual cell instantiated in a user's own tree) — a cell is always exactly one, never both (`owl:disjointWith`); `c:OneMember`, `c:MultiMember` (abstract), `c:TwoMember`, `c:ThreePlusMember`, and `c:TopicCell` — all subclasses of `c:MemberCell` rather than `c:Cell` directly (cell.ttl 3.7.0; `c:TopicCell` added cell.ttl 3.37.0, the subclass for a member cell that actually carries a `c:topic` value).
  - *Annotation properties*: `c:label` (default display name for a concrete `c:Cell` subtype, asserted on the class), `c:abstract` (marks a class as not directly instantiated in DataBooks). There is no `c:subject` annotation property — who or what a cell's relationship is about is derived from `c:members`/`c:topic` rather than independently asserted (see [Graph Link Properties](#graph-link-properties)).
  - *Object properties*: `c:origin` (domain `c:Cell`, range `cat:Category` — added cell.ttl 3.20.0; the `cat:Category` subclass this cell was originally instantiated as, else nil; fixed at creation, not re-derived from the folder's current name; at most one value); `c:templateShape` (domain `c:TemplateCell`); `c:memberCount`/`c:creator`/`c:members`/`c:shape` (domain `c:MemberCell` — every cell in a user's own tree is typed `c:MemberCell`, never `c:TemplateCell`, so every such cell carries all of these; the reusable class-level templates in `cell-templates.ttl` are typed `c:TemplateCell` instead and carry none of them); `c:topic` (domain `c:TopicCell`, the subclass reserved for cells that actually carry it).
  - *Datatype properties*: `c:isTopicCell` (domain `c:TemplateCell`, range `xsd:boolean` — added cell.ttl 3.38.0; required, exactly one value; flags whether Lazy Instantiation's clone of this template should be typed `c:TopicCell`).
  `c:creator`'s range is a union of `p:Person` and `o:Organization` — the same union-range pattern used by `g:claimant` (see [Graph Ontology File](#graph-ontology-file)). `c:memberCount`'s range is `c:MemberCell` itself: its value is the concrete subclass (`c:OneMember`/`c:TwoMember`/`c:ThreePlusMember`), not a string — class-value punning; `c:origin`'s range `cat:Category` uses this same punning — its value is the concrete leaf subclass (e.g. `cat:Others`), not a string. `c:templateShape`'s and `c:shape`'s ranges are both `sh:NodeShape` — see [Cell Ontology](#cell-ontology) above — but on different domains: `templateShape` describes what a graph filed under a *template* category should look like, while `shape` validates an *actual* cell's own content directly. `c:members`/`c:topic`'s range is `g:SCGraph` — the former is the required per-member baseline (split from the single `c:graphs` property, cell.ttl 3.14.0), the latter one or more additional graphs beyond it, present only on `c:TopicCell`. `c:Cell` carries no property pointing back to its own folder at all — a cell IS its folder together with this DataBook file, not two separately-associated things, so there is no distinct folder individual to point at (category.ttl 1.31.0 deleted `cat:Folder` and its subclasses outright); `c:origin`'s range is the classificatory `cat:Category`, not a tree position — it records what kind of thing a cell is, not where it lives, letting a recipient's app use it as a filing hint when a cell is shared with another member.
  These terms are referenced by name in the YAML front matter of each cell DataBook file. `cell.ttl` imports `graph.ttl` (for `c:members`/`c:topic`'s range, `g:SCGraph`); `graph.ttl` in turn imports `cell.ttl` back, solely to reuse `c:abstract` — a mutual import. `category.ttl` also imports `cell.ttl` (to reuse `c:abstract`, and by name in `c:origin`'s doc comments), but `cell.ttl` does not import `category.ttl` back — `c:origin`'s range `cat:Category` is referenced by name only, exactly like `cell.ttl` already does for `p:Person`/`o:Organization` in `c:creator`'s range, without importing `persona.ttl` or `organization.ttl` — the same choice `graph.ttl` makes for `g:claimant`.

**`cell-shacl.ttl`** — SHACL shapes for cell DataBook instances, split across shapes matching `cell.ttl`'s two-kind split: `:CellShape` (target `c:Cell`) constrains `c:origin` to at most one value (0..1, added cell-shacl.ttl 3.15.0 — not constrained via `sh:class cat:Category`, since a legal value is the concrete leaf subclass itself, never `rdf:type cat:Category`, mirroring `c:memberCount`'s own identical unconstrained, class-value-punning treatment above; its earlier `c:folder` cardinality constraint was removed outright in cell-shacl.ttl 3.17.0, once `c:folder` itself was removed from `cell.ttl`) and requires `rdf:type` to be exactly one of `c:TemplateCell`/`c:MemberCell` (`sh:xone`, added cell-shacl.ttl 3.24.0, mirroring `cell.ttl`'s `owl:disjointWith` — never both, never neither); `:TemplateCellShape` (target `c:TemplateCell`) constrains `c:templateShape` to at most one value and `c:isTopicCell` to exactly one value, which must be a boolean (added cell-shacl.ttl 3.26.0, tightened to required in cell-shacl.ttl 3.27.0); `:MemberCellShape` (target `c:MemberCell`) constrains `c:creator` to exactly one value, which must be a `p:Person` or `o:Organization`, `c:memberCount` to exactly one value which must be the class `c:OneMember`, `c:TwoMember`, or `c:ThreePlusMember`, and `c:shape` to at most one value. `:TopicCellShape` (target `c:TopicCell`, added cell-shacl.ttl 3.25.0) constrains `c:topic` to at least one value (no upper bound), each of which must be a `g:SCGraph` — this is what makes a cell's derived subject well-defined whenever `c:topic` is present (see [Graph Link Properties](#graph-link-properties)). Cardinality for `c:members` is enforced instead by three shapes targeting `cell:OneMember`/`cell:TwoMember`/`cell:ThreePlusMember` directly (`:OneMemberShape`, `:TwoMemberShape`, `:ThreePlusMemberShape`, since `yaml-to-rdf.py` types every cell individual with its concrete member class) — exactly 1/2..4/at least 3 respectively, replacing the single `c:graphs` property's old blanket "at least one, no upper bound" rule, which didn't vary by member count. `c:templateShape`/`c:shape` are deliberately not constrained to `sh:class sh:NodeShape`: the individuals they point at are only typed `sh:NodeShape` in `cell-templates-shacl.ttl`, which Tier 1 validation deliberately excludes from its merged-data run (see [Validation](EXAMPLE.md#validation)), so that constraint would spuriously fail there. There is no `c:subject` shape — that property no longer exists.

### Cell Ontology Validation

Cell DataBook instances are validated by `cell-shacl.ttl`: `origin`/`memberCount`/`members`/`graph`/`creator`/`shape` exist solely as `mia.` YAML frontmatter fields on cell DataBooks, so `yaml-to-rdf.py` synthesizes the corresponding `c:` triples (`rdf:type c:Cell`, `c:origin` if present, plus `rdf:type c:MemberCell`/the concrete member class/`c:memberCount`/`c:creator`/`c:members`/`c:shape` once `memberCount` is set, and `rdf:type c:TopicCell`/`c:topic` once `mia.graph` is present) directly from frontmatter, letting `:CellShape`/`:MemberCellShape`/`:TopicCellShape`/the per-member-count shapes actually fire against real instance data — see [Tier 1](EXAMPLE.md#validation). `c:origin` is asserted on every `c:Cell` regardless of kind, since its domain is `c:Cell` itself, not `c:MemberCell`. Every cell-databook carries a `mia.memberCount` value, so `yaml-to-rdf.py` always types it `rdf:type c:MemberCell` — satisfying `:CellShape`'s `c:TemplateCell`/`c:MemberCell` `sh:xone` requirement via the `c:MemberCell` branch — so `:MemberCellShape`'s and the per-member shapes' required `c:members` always apply; a category node with nothing substantive to say uses a minimal stub `c:members` entry rather than omitting member content (and, having no third party to link, stays a bare `c:MemberCell`, never also `c:TopicCell`). (`c:TemplateCell` individuals live only in `cell-templates.ttl`, a plain `.ttl` file rather than a DataBook excluded from Tier 1's merge entirely — see [Validation](EXAMPLE.md#validation) — so they need no such synthesis either.) There is no `mia.subject`/`c:subject` to synthesize — a cell's subject is derived, not stored.

## Graph Ontology

The graph ontology defines *graphs* (`g:Graph`) — named graphs containing sets of claims about some resource; that resource need not be a person (see `g:subject` below). Graphs are referenced by cells described in the Cell Ontology.

### Graphs

A graph is a container of structure information about another person, organization or any other topic . This information is expressed as a named graph of triples — typically using the Persona and Organization ontologies when the graph is about a person, or organization, though the ontology does not require this — and stored in a **[DataBook](https://github.com/w3c-cg/holon/tree/main/architectures/databook)** (`.databook.md`) file that describes one facet of its subject (called the `subject` of the graph). These claims may have originated from other graphs about the same subject. 

<p align="center"><img src="images/graph-ontology/graph.png" alt="graph ontology"></p>

One property applies to every `g:Graph`:

**`g:template`** — present only on graphs that contain instances of a template; its value is the name of a `p:PersonaTemplate` subclass (e.g. `"persona:BirthCertificateDocument"`, `"persona:JSContactCard"`, `"persona:DriversLicenseDocument"`, `"persona:PassportDocument"`, `"persona:MedicalAppointmentRecord"`).

A graph carries no field pointing back at the cell that references it — that link is asserted only on the cell side, via `c:members`/`c:topic` (see the Cell Ontology section above).

Two more properties apply to every graph linked from a cell, since every `c:members`/`c:topic` value is classified as `g:SCGraph`:

**`g:subject`** — The resource the graph is about. Value is any resource IRI — the ontology does not require it to be a `p:Person` or `o:Organization`, though in this example every `subject` value happens to be one of those two:
- `:Self` — the graph is about the user.
- a named individual of `p:Person` — the graph is about another user.
- a named individual of `o:Organization` — the graph is about an organization (legal corporation or government agency).

**`g:claimant`** — Who is making the claim. Values are local IRIs of `p:Person` or `o:Organization` individuals:
- `:Self` — the user that is entering the data, even if the underlying information originates from some other party such as a company, government agency, or another person.
- a named individual of class `p:Person` — another user is claiming the data directly.
- a named individual of class `o:Organization` — an organization is claiming the data.

The diagram below shows four kinds of graphs related to a hypothetical user, Alice, and her interactions with a Department of Motor Vehicles (DMV) agency. Across the top are two graphs where the DMV itself is the subject, and at the bottom where Alice is the subject. At the left are graphs where Alice has made the claims (e.g. Alice's own app instance has written the claims into the graph) and at the right are graphs where the DMV as the "other" has written the claims. 

<p align="center"><img src="images/graph-ontology/quadrants.png" alt="a quadrant of graph types"></p>

The lower left shows a graph that Alice might share with other people or companies. In it, she claims that her driver's license number is S43228943, having copied that number from her physical driver's license. The graph in the lower right carries the same information as the lower left, but because it is being claimed by the DMV it is more likely to be trusted by a recipient (especially if this information is conveyed via secure channel and the claims are cryptographically bound to the identity of the DMV).


### Graph Ontology File

**`graph.ttl`** — the Graph ontology, defines:
  - *Classes*: `g:Graph`, `g:SCGraph` (Subject-Claimant graph; the concrete class every self-vs-other classified graph is typed as directly — it has no subclasses; carries the `g:subject`/`g:claimant` annotations — every graph reachable from a cell, via `c:members`/`c:topic`, is a `g:SCGraph`).
  - *Annotation properties*: `g:template` (domain `g:Graph`), `g:claimant` (range a union of `p:Person`, `o:Organization`), `g:subject` (domain `g:SCGraph`; range `xsd:anyURI` — any resource IRI, not necessarily a `p:Person`/`o:Organization`).
  These terms are referenced by name in each graph's `mia.graphs[]` entry, inside its owning cell-databook file. `graph.ttl` imports `cell.ttl` to reuse `c:abstract` on `g:Graph`/`g:SCGraph`.

**`graph-shacl.ttl`** — SHACL shapes for graph instances: `:SCGraphShape` (target `g:SCGraph`) constrains `g:claimant` to exactly one value, which must be a `p:Person` or `o:Organization`, and `g:subject` to exactly one value, which must be an IRI.

### Graph Ontology Validation

`graph-shacl.ttl`'s `:SCGraphShape` (see above) targets `g:SCGraph`, but that typing is itself only ever asserted via the `claimant`/`subject` fields of that entry, never as a literal `rdf:type g:SCGraph` triple in the graph's own extracted Turtle body. `yaml-to-rdf.py` synthesizes it directly from the cell-databook's frontmatter — `rdf:type g:SCGraph` plus `g:claimant`/`g:subject`, asserted on the graph's plain `id` (the `mia.graphs[].id` value), not the `#graph`-suffixed `graph.named_graph` IRI (see `graph.ttl` 1.18.0) — so `:SCGraphShape` actually fires against real instance data; see [Tier 1](EXAMPLE.md#validation). The remaining classification facts are synthesized the same way from the cell-databook's frontmatter: `origin`/`memberCount`/`members`/`graph`/`creator`/`shape` (see [Cell Ontology Validation](#cell-ontology-validation)).

## Persona Ontology

The Persona ontology defines a formal, machine-readable model of a person. It is used by triples stored in `g:Graph` instances. 

We represent a person with the `p:Person` class — an app-specific subclass of CCO `Person` (`cco:ont00001262`).  The user's own `p:Person` individual always uses the IRI `:Self` across all of their graphs; other people, groups, and organizations are assigned locally-minted named IRIs (e.g. `:Bob_Johnson`). `:Self`'s type declaration (`rdf:type owl:NamedIndividual, persona:Person`) is asserted in `example/graphs/self.ttl` (see the [Validation](EXAMPLE.md#validation) section for how `self.ttl` is merged in alongside every embedded graph).

<p align="center"><img src="images/persona-ontology/persona.png" alt="Persona model"></p>

The persona ontology is used to describe the contents of **graphs** of **cells** (see [Cell Ontology](#cell-ontology) and [Graph Ontology](#graph-ontology)). These graphs, when describing people, function as *named-graph slices* — each is an independent facet of an identity in a specific cell context, carrying the claims relevant to that graph: names, addresses, phone numbers, SSNs, physical characteristics, parent-child relationships, social connections, payment cards, and more. The Persona ontology reuses existing well-known ontologies wherever possible and defines new terms only where no suitable existing term exists.

### Key Properties and Classes

This section describes the most fundamental properties and classes in the Persona ontology. A person's identity data is spread across multiple named-graph slices — each a graph embedded in some cell-databook — each containing one `p:Person` individual. The user's slices share the IRI `:Self`; each other person's slices share their locally-assigned named IRI.

**Classes:**

- `p:Person` — an app-specific subclass of CCO `Person` (`cco:ont00001262`). Each graph (named-graph slice) contains exactly one `p:Person` individual. The user's own `p:Person` always uses the IRI `:Self`, shared across all of their graphs. Other people, groups, and organizations are assigned locally-minted named IRIs (e.g. `:Bob_Johnson`, `:Paula_Walker`). `:Self` is a local IRI and is never exposed externally over the PDN, so there are no collisions between instances of the app. All identity data — names, identifiers, addresses, social networks, payment cards, and more — attaches to this individual.

### Social Classes and Properties

This section describes classes and properties related to a person's social network.

**Classes:**

- `cco:ont00001183` — Social Network

**Properties:**

- `p:hasSocialNetwork` — a social network — other people known by the `p:Person` carrying the social network. The holder is not included as a member part of the social network object, but *is* considered to be a part of it by virtue of holding the network entity.
- `BFO_0000115` — has member part. Links to `p:Person` members of this network.

#### Named Graph Scoping and Graph-Specific Membership

A `BFO_0000115` (has member part) triple on a Social Network individual — for example, `:Alice_Family_Network BFO_0000115 :Paula_Walker` in a graph about Alice's immediate family — targets `:Paula_Walker` as a person entity, not as a graph-specific slice of her data. The named graph architecture provides the isolation: that triple lives inside its own named graph, and when an application needs "Paula Walker's family graph data" it queries that graph together with Paula's own family graph, rather than the full merged dataset. (See graphs #21 and #5 in the [Illustrative Example](EXAMPLE.md#illustrative-example-alice) for the concrete instance of this pattern.)

This is the correct design for three reasons:

- **BFO semantics**: changing the range of `BFO_0000115` to a DataBook document IRI (e.g. `<http://www.example.org/mia/graphs/graph-07>`) would be a semantic error — the range of `has member part` must be a continuant (a person or group), not a document.
- **Model simplicity**: introducing graph-specific "view" individuals (e.g. `:Paula_Walker_Family`) would reintroduce the layered complexity that the removal of `p:Persona` was designed to eliminate.
- **Tooling maturity**: annotating the triple with RDF-star (`<< :Alice_Family_Network BFO_0000115 :Paula_Walker >> mia:inContext <...>`) is a valid future option, but is not yet supported by Protégé and remains non-standard.

The practical implication is that **Tier 1 validation** (which merges all graphs) correctly finds all reachability links across the full dataset, while **application queries** that display a social network's members should join against specific graph named graphs rather than the full triplestore merge.

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

- `is carrier of` (from BFO) — used to link a physical card to its corresponding `p:Person` in another graph.
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

- `p:PetMedicationRecord` — subclass of `p:PersonaTemplate`; template label for a graph that carries a pet's list of medications, and also the class of the record individual itself (a pet has no `p:Person` individual of its own, so `p:hasMedication` links hang off this record rather than off a person).
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

### Personality-Related Classes and Properties

This section describes the class and properties, defined in `persona-templates.ttl`, that model a self-assessed personality result from a named framework (MBTI, Big Five, DISC, Enneagram, etc.).

**Classes:**

- `p:PersonalityAssessment` — a self-assessment of personality, temperament, or social style from a named framework.

**Properties:**

- `p:hasPersonalityAssessment` — links a `p:Person` to one of its `p:PersonalityAssessment` individuals; repeatable (a person may record results from more than one framework).
- `p:personalityFramework` — the named framework or instrument (e.g. `"MBTI"`, `"Big Five"`, `"DISC"`, `"Enneagram"`) (domain `p:PersonalityAssessment`).
- `p:personalityResult` — the self-assessed result or type code within that framework, e.g. `"INFJ"` (domain `p:PersonalityAssessment`).
- `p:personalityAssessmentDate` — the date the self-assessment was taken or last confirmed (domain `p:PersonalityAssessment`).

### Modeling Details

This section describes a few details related to modeling names and addresses.

**Peer name pattern**: All name types (FullName, GivenName, FamilyName, AlternateName) connect directly to a `p:Person` via `designated by` (`ont00001879`). They are siblings, not nested under a PersonName parent. Legal names belong to the birth certificate graph (annotated `g:template p:BirthCertificateDocument`); a preferred/goes-by name (AlternateName) belongs to each social or professional graph where it applies.

**Address history**: Each address graph carries a `p:Person` with a USPostalAddress and an `AddressDesignation` with a `TemporalInterval` (start date required; no end date = current address).

### Persona Templates

`p:PersonaTemplate` is an abstract classification class that serves as the common superclass for all reusable, graph-type-specific template labels. These labels are defined in `persona-templates.ttl`. A graph declares its template as the `template` field of its `mia.graphs[]` entry (inside its owning cell DataBook's front matter) rather than by typing its `p:Person` individual. 

Five of the six per-template SHACL shapes (`p:BirthCertificateDocument`, `p:DriversLicenseDocument`, `p:PassportDocument`, `p:MedicalAppointmentRecord`, `p:PetMedicationRecord`) live in `cell-templates-shacl.ttl`, each directly linked from its class-level `c:TemplateCell` template (in `cell-templates.ttl`) via `c:templateShape` (`cell.ttl`) — so the shape is reachable by RDF traversal from the corresponding `cat:Category` class (`cat:BirthCertificate`, `cat:DriversLicense`, `cat:Passport`, `cat:MedicalAppointment`, `cat:PetsMedications`) via `cat:templateCell` — see [Lazy Instantiation](APP-BEHAVIOR.md#lazy-instantiation) in APP-BEHAVIOR.md; `p:JSContactCard`'s shape remains a standalone file in `shacl/`, since it's reused across many unrelated tree positions with no single `cat:Category` class of its own to attach to.

<p align="center"><img src="images/persona-ontology/persona-templates.png" alt="persona templates model"></p>

**Government-issued identity documents** — `p:BirthCertificateDocument`, `p:DriversLicenseDocument`, and `p:PassportDocument` are subclasses of both `p:PersonaTemplate` (template label use) and `p:IdentityDocument` (artifact instance use). `p:IdentityDocument` is the class for government-issued documents that formally identify a person. The property `p:hasIdentityDocument` (domain: `p:Person`, range: `p:IdentityDocument`) links a person to the government document they hold. Each government-ID graph declares one named individual of the document type and links it from `:Self`. `p:JSContactCard` is a format label only — not a government-issued document — and is a subclass of `p:PersonaTemplate` only.

The six currently defined subclasses of `p:PersonaTemplate` are:

- `p:BirthCertificateDocument` — label for graphs that carry a person's legal birth name record as issued by a state agency. Also a subclass of `p:IdentityDocument`. Declared as `template: "persona:BirthCertificateDocument"` in the graph's `mia.graphs[]` entry. SHACL shape `:BirthCertificateDocumentShape` (in `cell-templates-shacl.ttl`, alongside `cat:BirthCertificate`'s template cell in `cell-templates.ttl`) targets the `p:BirthCertificateDocument` document individual and validates the holding `p:Person` via `^persona:hasIdentityDocument`:
  - **Required**: either a `FullName` designator **or** both a `GivenName` and a `FamilyName` designator (via `designated by`, `ont00001879`) — expressed with `sh:or`.
  - **Optional**: `AdditionalName` (middle name), `AlternateName` (e.g. maiden name), `Nickname`, and `Legal Name` designators.

- `p:JSContactCard` — label for graphs that carry professional contact details in the JSContact (RFC 9553) format. A digital contact format (RFC 9553) — not a government-issued identity document, and therefore not a subclass of `p:IdentityDocument`. Declared as `template: "persona:JSContactCard"` in the graph's `mia.graphs[]` entry. SHACL shape `:JSContactCardPersonShape` (in `shacl/jscontactcard-shacl.ttl`) enforces:
  - **Required**: exactly one `OrganizationName` designator; at least one `Email` or `TelephoneNumber` designator.
  - **Optional**: all name components, `OrganizationUnit`, `JobTitle`, addresses, online services, anniversaries, personal info, photo.
  - **Max 1** on all single-valued name and organization components.
  See the [JSContact field coverage table](#contact-related-classes-and-properties) above for the complete mapping.

- `p:DriversLicenseDocument` — label for graphs that carry the identity claims on a state-issued driver's license. Also a subclass of `p:IdentityDocument`. Declared as `template: "persona:DriversLicenseDocument"` in the graph's `mia.graphs[]` entry. SHACL shape `:DriversLicenseDocumentShape` (in `cell-templates-shacl.ttl`, alongside `cat:DriversLicense`'s template cell in `cell-templates.ttl`) targets the `p:DriversLicenseDocument` document individual and validates the holding `p:Person` via `^persona:hasIdentityDocument`:
  - **Required**: `FullName` **or** (`GivenName` + `FamilyName`); exactly one `Birthdate` (`cco:ent00000046`); exactly one Driver's License Number (`cco:ent00000065`); exactly one expiration date (`cco:ent00000070` → Calendar Date Identifier `cco:ont00001340`).
  - **Optional**: `AdditionalName`; Issuing Jurisdiction (`cco:ent00000068`); `PostalAddress`; `p:hasPhoto`.
  Note: `p:PhysicalDriversLicense` (in `persona.ttl`) models the physical card object held in a wallet — `p:DriversLicenseDocument` is the template label that marks a graph as carrying driver's license identity data.

- `p:PassportDocument` — label for graphs that carry the identity claims on a government-issued passport. Also a subclass of `p:IdentityDocument`. Declared as `template: "persona:PassportDocument"` in the graph's `mia.graphs[]` entry. SHACL shape `:PassportDocumentShape` (in `cell-templates-shacl.ttl`, alongside `cat:Passport`'s template cell in `cell-templates.ttl`) targets the `p:PassportDocument` document individual and validates the holding `p:Person` via `^persona:hasIdentityDocument`:
  - **Required**: `FullName` **or** (`GivenName` + `FamilyName`); exactly one `Birthdate` (`cco:ent00000046`); exactly one Passport Number (`cco:ent00000066`); exactly one expiration date (`cco:ent00000070` → Calendar Date Identifier `cco:ont00001340`).
  - **Optional**: `AdditionalName`; issue date (`cco:ent00000069`); Issuing Jurisdiction (`cco:ent00000068`, collapsed from the former IssuingCountry); Place of Birth (`cco:ent00000067`); `p:GenderMarker`; `p:hasPhoto`.

- `p:MedicalAppointmentRecord` — label for graphs that carry the claims needed to arrange a medical appointment on behalf of someone else, shared between the members coordinating that care. Not a subclass of `p:IdentityDocument`. Declared as `template: "persona:MedicalAppointmentRecord"` in the graph's `mia.graphs[]` entry. SHACL shape `:MedicalAppointmentRecordShape` (in `cell-templates-shacl.ttl`, alongside `cat:MedicalAppointment`'s template cell in `cell-templates.ttl`) targets the `p:MedicalAppointmentRecord` record individual directly — the claims below are properties of the record, not of the patient's `p:Person`:
  - **Required**: exactly one `p:forPatient` link; exactly one `p:insuranceProvider`; exactly one `p:insurancePolicyNumber`.
  - **Optional**: `p:hasPrimaryCarePhysician`; `p:medicalHistoryNote`; `p:insuranceGroupNumber`; `p:preferredPharmacy`; repeatable `p:currentMedication` and `p:allergy`.

- `p:PetMedicationRecord` — label for graphs that carry a pet's list of medications. Not a subclass of `p:IdentityDocument`. Declared as `template: "persona:PetMedicationRecord"` in the graph's `mia.graphs[]` entry. SHACL shape `:PetMedicationRecordShape` (in `cell-templates-shacl.ttl`, alongside `cat:PetsMedications`' template cell in `cell-templates.ttl`) targets the `p:PetMedicationRecord` record individual directly — the pet has no `p:Person` individual of its own, so the medication list is a property of the record, not of a person:
  - **Required**: at least one `p:hasMedication` link, each pointing to a `p:Medication` individual.
  - Each `p:Medication` (validated by `:MedicationShape`) reuses external vocabulary wherever one fits, rather than inventing flat strings — see [Medication-Related Classes and Properties](#medication-related-classes-and-properties) below for the full rationale:
    - **Required**: at least one `p:hasActiveIngredient` (a ChEBI chemical-substance class IRI, repeatable for combination drugs); exactly one `p:hasDosageAmount` (a `p:DosageAmount` individual); exactly one `p:hasAdministration` (a `p:MedicationAdministration` individual).
    - **Optional**: `p:hasDoseForm` (a DrOn dose-form class IRI, e.g. "drug tablet" — omitted for measured liquid doses); `p:medicationBrandName`; `p:medicationManufacturer`; `p:medicationDuration` (these three stay plain strings — no reused ontology covers them).
  - `p:DosageAmount` (validated by `:DosageAmountShape`) requires exactly one of `cco:ont00001769` ("has decimal value") / `cco:ont00001773` ("has integer value"), and optionally `cco:ont00001863` ("uses measurement unit") pointing at a CCO Measurement Unit individual — omitted for a count of discrete dose-form units (tablets, capsules), since those aren't true measurement units.
  - `p:MedicationAdministration` (validated by `:MedicationAdministrationShape`, `rdfs:subClassOf` DrOn's "drug administration" class) carries optional `p:medicationFrequencyPerDay` and exactly one `BFO_0000199` ("occupies temporal region") link to a `BFO_0000038` interval carrying `cco:ent00000017`/`cco:ent00000018` ("has start/end date") — the same `AddressDesignation` temporal-interval pattern used elsewhere in this project; an absent end date means the medication is ongoing.

### Persona Ontology Files

- **`persona.ttl`** — The Persona ontology. Imports the domain ontologies above and documents which classes and properties the app uses (required vs. optional). Defines `p:Person` (Mee-specific subclass of CCO `Person`), app-specific extension properties (`p:hasSocialNetwork`, `p:hasBankAccount`, etc.), and the core data model classes (physical card classes, banking classes, and others).
- **`persona-templates.ttl`** — Defines `p:PersonaTemplate` (abstract classification superclass) and the six concrete subtypes `p:BirthCertificateDocument`, `p:JSContactCard`, `p:DriversLicenseDocument`, `p:PassportDocument`, `p:MedicalAppointmentRecord`, and `p:PetMedicationRecord`. These are used as values of a graph's `mia.graphs[].template` field — they classify the graph, not the `p:Person` individual inside it. Also defines `p:IdentityDocument` (superclass for government-issued identity document artifacts) and `p:hasIdentityDocument` (links a `p:Person` to a `p:IdentityDocument` individual they hold); `p:BirthCertificateDocument`, `p:DriversLicenseDocument`, and `p:PassportDocument` are subclasses of both `p:PersonaTemplate` and `p:IdentityDocument`. Also defines related designator classes (`p:DriversLicenseNumber`, `p:IssuingJurisdiction`, `p:PassportNumber`, `p:IssuingCountry`, `p:PlaceOfBirth`, `p:GenderMarker`, `p:IssueDate`, `p:Credential`, `p:WebURL`, `p:OrganizationUnit`, `p:JobTitle`), complex information classes (`p:Anniversary`, `p:PersonalInfo`, `p:PersonalityAssessment` — see [Personality-Related Classes and Properties](#personality-related-classes-and-properties)), annotation properties for JSContact channel labels (`p:contactContext`, `p:phoneFeature`, `p:serviceLabel`), `p:hasPhoto`, the `p:MedicalAppointmentRecord` claim properties (`p:forPatient`, `p:hasPrimaryCarePhysician`, `p:currentMedication`, `p:allergy`, `p:medicalHistoryNote`, `p:insuranceProvider`, `p:insurancePolicyNumber`, `p:insuranceGroupNumber`, `p:preferredPharmacy`), and the `p:PetMedicationRecord`/`p:Medication` classes and properties (`p:hasMedication`, `p:Medication`, `p:hasActiveIngredient`, `p:hasDoseForm`, `p:DosageAmount`, `p:hasDosageAmount`, `p:MedicationAdministration`, `p:hasAdministration`, `p:medicationFrequencyPerDay`, `p:medicationBrandName`, `p:medicationManufacturer`, `p:medicationDuration` — see [Medication-Related Classes and Properties](#medication-related-classes-and-properties)). `owl:imports` `dron-upper.ttl` (below) in addition to being imported by `persona.ttl`, so all graphs inherit these classes transitively.
- **`project_files/dron-upper.ttl`** — A hand-curated subset of [DrOn](https://github.com/mcwdsi/dron) (the Drug Ontology)'s upper module — five classes ("drug product", "active ingredient", "drug tablet", "drug capsule", "drug administration"), cited by their real upstream IRIs with real upstream labels/definitions, not a full mirror (DrOn's full distribution is ~300MB of RxNorm-derived per-product classes not relevant here). `owl:import`ed by `persona-templates.ttl`. The first non-CCO/non-`mee.foundation` external ontology this project has ever vendored.

- **`cell-templates.ttl`** — Class-level `c:Cell` templates for `cat:Category` subclasses. Holds one template cell individual per templated class: `cat:Passport`, `cat:BirthCertificate`, `cat:DriversLicense`, `cat:MedicalAppointment`, `cat:PetsMedications`. Each is pointed at by its class's own `cat:templateCell` value, which is asserted in `category.ttl` itself, alongside the class's declaration (not here) — the sole route to a template individual now, since category.ttl 1.31.0 deleted `cat:Folder` and its subclasses outright. Each individual is what the app clones into a new cell when a cell matching that class is first created in a user's tree (Lazy Instantiation). Each is typed solely `c:TemplateCell` — `c:TemplateCell` and `c:MemberCell` are disjoint, so a template cell carries no member composition of its own, just `c:templateShape` pointing to its SHACL shape in `cell-templates-shacl.ttl`, and the required `c:isTopicCell` — `true` on `ctpl:MedicalAppointmentTemplateCell`/`ctpl:PetMedicationsTemplateCell` (the two templates whose real cells always end up carrying a `c:topic` value), `false` on the other three. Imports `cell.ttl` directly (not `category.ttl` — no mutual import here).

- **`cell-templates-shacl.ttl`** — SHACL shapes for birth certificate, driver's license, passport, medical appointment, and pet medication graphs, each directly linked from its `cell-templates.ttl` template cell via `c:templateShape` (not merely co-located by naming convention):
  - `:BirthCertificateDocumentShape` (`g:template p:BirthCertificateDocument`) targets `p:BirthCertificateDocument` document individuals directly — all identity claims (names) are properties of the document individual, not the `p:Person`. Enforces: FullName OR (GivenName + FamilyName) required; optional AdditionalName, AlternateName, Nickname, Legal Name.
  - `:DriversLicenseDocumentShape` (`g:template p:DriversLicenseDocument`) targets `p:DriversLicenseDocument` document individuals directly. Enforces: FullName OR (GivenName + FamilyName) required; Birthdate, DriversLicenseNumber, ExpirationDateIdentifier required (1..1 each); IssuingJurisdiction, PostalAddress, and hasPhoto optional.
  - `:PassportDocumentShape` (`g:template p:PassportDocument`) targets `p:PassportDocument` document individuals directly. Enforces: FullName OR (GivenName + FamilyName) required; Birthdate, PassportNumber, ExpirationDateIdentifier required (1..1 each); IssueDate, IssuingCountry, PlaceOfBirth, GenderMarker, and hasPhoto optional.
  - `:MedicalAppointmentRecordShape` (`g:template p:MedicalAppointmentRecord`) targets `p:MedicalAppointmentRecord` record individuals directly — the claims needed to arrange the appointment are properties of the record, not of the patient's `p:Person`. Enforces: exactly one `forPatient`, `insuranceProvider`, and `insurancePolicyNumber` required; `hasPrimaryCarePhysician`, `medicalHistoryNote`, `insuranceGroupNumber`, `preferredPharmacy` optional; `currentMedication` and `allergy` repeatable.
  - `:PetMedicationRecordShape` (`g:template p:PetMedicationRecord`) targets `p:PetMedicationRecord` record individuals directly — the medication list is a property of the record, not of the pet (which has no `p:Person` individual). Enforces: at least one `hasMedication` link. `:MedicationShape` targets each linked `p:Medication` individual: at least one `hasActiveIngredient` (IRI); exactly one `hasDosageAmount` (`p:DosageAmount`) and `hasAdministration` (`p:MedicationAdministration`); optionally `hasDoseForm` (IRI), `medicationBrandName`, `medicationManufacturer`, `medicationDuration`. `:DosageAmountShape` targets `p:DosageAmount`: exactly one of "has decimal value"/"has integer value" (`sh:xone`), optionally "uses measurement unit". `:MedicationAdministrationShape` targets `p:MedicationAdministration`: optional `medicationFrequencyPerDay`; exactly one "occupies temporal region" link to a `BFO_0000038` interval.

- **`shacl/jscontactcard-shacl.ttl`** — SHACL shapes for JSContactCard graphs (`g:template p:JSContactCard`) — remains a standalone file, since JSContactCard is reused across many unrelated tree positions with no single `cat:Category` class of its own to attach a template cell to. Validates `p:Person` instances:
  - OrganizationName required (1..1); at least one Email or TelephoneNumber required; all name components and OrganizationUnit/JobTitle optional (0..1 each).

- **`persona-shacl.ttl`** — SHACL constraint rules for all `p:Person` individuals across all graphs. Validates properties including:
  - *All `p:Person` instances*: SSN format (`NNN-NN-NNNN`), email format, phone (E.164), address cardinality, payment cards, wallet, social network, bank account
  - *US Postal Address*: required street, city, state (USPS 2-letter), ZIP; optional country
  - *`p:Person`*: scalp hair (0..1); `has mother` / `is mother of` range must be a `p:Person`
  - *Social Network*: sub-groups (via `has part`) must be Social Networks; members (via `has member part`) must be `p:Person` instances
  - *Debit Card*: card number and expiration date required; CVV optional
  - *`p:Wallet`*: items declaring themselves `continuant part of` this wallet must be `p:PhysicalCard` instances
  - *`p:PhysicalCard`*: image scan, if present, must be `xsd:anyURI` (max 1); `continuant part of` target, if present, must be a `p:Wallet` (max 1)

### Persona Ontology Validation

`persona-shacl.ttl` runs against merged data from all graphs (Tier 1 validation). Per-template SHACL files in `shacl/` run against individual graphs, each isolated via `extract-graph.py` from its owning cell DataBook (Tier 2): birth certificate, JSContactCard, driver's license, passport, and medical appointment each have their own shape file and are validated separately to avoid their `sh:targetClass` constraints firing on every relevant slice in the merged dataset. See the [Validation](EXAMPLE.md#validation) section for commands.

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

See [**EXAMPLE.md**](EXAMPLE.md) for a worked illustrative example (Alice Walker) showing how these ontologies are used together in practice, plus diagram-generation instructions and the full validation pipeline for the example dataset, and [**APP-BEHAVIOR.md**](APP-BEHAVIOR.md) for how the app behaves on top of this data.
