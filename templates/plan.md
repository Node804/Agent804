# Plan: <feature>

- **Spec:** `docs/specs/<file>.md`
- **Branch:** <branch>
- **State:** active | done | abandoned
- **Checkout:** <absolute path; sequential contexts may reuse it>
- **Base:** <commit ID, or "no first commit yet">
- **Resources:** <checkout ID; database, port, queue, storage prefix as applicable>
- **Handoff:** <exact commit or preserved patch with its base; identify uncommitted work>
- **Valid approvals:** <IDs/source, reviewed subjects, scope/conditions and stage requirements>
- **Host/context:** <client/version or unavailable; capability record; exact context inputs>

The next session resumes from this file and the git log, not from chat. Keep it current.
Reuse valid scoped authorization; distinguish implementation permission from restricted
actions. Record freshness/trace dispositions without manufacturing missing human consent.

## Resume handoff

<!-- Keep compact: objective and approved scope; unresolved decisions; exact revision/patch,
dirty work, checkout/resources (above); relevant files/contracts; commands actually run,
results/known failures; next action and remaining verification. A summary/compaction is not
independent review or execution evidence. Recover artifacts and valid consent before resuming. -->

<!-- Context working state (IN-8/WK-8), proportionate to the task: relevant invariants,
authoritative paths/symbols/sections and revision/patch, actually inspected ranges, retrieval
scope and exclusions/index freshness, unresolved missing/truncated sources. Separate sourced
facts, human decisions and agent hypotheses. On recovery recheck critical sources and dirty
state; distinguish recorded prior results from fresh execution. Link rather than duplicate
contracts/logs; no separate context document or full-repository inventory is required. -->

## Steps

<!-- Optional model routing, only if enabled: link policy or record role, proposed/actual
model/host/native effort, access/quality evidence, pool/window/source and unknown allowance,
bounds, fallback trigger/authority, and exact context inputs. Include retries/transfer/rework
and actual outcomes in progress/evidence. Recommendations grant no execution/spending authority.
Single-model separate contexts need no routing policy. -->

<!-- Small ordered steps; distinguish an intentional red handoff from green implementation.
Tick the test-writing stage only with intended failure and independent validity evidence.
Feature completion requires the full check green. Separate structural and behavior changes. -->

- [ ] 1. Write the acceptance tests from the spec; run them; confirm they fail for the right reason.
- [ ] 2.
- [ ] 3. Run the full check; record the result below.

## Test strategy and evidence

<!-- Keep this proportionate; link PR evidence rather than duplicating it. Criteria -> test
references; chosen unit/component/integration/E2E boundaries, real vs simulated dependencies.
Red: pre-change revision or patch/base, command/environment and intended diagnostic (bug
reproduction for fixes); independent validity checks and expected missing-interface diagnostics.
Green/refactor: implementation revision, command/result and refactor disposition.
Final combined check: targets/features/platforms, discovered/executed counts, actual exit,
failures/retries/skips/exclusions and reasons. Identify unverified scope and test corrections.
Existing passing behavior is verification, not a fabricated red witness. -->

## Maintainability disposition

<!-- Relevant debt authority/IDs (MT-5): repay within scope, schedule separately, or retain
with reason, real deferral authority and review condition. Link specialist exceptions/findings.
Identify new compromises before relying on deferral; completion criteria and actual closure
evidence stay canonical. Tickets do not waive requirements or failing checks. -->

<!-- Link the area's public interfaces and tests; note existing capabilities to reuse.
For structural work (MT-4), identify the maintenance problem, preserved contracts and consumers,
baseline/characterization evidence, small transformations and final preservation limits.
After green: refactor performed or not needed; updated contracts/examples; threshold findings
and scoped exceptions; obsolete paths removed or retained with reasons and review conditions.
Record here or link the PR disposition rather than duplicating it. -->

## Progress notes

<!-- Date, what changed, what was learned, what surprised you. Newest last. -->

## Decisions made while building

<!-- Small ones live here. Anything hard to reverse becomes an ADR. -->

## Integration and cleanup

<!-- Record the check on combined changes. Before worktree removal, preserve the handoff and
inspect tracked, untracked and ignored work. Never force-remove or delete a branch by default. -->

## Security disposition

<!-- Link docs/security.md and relevant versioned requirements, abuse tests, current reports,
findings and scoped human decisions. Record dependency/install review before new execution.
Name missing deployment evidence; the plan grants no production access or messaging authority. -->
