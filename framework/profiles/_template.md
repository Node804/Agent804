# Profile: <stack>

- **Status:** Draft
- **Applies to:** <language and framework, versions>

Fill this in against the real project, with its real versions. Every rule in the table in
`profiles/README.md` gets a mechanism or a listed gap. It stays Draft until it has run.

## Baseline

| Concern | Tool | Why |
|---|---|---|
| Package manager and lock file | | |
| Formatter | | |
| Linter (with security rules) | | |
| Type checker | | |
| Test runner | | |
| End-to-end tests | | |
| Architecture / boundary checker | | |
| Complexity limits and review reports | | |
| Public-contract presence, maintained links and examples | | |
| Secret, static and dependency security checks | | |
| Deployment configuration and security acceptance tests | | |
| Task runner | | |
| Changelog | | |

## The check command

```
<one command>
```

Runs, in order: format check, lint and complexity, types, architecture, documentation/example
checks, security verification, framework checks, tests. Identify reports whose dispositions
need review before merge; missing/stale required security evidence cannot become green.

## Style

| Language | Formatter and linter | Pinned version | Check command (reports only) | Fix command |
|---|---|---|---|---|
| | | | | |

Keep the project's existing choices; otherwise use the ecosystem's standard tools (ST-1).

## Rule mapping

| Rule | Mechanism |
|---|---|
| IN-3, IN-5 | |
| IN-4 | Navigation to purpose, public interfaces, permitted dependencies and test command |
| MT-1 | Declared public-interface scope; documentation presence plus meaningful-contract review |
| MT-2 | Actual function-complexity limit, nesting/size/dependency review thresholds, reports and scoped exceptions |
| MT-3 | Unused-code/dependency candidates, dynamic consumers, replacement-path review and retention conditions |
| SE-1 | Versioned requirements, threat model, applicability and exclusions |
| SE-2 | Actual security commands, safe detection fixtures, tool/feed freshness and error/skip handling |
| SE-3 | Publisher/source verification, locked/integrity-checked resolution, install/build behavior and clean-build evidence |
| SE-4 | Secure initial defaults, deployment-shaped tests and separate authorized deployed-control verification |
| SE-5 | Abuse/refusal tests, bypasses and assertions of no prohibited effects or disclosure |
| SE-6 | Human owner, concrete deadlines, blocking/acceptance policy with expiry, safe response exercise |
| CK-1 | |
| CK-6 | |
| ST-1 | See Style above |
| RV-1 | |
| GR-1, GR-2, GR-4 | |
| SK-1 | |
| SK-2 | |
| TS-4 | Reviewed corrections preserve protection; changed outcomes require criteria review |
| TS-7 to TS-12 | Map [testing guidance](../testing.md): meaningful red diagnostics, independent assertions, bug regressions, isolation, actual integration and discovery/results per target |
| TS-13 (practice) | Optional isolated sensitivity tools/trials; survivors and limits, no universal quota |
| WK-6 | Unique checkout ID; database, port, queue and storage isolation; bootstrap and cleanup commands (see worktree playbook) |
| AR-1 | |
| AR-2 | |
| AR-3 | Enforced dependency directions and cycle restrictions; module-cohesion review |
| AR-4 | |
| AR-5 | |
| WK-4 | |
| OP-1 to OP-5 | |

## Gaps

| Rule | Why it cannot be enforced here | Instead |
|---|---|---|

## Maintainability adoption

Record actual thresholds and commands in `docs/maintainability.md`. New projects start clean;
existing projects can retain a reviewed, scoped baseline but introduce no unapproved or
worsening violations. Map generated exclusions, exception records, structural trend reports
and MS-4 exercise evidence. Presence checks and static unused-code reports still need review.

## Skeleton

What `start` generates: <files and the one end-to-end test>.

## Security readiness

Map the [security baseline](../security.md) to this stack. Review code, dependencies, templates,
configuration and build execution. Identify unsupported checks and restricted external
verification as gaps; a development check is not deployed evidence. State verification scope,
versions, freshness and response ownership. Mark new mechanisms Draft until exercised.

## Gotchas
