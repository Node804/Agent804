# Profile: Python

- **Status:** Draft; no full application trial. All mechanisms below are proposals.
- **Applies to:** General Python CLI/library/service projects using a supported pinned CPython.
- **Inherits:** [Shared baseline](README.md#shared-baseline). For Django use [django.md](django.md).

## Baseline

| Concern | Proposed mechanism |
|---|---|
| Dependencies | `uv`, committed `uv.lock`, reviewed package/build sources and pinned Python |
| Style and types | Project choice; offer Ruff and strict `mypy` for owned code; include tests |
| Tests | `pytest`, isolated temporary resources and subprocess/HTTP acceptance tests |
| Architecture | `import-linter` contracts plus registry/AST structural tests |
| Security | Ruff security rules, secret scan, reviewed locked-set dependency audit and deployment-specific checks |
| Task entry points | Generated Python check/bootstrap/doctor scripts; changelog entry validation |

## Check, bootstrap and skeleton

Generate `scripts/check.py` in the adopting project; run it with `uv run python scripts/check.py`.
It propagates failures from Ruff lint/format-check, mypy, import contracts, documentation and
structural checks, current security verification and pytest. No source-format fixes run here.
Generate rerunnable bootstrap using `uv sync --locked` against reviewed dependencies and
test/dev configuration; doctor reports the missing input/tool with its fix. Installation
itself is not proof the app boots. Add `uv run python -m <package>` or the chosen service's
run command, a real acceptance test, CI and the agent/security/maintainability records.

## Rule mapping beyond the shared baseline

| Rules | Mechanism to generate |
|---|---|
| ST-1 to ST-3 | Merge [Python starter](../../templates/style/python/ruff.toml), retain stronger checks, pin tools and prove the full fix chain converges |
| SK-1, SK-2 | Bootstrap/doctor plus one subprocess CLI or actual service acceptance test in CI; a pure helper test does not prove an app boots |
| MT-1, IN-5 | Public docstrings, argparse/help or schema contracts, maintained-link checks and executable examples |
| MT-2, MT-3 | Ruff complexity limit selected/recorded before adoption, reviewed size/duplication reports and unused/import candidates; investigate dynamic imports before removal |
| AR-1, AR-2 | One operation declaration with access, actor and input/output contract; discover actual entry points and fail on undeclared dispatch; acceptance tests exercise effective permissions |
| AR-3 | Import contracts expose only declared module interfaces; test forbidden imports/cycles |
| AR-4, AR-5, AR-6 | Actor-aware service writes with history, isolated integration clients, safe parsing/query/command/output handling and fake outside systems in tests |
| SE-2 to SE-5 | Complete reviewed dependency/build inputs, current secret/static/dependency reports, safe config and abuse tests for actual CLI/service boundaries |
| WK-6 | Unique checkout ID for database/temp storage/ports/queues; no test opens a developer's real database by default |
| OP-1 to OP-8 | If exposed as tools/API, adapters call the operation registry; add credential, attribution, duplicate, untrusted-data and load-budget tests |

## Testing evidence (draft)

Apply [testing guidance](../testing.md) (TS-7 to TS-12); exercise this mapping before claiming it met.
Record selected test paths and collection/execution counts; reject missing expected suites.
Use isolated fixtures and controlled clocks/seeds; exercise real persistence and installed CLI
or HTTP boundaries. Report marks, skips, retries and unavailable runtime/platform coverage.

## Gaps to resolve before scoring

Select the actual service framework, persistence, access model and deployment controls.
Generic Python introspection cannot prove all dynamically loaded entry points covered; add
framework discovery/tests and list remaining gaps. Choose real complexity/report commands,
feed freshness and check integration. Tool-specific approval/stop enforcement and host merge
protection need evidence. Libraries without a running service use an installed-consumer
acceptance scenario, not an invented server. No draft command is a claim that it ran here.

## Gotchas and sources

Importing modules or running build backends can execute code; review before installation or
discovery. A mocked integration passing is not production compatibility evidence. Confirm
supported interpreter/platform combinations and throwaway-resource cleanup.

- [pytest documentation](https://docs.pytest.org/en/stable/)
- [Shared style recommendations](../recommendations/style-defaults.md)
