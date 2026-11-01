# Validation

I built Agent804 from my own work building agentic apps with coding agents. Then I checked it
against what other people building this way have published, and used their work to reinforce
it: it confirmed most of what I had, tightened a few rules, and gave me some practices I didn't
have yet, like having a separate session write the tests and zoning code green, yellow or red
by how much damage a change could do.

The table records what each reference reinforced and, where Agent804 chose differently, why.
It is here so that anyone changing a rule, person or agent, can see what it rests on.

| Reference | Reinforced | Where Agent804 chose differently, and why |
|---|---|---|
| Anthropic, [Claude Code best practices](https://code.claude.com/docs/en/best-practices) | Short instructions holding only what an agent can't find for itself; must-always rules as hooks and deny rules; the check command up front; review in a fresh context; a stop hook so the agent can't finish with the check red | |
| Anthropic, [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Keep always-loaded context small; add instructions for failures you actually see | |
| Anthropic, [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) | A boot script before any feature; progress kept in the repository; an end-to-end check before "done" | |
| OpenAI, [Harness engineering](https://openai.com/index/harness-engineering/) | `AGENTS.md` as a map into `docs/`; the repository as the system of record; lint messages that tell the agent how to fix the problem; scheduled doc gardening | OpenAI makes human review optional at high volume. Agent804 keeps a person on every merge: few teams have the tooling and coverage that makes skipping it safe, and OpenAI says as much |
| Simon Willison, [Vibe engineering](https://simonwillison.net/2025/Oct/7/vibe-engineering/), [Designing agentic loops](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/) | Tests first and run first; small reviewed changes with evidence; no production credentials for agents | A production system reachable with no credential at all isn't scored as a leaked secret, because the repository can't fix it; it is reported as an outside risk instead |
| Harper Reed, [My LLM codegen workflow atm](https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/) | Spec, then plan, then checklist; a branch before every session | One workflow for every change. Agent804 sizes the spec to the change: a full spec for a one-line fix is waste |
| Addy Osmani, [My LLM coding workflow going into 2026](https://addyosmani.com/blog/ai-coding-workflow/), [Brownfield agentic engineering](https://addyosmani.com/blog/brownfield-agentic-engineering/) | Instructions hold only what code can't say; a review comment that keeps coming back becomes a check; a separate session writes the tests; risk zones; measure lead time and interventions, not lines | |
| Kent Beck, [Augmented coding: beyond the vibes](https://newsletter.kentbeck.com/p/augmented-coding-beyond-the-vibes) | One failing test at a time; structural and behavioural changes kept apart; signs an agent is going wrong | |
| Birgitta Böckeler, [Understanding spec-driven development](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) | One fixed workflow doesn't fit every size of change; heavy specs are hard to review | |
| Birgitta Böckeler, [Context engineering for coding agents](https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html), [Harness engineering for coding agent users](https://martinfowler.com/articles/harness-engineering.html) | Guides that steer and sensors that check; deterministic checks before AI review; a small always-loaded file with the rest on demand | |
| GitHub, [Spec Kit](https://github.com/github/spec-kit) | A project constitution (here, `AGENTS.md`); `[NEEDS CLARIFICATION]` markers resolved before planning | Spec Kit fixes bugs by changing the spec and regenerating the code. Agent804 fixes the code, and the harness if a rule was missing: regenerating from the same spec doesn't give the same code twice |
| Git, [worktree](https://git-scm.com/docs/git-worktree) and [rev-parse](https://git-scm.com/docs/git-rev-parse) documentation | Separate working files, index and HEAD with shared history; linked checkouts use a `.git` file. Discover private metadata through Git; keep check state separate and retain branch/removal safeguards (WK-6, GR-4) | Worktrees isolate files, not credentials, databases or processes. Agent804 requires separate mutable resources and an explicit handoff and integration check |
| Python, [PEP 8 comments](https://peps.python.org/pep-0008/#comments) | Useful current documentation, restrained inline comments and documented public interfaces (MT-1) | Contract scope follows each stack and project; no comment quota or requirement to restate obvious code |
| Ruff, [complexity](https://docs.astral.sh/ruff/rules/complex-structure/), [settings](https://docs.astral.sh/ruff/settings/#lint_mccabe_max-complexity) and [public-function documentation](https://docs.astral.sh/ruff/rules/undocumented-public-function/) | Deterministic Python complexity and documentation-presence mechanisms (MT-1, MT-2) | Presence cannot prove accuracy; metrics cannot prove cohesion. Project thresholds and exceptions need review; new Django mappings remain draft |
| GitClear, [The Maintainability Gap](https://www.gitclear.com/the_ai_code_quality_maintainability_gap) | Investigating duplication, declining reuse, error masking and churn supports authoritative rules, retirement review and structural trends (AR-2, MT-3, MS-1, MS-2) | Vendor observational analysis, not proof of causality or universal thresholds. Reports prompt investigation; fresh-maintainer exercises (MS-4) test actual maintenance |

## Local regression evidence

The independent repository review reproduced a skipped hook for `.git` files and an unchanged
fingerprint after editing a staged file before the first commit. `scripts/test_stop_check.py`
exercises these paths, independent worktree caches, command changes and failure reporting.
The retry contract now explicitly covers concurrency, crash recovery and unknown external
outcomes; these are required acceptance scenarios for adopting projects, not claims that the
framework implements a transaction layer. Separate append-only ADR evidence records resolve
the conflict between later test results and frozen Accepted decisions. Neither extension has
yet been trialled end to end in a production application.

## Maintainability adoption

MT-2 now gates rung 2, MT-1 gates rung 4, and MT-3 joins rung 6; there is no ninth rung.
The existing rules now address navigation, current references, authoritative business rules,
cohesive boundaries, dependency choices and red/green/refactor. Existing projects may retain
specific reviewed debt without allowing new unapproved or worsening findings. MS-4 remains
a practice pending trial. These scoring changes and new profile mechanisms have not yet been
reassessed against the reference projects; neither documentation nor repository checks prove
the adoption workflow works. The next trial must record scores under the revised gates and
dispositions from an unfamiliar human and a fresh agent context.

## Security references and adoption

| Reference consulted | Reinforced | Limits and choices |
|---|---|---|
| [NIST SSDF](https://csrc.nist.gov/projects/ssdf), version 1.1 overview and practices | Development preparation, software protection, secure production and vulnerability response support SE-1 to SE-6 | Risk-based selection, not a universal checklist or certification claim; application owners must read and map their selected requirements |
| [OWASP ASVS](https://asvs.owasp.org/), 5.0.0 overview and reference guidance | Versioned application-security requirements, applicability and verification evidence | Web controls are selected for actual exposure; a subset never implies an entire ASVS level is verified |
| [Django deployment checklist](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/) | Production settings and `check --deploy`, secret separation and effective environment checks | Local deployment-shaped configuration is not proof of actual TLS/proxy/database deployment |
| [pip-audit security model and options](https://github.com/pypa/pip-audit) | Known-vulnerability auditing with explicit collection coverage and restricted resolution | Auditing is not malicious-package detection; dependency resolution may execute code. Review sources first and avoid untrusted installation as an audit prerequisite |
| [Gitleaks commands and exit behavior](https://github.com/gitleaks/gitleaks) | Separate working-file and history scans, report handling and representative detection fixtures | Scope, redaction, errors and shallow history must be recorded; a baseline cannot itself accept exposure |

SE-2 gates rung 2, SE-1/SE-3 rung 3, SE-4/SE-6 rung 4 and SE-5 rung 5. Security enforcement
paths receive human review, and OP-6 now needs actual authority-boundary evidence. Build and
Operate scores remain separate from release/environment security readiness. The new gates,
dependency/build verification, response exercise and Django mappings remain untrialled on
reference projects; repository validation checks document integrity, not deployed security.

## Style references and adoption

| References consulted | Reinforced | Scope and limits |
|---|---|---|
| [Ruff](https://docs.astral.sh/ruff/formatter/), [Black](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html), [Prettier integration](https://prettier.io/docs/integrating-with-linters), [typescript-eslint](https://typescript-eslint.io/getting-started/) and [EditorConfig](https://editorconfig.org/) | A single layout authority, compatible lint stages, committed configuration and editor/CLI agreement support ST-1/ST-2 | Project choices prevail; shared editor properties and copied configs alone do not establish enforcement |
| [PHP-FIG PER](https://www.php-fig.org/per/coding-style/), [explicit fixer preset](https://cs.symfony.com/doc/ruleSets/PER-CS3x0.html), [Pint](https://laravel.com/docs/12.x/pint) and [blade-formatter](https://github.com/shufo/blade-formatter) | Explicit supported style revisions and separate PHP/Blade ownership | Pint's Laravel preset is a project choice, not exact PER conformance; pin packages and trial real Blade directives |
| [.NET format](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-format), [.NET options](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/code-style-rule-options) and [XAML Styler CLI/config](https://github.com/Xavalon/XamlStyler/wiki/Script-Integration) | C# EditorConfig and explicit diagnostic/check behavior; XAML is a separate grammar | Formatting can run build/analyzer code; UI/designer round-trips and generated-file ownership need project evidence |
| [PSScriptAnalyzer](https://github.com/PowerShell/PSScriptAnalyzer), [Go](https://go.dev/doc/effective_go#formatting), [rustfmt](https://github.com/rust-lang/rustfmt), [shfmt manual](https://raw.githubusercontent.com/mvdan/sh/master/cmd/shfmt/shfmt.1.scd) and [ShellCheck manual](https://raw.githubusercontent.com/koalaman/shellcheck/master/shellcheck.1.md) | Toolchain editions, explicit dialects and reliable error handling matter | A file list or diagnostic stream may not fail a check; wrappers and complete pipeline convergence need exercise |

ST-1 to ST-3 gate rung 2 without adding a rung or requiring these tool choices. Optional
starters are style-only Draft recommendations; adopting projects choose/pin compatible
versions and verify intended coverage. Parser/smoke checks do not validate full stacks,
cross-platform behavior, WPF/WinForms designers or every template grammar. Reference-project
scores and full application adoption under the new gates remain to be trialled.

Local starter checks used the installed Go 1.24.5 and .NET SDK 9.0.320 on isolated fixtures.
The Go wrapper rejected an unformatted file without changing it, passed after formatting,
remained stable on a second pass, and rejected syntax errors and flag-like path input.
The C# whitespace folder check likewise failed without changes, passed after formatting and
converged; this does not exercise a solution's full analyzers or Windows UI designers.
PHP config lint, JavaScript config syntax, PowerShell syntax/data parsing and standard-library
TOML/XML/JSON parsing passed. Uninstalled formatters/analyzer modules and full pipelines are
not validated by these syntax checks; no external style packages were installed for the trial.

## Draft stack profile coverage

The style catalog now lives under `framework/recommendations/`; it remains optional and
separate from complete-stack guidance and copyable templates. Eleven new Draft profiles add
proposed check/bootstrap/test, architecture, security and isolation mechanisms plus explicit
gaps. Laravel extends PHP; WPF and WinForms extend the shared .NET profile. The support matrix
distinguishes these drafts from Django's historical Reference baseline. No new application
was generated or trialled to justify this documentation change, and none was promoted.

Additional primary documentation consulted for those proposals:

| References | Supports | Limits |
|---|---|---|
| [pytest](https://docs.pytest.org/en/stable/), [PHPStan](https://phpstan.org/user-guide/getting-started), [Composer](https://getcomposer.org/doc/03-cli.md) | Language-specific tests, static analysis and reviewed dependency commands | Tool availability does not define an app's access model, architecture or safe install authority |
| [Laravel tests](https://laravel.com/docs/12.x/testing) and [authorization](https://laravel.com/docs/12.x/authorization) | Framework HTTP tests and policies/gates behind shared actions | Their existence does not prove every route/job uses them; discovery and bypass tests remain project work |
| [Node tests](https://nodejs.org/api/test.html), [.NET tests](https://learn.microsoft.com/en-us/dotnet/core/testing/), [runner selection](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-test) and [ASP.NET authorization](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/introduction) | Runtime/test-driver and effective authorization mechanisms | Actual runtime/framework, runner options, target scope and failure handling must be selected and exercised |
| [WPF](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/overview/), [WinForms](https://learn.microsoft.com/en-us/dotnet/desktop/winforms/overview/) and [FlaUI](https://github.com/FlaUI/FlaUI) | Shared .NET base with separate Windows UI/designer and automation obligations | A compatible desktop/runner and actual UI round-trips are unverified; headless unit tests do not replace them |
| [Go tests](https://go.dev/doc/tutorial/add-a-test), [Go vulnerabilities](https://go.dev/doc/security/vuln/), [Cargo tests](https://doc.rust-lang.org/cargo/commands/cargo-test.html), [Pester](https://pester.dev/docs/quick-start) and [bats-core](https://bats-core.readthedocs.io/en/stable/) | Native test, advisory and isolated automation mechanisms | Feature/platform scope, dependency trust, failure propagation and actual command/refusal acceptance remain project-specific |

## Traceable approval references and adoption

| Reference consulted | Reinforced | Limits and choices |
|---|---|---|
| [GitHub protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) | Required human reviews, reviewed-change freshness and independent latest-push approval support AP-1 to AP-3 and RV-1 | Host controls and bypasses must be inspected, not inferred from repo prose; other hosts need equivalent verified mechanisms |
| [SLSA attestation model v1.2](https://slsa.dev/spec/v1.2/attestation-model) | Distinguishing artifact identity, statement meaning and authenticated issuer supports explicit subject/scope/source records | A hash or agent-written reviewer name does not authenticate consent. Ordinary projects need not adopt signed attestations; no SLSA conformance is claimed |

AP-1 to AP-3 gate rung 3, AP-4 rung 5 and RV-1 rung 4; DC-4 requires actual owner-source
evidence. The portable validator and twelve synthetic regression cases verify mechanical
structure, preserved snapshots, selected scope/dependency freshness, conditions/expiry and
non-authorizing output. No fixture is a real human approval. Original-source authentication,
reviewer authority, materiality/administrative-transition adapters, actual host enforcement
and cross-session adoption remain untrialled; revised reference scores are not established.

## Testing references and adoption

| References consulted | Reinforced | Limits and choices |
|---|---|---|
| [Fowler: TDD](https://martinfowler.com/bliki/TestDrivenDevelopment.html) | Small red/green/refactor cycles and deliberate refactoring support TS-2 | Commit order cannot prove execution; preserved revision/patch and actual results are required. Existing passing behavior is verification, not fabricated TDD |
| [Google: change-detector tests](https://testing.googleblog.com/2015/01/testing-on-toilet-change-detector-tests.html) | Independent assertions and avoiding implementation mirrors support TS-8 | Protocol interaction/order assertions remain valid when they express a real contract |
| [Google: end-to-end tests](https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html) and [coverage practices](https://testing.googleblog.com/2020/08/code-coverage-best-practices.html?hl=sk) | Effective test boundaries and risk-focused coverage support TS-5/TS-11 | No fixed layer ratio or coverage percentage; representative journeys and real integration remain necessary |
| [Stryker introduction](https://stryker-mutator.io/docs/) and [mutant states](https://stryker-mutator.io/docs/mutation-testing-elements/mutant-states-and-metrics/), [Microsoft mutation testing](https://learn.microsoft.com/en-us/dotnet/core/testing/mutation-testing) | Deliberate faults can expose weak assertions (TS-13) | Invalid compilation is not behavioral detection; survivors need interpretation and no universal score proves requirement correctness |

TS-10/TS-12 gate rung 2, TS-11 rung 4, and TS-8/TS-9 (where bug fixes apply) rung 5.
TS-13 remains a reported practice pending trials. Existing runner references above informed
Draft stack-specific discovery, failure, isolation and target-scope guidance. Repository
checks validate documentation integrity and existing mechanical regressions, not the new
TDD workflow or every native runner. Full application red/green handoffs, compiled-interface
diagnostics, discovery failures, flaky-test remediation and sensitivity trials remain pending;
historical Reference scores have not been re-established under these gates.

## Refactoring reference and adoption

| Reference consulted | Reinforced | Limits and choices |
|---|---|---|
| [Fowler: Refactoring](https://refactoring.com/) | Small transformations preserve observable behavior while improving internal structure; preparatory and everyday refactoring support MT-4 | Agent804 adds explicit consumer/contract and baseline/final evidence for agent handoffs. Tests support exercised scope, not complete equivalence; characterization need not produce artificial red |

The new refactor playbook uses existing plan/PR records and approval rules. MT-4 is a reported
practice at rung 6, with no new rung or gate. Portable metadata, links, budgets and rule-ID
checks validate kit integrity, not behavioral preservation in adopting applications. Standalone
refactor trials, unknown/dynamic consumers, weak-test characterization and separation of
hidden behavior changes remain untrialled. No Reference scores or runtime compatibility are
established by adding this documentation.

## Agent-host references and adoption

Official OpenAI documentation checked 2026-10-31:

| References consulted | Reinforced | Limits and choices |
|---|---|---|
| [AGENTS.md discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md) and [skills](https://learn.chatgpt.com/docs/build-skills) | Effective root/nested/override guidance, loading limits, progressive skill discovery and intact resource layout support IN-1/IN-4/IN-5 | Shared policy remains host-neutral; metadata/path resolution does not prove actual loading or independent context |
| [Hooks](https://learn.chatgpt.com/docs/hooks) | Codex Stop JSON/exit-2 contract, trust, config merging and orchestration-specific limits inform GR-4 adapters | Fixture success does not establish host registration, trust, continuation or timeout handling. Reporting escape never means a passing check |
| [Configuration](https://learn.chatgpt.com/docs/config-file/config-reference) and [command rules](https://learn.chatgpt.com/docs/agent-configuration/rules) | Effective sandbox/approval controls and limited command-prefix enforcement support GR-2 | Outside-sandbox Git prompts are supplementary; wrappers/other tools need review. Automatic permission approval is not human architecture/feature/merge consent |
| [Plugin packaging](https://developers.openai.com/plugins/build/plugins) | Root portable manifest, fixed skill layout and OpenAI extension match the existing distribution format | No compatibility-overlay migration is required; intact layout/resource checks do not prove live installation |

Thirteen Codex adapter fixtures exercise the installed pair, wire validation, Git failures,
cache/resource paths, linked worktrees, bounded reporting, malformed input and the rendered
absolute-path command from a subdirectory. Two resource-layout fixtures resolve an intact
relocated kit and reject a skills-only copy. Existing Claude/shared-engine
regressions remain. A local Codex CLI 0.141.0 rule evaluation parsed the Draft direct Git
push rule and returned prompt; no Git push occurred. This is not a live approval/trust test.
The CLI reported inaccessible alias/temp maintenance paths; no global configuration was changed.
TOML/JSON and Python validation cover starter integrity, not effective runtime policy.
Actual client discovery/trust/Stop continuation, timeout behavior, platform configuration,
independent-context handoffs and cross-host application comparisons remain pending. Host
profiles and adapters are Draft integration guidance, with no automatic Reference promotion.

## Optional routing references and limits

| References consulted (2026-10-31) | Reinforced | Limits and choices |
|---|---|---|
| [OpenAI models/effort](https://learn.chatgpt.com/docs/models) | Task-based selection, native effort tradeoffs and non-equivalent settings inform optional WK-7 | Guidance is a starting point, not account access or cross-provider superiority evidence; power modes may include delegation |
| [OpenAI usage guidance](https://learn.chatgpt.com/docs/pricing?codex-pricing-plans=individual) | Model, context, reasoning, tools and cache affect usage; shared pools and current observations inform MS-5 | No static balance/rate table, invented token conversion, API entitlement or guaranteed saving. Consult each selected provider's current official guidance |

The role/effort/budget policy and adversarial input boundaries are proposed framework design,
not an empirical claim that model diversity improves correctness. WK-7/MS-5 are conditional
practices with no scoring gates; single-model separate contexts remain sufficient. Integrity
checks cover new references/frontmatter/budgets, not actual entitlement, quota telemetry,
model routing, independent-role effectiveness or cost savings. Single-model, same-family,
cross-provider and bounded fallback/effort trials remain pending; no model calls or paid
evaluations were performed, and no automatic orchestrator or account adapter was added.

## Context management and debt

[Research and validation limits](validation/context.md) record consulted sources and the
proposed IN-8/WK-8 practices. Context-effectiveness/recovery trials remain pending under MS-4;
repository integrity checks do not establish attention, retrieval recall or complete evidence.
[Debt research](validation/debt.md) and [Grok Build evidence](validation/grok-build.md) record their scopes and pending trials.
