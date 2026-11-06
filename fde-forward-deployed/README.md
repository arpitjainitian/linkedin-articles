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
| 2 | H1 / R1 | [What should you learn from the customer before you build anything?](02-learn-before-you-build.md) | What would make this worth paying for? | Customer discovery, workflow mapping, value and baselines (R: AI for enterprises, PoV to PoC to MVP) | None | No published article on PoV to PoC to MVP | Draft for review | |
| 3 | H2 | [How do you turn the customer's rules into something you can test?](03-rules-you-can-test.md) | Which rules must the system follow, and how will we know it does? | Solution and service foundation: architecture, trust boundaries, API contracts, tests | None | No published article on architecture or API contracts | Draft for review | |
| 4 | H3 / R1 | [Where does the customer's data hide, and which copy is true?](04-where-the-data-hides.md) | Which system is the record of truth? | Data estate, canonical model, data quality (R: pipelines, metrics, visualisation) | #JustAddRAG: [Why can't your AI read a PDF that a 10-year-old can?](https://www.linkedin.com/pulse/why-cant-your-ai-read-pdf-10-year-old-can-arpit-jain-fimif/) | None | Draft for review | |
| 5 | H4 | [What happens when two of the customer's systems disagree?](05-when-systems-disagree.md) | What happens to an order when the systems disagree? | Integrations, retries, idempotency, events and replay | #BeyondJustRAG: [It Filed the Same Claim Twice](https://www.linkedin.com/pulse/3-filed-same-claim-twice-safe-retries-arpit-jain-7ttrf) | None | Draft for review | |
| 6 | H5 | [How do you let a model act in the customer's systems without breaking their records?](06-model-that-acts.md) | Which actions may the assistant take on its own? | Model interfaces, structured outputs, schema checks, controlled tool execution | Just put the rules in the prompt: [Code Decides. The AI Explains.](https://www.linkedin.com/pulse/2-code-decides-ai-explains-splitting-work-arpit-jain-ebeif) | None | Draft for review | |
| 7 | R2 | [How do you write prompts the customer's security team will sign off?](07-prompts-security-signs.md) | What must the prompts never do in this business? | Role, task and context prompts; chain-of-thought; reviewable prompt libraries | None | No published article on prompt design | Draft for review | |
| 8 | H6 / R2 | [How do you make answers point to the customer's own documents?](08-answers-with-sources.md) | Can the customer check every answer against its source? | Document ingestion, hybrid search, reranking, evidence-grounded answers, access filters | #JustAddRAG: [What does your AI say when it doesn't know?](https://www.linkedin.com/pulse/5-what-does-your-ai-say-when-doesnt-know-arpit-jain-wr5bf) | None | Draft for review | |
| 9 | R1 | [Fine-tune, retrieve or prompt: which fits the customer's problem?](09-fine-tune-retrieve-prompt.md) | Does the customer need new knowledge, new behaviour, or both? | Fine-tuning (LoRA) against retrieval and prompting, and the cost of each | Explain It Like Hello World: [How Do Embeddings Know "King" Is Close to "Queen"?](https://www.linkedin.com/pulse/12-how-do-embeddings-know-king-close-queen-arpit-jain-a5xuf) | No published article on fine-tuning | Draft for review | |
| 10 | H7 | [What happens when an agent stops halfway through the customer's job, and who steers it?](10-agent-halfway.md) | Who approves a step, and where does the job resume? | Durable workflow state, checkpoints, human approvals, operator controls | #BeyondJustRAG: [The Claim Was Filed. The Receipts Weren't Attached.](https://www.linkedin.com/pulse/4-claim-filed-receipts-werent-attached-jobs-stop-halfway-arpit-jain-ki3vf) | MCP, memory and agent harness series not published | Draft for review | |
| 11 | R3 | [Who decides when several agents work on the customer's case?](11-several-agents.md) | Which agent owns which part of the customer's case? | Autonomy vs orchestration, multi-agent patterns | None | Multi-agent and agentic RAG series not published | Draft for review | |
| 12 | R3 | [How do you test the customer's assistant before a stranger does?](12-test-before-stranger.md) | How could someone misuse this against the customer? | Bias, adversarial prompts, attack and defence, red-teaming for the customer's use case | #JustTellItNot: [What If a Customer Tries to Trick It?](https://www.linkedin.com/pulse/4-what-customer-tries-trick-red-teaming-arpit-jain-m7l5f) | None | Draft for review | |
| 13 | H8 / R4 | [How do you show the customer it is good enough, and what it will cost them?](13-good-enough-and-cost.md) | What quality and cost are acceptable, and who signs? | Evaluation datasets, failure analysis, judge calibration, model comparison, cost and latency, release gates | #JustAddRAG: [How many questions did you test before saying "it works"?](https://www.linkedin.com/pulse/9-how-many-questions-did-you-test-before-saying-works-arpit-jain-vrmqf) and [A few cents per question: so why is finance calling?](https://www.linkedin.com/pulse/10-few-cents-per-question-so-why-finance-calling-cost-arpit-jain-bqppf/) | None | Draft for review | |
| 14 | H9 / R4 | [Who at the customer may do what, and can you prove it later?](14-who-may-do-what.md) | Who is accountable for each decision the system makes? | Enterprise identity, authorisation, privacy, risk frameworks, safety policies, audit evidence | #JustAddRAG: [Can the intern ask your AI about the CEO's salary?](https://www.linkedin.com/pulse/8-can-intern-ask-your-ai-ceos-salary-arpit-jain-7m9zf) and #JustTellItNot: [What If Your Guardrails Lock Out Your Own Team?](https://www.linkedin.com/pulse/5-what-your-guardrails-lock-out-own-team-staff-exceptions-arpit-jain-sqgrf) | None | Draft for review | |
| 15 | H10 / R2 | [Where should it run in the customer's cloud, and who restarts it at 2 am?](15-where-it-runs.md) | Which cloud and network may the customer's data touch? | Deployment topologies, containers, secrets, networking, release delivery (R: cloud basics, Docker, serverless) | #JustAddRAG: [It's fast in the demo, so why are users clicking twice?](https://www.linkedin.com/pulse/11-its-fast-demo-so-why-users-clicking-twice-performance-arpit-jain-zvcsf) | AI gateway series not published | Draft for review | |
| 16 | H11 | [How does the customer know it is working on a Tuesday afternoon?](16-tuesday-afternoon.md) | Who is told first when it degrades? | End-to-end telemetry, service-level objectives, capacity tests, failure diagnosis, incident recovery | #JustAddRAG: [When your AI gives a wrong answer, can you tell why?](https://www.linkedin.com/pulse/13-when-your-ai-gives-wrong-answer-can-you-tell-why-arpit-jain-m4kff) | None | Draft for review | |
| 17 | H12 | [How do you run a pilot with real users without betting the customer's business?](17-pilot-cutover.md) | What does the customer's team need to see before they switch over? | User acceptance tests, pilot design, migration readiness, cutover, rollback | None | "It worked in the demo" series not published | Draft for review | |
| 18 | H13 | [What does the customer's team need to run this without you?](18-run-without-you.md) | Who on the customer's side owns it after you leave? | Operational handover, measured business value, reusable assets, feedback to the product | None | No published article on handover | Draft for review | |
| 19 | R4 | [Which AI bets should the customer make first, and how do you score the risk?](19-which-bet-first.md) | Which problem is worth the money first? | Stakeholder mapping, KPI alignment, AI roadmap per function, risk scoring, case studies, portfolio artefacts | None | AI transformation series not published | Draft for review | |
| 20 | Finale | [Is it ready for the customer, or only for the demo?](20-finale-ready-or-demo.md) | Would the customer accept this and keep using it? | Readiness checklist; capstone readout of discovery, working system, evaluation, operations and measured value (H capstone; R capstone plan) | Pre-reads: the five in the curtain raiser | None | Draft for review | |

## Red flags to resolve before writing

These topics have no published LinkedIn article to point readers to yet. Each write-up in these weeks either needs its own explanation or a link to a series that is published first. Drafts now exist for weeks 7, 9 and 18, but they are not on LinkedIn yet, so those flags stay until they are published.

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
