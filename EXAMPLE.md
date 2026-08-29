# Cellula Ontologies — Illustrative Example

This file continues [README.md](README.md), which describes the Category, Cell, Graph, Persona, and Organization ontologies, and is continued by [APP-BEHAVIOR.md](APP-BEHAVIOR.md), which documents how the app behaves on top of this data. It provides an illustrative example — a hypothetical user, Alice Walker — showing how those ontologies are used together, followed by diagram-generation instructions and the full validation pipeline for the example dataset. 

## Illustrative Example: Alice 

This section describes the local dataset for a hypothetical user, Alice Walker. Alice's cells — each a folder holding exactly one cell DataBook file — live in a tree of cells rooted at `example/Cells/`. Every mention of "Self" in the following is a reference to the user, Alice.

### Bob and Fred

Alice knows two people, Bob and Fred. She has created two *Two-Member* cells nested under *Others* sharing one with Bob and the other with Fred. 

In her shared cell with Bob ([cell 16](<example/Cells/People/Others/Bob Johnson/Bob Johnson(others).databook.md>)) Alice has included some claims about herself ([graph 12](<example/Cells/People/Others/Bob Johnson/Bob Johnson(others).databook.md#graph-12>)) including her given name "Alice", her family name "Walker", etc. She has included ([graph 4](<example/Cells/People/Others/Bob Johnson/Bob Johnson(others).databook.md#graph-04>)) her claim that Bob's favorite drink is an oat milk cappuccino. Bob has claimed some contact information about himself ([graph 2](<example/Cells/People/Others/Bob Johnson/Bob Johnson(others).databook.md#graph-02>)), and he claims that her favorite drink is Pepsi ([graph 8](<example/Cells/People/Others/Bob Johnson/Bob Johnson(others).databook.md#graph-08>)).

<p align="center"><img src="example/images/people.png" alt="People cells"></p>

### Taking Care of Paula

To capture Alice's family-related relationship with her mother, Paula Walker, Alice created a cell ([cell 12](<example/Cells/People/Immediate Family/Paula Walker/Paula Walker(immediate-family).databook.md>)) named *Paula Walker*, nested under her *Immediate Family* cell. The subjects of this cell are Self and Paula. The cell (graphs [7](<example/Cells/People/Immediate Family/Paula Walker/Paula Walker(immediate-family).databook.md#graph-07>), [5](<example/Cells/People/Immediate Family/Paula Walker/Paula Walker(immediate-family).databook.md#graph-05>), [21](<example/Cells/People/Immediate Family/Paula Walker/Paula Walker(immediate-family).databook.md#graph-21>)) capture her connection with Paula. 

Alice spends time taking care of her mother, so she has, by herself assembled some information about Paula in some non-shared cells. In the *Health & Wellness* cell Alice keeps a record of Paula's physical characteristics such as height, eye color, hair color in [graph 17](<example/Cells/People/Immediate Family/Paula Walker/Health & Wellness/Health & Wellness.databook.md#graph-17>). This is a *Single-Member* cell whose subject is Paula. Its required `members` slot holds a minimal graph about Alice herself ([graph 35](<example/Cells/People/Immediate Family/Paula Walker/Health & Wellness/Health & Wellness.databook.md#graph-35>)). [Graph 17](<example/Cells/People/Immediate Family/Paula Walker/Health & Wellness/Health & Wellness.databook.md#graph-17>) is linked via `cell:topic`.  

Under *Medical* > *Provider* > *Primary Care Physician*, Alice keeps a record of Dr. Jane Starostina, Paula's primary care physician ([graph 25](<example/Cells/People/Immediate Family/Paula Walker/Health & Wellness/Medical/Provider/Jane Starostina/Jane Starostina(primary-care-physician).databook.md#graph-25>)). This is a *Single-Member* cell whose subject is Jane.

Alice's sister Carol is involved in taking care of their mother. The sisters need to arrange medical appointments, etc. To do so, they need to share and synchronize medical information about Paula, including her list of medications, medical history, health insurance policy, contact information and so on. To work on this as a team, Alice creates a two-member *Medical Appointment* cell and shares it with Carol. They both use it to share information about Paula's upcoming medical appointment ([graph 26](<example/Cells/People/Immediate Family/Paula Walker/Health & Wellness/Medical/Provider/Medical Appointment/Medical Appointment.databook.md#graph-26>)). This graph includes the name of Paula's doctor (primary care physician) which the app copies from the Dr. Jane Starostina cell ([graph 25](<example/Cells/People/Immediate Family/Paula Walker/Health & Wellness/Medical/Provider/Jane Starostina/Jane Starostina(primary-care-physician).databook.md#graph-25>)). 

<p align="center"><img src="example/images/people2.png" alt="People cells, continued — Immediate Family, Paula Walker, and her Health & Wellness, Medical, and Provider cells"></p>

### Working for Acme

Alice is an employee of Acme, so under her *Work* cell she has created an *Acme* cell to represent her employer. Since Acme is an organization, rather than using `cat:Person` categories she has switched to `cat:Organization` categories (light blue color). 

Under *Employees* she has added her own *Alice Walker* cell holding her Business Card claims ([graph 10](<example/Cells/Work/Acme/Employees/Alice Walker/Alice Walker(employee).databook.md#graph-10>)) — job title at Acme, work telephone number, work email, etc. One of the employees she works with is Paula Walker, so she has a *Paula Walker* cell for her, containing statements Alice has made about Paula ([graph 6](<example/Cells/Work/Acme/Employees/Paula Walker/Paula Walker(employee).databook.md#graph-06>)) and statements about herself ([graph 20](<example/Cells/Work/Acme/Employees/Paula Walker/Paula Walker(employee).databook.md#graph-20>)) neither of which have been shared with Paula since this is a (non-shared) Single-Member Cell.

<p align="center"><img src="example/images/work.png" alt="Work cells"></p>

### Service Providers

Alice has relationships with two companies, Google and ATT. The former provides her Gmail address, and the latter is her cell phone provider.

<p align="center"><img src="example/images/companies.png" alt="Companies cells"></p>

### Checking Account and Debit Card

Alice has a checking account (and associated debit care) at Citibank. In our example Citibank is compatible with PDN and participates directly as a member of this Self<>Citibank cell. Citibank directly write the data about Alice's checking account into [graph 9](<example/Cells/Finances/Banking & Payments Firms/Citibank/Citibank(banking-payments).databook.md#graph-09>). It is colored green because the claimant is Citibank, not Alice. Alice self-asserts her username and password. Citibank asserts some information about itself in [graph 27](<example/Cells/Finances/Banking & Payments Firms/Citibank/Citibank(banking-payments).databook.md#graph-27>).

<p align="center"><img src="example/images/finances.png" alt="Financial cells"></p>

### Birth Certificate and Driver's License

Alice was born in Texas and their vital records department issued a birth certificate about Alice. Alice has manually entered the information from her birth certificate ([graph 24](<example/Cells/Government/State/Texas Vital Records/Texas Vital Records(birth-certificate).databook.md#graph-24>)) and has included a scan of her paper birth certificate as content in the *Texas Vital Records* cell's Attachments tab (not shown). She recently moved to Paradise, California, and was issued a license by the California DMV. Alice manually entered the information from her plastic license card ([graph 15](<example/Cells/Government/State/California DMV/California DMV(drivers-license).databook.md#graph-15>)) and included a scan of it as content in the *California DMV* cell's Attachments tab (not shown).

<p align="center"><img src="example/images/gov-state.png" alt="Government — State cells"></p>

### Passport and Social Security Number

Alice has a social security number (SSN) issued to her by the Social Security Administration. Similarly, she has a Passport issued to her by the US Department of State.

<p align="center"><img src="example/images/gov-federal.png" alt="Government — Federal cells"></p>

### Current and Previous Homes

Alice used to live in Boston until late 2025, but now lives in Paradise, CA. Information about these two residences are in graphs [13](<example/Cells/Government/Municipality/Boston/Boston(residence).databook.md#graph-13>) and [18](<example/Cells/Government/Municipality/Paradise/Paradise(residence).databook.md#graph-18>). 

<p align="center"><img src="example/images/gov-municipality.png" alt="Government — Municipality cells"></p>

### Possessions 

Alice, like everyone, owns (or borrows, or rents) zillions of things. A tiny few of them are described in [graph 22](<example/Cells/Things/Things.databook.md#graph-22>). We focused on a few identity documents. Alice has a plastic driver's license card, a health insurance cards, social security number cards. She also has a wallet. She keeps some of these in her wallet and some separately. Presumably Alice has a vehicle of some kind, and so many other things, so this example is extremely limited at the moment. 

Here are a few lines from [graph 22](<example/Cells/Things/Things.databook.md#graph-22>):
```turtle 
:Self persona:hasWallet :Alice_Wallet ;
    persona:hasPhysicalCard :Alice_HealthInsuranceCard ;   # carried separately
    persona:hasPhysicalCard :Alice_SSNCard ;               # stored at home
    persona:hasPhysicalCard :Alice_DriversLicense ;        # in wallet
    persona:hasPhysicalCard :Alice_PaymentCard .           # in wallet

:Alice_DriversLicense rdf:type persona:PhysicalDriversLicense ;
    BFO_0000176 :Alice_Wallet .                            # in the wallet

:Alice_PaymentCard rdf:type persona:PhysicalPaymentCard ;
    BFO_0000176 :Alice_Wallet .                            # in the wallet
```

<p align="center"><img src="example/images/misc.png" alt="Miscellaneous cells"></p>


### Caring for Ginger

Alice also has a cat, Ginger. Under her *Pets* cell she has created a *Ginger* cell for this specific pet — reusing its parent's own `cat:Pets` origin, and now, thanks to `cat:Pets`'s own template cell, identifying Ginger's name, species (*Felis catus*, an NCBITaxon class IRI), breed (VBO's own "Mixed Breed (Cat)" class), birth date, and current body weight as a real `pets:Pet` individual rather than a bare label ([graph 37](<example/Cells/Pets/Ginger/Ginger(pets).databook.md#graph-37>)) — and, nested inside it, two sibling cells: a *Medical* cell recording Ginger's medical care directly (reusing its parent's own `cat:PetsMedical` origin, since `cat:PetsMedications` is no longer a category of its own, and the cell no longer needs a separate organizational scaffold cell wrapping it either, now that the merge removed the reason for one) — a completed course of amoxicillin/clavulanate (brand name Clavamox, from Zoetis) and an ongoing daily glucosamine/chondroitin joint supplement ([graph 32](<example/Cells/Pets/Ginger/Medical/Medical.databook.md#graph-32>)) — and a *Care & Feeding* cell (`cat:PetsCareAndFeeding`) recording her day-to-day care instructions: her feeding schedule and where she sleeps ([graph 60](<example/Cells/Pets/Ginger/Care & Feeding/Care & Feeding.databook.md#graph-60>)). Alice shared both cells with Paula, who also helps look after Ginger, making each a `cell:TwoMember` cell with Alice's and Paula's own bare identity claims as their two `members` ([graph 33](<example/Cells/Pets/Ginger/Medical/Medical.databook.md#graph-33>) and [graph 57](<example/Cells/Pets/Ginger/Medical/Medical.databook.md#graph-57>) for Medical; [graph 58](<example/Cells/Pets/Ginger/Care & Feeding/Care & Feeding.databook.md#graph-58>) and [graph 59](<example/Cells/Pets/Ginger/Care & Feeding/Care & Feeding.databook.md#graph-59>) for Care & Feeding).

<p align="center"><img src="example/images/pets.png" alt="Pets cells"></p>

When Alice shares her Medical cell with Paula, the app must decide where to file it in Paula's own tree — see APP-BEHAVIOR.md's [Auto-Filing on Receipt](APP-BEHAVIOR.md#auto-filing-on-receipt) for how that filing heuristic works, using this very cell as its worked example.

### Boston Hub Society

Alice is a member of the Boston Hub Society, an informal professional networking society. In our example BHS has PDN support into their server, allowing it to participate directly as an `o:Organization` member of this cell, alongside Alice and Bob. Alice maintains her BHS profile in [graph 14](<example/Cells/Affiliations/Boston Hub Society/Boston Hub Society(affiliations).databook.md#graph-14>), Bob another member keeps his profile updated ([graph 3](<example/Cells/Affiliations/Boston Hub Society/Boston Hub Society(affiliations).databook.md#graph-03>)), and BHS itself asserts a basic profile about itself in [graph 1](<example/Cells/Affiliations/Boston Hub Society/Boston Hub Society(affiliations).databook.md#graph-01>). The subject of the cell, is one of its members, BHS.

<p align="center"><img src="example/images/affiliations.png" alt="Affiliations cells"></p>

## Cells Mentioned

A summary of every narratively-illustrated cell under `example/Cells/`, grouped by the narrative subsection above it describes. 

| Subsection | Name | Cell DataBook | Subject(s) | Cell Category | Graphs |
|---|---|---|---|---|---|
| Bob and Fred | Bob Johnson | [Bob Johnson(others).databook.md](<example/Cells/People/Others/Bob Johnson/Bob Johnson(others).databook.md>) {16} | Self, Bob Johnson | `cat:Others` | 2, 4, 8, 12 |
| Bob and Fred | Fred Flintstone | [Fred Flintstone(others).databook.md](<example/Cells/People/Others/Fred Flintstone/Fred Flintstone(others).databook.md>) {17} | Self, Fred Flintstone | `cat:Others` | 29, 31 |
| Taking Care of Paula | Paula Walker | [Paula Walker(immediate-family).databook.md](<example/Cells/People/Immediate Family/Paula Walker/Paula Walker(immediate-family).databook.md>) {12} | Self, Paula Walker | `cat:ImmediateFamily` | 5, 7, 21 |
| Taking Care of Paula | Health & Wellness | [Health & Wellness.databook.md](<example/Cells/People/Immediate Family/Paula Walker/Health & Wellness/Health & Wellness.databook.md>) {13} | Paula Walker | `cat:HealthWellness` | 17, 35 |
| Taking Care of Paula | Jane Starostina | [Jane Starostina(primary-care-physician).databook.md](<example/Cells/People/Immediate Family/Paula Walker/Health & Wellness/Medical/Provider/Jane Starostina/Jane Starostina(primary-care-physician).databook.md>) {14} | Jane Starostina | `cat:PrimaryCarePhysician` | 25, 34 |
| Taking Care of Paula | Medical Appointment | [Medical Appointment.databook.md](<example/Cells/People/Immediate Family/Paula Walker/Health & Wellness/Medical/Provider/Medical Appointment/Medical Appointment.databook.md>) {15} | Paula Walker | `cat:MedicalAppointment` | 26, 28, 30 |
| Working for Acme | Alice Walker | [Alice Walker(employee).databook.md](<example/Cells/Work/Acme/Employees/Alice Walker/Alice Walker(employee).databook.md>) {18} | Self | `cat:Employee` | 10 |
| Working for Acme | Paula Walker | [Paula Walker(employee).databook.md](<example/Cells/Work/Acme/Employees/Paula Walker/Paula Walker(employee).databook.md>) {19} | Paula Walker | `cat:Employee` | 6, 20 |
| Service Providers | Google | [Google(companies).databook.md](<example/Cells/Companies/Google/Google(companies).databook.md>) {3} | Self | `cat:Companies` | 16 |
| Service Providers | ATT | [ATT(companies).databook.md](<example/Cells/Companies/ATT/ATT(companies).databook.md>) {2} | Self | `cat:Companies` | 11 |
| Checking Account and Debit Card | Citibank | [Citibank(banking-payments).databook.md](<example/Cells/Finances/Banking & Payments Firms/Citibank/Citibank(banking-payments).databook.md>) {4} | Self, Citibank | `cat:BankingPayments` | 9, 27 |
| Birth Certificate and Driver's License | Texas Vital Records | [Texas Vital Records(birth-certificate).databook.md](<example/Cells/Government/State/Texas Vital Records/Texas Vital Records(birth-certificate).databook.md>) {10} | Self | `cat:BirthCertificate` | 24 |
| Birth Certificate and Driver's License | California DMV | [California DMV(drivers-license).databook.md](<example/Cells/Government/State/California DMV/California DMV(drivers-license).databook.md>) {9} | Self | `cat:DriversLicense` | 15 |
| Passport and Social Security Number | Department of State | [Department of State(passport).databook.md](<example/Cells/Government/Federal/Department of State/Department of State(passport).databook.md>) {5} | Self | `cat:Passport` | 19 |
| Passport and Social Security Number | Social Security Administration | [Social Security Administration(ssn).databook.md](<example/Cells/Government/Federal/Social Security Administration/Social Security Administration(ssn).databook.md>) {6} | Self | `cat:SSN` | 23 |
| Current and Previous Homes | Boston | [Boston(residence).databook.md](<example/Cells/Government/Municipality/Boston/Boston(residence).databook.md>) {7} | Self | `cat:Residence` | 13 |
| Current and Previous Homes | Paradise | [Paradise(residence).databook.md](<example/Cells/Government/Municipality/Paradise/Paradise(residence).databook.md>) {8} | Self | `cat:Residence` | 18 |
| Possessions | Things | [Things.databook.md](<example/Cells/Things/Things.databook.md>) {11} | Self | `cat:Things` | 22 |
| Caring for Ginger | Ginger | [Ginger(pets).databook.md](<example/Cells/Pets/Ginger/Ginger(pets).databook.md>) {41} | Ginger | `cat:Pets` | 36, 37 |
| Caring for Ginger | Medical | [Medical.databook.md](<example/Cells/Pets/Ginger/Medical/Medical.databook.md>) {40} | Ginger | `cat:PetsMedical` | 32, 33, 57 |
| Caring for Ginger | Care & Feeding | [Care & Feeding.databook.md](<example/Cells/Pets/Ginger/Care & Feeding/Care & Feeding.databook.md>) {42} | Ginger | `cat:PetsCareAndFeeding` | 58, 59, 60 |
| Boston Hub Society | Boston Hub Society | [Boston Hub Society(affiliations).databook.md](<example/Cells/Affiliations/Boston Hub Society/Boston Hub Society(affiliations).databook.md>) {1} | BHS | `cat:Affiliations` | 1, 3, 14 |

## Graphs

The graphs in the table below are *about* Alice and claimed *by* Alice. The "Cell DataBook" link jumps straight to each graph's own `### Graph NN` section inside its owning cell-databook file under `example/Cells/`.

| #  | Cell DataBook                                                                          | Category | Key data                                                         | Diagram |
|--- |:--------------------------------------------------------------------------------------|:-------------|:-----------------------------------------------------------------|:--------|
| 10 | [Alice Walker(employee).databook.md](<example/Cells/Work/Acme/Employees/Alice Walker/Alice Walker(employee).databook.md#graph-10>) {18} | `cat:Employee`     | Business card — given name, family name, email, phone, employer  | [view](example/graphs/images/graph-10.png) |
| 11 | [ATT(companies).databook.md](<example/Cells/Companies/ATT/ATT(companies).databook.md#graph-11>) {2}                     | `cat:Companies`    | Phone number                                                     | [view](example/graphs/images/graph-11.png) |
| 12 | [Bob Johnson(others).databook.md](<example/Cells/People/Others/Bob Johnson/Bob Johnson(others).databook.md#graph-12>) {16}                     | `cat:Others`       | Alice's 1:1 graph with Bob; social network with Bob as member  | [view](example/graphs/images/graph-12.png)|
| 13 | [Boston(residence).databook.md](<example/Cells/Government/Municipality/Boston/Boston(residence).databook.md#graph-13>) {7}               | `cat:Residence` | Previous address — Boston, MA (2020–2025) with temporal interval | [view](example/graphs/images/graph-13.png) |
| 14  | [Boston Hub Society(affiliations).databook.md](<example/Cells/Affiliations/Boston Hub Society/Boston Hub Society(affiliations).databook.md#graph-14>) {1}                     | `cat:Affiliations` | BHS profile: email, phone and current address                    | [view](example/graphs/images/graph-14.png)|
| 15 | [California DMV(drivers-license).databook.md](<example/Cells/Government/State/California DMV/California DMV(drivers-license).databook.md#graph-15>) {9} | `cat:DriversLicense`      | California driver's license — legal name, DOB, DL#, expiry, photo | [view](example/graphs/images/graph-15.png) |
| 16 | [Google(companies).databook.md](<example/Cells/Companies/Google/Google(companies).databook.md#graph-16>) {3}               | `cat:Companies`    | Gmail address                                                    | [view](example/graphs/images/graph-16.png) |
| 18 | [Paradise(residence).databook.md](<example/Cells/Government/Municipality/Paradise/Paradise(residence).databook.md#graph-18>) {8}           | `cat:Residence` | Current address — Paradise, CA (2025–present)                    | [view](example/graphs/images/graph-18.png) |
| 19 | [Department of State(passport).databook.md](<example/Cells/Government/Federal/Department of State/Department of State(passport).databook.md#graph-19>) {5}             | `cat:Passport`    | US passport — legal name, DOB, passport#, issue/expiry, place of birth, gender marker, photo | [view](example/graphs/images/graph-19.png) |
| 20 | [Paula Walker(employee).databook.md](<example/Cells/Work/Acme/Employees/Paula Walker/Paula Walker(employee).databook.md#graph-20>) {19}                   | `cat:Employee`     | Acme employee graph; company email; works with Paula           | [view](example/graphs/images/graph-20.png)|
| 21 | [Paula Walker(immediate-family).databook.md](<example/Cells/People/Immediate Family/Paula Walker/Paula Walker(immediate-family).databook.md#graph-21>) {12}   | `cat:ImmediateFamily`       | Alice as a family member                       | [view](example/graphs/images/graph-21.png) |
| 22 | [Things.databook.md](<example/Cells/Things/Things.databook.md#graph-22>) {11}     | `cat:Things`  | Wallet (driver's license + payment card); health ins., SSN card  | [view](example/graphs/images/graph-22.png) |
| 23 | [Social Security Administration(ssn).databook.md](<example/Cells/Government/Federal/Social Security Administration/Social Security Administration(ssn).databook.md#graph-23>) {6}                     | `cat:SSN`      | Social security number (SSN)                                     | [view](example/graphs/images/graph-23.png) |
| 24 | [Texas Vital Records(birth-certificate).databook.md](<example/Cells/Government/State/Texas Vital Records/Texas Vital Records(birth-certificate).databook.md#graph-24>) {10} | `cat:BirthCertificate`        | Legal names, maiden name                                         | [view](example/graphs/images/graph-24.png) |
| 29 | [Fred Flintstone(others).databook.md](<example/Cells/People/Others/Fred Flintstone/Fred Flintstone(others).databook.md#graph-29>) {17}                     | `cat:Others`       | Alice's 1:1 graph with Fred; social network with Fred as member  | [view](example/graphs/images/graph-29.png) |
| 33 | [Medical.databook.md](<example/Cells/Pets/Ginger/Medical/Medical.databook.md#graph-33>) {40} | `cat:PetsMedical`     | Deliberately empty — the Ginger-Medical cell's required member entry          | [view](example/graphs/images/graph-33.png) |
| 34 | [Jane Starostina(primary-care-physician).databook.md](<example/Cells/People/Immediate Family/Paula Walker/Health & Wellness/Medical/Provider/Jane Starostina/Jane Starostina(primary-care-physician).databook.md#graph-34>) {14} | `cat:PrimaryCarePhysician`     | Alice's bare given-name claim — the Jane-Starostina cell's required member entry          | [view](example/graphs/images/graph-34.png) |
| 35 | [Health & Wellness.databook.md](<example/Cells/People/Immediate Family/Paula Walker/Health & Wellness/Health & Wellness.databook.md#graph-35>) {13} | `cat:HealthWellness`     | Alice's bare given-name claim — the Health & Wellness cell's required member entry          | [view](example/graphs/images/graph-35.png) |
| 36 | [Ginger(pets).databook.md](<example/Cells/Pets/Ginger/Ginger(pets).databook.md#graph-36>) {41} | `cat:Pets`     | Deliberately empty — the Ginger cell's required member entry; the `members` requirement is about `g:subject`/`g:claimant`, not about carrying content          | [view](example/graphs/images/graph-36.png) |
| 58 | [Care & Feeding.databook.md](<example/Cells/Pets/Ginger/Care & Feeding/Care & Feeding.databook.md#graph-58>) {42} | `cat:PetsCareAndFeeding`     | Deliberately empty — the Ginger-Care & Feeding cell's required member entry          | [view](example/graphs/images/graph-58.png) |

The following table lists graphs that are *about* Alice but claimed by others.

| #  | Cell DataBook                                                                         | Category | Key data                             | Diagram |
|--- |:-------------------------------------------------------------------------------------|:-------------|:-------------------------------------|:--------|
| 8  | [Bob Johnson(others).databook.md](<example/Cells/People/Others/Bob Johnson/Bob Johnson(others).databook.md#graph-08>) {16}                         | `cat:Others`            | Alice as seen by Bob                 | [view](example/graphs/images/graph-08.png)|
| 9 | [Citibank(banking-payments).databook.md](<example/Cells/Finances/Banking & Payments Firms/Citibank/Citibank(banking-payments).databook.md#graph-09>) {4}     | `cat:BankingPayments` | Debit card                           | [view](example/graphs/images/graph-09.png) |

The following table lists graphs about other people (Paula and Bob) or organizations (Boston Hub Society) in Alice's own tree. As above, each "Cell DataBook" link jumps to that graph's section inside its owning cell-databook file.

| #  | Cell DataBook                                                                                     | Category | Key data                                                         | Diagram |
|--- |:-------------------------------------------------------------------------------------------------|:-------------|:-----------------------------------------------------------------|:--------|
| 1  | [Boston Hub Society(affiliations).databook.md](<example/Cells/Affiliations/Boston Hub Society/Boston Hub Society(affiliations).databook.md#graph-01>) {1}             | `cat:Affiliations` | BHS's own organization profile, claimed by BHS                | [view](example/graphs/images/graph-01.png) |
| 2  | [Bob Johnson(others).databook.md](<example/Cells/People/Others/Bob Johnson/Bob Johnson(others).databook.md#graph-02>) {16}                     | `cat:Others`       | Bob's self-claimed Bob persona                                 | [view](example/graphs/images/graph-02.png)|
| 3  | [Boston Hub Society(affiliations).databook.md](<example/Cells/Affiliations/Boston Hub Society/Boston Hub Society(affiliations).databook.md#graph-03>) {1}                     | `cat:Affiliations` | Bob's BHS member persona (name, email, phone, address)          | [view](example/graphs/images/graph-03.png) |
| 4  | [Bob Johnson(others).databook.md](<example/Cells/People/Others/Bob Johnson/Bob Johnson(others).databook.md#graph-04>) {16}                 | `cat:Others`       | Alice's notes about Bob; fav drink: oat milk cappuccino         | [view](example/graphs/images/graph-04.png) |
| 5  | [Paula Walker(immediate-family).databook.md](<example/Cells/People/Immediate Family/Paula Walker/Paula Walker(immediate-family).databook.md#graph-05>) {12} | `cat:ImmediateFamily`       | Paula's own family persona; social network with Alice       | [view](example/graphs/images/graph-05.png)|
| 6  | [Paula Walker(employee).databook.md](<example/Cells/Work/Acme/Employees/Paula Walker/Paula Walker(employee).databook.md#graph-06>) {19}           | `cat:Employee`     | Paula as Alice's Acme colleague (Alice-claimed)                | [view](example/graphs/images/graph-06.png)|
| 7  | [Paula Walker(immediate-family).databook.md](<example/Cells/People/Immediate Family/Paula Walker/Paula Walker(immediate-family).databook.md#graph-07>) {12} | `cat:ImmediateFamily`       | Paula as Alice's family member (Alice-claimed)           | [view](example/graphs/images/graph-07.png)|
| 17 | [Health & Wellness.databook.md](<example/Cells/People/Immediate Family/Paula Walker/Health & Wellness/Health & Wellness.databook.md#graph-17>) {13} | `cat:HealthWellness`     | Paula's physical body — height (68 in.), blue eyes, grey hair — as recorded by Alice; linked via `cell:topic` (Paula is the cell's subject, not its member)            | [view](example/graphs/images/graph-17.png) |
| 25 | [Jane Starostina(primary-care-physician).databook.md](<example/Cells/People/Immediate Family/Paula Walker/Health & Wellness/Medical/Provider/Jane Starostina/Jane Starostina(primary-care-physician).databook.md#graph-25>) {14} | `cat:PrimaryCarePhysician`       | Alice's record of Dr. Jane Starostina, Paula Walker's primary care physician           | [view](example/graphs/images/graph-25.png)|
| 26 | [Medical Appointment.databook.md](<example/Cells/People/Immediate Family/Paula Walker/Health & Wellness/Medical/Provider/Medical Appointment/Medical Appointment.databook.md#graph-26>) {15} | `cat:MedicalAppointment`       | Alice and Carol's shared claims for Paula's medical appointment — medications, allergies, insurance, PCP reference           | [view](example/graphs/images/graph-26.png)|
| 28 | [Medical Appointment.databook.md](<example/Cells/People/Immediate Family/Paula Walker/Health & Wellness/Medical/Provider/Medical Appointment/Medical Appointment.databook.md#graph-28>) {15} | `cat:MedicalAppointment`       | Carol's own self-claimed persona and contact info — one of this cell's two members, alongside Alice (graph 30)           | [view](example/graphs/images/graph-28.png) |
| 30 | [Medical Appointment.databook.md](<example/Cells/People/Immediate Family/Paula Walker/Health & Wellness/Medical/Provider/Medical Appointment/Medical Appointment.databook.md#graph-30>) {15} | `cat:MedicalAppointment`       | Alice's own self-claimed contact info — the other of this cell's two members, alongside Carol (graph 28)           | [view](example/graphs/images/graph-30.png) |
| 27 | [Citibank(banking-payments).databook.md](<example/Cells/Finances/Banking & Payments Firms/Citibank/Citibank(banking-payments).databook.md#graph-27>) {4} | `cat:BankingPayments` | Alice's own self-claimed notes about Citibank as an institution, alongside Citibank's own claimed record about her (graph 09) | [view](example/graphs/images/graph-27.png) |
| 31 | [Fred Flintstone(others).databook.md](<example/Cells/People/Others/Fred Flintstone/Fred Flintstone(others).databook.md#graph-31>) {17}                     | `cat:Others`       | Fred's self-claimed Fred persona                                 | [view](example/graphs/images/graph-31.png) |
| 32 | [Medical.databook.md](<example/Cells/Pets/Ginger/Medical/Medical.databook.md#graph-32>) {40} | `cat:PetsMedical`       | Alice's record of her cat Ginger's medications — amoxicillin/clavulanate course, ongoing glucosamine/chondroitin supplement           | [view](example/graphs/images/graph-32.png)|
| 37 | [Ginger(pets).databook.md](<example/Cells/Pets/Ginger/Ginger(pets).databook.md#graph-37>) {41} | `cat:Pets`       | Alice's basic claim identifying Ginger — name, species (Felis catus, NCBITaxon), breed (Mixed Breed (Cat), VBO), birth date, and current body weight — backs the Ginger cell's `subject: ":Ginger"` with a real graph, typed `pets:Pet`           | [view](example/graphs/images/graph-37.png)|
| 57 | [Medical.databook.md](<example/Cells/Pets/Ginger/Medical/Medical.databook.md#graph-57>) {40} | `cat:PetsMedical`       | Paula's own self-claimed given-name claim — the cell's second `members` entry after Alice shared it with her, making it a `cell:TwoMember` cell           | [view](example/graphs/images/graph-57.png)|
| 59 | [Care & Feeding.databook.md](<example/Cells/Pets/Ginger/Care & Feeding/Care & Feeding.databook.md#graph-59>) {42} | `cat:PetsCareAndFeeding`       | Paula's own self-claimed given-name claim — the cell's second `members` entry after Alice shared it with her, making it a `cell:TwoMember` cell           | [view](example/graphs/images/graph-59.png)|
| 60 | [Care & Feeding.databook.md](<example/Cells/Pets/Ginger/Care & Feeding/Care & Feeding.databook.md#graph-60>) {42} | `cat:PetsCareAndFeeding`       | Alice's day-to-day care and feeding instructions for Ginger — feeding schedule, food, and where she sleeps           | [view](example/graphs/images/graph-60.png)|

## Diagrams

`draw.py` generates a Mermaid (`.mmd`) and PNG diagram for a single embedded graph, given its owning cell DataBook file and its id (or id local-name):

```bash
python3 draw.py "example/Cells/Finances/Banking & Payments Firms/Citibank/Citibank(banking-payments).databook.md" "graph-09"
python3 draw.py "example/Cells/Government/Municipality/Paradise/Paradise(residence).databook.md" "graph-18"
```

Both output files are always written to `example/graphs/images/` (must be run from the repo root), keyed by the graph's own id local-name — the same location and naming graph diagrams used before the graph/cell merge, even though the graph's own file no longer exists.

**Dependencies** (one-time setup):
```bash
pip install rdflib pyyaml
npm install -g @mermaid-js/mermaid-cli
```

Each diagram shows the `p:Person` individual (yellow), supporting named individuals (white boxes), class labels (plain text), blank-node designator chains, and literal values (green).

## Validation

Validation requires [Apache Jena](https://jena.apache.org/) (`riot`, `shacl`), the [DataBook CLI](https://github.com/kurtcagle/databook) (`databook`; install: `git clone https://github.com/kurtcagle/databook.git && cd databook && npm install && npm install -g .`) — the CLI's reference implementation moved here from `w3c-cg/holon`, which retired its two previously-vendored copies in favor of this single upstream source — `pyyaml` for `yaml-to-rdf.py` (`pip install pyyaml`), and `extract-graph.py` (no extra dependencies) for isolating one embedded graph's Turtle from a cell DataBook that may hold several — needed since `databook extract` has no notion of "pick one graph out of many" and Tier 2 validates one graph at a time. SHACL shapes remain plain Turtle (`.ttl`).

### Quick check — DataBook syntax

Verify that every DataBook file has valid YAML frontmatter and well-formed block annotations:

```bash
find example -name "*.databook.md" -not -path "*/under-development/*" -print0 | sort -z |
while IFS= read -r -d '' f; do
  databook head "$f" -q > /dev/null || echo "FAIL: $f"
done
```

A file that fails here will also fail silently in `databook extract`, producing no Turtle output and causing downstream `riot` or SHACL errors that are harder to trace. (Uses `-print0`/`read -d ''` rather than `for f in $(find ...)` — cell DataBook paths under `example/Cells/` routinely contain spaces, e.g. `Banking & Payments Firms`, which word-splitting would otherwise silently break.)

### Tier 1 — general validation (all graphs)

`persona-shacl.ttl` applies to every `p:Person` individual across every embedded graph.

```bash
# Step 1 — extract turtle from every DataBook file (excluding under-development).
# Uses -print0/read -d '' rather than for f in $(find ...) — cell-databook paths
# under example/Cells/ routinely contain spaces (e.g. "Banking & Payments Firms"),
# which word-splitting would otherwise silently break.
> /tmp/mia-data.ttl
find example -name "*.databook.md" -not -path "*/under-development/*" -print0 | sort -z |
while IFS= read -r -d '' f; do
  databook extract "$f" 2>/dev/null
done >> /tmp/mia-data.ttl

# Step 1b — synthesize c:/graph: triples from each cell DataBook's own YAML
# frontmatter (mia.* fields, including its mia.graphs list — since
# graph-databooks were merged into their owning cell-databooks, a graph's
# claimant/subject now live there rather than in a separate graph-databook
# file). There is no cat: synthesis at all any more — category.ttl 1.31.0
# deleted cat:Folder and its subclasses outright, so a folder's tree position
# is purely a filesystem fact with no RDF individual to synthesize; the only
# surviving classification fact, c:origin, is read directly from each cell
# DataBook's own explicit mia.origin field. databook extract only pulls
# fenced Turtle blocks, which cell DataBooks don't carry — without this
# step, c:Cell individuals and g:SCGraph's subject/claimant never
# reach the merged graph, and cell-shacl.ttl/graph-shacl.ttl's
# :SCGraphShape never fire against real instance data. See yaml-to-rdf.py.
python3 yaml-to-rdf.py . > /tmp/mia-yaml.ttl

# Step 2 — merge data with all ontology files, foundation ontologies, and self.ttl
# (cell-templates.ttl is deliberately excluded here, unlike Tier 2's base merge
# below: its template individuals are generic, reusable content with no real
# person bound to them, so they can't sensibly carry cell-shacl.ttl's required
# c:members/c:creator — they're validated only via cell-templates-shacl.ttl/
# other/pets-shacl.ttl, in Tier 2. other/pets.ttl is included below — it's a
# full peer application ontology, same as persona-templates.ttl/graph.ttl/etc.)
riot --output=turtle \
  project_files/bfo-core.ttl \
  project_files/PersonOntology.ttl \
  project_files/AddressOntology.ttl \
  project_files/StagingOntology.ttl \
  project_files/UnitsOfMeasureOntology.ttl \
  project_files/InformationEntityOntology.ttl \
  project_files/dron-upper.ttl \
  project_files/ncbitaxon-subset.ttl \
  project_files/vbo-subset.ttl \
  persona.ttl persona-templates.ttl graph.ttl cell.ttl category.ttl other/pets.ttl \
  organization.ttl \
  example/graphs/self.ttl \
  /tmp/mia-data.ttl \
  /tmp/mia-yaml.ttl \
  2>/dev/null > /tmp/mia-merged.ttl

# Step 3 — collect shapes (shacl/jscontactcard-shacl.ttl, cell-templates-shacl.ttl, and
# other/pets-shacl.ttl excluded — see Tier 2; all three target document classes and would
# fire incorrectly on all individuals when applied to merged data. pdn-identity-shacl.ttl
# is also excluded: its ontology, pdn-identity.ttl, isn't part of the Step 2 merge —
# nothing here ever references an identity: term, see persona.ttl 4.0.6)
grep -v 'owl:imports' persona-shacl.ttl > /tmp/mia-shapes.ttl
grep -v 'owl:imports' graph-shacl.ttl >> /tmp/mia-shapes.ttl
grep -v 'owl:imports' cell-shacl.ttl >> /tmp/mia-shapes.ttl
grep -v 'owl:imports' organization-shacl.ttl >> /tmp/mia-shapes.ttl

# Step 4 — validate
shacl validate --shapes /tmp/mia-shapes.ttl --data /tmp/mia-merged.ttl --text
```

Expected output: `Conforms`

### Tier 2 — per-template validation (individual graphs)

Four of the seven per-template shapes (BirthCertificate, DriversLicense, Passport, MedicalAppointment) live in `cell-templates-shacl.ttl`; two (Pet, PetMedicationRecord) live in `other/pets-shacl.ttl`; JSContactCard's shape remains a standalone file in `shacl/` (it has no `cat:Category` class of its own — see [Persona Templates](README.md#persona-templates)). Each is run against only the relevant graph, isolated via `extract-graph.py` from its owning cell DataBook file and merged with the foundation ontologies. Isolation matters because a cell may hold more than one graph — the MedicalAppointment case below lives in a three-graph cell, so a whole-file `databook extract` there would wrongly pull in its two sibling graphs' data too.

```bash
# Shared base: foundation ontologies + application ontologies + self.ttl
riot --output=turtle \
  project_files/bfo-core.ttl \
  project_files/PersonOntology.ttl \
  project_files/AddressOntology.ttl \
  project_files/StagingOntology.ttl \
  project_files/UnitsOfMeasureOntology.ttl \
  project_files/InformationEntityOntology.ttl \
  project_files/dron-upper.ttl \
  project_files/ncbitaxon-subset.ttl \
  project_files/vbo-subset.ttl \
  persona.ttl persona-templates.ttl graph.ttl cell.ttl category.ttl cell-templates.ttl other/pets.ttl \
  organization.ttl \
  example/graphs/self.ttl \
  2>/dev/null > /tmp/mia-base.ttl

# BirthCertificate — graph-24
python3 extract-graph.py "example/Cells/Government/State/Texas Vital Records/Texas Vital Records(birth-certificate).databook.md" "graph-24" > /tmp/data-birth-cert-raw.ttl
riot --output=turtle /tmp/mia-base.ttl /tmp/data-birth-cert-raw.ttl 2>/dev/null > /tmp/data-birth-cert.ttl
grep -v 'owl:imports' cell-templates-shacl.ttl > /tmp/shapes-cell-templates.ttl
shacl validate --shapes /tmp/shapes-cell-templates.ttl --data /tmp/data-birth-cert.ttl --text

# JSContactCard — graph-10
python3 extract-graph.py "example/Cells/Work/Acme/Employees/Alice Walker/Alice Walker(employee).databook.md" "graph-10" > /tmp/data-jscontact-raw.ttl
riot --output=turtle /tmp/mia-base.ttl /tmp/data-jscontact-raw.ttl 2>/dev/null > /tmp/data-jscontact.ttl
grep -v 'owl:imports' shacl/jscontactcard-shacl.ttl > /tmp/shapes-jscontact.ttl
shacl validate --shapes /tmp/shapes-jscontact.ttl --data /tmp/data-jscontact.ttl --text

# DriversLicense — graph-15
python3 extract-graph.py "example/Cells/Government/State/California DMV/California DMV(drivers-license).databook.md" "graph-15" > /tmp/data-dl-raw.ttl
riot --output=turtle /tmp/mia-base.ttl /tmp/data-dl-raw.ttl 2>/dev/null > /tmp/data-dl.ttl
shacl validate --shapes /tmp/shapes-cell-templates.ttl --data /tmp/data-dl.ttl --text

# Passport — graph-19
python3 extract-graph.py "example/Cells/Government/Federal/Department of State/Department of State(passport).databook.md" "graph-19" > /tmp/data-passport-raw.ttl
riot --output=turtle /tmp/mia-base.ttl /tmp/data-passport-raw.ttl 2>/dev/null > /tmp/data-passport.ttl
shacl validate --shapes /tmp/shapes-cell-templates.ttl --data /tmp/data-passport.ttl --text

# MedicalAppointment — graph-26
# (this cell has THREE embedded graphs — extract-graph.py isolates just this one,
# unlike the other four, which happen to be alone in a single-graph cell)
python3 extract-graph.py "example/Cells/People/Immediate Family/Paula Walker/Health & Wellness/Medical/Provider/Medical Appointment/Medical Appointment.databook.md" "graph-26" > /tmp/data-medical-appt-raw.ttl
riot --output=turtle /tmp/mia-base.ttl /tmp/data-medical-appt-raw.ttl 2>/dev/null > /tmp/data-medical-appt.ttl
shacl validate --shapes /tmp/shapes-cell-templates.ttl --data /tmp/data-medical-appt.ttl --text

# PetMedications — graph-32
python3 extract-graph.py "example/Cells/Pets/Ginger/Medical/Medical.databook.md" "graph-32" > /tmp/data-pet-medications-raw.ttl
riot --output=turtle /tmp/mia-base.ttl /tmp/data-pet-medications-raw.ttl 2>/dev/null > /tmp/data-pet-medications.ttl
grep -v 'owl:imports' other/pets-shacl.ttl > /tmp/shapes-pets.ttl
shacl validate --shapes /tmp/shapes-pets.ttl --data /tmp/data-pet-medications.ttl --text

# PetProfile — graph-37
python3 extract-graph.py "example/Cells/Pets/Ginger/Ginger(pets).databook.md" "graph-37" > /tmp/data-pet-profile-raw.ttl
riot --output=turtle /tmp/mia-base.ttl /tmp/data-pet-profile-raw.ttl 2>/dev/null > /tmp/data-pet-profile.ttl
shacl validate --shapes /tmp/shapes-pets.ttl --data /tmp/data-pet-profile.ttl --text
```

Expected output for each: `Conforms`
