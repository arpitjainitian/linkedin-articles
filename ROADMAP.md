# Roadmap

Three kinds of writing, all in one place:

1. **AI engineering series** (1 to 17): things that look simple and fail often in AI projects.
2. **Today in AI** (20): what's new in AI, and what it means, in plain words.
3. **AI system design** (21): one AI system design question per post.

## 1. AI engineering series

Each topic is its own series, numbered below. Each is a sentence that sounds easy in a kickoff meeting and turns out to be the hard part of an AI project.

**Order:** technical difficulty goes up gradually, from L1 (easy) to L5 (advanced).
**Writing:** stays as simple as possible at every level: plain words, everyday analogies, real examples.

| Series | Topic ("looks simple") | Level | What it covers | Status | Why a full series, not one article |
|---|---|---|---|---|---|
| 1 | "Just add RAG over our docs" | L2 | A full series of 15 write-ups, see [01-just-add-rag/](01-just-add-rag/README.md) | **Complete** (15 write-ups, finale 15 Oct 2026) | RAG hides 16 separate layers (ingestion, chunking, retrieval, permissions, cost...). Any one of them can sink the project on its own, and each needs its own explanation. |
| 2 | "It answered. Now make it act." (#NowMakeItAct) | L3 | From answers to actions, picking up where #JustAddRAG ends: exact data from messy input, minimal access, instructions hidden in data, safe retries, human approval, systems that change. Absorbs the old "Just ask it for JSON" and "Give the agent the keys" series. Example: An expense-claims assistant at work. Plan: [02-answers-to-actions/](02-answers-to-actions/README.md) | **Planned (outline ready)** | Acting is harder than answering: every action needs exact data, the right keys, safe retries and a human yes where money moves. Each step fails in its own way. |
| 3 | "We bought AI, so we're AI-first now" | L1 | Process redesign, people, changing roles and simple rules for using AI. Example: An e-commerce company's 500 support agents getting AI. Plan: [03-ai-transformation/](03-ai-transformation/README.md) | **Planned (outline ready)** | Transformation touches people, process, skills, metrics, governance and culture. Buying licences is one decision; changing how work gets done is many. |
| 4 | "It worked in the demo" | L2 | The POC-to-production cliff, ownership. Example: Invoice processing in accounts payable. Plan: [04-poc-to-production/](04-poc-to-production/README.md) | **Planned (outline ready)** | The gap between demo and production is a dozen gaps, each owned by a different team: security, operations, support, finance, legal. |
| 5 | "What's a few cents between friends?" | L2 | The money decisions behind AI: pricing AI features, renting vs running models, batch vs real time, value per feature, forecasting (the basics are in #JustAddRAG 10). Example: A product-question assistant on a shopping site. Plan: [05-few-cents-per-call/](05-few-cents-per-call/README.md) | **Planned (outline ready)** | An AI bill is a set of business decisions: who pays, rent or own, now or later, worth it or not, next year's budget. Each has its own trap and its own fix. |
| 6 | "Works on my prompt" | L2 | Evals, one level deeper: grading each step, auditing the AI grader, release gates, test questions leaking into prompts (the basics are in #JustAddRAG 9). Example: An HR policy assistant for employees. Plan: [06-the-prompt-works-ship-it/](06-the-prompt-works-ship-it/README.md) | **Planned (outline ready)** | Testing AI well goes beyond a test set: right-for-the-wrong-reason answers, biased graders, launch thresholds and leaky tests each deserve their own deep dive. |
| 7 | "Just put the rules in the prompt" | L3 | Deterministic rules vs a probabilistic model. Example: An airline's refund and cancellation assistant. Plan: [07-business-rules/](07-business-rules/README.md) | **Planned (outline ready)** | Where code ends and the model begins differs for eligibility, pricing, compliance and approvals. One rule of thumb doesn't fit every rule. |
| 8 | "Just tell it not to" | L3 | Guardrails: input and output checks, jailbreaks, staff exceptions, safety vs usefulness. Example: An online pharmacy's medicine-question assistant. Plan: [08-guardrails/](08-guardrails/README.md) | **Planned (outline ready)** | Guardrails are layers, not a single prompt: input checks, output checks, jailbreak tests, staff exceptions and strictness each handle a different failure. |
| 9 | "We'll know when it breaks" | L3 | Beyond observability basics: cost as a warning sign, canary questions, fault testing, service targets and incidents (the basics are in #JustAddRAG 13). Example: A food-delivery app's support bot. Plan: [09-observability/](09-observability/README.md) | **Planned (outline ready)** | Traces and dashboards miss the quiet failures. Cost signals, canary questions, fault testing and incident handling each catch a different kind. |
| 10 | "Everyone gets an API key" | L4 | AI gateway: auth, routing, rate limits, caching, fallbacks across providers. Example: A 5,000-person company sharing one AI platform. Plan: [10-ai-gateway/](10-ai-gateway/README.md) | **Planned (outline ready)** | A gateway handles access, routing, limits, caching, fallbacks and governance. Each solves a different problem when many teams share AI. |
| 11 | "Just connect the dots" | L4 | GraphRAG: entities and relationships, multi-hop questions, explainable paths, and the real cost of building and maintaining the graph. Example: Supplier risk at a manufacturer. Plan: [11-knowledge-graph/](11-knowledge-graph/README.md) | **Planned (outline ready)** | A knowledge graph has to be designed, built, kept current and queried, and it's not always worth it. Each step is a project of its own. |
| 12 | "Just plug it in" | L4 | What MCP is, why it helps, and what it doesn't solve. Example: An IT helpdesk assistant connected through MCP. Plan: [12-mcp-server/](12-mcp-server/README.md) | **Planned (outline ready)** | MCP looks like plug-and-play, but servers, discovery, permissions, versioning and third-party trust each raise different questions. |
| 13 | "It should just remember me" | L4 | AI memory: short-term context, summarising long chats, long-term memory stores, what to remember and what to forget, privacy of remembered facts. Example: A shopping assistant that remembers you. Plan: [13-ai-memory/](13-ai-memory/README.md) | **Planned (outline ready)** | Memory spans short-term context, long-term stores, what to forget, privacy and cost. Getting one right doesn't fix the others. |
| 14 | "Just make it agentic" | L4 | Agentic loops: plan, act, observe, reflect; when a workflow beats an agent. Example: A corporate travel-booking agent. Plan: [14-lets-make-it-agentic/](14-lets-make-it-agentic/README.md) | **Planned (outline ready)** | An agent is a loop with many moving parts: planning, tools, stopping, recovery and testing. Each fails differently. |
| 15 | "Let it do its own research" | L5 | Agentic RAG: plan, retrieve, reason, retrieve again; loops, cost and latency, when plain RAG is enough. Example: Contract review for the legal team. Plan: [15-agentic-rag/](15-agentic-rag/README.md) | **Planned (outline ready)** | Letting the agent search adds loops, extra cost, extra latency and new failure modes, plus the question of when plain RAG is enough. |
| 16 | "More agents, more brains" | L5 | Multi-agent systems: orchestrators, isolated context, compounding errors. Example: New-employee onboarding with multiple agents. Plan: [16-multi-agent/](16-multi-agent/README.md) | **Planned (outline ready)** | Many agents bring orchestration patterns, handoffs, shared context and compounding errors. Each pattern needs its own trade-offs. |
| 17 | "We bought the brain, we're done" | L5 | The agent harness: you own the loop. Example: An insurance claims-processing agent. Plan: [17-agent-harness/](17-agent-harness/README.md) | **Planned (outline ready)** | The harness around the model (state, sandboxes, what the model sees, layered defences) is everything you own. Each part deserves its own look. |


## 2. Today in AI

| Series | Topic | Level | What it covers | Status | Why a full series, not one article |
|---|---|---|---|---|---|
| 20 | "Today in AI" (#TodayInAI) | Mixed | One AI story that matters per write-up (news, plus occasional explainers), checked against original sources and explained in plain words, for both people learning AI and leaders. Fixed cover frame, fresh middle design each time. Plan and write-ups: [20-today-in-ai/](20-today-in-ai/README.md) | **In progress** (No. 001 to 008 published) | AI changes every week. An ongoing series, with no fixed cadence and no end, keeps up with it one story at a time. |

## 3. AI system design

| Series | Topic | Level | What it covers | Status | Why a full series, not one article |
|---|---|---|---|---|---|
| 21 | "It works in the demo. Now design it for production." | L3 to L5 | One AI system design question per post, the kind asked in architect interviews and design reviews: cost, agent loops, consistency, evals, architecture and scale. Plan and articles: [21-system-design/](21-system-design/README.md) | **In progress** (question 1 drafted, 2 to 6 planned) | Each production problem (cost, loops, scale, quality) is a separate design question with its own trade-offs. One question per post keeps each answer clear. |

Topics 9-11, 16, 18 and 19 were inspired by a "9 AI concepts" infographic by Brij Kishore Pandey ([@brijpandeyji](https://www.linkedin.com/in/brijpandeyji/)). Topics 12 and 17 were inspired by an "Agentic RAG vs GraphRAG" comparison infographic. Topic 15 was inspired by an "Anatomy of an AI Agent" diagram.


**Retired 2026-10-15:** "Build it and they will chat" (old series 2; its topics overlapped #JustAddRAG), "Just ask it for JSON" (old 7) and "Give the agent the keys" (old 14), both absorbed into the new Series 2. Files kept in [_retired/](_retired/).
