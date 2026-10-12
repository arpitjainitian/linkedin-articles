# Series 21: AI system design (one question per post)

An ongoing series. Each post takes **one** AI system design question (the kind asked in architect interviews and design reviews) about AI that already works in a demo and now has to work in production: cost, speed, reliability, safety and scale.

Questions are rephrased in my own words, and each source is credited below.

| # | Question | Topic | Level | Related write-up | Source | Status |
|---|---|---|---|---|---|---|
| 1 | You have an AI agent in production. Its answers are accurate, but token usage keeps climbing every week. How would you fix it? | Token cost, context growth, agent loops, caching, model routing | L3 | #JustAddRAG write-up 10 (cost); series 5 (few cents per call) | S1 | [Drafted](01-token-usage-climbing.md) |
| 2 | Your AI agent keeps calling the same tool and never reaches a final answer. What do you check first, and how do you stop it happening again? | Agent loops, stop conditions | L4 | Series 16: Let's make it agentic | S2 | Planned |
| 3 | Your agent gives different answers to the same question, and nothing in the code changed. What could cause it, and how do you debug it? | Non-determinism, model changes | L3 | #JustAddRAG: model changes, observability | S2 | Planned |
| 4 | How do you know your agent is actually getting better? Which metrics go beyond "it seems to work"? | Evals | L3 | #JustAddRAG: evals | S2 | Planned |
| 5 | A task needs retrieval, planning, reasoning and several tool calls. Single agent, multi-agent, or orchestrator, and why? | Agent architecture | L5 | Series 18: multi-agent systems | S2 | Planned |
| 6 | Your agent works for 100 users. Now it needs 100,000. What breaks first: latency, cost, memory or tool reliability? How would you redesign? | Scale, cost, performance | L5 | #JustAddRAG: cost, performance | S2 | Planned |

## Sources

- **S1:** shared directly by Arpit (no link).
- **S2:** LinkedIn post by Naresh Edagotti, "I had LangGraph on my resume. The interviewer had 5 questions." https://lnkd.in/p/dZH4zR3h

## Rules for this series

- One question per post. No fixed schedule.
- Questions rephrased in my words; source credited in the post.
- Each answer covers: what's really being asked, how to find the cause, the fixes, the trade-off, how to stop it coming back, a simple diagram idea, and a 3-line "what I'd say in the room" answer.
- Accuracy is a hard constraint: every fix is checked with evals before and after.
- Link to a related AI write-up where one exists.
