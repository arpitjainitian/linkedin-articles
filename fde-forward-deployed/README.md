# Forward Deployed: the FDE series

**Hashtag:** #ForwardDeployed

**Track:** a parallel track, alongside the AI engineering series (1 to 16). It follows the job of a Forward Deployed Engineer (FDE), not the AI engineering order. It is listed as section 6 of the [ROADMAP.md](https://github.com/arpitjainitian/linkedin-articles/blob/main/ROADMAP.md) in the [linkedin-articles repo](https://github.com/arpitjainitian/linkedin-articles/tree/main).

**The promise:** the demo is the easy part. This series follows the FDE's job from the first customer meeting to the handover, one week at a time.

**The focus:** the customer. Every write-up starts from a customer's problem, people or Monday, and asks what the engineer must do so that customer gets value. Tools and methods appear only when they serve that.

**Running example:** a wholesale distributor's order desk. Customers email their orders, the desk checks stock and prices, and an assistant drafts the replies. Every write-up uses this same desk.

A write-up is marked **Published** only once it is live on LinkedIn.

## Planned write-ups

The plan covers both programmes. **H** marks the 13-week programme (weeks and capstone), **R** marks the 4-phase programme. "Covered elsewhere" points to the existing series that holds the basics.

| # | Week | Title | Customer question | Covers | Covered elsewhere | Status | LinkedIn |
|---|---|---|---|---|---|---|---|
| 1 | Curtain raiser | [Why does the customer's Monday matter more than your demo?](01-curtain-raiser.md) | What does the customer's real week look like? | FDE role, three hats (R: why FDE, skills) | | Draft for review | |
| 2 | H1 / R1 | What should you learn from the customer before you build anything? | What would make this worth paying for? | Customer discovery, workflow mapping, value and baselines (R: AI for enterprises, PoV to PoC to MVP) | | Planned | |
| 3 | H2 | How do you turn the customer's rules into something you can test? | Which rules must the system follow, and how will we know it does? | Solution and service foundation: architecture, trust boundaries, API contracts, tests | | Planned | |
| 4 | H3 / R1 | Where does the customer's data hide, and which copy is true? | Which system is the record of truth? | Data estate, canonical model, data quality (R: pipelines, metrics, visualisation) | Ingestion basics in [Just add RAG](../01-just-add-rag/README.md) | Planned | |
| 5 | H4 | What happens when two of the customer's systems disagree? | What happens to an order when the systems disagree? | Integrations, retries, idempotency, events and replay | Safe retries in [Beyond Just RAG](../02-answers-to-actions/README.md) | Planned | |
| 6 | H5 | How do you let a model act in the customer's systems without breaking their records? | Which actions may the assistant take on its own? | Model interfaces, structured outputs, schema checks, controlled tool execution | Tools in [Beyond Just RAG](../02-answers-to-actions/README.md), rules in [Just put the rules in the prompt](../03-business-rules/README.md) | Planned | |
| 7 | R2 | How do you write prompts the customer's security team will sign off? | What must the prompts never do in this business? | Role, task and context prompts; chain-of-thought; reviewable prompt libraries | Prompt basics in [Just add RAG](../01-just-add-rag/README.md) | Planned | |
| 8 | H6 / R2 | How do you make answers point to the customer's own documents? | Can the customer check every answer against its source? | Document ingestion, hybrid search, reranking, evidence-grounded answers, access filters | [Just add RAG](../01-just-add-rag/README.md) (the basics) | Planned | |
| 9 | R1 | Fine-tune, retrieve or prompt: which fits the customer's problem? | Does the customer need new knowledge, new behaviour, or both? | Fine-tuning (LoRA) against retrieval and prompting, and the cost of each | Embeddings and transformers in [Explain It Like Hello World](../23-explain-like-hello-world/README.md) | Planned | |
| 10 | H7 | What happens when an agent stops halfway through the customer's job, and who steers it? | Who approves a step, and where does the job resume? | Durable workflow state, checkpoints, human approvals, operator controls | [Beyond Just RAG](../02-answers-to-actions/README.md), [MCP](../11-mcp-server/README.md), [memory](../12-ai-memory/README.md), [agent harness](../16-agent-harness/README.md) | Planned | |
| 11 | R3 | Who decides when several agents work on the customer's case? | Which agent owns which part of the customer's case? | Autonomy vs orchestration, multi-agent patterns | [Multi-agent](../15-multi-agent/README.md), [agentic RAG](../14-agentic-rag/README.md) | Planned | |
| 12 | R3 | How do you test the customer's assistant before a stranger does? | How could someone misuse this against the customer? | Bias, adversarial prompts, attack and defence, red-teaming for the customer's use case | [Just tell it not to](../04-guardrails/README.md) | Planned | |
| 13 | H8 / R4 | How do you show the customer it is good enough, and what it will cost them? | What quality and cost are acceptable, and who signs? | Evaluation datasets, failure analysis, judge calibration, model comparison, cost and latency, release gates | [The prompt works, ship it](../05-the-prompt-works-ship-it/README.md), [A few cents between friends](../08-few-cents-per-call/README.md) | Planned | |
| 14 | H9 / R4 | Who at the customer may do what, and can you prove it later? | Who is accountable for each decision the system makes? | Enterprise identity, authorisation, privacy, risk frameworks, safety policies, audit evidence | [Just tell it not to](../04-guardrails/README.md) | Planned | |
| 15 | H10 / R2 | Where should it run in the customer's cloud, and who restarts it at 2 am? | Which cloud and network may the customer's data touch? | Deployment topologies, containers, secrets, networking, release delivery (R: cloud basics, Docker, serverless) | [AI gateway](../10-ai-gateway/README.md) | Planned | |
| 16 | H11 | How does the customer know it is working on a Tuesday afternoon? | Who is told first when it degrades? | End-to-end telemetry, service-level objectives, capacity tests, failure diagnosis, incident recovery | [We'll know when it breaks](../06-observability/README.md) | Planned | |
| 17 | H12 | How do you run a pilot with real users without betting the customer's business? | What does the customer's team need to see before they switch over? | User acceptance tests, pilot design, migration readiness, cutover, rollback | [It worked in the demo](../07-poc-to-production/README.md) | Planned | |
| 18 | H13 | What does the customer's team need to run this without you? | Who on the customer's side owns it after you leave? | Operational handover, measured business value, reusable assets, feedback to the product | | Planned | |
| 19 | R4 | Which AI bets should the customer make first, and how do you score the risk? | Which problem is worth the money first? | Stakeholder mapping, KPI alignment, AI roadmap per function, risk scoring, case studies, portfolio artefacts | [AI transformation](../09-ai-transformation/README.md) | Planned | |
| 20 | Finale | Is it ready for the customer, or only for the demo? | Would the customer accept this and keep using it? | Readiness checklist; capstone readout of discovery, working system, evaluation, operations and measured value (H capstone; R capstone plan) | | Planned | |

## Not in the series: the basics

These topics from the two courses are taught in existing series. The FDE series links to them instead of repeating them.

- Tokens, embeddings, attention, LLM basics: [Explain It Like Hello World](../23-explain-like-hello-world/README.md)
- RAG ingestion, chunking and retrieval basics: [Just add RAG](../01-just-add-rag/README.md)
- Deterministic rules vs model judgment: [Just put the rules in the prompt](../03-business-rules/README.md)

## After each publish

- Mark the row **Published** with the date, and add the LinkedIn link.
- Post the series index as the first comment, then pin it.
- Update the pinned index on write-up 1.
