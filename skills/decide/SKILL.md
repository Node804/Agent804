---
name: decide
description: Record architecture decision records (which way, and why) with the Proposed / Validated / Accepted / Rejected lifecycle, and record evidence back once a feature's tests pass. Use when a change may need a hard-to-reverse decision, contradicts an accepted one, when the user asks for an ADR, or after a spec's tests pass.
---

# Record a decision

An ADR records a hard-to-reverse decision: which way, and why (DC-1 to DC-3). A spec applies
the ADRs to one feature and makes them testable (`spec`). Tests passing make the spec Built
and may validate a Proposed ADR; an Accepted ADR stays Accepted.

Some projects also state system-wide qualities as measurable scenarios that ADRs serve. If
the project has them, read and cite them; adding one is the user's call.

**Framework files**: in Claude Code, `${CLAUDE_PLUGIN_ROOT}/templates/`; for other agents,
`../../templates/` from this file (`adr.md`, `evidence.md`).

## Read before deciding

Read the ADRs on the change's topics. An Accepted ADR is a
rule: follow it, or propose an amending ADR. Never work around it quietly.
Only a person accepts an ADR, in their own words (GR-7).

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
   that keeps a final Evidence section in each ADR keeps doing so; it only ever grows. Context: facts and forces, and
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

| ADR status | Requires |
|---|---|
| Validated | Linked evidence record as above, citing the acceptance tests |
| Accepted | A person's own decision on this version (GR-7). Decision text frozen from here |
| Rejected | Linked evidence says why. Keep the ADR and evidence: they stop the next person trying again |
| Superseded by NNNN | The new ADR exists and names this one |

A project may run a shorter lifecycle (Proposed, Accepted, Superseded) with evidence gathered
while Proposed; follow the project's own rule. If it keeps an index of ADRs, regenerate it.
Report what you recorded and what is still not tested.
