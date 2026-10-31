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
5. **Check, in this order**:
   - **Criteria**: each acceptance criterion has a test, and the code does what it says. Look
     for refusal paths (the user without access, bad input, the outside system down).
   - **Tests**: did any test get skipped, weakened, deleted, or changed to match the code?
     Tests that pass without the implementation are worthless.
   - **Scope**: features nobody asked for (KB); changes outside the plan.
   - **Rules**: each rule in `AGENTS.md` that the change could break.
   - **Red zones**: every line.
6. **Confirm each finding** by reading the code around it. Drop anything you cannot confirm.

Skip style: the formatter owns it. Do not report findings about cases that cannot happen
(RV-5).

## Report

Findings, most serious first: `path:line`, what breaks, who sees what (a concrete failure, not
"could be an issue"), and which criterion or rule it breaks. Then:
- criteria with no test;
- a mistake that will recur, with the check that would prevent it (hand it to `sensor`);
- one line listing what was checked and found clean.

If nothing survives verification, say so plainly.
