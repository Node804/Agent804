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
| Size and dependency spread | <scope> | <review triggers> | <report and reviewer disposition> |
| Duplication and unused code | <scope> | <investigation triggers> | <report and reviewer disposition> |

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
characterization tests may already pass. MT-4 is a reported practice, not a rung gate.
Preserve old entries when correcting or resolving them. No blanket package exclusions. -->

## Measurements

- Comparable reports: <locations, tool versions, scope and cadence>
- Gardening: <routine, responsible reviewer and exception follow-up>
- Maintenance exercises: <schedule or planned trial; results in docs/metrics/maintenance-exercises.md>
