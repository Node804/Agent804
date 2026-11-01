# Security

<!-- Copy to docs/security.md and link it from AGENTS.md, so agents read it before building.
Keep secrets and incident details out of this file. A small tool can keep it short. -->

- **Owner:** <person, and how to report a suspected problem>
- **Standards:** <e.g. OWASP ASVS version and the requirements selected; selecting some is not compliance>
- **Last reviewed:** <date, and what changed>

## What we protect, from whom

| Asset or data | Who or what can reach it | Trust boundary | Credible abuse |
|---|---|---|---|
| | | | |

Include agents: outside text they read, and code that runs on install or build.

## Production access from development (GR-1)

<!-- Only when production is the only source to develop against. Delete otherwise. -->

| Source | Data, and why it is not sensitive | Credential separate from production's? | Read-only enforced by | Rate limit | Decided by, date |
|---|---|---|---|---|---|
| | | | | | |

## Checks (SE-2)

| Check | Command | How we know it fails (fixture) | Advisory freshness |
|---|---|---|---|
| Secrets | | | |
| Static analysis | | | |
| Dependencies | | | |

A check that errored, was skipped or used stale data is a gap, not a pass.

## Dependencies (SE-3)

<!-- How a new package's publisher and identity are verified, and who reviews it. -->

## Findings

| ID | What and where | Owner | Deadline | Outcome |
|---|---|---|---|---|
| | | | | |

Only a person accepts a risk, with a scope and an expiry. Suppressions link here.

