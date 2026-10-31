# Profile: Django

- **Status:** Reference (used on a line-of-business platform). Items marked † are recommended
  here but were not yet running on that project; treat them as draft.
- **Applies to:** Python 3.12+, Django 5.2 LTS or later, PostgreSQL

## Baseline

| Concern | Tool | Why |
|---|---|---|
| Package manager and lock file | `uv` with committed `uv.lock` | Fast, one tool, reproducible installs |
| Formatter | `ruff format` | One style; agents never hand-format |
| Linter | `ruff check` with rules `E,F,W,I,B,UP,DJ,S,SIM,RUF,PT` | `S` (bandit) and `DJ` (Django) catch the common security and framework mistakes |
| Type checker | `mypy` with `django-stubs`, strict in the platform package | Types are the cheapest sensor an agent gets |
| Test runner | `pytest-django`, `factory_boy`, coverage floor | Fixtures as code; the floor is a smoke alarm, not a goal |
| End-to-end tests | `pytest-playwright` † | Drives the real pages (TS-5, SK-2) |
| Architecture checker | `import-linter` | Module boundaries as contracts (AR-3) |
| Framework checks | Django system checks (`manage.py check`) | The project's own invariants fail `check` with a hint (CK-4, AR-1, AR-2) |
| Migrations | `django-linear-migrations` | Two parallel migrations become a merge conflict, not a broken deploy |
| Task runner | `just` | Thin recipes over `uv run`; nothing requires it |
| Changelog | `towncrier` fragments | One file per change, no merge conflicts (WK-4) |
| Pre-commit | `pre-commit` with ruff, `makemigrations --check`, a secret scan | Fast checks before CI (CK-6) |

## The check command

```
just check
```

Runs `ruff check`, `ruff format --check`, `mypy`, `lint-imports`,
`manage.py check --fail-level WARNING`, `makemigrations --check --dry-run`, the instruction-file
check, then `pytest --cov`. CI runs the same recipe against a PostgreSQL service container.

## Rule mapping

| Rule | Mechanism |
|---|---|
| IN-3, IN-5 | `scripts/check_agent_docs.py`: line budgets, every nested `AGENTS.md` has a `CLAUDE.md` pointer; named paths exist † |
| CK-1 | `just check`, mirrored step for step in CI |
| CK-8 | Gitea or GitHub Actions running the check against a PostgreSQL service container, with branch protection. Until a runner exists, `just check-clean`: clones the committed branch to a temporary folder, `uv sync --locked`, runs the check with only `DATABASE_URL` passed through (partly met) |
| CK-4 | System checks raise `checks.Error(msg, hint=..., id="app.E0xx")`; the hint says how to fix it |
| CK-6 | `.claude/settings.json` PostToolUse hook runs ruff on each edited `.py`; pre-commit |
| GR-1 | Deny `Read(./.env)` and `Read(./.env.*)`; settings read with `django-environ`; agent sessions use a dev database and test credentials for outside sources † |
| GR-2 | `git commit`, `git push`, `manage.py migrate` in the `ask` list; force-push denied |
| GR-4 | † Stop hook (`start` templates) runs the check when the tree changed since its last green run |
| GR-6 | A base management command adds `--commit`; without it the command reports what it would do |
| SK-1 | `just bootstrap` writes `.env`, creates the database, migrates, creates an admin; `just doctor` reports problems with one fix each |
| SK-2 | † One Playwright test: sign in, open the landing page, see the module list |
| TS-4 | `AGENTS.md` rule, plus review flags new `skip`/`xfail` markers |
| TS-7 | The test-writing step runs `ruff` and `mypy` on its new tests; then `pytest` shows only the new acceptance tests failing |
| WK-6 | Each worktree's `.env` names its own database (`<project>_<branch>`), so pytest-django's `test_<name>` never collides between sessions; parallel sessions start in their own worktree |
| AR-1 | `LoginRequiredMiddleware` (Django 5.1+) on; every view either `@login_not_required` or carries an access mixin or decorator; a system check fails on a view with no declared rule, and a test resolves every URL and asserts it is protected |
| AR-2 | Modules subclass a `ModuleConfig(AppConfig)` with key, label, nav, URL prefix and access levels; settings, URLs, nav and permission groups are built from the registry; system checks catch duplicates and gaps |
| AR-3 | `import-linter` contracts: the platform never imports modules; a module imports another only through its `services` (writes) and `selectors` (reads) |
| AR-4 | Writes go through `services.py`, take an actor, and record a history row |
| AR-5 | Only the integrations package imports database drivers or outside clients (import contract); reads go through a cache so no request waits on a source |
| WK-4 | `towncrier create`; CI fails without a fragment unless labelled |
| OP-1 | An `@operation` decorator in `operations.py` declares name, level, read or write, and pydantic schemas; Django Ninja serves it as REST and a small view serves it as MCP tools |
| OP-2 | API tokens have module scopes, site limits and `can_write` off by default; stored hashed |
| OP-3 | The actor carries user, token and channel (`web`, `api`, `mcp`) into every history row |
| OP-4 | Write operations take an optional request ID, stored with the result; a repeat returns the stored result |
| OP-5 | Bearer header only; query-string tokens refused |
| OP-6 | † An ADR names the tools that act on text from outside data; those tools need a narrower token |
| OP-7 | † Definitions (labels, forms, screens) are drafted and saved through operations at `designer` level; publishing needs a person at that level, never a token |
| OP-8 | Each MCP or ODBC source has a request budget (a requests-per-minute setting), refused before sending when spent; reads go through the shared cache, so many viewers and agents cause one read |

## Gaps

| Rule | Why | Instead |
|---|---|---|
| Template rules (single-line `{# #}`, literal `{{`, `json_script` double-encoding) | Django does not lint templates; mistakes render silently | A small template linter in the check, or `djlint` plus custom rules |
| Translatable text | No check finds an untranslated literal reliably | Review checklist item; `makemessages` diff in CI shows new strings |

## Skeleton

`start` generates: `pyproject.toml` (uv, ruff, mypy, pytest, import-linter config),
`config/settings/{base,dev,test,prod}.py` reading the environment, a `core` app with one view
behind login, `justfile` (`bootstrap`, `doctor`, `check`, `test`, `fmt`, `run`), CI workflow,
pre-commit config, `changelog.d/`, the access test, one Playwright test, and the agent files.

## Gotchas

- `post_migrate` runs after every app migrates; permission sync that depends on content types
  must live there, not in a data migration.
- `ManifestStaticFilesStorage` fails at runtime on a missing file; prefer hashed query strings.
- `{% translate %}` output is not escaped: never put `<` or `&` in a translated literal.
- Tests run against a throwaway database; anything that reads a second database (outside
  sources) needs a fake in tests.
