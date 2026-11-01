# Profile: <stack>

- **Status:** Draft
- **Applies to:** <language and framework, versions>
- **Inherits/extends:** <shared baseline and parent profile links, or none; read parents first>

Resolve parent choices and explicit overrides in the adopting project's stack profile.
Do not duplicate parent checks or inherit validation status. Shared recommendations and
starter configurations do not satisfy the remaining stack mechanisms. Name project recipes
to generate and verify; do not imply the framework already ships those applications.

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

## Project-owned style

Preserve existing choices, apply user preferences, or offer the optional style defaults.
Config files govern after adoption; templates never override project policy (ST-1 to ST-3).

| Language/grammar and maintained paths | Adopted convention/config | Exact runtime/tool pins | Check command | Fix pipeline/order | Exclusions/manual review |
|---|---|---|---|---|---|
| <include tests/scripts/tooling and UI/template grammars> | <authoritative files> | <manifest/lock references> | <non-mutating, failing status> | <stable second pass> | <scoped reasons and migration plan> |

Verify a violation fails without source edits, the fix passes and a second pass changes
nothing. Include CI/editor agreement and parser-error handling. Independent monorepo
applications may vary only with declared boundaries. Record unsupported coverage as a gap.

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
| ST-1 | Language matrix, project-selected configs and actual version pins |
| ST-2 | Full check/fix commands and non-mutating failure/fix/convergence evidence |
| ST-3 | Reviewed exclusions, preset/tool upgrades and formatting-only or staged migration scope |
| AP-1 to AP-4, RV-1 | Record schema/native adapter, preserved subjects, trusted original-source/authority verification, required-stage IDs, freshness/conditions and actual requirement trace |
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
