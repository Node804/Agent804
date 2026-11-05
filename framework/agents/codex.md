# Host: Codex (Draft integration)

Documentation checked 2026-11-03. The [Desktop completion trial](../validation/codex-desktop.md) failed:
automatic continuation did not occur despite the approaches tried. The Codex completion
integration has been removed; historical fixture/discovery results do not prove it worked.
Record the actual client,
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

## Setup and verification

1. Merge [codex-config.toml](../../templates/codex-config.toml) into `.codex/config.toml`.
   It requests workspace-write, interactive on-request approvals and command network off.
   Inspect effective managed/user/project settings and platform restrictions; do not weaken
   them or overwrite unrelated settings. Noninteractive runs need a separately bounded policy.
2. Optionally adapt [command rules](../../templates/codex-agent804.rules) into the active
   layer's `rules/` directory. Direct Git prompts are supplementary outside-sandbox controls,
   not comprehensive authorization enforcement. Review aliases, options, shell wrappers,
   SDK/MCP routes and project deploy/migration commands; preserve valid scoped consent.
3. Run the project's declared check directly against the current changed state and report
   actual commands, scope and results (GR-4). Required CI runs independently (CK-8).
   Missing or failed checks remain incomplete; no automatic continuation is assumed.
4. Exercise applicable action controls and instruction/skill discovery using the
   [capability checklist](README.md). Record unavailable facilities and evidence limits.

## Completion automation removed

The tested Codex Desktop session did not automatically continue after Stop attempts; none
of the approaches tried enabled it. The failure cause remains unresolved. Adapter fixture
passes and separate-process discovery/trust did not establish working host continuation.

Agent804 0.6 removes the Codex Stop adapter, hook configuration and enabling flag. Do not
install a completion handler or start another trust/restart troubleshooting loop as part of
Codex setup. Automatic continuation is unavailable for reliance in the tested environment;
GR-8 has no supplied Codex integration. Direct checks, CI and human review remain the path.
The [failed-trial record](../validation/codex-desktop.md) preserves historical evidence.
Removing these kit files does not remove handlers already installed in another project.

Sandbox permission or Auto-review is a tool decision, not human approval (GR-7). Verify
effective action controls, source/authority and conditions separately. Network-off for shell
commands is not a blanket statement about browser/MCP tools or their credentials.

## Sources

- [Instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Skills](https://learn.chatgpt.com/docs/build-skills)
- [Hooks and trust](https://learn.chatgpt.com/docs/hooks)
- [Configuration](https://learn.chatgpt.com/docs/config-file/config-reference)
- [Command rules and their scope](https://learn.chatgpt.com/docs/agent-configuration/rules)
- [Portable plugin layout](https://developers.openai.com/plugins/build/plugins)
