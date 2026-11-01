# Stack profiles and support

`rules.md` says what must be true; a profile says how one stack makes it true. `start` and
`sensor` read the profile for the project's stack; `assess` uses it to know where to look.
Profiles explain stack mechanisms. [Shared recommendations](../recommendations/README.md)
offer optional choices across stacks; [templates](../../templates/) supply files to copy.
Neither a copied config nor a draft recipe proves a mechanism runs.
Select [agent-host guidance](../agents/README.md) separately for instruction/skill discovery,
permissions and completion controls; language profiles do not imply Claude-specific hooks.

A profile is one file, `<stack>.md`, copied from `_template.md`. It has:

1. **Baseline**: the tools a new project gets (package manager, formatter, linter, type checker,
   test runner, architecture checker, task runner), with one line each on why.
2. **The check command**, in the order the steps run.
3. **Rule mapping**: for each rule that needs a mechanism, how this stack enforces it. A rule the
   stack cannot enforce is listed under **Gaps** with what to do instead. Never drop it silently.
4. **Skeleton**: what `start` generates for a walking skeleton, including initial safe defaults
   and authorized/refused behavior, security ownership and a safe response exercise.
5. **Gotchas**: things in this stack that pass every check and still break.

Rules that are pure process (decisions, review, measurement) need no mapping.
Map [project-owned style](../style.md): existing conventions or user choices take precedence
over our [optional defaults](../recommendations/style-defaults.md). The [starter configs](../../templates/style/README.md)
include Python, PHP/Laravel, JS/TS, PowerShell, C#/WPF/WinForms, Go, Rust and Bash. These are
style-only draft recommendations, not complete reference profiles for those stacks. Record
all maintained languages/grammars, pins, check/fix commands and convergence evidence.
Map [maintainability](../maintainability.md) from the beginning: actual complexity limits,
review thresholds, public-contract scope, reference/example checks and retirement reports.
State which mechanisms enforce invariants and which need human interpretation. Mark untrialled
mappings draft even in a Reference profile; missing mechanisms stay visible under Gaps.
Map the [security baseline](../security.md) to actual checks and safe detection fixtures,
dependency/install trust, secure initial defaults and abuse tests. Define current report
evidence, error/skip handling, response ownership and a separate authorized deployment
verification procedure. New security mechanisms remain draft until trialled; a reference
label on the profile does not certify application or deployment security.
For WK-6, map the [worktree lifecycle](../worktrees.md) to concrete bootstrap and cleanup
commands and configuration keys for databases, ports, queues and storage used by the stack.

## Support matrix

| Stack or scope | Style starters | Stack guidance | Reference evidence |
|---|---|---|---|
| [Django](django.md) | Python; template/frontend scope selected separately | Reference baseline; newer mappings marked † are draft | Historic Django trials; new MT/SE/ST/TS mechanisms untrialled |
| [Python](python.md) | [Python](../../templates/style/python/ruff.toml) | Draft CLI/service profile | No full application trial |
| [PHP](php.md) | [PHP](../../templates/style/php/.php-cs-fixer.dist.php) | Draft CLI/service profile | No full application trial |
| [Laravel](laravel.md) | [Pint](../../templates/style/laravel/pint.json) and [Blade](../../templates/style/laravel/.bladeformatterrc.json) | Draft PHP extension | No full application trial |
| [JavaScript / TypeScript](node-typescript.md) | [JS/TS](../../templates/style/javascript/eslint.config.mjs) | Draft Node/application guidance | Syntax checks only |
| [C# / .NET](dotnet.md) | [C#](../../templates/style/csharp/.editorconfig) | Draft shared .NET profile | Local whitespace smoke only |
| [WPF](wpf.md) | C# plus [XAML](../../templates/style/wpf/Settings.XamlStyler) | Draft .NET extension | No designer/UI application trial |
| [WinForms](winforms.md) | C# plus [resources](../../templates/style/winforms/.editorconfig) | Draft .NET extension | No designer/UI application trial |
| [Go](go.md) | [Go](../../templates/style/go/check-format.go) | Draft CLI/service profile | Local formatter-wrapper smoke only |
| [Rust](rust.md) | [Rust](../../templates/style/rust/rustfmt.toml) | Draft CLI/service profile | Configuration parsing only |
| [PowerShell](powershell.md) | [PowerShell](../../templates/style/powershell/Invoke-Style.ps1) | Draft automation/module profile | Syntax/data parsing only |
| [Bash](bash.md) | [Bash](../../templates/style/bash/.editorconfig) | Draft shell-tool profile | No full pipeline/application trial |
| JSON/YAML/Markdown/CSS/HTML | [Shared defaults](../recommendations/style-defaults.md) | Supporting file types within the selected stack | Verify parser and actual coverage per project |
| Other stacks | Adapt suitable starters | Create a Draft from [_template.md](_template.md) | No implied support or omitted rules |

**Starter** means an asset exists; **Draft** means proposed mechanisms and gaps exist;
**Reference** requires a real project trial. New draft mappings never inherit validation just
because they appear in a Reference file. No label certifies application or deployment security.

## Select and combine

Prefer the actual framework: Django for Django, PHP plus Laravel for Laravel, .NET plus WPF
or WinForms for desktop apps. Read parents first. An extension replaces only explicitly
overridden mechanisms; other parent obligations still apply. Resolve choices in the project's
`docs/stack-profile.md`; do not run competing formatters or duplicate base recipes.

Mixed stacks combine scoped mechanisms under one check. Browser-only JS/TS must select its
framework/bundler rather than inherit Node runtime assumptions. Shell tools state their local
principal, permitted resources and destructive-action policy instead of omitting access tests.
These profiles describe project recipes to generate, not scripts shipped as runnable apps
inside this kit. Create and exercise recipes before claiming rules met. Select supported
versions, pin reviewed inputs and preserve safe data/credentials. A profile grants no install,
production, deployment or messaging authority.

## Shared baseline

Each Draft inherits these mappings and supplies stack specifics or gaps in its own table.
Pure process rules remain in the framework playbooks rather than being repeated per stack.

| Rules | Mechanism to generate and verify in the adopting project |
|---|---|
| IN-1, IN-3 to IN-5, CK-2 | Agent instructions/navigation plus command, path, link and budget checks |
| CK-1, CK-4, CK-6, CK-8 | One fail-fast check with useful messages, local feedback, clean committed-state CI and host merge protection |
| ST-1 to ST-3 | Language matrix/configs/pins, check/fix/convergence evidence and reviewed scope/exceptions |
| AP-1 to AP-4, RV-1 | Approval policy/index, preserved subjects and real human source/authority; trusted required-stage selection, freshness and requirement trace. Mechanical checks alone are not consent |
| GR-1 to GR-4 | Safe credentials/data, task checkout, human authorization and tool-specific blocking. Claude hook exists; other agents need real equivalents or explicit gaps |
| GR-5, GR-6 | Bounded sandboxed automation and dry-run data commands with explicit apply |
| MT-1 to MT-3 | Contract checks/review, actual complexity limits and reviewed findings, retirement evidence and scoped baselines |
| MT-4 (practice) | Baseline/characterization checks, consumer and contract analysis, incremental preservation evidence and final scope/limits; apply stack-specific reflection/configuration/serialization checks where relevant |
| MT-5 (practice) | Canonical debt evidence/ownership/dispositions, linked stack-specific exceptions/consumers, reviewed deferral and verifiable resolution; scanner output alone is a candidate |
| TS-1 to TS-12 | [Testing guidance](../testing.md): approved criteria, separate acceptance context, witnessed red/green/refactor, independent validity/assertions, bug regressions, resource isolation, real boundary coverage and complete discovery/results |
| TS-13 (practice) | Selected critical-behavior sensitivity trials in isolated copies; record survivors/limits, no universal score or promotion without trials |
| WK-4, WK-6 | Changelog checks and isolated per-checkout databases/ports/queues/storage with explicit handoff and integration |
| SE-1, SE-6 | Versioned threats/requirements and owned findings with deadlines, expiring human decisions and response exercise |
| SE-2, SE-3 | Applicable secret/code/dependency/config checks, reviewed transitive/build sources, reproducible installs and current complete reports |
| SE-4, SE-5 | Safe skeleton behavior, effective authorization and abuse tests; release/environment verification stays separate |
| AR-1 to AR-6 | Access declarations, authoritative operations, dependency boundaries, actor-attributed writes and controlled integration/input sinks; unsupported enforcement remains a gap |
| OP-1 to OP-8 | When machines use the system: shared operation contracts, narrowed credentials, attribution, safe retries, constrained authority and outside-load budgets |

## Gaps and promotion

Every Draft must resolve actual versions, check scripts, framework choices, complexity limits,
security tools/freshness and administrative controls before scoring. No general profile
proves a tenant model or deployment safe. List unmapped rules, not only absent tools; a
missing implementation is not evidence of non-applicability.

Promote only after a real project trial records bootstrap/check/CI, refusal behavior, gaps and
adoption evidence in [validation](../validation.md) and README status. Human review decides
promotion; a syntax smoke or agent-written description does not make a profile Reference.
