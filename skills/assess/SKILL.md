---
name: assess
description: Audit an existing repository against Agent804 levels, rules and modules, read-only, with evidence, one bounded next action and optional follow-ups. Use to understand the project's position; adopt guides implementation of missing protections on existing code.
---

# Assess a repository

Score a repository against `framework/levels.md` and `framework/rules.md`, with evidence for
every claim. Read-only: never edit, commit or install anything.

Adoption does not require earning a level first. Recommend one useful increment, not a
whole-repository conversion. To carry it out, use `adopt`: Claude Code
`${CLAUDE_PLUGIN_ROOT}/skills/adopt/SKILL.md`, otherwise `../adopt/SKILL.md` from here.
Do not invoke it or create an adoption record during this read-only assessment.

**Framework files**: in Claude Code, `${CLAUDE_PLUGIN_ROOT}/framework/`; for other agents,
`../../framework/` from this file.

Assess TS-2 using actual red/green results and revision/patch evidence, not commit order
alone. Check TS-10/TS-12 at level 1 and TS-1 to TS-4, TS-8/TS-9 where applicable at level 3; report
TS-11 as a practice.
Report isolation, discovery, retry/quarantine and unexecuted target gaps. TS-13 is a practice;
no universal mutation score is required and historical TDD must not be invented.

Keep stage completion distinct from feature completion; no commit history or passing
metadata substitutes for execution evidence.

## Steps

Read host guidance: Claude Code `${CLAUDE_PLUGIN_ROOT}/framework/agents/README.md`, otherwise
`../../framework/agents/README.md` from here. Inspect actual client/version, orchestration,
instruction overrides/loading limits, installed skill resources, effective permissions and
hook trust/load/failure evidence. Report configured vs fixture-tested vs actual-host evidence.
Actual-host evidence comes from records (the project's host record, hook state files, CI
logs); when there are none, say so. Do not install plugins, change trust/global policy or
launch host sessions to create it.
For Grok Build, inspect native versus imported compatibility sources and version-specific
Stop/trust evidence; public and upstream docs differ. Never equate native skill discovery
or a fixture adapter pass with active project permissions or a working completion gate.

1. **Read the framework**: `levels.md`, `modules.md`, `rules.md`, and the profile for the stack if one exists
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
   count as testing, unless the user said strictly read-only, and so does git-ignored output
   the check generates (compiled translations, caches); changing a tracked file does not. If it needs credentials or a
   service that is not available, or running it could write to data the user asked you not
   to touch, run the steps that are safe, name the exact commands you would have run, and do
   not work around it. Test runners that use an in-memory or throwaway database are safe;
   anything that opens the project's own database file is not, when told read-only.
   With no check command, CK-1 is not met; still run the safe pieces that exist (the test
   runner, the linter) one by one to grade the other rules, and say you did. If the tests
   cannot run at all, report why: that is the first gap.
4. **Decide which modules apply.** For each module in `modules.md`, state whether its
   trigger is true and the evidence: an MCP server, agent API, or embedded model feature
   (Operate), the data the system
   holds and who can reach it (Security), signs of several
   concurrent writers (Parallel work), and so on. When the evidence is unclear, ask; when
   nobody can answer, assume and say so.
5. **Go through gates by introduction level** (the practice mapping in `levels.md`), then rules of
   each triggered module, then the other core rules as practices. For each rule: **met**, **partly
   met**, **not met**, **not verifiable** (history cannot show it), **not applicable**, or
   **not assessed (above target)** where evidence was not examined, with the file and line or command
   output that shows it. Do not mark a rule met because a document says it is done; find the
   mechanism. When a grade depends on something you cannot see (a restricted file, a host
   setting, who decided), mark it not verifiable, say what you saw and the question that
   settles it, and ask the owner if you can. Never write a guess as a finding. Steps 7 to
   12 say what to look for in areas where the Check column is not enough.
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

12. **Operate**: when the module applies, grade OP-1 to OP-11. A protocol library or a
    generated wrapper per function is not a designed surface (OP-9). An embedded model
    feature whose prompt and allowlist are not in the repo, or whose output can approve or
    publish, is not met (OP-10). No such feature is not applicable. A forwarded foreign
    token, a skipped per-client consent, or a session used as login is not met (OP-11).

13. **Score it**, only now that every rule is graded, using "Scoring" in `levels.md`: mark
    the highest cumulative core level with every applicable gate met. Partial or missing
    gates block advancement. Unverified gates support only a separately named provisional
    level with assumptions; never present it as earned. Report progress by named practice,
    including lower-level blockers and later strengths. Score triggered modules by their
    own marks (Operate O1–O3); report trial modules without a mark.

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
conditional practices. Missing optional routing or multiple subscriptions never fails a level;
one model in separate contexts remains valid. Do not probe accounts or launch models to score it.

1. **Score**: earned level number and name, target and any additional requirements
   for this kind of project. Ask the two questions in `levels.md` if you can; when nobody can
   answer (a subagent, an unattended run), assume from the brief and state the assumption.
   For example: `Core: Level 2 — Controlled. Target: Level 3 — Verified.` Give any
   provisional level and assumptions separately; Level 0 means no level earned. Show named
   practice progress toward the next level, not a second aggregate score. If the target and
   additions are met, say so and label further advancement optional.
   Then the modules line from `modules.md`, triggered modules first with the reason each
   applies, for example `Modules: Operate O1✓ O2✓* O3◐ · Security ◐ · Parallel ✓`.
2. **Strengths**: rules met well, with evidence. Be specific; no praise without a file reference.
3. **Gaps**, most serious first: rule ID, what is missing, what goes wrong because of it.
   Distinguish "designed but not running" (documented, never exercised) from "absent".
4. **Do next**: one bounded improvement with benefit, scope, rule IDs, rough size and
   observable completion evidence. Recommend guided `adopt` implementation; keep this report
   read-only. Address serious risks first, then unmet additions to the stated target, then
   gates blocking levels that target actually requires. A Level 2 prototype owing only
   TS-1, TS-6 and DC-1 to DC-3 does not need the rest of Level 3 to meet its target.
   Offer at most two **optional follow-ups**; do not make every finding today's backlog.
   Above-target work is not a required gap; urgent module risks need explicit attention.
5. **Not checked**: anything you could not verify and why.
   Include host capability gaps: model name, file presence and automatic tool permission
   review do not establish instruction loading, human consent or enforced completion checks.

Put the score, up to three key gaps (urgent risks explicit) and the one next action in the
first 15 lines; optional follow-ups and full evidence follow. Keep all verified findings
available without implying agreement to fix them now. Do not invent findings.
