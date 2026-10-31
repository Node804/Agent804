# <Feature name>

- **Size:** <small | medium | large> (see the `spec` skill)
- **Zone:** <green | yellow | red> (from `docs/risk-zones.md`)
- **Quality scenarios:** <QS-n this touches, or "none">
- **ADRs:** <numbers this applies or exercises, or "none">
- **Status:** Draft | Agreed | Built | Dropped

## Why

Who needs this and what they do today without it. Two or three sentences.

## Out of scope

What this does not do, so the agent does not add it.

## Acceptance criteria

<!-- Behaviour a person can observe, never implementation. Each becomes at least one test,
written before the code and seen to fail. Small changes need one or two; large ones a scenario
per path, including who must NOT be able to do it. -->

1. **Given** <state> **when** <action> **then** <observable result>.
2. **Given** a user without access **when** <action> **then** <refused, and nothing changes>.

## Open questions

<!-- [NEEDS CLARIFICATION] items. All resolved before planning starts. -->

- [NEEDS CLARIFICATION] <question>

## Decisions this touches

<ADR numbers, or "none">
