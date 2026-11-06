# Forward Deployed: the FDE series

**Hashtag:** #ForwardDeployed

**Track:** a parallel track, alongside the AI engineering series (1 to 16). It follows the job of a Forward Deployed Engineer (FDE), not the AI engineering order. It is listed as section 6 of the [ROADMAP.md](https://github.com/arpitjainitian/linkedin-articles/blob/main/ROADMAP.md) in the [linkedin-articles repo](https://github.com/arpitjainitian/linkedin-articles/tree/main).

**The promise:** the demo is the easy part. This series follows the FDE's job from the first customer meeting to the handover, one week at a time.

**The focus:** the customer. Every write-up starts from a customer's problem, people or Monday, and asks what the engineer must do so that customer gets value. Tools and methods appear only when they serve that.

**Running example:** a wholesale distributor's order desk. Customers email their orders, the desk checks stock and prices, and an assistant drafts the replies. Every write-up uses this same desk.

A write-up is marked **Published** only once it is live on LinkedIn.

**Reference rule:** every link to an article in this series points to LinkedIn. Series names are plain text. A **Red flag** means no published LinkedIn article covers that topic yet.

## Planned write-ups

The plan covers both programmes. **H** marks the 13-week programme (weeks and capstone), **R** marks the 4-phase programme. "Read first" names the earlier series and the LinkedIn article to read.

| # | Week | Title | Customer question | Covers | Read first (series: article) | Red flag | Status | LinkedIn |
|---|---|---|---|---|---|---|---|---|
| 1 | Curtain raiser | [Why does the customer's Monday matter more than your demo?](01-curtain-raiser.md) | What does the customer's real week look like? | FDE role, three hats (R: why FDE, skills) | Five pre-reads, listed in the curtain raiser | None | Draft for review | |
| 2 | H1 / R1 | What should you learn from the customer before you build anything? | What would make this worth paying for? | Customer discovery, workflow mapping, value and baselines (R: AI for enterprises, PoV to PoC to MVP) | None | No published article on PoV to PoC to MVP | Planned | |
| 3 | H2 | How do you turn the customer's rules into something you can test? | Which rules must the system follow, and how will we know it does? | Solution and service foundation: architecture, trust boundaries, API contracts, tests | None | No published article on architecture or API contracts | Planned | |
| 4 | H3 / R1 | Where does the customer's data hide, and which copy is true? | Which system is the record of truth? | Data estate, canonical model, data quality (R: pipelines, metrics, visualisation) | #JustAddRAG: [Why can't your AI read a PDF that a 10-year-old can?](https://www.linkedin.com/pulse/why-cant-your-ai-read-pdf-10-year-old-can-arpit-jain-fimif/) | None | Planned | |
| 5 | H4 | What happens when two of the customer's systems disagree? | What happens to an order when the systems disagree? | Integrations, retries, idempotency, events and replay | #BeyondJustRAG: [It Filed the Same Claim Twice](https://www.linkedin.com/pulse/3-filed-same-claim-twice-safe-retries-arpit-jain-7ttrf) | None | Planned | |
| 6 | H5 | How do you let a model act in the customer's systems without breaking their records? | Which actions may the assistant take on its own? | Model interfaces, structured outputs, schema checks, controlled tool execution | Just put the rules in the prompt: [Code Decides. The AI Explains.](https://www.linkedin.com/pulse/2-code-decides-ai-explains-splitting-work-arpit-jain-ebeif) | None | Planned | |
| 7 | R2 | How do you write prompts the customer's security team will sign off? | What must the prompts never do in this business? | Role, task and context prompts; chain-of-thought; reviewable prompt libraries | None | No published article on prompt design | Planned | |
| 8 | H6 / R2 | How do you make answers point to the customer's own documents? | Can the customer check every answer against its source? | Document ingestion, hybrid search, reranking, evidence-grounded answers, access filters | #JustAddRAG: [What does your AI say when it doesn't know?](https://www.linkedin.com/pulse/5-what-does-your-ai-say-when-doesnt-know-arpit-jain-wr5bf) | None | Planned | |
| 9 | R1 | Fine-tune, retrieve or prompt: which fits the customer's problem? | Does the customer need new knowledge, new behaviour, or both? | Fine-tuning (LoRA) against retrieval and prompting, and the cost of each | Explain It Like Hello World: [How Do Embeddings Know "King" Is Close to "Queen"?](https://www.linkedin.com/pulse/12-how-do-embeddings-know-king-close-queen-arpit-jain-a5xuf) | No published article on fine-tuning | Planned | |
| 10 | H7 | What happens when an agent stops halfway through the customer's job, and who steers it? | Who approves a step, and where does the job resume? | Durable workflow state, checkpoints, human approvals, operator controls | #BeyondJustRAG: [The Claim Was Filed. The Receipts Weren't Attached.](https://www.linkedin.com/pulse/4-claim-filed-receipts-werent-attached-jobs-stop-halfway-arpit-jain-ki3vf) | MCP, memory and agent harness series not published | Planned | |
| 11 | R3 | Who decides when several agents work on the customer's case? | Which agent owns which part of the customer's case? | Autonomy vs orchestration, multi-agent patterns | None | Multi-agent and agentic RAG series not published | Planned | |
| 12 | R3 | How do you test the customer's assistant before a stranger does? | How could someone misuse this against the customer? | Bias, adversarial prompts, attack and defence, red-teaming for the customer's use case | #JustTellItNot: [What If a Customer Tries to Trick It?](https://www.linkedin.com/pulse/4-what-customer-tries-trick-red-teaming-arpit-jain-m7l5f) | None | Planned | |
| 13 | H8 / R4 | How do you show the customer it is good enough, and what it will cost them? | What quality and cost are acceptable, and who signs? | Evaluation datasets, failure analysis, judge calibration, model comparison, cost and latency, release gates | #JustAddRAG: [How many questions did you test before saying "it works"?](https://www.linkedin.com/pulse/9-how-many-questions-did-you-test-before-saying-works-arpit-jain-vrmqf) and [A few cents per question: so why is finance calling?](https://www.linkedin.com/pulse/10-few-cents-per-question-so-why-finance-calling-cost-arpit-jain-bqppf/) | None | Planned | |
| 14 | H9 / R4 | Who at the customer may do what, and can you prove it later? | Who is accountable for each decision the system makes? | Enterprise identity, authorisation, privacy, risk frameworks, safety policies, audit evidence | #JustAddRAG: [Can the intern ask your AI about the CEO's salary?](https://www.linkedin.com/pulse/8-can-intern-ask-your-ai-ceos-salary-arpit-jain-7m9zf) and #JustTellItNot: [What If Your Guardrails Lock Out Your Own Team?](https://www.linkedin.com/pulse/5-what-your-guardrails-lock-out-own-team-staff-exceptions-arpit-jain-sqgrf) | None | Planned | |
| 15 | H10 / R2 | Where should it run in the customer's cloud, and who restarts it at 2 am? | Which cloud and network may the customer's data touch? | Deployment topologies, containers, secrets, networking, release delivery (R: cloud basics, Docker, serverless) | #JustAddRAG: [It's fast in the demo, so why are users clicking twice?](https://www.linkedin.com/pulse/11-its-fast-demo-so-why-users-clicking-twice-performance-arpit-jain-zvcsf) | AI gateway series not published | Planned | |
| 16 | H11 | How does the customer know it is working on a Tuesday afternoon? | Who is told first when it degrades? | End-to-end telemetry, service-level objectives, capacity tests, failure diagnosis, incident recovery | #JustAddRAG: [When your AI gives a wrong answer, can you tell why?](https://www.linkedin.com/pulse/13-when-your-ai-gives-wrong-answer-can-you-tell-why-arpit-jain-m4kff) | None | Planned | |
| 17 | H12 | How do you run a pilot with real users without betting the customer's business? | What does the customer's team need to see before they switch over? | User acceptance tests, pilot design, migration readiness, cutover, rollback | None | "It worked in the demo" series not published | Planned | |
| 18 | H13 | What does the customer's team need to run this without you? | Who on the customer's side owns it after you leave? | Operational handover, measured business value, reusable assets, feedback to the product | None | No published article on handover | Planned | |
| 19 | R4 | Which AI bets should the customer make first, and how do you score the risk? | Which problem is worth the money first? | Stakeholder mapping, KPI alignment, AI roadmap per function, risk scoring, case studies, portfolio artefacts | None | AI transformation series not published | Planned | |
| 20 | Finale | Is it ready for the customer, or only for the demo? | Would the customer accept this and keep using it? | Readiness checklist; capstone readout of discovery, working system, evaluation, operations and measured value (H capstone; R capstone plan) | Pre-reads: the five in the curtain raiser | None | Planned | |

## Red flags to resolve before writing

These topics have no published LinkedIn article to point readers to yet. Each write-up in these weeks either needs its own explanation or a link to a series that is published first.

- Prompt design (week 7) and handover (week 18): no published article.
- Architecture, API contracts and PoV to PoC to MVP (weeks 2 and 3): no published article.
- Fine-tuning (week 9): no published article.
- Multi-agent and agentic RAG (week 11): series not published.
- MCP, memory, agent harness (week 10): series not published.
- AI gateway (week 15): series not published.
- "It worked in the demo" (week 17): series not published.
- AI transformation (week 19): series not published.

## After each publish

- Mark the row **Published** with the date, and add the LinkedIn link.
- Post the series index as the first comment, then pin it.
- Update the pinned index on write-up 1.
