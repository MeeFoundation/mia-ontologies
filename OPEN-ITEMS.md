# Open Items — as of 2026-09-04

Two things deliberately left unfixed from the 2026-09-04 session. Not urgent, not load-bearing for
any integrity check — just notes for whenever they're picked back up.

## 1. Ontology-internal prose staleness (`cell-templates.ttl` / `persona-templates.ttl`)

Both files have a big top-level `rdfs:comment` block on their `owl:Ontology` header that narrates the
whole file's design in prose. Every time a new template was added this session, `owl:versionInfo` got
bumped with a one-line "what changed" note — but the bigger descriptive paragraph above it was never
rewritten to match. The versioned change-log is accurate; the "current state" prose has drifted.

**`cell-templates.ttl`'s header comment still says:**

> "Three patterns: (1) ... for the **three** templates whose content is filed as a `cell:member` graph
> (**Passport, BirthCertificate, DriversLicense**) ... (2) ... for the **five** whose content is filed
> as a `cell:topic` graph instead (MedicalAppointment, PetMedications, PetProfile, VehicleProfile,
> Companies) ... `cell:isTopicCell` — true on the **five** templates in pattern (2) ... false on the
> other **eight**"

All of that is now wrong:
- Pattern (1) is *empty* — Passport/BirthCertificate/DriversLicense all moved into pattern (2) this
  session.
- The true/false split is 12/6, not 5/8.
- The comment never mentions SSN, Home, Trips, BankingPayments, or `ctpl:UserDefinedTemplateCell` at
  all — five templates that now exist aren't described here.

**`persona-templates.ttl`'s header comment still says:**

> "Each concrete template type (BirthCertificateDocument, JSContactCard, DriversLicenseDocument,
> PassportDocument, MedicalAppointmentRecord, ServiceAccount) ... **Five of the six** ... Class
> hierarchy: `p:PersonaTemplate` → ... → `p:MedicalAppointmentRecord`"

This only names 6 of the 10 template classes — `DebitCard`, `Residence`, `Itinerary`, and
`CheckingAccount` are missing from both the narrative and the "Class hierarchy" diagram at the bottom.

**Why this was left alone**: everything a reader would actually consult for current facts —
README.md's and CLAUDE.md's Core Files tables, plus the Check 5/10g/10h prose the integrity checks
depend on — was already fixed. These two `rdfs:comment` blocks are more like each file's own internal
"architecture note to self," accurate as of whenever last rewritten wholesale, but not load-bearing
for any check. Low risk, but worth a full rewrite next time either file gets touched again, so it
doesn't drift further.

## 2. Tier 2 validation-scoping design question

Also tracked in Claude's memory as `project_shacl_validation_scoping.md`.

**The concrete bug that surfaced it**: running `JSContactCardPersonShape` against Bob Johnson's own
graph (graph-02) reports a violation on node `:Self` — not `:Bob_Johnson` — for missing a `GivenName`.
Bob's own data is completely fine (he has one). The failure happens because:

1. Every graph that mentions `:Self` re-asserts `:Self rdf:type persona:Person` (the self-containment
   convention), even when the graph is really about someone else and `:Self` only appears incidentally
   (e.g. as a bare social-network member).
2. `JSContactCardPersonShape` targets the whole `persona:Person` *class*, so it fires on every
   `persona:Person` in the test slice — including that bare, nameless `:Self` — not just the one
   individual the graph is actually "about."

**The direction given**: Tier 2 validation should scope to a single cell/subject, not fire against
every `persona:Person` in the merged test graph. Noted for later rather than fixed now.

**Options to consider when it's picked back up**:
- Give shapes a focus-node derived from the graph's own `cell:subject` instead of a class-wide
  `sh:targetClass`.
- Otherwise exclude incidental individuals from the merged test slice before validating.

**Practical implication in the meantime**: if a future Tier 2 run reports "must have exactly one
GivenName" (or similar), check *which node* the violation names before treating it as a real data
bug — if it's `:Self` (or another bystander) rather than the graph's declared subject, it's this same
artifact, not a defect.
