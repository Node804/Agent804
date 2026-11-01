# Operate research and validation limits

Read on 2026-11-01 to inform OP-9 to OP-11. These pages describe the Model Context Protocol.
They are not evidence that a project following them is safe, and they do not certify an
implementation.

| Reference consulted | Reinforced | Limits and framework choice |
|---|---|---|
| [MCP tools](https://modelcontextprotocol.io/specification/2025-11-25/server/tools), 2025-11-25 | Tools are model-controlled: the model discovers and invokes them, and results return to the model. Each tool has a name, description, and input schema. Servers must validate inputs, enforce access, rate-limit calls, and sanitize outputs. A human should be able to deny a tool invocation. Clients must treat tool annotations as untrusted unless the server is trusted | OP-9 requires a designed list, a bounded secret-free result, and a server-enforced effect. Agent804 requires a person can refuse a write or destructive call before the effect. A confirmation on every read is not a universal gate. No SDK, annotation, or JSON-RPC shape is required |
| [MCP security best practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices), 2025-11-25, through the local-server and token-passthrough sections | Servers must not accept a token that was not issued for them (token passthrough). Sessions must not authenticate. An OAuth proxy that uses one static client for a third party must take per-client consent before forwarding, or a consent cookie skips the person. Local servers run as the user; a one-click install shows the command and waits for approval. Clients that fetch authorization URLs have to consider SSRF | OP-11 states those properties without adopting an OAuth flow, dynamic client registration, or a particular cookie prefix. The rest of that page (URL-scheme handling onward) was not used. SSRF on discovery URLs is the client's problem; a project that ships such a client treats it under AR-6 and SE-1 rather than a new Operate rule |

OP-10 is this kit's rule, not a clause of the specification. The specification does not
discuss an in-product chat or classifier. Leaving that feature out of Operate would make it
a side door around OP-6 and OP-9.

OP-1 to OP-8 still come from one reference project's design. OP-9 to OP-11 have not been
trialled. No MCP server was built or attacked for this change. Repository checks cover the
new rule IDs, links, and budgets. They do not show that an agent follows the operate skill
or that a tool list stays small once a real feature is added.

Release-review corrections keep an unbounded OP-9 result consistently not met, restore the
OP-4 replay/recovery instructions and test cases, and limit OP-11's per-client consent to
OAuth proxies as the reference above describes. These are text-alignment corrections, not
new implementation or application-trial evidence.
