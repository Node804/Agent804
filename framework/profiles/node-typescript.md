# Profile: JavaScript / TypeScript

- **Status:** Draft; no full application trial.
- **Applies to:** Supported pinned Node projects or shared JS/TS application tooling.
- **Inherits:** [Shared baseline](README.md#shared-baseline). Browser framework/bundler choices remain explicit.

## Baseline

| Concern | Proposed mechanism |
|---|---|
| Dependencies | One chosen package manager and committed lock; pinned runtime/package-manager version |
| Style/types | Project choice; offer Prettier, compatible ESLint/typescript-eslint and TypeScript compiler |
| Tests | Node test runner or agreed pinned alternative; HTTP/CLI/browser acceptance for actual product |
| Architecture | Module dependency/AST checks and one operation/schema authority |
| Security | Secret/static checks, chosen package-manager advisory audit, install/build origin review and runtime abuse tests |

## Check, bootstrap and skeleton

Generate the chosen package manager's `check` task with formatter-check, ESLint, `tsc --noEmit`
where TypeScript is used, dependency/operation/docs checks, current security verification,
build and tests in fail-fast order. Declare actual script paths and compiler configs; plain
JS uses an agreed checked-JS/static-analysis policy instead of a fictitious TS type check.
Bootstrap uses a clean lock-enforcing install after package/lifecycle-script review, then
isolated dev/test settings and doctor diagnostics. Add one command, protected endpoint or
browser action with real acceptance evidence. Pure Node test coverage is not browser coverage.
An install/build/test can execute package code; keep contributor CI unprivileged.

## Rule mapping beyond the shared baseline

| Rules | Mechanism to generate |
|---|---|
| ST-1 to ST-3 | [JS/TS starters](../../templates/style/README.md), scoped runtime globals/parsers, local pinned binaries and convergent ESLint/fmt stages |
| SK-1, SK-2 | Bootstrap/doctor plus installed-command or real HTTP/browser acceptance scenario in CI |
| MT-1 to MT-3 | Public schemas/types and examples; explicit ESLint complexity/nesting limits, dependency/duplication reports and investigated obsolete exports/dependencies |
| AR-1, AR-2, OP-1 | One operation registry with access and input/output schemas; discover actual router/tool/job dispatch and test undeclared/bypass paths |
| AR-3 | Export/import contracts and dependency-graph tests reject internal imports and unapproved cycles; include runtime aliases and bundler resolution |
| AR-4 to AR-6 | Actor-aware transactional services/history, one integration adapter layer, safe queries/rendering/paths and validated data at actual sinks |
| WK-6 | Unique ports, database/schema and cache/queue/storage prefixes; isolate browser state and test workers |
| SE-2 to SE-5 | Current code/dependency/secret/config checks, trusted install scripts, secure session/token/network config and effective authorization/refusal tests |
| OP-2 to OP-8 | Scoped credentials, attributed idempotent writes, untrusted-input authority limits and shared outside-load budgets |

## Testing evidence (draft)

Apply [testing guidance](../testing.md) (TS-7 to TS-12); exercise this mapping before claiming it met.
Record selected files/projects and discovered/executed counts for the chosen runner.
Isolate workers, timers, files and service fixtures; exercise built CLI/HTTP/browser contracts
as applicable. Report skips, retries and unavailable runtime/browser/platform coverage.

## Gaps and gotchas

Select a concrete server or frontend framework, router discovery, runtime principal, data
layer, test runner, architecture tool and deployment policy. Do not combine Node and browser
globals everywhere or assume import-time code is safe. Type assertions do not validate
outside JSON. Build plugins, test transforms and package scripts are executable dependencies.
Unsupported template grammars, dynamic imports and target-browser behavior need explicit
tests/gaps. Windows/POSIX task behavior and host/tool-specific enforcement remain untrialled.

## Sources

- [Node test runner](https://nodejs.org/api/test.html)
- [typescript-eslint](https://typescript-eslint.io/getting-started/)
- [Shared style catalog](../recommendations/style-defaults.md)
