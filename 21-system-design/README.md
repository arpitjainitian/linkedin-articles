# Series 21: AI system design (one question per post)

An ongoing series. Each post takes **one** AI system design question, the kind asked in AI engineer and architect interviews and in design reviews, and answers it the way you'd answer it in the room.

**The roadmap (new, 23 Oct 2026):** 28 questions in 8 areas. It keeps every topic from the "25 problems that cover most AI interviews" list (S4), merged with the 8 questions already planned here (S1 to S3). Where two questions were the same problem, they became one question (noted in "Merged from").

Questions are rephrased in my own words, and each source is credited below.

**Levels:** L3 = explain the idea clearly. L4 = design and debug it. L5 = design it at scale and defend the trade-offs.

## A. RAG and retrieval

| # | Question | What a strong answer covers | Level | Related write-up | Source | Status |
|---|---|---|---|---|---|---|
| 1 | Design a RAG system for 10 million documents. What breaks as it grows, and how do you redesign? | Offline ingestion (chunk, embed, index), sharding and metadata filters, hybrid search plus reranking, citations, re-indexing time and cost | L5 | #JustAddRAG (retrieval, cost) | S4, S3 (merged from old Q7: 10,000 to 1 million documents) | Planned |
| 2 | Your RAG system gives wrong answers. How do you debug it? | Trace each answer, split the failure into retrieval vs generation, fix the broken stage, prove it on a golden set | L4 | #JustAddRAG 13 (why the answer was wrong) | S4 | Planned |
| 3 | How do you chunk legal contracts? | Chunk by clause using the contract's own numbering, keep the heading path and definitions with each chunk, test on a golden set | L4 | #JustAddRAG (chunking) | S4 | Planned |
| 4 | BM25, dense or hybrid search: when do you use each? | Keyword search for exact terms and IDs, dense for meaning, hybrid with rank fusion when queries mix both; let a golden set decide | L3 | #JustAddRAG (retrieval) | S4 | Planned |
| 5 | You add a reranker. How do you prove it helped? | Retrieve wide and cheap, rerank to a few with a cross-encoder, measure ranking quality and answer quality before and after, and the latency cost | L4 | Series 5 (evals) | S4 | Planned |
| 6 | A question needs facts from 5 different documents. How do you design retrieval and the context so the answer uses all of them? | Query splitting, retrieval per sub-question, dedup, ordering, context budget, checking every part is answered | L4 | Series 13 (knowledge graph), 14 (agentic RAG) | S3 (old Q8) | Planned |

## B. Cost and latency

| # | Question | What a strong answer covers | Level | Related write-up | Source | Status |
|---|---|---|---|---|---|---|
| 7 | Cut LLM cost by 70% without hurting quality. (Or: answers are accurate but token usage keeps climbing.) | Measure where tokens go, fix the growing part, caching, shorter prompts, cheaper model for easy requests, every change gated on evals | L4 | Series 8 (cost) | S4, S1 (merged from old Q1) | [Drafted](07-token-usage-climbing.md) |
| 8 | Users wait too long for the first word of the answer. How do you cut time to first token? | Measure each stage, remove work before the first token: smaller prompts, prompt caching, parallel retrieval, streaming, a warm fast model | L4 | Series 8 (cost) | S4 | Planned |
| 9 | Design a semantic cache, and track whether it's working | Normalise and embed the query, strict similarity threshold, scope keys (user, tenant, version), hit rate and wrong-hit tracking | L4 | Series 8 (cost) | S4 | Planned |
| 10 | Route requests between a cheap model and a smart model | Judge difficulty up front, default to cheap, check the output, escalate failures, measure cost and quality together | L4 | Series 10 (gateway) | S4 | Planned |

## C. Agents and memory

| # | Question | What a strong answer covers | Level | Related write-up | Source | Status |
|---|---|---|---|---|---|---|
| 11 | Build an agent that uses tools reliably | Small set of typed tools, strict input validation, safe retries, clear error results, a step budget | L4 | Series 2 (answers to actions), 11 (MCP) | S4 | Planned |
| 12 | Your agent keeps calling the same tool and never finishes. What do you check first, and how do you stop it happening again? | Detect repeated state, tell the model what already failed, cap steps and cost, hand over instead of retrying forever | L4 | Series 2, write-up 5 (40 times) | S4, S2 (merged from old Q2) | Planned |
| 13 | A task needs retrieval, planning, reasoning and several tool calls. Single agent, multi-agent, or orchestrator? | When one agent is enough, when to split, coordinator and workers, cost and debugging trade-offs | L5 | Series 15 (multi-agent) | S2 (old Q5) | Planned |
| 14 | Design memory for an assistant that runs for months | Recent turns word for word, a rolling summary, a searchable long-term store of facts, and the user's control over what's kept | L5 | Series 12 (memory) | S4 | Planned |

## D. Output quality and evals

| # | Question | What a strong answer covers | Level | Related write-up | Source | Status |
|---|---|---|---|---|---|---|
| 15 | Make LLM output always valid JSON | Native structured output or constrained decoding, schema validation, repair or retry with the error fed back | L3 | Series 2, write-up 2 (exact data) | S4 | Planned |
| 16 | Detect and reduce hallucinations | Ground answers in retrieved sources, require citations, check claims against sources, let the model say "I don't know" | L4 | #JustAddRAG (grounding) | S4 | Planned |
| 17 | Build an eval suite for a customer support bot. How do you know it's actually getting better? | Layers: code checks, a labelled golden set, rubric scoring by a calibrated judge, sampling real traffic; metrics beyond "it seems to work" | L4 | Series 5 (evals) | S4, S2 (merged from old Q4) | Planned |
| 18 | LLM-as-a-judge: how do you make it trustworthy? | Calibrate against human labels, rubrics, swap the order in pairwise tests to remove bias, watch agreement over time | L4 | Series 5 (evals) | S4 | Planned |
| 19 | Same question, different answers, and nothing in the code changed. Why, and how do you debug it? | Sampling, silent model updates, changed retrieval results, prompt or data drift, pinning versions, logging everything | L3 | #JustAddRAG 14 (model changes) | S2 (old Q3) | Planned |

## E. Safety and security

| # | Question | What a strong answer covers | Level | Related write-up | Source | Status |
|---|---|---|---|---|---|---|
| 20 | Block prompt injection in an agent that uses tools | Treat all tool output as untrusted data, least-privilege tools, confirm risky actions, detect injected instructions before they act | L5 | #JustAddRAG (injection), Series 4 (guardrails) | S4 | Planned |
| 21 | Remove personal data before it reaches the model | Detect it at the gateway, swap in stable placeholders, call the model, put the real values back locally | L4 | #JustAddRAG 12 (privacy) | S4 | Planned |

## F. Training and adaptation

| # | Question | What a strong answer covers | Level | Related write-up | Source | Status |
|---|---|---|---|---|---|---|
| 22 | Fine-tuning, RAG or prompting: pick one and defend it | Prompting for behaviour, RAG for knowledge that changes, fine-tuning for style or format at scale; start with the cheapest | L3 | #JustAddRAG | S4 | Planned |
| 23 | Fine-tune a small model with LoRA on 5,000 examples | Clean the data, hold out a test set, sensible LoRA settings, compare with the base model before shipping | L5 | (none yet) | S4 | Planned |

## G. Serving and infrastructure

| # | Question | What a strong answer covers | Level | Related write-up | Source | Status |
|---|---|---|---|---|---|---|
| 24 | Serve an open model at scale | Continuous batching, KV cache management, quantization, how they turn one request per GPU into dozens | L5 | (none yet) | S4 | Planned |
| 25 | Stream answers over SSE, and handle disconnects | Stream tokens as events with IDs, keep the response on the server, let clients resume with Last-Event-ID | L4 | (none yet) | S4 | Planned |
| 26 | Design a ChatGPT-style chat for 1 million daily users. (Or: it works for 100 users; what breaks at 100,000?) | Stateless API with streaming, a queue in front of GPU workers, conversation store plus cache, what breaks first: latency, cost, memory or tools | L5 | Series 7 (demo to production) | S4, S2 (merged from old Q6) | Planned |

## H. Observability and operations

| # | Question | What a strong answer covers | Level | Related write-up | Source | Status |
|---|---|---|---|---|---|---|
| 27 | Trace every step of a multi-agent workflow | One trace ID per request, a span for every agent step, tool call and model call, with prompts, tokens and cost | L4 | Series 6 (observability) | S4 | Planned |
| 28 | A prompt change broke production. How do you roll back? | Prompts as versioned, deployed artifacts, detect with evals and live metrics, switch back in seconds, then fix forward | L4 | #JustAddRAG 14 (model changes), Series 6 | S4 | Planned |

## Sources

- **S1:** shared directly by Arpit (no link).
- **S2:** LinkedIn post by Naresh Edagotti, "I had LangGraph on my resume. The interviewer had 5 questions." https://lnkd.in/p/dZH4zR3h
- **S3:** LinkedIn post "RAG ruined my AI interview" (promoting an AI Engineer Interview Kit, practicai.tech). Its 5 questions were checked against #JustAddRAG on 15 Oct 2026: questions 1-3 are covered, 4 partly, 5 not at all, so old 7 and 8 were added here.
- **S4:** an "AI engineer interview prep" page, "25 problems that cover 95% of AI interviews", shared by Arpit as a screenshot on 23 Oct 2026 (no link). All 25 topics are kept here, rephrased.

## Rules for this series

- One question per post. No fixed schedule.
- Questions rephrased in my words; source credited in the post.
- **Length:** the post takes at most 15 seconds to read (about 55 words); the article at most 2 minutes (about 400 words).
- Each answer covers: what's really being asked, how to find the cause, the fixes, the trade-off, how to stop it coming back, a simple diagram idea, and a 3-line "what I'd say in the room" answer.
- Accuracy is a hard constraint: every fix is checked with evals before and after.
- Link to a related AI write-up where one exists. Where a series already tells the story, the question here gives the interview-style design answer, not the same story again.
