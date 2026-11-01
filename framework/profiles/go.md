# Profile: Go

- **Status:** Draft; isolated formatter-wrapper smoke only, no full application trial.
- **Applies to:** Supported pinned Go toolchains for CLI, library or service projects.
- **Inherits:** [Shared baseline](README.md#shared-baseline).

## Baseline

| Concern | Proposed mechanism |
|---|---|
| Dependencies | Reviewed Go modules, committed `go.mod`/`go.sum`, explicit workspace/toolchain/download policy |
| Style/types | `gofmt`, compiler and `go vet`; optional extra analyzers pinned and reviewed |
| Tests | `go test`, throwaway integration resources and compiled-command or real HTTP acceptance |
| Architecture | `internal` packages plus package-import/operation-registry tests |
| Security | Secret scan, current `govulncheck`, reviewed build inputs and effective runtime config/abuse checks |

## Check, bootstrap and skeleton

Generate one native/portable project check runner that calls the supplied Go formatting
wrapper on maintained paths, `go vet ./...`, package/declaration/docs checks, current security
verification, build and `go test ./...`. Define package/workspace/target scope explicitly.
Include race tests where the target supports them; missing required target execution remains
a gap. Add vulnerability/build input evidence, not just a successful compiler invocation.
Bootstrap verifies the pinned toolchain, retrieves only reviewed locked module inputs without
silently changing the lock and prepares isolated dev/test resources. Doctor explains missing
config/tool/target prerequisites. Add a runnable command or service, one acceptance scenario,
CI and docs. Module download/check commands and generators are not an untrusted-code sandbox.

## Rule mapping beyond the shared baseline

| Rules | Mechanism to generate |
|---|---|
| ST-1 to ST-3 | [Formatting wrapper](../../templates/style/go/check-format.go) fails on listed differences; fix with gofmt, prove convergence and scope/pins |
| SK-1, SK-2 | Bootstrap/doctor and compiled executable or actual HTTP acceptance in CI; library projects test a consumer |
| MT-1 to MT-3 | Exported Go docs/types, tested examples, actual project complexity thresholds and reference/retirement review |
| AR-1, AR-2 | Typed operation/access descriptors and discovered CLI/router/tool handlers; fail on undeclared handlers and test effective object/tenant authorization |
| AR-3 | Compiler rejects package cycles and `internal` restricts imports; project AST/import tests enforce narrower module interfaces and dependency directions |
| AR-4 to AR-6 | Actor-aware service/transaction/history interfaces, one outside-client package, safe queries/paths/commands and input/output handling |
| WK-6 | Unique DB/schema, listening ports, cache/queue/storage prefixes and process cleanup per checkout; parallel tests use isolated fixtures |
| SE-2 to SE-5 | Current vuln/secret/config/static reports, reviewed transitive/build origins, least-privilege runtime and refusal/resource-limit tests |
| OP-1 to OP-8 | Registry adapters share access; test credentials, attribution, concurrent idempotency/reconciliation, untrusted text and request budgets |

## Testing evidence (draft)

Apply [testing guidance](../testing.md) (TS-7 to TS-12); exercise this mapping before claiming it met.
Record packages, build tags, targets and executed/skipped tests. Distinguish cached results
from fresh execution and require fresh runs when proving changed environments or red witnesses.
Isolate parallel fixtures and real integration; report race-test availability and target gaps.

## Gaps and gotchas

Choose actual router/auth/storage, complexity tool/limits, import checker, target/CGO policy,
vulnerability invocation/coverage and deployment controls. `go.sum` integrity is not publisher
trust. A reachable-code vulnerability result is not proof of every platform/feature safe.
Generators and external commands need review; `go test` can execute arbitrary test code.
An outside-call timeout/cancellation must not leave duplicate writes or a leaked goroutine.
Tool-specific guardrails and host merge protection need evidence; all new mappings remain Draft.

## Sources

- [Go tests](https://go.dev/doc/tutorial/add-a-test)
- [Go vulnerability management](https://go.dev/doc/security/vuln/)
- [Style recommendations](../recommendations/style-defaults.md)
