# Host: ChatGPT or a custom API harness (Draft)

Use [capability evidence](README.md), not the product/model name, to choose a workflow.
Core GR-4 requires truthful verification, not a stop hook. Optional end-of-turn automation
belongs to the Completion automation Trial module (GR-8); unsupported hooks alone cannot
lower the core level. See the [setup playbook](completion.md) if the developer opts in.
ChatGPT, Codex and API integrations may expose different repository, execution and approval
surfaces. This page does not establish automatic local instruction discovery for every chat.

## Choose the actual capabilities

- With supplied documents only: review/design/specify against the supplied revision, state
  missing context and produce reviewable proposals. Mark commands and tests unexecuted;
  do not invent repository access, a patched working tree, CI results or blocking hooks.
- With repository/tools available: inspect the provided root and actual instructions, use
  the project's check and select the host's real execution/permission mechanisms. If the
  environment is Codex, use [codex.md](codex.md); do not transplant Claude settings.
- With a custom API harness: its author must explicitly supply instructions/resources,
  implement tool boundaries, sandboxing, approval routing, durable handoff and check/result
  enforcement. API model access alone installs none of this framework's local adapters.

Skills can be distributed through supported plugins, but availability does not establish
filesystem or shell access. Confirm actual invocation and bundled resource retrieval. For
manually supplied playbooks, preserve their framework/templates or provide resolvable
equivalents; mark unavailable references rather than guessing their content.

Keep decisions, criteria, plans and evidence in durable project artifacts when a write
surface exists, or provide exact proposed artifact text otherwise. A chat summary or memory
is not source approval or test evidence. Use separate contexts for acceptance authorship and
review; verify input boundaries. No requirement for a particular subagent API or UI command.

Passing local checks cannot establish remote deployment readiness. Host automatic permission
review cannot replace required human architecture/criteria/merge review. Report missing
enforcement explicitly and never claim a fully exercised core level from document access.

## Sources and limits

[Official skills documentation](https://learn.chatgpt.com/docs/build-skills) describes
reusable workflow packaging across ChatGPT and Codex. It does not guarantee a particular
chat's tools or repository access. The API harness checklist above is Agent804's proposed
integration contract, not a claim that all API products implement it. No custom API or
chat-only application workflow has been trialled under this Draft profile.
