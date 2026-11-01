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
testable. Tests passing make the spec Built, may validate a Proposed ADR, and update only the
part of a scenario those tests prove. An Accepted ADR stays Accepted.

**Framework files**: in Claude Code, `${CLAUDE_PLUGIN_ROOT}/templates/`; for other agents,
`../../templates/` from this file (`adr.md`, `evidence.md`, `quality-scenarios.md`).

## Read before deciding

Read the project's quality scenarios and the ADRs on the change's topics. An Accepted ADR is a
rule: follow it, or propose an amending ADR. Never work around it quietly.
Only a person accepts an ADR, in their own words (GR-7).

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
3. Create its evidence record before acceptance (DC-2): by default
   `docs/evidence/<adr-number>-<topic>.md` from `evidence.md`, linked from the ADR. A project
   that keeps a final Evidence section in each ADR keeps doing so; it only ever grows. Context: facts and forces, the quality scenarios it serves (`QS-n`), and
   what went wrong before. Decision: numbered, each checkable. Consequences: what becomes a
   rule, and which check will enforce it.
4. Status: Proposed. Deciders: the people who will own it, not only the author.
5. Show the reviewable decision and requested transition to the user, unless existing valid
   consent already covers it. Do not build on Proposed without authorization. Note where
   the owners' decision is (their message, a review); Deciders names alone are not consent.

## Evidence and status

After a spec's tests pass:

Record environment, discovered/executed scope,
actual results and skips/exclusions (TS-12); unexecuted quality/security boundaries remain
unverified. A green subset cannot validate an entire architecture decision.

- **Evidence record:** append to the ADR's evidence record what the tests showed,
  what **contradicted** the decision, what was **learned**, and what was **not tested or built**. Exercising means
  testing how it could fail (the outside system is down, the user lacks access, the request is
  repeated), not only that it was built. Include the spec, test paths, exact revision or
  preserved patch, command and result. Keep prior entries; correct them with a later entry.
- **ADR:** a Proposed record may become Validated when its decision has been exercised.
  An Accepted record stays Accepted and its decision text frozen; later evidence changes
  only the evidence record. Contradictory evidence triggers owner review and an amending or superseding ADR
  when needed, never an automatic downgrade or quiet rewrite.
- **Scenario:** update "Now" only from passing tests, and say what part is met ("Met for API
  writes; web forms not yet"). Never mark one Met because code exists.

| ADR status | Requires |
|---|---|
| Validated | Linked evidence record as above, citing the acceptance tests |
| Accepted | The owners' own decision on this version (DC-4). Decision text frozen from here |
| Rejected | Linked evidence says why. Keep the ADR and evidence: they stop the next person trying again |
| Superseded by NNNN | The new ADR exists and names this one |

A project may run a shorter lifecycle (Proposed, Accepted, Superseded) with evidence gathered
while Proposed; follow the project's own rule. If it keeps an index of ADRs, regenerate it.
Report what you recorded and what is still not tested.

## Moving to separate evidence files (optional)

An append-only Evidence section already meets DC-2; move only if the project wants files.
For a frozen ADR with inline evidence or no evidence link, create its separate record with a
backlink to the ADR. Preserve any earlier evidence verbatim with its source revision; do not
invent missing results. Add the ADR-to-record mapping to `docs/evidence/index.md` without
editing the frozen ADR. Later results append to the record. New ADRs link their records
before acceptance; migrated ADRs are located through the index.

