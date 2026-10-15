# Course plan: from LinkedIn series to an edtech course

Every LinkedIn write-up doubles as a course lesson. LinkedIn gets the short version (a 15-second post, a 2-minute article). The course gets the full version, built from the same lesson.

## Course structure

| Course level | Comes from | Example |
|---|---|---|
| **Course** | The whole roadmap | "Building AI systems that work in the real world" |
| **Part** | An act | Part 1: Make it work |
| **Module** | A series | Module 1: Just add RAG |
| **Lesson** | A write-up | Lesson 1.3: Chunking |
| **Project** | A series' running example | Passport assistant (Module 1), expense-claims agent (Module 2) |
| **Capstone** | The finale checklists | Score and fix a real AI project end to end |

| Part | Modules |
|---|---|
| **1. Make it work** | 1 Just add RAG · 2 From answers to actions |
| **2. Make it trustworthy** | 3 Rules · 4 Guardrails · 5 Evals · 6 Observability |
| **3. Make it real** | 7 Demo to production · 8 Cost · 9 AI transformation |
| **4. Make it bigger** | 10 AI gateway · 11 MCP · 12 Memory · 13 Knowledge graph · 14 Agentic RAG · 15 Multi-agent · 16 Agent harness |

## What every lesson needs

Each write-up gets a **course companion file** next to it: `NN-slug.course.md`. It's never posted on LinkedIn.

| Section | What goes in it | Source |
|---|---|---|
| **Learning objective** | One line: "After this lesson, you can..." | New |
| **The story** | The 2-minute LinkedIn article, as the lesson intro | The article |
| **Deep dive** | The full explanation the article had to cut, about 800-1,200 words | Drafts and research |
| **Hands-on lab** | A short exercise on the module's project, with real code | Running example repo |
| **Quiz** | 3 to 5 questions with answers | New |
| **Checklist line** | The one question this lesson adds to the module's finale checklist | The finale |
| **Glossary** | The "Words to know" | The article |
| **Further reading** | Original sources | The references |
| **Reader questions** | Good questions and answers from LinkedIn comments | Comments |

## Projects (one per module)

- **Module 1:** the passport assistant (PaperMind): upload, OCR, chunking, retrieval, grounding, permissions, evals, cost.
- **Module 2:** the expense-claims agent: messy receipts to exact data, safe retries, half-done jobs, loops, workflow vs agent, testing.
- Later modules: their own running example, built as a small lab project.

Labs live in a separate code repository so learners can clone and run them.

## Writing rules that keep the course possible

1. **Original only:** every diagram and example is mine; facts cite their sources. No copied slides or text.
2. **One running example per series:** it becomes that module's project.
3. **Real, runnable demos:** every lesson shows something real, which becomes the lab.
4. **Consistent shape:** the same sections in every article, so lessons line up.
5. **Unique topics:** no lesson repeats another, so the course has no duplicates.
6. **Capture extras as you write:** anything cut from the 2-minute article goes into the course companion, not the bin.

## Status

| Module | Lessons | Companions written |
|---|---|---|
| 1 Just add RAG | 15, published | 0 of 15 (to be backfilled from the drafts and the master article) |
| 2 From answers to actions | 8, planned | 0 of 8 (write each companion alongside its article) |
| 3 to 16 | planned | none yet |
