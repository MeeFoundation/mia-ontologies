---
id: http://www.example.org/mia/cells/cell-47
title: "Kyoto Trip 2027"
type: cell-databook
version: 1.0.0
created: 2026-08-30
description: >
  Cell DataBook for folder "Kyoto Trip 2027" (cell:category: cat:Trips, reusing its parent "Trips"
  cell's own origin), nested under "Travel" > "Trips". A user-defined instance folder for a
  specific trip Alice is planning with her spouse Dave. A three-member cell demonstrating
  agent:Agent as a real cell member: Alice's own AI travel agent joins alongside Alice and Dave,
  each with a self-claimed member entry (graph-66, graph-67, graph-68). The trip itself is backed
  by two topic graphs sharing one subject (:Kyoto_Trip_2027) but two different claimants — Alice's
  own basic claim (graph-69) and her agent's own evolving, collaboratively-drafted itinerary
  (graph-70) — mirroring how a cell:topic may be claimed from more than one side (see the Medical
  Appointment cell's two "Med. Appt mt." squares in README.md's Representative Cells diagram).
mia:
  category: "cat:Trips"
  creator: ":Self"
  owner: ":Self"
  member:
    - "graph-66"
    - "graph-67"
    - "graph-68"
  topic:
    - "graph-69"
    - "graph-70"
  graphs:
    - id: "http://www.example.org/mia/graphs/graph-66"
      claimant: ":Self"
      subject: ":Self"
    - id: "http://www.example.org/mia/graphs/graph-67"
      claimant: ":Alice_Travel_Agent"
      subject: ":Alice_Travel_Agent"
    - id: "http://www.example.org/mia/graphs/graph-68"
      claimant: ":Dave"
      subject: ":Dave"
    - id: "http://www.example.org/mia/graphs/graph-69"
      claimant: ":Self"
      subject: ":Kyoto_Trip_2027"
    - id: "http://www.example.org/mia/graphs/graph-70"
      claimant: ":Alice_Travel_Agent"
      subject: ":Kyoto_Trip_2027"
---

## Graphs

<a id="graph-66"></a>
### Graph 66

#### Overview

This graph is one of the cell's three required `member` entries — Alice's own bare given-name claim (see Check 21: `:Self` must be a member of every cell in the user's own tree, regardless of member count), extended with her social network link to Dave (mirroring the pattern used in graph 12's Alice–Bob connection) — this is what makes `:Dave` reachable per Check 4, since he is otherwise referenced only via this cell's `member`/`topic`, not via a dedicated Immediate Family cell of his own (out of scope for this worked example).

#### Graph

```turtle
<!-- databook:id: alice-kyoto-trip-member-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-66#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Self persona:hasSocialNetwork :Alice_Dave_Network .

:Alice_Dave_Network rdf:type owl:NamedIndividual ,
                             cco:ont00001183 ;  # Social Network
    rdfs:label "Alice Walker's Dave connection"@en ;
    <http://purl.obolibrary.org/obo/BFO_0000115> :Dave .  # has member part
```

<a id="graph-67"></a>
### Graph 67

#### Overview

This graph is another of the cell's three required `member` entries — Alice's own AI travel agent, invited to collaborate on planning this trip, joins as a real cell member (see README.md's Agent Ontology section) rather than staying an invisible tool: it gets its own self-claimed member graph, exactly like a human member's, typed `agent:Agent` and carrying `agent:actsFor :Self` to record which member it is a delegate for. `agent:Agent` is never a `cell:creator` — Alice alone created this cell — but it is a legitimate `g:claimant` and `cell:member` participant.

#### Graph

```turtle
<!-- databook:id: alice-travel-agent-member-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-67#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix agent: <http://mee.foundation/ontologies/agent#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Alice_Travel_Agent rdf:type owl:NamedIndividual ,
               agent:Agent ;
    rdfs:label "Alice's Travel Agent (ChatGPT)"@en ;
    agent:actsFor :Self .
```

<a id="graph-68"></a>
### Graph 68

#### Overview

This graph is the cell's third required `member` entry — Dave's own self-claimed bare given-name persona, transmitted from Dave's own instance of the app to Alice's over the PDN once she invited him to this cell, the same "self-claimed member" pattern Bob Johnson's own graphs use. This third distinct `member` subject (alongside `:Self` and `:Alice_Travel_Agent`) is what makes the cell a three-member cell rather than a two-member cell.

#### Graph

```turtle
<!-- databook:id: dave-dave-member-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-68#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix persona: <http://mee.foundation/ontologies/persona#> .
@prefix cco: <https://w3id.org/cco-domains/cco/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Dave rdf:type owl:NamedIndividual ,
              persona:Person ;
    rdfs:label "Dave (Alice's spouse)"@en ;
    <https://w3id.org/cco-domains/cco/ont00001879> [  # designated by → GivenName
        rdf:type cco:ent00000002 ;  # GivenName
        <https://w3id.org/cco-domains/cco/ont00001765> "Dave"  # has text value
    ] .
```

<a id="graph-69"></a>
### Graph 69

#### Overview

This graph is one of the cell's two `topic` entries — Alice's own basic claim identifying the trip itself, backing the cell's derived subject `:Kyoto_Trip_2027` with a real graph claimed by her directly (see Check 18/22), distinct from her agent's own more substantive contribution ([graph 70](#graph-70)). Both topic graphs share the same subject but a different claimant — mirroring the Medical Appointment cell's two "Med. Appt mt." squares (see README.md's Representative Cells diagram), where one topic subject is claimed from each side.

#### Graph

```turtle
<!-- databook:id: alice-kyoto-trip-topic-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-69#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Kyoto_Trip_2027 rdf:type owl:NamedIndividual ;
    rdfs:label "Kyoto Trip, Spring 2027"@en .
```

<a id="graph-70"></a>
### Graph 70

#### Overview

This graph is the cell's other `topic` entry — Alice's travel agent's own evolving understanding of the trip, claimed by the agent rather than by Alice, Dave, or a third `p:Person`/`o:Organization`. This is the agent's single evolving graph — revised in place turn by turn as Alice and her agent go back and forth (see APP-BEHAVIOR.md's Agent Collaboration section), rather than a new graph per conversation turn. There is no dedicated "Trip" domain ontology yet, so this graph stays a minimal label/comment pair — enough to identify the trip as a real resource IRI, per `g:subject`'s open range.

#### Graph

```turtle
<!-- databook:id: alice-travel-agent-kyoto-trip-topic-graph -->
<!-- databook:graph: http://www.example.org/mia/graphs/graph-70#graph -->
@prefix : <http://www.example.org/mia#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Kyoto_Trip_2027 rdfs:comment "Draft itinerary, collaboratively refined turn by turn with Alice's own travel agent: cherry blossom season in Kyoto and Nara, proposed late-March dates, and a shortlist of ryokan lodging near Higashiyama."@en .
```
