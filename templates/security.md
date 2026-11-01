# Security record

<!-- Copy to docs/security.md. Fill actual controls, commands, decisions and cadence; remove
placeholders. Keep secrets and sensitive incident details out; link restricted evidence. -->

- **Owner and escalation:** <accountable person, private reporting route, backup>
- **Scope:** <application, agent environment, build/release inputs, deployment environments>
- **Standards:** <versions, selected requirements and rationale; no unsupported compliance claim>
- **Last review:** <date, reviewer, revision and exposure changes>

## Assets, boundaries and threats

| Asset/data sensitivity | Actors and entry points | Trust boundary | Credible abuse | Requirement IDs |
|---|---|---|---|---|
| <asset> | <human/machine/interface> | <boundary> | <failure or abuse> | <IDs> |

## Requirements and exclusions

| Versioned requirement ID | Applicable or excluded, with reason | Control and owner | Spec/criterion/test | Evidence and limits |
|---|---|---|---|---|
| <ID> | <reason, reviewer> | <implementation or configuration> | <references> | <revision, environment, result> |

## Verification policy

| Check | Scope and command | Tool/feed version and freshness limit | Expected coverage and failure policy | Redacted report |
|---|---|---|---|---|
| <secret/static/dependency/config/test check> | <actual command> | <version/cadence/max age> | <coverage; errors/skips stay visible> | <location> |

- Representative detection fixtures and results: <safe test, command, revision, outcome>
- Dependency/build policy: <verified sources/identity, lock/integrity controls, reviewed install
  behavior, clean-build command, safe data and credentials, isolated contributor CI>
- Runtime policy: <least privilege, authentication/authorization, object/tenant isolation,
  safe inputs/outputs, sessions/files/network, sensitive data, logging and resource limits>
- Production configuration checks: <actual command; missing required settings fail safely>
- Required human review: <security enforcement paths, reviewed revision and host controls>

## Findings and response deadlines

| ID | Affected scope and evidence | Exposure, exploitability, impact and severity | Owner | Deadline | Disposition and verification |
|---|---|---|---|---|---|
| <stable ID> | <dependency/control/release> | <risk assessment> | <person> | <date> | <remediate/not affected/acceptance reference; retest> |

Response policy: <concrete deadlines by risk; urgent escalation; release-blocking conditions>.
An existing-finding inventory is not permission to retain exposure. Failed, unavailable,
incomplete or stale required checks do not pass. Define a permitted decision path when
verification cannot be obtained; only an authorized human can accept the scoped risk.

## Human risk acceptance

| Finding IDs and exact scope | Reason and compensating controls | Human approver and decision date | Expiry and review triggers | Blocking policy decision |
|---|---|---|---|---|
| <IDs> | <reason> | <person, record> | <date/events> | <permitted scope only> |

Agents propose decisions; humans accept them. Link suppressions to this record. Preserve
decision history. Expired acceptance blocks readiness until explicitly resolved or renewed.
Link the authoritative approval/source from `docs/approvals/README.md`; do not duplicate or
invent a second decision. Verify reviewer authority, reviewed scope and original evidence.

## Suspected exposure and response exercise

- Notify: <responsible person and reporting procedure; no automatic messaging authority>
- Contain and revoke/rotate: <authorized operator and steps; never paste credentials here>
- Preserve evidence and assess impact: <restricted location and responsible person>
- Remediate and verify recovery: <commands/checks, owners and criteria>
- Safe exercise: <date, tabletop/fixture, participants, outcome, gaps and follow-up>

## Production readiness

- **Status:** Pending | Blocked | Verified for the stated scope
- **Release/artifact and target environment:** <identities>
- **Verifier, time and evidence expiry:** <person, date, freshness/review triggers>
- **Effective deployment checks and results:** <authorized evidence, not just local settings>
- **Open risks and human decisions:** <finding/acceptance references>
- **Missing evidence and blockers:** <list, including outside administrative controls>

Local skeleton evidence may establish development controls while deployment evidence stays
pending. A Build score or this record never grants production access or deployment authority.
