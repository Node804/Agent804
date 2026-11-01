# Roadmap

**Status:** 0.4.0, preview, not yet released. What is proven and what is only an idea is in
the README's Evidence section; this page is what's next and why things are the way they are.

## Before the first public release

The first public release is the push to the public repository under Node 804, with a release
zip attached.

- [x] ChatGPT review of the 0.4 rewrites against 0.3 (2026-11-01); corrected the missing-interface
      test exception, stale gate/lifecycle summaries and conditional Security setup.
- [x] Independent Grok review of the 0.4 skill rewrites against 0.3; completed per the
      developer, with the follow-up Operate corrections checked on 2026-11-01.
- [ ] Build `agent804-0.4.0.zip` from the release commit.

## Trials before 1.0

Each is one session. Record the result in the README's Evidence section, and fix whatever the
trial shows is unclear before moving on.

- [ ] Install from the release zip on a clean machine, in Claude Code and in Codex, and run
      `assess` once from each. This remains a follow-up, not a blocker to publishing the repo.

- [ ] Run the change flow on a real feature with the kit's own current skills (`spec`, tests
      written in a separate context, build, `review`, `decide`), not a project's own playbooks.
- [ ] Trial the [testing workflow](framework/testing.md) on an application: red and green output
      in the plan, a bug regression, an empty suite failing the check, isolated tests, and a
      flaky test reported rather than retried into a pass.

- [ ] Trial Grok Build CLI with actual trusted project instructions/skills/permissions and
      passing/failing native Stop continuation, reporting escape, timeouts and worktrees.
      Reconcile the public/upstream hook-doc discrepancy for the tested client; verify actual
      OS/network isolation and keep web/mobile Build Mode separate from CLI capability claims.
- [ ] Trial MT-5 debt management: confirm/reject candidates, reuse scoped deferral, revisit
      overdue/triggered review, repay in authorized feature/refactor work and verify closure.
      Include partial repayment and renamed items; prove ticket creation does not waive a
      defect, unmet criterion, failing check or security acceptance requirement. Keep MT-5
      a reported practice until real adoption evidence supports a change.
- [ ] Trial scoped context and recovery on equivalent maintenance tasks: stale/current
      authority, cross-file constraints, superseding decisions, truncated evidence, dirty
      work missing from an index and insufficient evidence. Predefine expected outcomes;
      record missed contracts, actual recovery, unnecessary reads and overhead.
      IN-8/WK-8 remain practices; no extra model sessions are authorized by this checklist.
- [ ] Trial optional routing with one model/separate contexts, multiple classes in one family,
      and multiple providers where access/data/spend policy permits. Record native effort,
      shared/unknown/exhausted allowances, bounded escalation and adversarial input boundaries;
      compare equivalent accepted outcomes including retries/transfer/rework. Actual calls
      and paid trials require applicable authorization; WK-7/MS-5 remain conditional practices.
- [ ] Exercise host capability records and equivalent bug-fix/feature/refactor/review fixtures
      in Claude Code and Codex. Verify actual instruction discovery, nested overrides, intact
      relocated skill resources, hook trust/loading/failure continuation and missing-control
      reporting on the tested clients/OS; don't infer other surfaces from one CLI trial.
- [ ] Trial `refactor` on a scoped existing-code change: capture consumers/contracts and
      baseline, add immediately passing characterization tests where needed, restructure in
      small steps and verify final preservation/retirement. Exercise a hidden behavior-change
      case and an unknown consumer without claiming equivalence. MT-4 stays a practice.
- [ ] `start` on an empty repository, through to a green check and a walking skeleton.
- [ ] One small change end to end, to prove the light path really is light.
- [ ] The full flow under Codex: spec, separate test session, build, review, evidence. Work out
      Codex's equivalents for the stop hook and the commit/push/migrate approvals (GR-2 to GR-4).
- [ ] Exercise a non-Django Draft profile on a real application before considering Reference
      promotion; record its resolved mappings, bootstrap/check/CI, refusal evidence and gaps.
- [ ] Someone other than the author runs `assess` cold on their own repository.
- [ ] Run `sensor`, `garden`, `measure` and `operate` once each on a real project.
- [ ] Trial two concurrent worktrees with separate databases and ports, an explicit test
      handoff, combined-change verification and cleanup; exercise the strengthened retry
      contract and append evidence without editing an Accepted ADR.
- [ ] Reassess reference projects against the revised maintainability gates; trial the Django
      complexity and contract checks, gradual adoption baseline and retirement review.
- [ ] Trial SE-1 to SE-6 and revised reference-project scores: versioned requirement mapping,
      scanner detection/error/staleness, dependency trust and isolated builds, secure skeleton,
      abuse tests and expiry-aware human decisions.

## Known gaps

- Codex and Grok have Draft guardrail adapters and settings; actual-host enforcement remains unverified.
- Under Codex, skill names show without a prefix (`spec`, `start`), so they can clash with
  other skills.
- Items marked † in `framework/profiles/django.md` have not run on a real project.
- Django is the only stack profile. Others are written per project by `start` and join the
  kit after a real project has used them.
- The `operate` skill and OP-9 to OP-11 have not been trialed. A designed tool list and an
  embedded model feature are specified; no reference project has been graded against them.
- Not yet read, so not relied on: arc42 §10 and the SEI's quality attribute scenarios (the
  quality scenarios follow their form); StrongDM's "software factory" write-up; the DORA 2025 AI
  report; METR's 2025 developer productivity study.
- The scoring rules are sensitive to wording. Any change to `rungs.md` or a rule's Check column
  should be followed by a fresh `assess` run on the reference projects.

## Decisions so far, and why

- **Name: Agent804.** Ties to the Node 804 organisation. "Harness" names clash with Harness
  Inc.; "Node" reads as Node.js; "Factory" clashes with Factory.ai and "AI factory" hardware.
  The tagline, "build the harness before the app", says what it is.
- **Licence: MIT, with `templates/` under MIT No Attribution.** Templates are meant to be copied
  into other projects and edited, so they shouldn't carry a notice.
- **Credit: Node 804.** Copyright, manifests and the framework's origin name the organisation,
  not a person.
- **Voice: plain.** "I built this, then checked it against and reinforced it with these
  references." `framework/validation.md` records what each reference reinforced and why
  Agent804 chose differently where it did, without per-rule citations, academic framing or
  claims about going further. Agreement is never presented as origin.
- **Two plugin manifests.** `.claude-plugin/plugin.json` for Claude Code, root `plugin.json` for
  Codex; the check fails if they drift. Codex labels a privately added plugin with the account
  that added it, whatever the manifest says.
- **Scoring.** Build rungs 1–4 are strict and cumulative (the foundation); 5–8 are independent.
  A rule with a hole is "partly met" and leaves the rung "met with holes"; only a missing
  protection fails a rung. Operate (O1–O3) is scored the same way, separately. Earlier versions
  failed a rung on any partial rule and swung scores on trivia; three assessment rounds settled
  this form.
- **GR-1 judges what a credential allows, not whether it is production's.** A production
  credential in the agent's reach fails it, except a recorded development credential that
  is read-only, non-sensitive, rate-limited and separate from production's own; the
  alternative failed a project whose only data was production. Non-sensitive production
  data is a threat-model entry, not a failure. An example file's empty slot proves nothing.
- **No Approvals module.** Agent804 governs development: agents building for the developer
  directing them, and the AI-facing parts of a product (Operate). Project sign-off and audit
  are that developer's governance. Only the agent-specific part
  stays, in GR-7: approval is the person's own, and a material change needs them again.
- **Decisions, not one project's process.** ADRs record hard-to-reverse choices, accepted by
  a person, with evidence that only grows. Quality scenarios, delivery metrics, audit history
  in the write layer and a production-readiness status were one reference project's process
  or governance, and were dropped in 0.4.
- **Operate is development of the AI-facing surface.** MCP servers, APIs and tools for agents,
  and embedded model features are a primary goal, scored when the project builds them and
  left unscored when it does not. The `operate` skill and OP-9 to OP-11 (a designed tool
  list, embedded features, credentials issued for this server) are written and untrialled.
  OP-1, OP-4, OP-7 and OP-8 still describe one project's mechanisms and need a second
  implementation. The former AR-5 (outside systems reached from one place, never waited on
  during a request) remains a candidate for OP-8.

## Changing the framework

1. Read `AGENTS.md` and `framework/validation.md` before changing a rule.
2. Run `python scripts/check.py`.
3. For scoring or rule-wording changes, re-run `assess` on the reference projects with fresh
   agents that follow the playbook alone, and compare with the previous scores.
4. Add a line to `CHANGELOG.md`.
