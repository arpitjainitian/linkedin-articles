# AI Engineering Q&A: one question per post

A separate, ongoing series. Each post takes **one** real-world AI engineering question (the kind asked in interviews and design reviews) and answers it in plain words, with a passport-style example and a short "what I'd say in the room" answer.

Questions are collected from posts and discussions shared over time. They are rephrased in my own words, and each source is credited below.

| # | Question | Topic | Level | Related write-up | Source | Status |
|---|---|---|---|---|---|---|
| 1 | Your AI agent keeps calling the same tool and never reaches a final answer. What do you check first, and how do you stop it happening again? | Agent loops, stop conditions | L4 | Series 16: Let's make it agentic | S1 | Planned |
| 2 | Your agent gives different answers to the same question, and nothing in the code changed. What could cause it, and how do you debug it? | Non-determinism, model changes | L3 | #JustAddRAG: model changes, observability | S1 | Planned |
| 3 | How do you know your agent is actually getting better? Which metrics go beyond "it seems to work"? | Evals | L3 | #JustAddRAG: evals | S1 | Planned |
| 4 | A task needs retrieval, planning, reasoning and several tool calls. Single agent, multi-agent, or orchestrator, and why? | Agent architecture | L5 | Series 18: multi-agent systems | S1 | Planned |
| 5 | Your agent works for 100 users. Now it needs 100,000. What breaks first: latency, cost, memory or tool reliability? How would you redesign? | Scale, cost, performance | L5 | #JustAddRAG: cost, performance | S1 | Planned |

## Sources

- **S1:** LinkedIn post by Naresh Edagotti, "I had LangGraph on my resume. The interviewer had 5 questions." https://lnkd.in/p/dZH4zR3h

## Rules for this series

- One question per post. No fixed schedule.
- Questions rephrased in my words; source credited in the post.
- Answer in plain words, with one concrete example, then a 3-line "interview answer".
- Link back to the related #JustAddRAG write-up where one exists.
