# Host: Codex (Draft integration)

Documentation checked 2026-10-31. Adapter fixtures are exercised; live hook loading, trust,
continuation and complete application workflows remain pending. Record the actual client,
version, model, platform and execution mode in the [host record](../../templates/agent-host.md).
An installed CLI or a historical plugin assessment does not validate every Codex surface.

## Instructions and skills

Use root `AGENTS.md` as shared policy with concise scoped additions. Codex discovers global
and root-to-working-directory guidance, selecting `AGENTS.override.md` before `AGENTS.md`
within a directory; closer guidance takes precedence. Inspect effective overrides and
conflicts without changing personal instructions. Its combined `project_doc_max_bytes`
limit defaults to 32 KiB; framework line budgets do not establish loading completeness.
Host/system/developer policy still governs; repository prose cannot override enforced policy.

Prefer a reviewed plugin installation or preserve the full kit for local invocation. Codex
discovers `.agents/skills` folders and supports linked skill folders. Link to the original
`skills/<name>` in the intact kit and resolve references from the real skill location; verify
this in the actual client. Copying a lone `SKILL.md` or flattening a skill breaks its relative
`../../framework/` and `../../templates/` dependencies. Avoid duplicate plugin/local names.
For direct CLI/IDE invocation use `$assess`, `$spec`, `$refactor` or `$review` after discovery;
otherwise ask the agent to follow the actual file. ChatGPT selectors use their available UI.
Optional `agents/openai.yaml` presentation/policy metadata is separate from portable skill
frontmatter; it is not required to run these playbooks. No tool dependency is invented.

## Draft setup recipe

1. Merge [codex-config.toml](../../templates/codex-config.toml) into `.codex/config.toml`.
   It requests workspace-write, interactive on-request approvals, command network off and
   hooks enabled. Inspect effective managed/user/project settings and platform restrictions;
   do not weaken them or overwrite unrelated settings. Noninteractive runs need a separately
   bounded policy; this starter is not a headless configuration.
2. Copy [codex_stop_check.py](../../templates/codex_stop_check.py) and the shared engine
   [stop_check.py](../../templates/stop_check.py) beside each other in `.codex/hooks/`.
   Put the reviewed project check invocation in `.agent-check` (one executable command,
   no shell chaining). `AGENT_CHECK` may override it; inspect the effective value.
3. Merge [codex-hooks.json](../../templates/codex-hooks.json) into `.codex/hooks.json`.
   Replace BOTH absolute checkout path placeholders and select actual Python executables.
   The command must locate the installed adapter even when started in a subdirectory.
   Bootstrap must render per-checkout paths; never retain another worktree's path. An
   unrendered starter is deliberately not an installed working control. Avoid duplicate
   hooks from inline config, user layers or plugins. Never enable this kit's hook globally
   as a side effect of adopting one project.
4. Review/trust the exact hook definition and project layer in the client (`/hooks` where
   available). Changed hook definitions may be skipped until reviewed again. Do not bypass
   trust to make an adoption report green. Some orchestration modes do not load local hooks;
   record that gap and use supported managed controls only with applicable authority.
5. Optionally adapt [command rules](../../templates/codex-agent804.rules) into the active
   layer's `rules/` directory. Direct Git prompts are supplementary outside-sandbox controls,
   not comprehensive authorization enforcement. Review aliases, options, shell wrappers,
   SDK/MCP routes and project deploy/migration commands; preserve valid scoped consent.
6. Exercise the [capability checklist](README.md) in the actual host with safe fixtures.
   A script's exit status alone proves neither host discovery nor actual continuation.

## Stop adapter contract and limits

The adapter validates a `Stop` object and uses event `cwd`, ignoring `CLAUDE_PROJECT_DIR`.
Success emits `{}` with exit 0; failures exit 2 with a stderr reason requesting continuation.
After `stop_hook_active`, it allows reporting with an explicit unverified-result message,
not a passing result. This bounds retry loops. Intentional red handoffs must report their
stage and unresolved check truthfully; they do not complete a feature.

The shared engine discovers Git roots/private metadata, so linked worktree caches remain
private. It caches successful tracked/untracked content and command after the first commit;
ignored configuration, external services and time-dependent scans are outside that key.
Delete the private `agent-stop-check` state to force refresh; final/CI verification runs the
full check independently. Configure a realistic hook timeout and exercise failures/timeouts;
do not assume a host-level error or skipped hook blocks completion. The script cannot revoke
tools, prevent a merge or authenticate consent; required CI and human review remain separate.

Sandbox permission or Auto-review is a tool decision, not AP/RV human approval. Verify
effective action controls, source/authority and conditions separately. Network-off for shell
commands is not a blanket statement about browser/MCP tools or their credentials.

## Sources

- [Instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Skills](https://learn.chatgpt.com/docs/build-skills)
- [Hooks and trust](https://learn.chatgpt.com/docs/hooks)
- [Configuration](https://learn.chatgpt.com/docs/config-file/config-reference)
- [Command rules and their scope](https://learn.chatgpt.com/docs/agent-configuration/rules)
- [Portable plugin layout](https://developers.openai.com/plugins/build/plugins)
