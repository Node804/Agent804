# Host: Grok Build CLI (Draft integration)

Documentation checked 2026-11-01. Installed CLI reports 1.0.70 (f50904eaee6c), stable.
Historical adapter fixtures and isolated offline discovery were exercised. The Stop adapter
is withdrawn in 0.6; actual permissions and OS isolation remain pending. Record actual version,
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

Use direct checks and independent CI for GR-4/CK-8. The supplied Stop adapter is withdrawn
in 0.6 with the shared engine's known cache/input/process-bound limitations. GR-8 remains
an opt-in Trial design; [completion criteria](completion.md) establish no shipped integration.

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
3. Exercise instruction/skill discovery and applicable action controls using the
   [capability checklist](README.md). Inspect effective configuration and trust in the actual
   session; offline discovery proves neither action refusal nor OS isolation. Trust may cover
   instructions, skills, MCP and LSP. Never bypass it to make an assessment green.
4. Run the project's declared check directly and report current state/scope/results.
   No Stop handler or automatic continuation is supplied. Existing installed handlers and
   diagnostics need separately authorized review; changing this kit does not uninstall them.

## Historical Stop evidence

The [trial record](../validation/grok-build.md) retains the public/upstream contract
discrepancy and fixture/discovery results. They did not establish live continuation.
The withdrawn shared engine also had dirty-gitlink cache reuse, EOF-dependent input and
unbounded child execution; fixture success did not make those behaviors reliable.
No subagent completion coverage is supplied. Worktree/resource isolation and independent
acceptance/review contexts remain required where applicable.

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
