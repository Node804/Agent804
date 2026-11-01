---
name: refactor
description: Plan and perform scoped restructuring of existing code while preserving observable behavior, with baseline tests, consumer analysis and verification evidence. Use for standalone refactors or substantial preparatory restructuring; routine refactoring within an approved feature needs no separate invocation.
---

# Refactor existing code

Improve a concrete maintenance problem while preserving the affected behavior and contracts.
MT-4 is a reported practice pending trials, not a rung gate. A passing suite supports only
the scope it exercises; it is not proof of complete equivalence.

**Framework files**: in Claude Code, `${CLAUDE_PLUGIN_ROOT}/framework/`; for other agents,
`../../framework/` from this file. Read [maintainability](../../framework/maintainability.md),
especially MT-4: Claude Code `${CLAUDE_PLUGIN_ROOT}/framework/maintainability.md`.
Read [testing](../../framework/testing.md): Claude Code
`${CLAUDE_PLUGIN_ROOT}/framework/testing.md`. Use the project's resolved stack profile,
conventions, risk zones, applicable ADRs and approval policy.

## Scope and preservation contract

Inspect relevant canonical debt (MT-5): Claude Code
`${CLAUDE_PLUGIN_ROOT}/framework/technical-debt.md`, otherwise `../../framework/technical-debt.md`.
Link authorized repayment/completion criteria and retained scope; don't expand into unrelated
cleanup. Verify debt outcomes and reconcile exceptions before proposing closure. Moving a
finding or replacing a workaround preserves history and cannot silently resolve the item.

- Identify the maintenance friction, affected area and expected improvement. Explain how
  the restructuring helps; a large file or a metric alone does not justify it.
- Trace callers and consumers, including dynamic registration, reflection, serialization,
  configuration, external clients and maintained examples where applicable. Record uncertain
  consumers; absence from static search is not permission to remove compatibility.
- Identify what must remain stable: relevant results, errors, side effects, public interfaces,
  security/refusal behavior, ordering, transactions, retries and performance constraints.
- Reuse authorization within its scope. Read [approval guidance](../../framework/approvals.md):
  Claude Code `${CLAUDE_PLUGIN_ROOT}/framework/approvals.md`. Material architecture or contract
  changes follow the existing spec/ADR/approval process. A bug fix or changed public outcome
  is specified separately rather than hidden inside a refactor. No commit/push/deploy authority
  is implied. Routine extractions within an approved task need no repeated permission.

## Establish the baseline

Use context guidance: Claude Code `${CLAUDE_PLUGIN_ROOT}/framework/context-management.md`,
otherwise `../../framework/context-management.md`. Follow consumers/config/registrations,
verify dirty-state/index freshness and inspect missing/truncated relevant output. Search
absence alone cannot justify deleting compatibility paths (IN-8); preserve recovery evidence.

Run relevant tests and available full checks before restructuring. Record revision or
preserved patch/base, commands, environment, scope/results and existing failures. Do not
attribute pre-existing failures to the refactor or silently treat them as accepted debt.

Where protection is insufficient, add focused characterization tests before changing
structure: they document observed current behavior and may pass immediately. Do not invent a
red failure or claim TDD for preserved behavior. Identify known bugs as defects rather than
approving them as requirements. Derive new acceptance outcomes independently in a separate
context when behavior changes (TS-3); implementers may add supporting preservation tests.
Use safe fixtures and actual integration evidence where mocks cannot establish compatibility.
If critical behavior cannot be checked, narrow the scope or report the gap and seek an
affected decision before proceeding beyond existing authorization; never claim it preserved.

## Make small transformations

For non-trivial work, use the existing [plan template](../../templates/plan.md): Claude Code
`${CLAUDE_PLUGIN_ROOT}/templates/plan.md`. Record the problem, preservation contract, baseline,
ordered transformations and verification. A small refactor can use plan/PR notes instead.

Separate structural transformations from behavioral changes (WK-1). Use the stack's safe
rename/extract tools where useful, then inspect the actual diff and dynamic consumers.
Keep affected tests green after each meaningful transformation; investigate unexpected
failures before extending the change. Explain legitimate test adjustments and preserve
acceptance outcomes (TS-4/TS-8); rewriting assertions to bless changed behavior is not evidence.
Avoid unrelated cleanup, speculative abstractions and broad formatting changes. Follow
project-owned style and maintainability limits; don't move violations to erase their history.
For concurrent writers, follow [worktrees](../../framework/worktrees.md): Claude Code
`${CLAUDE_PLUGIN_ROOT}/framework/worktrees.md`; isolate resources and check combined changes.

## Complete and review

Preserve the plan's resume handoff across contexts. Verify actual host capabilities via
Claude Code `${CLAUDE_PLUGIN_ROOT}/framework/agents/README.md`, otherwise
`../../framework/agents/README.md`; unsupported execution remains a reported gap.

Update callers, public-contract documentation, navigation and examples. Remove obsolete paths,
dependencies and configuration or record retained consumers, reason and review condition
(MT-3). Preserve required migrations and compatibility code; investigate uncertain usage.

Run relevant regressions and the full check on the combined result. Record revision/patch,
commands/environment, discovered/executed scope, actual results and skips/exclusions (TS-12).
Compare the maintenance outcome with the stated problem; fewer lines alone proves no benefit.
Report unsupported contracts and platforms as gaps, not equivalent behavior. Keep production
resources and outside writes out of verification unless independently authorized.

Hand the result to fresh-context review when applicable; every merge requires human review
(RV-1). An author-written evidence record is not that approval. Do not report completion
while applicable checks fail; explain blockers and preserve the handoff.

Report: problem and scoped changes, preserved contracts and consumer analysis, baseline and
final evidence, maintenance improvement, removed/retained paths, gaps and required review.
