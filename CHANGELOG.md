# Changelog

## 0.4.0 - Unreleased preview

- Version 0.4.0 in both plugin manifests. The README links the release zip on
  [GitHub](https://github.com/Node804/agent804/releases). The roadmap's release list is what
  actually remains: an independent review of the 0.4 skill rewrites, the release zip and a
  clean-machine install; publishing is the push itself.

- The README says what is proven and what is only an idea. Every skill and module carries one
  of four marks (Proven, Used once, Fixture-tested, Idea), and the Status section becomes
  Evidence, saying what each mark rests on. Only `assess` is proven; the change flow ran once,
  with the reference project's own playbooks, and the kit's current skill text has not yet
  run on a real feature.

- Fixes from the reassessment of both reference projects. `assess` no longer checks TS-11 at
  rung 4, counts git-ignored output from the check as testing, and takes actual-host
  evidence from records rather than launching sessions. A missing check is graded once, under
  its own rule, even when it runs elsewhere such as a pre-commit hook. Rung 5 judges work
  since adoption, dated from the commit that introduced the harness, instead of "two
  features". A not-verifiable rule counts as met, with the assumption named. TS-4 is not
  verifiable while no test can run. The Security trigger no longer fires on staff sign-in
  data alone; Parallel work names its evidence; Routing covers development only. IN-3 and CK-2
  apply to a tool-specific root file when there is no `AGENTS.md`; WK-1 counts per merged
  change; GR-7 notes that a co-author trailer does not show who decided; SK-1 says how a
  read-only assessment grades it. When several target rows apply, the most demanding one is used.

- Lighter where the goals need less. TS-12 asks the check to print test counts and fail on an
  empty suite; TS-10 asks for isolated, repeatable tests with flakes reported (owning them is
  `garden`'s job); TS-2 asks for red and green output in the plan or PR. TS-11 stops gating
  rung 4. SK-1 drops the second "doctor" command. DC-2 requires only Proposed, Accepted and
  Superseded; Validated and Rejected are optional. MS-4 (maintenance exercises) is removed
  until a project trials it, and so is `decide`'s procedure for moving evidence to files. The
  plan template goes from 89 lines to 34 and the pull request template from 54 to 34.

- Close gaps against the framework's goals. TS-4 (never weaken, skip or delete a test to get
  green) gates rung 5, and a changed expected outcome goes back to the person who agreed it.
  AR-6 (parse input at the boundary, encode output for each destination) gates rung 6.
  MT-2 limits file or module size, so a unit can be read whole within an agent's context, and
  duplicated code, as well as function complexity; the Django profile gains Draft mechanisms
  for both. MT-1 asks for a comment on non-obvious logic. ST-1 makes the language's standard
  style the default and asks a project that keeps another to record why.

- Cut what one reference project's process or governance had written as universal rules.
  AR-5 (outside systems never waited on during a request) leaves rung 6 and is noted for the
  Operate work in phase 2; AR-4 keeps "every write is validated in one place" and drops
  attribution and history. DC-5 (quality scenarios) and DC-4 (owners accept ADRs, now covered
  by GR-7) are removed, so rung 7 gates DC-1 to DC-3; quality scenarios stay optional in
  `decide` and `spec`, and their template is removed. MS-1 measures whether agent work holds
  (corrections, rework, escaped defects, test reliability) instead of delivery speed. The
  production-readiness status and the SE-6 response exercise are removed as governance.
  Examples from one project's domain are replaced.

- Remove the Approvals module (AP-1 to AP-4), its guide, record format, validator and twelve
  tests. Agent804 governs development, by agents and of a product's AI-facing parts; who
  signs off on a project, and how that is shown to others, is that developer's governance, which agents do
  not change. The agent-specific part moves into GR-7: approval comes from the person
  directing the work, and a material change after agreement needs them again. TS-1 and DC-4
  no longer require approval records; they point to the person's own agreement.

- Assessment fixes from the 0.4 round. `assess` scores only after every rule is graded. DC-2
  and DC-3 state the property (an append-only evidence record; decision text frozen once
  Accepted) instead of requiring `docs/evidence/`: an Evidence section that only grows meets
  them. A rule naming several mechanisms is partly met when some run; a missing piece is
  graded once, under its own rule, so CK-1 no longer double-counts. New guidance for tests
  that cannot run, a project with no check command, a profile covering part of the stack,
  and Operate levels above an unmet one.

- README "Use it" is rewritten in the order people need it: install per host in one table,
  the first run of `start` or `assess`, the steps of every change, and the periodic skills.
  It replaces "The loop, once set up". Host details stay in the host recipes. Install is from
  a release zip on GitHub until the kit is in a marketplace. "What is in it" marks which pages
  agents read and which are for people; "Status" is rewritten for 0.4 and drops claims about
  approval and security gates that are now modules. Stale rung numbers in three `rules.md`
  headings are corrected.

- The kit's own `AGENTS.md` is about working on the kit and says how a rule stays aligned:
  its row in `rules.md`, the instruction in the skill or template that sets it up, and the
  reason in the framework page change in one commit. The check now fails a rule no skill or
  template cites, and a gating rule only `assess` cites. Twenty rules had no such citation;
  `start`, `spec` and `review` now cite them where they set them up, and say what to do for
  the ones that had no instruction at all (CK-6, CK-8, GR-5, SK-4, TS-5, AR-4 to AR-6).

- Agents load instructions, not explanations. `framework/` stays the reference for people;
  skills no longer send agents to its guidance pages and say what to do themselves. `spec`
  now loads about 5k characters before work starts, down from about 52k with the pages it
  pointed at; `review` about 4k, down from 57k. The `AGENTS.md` template every project loads
  each session goes from 6.4k characters to 2.1k: module lines are added by `start` only when
  a module applies, and its guidance for people moves into `start`. The check fails a skill
  that links a guidance page, a skill over its size budget, or HTML comments in the template.

- GR-1 judges what a credential allows. When production is the only source to develop
  against, a development credential passes if a person decided it in writing and it is
  read-only and non-sensitive by the source's own limits, rate-limited and separate from
  production's own. Credentials and data are graded separately; non-sensitive production
  data is a threat-model entry. `security.md` no longer contradicts the rule, and the
  security template records the exception.
- `assess` never writes a guess as a finding: a grade that depends on something it cannot
  see is not verifiable, with the question that settles it. An example file's empty slot
  shows a setting exists, not that it is set.
- Add GR-7 to the core, gating rung 3: agents cannot supply consent. An approved plan, a tool
  permission, a passing check or an agent-filled record is not approval. AP-2 keeps only the
  provenance of recorded decisions; the rest of Approvals stays a module.
- Add the ownership boundary to `AGENTS.md`: Agent804 owns what coding agents change, and
  links established standards for the rest.
- Cut technical debt to what agents change (they create debt faster, invent candidates,
  expand scope, and must not defer debt themselves); tracking itself is left to the project.
  The guide goes from 124 lines to 29 and the template to one short item.
- Cut security to what agents change, linking OWASP ASVS, NIST SSDF and OWASP SAMM for the
  rest. SE-1 to SE-6 are reworded plainly; the guide goes from 160 lines to 78.
- Rewrite model routing around quality: capability matched to judgement, review by a
  different model where available, and allowances planned so review and the final check are
  never the steps cut. Roles map to capability tiers, never model names. WK-7 and MS-5 are
  reworded; the guide, `route` skill and template are rewritten.

- The check fails when a file names a private project, organisation or person listed in the
  git-ignored `private-names.local.md`; the kit refers to "a reference project" instead.

- Split the framework into a core and modules. The eight rungs are the core (69 rules, 39 of
  them gating). Modules apply only when their trigger is true and are listed in the new
  `framework/modules.md`: Operate (OP-1 to OP-8), Security (SE-1, SE-4 to SE-6), Approvals
  (AP-1 to AP-4) and Parallel work (WK-6) are scored; Maintenance (MT-4, MT-5), Context
  (IN-8, WK-8) and Routing (WK-7, MS-5) are trial modules, reported without a mark until a
  real project has used them. Rule IDs are unchanged.
- Rungs 3 to 5 no longer gate on AP-1 to AP-4, SE-1, SE-4, SE-5 or SE-6. SE-2 and SE-3 stay
  core. Operate levels and production readiness move from `rungs.md` to `modules.md`.
- `assess` decides which modules apply before scoring and reports a modules line; `start`
  asks the triggers in its interview and sets up module mechanisms only when they apply.

- Remove the eleven Draft stack profiles (Python, PHP, Laravel, JS/TS, .NET, WPF, WinForms,
  Go, Rust, PowerShell, Bash). None had run on a real project. Django stays as the one
  profile; `start` writes a Draft profile per project from the template, and a profile joins
  the kit only after a real project has used it.
- Reduce style to one rule, ST-1: a pinned formatter and linter per language, run by the
  check without rewriting files, with a separate fix command. ST-2's check folds into ST-1;
  ST-3 is dropped. Remove `framework/style.md`, `framework/recommendations/` and the
  per-language starters; keep `templates/editorconfig` and `templates/gitattributes`.

## 0.3.0 - Unreleased preview

Version prepared 2026-11-01; not published. This revision changes assessment gates as well
as adding workflows; earlier project scores need reassessment under the current rules.
Application trials and adoption limits remain documented in README and validation records.

- Add Draft Grok Build CLI support: native host recipe, project/user config starters and a
  camelCase Stop adapter using the shared check engine. Cover thirteen wire/Git/worktree
  cases; isolated CLI inspection discovers twelve skills without a model call. Record public
  versus upstream hook-doc differences, untrusted-project skips and pending live enforcement.

- Rework README navigation around the five development goals and supporting workflows,
  including host/stack distinctions, optional routing, context recovery, refactoring and
  debt management. Add starting paths, complete template links and current regression-suite
  evidence while preserving explicit application-trial limits.

- Add technical-debt lifecycle guidance and a lightweight canonical-record template. MT-5
  covers confirmed consequences, ownership, scoped deferral/review and verified closure as
  a practice, not a rung gate. Link specialist exceptions/security/test records without waivers.
- Update existing assessment, setup, spec, gardening, refactor, review and measurement skills,
  plus instructions/plans/PRs. Preserve debt identity through moves/partial repayment; application
  trials remain pending. No separate debt skill or tracker integration is added.

- Add context-management guidance and optional `context` skill for scoped retrieval,
  source/freshness, incomplete output, durable working state and post-compaction recovery.
  Add IN-8/WK-8 as reported practices, clarify navigation/freshness and reuse MS-4 trials.
- Update skills, plans, instructions and host/model handoffs. Record research/task/model
  limits separately in `framework/validation/context.md`; retrieval/recovery trials remain
  pending. No mandatory index, universal token threshold or attention-internals claim.

- Add optional model-routing guidance, policy/inventory template and recommend-only `route`
  skill. Support single-model contexts, multiple classes/families, native effort, verified
  access and separate subscription/API budgets with bounded escalation and no silent spend.
- Add WK-7/MS-5 as conditional practices, not rung gates; define independent adversarial
  test/code/review roles and quality-adjusted usage evidence. Update planning, setup,
  assessment, review, measurement and instructions. Real routing/savings trials remain pending.

- Add host profiles separate from language profiles, a capability record/checklist and
  explicit context handoffs. Setup selects Claude/Codex/other mechanisms; assessment reports
  effective instruction/override, permission, trust and execution gaps. Qualify completion
  claims and keep automatic tool permission distinct from human design/merge approval.
- Add a Draft Codex Stop adapter using the shared check engine, config/hook/command-rule
  starters, thirteen wire/Git/worktree regressions and two relocated-resource checks. Native
  hook loading, trust, timeouts and full cross-host application trials remain pending.

- Add the portable `refactor` skill and MT-4 verified refactoring as a reported practice,
  not a rung gate. Require a concrete maintenance problem, consumer/contract analysis,
  baseline/characterization evidence, small transformations and honest preservation limits.
  Update assessment, gardening, specification, review, instructions and plan/PR guidance;
  behavior changes retain existing TDD/approval requirements. Application trials remain pending.

- Audit the five domains across documentation and agent entry points: complete README
  testing navigation, root guidance, generated-project README/instructions, human merge
  review and acceptance-context requirements; strengthen sensor/operate/decision handoffs.

- Add testing guidance and TS-8 to TS-13: independent assertions, bug regressions, isolated
  reliable tests, actual integration, complete discovery/results and optional sensitivity trials.
  Gate TS-10/TS-12 at rung 2, TS-11 at rung 4 and TS-8/TS-9 where applicable at rung 5.
- Require actual red/green execution evidence; supersede the historical tests-only-commit
  claim below. Clarify expected missing-interface diagnostics, reviewed test corrections,
  separate acceptance contexts and intentional red handoffs versus green feature completion.
  Update plans/PRs, skills, Draft runner mappings and reliability measures; app trials pending.

- Add AP-1 to AP-4 for identified human decisions, trusted-source/authority evidence, valid
  scoped reuse and requirement trace. Gate AP-1 to AP-3 at rung 3, AP-4 at rung 5 and RV-1
  at rung 4; strengthen owner ADR acceptance without reopening frozen decisions.
- Add approval policy/record templates and a portable mechanical validator for snapshots,
  selected-record freshness, dependencies, revocation, conditions and expiry. Structural
  success explicitly does not authenticate humans or authorize actions; source/host adapters
  and permitted administrative-transition handling still need project integration/trials.
- Add twelve mechanical approval regression tests and AP reference recognition. Update setup,
  specs, decisions, review, assessment, gardening, templates and shared profile mappings.

- Separate optional shared recommendations from stack profiles; move the style catalog to
  `framework/recommendations/` while leaving reusable assets in `templates/style/`.
- Add eleven Draft profiles: Python, PHP, Laravel, JS/TS, .NET, WPF, WinForms, Go, Rust,
  PowerShell and Bash. Laravel extends PHP; WPF/WinForms extend .NET. Shared baseline mappings
  and explicit overrides avoid duplicating common requirements or implying inherited evidence.
- Publish a support matrix distinguishing starter assets, draft guidance and actual reference
  evidence; update setup/assessment/sensor selection and remove the stale Django-only claim.
  No draft profile has been promoted or trialled on a complete application.

- Add ST-1 to ST-3 at rung 2: project-owned conventions, stable non-mutating check/fix
  enforcement and controlled exceptions/upgrades/migrations. Existing or custom styles take
  precedence over framework defaults; no new rung or skill is introduced.
- Add optional draft style recommendations and editable starters for Python, PHP, Laravel
  (including Blade), JS/TS, PowerShell, C#, WPF XAML, WinForms, Go, Rust and Bash, plus shared
  editor/text policies. Include explicit diagnostic-exit handling and generated-code caveats.
- Update profiles, setup/review/assessment/gardening guidance and templates. Recognize ST rule
  references and parse starter TOML, XML and XAML Styler JSON in the check (Python 3.11+).
  Full application/designer and reference-score trials remain outstanding.

- Add SE-1 to SE-6 for threats and versioned requirements, complete/current verification,
  dependency/build trust, safe runtime defaults, abuse-test evidence and accountable response.
  Gate rungs 2 to 5 and report production readiness separately from Build/Operate scores.
- Add security guidance and a project record template, scoped expiring human risk acceptance,
  safe response exercises and draft Django tooling mappings. Security debt is not accepted
  through a maintainability baseline; missing/stale verification cannot be called clean.
- Strengthen development data isolation, effective object/tenant authorization, safe input
  interpretation/output and agent-tool authority evidence. Zone security tests, policy and
  CI/approval controls by consequences, with explicit human review of changes.
- Update setup/spec/review/assessment/operate/gardening/measurement guidance, templates and
  reference validation. Check SE rule references; real-project security trials remain pending.

- Add MT-1 (understandable contracts), MT-2 (controlled complexity) and MT-3 (complete
  retirement), gating rungs 4, 2 and 6 respectively. Broaden rung 6 to architecture and
  maintainability, strengthen navigation/references, reuse/boundaries, dependency choices and
  red/green/refactor, and add MS-4 maintenance exercises as a practice pending trial.
- Add maintainability guidance and a project record template for actual limits, review
  triggers, scoped adoption baselines and exceptions. Update setup, assessment, review,
  gardening and measurement playbooks and draft Django mappings; reference-project scoring
  and end-to-end adoption trials remain outstanding.
- Validate MT references in skills, templates and framework pages through the repository check.

- Fix the stop hook for linked worktrees and subdirectories, keep cache state private to each
  checkout, invalidate it when the check command changes, and block on discovery or execution
  errors. Disable caching before the first commit so staged edits cannot bypass the check.
- Run behavioral hook regressions in `python scripts/check.py`; compilation alone is insufficient.
- Check the working branch independently of Git initialization during project setup.
- Define retry safety for concurrent requests, changed input, authorization, expiry, crash
  recovery and unknown external effects; machine request IDs are required in the Django profile.
- Store append-only decision evidence in `docs/evidence/`; Accepted ADRs stay frozen and are
  never automatically downgraded when later features exercise them.
- Add a worktree lifecycle covering checkout creation, resource isolation, explicit handoffs,
  integration checks and cleanup, with setup, plan and profile guidance.

## 0.2.0 - 2026-10-31

From three assessment rounds on two repositories and one full-flow feature trial.

### Added
- Tested: the plugin installs in Codex (ChatGPT desktop) from the same package, and `assess`
  runs there as designed.
- A Codex manifest (root `plugin.json`) beside the Claude Code one, so Codex shows Node 804 as
  the publisher; the check keeps the two in step.
- **Validation** (`framework/validation.md`) replaces the sources page: how Agent804 was
  checked against published practice, what each reference reinforced, and why it chose
  differently where it did.
  Rules no longer carry per-rule source codes.
- **Operate**, the framework's second half: how agents *use* the built system. Levels O1 (one
  contract), O2 (safe by default) and O3 (bounded) over the OP rules, scored like the rungs;
  `start` asks whether agents will use the system; `assess` reports the level; the `operate`
  skill is organised by level. New rule OP-8: load on outside systems is budgeted.
- Licensed: MIT, with `templates/` under MIT No Attribution so they can be copied into any
  project without a notice.
- Renamed from Agent Factory to **Agent804**; commands are now `/agent804:<skill>`.
- Authorship stated plainly: the framework comes from Node 804's own experience building
  agentic apps, later compared with published practice.
- **Quality scenarios (DC-5)**: system-wide requirements as measurable scenarios with stable
  `QS-n` IDs, above ADRs and specs. `templates/quality-scenarios.md`; specs and ADRs cite them;
  `decide` explains the three layers; `start` seeds the first scenarios.
- **TS-7**: acceptance tests pass the project's own lint and type checks before handover, so the
  only failures are the intended ones.
- **WK-6**: parallel agent sessions each get their own worktree and test database.
- **CK-8**: the check runs from committed state in a clean environment before a merge; CI is the
  standard mechanism, a clean-clone script counts as partly met.
- `spec` offers a tests-only commit (the only evidence for TS-2) and ends by recording evidence.

### Changed
- **Scoring**: foundation (rungs 1-4, strict) plus a coverage line, with each rung met, met with
  holes, started or absent. A partly met rule is a hole to close, not a missing rung. Rungs 5-8
  are independent practices.
- Rung 5 counts features since the workflow was adopted, at least two.
- **GR-1** judges impact: production secrets within the agent's reach fail it; production
  reachable with no credential at all is an outside risk, not a failure. Never infer a secret
  from a placeholder.
- Gating rules are listed per rung; any file over the instruction budget fails IN-3; several
  checks gained explicit partly-met wording (CK-1, CK-2, GR-2 to GR-4, TS-2, WK-1, AR-3, RV-1).
- `assess` reads `.env.example`, counts uncommitted work, ignores personal settings, and states
  assumptions when it cannot verify something.

## 0.1.0 - 2026-10-31

First version: rungs, rules with sources, Django profile, templates, nine skills, plugin
manifest and self-check.
