# Roadmap: AI engineering that looks simple, and fails often

Each topic is a sentence that sounds easy in a kickoff meeting and turns out to be the hard part of an AI project.

**Order:** technical difficulty goes up gradually, from L1 (easy) to L5 (advanced).
**Writing:** stays as simple as possible at every level: plain words, everyday analogies, real examples.

| # | Topic ("looks simple") | Level | What it covers | Status |
|---|---|---|---|---|
| 1 | "Just add RAG over our docs" | L2 | A full series of write-ups, see [just-add-rag/](just-add-rag/README.md) | **In progress** |
| 2 | "Users will love the chatbot" | L1 | Trust, UX, citations, "I don't know", adoption | Planned |
| 3 | "AI transformation = buy licenses + train people" | L1 | Process redesign, success metrics | Planned |
| 4 | "The POC got a standing ovation" | L2 | The POC-to-production cliff, ownership | Planned |
| 5 | "It's only a few cents per call" | L2 | Inference economics: tokens, caching, model choice, the total bill | Planned |
| 6 | "The prompt works, ship it" | L2 | Evals: test cases, judge LLMs, rubrics, silent regressions | Planned |
| 7 | "LLM output → JSON → done" | L3 | Structured output, validation | Planned |
| 8 | "Let the LLM handle the business rules" | L3 | Deterministic rules vs a probabilistic model | Planned |
| 9 | "Just tell it in the prompt not to do that" | L3 | Guardrails: input and output filters, PII, jailbreaks, policy | Planned |
| 10 | "We'll just check the logs" | L3 | Observability: traces, logs, metrics, feedback | Planned |
| 11 | "Just call the model API directly" | L4 | AI gateway: auth, routing, rate limits, caching, fallbacks across providers | Planned |
| 12 | "Just add an MCP server" | L4 | What MCP is, why it helps, and what it doesn't solve | Planned |
| 13 | "Connect the agent to our DB/tools" | L4 | Tool security, least privilege, prompt injection through data | Planned |
| 14 | "Let's make it agentic" | L4 | Agentic loops: plan, act, observe, reflect; when a workflow beats an agent | Planned |
| 15 | "Add more agents, it'll get smarter" | L5 | Multi-agent systems: orchestrators, isolated context, compounding errors | Planned |
| 16 | "The vendor ships the model, so we're done" | L5 | The agent harness: you own the loop | Planned |

Topics 9-11 and 14-16 were inspired by a "9 AI concepts" infographic by Brij Kishore Pandey ([@brijpandeyji](https://www.linkedin.com/in/brijpandeyji/)).
