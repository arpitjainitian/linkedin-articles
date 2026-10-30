# Roadmap

Four kinds of writing, all in one place:

1. **AI engineering series** (1 to 16, in four acts): things that look simple and fail often in AI projects.
2. **Today in AI** (20): what's new in AI, and what it means, in plain words.
3. **AI system design** (21): one AI system design question per post.
4. **Certification prep** (22): the Claude Certified Architect – Foundations exam, one objective per post.
5. **Explainers** (23): trending AI ideas explained the "hello world" way, no code.

## 1. AI engineering series

Each topic is its own series, numbered below. Each is a sentence that sounds easy in a kickoff meeting and turns out to be the hard part of an AI project.

**The storyline:** one journey, the life of an AI system. Each series picks up where the last one ended, and each curtain raiser opens with a one-line bridge from the previous series.

- **Act 1. Make it work:** it answers (1), then it acts (2).
- **Act 2. Make it trustworthy:** it follows the rules (3), stays safe (4), proves it's right (5), and you can see inside it (6).
- **Act 3. Make it real:** it ships (7), it pays its way (8), and people actually change how they work (9).
- **Act 4. Make it bigger:** one front door (10), every tool (11), memory (12), connected knowledge (13), its own research (14), a team of agents (15), and the whole system around them (16).

**Order:** follows the story; difficulty still rises overall, from the basics in Act 1 to L5 in Act 4.
**Writing:** stays as simple as possible at every level: plain words, everyday analogies, real examples.

| Series | Topic ("looks simple") | Level | What it covers | Status | Why a full series, not one article |
|---|---|---|---|---|---|
| **Act 1. Make it work** | | | | | |
| 1 | "Just add RAG over our docs" | L2 | A full series of 15 write-ups, see [01-just-add-rag/](01-just-add-rag/README.md) | **Complete** (15 write-ups, finale 15 Oct 2026) | RAG hides 16 separate layers (ingestion, chunking, retrieval, permissions, cost...). Any one of them can sink the project on its own, and each needs its own explanation. |
| 2 | "Beyond Just RAG: From Answers to Actions" (#BeyondJustRAG #AnswersToActions) | L3 | From answers to actions, picking up where #JustAddRAG ends: exact data from messy input, safe retries, jobs that stop halfway, agents stuck in loops, workflow vs agent, testing agents. (Access, prompt injection and human approval were covered in #JustAddRAG.) Absorbs the old "Just ask it for JSON", "Give the agent the keys" and "Just make it agentic" series. Example: An expense-claims assistant at work. Plan: [02-answers-to-actions/](02-answers-to-actions/README.md) | **Complete** (all 8 published, 15 to 24 Oct 2026) | Acting is harder than answering: every action needs exact data, the right keys, safe retries and a human yes where money moves. Each step fails in its own way. |
| **Act 2. Make it trustworthy** | | | | | |
| 3 | "Just put the rules in the prompt" | L3 | Deterministic rules vs a probabilistic model. Example: An airline's refund and cancellation assistant. Plan: [03-business-rules/](03-business-rules/README.md) | **Complete** (write-ups 1-5 published, finale 30 October 2026) | Where code ends and the model begins differs for eligibility, pricing, compliance and approvals. One rule of thumb doesn't fit every rule. |
| 4 | "Just tell it not to" | L3 | Guardrails: input and output checks, jailbreaks, red-teaming agents, staff exceptions, safety vs usefulness. Example: An online pharmacy's medicine-question assistant. Plan: [04-guardrails/](04-guardrails/README.md) | **Planned (outline ready)** | Guardrails are layers, not a single prompt: input checks, output checks, jailbreak tests, staff exceptions and strictness each handle a different failure. |
| 5 | "Works on my prompt" | L2 | Evals, one level deeper: grading each step, auditing the AI grader, release gates, test questions leaking into prompts (the basics are in #JustAddRAG 9). Example: An HR policy assistant for employees. Plan: [05-the-prompt-works-ship-it/](05-the-prompt-works-ship-it/README.md) | **Planned (outline ready)** | Testing AI well goes beyond a test set: right-for-the-wrong-reason answers, biased graders, launch thresholds and leaky tests each deserve their own deep dive. |
| 6 | "We'll know when it breaks" | L3 | Beyond observability basics: cost as a warning sign, canary questions, fault testing, service targets and incidents (the basics are in #JustAddRAG 13). Example: A food-delivery app's support bot. Plan: [06-observability/](06-observability/README.md) | **Planned (outline ready)** | Traces and dashboards miss the quiet failures. Cost signals, canary questions, fault testing and incident handling each catch a different kind. |
| **Act 3. Make it real** | | | | | |
| 7 | "It worked in the demo" | L2 | The POC-to-production cliff, ownership. Example: Invoice processing in accounts payable. Plan: [07-poc-to-production/](07-poc-to-production/README.md) | **Planned (outline ready)** | The gap between demo and production is a dozen gaps, each owned by a different team: security, operations, support, finance, legal. |
| 8 | "What's a few cents between friends?" | L2 | The money decisions behind AI: pricing AI features, renting vs running models, batch vs real time, value per feature, forecasting (the basics are in #JustAddRAG 10). Example: A product-question assistant on a shopping site. Plan: [08-few-cents-per-call/](08-few-cents-per-call/README.md) | **Planned (outline ready)** | An AI bill is a set of business decisions: who pays, rent or own, now or later, worth it or not, next year's budget. Each has its own trap and its own fix. |
| 9 | "We bought AI, so we're AI-first now" | L1 | Process redesign, people, changing roles and simple rules for using AI. Example: An e-commerce company's 500 support agents getting AI. Plan: [09-ai-transformation/](09-ai-transformation/README.md) | **Planned (outline ready)** | Transformation touches people, process, skills, metrics, governance and culture. Buying licences is one decision; changing how work gets done is many. |
| **Act 4. Make it bigger** | | | | | |
| 10 | "Everyone gets an API key" | L4 | AI gateway: auth, routing, rate limits, caching, fallbacks across providers. Example: A 5,000-person company sharing one AI platform. Plan: [10-ai-gateway/](10-ai-gateway/README.md) | **Planned (outline ready)** | A gateway handles access, routing, limits, caching, fallbacks and governance. Each solves a different problem when many teams share AI. |
| 11 | "Just plug it in" | L4 | What MCP is, why it helps, and what it doesn't solve. Example: An IT helpdesk assistant connected through MCP. Plan: [11-mcp-server/](11-mcp-server/README.md) | **Planned (outline ready)** | MCP looks like plug-and-play, but servers, discovery, permissions, versioning, third-party trust and tool poisoning each raise different questions. |
| 12 | "It should just remember me" | L4 | AI memory: short-term context, summarising long chats, long-term memory stores, what to remember and what to forget, privacy of remembered facts. Example: A shopping assistant that remembers you. Plan: [12-ai-memory/](12-ai-memory/README.md) | **Planned (outline ready)** | Memory spans short-term context, long-term stores, what to forget, privacy and cost. Getting one right doesn't fix the others. |
| 13 | "Just connect the dots" | L4 | GraphRAG: entities and relationships, multi-hop questions, explainable paths, and the real cost of building and maintaining the graph. Example: Supplier risk at a manufacturer. Plan: [13-knowledge-graph/](13-knowledge-graph/README.md) | **Planned (outline ready)** | A knowledge graph has to be designed, built, kept current and queried, and it's not always worth it. Each step is a project of its own. |
| 14 | "Let it do its own research" | L5 | Agentic RAG: plan, retrieve, reason, retrieve again; loops, cost and latency, when plain RAG is enough. Example: Contract review for the legal team. Plan: [14-agentic-rag/](14-agentic-rag/README.md) | **Planned (outline ready)** | Letting the agent search adds loops, extra cost, extra latency and new failure modes, plus the question of when plain RAG is enough. |
| 15 | "More agents, more brains" | L5 | Multi-agent systems: orchestrators, isolated context, compounding errors. Example: New-employee onboarding with multiple agents. Plan: [15-multi-agent/](15-multi-agent/README.md) | **Planned (outline ready)** | Many agents bring orchestration patterns, handoffs, shared context and compounding errors. Each pattern needs its own trade-offs. |
| 16 | "We bought the brain, we're done" | L5 | The agent harness: you own the loop. Example: An insurance claims-processing agent. Plan: [16-agent-harness/](16-agent-harness/README.md) | **Planned (outline ready)** | The harness around the model (state, sandboxes, what the agent is allowed to do, what the model sees, layered defences) is everything you own. Each part deserves its own look. |


## 2. Today in AI

| Series | Topic | Level | What it covers | Status | Why a full series, not one article |
|---|---|---|---|---|---|
| 20 | "Today in AI" (#TodayInAI) | Mixed | One AI story that matters per write-up (news, plus occasional explainers), checked against original sources and explained in plain words, for both people learning AI and leaders. Fixed cover frame, fresh middle design each time. Plan and write-ups: [20-today-in-ai/](20-today-in-ai/README.md) | **In progress** (No. 001 to 011 published) | AI changes every week. An ongoing series, with no fixed cadence and no end, keeps up with it one story at a time. |

## 3. AI system design

| Series | Topic | Level | What it covers | Status | Why a full series, not one article |
|---|---|---|---|---|---|
| 21 | "It works in the demo. Now design it for production." | L3 to L5 | One AI system design question per post, the kind asked in AI engineer and architect interviews: 33 questions in 8 areas (RAG and retrieval, cost and latency, agents and memory, output quality and evals, safety, training, serving, observability). Plan and articles: [21-system-design/](21-system-design/README.md) | **In progress** (question 8 drafted, the rest planned) | Each production problem (cost, loops, scale, quality) is a separate design question with its own trade-offs. One question per post keeps each answer clear. |

Topics 9-11, 16, 18 and 19 were inspired by a "9 AI concepts" infographic by Brij Kishore Pandey ([@brijpandeyji](https://www.linkedin.com/in/brijpandeyji/)). Topics 12 and 17 were inspired by an "Agentic RAG vs GraphRAG" comparison infographic. Topic 15 was inspired by an "Anatomy of an AI Agent" diagram.


**Retired 2026-10-15:** "Build it and they will chat" (old series 2; its topics overlapped #JustAddRAG), "Just ask it for JSON" (old 7) and "Give the agent the keys" (old 14), both absorbed into the new Series 2. "Just make it agentic" (old 16, then 14) was also absorbed into Series 2 on 2026-10-15. Files kept in [_retired/](_retired/).

## 4. Certification prep

| Series | Topic | Level | What it covers | Status | Why a full series, not one article |
|---|---|---|---|---|---|
| 22 | "Claude Architect, One Objective at a Time" (#ClaudeArchitectPrep) | L3 to L4 | Study series for the Claude Certified Architect – Foundations exam: one write-up per exam objective (30), with a practice question each. Running example: ParentPace, a fictional parenting-coach company. 38 articles: 30 objectives, 5 domain checkpoints, curtain raiser, mock exam, exam-day finale. Plan: [22-claude-architect-exam/](22-claude-architect-exam/README.md) | **Planned (outline ready)** | The exam has 30 objectives across 5 domains; each one is a separate skill with its own practice question. |

## 5. Explainers

| Series | Topic | Level | What it covers | Status | Why a full series, not one article |
|---|---|---|---|---|---|
| 23 | "Explain It Like Hello World" (#ExplainItLikeHelloWorld) | L1 to L2 | Trending AI ideas (tokens, embeddings, attention, quantization, mixture of experts, reasoning models, diffusion, A2A and more), each explained through the smallest example that shows it working. No code. 104 write-ups in 10 parts, one word each, ending with an AI dictionary. Topics covered by other series (RAG, MCP, agents, guardrails, memory, evals, cost) are linked, not repeated. Plan: [23-explain-like-hello-world/](23-explain-like-hello-world/README.md) | **In progress** (write-ups 1-5 published, latest 30 Oct 2026; 124 write-ups drafted) | Each AI word is its own idea with its own hello-world example; readers can share one explainer at a time. |
