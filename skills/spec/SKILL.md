---
name: spec
description: Discover missing requirements and interaction outcomes, then agree acceptance criteria sized to the change before code. Use for a feature, behaviour change or bug fix; larger work can pass to plan for verifiable increments before independent test writing.
---

# Specify a change

Agree observable behavior before code; acceptance authors work separately from implementation
(TS-1, TS-3). Scale the records to the change.

**Templates:** Claude Code `${CLAUDE_PLUGIN_ROOT}/templates/`; other agents `../../templates/`
from this file. Load only the template needed at the chosen size, not the full framework.

## 1. Establish the baseline and size

Read affected current behavior and verify relevant code/config/tests (IN-5). Reuse README/
contracts; if missing, establish only needed scope, optionally using `current-behavior.md`.
Keep unknowns/defects explicit, intended contracts intact and deployment unclaimed.
Read applicable quality scenarios, ADRs, risk zones, security and debt records; update
affected threats in the security record (SE-1). Follow
Accepted decisions; a new hard-to-reverse choice requires a Proposed ADR through `decide`
and resolution before dependent work. Do not silently re-decide it.

| Size | Scope | Record |
|---|---|---|
| Small | Clear fix, label, field, one query | One or two criteria in plan/PR; no spec file or extra discovery artifact |
| Medium | One screen/endpoint/rule/module | Short interview and `docs/specs/<name>.md` from template |
| Large | Several modules, new concept/data model or red zone | Full interview, scenarios/refusals and an ADR for hard-to-reverse choices |

A red-zone change is never small. Ask when size is uncertain. Pure restructuring uses
`refactor`: Claude Code `${CLAUDE_PLUGIN_ROOT}/skills/refactor/SKILL.md`; otherwise
`../refactor/SKILL.md` from here.

## 2. Discover missing requirements (medium/large)

Reuse facts/answers; ask only consequential unknowns, one question at a time with a suggested
default. Establish who needs it, today's behavior, problem/desired observable improvement,
out-of-scope actions, success/error/refusal outcomes, preserved behavior and constraints/
integrations/data/decisions that change the answer.
For interactions, walk entry to outcome, relevant empty/loading/error/refusal/recovery states,
permissions and accessibility. Reuse design conventions. A sketch may settle ambiguity; it
is a proposal, not agreement or evidence. Use relevant prompts, not a universal checklist.
Cite factual sources, distinguish proposed assumptions from agreed choices, and ask about
consequential assumptions. Mark unresolved answers `[NEEDS CLARIFICATION]` (TS-6); resolve
all marks before planning.

## 3. Agree criteria

- Compare baseline: added, changed, removed and preserved behavior; one sentence can suffice
  for small work. Proposals stay in the change record until delivered.
- State observable outcomes, never implementation. Each criterion gets at least one test;
  include relevant refusal/access boundaries, failures and effects. Cite applicable quality
  scenarios. Security changes include abuse/bypass tests (SE-5); explain any no-impact judgment.
- MCP/agent APIs and embedded models declare effect, forbidden results and output that cannot
  approve/publish (OP-9, OP-10); use `operate` for that surface.
- Show criteria to the developer and retain their agreement in their own words (GR-7).
  Material changes return for agreement; an agent-written status cannot supply it.

## 4. Plan and hand off

Inspect consumers/contracts and debt relevant to the change; repay in scope, schedule or
leave with a reason. A new shortcut needs the person's agreement. Keep reasons/evidence
traceable; an unread summary or search miss is not complete coverage.
Medium/large work uses the existing plan or `docs/plans/<name>.md` (WK-2); separate structural
and behavior steps. For dependent changes/handoffs use `plan`: Claude Code
`${CLAUDE_PLUGIN_ROOT}/skills/plan/SKILL.md`; otherwise `../plan/SKILL.md`. Reuse agreed records.

- **Independent tests first (TS-3):** a separate session/subagent derives tests from agreed
  criteria and existing contracts, without new implementation. Run them before implementation
  and retain intended red output (TS-2, TS-9). Validity checks pass first (TS-7): a specific
  planned missing-interface compiler diagnostic may be expected red; unrelated syntax,
  dependencies, fixture or environment errors are not. Already-passing behavior stays reported
  as passing. A red handoff completes the test stage, not the feature.
- **Exact handoff:** criteria, tests, revision/patch and actual commands/results, not a summary
  saying tests ran. Fresh implementation context receives these (WK-3); supporting unit tests
  are allowed. Never edit acceptance tests to fit code; suspected wrong expectations return to
  the developer (TS-4). After green, refactor where useful or note none needed; update public
  contracts (MT-1), retire replaced paths (MT-3) and respect limits (MT-2).
- **Optional coordination:** follow existing routing records and record the model per role (WK-7);
  one model in separate contexts is enough. Concurrent writers need separate checkout/resources and exact patch/commit handoffs
  (WK-6); uncommitted files do not appear in another worktree. Neither plan nor skill launches
  sessions or grants commit authority.
- **Evidence back up (`decide`):** once tests pass, mark the spec Built and update evidence for
  exercised ADRs/scenarios with actual scope/results. Accepted ADR text/status stays frozen;
  later evidence goes in its linked record and scenario “Now” records exercised outcomes.
- **Reconcile current behavior (IN-5):** update its existing home with verified outcomes,
  source/test links, revision/patch and limits. Partial delivery names implemented scope;
  pending work stays proposed. Preserve historical records and never infer deployment.

Report size/reason, criteria, open questions and next session. Small work needs no framework
table, host recipe, planning skill or new artifact unless its actual risk/dependencies require it.
