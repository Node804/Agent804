# Validation

I built Agent804 from my own work building agentic apps with coding agents. Then I checked it
against what other people building this way have published, and used their work to reinforce
it: it confirmed most of what I had, tightened a few rules, and gave me some practices I didn't
have yet, like having a separate session write the tests and zoning code green, yellow or red
by how much damage a change could do.

The table records what each reference reinforced and, where Agent804 chose differently, why.
It is here so that anyone changing a rule, person or agent, can see what it rests on.

| Reference | Reinforced | Where Agent804 chose differently, and why |
|---|---|---|
| Anthropic, [Claude Code best practices](https://code.claude.com/docs/en/best-practices) | Short instructions holding only what an agent can't find for itself; must-always rules as hooks and deny rules; the check command up front; review in a fresh context; a stop hook so the agent can't finish with the check red | |
| Anthropic, [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Keep always-loaded context small; add instructions for failures you actually see | |
| Anthropic, [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) | A boot script before any feature; progress kept in the repository; an end-to-end check before "done" | |
| OpenAI, [Harness engineering](https://openai.com/index/harness-engineering/) | `AGENTS.md` as a map into `docs/`; the repository as the system of record; lint messages that tell the agent how to fix the problem; scheduled doc gardening | OpenAI makes human review optional at high volume. Agent804 keeps a person on every merge: few teams have the tooling and coverage that makes skipping it safe, and OpenAI says as much |
| Simon Willison, [Vibe engineering](https://simonwillison.net/2025/Oct/7/vibe-engineering/), [Designing agentic loops](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/) | Tests first and run first; small reviewed changes with evidence; no production credentials for agents | A production system reachable with no credential at all isn't scored as a leaked secret, because the repository can't fix it; it is reported as an outside risk instead |
| Harper Reed, [My LLM codegen workflow atm](https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/) | Spec, then plan, then checklist; a branch before every session | One workflow for every change. Agent804 sizes the spec to the change: a full spec for a one-line fix is waste |
| Addy Osmani, [My LLM coding workflow going into 2026](https://addyosmani.com/blog/ai-coding-workflow/), [Brownfield agentic engineering](https://addyosmani.com/blog/brownfield-agentic-engineering/) | Instructions hold only what code can't say; a review comment that keeps coming back becomes a check; a separate session writes the tests; risk zones; measure lead time and interventions, not lines | |
| Kent Beck, [Augmented coding: beyond the vibes](https://newsletter.kentbeck.com/p/augmented-coding-beyond-the-vibes) | One failing test at a time; structural and behavioural changes kept apart; signs an agent is going wrong | |
| Birgitta Böckeler, [Understanding spec-driven development](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) | One fixed workflow doesn't fit every size of change; heavy specs are hard to review | |
| Birgitta Böckeler, [Context engineering for coding agents](https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html), [Harness engineering for coding agent users](https://martinfowler.com/articles/harness-engineering.html) | Guides that steer and sensors that check; deterministic checks before AI review; a small always-loaded file with the rest on demand | |
| GitHub, [Spec Kit](https://github.com/github/spec-kit) | A project constitution (here, `AGENTS.md`); `[NEEDS CLARIFICATION]` markers resolved before planning | Spec Kit fixes bugs by changing the spec and regenerating the code. Agent804 fixes the code, and the harness if a rule was missing: regenerating from the same spec doesn't give the same code twice |
