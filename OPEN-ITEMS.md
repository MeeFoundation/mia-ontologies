# Open Items — as of 2026-09-04



## 1. Tier 2 validation-scoping design question

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
