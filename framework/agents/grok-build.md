# Host: Grok Build CLI (Draft integration)

Documentation checked 2026-11-01. Installed CLI reports 1.0.70 (f50904eaee6c), stable.
Native adapter fixtures and isolated offline discovery are exercised; actual model-driven
hook continuation, permissions and OS isolation remain pending. Record actual version,
platform, model/effort, trust and capability results in the [host record](../../templates/agent-host.md).
This recipe targets the coding CLI/TUI, not Grok's separate web/mobile Build Mode.

## Instructions, skills and plugins

Use root `AGENTS.md` as shared authority with concise scoped additions. Grok documents
root-to-working-directory loading and additional AGENTS/Claude/rules compatibility sources;
inspect actual discovered files, precedence and exclusions. Compatibility may duplicate or
import unintended instructions. Keep `CLAUDE.md` a pointer rather than a second policy.
Ignored instruction files can be skipped; no loading cap does not make long context reliable.

Use the intact kit's skill files directly or a reviewed native discovery path. Grok supports
`.grok/skills/`, enabled plugins' `skills/` and additional `[skills] paths` in its user layer.
Keep the kit's `framework/`, `templates/` and `skills/` relationships intact; copying only a
skill folder breaks relative resources. Use the native skills selector or `/assess`, `/spec`,
`/refactor`, `/route`, `/context`, etc. only after verifying discovery and name collisions.
Availability is not permission to invoke an excluded plugin or launch a model session.

Claude plugin compatibility can reuse `.claude-plugin/plugin.json`; no third manifest is
required here. A plugin's installation/load/trust must be verified in the selected version.
Do not assume the portable OpenAI manifest or `.codex/` config establishes Grok discovery.
The current upstream configuration guide calls most Codex compatibility cells inert.
Avoid loading local and plugin copies under duplicate names, and review imported hooks/MCPs.
This addition installs/enables no plugin or MCP and changes no personal configuration.

## Native setup recipe

1. Keep project commands and policy in `AGENTS.md`. Merge
   [grok-project.toml](../../templates/grok-project.toml) into `.grok/config.toml`. It supplies
   supplementary prompts for direct Git command text, not comprehensive action authorization.
   Review options before subcommands, aliases, wrappers, SDK/MCP routes and the actual
   deploy/migration commands. Do not broadly allow `git *` or all shell commands.
2. Review [user-layer fragments](../../templates/grok-user-config.toml) with the operator;
   they request ask mode, strict sandbox and no automatic `.envrc` loading. These settings
   are not established by project config. Do not copy them globally or replace stricter
   managed/user policy automatically. A session may select reviewed CLI controls such as
   `--permission-mode default --sandbox strict --no-subagents`; verify version/platform
   behavior. A sandbox profile name alone proves neither secret isolation nor network denial.
3. For clients with the newer Stop-gate contract, copy
   [grok_stop_check.py](../../templates/grok_stop_check.py) and shared
   [stop_check.py](../../templates/stop_check.py) together under `.grok/hooks/`. Put the
   reviewed project executable check command in `.agent-check`; inspect `AGENT_CHECK` overrides.
4. Copy [grok-hooks.json](../../templates/grok-hooks.json) to
   `.grok/hooks/agent804.json`; render the actual absolute checkout path and Python executable
   for each platform/worktree. The command must work from a subdirectory. Review existing
   native/Claude-compatible hooks to avoid duplicates. Do not enable plugin-wide hooks merely
   by adding this profile to the kit.
5. Inspect discovery using `grok inspect --json` (don't publish raw output with private config
   details). Review the project's trust surfaces before `/hooks-trust`; trust can cover MCP,
   LSP, project instructions and skills as well as hooks. Never turn trust off to make a
   report green. Managed-only policies can skip local/plugin/compatibility hooks.
6. Exercise the [capability checklist](README.md) in the actual session. Offline discovery
   proves neither permission refusal nor Stop dispatch/continuation. If unsupported or
   skipped, report the GR-4 gap; required CI and human review remain separate protections.

## Stop contract, version discrepancy and limits

The public hooks page (updated July 2026) describes Stop as passive. The newer official
repository guide explicitly describes Stop/SubagentStop blocking, exit 2 with stderr feedback,
and native camelCase inputs. Therefore this adapter is Draft against the newer contract;
don't infer the installed binary implements it from the website or latest branch alone.

It accepts a native Stop event (`hookEventName` of `stop` or `Stop`), uses `cwd` to discover
the checkout and tests `stopHookActive` for the reporting escape. It rejects a foreign
`stop_hook_active` flag rather than silently losing the retry bound. Success allows stopping;
check/validation errors exit 2 requesting continuation. An already-active continuation
allows an honest unresolved-failure report and does not report a passing check. It does not
register SubagentStop by default; subagent completion coverage remains a separate gap.

Upstream describes hook failures/timeouts as fail-open and a built-in continuation cap.
No adapter can make skipped dispatch, a timeout or that cap into fail-closed enforcement.
Exercise effective behavior; never claim GR-4 met solely from a configured file. Claude's
engine entry point alone reads the wrong active-flag spelling for this native protocol.

The shared engine preserves per-worktree private caches and Git/root discovery. Ignored
files, external services and time-dependent checks are outside the success key; refresh the
private `agent-stop-check` state when needed and run independent final/CI checks. Concurrent
writers still isolate mutable resources; native worktree creation does not isolate databases,
ports or credentials. Context compaction/forking alone is not independent acceptance/review.

## Permissions, routing and privacy

Separate action consent, tool permissions and actual OS/network isolation. An automatic
permission classifier is not human approval (GR-7). Supported sandbox enforcement is platform
dependent; current public docs distinguish child-process from in-process network access.
Verify Windows/Linux/macOS behavior rather than promising the same boundary everywhere.
Keep production credentials/data unavailable to the agent; native rules are supplementary.

For optional routing, verify account entitlement and the native `--model`/`--reasoning-effort`
settings. Do not hard-code a model, effort class, subscription allowance or API fallback.
Skill frontmatter such as `model`/`effort` is not a proven routing mechanism. Keep portable
frontmatter unchanged and use [routing guidance](../model-routing.md). Tools that read usage
or model catalogs may require network/account access; no such call is authorized by a recipe.
Use [context recovery](../context-management.md) and preserved artifacts across hosts.

## Sources

- [Overview](https://docs.x.ai/build/overview), [instructions](https://docs.x.ai/build/features/project-rules) and [skills/plugins](https://docs.x.ai/build/features/skills-plugins-marketplaces)
- [Public hooks reference](https://docs.x.ai/build/features/hooks)
- [Newer upstream hook contract](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/10-hooks.md)
- [Configuration scopes](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/05-configuration.md)
- [Permission rules](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/22-permissions-and-safety.md) and [sandbox limits](https://docs.x.ai/build/features/sandbox)
