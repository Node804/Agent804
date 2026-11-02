---
name: adopt
description: Guide an existing project into Agent804 incrementally, creating and exercising missing instructions, style conventions, checks and other protections with the developer. Use to begin or continue adoption on existing code; assess is a read-only diagnosis and start is for new projects.
---

# Adopt Agent804 on existing code

Build missing pieces one useful increment at a time. Assessment is optional input.
A project can use Agent804 before Level 1; do not require every finding repaired first.

**Resources**: Claude Code `${CLAUDE_PLUGIN_ROOT}/framework/` and
`${CLAUDE_PLUGIN_ROOT}/templates/`; otherwise `../../framework/` and `../../templates/`
from this file. Read `framework/levels.md`, `framework/modules.md` and the relevant checks
in `framework/rules.md`. Use `profiles/README.md` and available profiles for mechanisms.
With no profile, record only this increment's mechanisms as Draft; defer full mapping.

## 1. Find the current position

- Read project instructions, applicable ADRs, existing checks/configuration/CI and any
  assessment or adoption record. Inspect branch and dirty work; preserve others' changes.
  Work on a task branch (GR-3). Empty projects go to `start`, not this workflow.
- Inspect what exists before proposing replacements. Reuse the project's conventions,
  runner, CI, dependency manager and records where they serve the required property.
- Revalidate relevant assessment evidence against current files. Without an assessment,
  inspect enough for this increment; do not turn adoption into an unrequested full audit.
- Establish unanswered context: purpose, impact and prototype/production; stack and
  agent host; who reviews; module triggers; the time or change scope available today.
  Ask one question at a time with a default and consequence; reuse prior answers.
  Set a destination from `levels.md`; it is not today's completion condition.
- Flag an immediate credential/data or destructive-action risk before proceeding (GR-1,
  GR-7). Do not read restricted secrets or acquire live authority to investigate it.

## 2. Agree one increment

Recommend one improvement: benefit, size, files touched and proof. Offer up to two later
possibilities, not a mandatory backlog. One increment can include several dependent steps.
Ask only when existing authorization does not settle the scope.

Record proportionate criteria before implementation (TS-1). Continue the work through
configuration, implementation and evidence; a recommendation alone does not finish it.
If it needs more time or authority than agreed, record the blocker and resume point rather
than expanding into a full migration. Changes to application behavior use `spec`; standalone
restructuring uses `refactor` (MT-4), not cleanup hidden inside setup.

## 3. Walk through the missing piece

Use only the section needed for the increment.

**Instructions missing (IN-1, IN-3, CK-2).** Merge concise project guidance from the
`AGENTS.md` template into the existing authority. Put real commands first; say when a command
does not exist yet. Remove template claims about controls not implemented. Preserve local
policy and verify host discovery rather than treating file presence as enforcement.

**Style guidance or enforcement missing (ST-1).** Inspect code and existing configuration.
Ask whether to retain a deliberate convention or use the language standard; recommend
the standard when no choice exists. Agree maintained-language scope and rollout; record its authority
in existing docs or the stack profile. Pin a compatible formatter/linter in the project's
dependency mechanism, with reviewed sources (SE-3). Configure report-only check and separate
fix commands. Avoid a second competing style guide if configuration already defines it.
Show a deliberate violation failing without rewriting files, a targeted fix, then an
idempotent second fix. Restore the fixture afterwards. Do not bulk-format legacy code.
Legacy style failures stay visible; any staged scope is explicit and unexamined areas remain
gaps. ST-1 is partial until all maintained languages and required scope are enforced.

**One check command missing (CK-1, CK-2, TS-10, TS-12).** Inventory existing format, lint,
type, test, complexity and security commands, then create a runner suited to the stack.
Keep existing working commands; do not introduce a new build system just to wrap them.
Agree unavailable pieces as later increments. Report the runner's scope and missing checks
in its output and instructions; its documented scope matches what it actually executes.
Propagate each failure to a nonzero exit; format/lint check steps must not rewrite files.
Report discovered/executed tests and skips; unexpected empty discovery fails. No tests means
a visible gap, not successful verification. Run available checks safely, and demonstrate
failure propagation and the empty-suite case in isolation. A deliberately partial runner
with missing required checks exits nonzero; it can still be useful setup work, but report
adoption incomplete and never claim the full check green. Grade missing pieces once under
their own rules; grade CK-1 separately for the runner/CI contract. Put the command in
project instructions. Install `.agent-check`/completion integration only with truthful
failure reporting; local execution alone does not prove CI or host enforcement.

**Guardrails or CI missing (GR-1 to GR-4, GR-7, CK-8, RV-1).** Read the host checklist:
Claude Code `${CLAUDE_PLUGIN_ROOT}/framework/agents/README.md`, otherwise
`../../framework/agents/README.md`. Merge configuration, exercise a safe blocked failure, and record
configured versus exercised controls. Create CI around the actual check and an existing
representative journey rather than rebuilding the app as a skeleton (SK-1, SK-2). A green
local run is not branch protection or human review. Live settings need their own authority.

**Other gaps.** Work from the relevant rule's Check column and actual code. Help set
stack-appropriate complexity/size/duplication limits (MT-2), retain or clarify public
contracts (MT-1), add boundary checks (AR-1, AR-3, AR-6), establish independent acceptance
contexts (TS-3), or create decision evidence (DC-1 to DC-3). Module work follows its trigger
and existing playbook. Create only records needed now, not every template directory.

Existing findings do not require a wholesale cleanup. For maintainability, propose a narrow
baseline with exact findings, reason, reviewer and review condition in `maintainability.md`
from the template (MT-2); only a person accepts it. New work cannot worsen it. A baseline,
debt item or adoption plan cannot waive failed tests, missing controls or security findings.
Report pre-existing failures separately; do not skip, weaken or delete tests for green (TS-4).

## 4. Prove, record and resume

Run relevant checks before and after the increment. Distinguish expected negative fixture
results, existing failures, new failures, skips and unavailable services. Preserve the
commands/results and enough revision or patch context to reproduce them. Use safe isolated
test data; no production calls or automatic migrations to prove setup.

Update the project plan or `docs/agent804-adoption.md` from `templates/adoption.md` (WK-2).
Keep one active increment, linked evidence and a proposed next step; link the assessment
instead of copying its gaps. A continuation rechecks current state and skips answered
questions. That proposal is not authorization: agree its scope and evidence before
implementing it (GR-7). A stale plan never overrides the project.

Report changes, evidence, remaining gaps and one next action. Name
urgent risks separately. Use `assess` for a full score when useful; do not invent an overall
level from this increment. Updated score claims must follow the full `levels.md` gates.
Stop at the agreed boundary. Never commit, push, deploy or migrate without the developer's
specific instruction (GR-7).
