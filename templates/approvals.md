# Approval policy and index

<!-- Copy to docs/approvals/README.md. Records are flat APP-<id>.json files; snapshots live
in snapshots/. Fill the project-specific policy; a copied Pending template grants no authority. -->

## Authority and required stages

| Stage/decision | Human owner or authorized reviewer | Independence requirement | Required approval IDs/source |
|---|---|---|---|
| Feature/spec | <role and identity> | <policy> | <IDs and original review/message> |
| Architecture | <system owners> | <policy> | <IDs and reviewed ADR content> |
| Implementation/merge | <human code reviewer> | <author/latest-pusher policy> | <IDs, actual change/revision and host review> |
| Restricted action | <commit/push/migration/deployment owner> | <policy> | <IDs and exact action/target/conditions> |

Several named decisions may be approved together. Valid authorization carries across sessions
within its scope; do not ask repeatedly. Feature implementation does not imply commit/push/
deployment permission. Silence, an agent's approval label and passing tests are not consent.

## Index and original evidence

| Approval ID | Kind and subject | Reviewed revision/snapshot | Original source | Related requirements/ADRs/decisions |
|---|---|---|---|---|
| <unique ID> | <scope> | <immutable reference> | <real locator/export; limitations explicit> | <references> |

Reviewer/source verification: <how actual identity, authority, original decision and subject
are checked; restrictions and unavailable evidence remain explicit>. Do not fabricate message
IDs or timestamps. Keep private evidence restricted and record a suitable reference.

## Freshness and administrative transitions

Material changes: <criteria, scope, architecture, security, actions and dependency changes
requiring renewed decisions>. Unrelated edits preserve valid scoped approval.

Permitted nonmaterial transitions: <narrow policy for status/index updates; reviewed old/new
revision and original authority, or none>. Never expand behavior through this exception.
The portable byte checker is conservative; define any needed trusted adapter rather than
silently changing the reviewed hash. Missing integration remains a gap, not permission.

Revocation/supersession: <append a new sourced record; retain original decisions/snapshots>.
Conditions and expiry: <verification path; pending/expired decisions block covered actions>.
Risk acceptance still requires a scoped human decision with expiry under docs/security.md.

## Mechanical integration and traceability

- Record validation: <actual command and schema; structural success is not human provenance>
- Required-ID selection: <trusted stage mapping; agents cannot select their own substitute>
- Host gates: <required/stale/independent reviews, check protection and bypass policy>
- Requirement trace: <plan/PR matrix linking IDs -> criteria -> actual tests -> implementation
  revision -> results; early decisions need not invent future implementation evidence>
- Frozen ADR index: <external mappings; do not rewrite Accepted content to add backlinks>
- Adoption evidence: <valid reuse/unrelated edit, material change, missing source, conditions,
  revocation/expiry/dependency tests, cross-session handoff and actual host-review trials>
