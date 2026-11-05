---
name: adopt
description: Guide incremental adoption on existing code, creating and exercising missing instructions, conventions, checks and protections. Use to begin or continue setup; assess diagnoses read-only and start handles empty projects.
---

# Adopt Agent804 on existing code

Implement one useful increment. Assessment is optional; earning a level is not a prerequisite.

**Resources:** Claude Code `${CLAUDE_PLUGIN_ROOT}/framework/` and
`${CLAUDE_PLUGIN_ROOT}/templates/`; otherwise `../../framework/` and `../../templates/`
from this file. Load by step, not the whole kit. For the destination read How much a project
needs in `framework/levels.md`; for applicability read The modules trigger table in
`framework/modules.md`. Load triggered details only for this increment. Retrieve relevant
rule rows from `framework/rules.md` with its opening definitions and family qualifications;
follow applicable cited rule dependencies. Full scoring additionally requires levels.md Scoring and the
complete applicable gates. Use only needed profile mappings, or `profiles/README.md` where
missing; record this increment's unmapped mechanisms as Draft, not a whole-stack conversion.

## 1. Establish and agree one increment

Read project instructions, relevant ADRs, code/checks/CI and assessment/adoption records.
Inspect branch and dirty work; preserve changes and use a task branch (GR-3). Empty projects
use `start`. Revalidate prior evidence; reuse conventions, working tools and answered questions.
Inspect enough for this increment, not a full audit.

Establish missing purpose/impact, prototype or production, stack/host, reviewer, module
triggers and today's scope. Ask remaining questions one at a time with a default/consequence.
Set the destination from levels.md; it is not today's completion condition. Flag immediate
credential/data or destructive-action risks (GR-1, GR-7) without reading secrets or acquiring
live authority. Recommend one improvement with benefit, size, files and observable criteria
(TS-1), plus at most two optional follow-ups. Ask only where existing authorization leaves a
choice. Implement through evidence; report blockers rather than expanding the agreed scope.
Application behavior uses `spec`; standalone restructuring uses `refactor` (MT-4).

## 2. Implement the missing piece

Use only the relevant section and dependencies:

- **Instructions (IN-1, IN-3, CK-2):** merge `templates/AGENTS.md` into existing authority.
  Put actual check commands first, or say none exists. Remove unimplemented template claims,
  preserve local policy, enforce the budget and verify selected-host discovery. For host work
  read the shared checklist, Claude Code `${CLAUDE_PLUGIN_ROOT}/framework/agents/README.md`,
  otherwise `../../framework/agents/README.md`, then only the selected host profile.
- **Style (ST-1):** inspect code/config; retain a deliberate convention or recommend the
  language standard. Agree maintained-language rollout and authority in existing docs/profile.
  Pin reviewed formatter/linter sources in the existing dependency mechanism (SE-3). Separate
  report-only check and fix commands. Show violation/failure without rewriting, targeted fix,
  idempotent second fix; restore fixtures. No competing guide or bulk legacy formatting.
  Legacy/unexamined failures remain visible; ST-1 is partial until required scope is enforced.
- **Check (CK-1, CK-2, TS-10, TS-12):** inventory and reuse format/lint/type/test/complexity/
  security commands; wrap them without a new build system. Agree missing pieces as later
  increments; output/instructions state executed scope and gaps. Propagate failures nonzero;
  checks do not rewrite. Print discovered/executed tests and skips; unexpected empty discovery
  fails. Demonstrate failure propagation and empty-suite behavior in isolation. A deliberately
  partial runner missing required checks exits nonzero: useful setup, incomplete adoption,
  never a full green check. Grade missing mechanisms under their own rules; CK-1 grades the
  runner/CI contract. Document the command first; match claims to current results (GR-4).
  Hooks/`.agent-check` are optional and local execution proves neither CI nor branch protection.
- **Guardrails/CI (GR-1 to GR-4, GR-7, CK-8, RV-1):** read the shared host checklist and
  selected profile as above. Merge authorized action settings, preserve stricter controls and
  prove relevant refusals. Build CI around the existing check and representative journey
  (SK-1, SK-2), not a replacement skeleton. Local green is not review/branch-protection evidence;
  live settings retain their own authority. Only for opted-in supported GR-8 load Claude Code
  `${CLAUDE_PLUGIN_ROOT}/framework/agents/completion.md`, otherwise
  `../../framework/agents/completion.md`; agree runtime/prerequisites before installation.
  No Stop adapter ships in 0.6; do not recreate withdrawn integrations during setup.
- **Current behavior (IN-5):** reuse one area guide or `templates/current-behavior.md`, link
  from instructions and cite inspected sources/tests, revision/patch, scope and gaps. Do not
  imply deployment or document the whole system before a small increment can proceed.
- **Other gaps:** use actual code and relevant Check rows: limits/contracts (MT-1, MT-2),
  boundaries (AR-1, AR-3, AR-6), independent acceptance (TS-3), decision evidence (DC-1 to
  DC-3). Modules follow their triggers/playbooks. Create only records needed now.

For existing maintainability findings, propose a narrow baseline in `maintainability.md`
from the template: exact findings, reason, reviewer and review condition (MT-2). Only a person
accepts it; new work cannot worsen it. Baselines/debt/plans waive no failed tests, missing
controls or security exposure. Separate existing failures; never weaken/skip/delete tests
for green (TS-4).

## 3. Prove, record and resume

Run relevant checks before/after; distinguish negative fixtures, existing/new failures,
skips and unavailable services. Preserve commands/results and reproducible revision/patch
context. Use isolated test data, no production calls or automatic migrations.

Update the existing plan or `docs/agent804-adoption.md` from `templates/adoption.md` (WK-2):
one active increment, linked evidence and a proposed next step. Link rather than copy the
assessment. On continuation recheck state and reuse answers; a stale plan cannot override
the project. Agree the next increment's scope/evidence within existing authorization (GR-7).
Report changes, evidence, gaps, urgent risks and one next action. Use `assess` for a full
score; never extrapolate a level from one increment. Stop at the agreed boundary. Commit,
push, deployment and migration need the developer's specific instruction.
