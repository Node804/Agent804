---
name: measure
description: Report whether agent-built work is getting faster and better or just busier - lead time, first-pass check rate, human interventions, rework, escaped defects and rollbacks - from git history, CI results and a simple log. Use when the user asks how the agent workflow is performing, or on a regular schedule.
---

# Measure the factory

Developers using AI often feel faster than they are. This skill replaces the feeling with a few
numbers (MS-1). Never count lines generated.

## What to measure

| Measure | Source | Means |
|---|---|---|
| Lead time | Branch first commit to merge, from git | How long a change takes end to end |
| Change size | Lines and files per merge | Large changes are rarely reviewed well (WK-1) |
| First-pass check rate | CI runs per pull request; share green on first run | How often the agent's "done" is really done |
| Interventions | `docs/metrics/interventions.md`: one line each time a person had to correct the agent | Where the harness is weak |
| Rework | Commits that change lines merged in the last two weeks | Code that did not hold |
| Escaped defects | Bugs found after merge, from the issue tracker or the log | What review and tests missed |
| Rollbacks and reverts | `git log --grep=Revert` | |
| Harness growth | Checks added by `sensor` in the period | Whether mistakes become checks |

If the project has no interventions log, create `docs/metrics/interventions.md` with the
columns: date, what the agent did, what was corrected, rule or check that now prevents it
(or "none").

## Steps

1. Pick the period (default: the last 30 days) and the previous period for comparison.
2. Compute what the sources allow. When a source is missing (no CI history, no issue tracker),
   say so; do not estimate.
3. Read the interventions log and group it by cause. The largest group is the next `sensor` or
   `AGENTS.md` change.

## Report

A small table of this period against the last, three observations, and one recommendation.
Note any measure that could not be computed and what would make it computable.
