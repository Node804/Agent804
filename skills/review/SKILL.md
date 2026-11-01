---
name: review
description: Review a change (uncommitted work, a branch or a pull request) in a fresh context, working back from its acceptance criteria and the project's rules, with depth set by risk zone. Reports findings only, never edits. Use before a merge or when the user asks for a review.
---

# Review a change

A second look from a context that did not write the code (RV-2), aimed where damage is likely
(RV-3). Report only: never edit, commit or push. Run this in a fresh session or subagent, not
in the one that wrote the change. If you inherited the author's conversation or conclusions,
say so in the report: it limits the review.

## Steps

1. **Get the change**: the diff against the base branch, plus uncommitted and untracked files,
   or the pull request or paths given. Note the revision you reviewed.
2. **Get the intent**: the spec in `docs/specs/` or the PR description. If there are no
   acceptance criteria, say so first: the review can only check rules, not correctness.
3. **Get the zones** from `docs/risk-zones.md`. Spend most of the effort on red, then yellow.
4. **Read the rules**: the root `AGENTS.md`, the `AGENTS.md` of every directory touched, and
   where they exist `docs/maintainability.md` and `docs/security.md`.
5. **Run the check** if it only reads and tests. Use its real result; never the author's report
   of it.
6. **Check, in this order**:
   - **Criteria**: each acceptance criterion has a test, and the code does what it says. Look
     for refusal paths (the user without access, bad input, the outside system down).
   - **Tests** (TS-2, TS-4, TS-7 to TS-12): changed behaviour has a test that failed before
     the change; assertions are independent of the code; any edited acceptance test has a
     reason; the boundary is real where it matters; retries, skips and quarantines are
     reported, not hidden.
   - **Scope**: features nobody asked for; changes outside the plan.
   - **Rules**: each rule in `AGENTS.md` that the change could break.
   - **Maintainability**: public contracts documented (MT-1); complexity limits and new
     exceptions (MT-2); business rules kept in one place (AR-2); boundaries and cycles (AR-3); writes validated in one place (AR-4);
     an existing capability reused before a new one or a new dependency (SK-3); retired paths
     removed (MT-3). Moving a violation does not make it new or make it go away. "No refactor
     needed" is a valid result. For a restructuring, check the stated problem, the preserved
     contracts and the before/after test results; flag hidden behaviour changes.
   - **Security**: object and tenant access, input parsed and output encoded (AR-6), what agent tools can do,
     abuse paths tested (SE-5), dependencies from intended sources (SE-3). A weakened security
     check, test or approval policy without a person's review is a finding (GR-2).
   - **Agreement** (GR-7): the person agreed to the criteria this change meets, and material
     changes since then were shown to them again.
   - **Debt**: a new shortcut was agreed by a person; a debt ticket never waives a failed check
     or an unmet criterion.
   - **Style** (ST-1): unexplained formatter config changes, broad exclusions, and
     reformatting of files the change did not need to touch.
   - **Red zones**: every line.
7. **Confirm each finding** by reading the code around it, with its callers and configuration.
   Drop anything you cannot confirm, and findings about impossible cases (RV-5).

Skip layout the formatter owns. Naming, interface clarity and documentation remain reviewable.
Do not judge maintainability from comment counts or file size alone.

## Report

Findings, most serious first: `path:line`, what breaks, who sees what (a concrete failure, not
"could be an issue"), and which criterion or rule it breaks. Then:
- criteria with no test;
- a mistake that will recur, with the check that would prevent it (hand it to `sensor`);
- what you could not check, and why;
- what still needs a person: this review is not the human review before merge (RV-1), and it
  never approves a deployment;
- one line listing what was checked and found clean.

If nothing survives verification, say so plainly.
