# Profile: Rust

- **Status:** Draft; configuration parsing only, no full application trial.
- **Applies to:** Supported pinned Rust toolchains for CLI, library or service workspaces.
- **Inherits:** [Shared baseline](README.md#shared-baseline).

## Baseline

| Concern | Proposed mechanism |
|---|---|
| Dependencies | Exact `rust-toolchain.toml`, reviewed Cargo sources/build scripts and committed lock policy |
| Style/types | rustfmt with matching parse/style editions, compiler and Clippy |
| Tests | Cargo unit/integration/doc tests plus built-command/HTTP acceptance and isolated resources |
| Architecture | Crate visibility and workspace dependency/operation-discovery tests |
| Security | Secret scan, selected current Cargo-lock advisory checks, build/proc-macro review and runtime abuse tests |

## Check, bootstrap and skeleton

Generate one project check task: `cargo fmt --all -- --check`, `cargo clippy --locked
--all-targets -- -D warnings`, architecture/docs/security stages, build and `cargo test --locked`
for the declared workspace, targets and feature combinations. Include doc tests deliberately;
do not assume one feature selection covers mutually exclusive or platform-specific behavior.
Bootstrap verifies the exact reviewed toolchain/components, fetches reviewed locked inputs
and prepares isolated dev/test state; doctor identifies missing targets/config. Installation
or cross-compilation alone does not prove runtime behavior. Add an actual executable/consumer
acceptance test, CI and docs. Build scripts and procedural macros execute during compilation.

## Rule mapping beyond the shared baseline

| Rules | Mechanism to generate |
|---|---|
| ST-1 to ST-3 | [rustfmt starter](../../templates/style/rust/rustfmt.toml), actual toolchain/edition pins and tested check/fix/convergence |
| SK-1, SK-2 | Rerunnable bootstrap/doctor and built executable, HTTP or consumer acceptance under CI |
| MT-1 to MT-3 | Public rustdoc/contracts, examples/doc tests, agreed complexity/report rules and investigated obsolete features/dependencies |
| AR-1, AR-2 | Typed operation/access contract and discovery of actual dispatch; refusal tests include bypass/direct calls |
| AR-3 | Public/private crate interfaces and dependency-manifest/AST checks enforce domain boundaries, not merely compilation |
| AR-4 to AR-6 | Actor-aware transaction/history services, explicit integration traits/adapters and safe parse/query/path/output boundaries |
| WK-6 | Unique DB/schema, ports and outside-resource prefixes; isolate test processes and integration workers |
| SE-2 to SE-5 | Current advisory/static/secret/config evidence, review unsafe/FFI/proc-macro/build authority and effective auth/resource-limit tests |
| OP-1 to OP-8 | Same operation adapters with scoped credentials, attributed writes, atomic deduplication/reconciliation and constrained outside access |

## Testing evidence (draft)

Apply [testing guidance](../testing.md) (TS-7 to TS-12); exercise this mapping before claiming it met.
Record workspace members, targets, features and discovered/executed/ignored tests, including
doctests as applicable. Isolate fixtures and real runtime boundaries. Expected missing public
interfaces may establish red; unrelated compiler errors cannot. Report feature/platform gaps.

## Gaps and gotchas

Choose the actual framework/runtime, persistence, advisory tool/coverage, complexity limits,
architecture checker, unsafe/FFI policy and deployment verification. Memory-safety guarantees
do not enforce authentication, business authorization or safe SQL/commands. Cargo feature
unification and generated code can change effective behavior; test real supported combinations.
Locked inputs do not establish source trust. Keep platform/feature and doc-test exclusions
explicit. Agent approval/stop enforcement and administrative CI gates remain evidence gaps.

## Sources

- [Cargo test](https://doc.rust-lang.org/cargo/commands/cargo-test.html)
- [rustfmt](https://github.com/rust-lang/rustfmt)
- [Starter commands and editions](../../templates/style/README.md)
