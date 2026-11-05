# Profile: Django

- **Status:** Reference (used on a line-of-business platform). Items marked † are recommended
  here but were not yet running on that project; treat them as draft.
- **Applies to:** Python 3.12+, Django 5.2 LTS or later, PostgreSQL

## Baseline

| Concern | Tool | Why |
|---|---|---|
| Package manager and lock file | `uv` with committed `uv.lock` | Fast, one tool, reproducible installs |
| Formatter | `ruff format` | One style; agents never hand-format |
| Linter | `ruff check` with rules `E,F,W,I,B,UP,DJ,S,SIM,RUF,PT`, plus `C90` † | Security and Django checks; the added complexity gate prevents uncontrolled branching |
| Type checker | `mypy` with `django-stubs`, strict in the platform package | Types are the cheapest sensor an agent gets |
| Test runner | `pytest-django`, `factory_boy`, coverage floor | Fixtures as code; the floor is a smoke alarm, not a goal |
| End-to-end tests | `pytest-playwright` † | Drives the real pages (TS-5, SK-2) |
| Architecture checker | `import-linter` | Module boundaries as contracts (AR-3) |
| Framework checks | Django system checks (`manage.py check`) | The project's own invariants fail `check` with a hint (CK-4, AR-1, AR-2) |
| Migrations | `django-linear-migrations` | Two parallel migrations become a merge conflict, not a broken deploy |
| Task runner | `just` | Thin recipes over `uv run`; nothing requires it |
| Changelog | `towncrier` fragments | One file per change, no merge conflicts (WK-4) |
| Pre-commit | `pre-commit` with ruff, `makemigrations --check`, a secret scan | Fast checks before CI (CK-6) |
| Security verification | † Gitleaks, `pip-audit`, Ruff security rules and Django deployment checks | Separate secret, known-dependency, code and configuration evidence; none alone proves safety |

## The check command

```
just check
```

Runs `ruff check`, `ruff format --check`, `mypy`, `lint-imports`,
`manage.py check --fail-level WARNING`, `makemigrations --check --dry-run`, the instruction-file
check, then `pytest --cov`. † Add the security verification steps below to this same recipe.
CI runs the same command against a PostgreSQL service container; unavailable security steps
remain failures or explicit gaps, never silently omitted checks.

## Rule mapping

| Rule | Mechanism |
|---|---|
| IN-3, IN-5 | `scripts/check_agent_docs.py`: line budgets, every nested `AGENTS.md` has a `CLAUDE.md` pointer; named paths exist † |
| IN-4 | † README or local module guide links purpose, public services/selectors, dependency direction and test command; no full symbol inventory |
| ST-1 | Ruff for lint and format, pinned in the lock file; `ruff check .` and `ruff format --check .` in the check, `ruff format .` to fix. Django templates and any frontend code need their own tool or a listed gap |
| RV-1 | † Branch protection on the main branch with a required review from someone other than the author; merges only through pull requests |
| MT-1, IN-5 | † Select Ruff `D100,D101,D102,D103` for public module/class/method/function presence in the declared interface scope. Review meaningful constraints, failures and side effects; check maintained links and exercise examples through tests. Mark history and generated files explicitly |
| MT-2 | † Ruff `C901` via `C90`, with `lint.mccabe.max-complexity = 10` initially. File size: Pylint `max-module-lines` (C0302) or a short script in the check, starting at 500 lines. Duplication: Pylint `duplicate-code` (R0801) or jscpd, with a minimum block size. Review nesting over four blocks and new cross-module dependencies. These are initial choices, not universal limits |
| MT-3 | † Ruff `F401,F841` and reference searches identify candidates; review replaced callers, configuration and dependencies. Trace Django registration, management commands and migrations before removal; record compatibility consumers and review conditions |
| SE-1 | † `docs/security.md` maps assets, identities, routes/jobs/tools, trust boundaries and abuse to pinned SSDF/ASVS requirements; review applicable controls and justified exclusions |
| SE-2 | † Gitleaks scans working files and relevant history with redacted reports; Ruff `S,DJ` checks code; `pip-audit` checks the complete resolved dependency set; Django config and pytest refusal tests run in `just check`. Record tool/feed versions, skips, exclusions, freshness and failures |
| SE-3 | † Review package publisher/source, `uv.lock`, indexes, integrity metadata, build backends and install/CI execution before introduction. `uv sync --locked` in isolated builds verifies resolution consistency, not publisher trust; include transitive/build dependencies and build/release provenance |
| SE-4 | † Separate dev/test/prod settings; require production secrets from the authorized environment, safe production defaults and least-privilege database/service roles. Run deployment-shaped config checks and denial tests locally; authorized operators verify actual TLS/proxy, cookies, exposure, storage and logging before readiness |
| SE-5 | † pytest covers cross-user/object/site/tenant refusals, direct URLs and alternate adapters, plus applicable injection, CSRF, uploads/paths, network access and resource limits. Assert no prohibited state change, disclosure or outside effect; verify authorized paths too |
| SE-6 | † `docs/security.md` identifies owner, concrete response deadlines, blocking policy, scoped human decisions with expiry; scheduled review rechecks advisories and support status |
| CK-1 | `just check`, mirrored step for step in CI |
| CK-8 | Gitea or GitHub Actions running the check against a PostgreSQL service container, with branch protection. Until a runner exists, `just check-clean`: clones the committed branch to a temporary folder, `uv sync --locked`, runs the check with only `DATABASE_URL` passed through (partly met) |
| CK-4 | System checks raise `checks.Error(msg, hint=..., id="app.E0xx")`; the hint says how to fix it |
| CK-6 | `.claude/settings.json` PostToolUse hook runs ruff on each edited `.py`; pre-commit |
| GR-1 | Deny secret reads as supplementary protection; † isolate development from production credentials/data, use scoped test credentials and synthetic or reviewed sanitized fixtures, or the GR-1 exception recorded in `docs/security.md`. Credential-free production exposure remains a security finding |
| GR-2 | `git commit`, `git push`, `manage.py migrate` in the `ask` list; force-push denied |
| GR-4 | † Run `just check` directly against the current changed state; retain command, scope, revision/patch and results. Failed/missing verification stays incomplete; no Stop hook required |
| GR-6 | A base management command adds `--commit`; without it the command reports what it would do |
| SK-1 | `just bootstrap` writes `.env`, creates the database, migrates and creates an admin; safe to rerun |
| SK-2 | † One Playwright test: sign in, open the landing page, see the module list |
| TS-4 | `AGENTS.md` rule, plus review flags new `skip`/`xfail` markers |
| TS-7 | The test-writing step runs `ruff` and `mypy` on its new tests; then `pytest` shows only the new acceptance tests failing |
| WK-6 | Follow [worktrees](../worktrees.md). Each checkout gets a short unique ID in ignored dev config: `<project>_<id>` database (pytest-django uses `test_<name>`), port, queue and storage prefix as needed. Bootstrap from the lock file, provision dev credentials explicitly, and verify the declared check, action settings and isolated resources inside each checkout |
| AR-1 | `LoginRequiredMiddleware` on; views declare public or explicit access; a system check and URL-resolution test catch missing declarations. † Direct URL/API/tool tests verify effective object and tenant authorization; login middleware alone does not enforce these boundaries |
| AR-2 | Modules subclass a `ModuleConfig(AppConfig)` with key, label, nav, URL prefix and access levels; settings, URLs, nav and permission groups derive from it. † Review changed business rules for one authority in services/selectors and duplicate findings for independent-domain justifications |
| AR-3 | `import-linter` contracts: the platform never imports modules; cross-module imports use public `services` (writes) and `selectors` (reads). † Add declared layer/independence contracts to reject unapproved cycles and review module cohesion |
| AR-4 | Writes go through `services.py`, which validates them |
| AR-6 | † Use Django parameterized ORM/query APIs, template autoescaping and safe serializers; review raw SQL, shell calls, unsafe template escapes, file paths and outbound destinations. Test applicable injection/output/path controls rather than treating validated strings as safe everywhere |
| WK-4 | `towncrier create`; CI fails without a fragment unless labelled |
| OP-1 | An `@operation` decorator in `operations.py` declares name, level, read or write, and pydantic schemas; Django Ninja serves it as REST and a small view serves it as MCP tools |
| OP-2 | API tokens have module scopes, site limits and `can_write` off by default; stored hashed |
| OP-3 | The actor carries user, token and channel (`web`, `api`, `mcp`) into every history row |
| OP-4 | Machine writes require a request ID. A database uniqueness constraint scopes it by owner or tenant and operation; store a validated-input digest and outcome, authorize replay, and reject changed input. Claim and record database effects in one transaction; coordinate concurrent duplicates. Specify retention and expiry. For outside effects use downstream deduplication or a durable job with reconciliation; an unknown outcome cannot be blindly retried |
| OP-5 | Bearer header only; query-string tokens refused |
| OP-6 | † Record outside-text threats and exercise planted instructions against tool credentials, destinations and write/publish permissions; inspect attempted operations, not only the agent's response |
| OP-7 | † Definitions (labels, forms, screens) are drafted and saved through operations at `designer` level; publishing needs a person at that level, never a token |
| OP-8 | Each MCP or ODBC source has a request budget (a requests-per-minute setting), refused before sending when spent; reads go through the shared cache, so many viewers and agents cause one read |
| OP-9 | † The operation decorator exposes MCP tools. A designed list, a result bound, and a server-enforced effect are not a running check. Review the list; a wrapper per function is a gap |
| OP-10 | † This profile describes no embedded model feature. When one is added, its prompt, allowed actions, and output effects follow OP-10. Until then the rule is not applicable |
| OP-11 | † Bearer tokens are scoped to modules and sites. Refusal of a foreign token, per-client consent before a third-party call, and session-is-not-authentication are not recorded as running. A local MCP process takes no production credential (GR-1) |

## Testing evidence (draft)

Apply [testing guidance](../testing.md) (TS-7 to TS-12); exercise this mapping before claiming it met.
Record selected apps/test labels and discovery/execution counts. Isolate test databases,
workers and storage; prove actual HTTP/persistence boundaries, not only mocked ORM calls.
Report skips/retries and unavailable database/backend/platform coverage explicitly.

## Gaps

| Rule | Why | Instead |
|---|---|---|
| Template rules (single-line `{# #}`, literal `{{`, `json_script` double-encoding) | Django does not lint templates; mistakes render silently | A small template linter in the check, or `djlint` plus custom rules |
| Translatable text | No check finds an untranslated literal reliably | Review checklist item; `makemessages` diff in CI shows new strings |

## Skeleton

`start` generates: `pyproject.toml` (uv, ruff, mypy, pytest, import-linter config),
`config/settings/{base,dev,test,prod}.py` reading the environment, a `core` app with one view
behind login, `justfile` (`bootstrap`, `check`, `test`, `fmt`, `run`), CI workflow,
pre-commit config, `changelog.d/`, the access test, one Playwright test, and the agent files.

## Worktree resources

Run `just bootstrap` and `just check` inside each checkout. Set its ignored
`DATABASE_URL` to the unique development database; do not point two checkouts at the same
database or override Django's test database name with a shared value. Run the development
server with `manage.py runserver 127.0.0.1:<allocated-port>`.

Where queues or object storage are used, map their actual namespace settings and worker start
commands in the project's `docs/worktrees.md`. Record process IDs and resource ownership in
the plan. Supply stack-specific cleanup commands there before enabling parallel use; cleanup
stops only those workers and removes only that checkout's disposable resources. Never infer
permission to drop a database from its name. This full resource lifecycle remains untrialled.

## Maintainability adoption

The new maintainability mappings above are draft (†); they have not been trialled together.
Generate `docs/maintainability.md` with public-interface scope, actual report commands and
review dispositions. Existing `ruff check`, `mypy` and `lint-imports` steps run added rules and
contracts; add maintained-link/example checks to `just check`. Review-based reports must be
resolved before merge even when no automated tool can prove their meaning.

For existing code, review findings into a baseline tied to a revision. Use narrowly scoped
suppressions only with a matching record naming reason, reviewer and review condition; do not
raise the global complexity limit to hide one function. Exercise an over-limit fixture and a
forbidden import to show the check fails, then remove them. Static unused-code reports cannot
prove a dynamically registered view or model unused; investigate instead of auto-removing.

During gardening, compare complexity, duplication and aging exceptions with the same scope
and tool versions; do not claim this draft mechanism is validated until it has run.

## Security verification (draft)

Generate actual pinned commands and report handling in the project's `docs/security.md` and
`just check`. For secrets, `gitleaks dir --redact .` includes working files and
`gitleaks git --redact .` covers the declared history scope; treat shallow-clone limitations explicitly.
Use safe fixtures, never real leaked tokens, to verify detection. Do not read prohibited files
or emit raw secret reports; report any access-related coverage gap.

For dependencies, export the complete reviewed pinned set from the lock, then use
`pip-audit --no-deps --disable-pip --strict -r <reviewed-export>`; record skipped or unsupported
coverage, including platform/build dependencies separately. `pip-audit` detects known package
vulnerabilities, not malicious packages or all native-library flaws. Its ordinary dependency
resolution can execute package code; never audit an untrusted manifest as a safety precheck
for installing it. Review sources first and use isolated, restricted build/audit jobs.

Run `manage.py check --deploy --fail-level WARNING --settings=config.settings.prod` with
isolated deployment-shaped configuration and test-only credentials. Test `DEBUG=False`, host
allowlists, required settings, session/CSRF controls and error/log redaction. An authorized
operator verifies real production settings and effective TLS/proxy and service permissions;
never bring production secrets into an agent session to satisfy this evidence. The command
does not verify all controls or prove the proxy or database is deployed safely.

Link redacted reports to revision, environment and time; keep current advisory evidence and
expiry-aware risk dispositions. No automatic `--fix`, blanket scanner suppression or
untrusted-contributor job with release credentials. All new SE mappings remain untrialled.

## Project-owned style

The existing Ruff recommendation is optional; retain a coherent Black or other project
policy unless a change is agreed. Pin the actual formatter/linter version in the lock/tool
environment. `ruff check .` and `ruff format --check .` do not rewrite source; reviewed safe
lint fixes precede `ruff format .`. A second full pass must make no changes.


## Gotchas

- `post_migrate` runs after every app migrates; permission sync that depends on content types
  must live there, not in a data migration.
- `ManifestStaticFilesStorage` fails at runtime on a missing file; prefer hashed query strings.
- `{% translate %}` output is not escaped: never put `<` or `&` in a translated literal.
- Tests run against a throwaway database; anything that reads a second database (outside
  sources) needs a fake in tests.
