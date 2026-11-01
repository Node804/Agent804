# Optional style starters

These are editable recommendations, not requirements to choose these styles or tools. The
project-owned policy governs after adoption (ST-1 to ST-3). All starters are Draft until
their actual project pipeline passes violation/check/fix/convergence trials.

## Adopt

1. Inspect existing conventions and preserve them unless a change is agreed. Offer these
   defaults only when the user wants a starting point. Do not mass-copy every language folder.
2. Copy the selected files to the project root or documented tool directory; merge existing
   configs rather than replacing them. Merge [.editorconfig](.editorconfig) and optional
   [.gitattributes](.gitattributes) deliberately. Do not change unrelated files' line endings.
3. Review sources and select compatible exact tool/runtime versions before installation.
   Commit project lock/manifests and verified binary/toolchain pins. These templates do not
   embed arbitrary or perpetually current package versions. Configure CI/editor to match.
4. Record language/grammar scope, exclusions, check/fix commands and migration plan in the
   stack profile or project style document. Include tests and tools, not only application code.
5. Connect the checks below to the one check command. Replace example paths with maintained
   paths. Assert failures and stable formatting with safe fixtures before declaring coverage.

Commands below assume reviewed, pinned tools have already been installed/restored. Never
download latest tools implicitly in the check. Formatting/build analyzers and plugins execute
code: untrusted projects and dependencies still need the security baseline's isolation.

## Python

Copy [ruff.toml](python/ruff.toml), or merge it into the existing Ruff/pyproject configuration.
Pin Ruff through the project's Python lock or tool environment; align supported Python syntax.
Check: `ruff check .` followed by `ruff format --check .`. Fix imports/lint with reviewed safe
`ruff check --fix .`, then `ruff format .`; run checks again. Do not run a second competing
formatter. This small style config does not replace a Django/security/type-checking profile.

## PHP

Copy [.php-cs-fixer.dist.php](php/.php-cs-fixer.dist.php). It selects explicit PER 3.0 rather
than a moving latest alias. Pin PHP and a compatible `friendsofphp/php-cs-fixer` in the
Composer lock. Review Finder scope, cache location and vendored/generated exclusions.
Check: `php vendor/bin/php-cs-fixer fix --dry-run --diff --using-cache=no`.
Fix: `php vendor/bin/php-cs-fixer fix`. This formats PHP; semantic analysis is a separate
project-selected stage. Configuration itself is executable PHP and must be trusted.

## Laravel

Copy [pint.json](laravel/pint.json). Choose Pint's `laravel` preset as the PHP authority instead
of running the standalone PER fixer over the same files. Pin `laravel/pint` with Composer.
Check: `php vendor/bin/pint --test`. Fix: `php vendor/bin/pint`.
Pint's preset follows its pinned release; it is not a claim of exact PER conformance. Copy
[.bladeformatterrc.json](laravel/.bladeformatterrc.json) and pin `blade-formatter` with the
frontend lock for Blade: check `blade-formatter "resources/views/**/*.blade.php" --check-formatted`,
fix with `--write` instead. Trial custom directives and embedded PHP/JS; exclude Blade from
generic HTML/PHP formatters so they do not fight its owner.
Frontend JS/TS/CSS and JSON need their own declared checks; Pint does not cover them.

## JavaScript and TypeScript; structured text

Copy [.prettierrc.json](javascript/.prettierrc.json), [.prettierignore](javascript/.prettierignore)
and [eslint.config.mjs](javascript/eslint.config.mjs). Pin Node, `prettier`, `eslint`,
`@eslint/js`, `typescript`, `typescript-eslint` and `eslint-config-prettier` using the chosen
package-manager lock. Use locally installed binaries through scripts; do not use download-on-
demand commands. Declare browser/Node globals for actual path scopes and add framework parsers
for JSX/templates as needed. The starter intentionally does not grant all runtime globals.
Check: `prettier --check .` and `eslint . --max-warnings=0` in package scripts.
Fix: reviewed `eslint . --fix`, then `prettier --write .`, then check again.
Prettier may cover maintained JSON/YAML/Markdown/CSS/plain HTML too; inventory those paths.
Unknown grammars and template plugins need explicit trial/coverage, not a blanket claim.

## PowerShell

Copy [settings](powershell/PSScriptAnalyzerSettings.psd1) and [Invoke-Style.ps1](powershell/Invoke-Style.ps1)
together into a tools folder. Pin PowerShell and the PSScriptAnalyzer module; load that pinned
version in the project environment. The wrapper compares formatter output and fails on
analyzer diagnostics instead of merely printing them. Supply explicit maintained files, for
example `pwsh -File tools/Invoke-Style.ps1 -Path scripts/Example.ps1`.
Add `-Fix` for formatting. The caller must collect all declared `.ps1`, `.psm1` and `.psd1`
files, including extensionless scripts when applicable, and propagate failures. Format mode
does not automatically fix every analyzer finding. The rule list is not a security baseline.

## C#

Merge [.editorconfig](csharp/.editorconfig) and [Directory.Build.props](csharp/Directory.Build.props).
The optional default is four spaces, explicit braces and file-scoped namespaces; select a
compatible language version, or customize for an older project. Pin the exact SDK in
`global.json` with an explicit roll-forward policy; pin third-party analyzers and lock restore
where used. Restore only reviewed dependencies before checking.
Check: `dotnet format <solution> --verify-no-changes --no-restore`, followed by the declared
build/analyzer check. Fix: `dotnet format <solution> --no-restore`.
Build style enforcement is enabled, but warnings must be translated into a failing check by
the project's selected diagnostics/warning policy. Do not assume IDE suggestions fail CI.
Formatting can compile/run analyzers; `--no-restore` does not make untrusted projects safe.

## WPF

Use the C# starter for authored code-behind/view models, and copy
[Settings.XamlStyler](wpf/Settings.XamlStyler) for authored XAML. Pin `XamlStyler.Console` in
the local .NET tool manifest and restore it deliberately. Example XAML check:
`dotnet tool run xstyler -- -d <authored-xaml-directory> -r -c Settings.XamlStyler -p`.
The same command without `-p` formats. Verify the pinned tool's failure exit status with a
bad-format fixture. Exclude generated `obj` output by selecting authored roots; review
bindings, resources and designer/build round-trips on Windows. `dotnet format` alone does
not establish XAML coverage. A UI formatter is not proof of equivalent UI behavior.

## WinForms

Use the C# starter for authored partial classes and event handlers; merge the optional
[resource settings](winforms/.editorconfig). Inspect actual generator ownership before
excluding specific `.Designer.cs` or generated resource outputs. Never blanket-exclude all
partial classes or all C# in a forms directory. Do not hand-reformat designer-owned output.
Document its generation policy and verify a Visual Studio designer round-trip and Windows
build. Authored `.resx` content needs an XML-aware policy/check or an explicit coverage gap;
editor indentation settings alone do not enforce XML formatting. Designer compatibility
remains an explicit trial, not a claim made by this starter.

## Go

Merge the [Go editor settings](go/.editorconfig); `gofmt` owns layout. Pin the Go toolchain and
review any automatic toolchain-download policy. Copy [check-format.go](go/check-format.go)
to `tools/check-format.go`. Check with `go run tools/check-format.go <maintained-path>`;
the wrapper fails when `gofmt -l` lists files, since listing alone can exit successfully.
Fix with `gofmt -w <maintained-path>`. Run `go vet ./...` as a separate quality check using
the project's reviewed module/workspace scope. Do not feed `./...` package syntax to gofmt.
Keep vendor/generated handling explicit and check authored tests/tools too.

## Rust

Copy [rustfmt.toml](rust/rustfmt.toml); align edition/style edition with `Cargo.toml`. This
new-project default is 2024, not permission to migrate an existing crate. Pin an exact release
in `rust-toolchain.toml` with `rustfmt` and `clippy` components; commit the relevant lock files.
Check: `cargo fmt --all -- --check`, then `cargo clippy --all-targets -- -D warnings` for the
declared workspace/features. Fix: `cargo fmt --all`. Keep feature/target coverage explicit;
Rust formatting alone does not check macro-generated syntax or unselected targets.

## Bash

Merge the [Bash editor/shfmt settings](bash/.editorconfig) and copy [.shellcheckrc](bash/.shellcheckrc).
Pin Bash, shfmt and ShellCheck. Check with `shfmt -d <bash-files>` and
`shellcheck <bash-files>`; both failures must propagate. Fix with `shfmt -w <bash-files>`.
Use explicit inventory paths including extensionless scripts. Bash is distinct from POSIX
sh: do not force these settings over scripts declaring another dialect. shfmt printer/parser
flags override its EditorConfig settings, so do not add conflicting flags. Check safe scripts
statically; do not execute them merely to test style. Clear/review user-level tool overrides
in CI and account for sourced-file coverage.
