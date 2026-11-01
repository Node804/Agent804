# Profile: C# / .NET

- **Status:** Draft; only an isolated whitespace/config smoke has run, not a full app trial.
- **Applies to:** A supported pinned SDK/runtime for C# CLI, library, service or desktop code.
- **Inherits:** [Shared baseline](README.md#shared-baseline). Add [WPF](wpf.md) or [WinForms](winforms.md) for desktop UI.

## Baseline

| Concern | Proposed mechanism |
|---|---|
| Dependencies | Exact SDK/roll-forward policy in `global.json`, reviewed NuGet sources, locked restore and pinned tools/analyzers |
| Style/types | Project EditorConfig and SDK formatter; compiler/nullability and selected build analyzers |
| Tests | Chosen pinned .NET test framework/runner via `dotnet test`; product-level CLI/HTTP/UI acceptance |
| Architecture | Project-reference and namespace dependency tests plus public-operation discovery |
| Security | Secret/static/dependency/config checks and actual identity/object/tenant refusal tests |

## Check, bootstrap and skeleton

Generate `scripts/check.ps1` (or an agreed portable task entry point) with explicit failure
propagation: `dotnet format <solution> --verify-no-changes --no-restore`, build/analyzers,
architecture/docs checks, current security verification and `dotnet test <solution>` using
options for the selected runner. Include all declared target frameworks/features. Warnings
that implement required rules must fail the check, not merely appear in an IDE.
Bootstrap performs reviewed locked restore/tool restore and isolated dev/test setup; doctor
checks SDK/workloads/config with actionable fixes. Create one runnable command or protected
endpoint, its installed/HTTP acceptance test and clean CI. Library projects exercise an
installed consumer. Desktop UI requires the extension's actual Windows acceptance evidence.

## Rule mapping beyond the shared baseline

| Rules | Mechanism to generate |
|---|---|
| ST-1 to ST-3 | Merge [C# EditorConfig](../../templates/style/csharp/.editorconfig)/[build properties](../../templates/style/csharp/Directory.Build.props), pin SDK/analyzers and prove check/fix/convergence |
| SK-1, SK-2 | Rerunnable bootstrap/doctor and real runnable/consumer/endpoint test in CI |
| MT-1 to MT-3 | Public XML docs/types/contracts and examples, selected analyzer complexity limits, reference/retirement review including reflection and serialization consumers |
| AR-1, AR-2 | Explicit operation/access metadata; structural discovery of handlers/routes/tools plus direct authorization tests. For ASP.NET Core, policies protect endpoints and resource handlers enforce object/tenant rules |
| AR-3 | Assembly/project/namespace contracts reject internal cross-module references and undeclared cycles; exercise a forbidden reference |
| AR-4 to AR-6 | Actor-aware transactional application services/history, isolated integration adapters, safe database/command/path/serialization sinks |
| WK-6 | Unique DB/schema, ports, storage and queue prefixes per checkout; isolate test workers and secrets/config sources |
| SE-2 to SE-5 | Current NuGet/build/secret/static/config evidence and abuse tests. Audit wrappers must fail on findings, incomplete coverage and errors rather than trusting a listing command's exit status |
| OP-1 to OP-8 | Shared operation contract behind adapters, constrained credentials, attribution/deduplication and tested integration/authority budgets |

For optional TS-13 trials, a reviewed pinned Stryker.NET setup can exercise selected critical
code in isolation; interpret survivors and invalid mutants rather than imposing a global score.

## Testing evidence (draft)

Apply [testing guidance](../testing.md) (TS-7 to TS-12); exercise this mapping before claiming it met.
Record selected runner, projects, target frameworks and discovered/executed counts; fail
on missing expected assemblies/tests. Isolate fixtures and real runtime/persistence boundaries.
Name expected missing-public-interface compiler diagnostics in red handoffs; unrelated build
errors are setup failures. Report skipped tests, retries and unavailable frameworks/platforms.

## Gaps and gotchas

Choose the actual host/framework, auth model, persistence, test runner, analyzer/architecture
tool and concrete complexity thresholds. Test-driver options vary by SDK and runner; verify
the selected invocation and discovery count. Formatters/build analyzers/source generators
execute code even with restore disabled. Cross-compilation is not Windows UI evidence.
Host controls, deployment config and non-Claude enforcement require proof. Explicitly fill
all shared gaps; a draft mapping is not an installed mechanism or production-readiness result.

## Sources

- [.NET testing](https://learn.microsoft.com/en-us/dotnet/core/testing/)
- [Test command and runner selection](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-test)
- [Formatter](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-format)
- [ASP.NET Core authorization](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/introduction)
