# Forward Deployed: the FDE series

**Hashtag:** #ForwardDeployed

**Track:** a parallel track, alongside the AI engineering series (1 to 16). It follows the job of a Forward Deployed Engineer (FDE), not the AI engineering order. It is listed as section 6 of the [ROADMAP.md](https://github.com/arpitjainitian/linkedin-articles/blob/main/ROADMAP.md) in the [linkedin-articles repo](https://github.com/arpitjainitian/linkedin-articles/tree/main).

**The promise:** the demo is the easy part. This series follows the FDE's job from the first customer meeting to the handover, one week at a time.

**Running example:** a wholesale distributor's order desk. Customers email their orders, the desk checks stock and prices, and an assistant drafts the replies. Every write-up uses this same desk.

A write-up is marked **Published** only once it is live on LinkedIn.

## Planned write-ups

| # | Week | Title | Topic | Status | LinkedIn |
|---|---|---|---|---|---|
| 1 | Curtain raiser | [Why does the customer's Monday matter more than your demo?](01-curtain-raiser.md) | The FDE job and its three hats | Draft for review | |
| 2 | 1 | What should you learn from the customer before you build anything? | Customer discovery and value definition | Planned | |
| 3 | 2 | How do you turn a customer's rules into a system you can test? | Solution and service foundation: architecture, API contracts, tests | Planned | |
| 4 | 3 | Where does the customer's data hide, and which copy is true? | Data estate and canonical model | Planned | |
| 5 | 4 | What happens when two of the customer's systems disagree? | Integrations and event processing | Planned | |
| 6 | 5 | How do you let a model use tools without letting it break things? | LLM interaction and safe tool execution | Planned | |
| 7 | 6 | How do you make answers point to the customer's own documents? | Enterprise retrieval and grounding | Planned | |
| 8 | 7 | What happens when an agent stops halfway through a job, and who steers it? | Durable agents and operator control | Planned | |
| 9 | 8 | How do you know it is good enough, and what will it cost? | System evaluation and model economics | Planned | |
| 10 | 9 | Who is allowed to do what, and can you prove it later? | Identity, security and governance | Planned | |
| 11 | 10 | Where should it run, and who restarts it at 2 am? | Deployment and runtime architecture | Planned | |
| 12 | 11 | How do you know it is working on a Tuesday afternoon? | Observability and operational reliability | Planned | |
| 13 | 12 | How do you run a pilot without betting the business on it? | Customer pilot and cutover | Planned | |
| 14 | 13 | What does the customer need to run this without you? | Handover and engagement defence | Planned | |
| 15 | Finale | So, are you ready to deploy, or only to demo? | The readiness checklist and the capstone readout | Planned | |

## Where it overlaps

The rule for the whole programme: a topic is covered once. Where a write-up here touches an existing series, it links to that series for the basics and stays on the customer side.

- Week 5 (tools): [Beyond Just RAG: from answers to actions](../02-answers-to-actions/README.md) covers how tools and actions work.
- Week 6 (retrieval): [Just add RAG](../01-just-add-rag/README.md) covers the basics of retrieval.
- Week 8 (evaluation and cost): [The prompt works, ship it](../05-the-prompt-works-ship-it/README.md) and [A few cents between friends](../08-few-cents-per-call/README.md).
- Week 9 (governance): [Just tell it not to](../04-guardrails/README.md).
- Week 11 (observability): [We'll know when it breaks](../06-observability/README.md).
- Week 12 (pilot and cutover): [It worked in the demo](../07-poc-to-production/README.md).

## After each publish

- Mark the row **Published** with the date, and add the LinkedIn link.
- Post the series index as the first comment, then pin it.
- Update the pinned index on write-up 1.
