---
name: spec
description: Turn a feature request into acceptance criteria sized to the change, before any code - from two lines for a small fix to an interview and Given/When/Then scenarios for a large or risky feature - then plan it and hand test-writing to a separate session. Use when the user describes a new feature, a behaviour change or a bug to fix.
---

# Specify a change

Write down what "done" looks like before code exists, at the size the change deserves. Heavy
specs for small changes are waste (BB-SDD); no spec for a large one means the agent's tests only
confirm what it built (TS-1, TS-3).

**Framework files**: in Claude Code, `${CLAUDE_PLUGIN_ROOT}/templates/`; for other agents,
`../../templates/` from this file. The project's zones are in `docs/risk-zones.md`.

Start by reading the project's quality scenarios and the ADRs on the change's topics (`decide`).
A spec applies them; it never re-decides them. If the change needs a new hard-to-reverse
decision, that is a Proposed ADR first, and a stop for the user.

## 1. Size it

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

Mark anything unanswered `[NEEDS CLARIFICATION]`. Do not plan until every mark is resolved.

## 3. Write the criteria

- Behaviour a person can observe, never implementation ("the list shows only site A's orders",
  not "filter the queryset").
- Each criterion becomes at least one test.
- Include who must **not** be able to do it, when the project has access control.
- For each quality scenario the change touches, at least one criterion exercises it and cites
  it ("QS-5: submitted twice with the same ID, one record") (DC-5).
- Show the criteria to the user and get agreement. Set Status: Agreed.

## 4. Plan

For medium and large changes, create `docs/plans/<name>.md` from the plan template: small
steps, structural changes separate from behaviour changes, each step ending green.

## 5. Hand over

- **Tests first, in a separate session** (TS-3): start a fresh session (or subagent) whose only
  job is to turn the criteria into tests and confirm they fail for the right reason. It must not
  write the implementation. Before handing over, it runs the project's lint and type checks
  on the new tests (TS-7): the only failures left are the intended ones.
- **Offer a tests-only commit** before any implementation. It is the only evidence that
  tests came first (TS-2); commit only if the user agrees.
- **Implementation in a fresh session**: it reads the spec, the plan and the failing tests,
  works step by step, and updates the plan's progress notes. It may not edit the acceptance
  tests; if one looks wrong, it stops and asks.
- **Parallel work** (WK-6): if another session works on this repository at the same time,
  each gets its own worktree and test database.
- **Evidence back up** (`decide`): once the tests pass, the spec is Built, each ADR it
  exercised gets its Evidence, and each scenario it proves updates its "Now".

Report: the size chosen and why, the criteria, open questions, and the next session to start.
