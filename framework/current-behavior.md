# Current behavior and historical records

A maintainer's usual question is "what does this do now?" Reconstructing the answer from
feature specs, ADR amendments and dated evidence costs context and can revive obsolete
requirements. IN-5 makes a maintained description the entry point; history supplies reasons
and traceability when needed. This extends existing documentation practice, not the levels.

## Three different questions

| Record | Answers | Changes when |
|---|---|---|
| Current behavior description | What does this area do, for whom, with which limits? | The described behavior changes |
| Change spec and plan | What are we proposing, preserving and verifying? | The agreed work evolves |
| ADRs and evidence | Why this choice, and what was demonstrated at a particular revision? | A decision is superseded or new evidence is appended |

An Accepted ADR is a governing decision, not proof of implementation. A Built feature spec
is a record of that delivery, not a promise that later work preserved all its behavior.
Neither has to be rewritten to explain today's system. Git retains earlier versions of the
maintained description; a second chronology inside it would recreate the retrieval problem.

## One maintained home per area

A README section or existing contract guide can suffice. Larger systems may use
`docs/system/<area>.md`, with a short map from project instructions. The optional
[template](../templates/current-behavior.md) covers externally observable behavior, actors,
refusals, limits, dependencies and relevant configuration, with source and test references.
It does not require a function inventory, copied code or a new document for every change.
Active decision links identify governing constraints without repeating their rationale.

Repository behavior and deployed behavior can differ by release, configuration or feature
flag. A useful description identifies its scope and last verification basis. It does not
claim deployment knowledge from a local test, or accuracy merely from a recent timestamp.
Unverified areas and known differences remain visible. A factual observation of a defect
does not replace the intended contract or authorize accepting the defect.

## Change and reconciliation

The existing `spec` workflow compares the current description with affected code and tests,
then records added, changed, removed and preserved behavior in the change's criteria. Pending
work stays in that change record. After verification, the maintained description reflects
the resulting behavior and links the actual evidence. Partial delivery describes only the
verified portion; proposed or unbuilt behavior is not promoted as current. Fresh review
checks the reconciliation alongside the implementation. History remains available by link.

For existing code, adoption can establish one useful area from inspected sources, expanding
as work touches other areas. There is no prerequisite to document the whole system. Gardening
can find drift later, but does not replace updating the description in the behavior change.

## Evidence limits

This workflow draws on OpenSpec's separation of current specs from proposed deltas; consulted
sources and pending trials are recorded in [validation](validation/current-behavior.md).
Kit integrity checks establish consistency, not freshness, agent retrieval quality or lower
maintenance cost. No external CLI, new skill, gate or module is required.
