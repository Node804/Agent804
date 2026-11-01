---
name: spec
description: Turn a feature request into acceptance criteria sized to the change, before any code - from two lines for a small fix to an interview and Given/When/Then scenarios for a large or risky feature - then plan it and hand test-writing to a separate session. Use when the user describes a new feature, a behaviour change or a bug to fix.
---

# Specify a change

Write down what "done" looks like before code exists, at the size the change deserves. A heavy
spec for a small change is waste; no spec for a large one means the agent's tests only confirm
what it built (TS-1, TS-3).

**Templates**: in Claude Code, `${CLAUDE_PLUGIN_ROOT}/templates/`; for other agents,
`../../templates/` from this file.

## 0. Read the project's records

- Quality scenarios and the ADRs on the change's topics (`decide`). A spec applies them; it
  never re-decides them. A new hard-to-reverse decision is a Proposed ADR first, and a stop.
- `docs/risk-zones.md`.
- If they exist: `docs/security.md` (update the threats this change affects, SE-1),
  `docs/approvals/README.md` (who must agree to what), and the project's debt record.

## 1. Size it

Pure restructuring with no behaviour change uses the `refactor` skill instead: Claude Code
`${CLAUDE_PLUGIN_ROOT}/skills/refactor/SKILL.md`, otherwise `../refactor/SKILL.md` from here.

| Size | Looks like | Spec |
|---|---|---|
| Small | A bug with a clear cause, a field, a label, one query | No file. One or two acceptance criteria in the plan or PR, as tests |
| Medium | One screen or endpoint, one rule, touches one module | `docs/specs/<name>.md` from the template, short interview |
| Large | Several modules, a new concept, data model change, or anything in a red zone | Full interview, a scenario per path, refusal paths, an ADR if it is hard to reverse |

A change in a red zone is never small. When unsure, ask the user which it is.

## 2. Interview (medium and large)

One question at a time, offering a default:
- Who needs this, and what do they do today without it?
- What must it **not** do? (This becomes "Out of scope".)
- What does the person see when it works? When they are not allowed? When the input is wrong?
- What existing behaviour must not change?

Mark anything unanswered `[NEEDS CLARIFICATION]` (TS-6). Do not plan until every mark is resolved.

## 3. Write the criteria

- Behaviour a person can observe, never implementation ("the list shows only site A's orders",
  not "filter the queryset").
- Each criterion becomes at least one test.
- Include who must **not** be able to do it, when the project has access control.
- For each quality scenario the change touches, at least one criterion exercises it and cites
  it ("QS-5: submitted twice with the same ID, one record") (DC-5).
- Security: include the abuse and bypass paths that apply (another tenant's object, a direct
  API call, bad input), each asserting nothing forbidden happens (SE-5). "No security impact"
  needs a reason.
- Show the criteria to the user and get agreement in their own words (GR-7). If the Approvals
  module applies, record who agreed, to which version, and any conditions (AP-1 to AP-3).

## 4. Plan

- Check the debt record for items in the area; repay in scope, schedule separately, or leave
  with a reason. A new shortcut needs a person's agreement, not a ticket written afterwards.
- Read the code the change touches, with its callers and configuration. A search with no hits
  or a summary is a pointer, not proof.
- For medium and large changes, create `docs/plans/<name>.md` from the plan template (WK-2):
  small steps, with structural changes separate from behaviour changes.

## 5. Hand over

- **Tests first, in a separate context** (TS-3): another session or subagent writes the
  acceptance tests from the agreed criteria, without the implementation, and runs them on the
  current code to show they fail for the intended reason. Record the command and output
  (TS-2, TS-9). The tests must type-check and lint (TS-7). Behaviour that already passes is
  reported as passing, not forced to fail. A red handoff ends this stage, not the feature.
- **Hand over exact artifacts**: the criteria, the tests, the revision or patch and the red
  output. A summarised chat is not a handoff.
- **Implementation in a fresh context** (WK-3): read the criteria, plan and red output; supporting
  unit tests are allowed. Never edit the acceptance tests to fit the code; a test that looks
  wrong goes back to the user (TS-4). After green, refactor where it helps (TS-2), update
  public contracts (MT-1), remove retired paths (MT-3) and stay within complexity limits (MT-2).
- **Routing**: if the project has `docs/model-routing.md`, use it and record the model each
  role actually used (WK-7). One model in separate contexts is enough.
- **Parallel work** (WK-6): if another session writes to this repository at the same time,
  each writer gets its own worktree and resources (`docs/worktrees.md`). Uncommitted tests do
  not appear in another checkout; hand over a commit or a patch.
- **Evidence back up** (`decide`): once the tests pass, the spec is Built, each ADR it
  exercised gets an entry in `docs/evidence/<adr-number>-<topic>.md`, and each scenario it
  proves updates its "Now". Accepted ADRs stay frozen and Accepted.

Report: the size chosen and why, the criteria, open questions, and the next session to start.
