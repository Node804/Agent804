# Maintainability

<!-- Copy to docs/maintainability.md. Fill with the stack's actual limits, commands and scope;
remove placeholders. Keep records narrow; reference the architecture docs instead of copying. -->

## Navigation and contracts

- Area guidance: <links to purpose, public interfaces, permitted dependencies and tests>
- Public-interface scope: <exports, module interfaces, commands and configuration>
- Documentation and example checks: <commands; what still needs human review>

## Limits and review triggers

| Signal | Scope | Enforced limit or review threshold | Command or review mechanism |
|---|---|---|---|
| Function complexity | <authored code> | <stack-appropriate limit> | <command in the check> |
| Nesting | <scope> | <limit or trigger> | <command or review> |
| File or module size | <authored code> | <stack-appropriate limit> | <command in the check> |
| Duplication | <authored code> | <stack-appropriate limit> | <command in the check> |
| Dependency spread and unused code | <scope> | <investigation triggers> | <report and reviewer disposition> |

## Adoption baseline and exceptions

Baseline revision: <commit, or preserved patch with its base; "none" for a clean new project>.
New work introduces no unapproved violations and does not worsen existing ones. Renames and
moves preserve finding identity. Reconsider exceptions when their review condition occurs.

| ID | Rule or signal | Exact location or retained item | Observed value | Reason | Reviewer | Review date or event |
|---|---|---|---|---|---|---|
| <stable ID> | <rule or signal> | <path and symbol, dependency, or compatibility consumer> | <value or n/a> | <why retained> | <person> | <condition> |

## Change dispositions

Technical-debt authority: <existing tracker or docs/debt.md; one canonical location>.
Link baseline/exception and retention IDs to relevant debt items without copying their status.
Use evidence/owner/review/verified-closure fields (MT-5); a record grants no exception.

<!-- Record here or link plan/PR dispositions: reused authority, justified independent copies,
new threshold findings, refactor performed or not needed, removed or retained obsolete paths.
For MT-4 structural work, include problem, preserved contracts, consumer analysis, baseline
and final results, actual maintenance improvement and compatibility gaps. Use plan/PR links;
characterization tests may already pass. MT-4 is a reported practice, not a level gate.
Preserve old entries when correcting or resolving them. No blanket package exclusions. -->

## Measurements

- Retain actual complexity, file/module-size, duplication and boundary-exception reports from
  installed checks in the setup/increment scope, after removing negative fixtures. Reuse existing
  evidence locations; no separate dashboard is required. Missing coverage stays explicit.

| Date | Revision or preserved patch | Command and tool version | Scope | Report | Unavailable coverage |
|---|---|---|---|---|---|
| <date> | <revision, or patch and base> | <reproducible command/version> | <paths/exclusions> | <link to observations and exception state> | <missing signals or none> |

One snapshot is a measurement baseline, not a trend or an approved legacy exception. Snapshots
grant no exceptions; approvals remain in Adoption baseline and exceptions above. Preserve earlier
reports. Changed tools or scope start a separate series unless comparability is established
explicitly; lower numbers alone do not prove maintainability.

- Comparison cadence: <project-appropriate review; no automation implied>
- Gardening: <routine, responsible reviewer and exception follow-up>
