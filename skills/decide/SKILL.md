---
name: decide
description: Record quality scenarios (what must always be true of the system, measurably) and architecture decision records (which way it is achieved, and why), with the Proposed / Validated / Accepted / Rejected lifecycle, and record evidence back on both once a feature's tests pass. Use when a change may need a hard-to-reverse decision, contradicts an accepted one, adds a system-wide quality requirement, when the user asks for an ADR, or after a spec's tests pass.
---

# Record a decision

Three layers sit above the code, and each has one job:

| Layer | Answers | Example | How many |
|---|---|---|---|
| **Quality scenario** (`QS-n`) | What must always be true of the system, measurably? | QS-5: the same action submitted twice creates one record | Few, stable (DC-5) |
| **ADR** | Which way do we achieve it, and why? | Write operations take a request ID; a repeat changes nothing | Tens (DC-1 to DC-4) |
| **Spec** | What does this feature do, and how do we know it is done? | Retrying a label print with the same ID prints once | One per change (`spec`) |

A scenario says *what*, an ADR says *how*, a spec *applies* both to one feature and makes them
testable. Evidence flows back up: tests pass, the spec is Built, the ADR is Validated, the
scenario is Met.

**Framework files**: in Claude Code, `${CLAUDE_PLUGIN_ROOT}/templates/`; for other agents,
`../../templates/` from this file (`adr.md`, `quality-scenarios.md`).

## Read before deciding

Read the project's quality scenarios and the ADRs on the change's topics. An Accepted ADR is a
rule: follow it, or propose an amending ADR. Never work around it quietly.

## Is it a quality scenario?

Rarely. Only when a requirement applies across the system and would shape the architecture
("a plant keeps working with its WAN down", "no request waits on an outside system"). Most
requirements are spec criteria. A new scenario gets the next `QS-n` (never reused), the
situation, the required response, how it is measured (the spec whose tests prove it, or "no
spec yet"), the ADRs that serve it, and "Not yet". Ask the user before adding one: scenarios are
what the system is judged against.

## Is it an ADR?

Yes if reversing it later would mean a migration, a rewrite, or breaking someone who depends on
it: a data store, an access model, a public contract, a module boundary, a hosting choice. No if
it is a design detail of one feature (put it in the plan's "Decisions made while building") or
a preference (put it in `AGENTS.md` or a lint rule). If the draft passes about 120 lines, it is
probably a spec; split it.

## New decision

1. If an existing ADR covers the topic, this is an amendment: write a new ADR that amends or
   supersedes it.
2. Copy `adr.md` with the next number. Title is the decision as a sentence.
3. Context: facts and forces, the quality scenarios it serves (`QS-n`), and what went wrong
   before. Decision: numbered, each checkable. Consequences: what becomes a rule, and which
   check will enforce it.
4. Status: Proposed. Deciders: the people who will own it, not only the author.
5. Stop and show the user. Do not build on a Proposed ADR until they say to.

## Evidence and status

After a spec's tests pass:
- **ADR:** add to its Evidence section what the tests showed, what **contradicted** the
  decision, what was **learned**, and what was **not tested or not built**. Exercising means
  testing how it could fail (the outside system is down, the user lacks access, the request is
  repeated), not only that it was built.
- **Scenario:** update "Now" only from passing tests, and say what part is met ("Met for API
  writes; web forms not yet"). Never mark one Met because code exists.

| ADR status | Requires |
|---|---|
| Validated | Evidence as above, linked to the acceptance tests |
| Accepted | The owners agreed. Frozen from here except Status and Topics |
| Rejected | Evidence says why. Keep the file: the reason stops the next person trying again |
| Superseded by NNNN | The new ADR exists and names this one |

A project may run a shorter lifecycle (Proposed, Accepted, Superseded) with evidence gathered
while Proposed; follow the project's own rule. If it keeps an index of ADRs, regenerate it.
Report what you recorded and what is still not tested.
