---
name: assess
description: Audit a repository against Agent804 levels, rules and triggered modules, with evidence and one bounded next action. Read-only; adopt implements protections and start handles empty projects.
---

# Assess a repository

Read-only: never edit, install, commit, change trust/policy or launch host/model sessions.
Report the level supported by actual evidence; assessment is not a prerequisite to adoption.

**Resources:** Claude Code `${CLAUDE_PLUGIN_ROOT}/framework/`; other agents `../../framework/`
from this file. For guided implementation use `adopt`: Claude Code
`${CLAUDE_PLUGIN_ROOT}/skills/adopt/SKILL.md`; otherwise `../adopt/SKILL.md`. Do not invoke it
or create an adoption record during assessment.

## 1. Establish scope and load authorities

- Identify the checkout, revision/dirty inputs, impact and prototype/production status.
  Use the target questions in `framework/levels.md`; reuse known answers. Ask what is missing;
  if nobody can answer, state assumptions from the brief. Do not turn assumptions into facts.
- Read `levels.md`, `modules.md` and `rules.md`. These own scoring, triggers and grading.
  A full assessment covers all core practices and every module trigger. Work through rule
  families in sections if needed; keep a coverage list so staged reads omit no required rule.
  Above-target gates may remain **not assessed (above target)**; examined strengths still count.
- Identify the stack from manifests/lock files. Read only its applicable profile and
  `profiles/README.md` where mappings are missing. Use partial profiles only for their scope;
  otherwise grade the property in the rule's Check column. Draft mechanisms are not optional.
- Read project instructions, nested/override sources, agent settings and relevant records.
  Include tool-specific sources actually used by the selected host. Inspect `.env.example`
  and comments without reading restricted secrets; an empty slot proves neither set nor unset.
  Repository-held uncommitted protections count, identified as such; personal ignored settings
  do not protect another developer.

## 2. Inspect the selected host and run safe checks

Read the shared capability checklist, Claude Code
`${CLAUDE_PLUGIN_ROOT}/framework/agents/README.md`, otherwise
`../../framework/agents/README.md`, then only the selected host profile. Inspect actual
client/version, overrides/loading limits, skill/resource resolution and effective action
controls. Use existing host records, CI/logs and authorized session evidence. Distinguish
configured, fixture-tested and exercised behavior; missing records remain unverified.

Load completion guidance only for opted-in GR-8: Claude Code
`${CLAUDE_PLUGIN_ROOT}/framework/agents/completion.md`, otherwise
`../../framework/agents/completion.md`. Inspect runtime/bootstrap and correlated lifecycle
evidence without installing anything. No Stop adapter ships in 0.6; do not retry withdrawn
setup. Other host protocol limits belong in their profiles.
GR-4 always grades current commands/state/results and claims, not presence of a hook.

Find the declared check in instructions, runner and CI. Run it if it only reads/tests;
disposable test data and ignored build output are allowed unless the user said strictly
read-only. Do not change tracked files or touch the project's own database in read-only work.
If credentials/services or safe isolation are unavailable, run safe components, name omitted
commands and report why. Do not obtain more authority to make the check pass.
No single runner fails CK-1; still exercise available safe checks. If tests cannot execute,
report that cause first; dependent execution rules cannot be met by those tests.

## 3. Grade with evidence

1. For every module trigger record applies/absent/uncertain and why. Resolve unknowns with
   the owner where possible; otherwise state the assumption. A false trigger costs nothing;
   a triggered module applies independently of the core target.
2. Grade core gates by introduction level, triggered module rules, then remaining core
   practices. Use the rule's Check column, not the topic essays. Record **met**, **partly met**,
   **not met**, **not verifiable**, **not applicable**, or **not assessed (above target)**,
   with file/line or actual command evidence. A document's claim is not its mechanism.
3. Read history for branch/merge use, change size, post-adoption features and human review.
   Tests-before-code needs actual red/green and revision/patch evidence, not commit order.
   Do not invent pre-adoption TDD or fail unexercised history as if a contrary event occurred.
4. For inaccessible host/external facts, restricted files or unexercised history, report
   what is known, the unresolved question and the owner who can settle it. Do not guess met
   or missing. An empty review history does not demonstrate RV-1; metadata is not consent.

Apply these evidence boundaries alongside the tables:

- **Tests:** report isolation, discovered scope/counts, skips, retries/quarantine and
  unexecuted targets. TS-10/TS-12 gate Level 1; TS-11/TS-13 are practices, without a universal
  mutation quota. Stage completion or a valid red handoff is not feature completion.
- **Maintainability:** inspect contracts/examples, exercised limits, trigger dispositions,
  exceptions, boundaries and retirement. A scoped reviewed baseline retains specific debt,
  never missing controls or worsening findings. Duplication/unused-code scans are leads.
  MT-4 reports the problem, consumers, baseline/final preservation and limits; green alone
  is not complete equivalence and a standalone refactor skill is not required in the project.
- **Security/style:** SE-2/SE-3 always apply; module security follows its trigger. Use real
  requirements, detection evidence, dependency trust and owned findings. Missing/stale/failed
  scans are gaps; debt cannot accept exposure. Inspect each maintained language's ST-1
  enforcement, including a deliberate project convention. Do not install scanners, bulk-format,
  scan live targets or infer deployed security from local settings.
- **Decisions/parallel work:** inspect append-only ADR evidence and contradictions (DC-2);
  never rewrite frozen decisions. Only for concurrent writers, inspect checkout/resources and
  private check state using Claude Code `${CLAUDE_PLUGIN_ROOT}/framework/worktrees.md`,
  otherwise `../../framework/worktrees.md`. Separate chats alone do not prove isolation.
- **Operate:** grade OP-1 to OP-11 when triggered. A protocol library or generated wrappers
  do not prove tool design. Inspect embedded prompts/allowed actions and whether output can
  approve/publish. Forwarded foreign tokens, skipped client consent and session-as-login fail
  OP-11. No AI-facing surface means not applicable.
- **Trial modules:** inspect canonical debt dispositions/authority/closure (MT-5); provenance,
  stale indexes/dirty inputs and recoverability (IN-8/WK-8); opted-in routing records,
  role/effort/access/budget bounds, fallbacks and actual independence (WK-7/MS-5). No invented
  debt, account probes or model sessions. One model in separate contexts remains valid.

## 4. Score and report

Use `levels.md` Scoring only after grading. Partial/missing gates block advancement;
unresolved gates support only a separately named provisional level with explicit assumptions.
Never average practices or convert an old score automatically. Score triggered modules by
their own marks (Operate O1–O3); report Trial modules, including GR-8, without a mark.

Put the earned level/name, target/additions, up to three key gaps (urgent risks explicit)
and one next action in the first 15 lines. Then give:

- Named practice progress, lower-level blockers and later strengths; module line with
  triggered modules first and reasons. Above-target gaps are optional, not target requirements.
  If target/additions are met, say so; the level is not product/deployment approval.
- Strengths and gaps with rule IDs/evidence, most serious first. Distinguish absent from
  designed-but-unexercised. Retain all verified findings without implying consent to fix them.
- **Do next:** one bounded adoption increment: benefit, scope, rule IDs, rough size and
  observable evidence. Prioritize serious risks, target additions, then required-level gates.
  A prototype needing only scenarios/decisions does not owe the rest of Level 3.
  Offer at most two optional follow-ups; do not convert the report into today's full backlog.
- What was not checked and why, including missing host, human review and execution evidence.
  File presence, model identity and automatic tool approval do not prove those protections.
