---
name: measure
description: Report whether agent-built work holds - first-pass check rate, human corrections, rework, escaped defects, reverts, test reliability and maintainability trends - from git history, CI results and a simple log. Use when the user asks how the agent workflow is performing, or on a regular schedule.
---

# Measure whether agent work holds

Agent work can look done and not be. This skill shows, with a few numbers, whether the
harness is catching that (MS-1). Never count lines generated.
Read the project's `docs/maintainability.md` if it exists.

Track test flakes/retries, quarantine age, skips/exclusions, suite duration and escaped
regressions (MS-1). Preserve original failures and scope/count changes; compare like targets
and environments. Missing data stays missing; retries alone do not turn failure into success.

## What to measure

| Measure | Source | Means |
|---|---|---|
| Change size | Lines and files per merge | Large changes are rarely reviewed well (WK-1) |
| First-pass check rate | CI runs per pull request; share green on first run | How often the agent's "done" is really done |
| Interventions | `docs/metrics/interventions.md`: one line each time a person had to correct the agent | Where the harness is weak |
| Rework | Commits that change lines merged in the last two weeks | Code that did not hold |
| Escaped defects | Bugs found after merge, from the issue tracker or the log | What review and tests missed |
| Rollbacks and reverts | `git log --grep=Revert` | |
| Harness growth | Checks added by `sensor` in the period | Whether mistakes become checks |
| Structural trends | Comparable complexity, file/module-size, duplication and dependency reports | Whether maintenance costs need investigation, not proof of their cause |
| Aging exceptions | Scoped baseline and retention records in `docs/maintainability.md` | Debt awaiting its agreed review condition |
| Security follow-up | `docs/security.md` and restricted report references | Verification gaps/freshness (SE-2); when Security applies, overdue findings and expired acceptances (SE-6). Counts are not proof of security |

If the project has no interventions log, create `docs/metrics/interventions.md` with the
columns: date, what the agent did, what was corrected, rule or check that now prevents it
(or "none").

## Steps

1. Pick the period (default: the last 30 days) and the previous period for comparison.
2. Compute what the sources allow. When a source is missing (no CI history, no issue tracker),
   say so; do not estimate.
3. Read the interventions log and group it by cause. The largest group is the next `sensor` or
   `AGENTS.md` change.
4. For structural trends, record tool version, scope, baseline changes and dispositions for
   threshold findings. Reuse the maintainability Measurements index; include boundary-exception
   changes and review conditions. One snapshot means "baseline only", not a trend. Changed tools
   or scope start a separate series unless comparability is established explicitly. Missing data
   stays missing; lower numbers alone prove no improvement. Do not rank developers by metrics.
5. Use the security record's risk categories and deadlines when comparing security follow-up.
   State missing data and changed scan scope; do not rank teams by raw finding count or label
   unavailable scans clean. Metrics do not authorize accepting risk or renewing exceptions.

## Report

For debt follow-up (MT-5, MS-1/MS-2), use the project's debt record. Track observed consequences, ownership gaps, due/overdue reviews, recurrence and verified
repayment with comparable scope. Separate estimated clean-code effort from measured friction;
raw ticket totals/closures prove no benefit. No universal score/capacity percentage is required,
and measurements do not authorize deferral, risk acceptance or automatic issue creation.

For context and recovery trials, compare equivalent tasks/model/host/effort and
expected evidence: missed contracts, retrieval gaps, unnecessary reads, recovery accuracy,
defects/interventions, task completion and measured overhead. Token reduction or a single
successful lookup alone proves no improvement. Missing trials are practices pending evidence.

If the project routes models (`docs/model-routing.md`), apply MS-5. Compare equivalent task/quality scopes and actual model/host/native effort;
include failures, transfers, retries, rework, interventions, defects and elapsed time. Keep
measured/estimated/unknown usage distinct and subscription pools/native units separate from
API spend. Do not infer savings from prompt length or rank models on incomparable tasks.
Missing routing/telemetry is not a new gate. Metrics authorize no paid evaluations or calls.

A small table of this period against the last, three observations, and one recommendation.
Note any measure that could not be computed and what would make it computable.
