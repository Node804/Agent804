---
name: assess
description: Audit an existing repository against the Agent804 rungs, rules and modules, read-only, and report its foundation, coverage and triggered modules with evidence and the next three steps. Use when the user asks how their project or agent setup measures up, where to start improving it, or before adopting the framework on existing code.
---

# Assess a repository

Score a repository against `framework/rungs.md` and `framework/rules.md`, with evidence for
every claim. Read-only: never edit, commit or install anything.

**Framework files**: in Claude Code, `${CLAUDE_PLUGIN_ROOT}/framework/`; for other agents,
`../../framework/` from this file.

Assess TS-2 using actual red/green results and revision/patch evidence, not commit order
alone. Check TS-10/TS-12 at rung 2, TS-11 at rung 4 and TS-8/TS-9 where applicable at rung 5.
Report isolation, discovery, retry/quarantine and unexecuted target gaps. TS-13 is a practice;
no universal mutation score is required and historical TDD must not be invented.

Keep stage completion distinct from feature completion; no commit history or passing
metadata substitutes for execution evidence.

## Steps

Read host guidance: Claude Code `${CLAUDE_PLUGIN_ROOT}/framework/agents/README.md`, otherwise
`../../framework/agents/README.md` from here. Inspect actual client/version, orchestration,
instruction overrides/loading limits, installed skill resources, effective permissions and
hook trust/load/failure evidence. Report configured vs fixture-tested vs actual-host evidence;
do not install plugins, change trust/global policy or launch host sessions to fill gaps.
For Grok Build, inspect native versus imported compatibility sources and version-specific
Stop/trust evidence; public and upstream docs differ. Never equate native skill discovery
or a fixture adapter pass with active project permissions or a working completion gate.

1. **Read the framework**: `rungs.md`, `modules.md`, `rules.md`, and the profile for the stack if one exists
   (`profiles/`). Identify the stack from the lock files and dependency manifests.
   With no profile for the stack, judge each rule by its property, using the table in
   `profiles/README.md`. When a profile covers only part of the stack (a Django backend
   with a separate frontend), use it for that part and judge the rest by property. A profile describes mechanisms; only running ones count as met.
   Grade from the Check column in `rules.md`; inspect the project's own maintainability
   and security records, not the framework's explanations of them.
2. **Read the repository's own instructions**: `AGENTS.md`, `CLAUDE.md`, `.cursor/rules/`,
   `.github/copilot-instructions.md`, nested instruction files, agent settings and hooks.
   Read `.env.example` (or its equivalent) and its comments: it says which settings hold
   secrets and which sources need none. A slot shows a setting exists, never that it is
   set or unset. Only what is in the repository counts; git-ignored
   personal settings do not. Uncommitted
   work counts, and the report says which findings depend on it.
3. **Find the check.** Look for a single check command in the instructions, task runner and CI.
   Run it if it only reads and tests. Tests that create and drop their own throwaway database
   count as testing, unless the user said strictly read-only. If it needs credentials or a
   service that is not available, or running it could write to data the user asked you not
   to touch, run the steps that are safe, name the exact commands you would have run, and do
   not work around it. Test runners that use an in-memory or throwaway database are safe;
   anything that opens the project's own database file is not, when told read-only.
   With no check command, CK-1 is not met; still run the safe pieces that exist (the test
   runner, the linter) one by one to grade the other rules, and say you did. If the tests
   cannot run at all, report why: that is the first gap.
4. **Decide which modules apply.** For each module in `modules.md`, state whether its
   trigger is true and the evidence: an API or MCP server (Operate), the data the system
   holds and who can reach it (Security), signs of several
   concurrent writers (Parallel work), and so on. When the evidence is unclear, ask; when
   nobody can answer, assume and say so.
5. **Go through the gating rules rung by rung** (the table in `rungs.md`), then the rules of
   each triggered module, then the other core rules as practices. For each rule: **met**, **partly
   met**, **not met**, **not verifiable** (history cannot show it), **not applicable**, or
   **above target** (not required for this kind of project), with the file and line or command
   output that shows it. Do not mark a rule met because a document says it is done; find the
   mechanism. When a grade depends on something you cannot see (a restricted file, a host
   setting, who decided), mark it not verifiable, say what you saw and the question that
   settles it, and ask the owner if you can. Never write a guess as a finding. Steps 7 to
   11 say what to look for in areas where the Check column is not enough.
6. **Look at history** for what documents cannot show: `git log` for change size, merge
   commits, branch use, whether tests arrive before or with code, whether there is a remote.
7. **Parallel work and evidence**: when the Parallel work module applies, inspect
   checkout/resource isolation and per-checkout hook state using the worktree playbook (Claude Code `${CLAUDE_PLUGIN_ROOT}/framework/worktrees.md`,
   otherwise `../../framework/worktrees.md` from this file). Check each ADR's evidence
   record, a linked file or an append-only Evidence section (DC-2), including contradictions
   awaiting owner review. Do not edit frozen ADRs in this assessment.
8. **Maintainability**: inspect public contracts and current examples (MT-1); exercised
   complexity checks, review-trigger dispositions and scoped exceptions (MT-2); authoritative
   business rules and boundaries (AR-2, AR-3); retirement evidence (MT-3). A reviewed baseline
   can retain specific debt, but cannot waive controls or permit worsening findings. Do not
   call documentation "met" from presence alone. Treat unused-code and duplication reports as
   leads needing confirmation.
   Report MT-4 refactoring separately as a practice: problem, consumers/contracts, baseline
   and final preservation evidence, improvement and compatibility gaps. A green suite does
   not prove complete equivalence; absence of a standalone refactor skill is not a failure.
9. **Security**: grade SE-2 and SE-3 always, and SE-1, SE-4 to SE-6 when the Security
   module applies, using actual requirements, safe detection evidence,
   dependency trust, effective controls, abuse tests and response/expiry records. Missing,
   incomplete, failed or stale checks are gaps, not clean results. A maintainability baseline
   cannot accept security exposure. Local settings do not verify a deployment. Never read restricted
   production secrets, scan live systems or acquire extra authority to fill an evidence gap.

10. **Style**: grade ST-1 per language the project maintains. The project's own choices
    qualify equally with standard ones; an editor config alone is not enforcement. Do not
    install tools or reformat files to gather evidence.

11. **Human decisions**: grade RV-1 and GR-7 from history: who reviewed what before merge,
    and whether approvals came from the person, in their own words. Metadata cannot establish
    consent. Distinguish session evidence from retrievable authenticated
    reviews, missing host evidence and configured-but-unexercised enforcement. An empty merge
    history is not an exercised human review workflow; never invent evidence to fill it.

12. **Score it**, only now that every rule is graded, using "Scoring" in `rungs.md`: mark
    each rung, then the foundation and the coverage line. Mark each triggered scored module
    the same way (Operate by level); report trial modules without a mark. List any
    not-verifiable rule as an assumption.

## Report

When the Maintenance module applies, report MT-5 (trial). Inspect confirmed consequences, owner,
disposition/review condition, actual deferral authority, linked exceptions and closure evidence
in the canonical record. Scanner candidates are not confirmed debt; a debt label neither
waives a gate nor accepts security/test failures. A clean project needs no invented debt items.

When the Context module applies, report IN-8/WK-8 (trial). Check missing/truncated evidence, stale
indexes/dirty work and assumptions promoted by summaries. Missing context trials stay pending;
do not run model sessions or modify the app to establish them during read-only assessment.

For opted-in routing, inspect the project's `docs/model-routing.md` and records for WK-7/MS-5. Report role,
native effort, access/budget evidence, bounds, fallbacks and actual context independence as
conditional practices. Missing optional routing or multiple subscriptions never fails a rung;
one model in separate contexts remains valid. Do not probe accounts or launch models to score it.

1. **Score**: foundation, the coverage line, the holes in rungs marked `✓*`, and the target
   for this kind of project. Ask the two questions in `rungs.md` if you can; when nobody can
   answer (a subagent, an unattended run), assume from the brief and state the assumption.
   Then the modules line from `modules.md`, triggered modules first with the reason each
   applies, for example `Modules: Operate O1✓ O2✓* O3◐ · Security ◐ · Parallel ✓`.
2. **Strengths**: rules met well, with evidence. Be specific; no praise without a file reference.
3. **Gaps**, most serious first: rule ID, what is missing, what goes wrong because of it.
   Distinguish "designed but not running" (documented, never exercised) from "absent".
4. **Next three steps**: the smallest changes that raise the foundation first, then close the
   gap to the target, each with the rule IDs it satisfies and a rough size (an hour, a day).
5. **Not checked**: anything you could not verify and why.
   Include host capability gaps: model name, file presence and automatic tool permission
   review do not establish instruction loading, human consent or enforced completion checks.

Put the score, the top three gaps and the next three steps in the first 15 lines, so a reader
can stop there; evidence follows. Plain statements; do not soften findings, and do not invent
ones you could not confirm.
