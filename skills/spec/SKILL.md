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
Read `docs/security.md` and security guidance: Claude Code
`${CLAUDE_PLUGIN_ROOT}/framework/security.md`, otherwise `../../framework/security.md` from
this file. Update affected threats, requirement applicability and evidence needs (SE-1).
Security-policy/test/CI/permission changes follow their risk, even in docs or tooling (RV-3).
Read approval policy/source records and guidance: Claude Code
`${CLAUDE_PLUGIN_ROOT}/framework/approvals.md`, otherwise `../../framework/approvals.md` from
this file. Reuse valid scoped decisions; material criteria/architecture/security changes need
renewed affected approval. An approval label, time elapsed or agent-written record is not consent.

## 1. Size it

Pure structural work uses the refactor playbook: Claude Code
`${CLAUDE_PLUGIN_ROOT}/skills/refactor/SKILL.md`, otherwise `../refactor/SKILL.md` from here.
Preserve existing behavior with baseline tests; no invented red failure or new feature spec
is required. Specify intended behavior changes here and retain applicable architecture review.

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
- Cite applicable versioned security requirement IDs and include relevant abuse/bypass paths
  (SE-5), including direct/alternate interfaces and object/tenant access where present. Assert
  no prohibited effect or disclosure, and successful authorized behavior. No security impact
  is a reasoned disposition, not an assumed exemption. Evidence identifies revision and scope.
- Show criteria and reviewable content to the user and get agreement, or resolve an existing
  approval covering that exact scope. Index the real source, reviewer authority, subject,
  conditions and grouped decisions (AP-1 to AP-3); set Agreed only from that decision. Apply
  preauthorized administrative status updates under policy, not repeated approval prompts.
- Assign stable requirement/criterion references and begin the trace (AP-4). Early approval
  must not invent future tests or results; append actual coverage in the plan/PR later.

## 4. Plan

Inspect relevant debt before planning (MT-5): Claude Code
`${CLAUDE_PLUGIN_ROOT}/framework/technical-debt.md`, otherwise `../../framework/technical-debt.md`.
Choose in-scope repayment, separate scheduling or justified retention; preserve approved criteria.
New compromises need real scoped deferral authority and review conditions, not a post-hoc ticket.

Scope retrieval and preserve critical authority/unknowns via Claude Code
`${CLAUDE_PLUGIN_ROOT}/framework/context-management.md`, otherwise
`../../framework/context-management.md` from here. Expand incomplete snippets to enclosing
contracts; summaries and missing search hits cannot resolve a requirement or establish consent.

For medium and large changes, create `docs/plans/<name>.md` from the plan template: small
steps separating intentional red handoff from implementation completion; structural changes
separate from behavior changes. Read testing guidance: Claude Code
`${CLAUDE_PLUGIN_ROOT}/framework/testing.md`, otherwise `../../framework/testing.md` from here.

## 5. Hand over

If optional routing is enabled, read Claude Code `${CLAUDE_PLUGIN_ROOT}/framework/model-routing.md`,
otherwise `../../framework/model-routing.md` from here. Record actual role/model/host/native
effort and input boundaries (WK-7); A/B/C may be the same model in separate contexts. Budget
pressure never permits weaker acceptance protection, automatic launches or paid fallback.

Use the host context contract: Claude Code `${CLAUDE_PLUGIN_ROOT}/framework/agents/README.md`,
otherwise `../../framework/agents/README.md`. A compacted chat or inherited implementation
reasoning alone does not establish independent test authorship; hand off exact artifacts.

- **Tests first, in a separate context** (TS-3): derive acceptance tests from agreed criteria,
  confirm the intended gap on the pre-change revision and preserve command, environment,
  diagnostic and revision/patch evidence (TS-2, TS-9). Independent validity checks pass (TS-7);
  identify expected missing-public-interface diagnostics separately from setup failures.
  A red handoff finishes this stage, not the feature. Existing behavior may already pass;
  report verification honestly instead of manufacturing failure.
- **Preserve the handoff**: a tests-only commit is useful only when authorized, and commit
  order alone proves no execution. A preserved patch/base plus run evidence also suffices.
- **Implementation in a fresh context**: read the criteria, plan and red evidence; supporting
  unit tests are allowed. Explain legitimate test corrections (TS-4); changing acceptance
  outcomes requires criteria review and affected approval. Never weaken tests to get green.
  After green, inspect duplication and structure; make justified behavior-preserving
  refactoring separately where practical (TS-2). Record the disposition, including when none
  is needed, update affected public contracts (MT-1), and remove or explain retired paths
  (MT-3). Stay within the approved scope and the project's complexity limits (MT-2).
  Recover and verify applicable approvals, not just the spec status. Preserve original
  decisions, renew affected material deltas and record actual tests, reviewed implementation
  revision and results in the requirement trace before acceptance.
- **Parallel work** (WK-6): if another session works on this repository at the same time,
  each writer gets its own worktree and isolated resources. Follow the worktree playbook:
  Claude Code `${CLAUDE_PLUGIN_ROOT}/framework/worktrees.md`, otherwise
  `../../framework/worktrees.md` from this file. Sequential test-writing and implementation
  contexts may reuse a checkout. A handoff between worktrees names the exact commit or
  preserved patch; uncommitted tests do not appear in another checkout automatically.
- **Evidence back up** (`decide`): once the tests pass, the spec is Built, each ADR it
  exercised gets an entry in `docs/evidence/<adr-number>-<topic>.md`, and each scenario it
  proves updates its "Now". Accepted ADRs stay frozen and Accepted.

Report: the size chosen and why, the criteria, open questions, and the next session to start.
