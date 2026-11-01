# Optional style recommendations

**Status: Draft.** These are style-only starting points, not complete validated stack profiles.
Projects choose conventions; these recommendations apply only when adopted (ST-1 to ST-3).
Preserve an existing policy or user preference. See [style policy](../style.md) and the
[starter guide](../../templates/style/README.md) for assets, commands, pins and known gaps.

## Language and framework matrix

| Scope | Optional recommendation | Check/fix authority and caveats |
|---|---|---|
| Python | Ruff formatter, lint/import rules; Black-based existing policies remain valid | `ruff check .` and `ruff format --check .`; safe lint fixes then format. Align supported Python syntax and preserve stronger project checks |
| PHP | PHP-FIG PER 3.0 through an explicit PHP-CS-Fixer ruleset | `@PER-CS3x0`, dry-run check versus explicit fix; pin PHP, Composer dependencies and preset support |
| Laravel | Pint `laravel` PHP preset; blade-formatter for Blade | `pint --test` versus fix; Blade check/write separately. Do not also run the generic PHP/HTML formatter on overlapping syntax |
| JavaScript / TypeScript | Prettier layout, ESLint/typescript-eslint quality rules, compatible conflict-disable config | Local pinned binaries and runtime globals/parsers scoped to real code; check versus explicit fix chain |
| JSON/YAML/Markdown/CSS/plain HTML | Prettier where syntax is supported, shared EditorConfig/Git text policy | Inventory maintained files and handle embedded grammars with selected plugins or explicit gaps; preserve meaningful Markdown whitespace |
| PowerShell | PSScriptAnalyzer settings and Invoke-Formatter | Supplied wrapper compares output, fails on diagnostics/parser errors and separates check from formatting; pin module and shell |
| C# | .NET EditorConfig, SDK formatter and build analyzers | Pin SDK/config; `dotnet format --verify-no-changes --no-restore`; explicit fix, and failing build diagnostics for non-fixable conventions |
| WPF | C# plus XAML Styler configuration and pinned local CLI | XAML passive check versus write; authored XAML and code-behind stay covered; generated `obj` output is handled by generation policy |
| WinForms | C# plus explicit designer/resource ownership | Authored partials/events use normal C# checks; specific generated designer/resource files use generation policy and Windows designer round-trips |
| Go | Toolchain `gofmt`, `go vet` quality checks, tab editor settings | Supplied Go wrapper fails on `gofmt -l` output; `gofmt -w` fixes. Use real paths, not package wildcards, for formatting |
| Rust | Toolchain rustfmt and Clippy, explicit parsing/style edition | `cargo fmt --all -- --check` versus format; declared Clippy feature/target checks. Pin exact Rust release/components |
| Bash | shfmt using Bash syntax/indent policy, ShellCheck quality rules | Diff check versus write and nonzero lint failures; include extensionless scripts and distinguish Bash from POSIX sh |

All check commands are run inside the adopting project against its selected scope. They do
not execute in the Agent804 repository merely because its templates are present. No starter
pins arbitrary current package versions: adoption must choose verified compatible exact
versions in the project's own manifests/locks before declaring reproducibility established.

## Scope and integration

Start with the language matrix in the [profile template](../profiles/_template.md). Record grammar/paths,
adopted convention, authoritative configuration, exact runtime/tool pins, check and fix
commands, exclusions and manual review. Complete application, test, script and tooling scope
matters; a formatter being installed is not evidence that it sees every maintained file.

Shared editor settings are advisory support, not a CLI checker. Makefile/Go tab requirements,
Markdown hard-break whitespace and platform-specific text requirements need deliberate
overrides. Merge provided files instead of introducing competing roots or overwriting config.

For UI frameworks, syntax formatting cannot prove UI equivalence. Verify designer/build
round-trips and representative bindings/resources. Authored `.resx` XML still needs a
project-selected XML check or an explicit gap; editor indentation alone does not supply it.
Never blanket-exclude all partial classes or a UI directory as generated.

## Source references

- [Ruff formatter](https://docs.astral.sh/ruff/formatter/) and [Black style](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html)
- [PHP-FIG PER](https://www.php-fig.org/per/coding-style/) and [explicit fixer preset](https://cs.symfony.com/doc/ruleSets/PER-CS3x0.html)
- [Laravel Pint](https://laravel.com/docs/12.x/pint) and [blade-formatter](https://github.com/shufo/blade-formatter)
- [Prettier/linter integration](https://prettier.io/docs/integrating-with-linters) and [typescript-eslint](https://typescript-eslint.io/getting-started/)
- [EditorConfig](https://editorconfig.org/)
- [PSScriptAnalyzer](https://github.com/PowerShell/PSScriptAnalyzer)
- [.NET formatting](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-format) and [code-style options](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/code-style-rule-options)
- [XAML Styler CLI](https://github.com/Xavalon/XamlStyler/wiki/Script-Integration) and [configuration](https://github.com/Xavalon/XamlStyler/wiki/External-Configurations)
- [Go formatting](https://go.dev/doc/effective_go#formatting)
- [rustfmt](https://github.com/rust-lang/rustfmt)
- [shfmt](https://github.com/mvdan/sh) and [ShellCheck](https://www.shellcheck.net/)

The primary documentation supports available mechanisms and syntax. It does not establish
that these starters work on every application or tool version. Pin and trial the actual
pipeline; full adoption and cross-platform/designer validation remain to be performed.
