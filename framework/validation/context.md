# Context-management research and validation limits

These primary sources were read to inform proposed IN-8/WK-8 guidance and recovery trials.
Research task/model conditions differ from actual repository maintenance; no universal
context limit, architectural diagnosis or guaranteed improvement is inferred.

| Reference consulted | Reinforced | Limits and framework choice |
|---|---|---|
| [Lost in the Middle](https://arxiv.org/abs/2307.03172), 2023 abstract | Relevant-position effects in multi-document QA and key-value retrieval motivate testing effective evidence use | Older tested models/tasks do not establish every current model's behavior; no universal placement rule |
| [RULER](https://arxiv.org/abs/2404.06654), 2024 abstract | Single-needle retrieval is insufficient; multi-hop tracing/aggregation motivate combined maintenance trials | Synthetic benchmarks are not proof of real project competence or a fixed safe token budget |
| [Robustness to irrelevant context](https://arxiv.org/abs/2310.01558), abstract | Irrelevant retrieval can reduce QA accuracy and compound multi-hop errors | Proposed relevance/coverage checks do not mandate this paper's training/filtering method or claim coding-task gains |
| [Anthropic contextual retrieval](https://www.anthropic.com/research/contextual-retrieval) | Exact identifiers, lexical/semantic complementarity, contextualized chunks and reranking inform scoped retrieval with provenance | Vendor experiments do not justify a universal chunk size/top-k, embedding choice or mandatory vector database |
| [Anthropic context engineering](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents) | Just-in-time retrieval, structured notes and compaction inform recoverable task state | An attention budget is a working model, not a measured universal quota. Summaries need source revalidation; no automatic delegation required |
| [Google: Retrieval Quality at Context Limit](https://research.google/pubs/retrieval-quality-at-context-limit/), 2025 abstract | Strong position-independent simple factoid retrieval in Gemini 2.5 Flash qualifies blanket lost-in-the-middle claims | Simple QA does not establish multi-source code reasoning, complete recall or equivalence across models |
| [Microsoft MInference FAQ](https://www.microsoft.com/en-us/research/project/minference-million-tokens-prompt-inference-for-long-context-llms/faq/) | Sparse attention is an implementation research topic evaluated on multiple tasks | Framework context hygiene does not modify attention internals or diagnose why a particular model missed a rule |

IN-8/WK-8 are reported practices, not rung gates. Existing navigation/freshness and handoff
rules are clarified, not replaced. The optional context playbook uses plan/PR working records
rather than a mandatory new document. No vector/index service, model-specific compactor or
attention adapter is shipped. Repository checks cover references, metadata and line budgets;
they do not measure retrieval recall, attention, context completeness or recovery accuracy.

Recovery trials remain pending: stale-versus-current authority, omitted cross-file constraints,
superseding decisions, truncation/summarization loss, dirty-worktree index drift and correct
recognition of insufficient evidence. Equivalent maintenance tasks must record expected
contracts/outcomes, actual host/model/effort/inputs, observed coverage, defects/interventions,
recovery accuracy, unnecessary reads and measured overhead. No additional model sessions,
paid trials or automatic source access were performed as part of this documentation change.
