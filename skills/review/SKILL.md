---
name: review
description: Review a change (uncommitted work, a branch or a pull request) in a fresh context, working back from its acceptance criteria and the project's rules, with depth set by risk zone. Reports findings only, never edits. Use before a merge or when the user asks for a review.
---

# Review a change

A second look from a context that did not write the code (RV-2), aimed where damage is likely
(RV-3). Report only: never edit, commit or push. Run this in a fresh session or subagent, not
in the one that wrote the change.

## Steps

1. **Get the change**: the diff against the base branch, plus uncommitted and untracked files,
   or the pull request or paths given.
2. **Get the intent**: the spec in `docs/specs/` or the PR description. If there are no
   acceptance criteria, say so first: the review can only check rules, not correctness.
3. **Get the zones** from `docs/risk-zones.md`. Spend most of the effort on red, then yellow.
4. **Read the rules**: the root `AGENTS.md` and the `AGENTS.md` of every directory touched.
   Read the project's `docs/maintainability.md` and the guidance: Claude Code
   `${CLAUDE_PLUGIN_ROOT}/framework/maintainability.md`, otherwise
   `../../framework/maintainability.md` from this file. Compare findings with the reviewed
   baseline and scoped exceptions; moving a violation does not make it new or erase it.
   Read `docs/security.md` and security guidance: Claude Code
   `${CLAUDE_PLUGIN_ROOT}/framework/security.md`, otherwise `../../framework/security.md` from
   this file. Check exposure changes, versioned requirements, blocking policy and expiry.
   Read declared project conventions and style guidance: Claude Code
   `${CLAUDE_PLUGIN_ROOT}/framework/style.md`, otherwise `../../framework/style.md` from this
   file. Assess project choices, not whether they match the framework's optional defaults.
   Read approval policy/index and guidance: Claude Code
   `${CLAUDE_PLUGIN_ROOT}/framework/approvals.md`, otherwise `../../framework/approvals.md`
   from this file. Verify required subjects, human sources/authority, scope and freshness.
5. **Check, in this order**:
   - **Criteria**: each acceptance criterion has a test, and the code does what it says. Look
     for refusal paths (the user without access, bad input, the outside system down).
   - **Tests** (TS-2, TS-4, TS-7 to TS-12): verify meaningful pre-change failure for changed
     behavior and bug regressions, independent assertions, justified test corrections, real
     integration boundaries, isolation and full discovery/results. Existing passing tests
     remain useful. Inspect retries, skips/quarantine and unavailable targets as explicit gaps.
     Read testing guidance: Claude Code `${CLAUDE_PLUGIN_ROOT}/framework/testing.md`, otherwise
     `../../framework/testing.md` from here. TS-13 sensitivity evidence is a practice, not a gate.
   - **Scope**: features nobody asked for (KB); changes outside the plan.
   - **Approvals/trace** (AP-1 to AP-4): original human decisions match required subjects and
     conditions; material changes renewed affected reviews, unrelated edits did not. Trace
     requirements through criteria, actual tests, reviewed revision and results. Agent review
     or mechanical record checks cannot replace required human implementation review (RV-1).
   - **Rules**: each rule in `AGENTS.md` that the change could break.
   - **Maintainability**: useful public contracts (MT-1); complexity limits and dispositions
     for new or worsening review triggers (MT-2); authoritative business rules (AR-2), cohesive
     boundaries and cycles (AR-3); existing capabilities before custom replacements or new
     dependencies (SK-3); and removed or explicitly retained obsolete paths (MT-3). Confirm
     duplication and unused-code reports against actual consumers before proposing changes.
     Check red/green/refactor disposition (TS-2); "no refactor needed" is a valid result.
     For structural work (MT-4), inspect the stated maintenance problem, affected consumers
     and preserved contracts, baseline/characterization tests and final results. Flag hidden
     behavior changes and unverified compatibility. Green tests prove only exercised scope;
     characterization tests need no artificial red witness. MT-4 itself remains a practice.
   - **Security**: threats/control mapping (SE-1), current complete checks (SE-2), intended
     dependency sources and build authority (SE-3), safe defaults and truthful deployment
     evidence (SE-4), abuse/bypass tests (SE-5), and owner/deadlines/expiry (SE-6). Check object
     and tenant authorization, unsafe sinks and agent-tool authority where applicable.
     Security gates/tests or approval policy weakened without explicit human review are
     findings; a scanner baseline or suppressed exit code does not accept risk.
   - **Style policy** (ST-1 to ST-3): unexpected config/version changes, conflicting tools,
     missing language/grammar coverage, broad exclusions, unreviewed overrides and unrelated
     formatting churn. Inspect migration scope and CI/editor agreement; authored code beside
     generated UI output still needs coverage. Do not recommend replacing a valid custom style.
   - **Red zones**: every line.
6. **Confirm each finding** by reading the code around it. Drop anything you cannot confirm.

Skip layout owned by automation. Naming, interface clarity and documentation meaning remain
reviewable when tools cannot judge them (RV-2). Drop findings about impossible cases (RV-5).
Do not infer maintainability from comment counts or file size alone. Report a breached
contract, unresolved threshold, duplicated authority or concrete maintenance consequence.

## Report

Inspect debt dispositions (MT-5): Claude Code `${CLAUDE_PLUGIN_ROOT}/framework/technical-debt.md`,
otherwise `../../framework/technical-debt.md`. Confirm new compromises were reviewed, deferred
scope has actual authority/review conditions, and closure meets stated outcomes. Tickets do
not waive gates, unmet criteria or security/test findings; partial repayment keeps remaining
scope open. Report MT-5 as a practice, without inventing debt from stylistic preferences.

Apply context guidance: Claude Code `${CLAUDE_PLUGIN_ROOT}/framework/context-management.md`,
otherwise `../../framework/context-management.md` from here. Verify source/revision and enough
enclosing caller/config/exception context; resolve necessary truncated ranges or report the
uninspected scope. An author's summary or stale index is not evidence the current diff is clean.

When optional routing is used (WK-7), compare actual role/model/host/effort and inherited
inputs with the proposed handoff. Read Claude Code `${CLAUDE_PLUGIN_ROOT}/framework/model-routing.md`,
otherwise `../../framework/model-routing.md` from here. Different models agreeing is not
correctness; require concrete counterexamples for findings and actual execution evidence.
No finding quota or majority vote replaces approved criteria and human review.

Check the review context's actual inputs against the host contract: Claude Code
`${CLAUDE_PLUGIN_ROOT}/framework/agents/README.md`, otherwise `../../framework/agents/README.md`
from here. Compaction or a fork label alone is not independence. Report inherited author
conclusions as a review limitation; don't claim tests or host controls you could not exercise.

Findings, most serious first: `path:line`, what breaks, who sees what (a concrete failure, not
"could be an issue"), and which criterion or rule it breaks. Then:
- criteria with no test;
- a mistake that will recur, with the check that would prevent it (hand it to `sensor`);
- one line listing what was checked and found clean.
- security blockers, missing/stale verification and scoped human acceptances; distinguish
  repository evidence from actual production verification and never authorize deployment.
- approval gaps, stale/conditional/revoked decisions and missing original provenance. State
  what still requires a human; do not declare your own review to be that human approval.

If nothing survives verification, say so plainly.
