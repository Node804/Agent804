# <Feature name>

- **Size:** <small | medium | large> (see the `spec` skill)
- **Zone:** <green | yellow | red> (from `docs/risk-zones.md`)
- **Quality scenarios:** <QS-n this touches, or "none">
- **ADRs:** <numbers this applies or exercises, or "none">
- **Security requirements:** <versioned IDs from docs/security.md, or reasoned "no impact">
- **Status:** Draft | Agreed | Built | Dropped
- **Approval evidence:** <IDs/source and reviewed content; status alone is not agreement>

## Why

Who needs this and what they do today without it. Two or three sentences.

## Out of scope

What this does not do, so the agent does not add it.

## Acceptance criteria

<!-- Behaviour a person can observe, never implementation. Each becomes at least one test,
written before the code and seen to fail. Small changes need one or two; large ones a scenario
per path, including who must NOT be able to do it. -->

<!-- Security-affecting criteria include realistic bypass/refusal paths, assertions of no
prohibited effect or disclosure, and authorized success. Update threats and requirement scope
when exposure changes; identify actual deployment verification separately from local tests. -->

1. **Given** <state> **when** <action> **then** <observable result>.
2. **Given** a user without access **when** <action> **then** <refused, and nothing changes>.

## Verification boundaries

<!-- Choose the lowest effective test level per criterion and representative end-to-end
journeys. Identify actual integration boundaries, safe substitutes and remaining assumptions.
Expected results come from requirements/independent examples, not copied production logic.
Small changes can record this in the plan/PR instead of adding another document. -->

## Requirement trace

<!-- Stable requirement/criterion IDs, proportionate to the change. Actual tests, reviewed
implementation revision and results can be linked later from the plan/PR; do not invent future
evidence or rewrite an earlier decision. Material criteria changes renew affected approval. -->

| Requirement | Criterion | Tests | Implementation revision | Verification evidence |
|---|---|---|---|---|
| <ID or issue reference> | <AC-n> | <actual reference or not written yet> | <revision or not built yet> | <result or pending> |

## Open questions

<!-- [NEEDS CLARIFICATION] items. All resolved before planning starts. -->

- [NEEDS CLARIFICATION] <question>

## Decisions this touches

<ADR numbers, or "none">
