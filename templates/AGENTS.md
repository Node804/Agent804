# <Project name>: agent instructions

<One paragraph: what this is, who uses it, what happens if it breaks.>

This file is the shared project-policy authority; scoped additions refine relevant areas.
Tool-specific files point here. It holds what code cannot explain; keep it under 200 lines (the check
enforces it).

## Check

```bash
<check command>          # everything CI runs; must be green before feature completion
<single test command>    # one test file or test
<bootstrap command>      # fresh clone to running app; safe to rerun
<run command>
```

## Rules

<!-- Only rules an agent would otherwise get wrong. When you correct the same thing twice, add it
here; when it can be checked mechanically, move it into the check and delete the line. -->

- Access: every entry point declares who may use it; the check fails otherwise.
- <Boundary rule: how modules may talk to each other.>
- <Where writes go, and what they record.>
- <Outside systems: where they are reached from, read-only or not.>
- Scripts that change data are dry-run unless given `--commit`.
- Project style scope, configs, pins and check/fix commands: <link to profile or style record>.
  Follow these choices; do not replace them with framework defaults. Checks do not rewrite
  source; fix only the authorized scope and keep unrelated formatting changes separate.
- Maintainability limits, public-contract scope, reviewed baselines and exceptions are in
  `docs/maintainability.md`. New work adds no unapproved violations or worsening findings.
- Debt uses the canonical tracker/document linked there: confirm evidence, owner, disposition
  and review condition; verify closure. A debt ticket grants no exception or failed-check waiver.
- Security requirements, threats, dependency trust, findings and response ownership are in
  `docs/security.md`. Missing or stale security evidence is not a clean check. Security debt
  needs its own scoped human decision with expiry; a baseline alone never permits exposure.

## Working here

- Host setup/capability evidence: `docs/agent-host.md`. Verify effective instruction overrides,
  skill resources and completion controls; never assume a Claude hook protects another host.
  Tool permission or automatic approval does not replace human architecture/criteria/review consent.
- Model routing is optional; use the project's policy only if enabled. Recommendations do not
  launch agents, transmit code or authorize spending. One model in separate contexts is valid;
  record actual selections and never lower required quality or silently use a paid fallback.
- Work on a branch. Never commit, push, deploy or migrate unless asked in chat.
- Approval policy/index is `docs/approvals/README.md`. Reuse valid human decisions within
  scope; material changes renew affected approvals. Records/status fields do not prove
  consent. Verify original source, authority and conditions; mechanical success grants no action.
- Concurrent writers use separate worktrees or clones and isolated mutable resources. Follow
  `docs/worktrees.md`; sequential contexts may reuse a checkout. Check the combined result
  after integration. Handoffs name an exact revision or preserved patch.
- New behaviour starts from acceptance criteria in `docs/specs/` (the `spec` skill sizes them)
  and acceptance tests derived in a context separate from implementation, written first and
  seen to fail for the intended gap. Implementers may add supporting unit tests.
- Preserve meaningful pre-change failure evidence and final scope/counts/results. An intentional
  red test handoff completes that stage only; it does not complete the feature or permit merge.
- Never skip, weaken or delete a failing test to get green. Explain legitimate test corrections;
  changed acceptance outcomes require criteria review and affected approval. Report failures,
  retries, skips and quarantine honestly; isolate mutable test resources and control nondeterminism.
- After green, inspect structure and duplication; refactor where justified while preserving
  behavior. Update affected contracts and remove obsolete paths or record why they remain.
- Standalone refactors state the maintenance problem, affected consumers/contracts and baseline
  preservation tests; verify small transformations. Characterization tests may pass immediately.
  Specify behavior changes separately and report unverified compatibility; green tests cover
  only their exercised scope. Use the `refactor` playbook for substantial restructuring.
- Non-trivial work has a plan in `docs/plans/` with progress notes; update it as you go.
- Retrieve to answer the next task question; inspect relevant enclosing constraints and callers.
  Search hits/summaries are pointers, not authority; no hits means no matches for that query/scope.
  Resolve necessary truncated/missing output or report the gap. Preserve source/revision,
  facts versus hypotheses and actual results in plan/PR notes; recheck critical state on recovery.
- Risk zones are in `docs/risk-zones.md`. In a red zone, stop and ask before changing behaviour.
- Security checks/tests, CI gates, permissions and approval policy require explicit human
  review of changes; existing authorization covers its agreed scope. Keep production secrets
  and sensitive data outside agent sessions; use test credentials and safe fixtures.
- **Done** means: acceptance criteria met, tests written and passing, the check green, a
  changelog entry, docs and this file updated if behaviour changed. Report the commands you ran
  and their result; never claim a check you did not run.
- Every change requires human review before merge, identifying the actual reviewed change
  under the approval policy. Agent review and passing checks do not substitute for it.
  Documentation/style-only work uses relevant validations; do not manufacture behavior tests.

## Decisions

Hard-to-reverse decisions are ADRs in `docs/adr/`. Read the ones on a topic before changing it.
Accepted ADRs stay frozen. Append later results to their linked records in `docs/evidence/`;
contradictions need owner review, never an automatic downgrade.

Production security readiness is separate from a green check or Build score. Require current
evidence for the actual release and environment; local settings alone leave deployment pending.
