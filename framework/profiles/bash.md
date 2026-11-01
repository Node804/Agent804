# Profile: Bash

- **Status:** Draft; no full pipeline or application trial.
- **Applies to:** Explicitly declared supported Bash versions/platforms, not all POSIX shells.
- **Inherits:** [Shared baseline](README.md#shared-baseline).

## Baseline

| Concern | Proposed mechanism |
|---|---|
| Dependencies | Pinned Bash/tools and reviewed OS packages or immutable image inputs; document external commands |
| Style/analysis | shfmt for the declared Bash dialect and ShellCheck with reviewed sourced-file scope |
| Tests | Pinned bats-core with isolated subprocess fixtures and real CLI acceptance |
| Architecture | Declared script/function interfaces plus source/command-usage checks |
| Security | Secret/static checks, current system/tool advisory review and least-privilege/path/command tests |

## Check, bootstrap and skeleton

Generate `scripts/check.sh` that verifies formatting, ShellCheck, syntax, architecture/docs,
current security verification and `bats tests`, explicitly propagating every failure. Discover
the intended tests and extensionless scripts; zero discovered tests is not success. Use
deliberate status/pipeline handling rather than assuming `set -e` catches every context.
Bootstrap verifies reviewed pinned commands and isolated configuration/resources; doctor
reports missing prerequisites. No automatic privilege escalation, system-package update or
curl-to-shell install is part of the check. Create one executable command with documented
input/output/status, success/refusal acceptance, dry-run behavior for writes and clean CI.

## Rule mapping beyond the shared baseline

| Rules | Mechanism to generate |
|---|---|
| ST-1 to ST-3 | [Bash starters](../../templates/style/bash/.editorconfig), explicit dialect/file inventory and non-mutating diff/lint checks with fix/convergence proof |
| SK-1, SK-2 | Bootstrap/doctor and real executable CLI scenario, asserting stdout/stderr/status and resource effects |
| MT-1 to MT-3 | Public command help/contracts, function/branch/nesting limits via chosen shell AST checks, and investigated obsolete scripts/flags/dependencies |
| AR-1, AR-2 | Dispatch manifest declares permitted principal/resources and write policy; discovered executables/functions match their authoritative operation definitions |
| AR-3 | Restrict sourced modules and external command access through declared interfaces; test disallowed sourcing/cycles/dynamic bypasses |
| AR-4 to AR-6 | One write/integration layer with actor/history; explicit argument arrays/quoting, literal paths and validated destinations. No eval of outside data |
| WK-6 | Unique temporary roots, files, ports and outside test namespaces; verify absolute cleanup targets before recursive deletion |
| SE-2 to SE-5 | Current secret/static/system-input evidence and safe privilege/argument/path/symlink/refusal tests; assertions cover prohibited filesystem/external effects |
| OP-1 to OP-8 | Only if used as machine tools: typed/schema wrapper around declared operations with scoped authority, attribution, retries and outside-load limits |

## Testing evidence (draft)

Apply [testing guidance](../testing.md) (TS-7 to TS-12); exercise this mapping before claiming it met.
Record discovered/executed test cases and propagate failure through the wrapper. Use isolated
temporary directories, environment and child processes; exercise real script exit codes,
stdout/stderr and effects. Report skips and unavailable shell/OS/tool coverage.

## Gaps and gotchas

Choose the actual OS/tool input pinning, complexity/source checker, advisory coverage and
runtime principal. Bash has no general static type checker; validate structured inputs at
boundaries, test contracts and record the limitation. Prefer a more suitable language if
complex state/contracts exceed what the chosen checks can protect. ShellCheck is not a proof
of safe arbitrary execution. Test PATH/tool assumptions and sourced files without touching
live resources; an isolated subprocess alone does not isolate the filesystem or network.
Host controls, agent guardrails and platform-specific behavior need explicit trial evidence.

## Sources

- [bats-core](https://bats-core.readthedocs.io/en/stable/)
- [shfmt](https://github.com/mvdan/sh)
- [ShellCheck](https://www.shellcheck.net/)
