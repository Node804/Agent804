# Testing and witnessed TDD

Tests protect agreed behavior and make change safe for humans and agents. Rules TS-1 to
TS-12 describe the properties; stack profiles select tools. TS-13 is an optional practice
pending real-project trials. Coverage counts alone establish neither correctness nor quality.

## A cycle sized to the change

1. Resolve approved criteria and relevant security/quality requirements. Choose observable
   outcomes and the lowest boundary that can prove them; identify real integration needs.
2. A separate context derives acceptance tests from those criteria, not implementation.
   Implementers may write supporting unit tests without another handoff for each helper.
3. Run against the pre-change state. Preserve a meaningful red witness: exact revision or
   reproducible preserved patch and base, command, environment and intended failure diagnostic.
4. Implement the smallest coherent behavior that meets the criteria; run the tests to green.
5. Inspect structure and duplication, refactor where justified and rerun affected tests.
   Record what changed or why no refactor was needed.
6. Run appropriate regressions and the full check on the combined result. CI checks the
   committed state. Trace actual results back to criteria and the reviewed implementation.

A tests-only commit can preserve content and ordering, but cannot prove that tests ran.
Commit only when authorized. Preserved revisions/patches plus execution evidence are equally
valid. Never invent history, backdate evidence or claim TDD from tests written after the fix.
An already passing test can verify existing behavior: record that result rather than
manufacturing a red failure. Documentation/style-only changes use relevant validations;
do not invent executable behavior or redundant tests to satisfy a ritual.
For pure structural work, establish a green baseline and preservation tests, then keep them
green. Characterization tests may pass before restructuring; see MT-4 in
[maintainability guidance](maintainability.md). Intentional behavior changes still follow TDD.

An intentional red handoff completes a test-writing stage, not an implemented feature.
Record the expected failure and independent checks honestly. Do not weaken CI or blocking
hooks to conceal it; report the incomplete implementation. Feature completion and merge
require the applicable full check green. Keep structural and behavior changes separable.

## What counts as red

The failure must distinguish the requested change from a broken test setup. An assertion
showing the wrong result or missing effect qualifies. In a compiled language, a specific
diagnostic for the planned missing public interface can qualify; retain the expected symbol
and diagnostic, then demonstrate behavior after it exists. It does not establish assertion
sensitivity by itself. Unrelated syntax errors, missing dependencies, unavailable databases,
invalid fixtures or failing discovery do not prove the requested behavior is absent.

Run formatting, lint, fixture/setup validation and type checks that are independent of the
missing interface. Identify dependent checks that cannot yet pass rather than asserting
everything is green. For bug fixes, reproduce the affected pre-fix bug and keep its test.
If reproduction is unsafe or unavailable, explain the limitation and review the alternative
evidence; do not report TS-9 as fully demonstrated without a valid witness.

## Useful assertions and boundaries

Derive expected values from criteria, worked examples, a standard or another independent
oracle. Repeating the production algorithm in a test repeats its mistakes. Assert meaningful
outputs, state changes and relevant absence of effects, including refusal paths. Checking
internal method order is useful only when that order is itself a real protocol obligation.

Use fast unit/component tests for detailed behavior, integration tests for important real
boundaries and representative end-to-end journeys for connected user behavior. No universal
ratio is required. State which dependencies are simulated and what remains unverified.
Mocks prove behavior under assumptions; they do not prove a real database, serializer or
service contract is compatible. Exercise representative real runtime/database versions.
Use safe local substitutes and contract evidence for outside services; this guidance grants
no live writes, credentials or network authority. UI screenshots aid review but do not
replace executable outcome checks. Desktop UI evidence needs an appropriate actual platform.

## Reliability and honest execution

Isolate databases, ports, queues, files and mutable state per test/worker/checkout as needed;
reset fixtures and clean up after failures. Control clocks, seeds and ordering where relevant.
Test order dependence deliberately when suspected; randomizing alone does not ensure isolation.
Keep original failures and retry counts visible. Retries are diagnostic evidence, not a way
to erase a failure. Quarantine needs a reviewed scope, owner, reason, compensating protection
and expiry; report the excluded protection as a gap until repaired. Never silently skip it.

Record revision/patch, command, runtime/environment, selected suites/targets/features/platforms,
discovered/executed counts, actual exit/result, failures, retries, skips and exclusions. Compare
unexpected count changes with intended scope. Zero tests is not automatically success: an
intentional empty scope needs a reason; a missing expected suite is a failed verification.
Report unavailable targets and prerequisites as gaps, not passing checks.

Test corrections are normal maintenance, but explain what was wrong and preserve protection.
Fixture/internal refactoring can follow normal review when outcomes remain intact. Changed
acceptance outcomes require criteria review and affected human approval. Never quietly alter
expectations to bless faulty implementation. Retain failures until their disposition is clear.

## Test sensitivity and adoption

For selected high-impact behavior, deliberately introduce a plausible wrong outcome in an
isolated disposable copy and show the intended test catches it (TS-13). Restore the change;
do not ship seeded faults or mutate shared resources. Review surviving faults, equivalent or
impossible cases and exclusions. A compiler error is not evidence of behavioral detection.
Mutation tooling is one option selected by profiles; no universal score is imposed. Detection
does not prove requirements are correct or complete. Coverage helps locate untested risk,
not justify an arbitrary percentage or prove all assertions are effective.

Use existing spec/plan/PR evidence fields, proportionate to risk; a tiny fix needs no separate
test-strategy document. Existing projects record an honest adoption baseline and improve new
work without fabricated retroactive TDD. Level 1 gates isolation and complete execution evidence;
level 2 gates a representative end-to-end test in CI; TS-11's broader integration coverage is
a reported practice. Level 3 adds behavior-focused assertions and regression
witnesses where bug fixes apply. Level 4 tracks flakes, quarantine age, skips, duration and
escaped regressions. Record missing evidence and unexercised mechanisms explicitly.
