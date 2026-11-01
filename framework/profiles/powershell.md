# Profile: PowerShell

- **Status:** Draft; starter syntax/data parsing only, no full automation/module trial.
- **Applies to:** Supported pinned PowerShell, selected OS targets and reviewed modules.
- **Inherits:** [Shared baseline](README.md#shared-baseline).

## Baseline

| Concern | Proposed mechanism |
|---|---|
| Dependencies | Exact PowerShell/module versions and reviewed repositories/manifest inputs; no global latest installs in checks |
| Style/analysis | PSScriptAnalyzer and Invoke-Formatter with project-selected settings |
| Tests | Pinned Pester with temporary resources and isolated subprocess command acceptance |
| Architecture | Exported module interfaces plus AST/dot-source/command-dependency checks |
| Security | Secret/static checks, current module-origin/advisory review and explicit resource/privilege tests |

## Check, bootstrap and skeleton

Generate `scripts/Invoke-Check.ps1` that explicitly propagates native exit codes, formatter/
analyzer diagnostics, parser errors, architecture/docs/security results and Pester failures.
Require nonzero test discovery and assert the selected Pester result/exit behavior; printing
failed tests alone must not return success. Include all supported OS/PowerShell targets.
Generate bootstrap/doctor for reviewed pinned module provisioning and isolated test/dev
configuration. Do not change execution policy, elevate or access production to make tests
pass. Create one exported command and real subprocess invocation, with success/refusal tests,
CI and records. Parameter validation and typed boundaries supplement testing; document where
static type enforcement is unavailable rather than claiming a compiler proves correctness.

## Rule mapping beyond the shared baseline

| Rules | Mechanism to generate |
|---|---|
| ST-1 to ST-3 | [Style wrapper/settings](../../templates/style/README.md), pinned module/runtime, complete file inventory and check/fix/convergence evidence |
| SK-1, SK-2 | Bootstrap/doctor and isolated invocation of the installed/exported command in CI |
| MT-1 to MT-3 | Comment-based public help, parameter/output/error/side-effect contracts, AST complexity thresholds and investigated unused exports/scripts |
| AR-1, AR-2 | Command manifest declares resource/actor/access policy; discovered exports and scheduled entry points must match it. Destructive operations support explicit apply and preview |
| AR-3 | Module exports are public interfaces; AST checks restrict dot-sourcing/private command access and import direction; dynamic invocation needs targeted tests |
| AR-4 to AR-6 | Actor-attributed service commands/history, one integration module, literal/validated paths and safe parameterized invocation/output handling |
| WK-6 | Unique test drive/temp/registry/config and remote test namespaces; parallel workers do not share mutable fixtures |
| SE-2 to SE-5 | Trusted module origins/install scripts, current verification coverage and least-privilege resource/refusal tests; no credentials in transcripts or command URLs |
| OP-1 to OP-8 | Exported operation contract shared by CLI/tools with constrained credentials, attribution, retry semantics and bounded remote load |

## Testing evidence (draft)

Apply [testing guidance](../testing.md) (TS-7 to TS-12); exercise this mapping before claiming it met.
Record discovered/executed tests, selected paths/tags and runner result; the wrapper must
propagate failures. Isolate files, processes and environment; distinguish mocks from actual
command/module boundaries. Report skips, retries and unavailable host/OS coverage.

## Gaps and gotchas

Select actual module pin/provisioning format, Pester version/result handling, AST checker,
complexity thresholds and security/advisory coverage. PowerShell errors and native command
exit codes require deliberate handling; a quiet pipeline is not proof of success. `-WhatIf`
or confirmation prompts alone are not authorization. Avoid broad cleanup, real user registry
or shared remote namespaces in tests. Dot-sourcing and module import execute code; review
before discovery. Tool-specific agent/host enforcement and platform differences need trials.

## Sources

- [Pester](https://pester.dev/docs/quick-start)
- [PSScriptAnalyzer](https://github.com/PowerShell/PSScriptAnalyzer)
- [Style starters](../../templates/style/README.md)
