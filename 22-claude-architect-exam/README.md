# Series 22: Claude Architect, One Objective at a Time

**What it is:** a study series for the **Claude Certified Architect – Foundations** exam (CCAR-F). One write-up per exam objective (task statement), 30 in all, plus a curtain raiser and an exam-day finale.

**Who it's for:** engineers and architects preparing for the exam, and anyone building with Claude who wants the "why" behind each practice. Also my own study notes.

**Level:** L3 to L4. Written so anyone with basic AI-app knowledge can follow it.

**Hashtags:** #ClaudeArchitectPrep (series tag) + #ClaudeCertifiedArchitect (check both before launch).

## The exam, in one table

| | |
|---|---|
| Exam code | CCAR-F |
| Questions | 60, multiple choice and multiple response |
| Format | 4 scenarios, drawn at random from a bank of 6 |
| Time | 120 minutes |
| Passing score | 720 (scale 100 to 1,000) |
| Domains and weights | 1 Agentic architecture and orchestration 27% · 2 Tool design and MCP 18% · 3 Claude Code configuration and workflows 20% · 4 Prompt engineering and structured output 20% · 5 Context management and reliability 15% |

Source: the official exam guide. Check Anthropic's certification pages for the latest version before the exam.

## Running example (fictional): TailWag Pet Care

**TailWag** is a made-up pet-care company: a network of 60 vet clinics plus a pet-food subscription service, with a small tech team. Every objective is shown inside one part of TailWag, so the series follows one company end to end. It's global (no country-specific details), and it deliberately doesn't reuse examples from any course material.

| TailWag part | What it is | Covers the exam's scenarios on |
|---|---|---|
| **Pet-parent help agent** | A support agent for appointments, prescription refills, missed deliveries, subscription changes and credits, with escalation to clinic staff | Customer support agents |
| **Food research team** | A coordinator with helpers that research ingredients, vet guidelines and owner reviews before TailWag launches a new food line | Multi-agent research |
| **Clinic paperwork** | Pulling clean data from lab reports, vaccination certificates and supplier invoices | Structured data extraction |
| **The tech team's Claude Code setup** | How the 6-person team uses Claude Code on the TailWag apps | Code generation, developer productivity |
| **Pull-request reviews in CI** | Automated reviews and tests on every pull request | Claude Code in CI/CD |

## Planned write-ups

| # | Objective | Title | TailWag moment | Status |
|---|---|---|---|---|
| 0 | Curtain raiser | Can You Pass an Architect Exam One Pet at a Time? | Meet TailWag, and why the exam tests judgement, not trivia | Planned |
| **Domain 1** | **Agentic architecture and orchestration (27%)** | | | |
| 1 | 1.1 Agentic loops | How Does an Agent Know When to Stop? | The help agent checks a missed delivery, issues a credit, and must know it's finished | Planned |
| 2 | 1.2 Coordinator and subagents | One Coordinator, Three Helpers: Who Researches the New Dog Food? | Ingredients, vet guidelines and reviews researched by separate helpers | Planned |
| 3 | 1.3 Subagent context passing | The Helper Never Saw the Brief | The guidelines helper doesn't know the food is for senior cats | Planned |
| 4 | 1.4 Enforcement and handoffs | The Prompt Said "Check the Account First". The Agent Didn't. | A prescription refill sent before the pet's record was checked | Planned |
| 5 | 1.5 Agent SDK hooks | Who Checks the Agent Before It Presses Send? | A hook blocks credits above a limit and masks owners' phone numbers | Planned |
| 6 | 1.6 Task decomposition | One Big Ask or Five Small Ones? | "Research the new food line" vs a step-by-step plan | Planned |
| 7 | 1.7 Session state | Pick Up Where You Left Off, or Try Two Ideas at Once? | Resuming yesterday's research; forking to compare grain-free and regular | Planned |
| **Domain 2** | **Tool design and MCP (18%)** | | | |
| 8 | 2.1 Tool interfaces | Two Tools, Nearly the Same Name. Guess Which One It Picked. | get_pet vs fetch_pet_record | Planned |
| 9 | 2.2 Structured errors | "Something Went Wrong" Tells the Agent Nothing | Clinic system busy vs pet not found vs not allowed | Planned |
| 10 | 2.3 Tool distribution and tool_choice | Should Every Agent Get Every Tool? | The research helper accidentally holds the "issue credit" tool | Planned |
| 11 | 2.4 MCP integration | Plugging the Clinics Into Claude | An MCP server for appointment slots across 60 clinics | Planned |
| 12 | 2.5 Built-in tools | Read, Grep, Glob or Edit: Which Tool for Which Job? | Finding every place the delivery fee is calculated | Planned |
| **Domain 3** | **Claude Code configuration and workflows (20%)** | | | |
| 13 | 3.1 CLAUDE.md | Stop Explaining the Codebase Every Morning | Team conventions, written once | Planned |
| 14 | 3.2 Slash commands and skills | The Release Checklist Everyone Forgets | A /release skill for the Friday deploy | Planned |
| 15 | 3.3 Path-specific rules | Payment Rules for Payment Files Only | Stricter rules that load only in the billing code | Planned |
| 16 | 3.4 Plan mode vs direct execution | Plan First, or Just Build It? | Adding multi-pet households vs fixing a typo | Planned |
| 17 | 3.5 Iterative refinement | The First Draft Was Fine. The Third Was Right. | Tests first, then code; Claude asks the questions | Planned |
| 18 | 3.6 Claude Code in CI/CD | The Pull-Request Reviewer That Never Sleeps | Automated review and tests on every pull request | Planned |
| **Domain 4** | **Prompt engineering and structured output (20%)** | | | |
| 19 | 4.1 Explicit criteria | 40 Comments on One Pull Request | A vague review prompt vs clear criteria and severity | Planned |
| 20 | 4.2 Few-shot prompting | Show It Three Examples, Not Thirty Rules | Sorting owner messages consistently: urgent, routine, billing | Planned |
| 21 | 4.3 Structured output with tools | From a Blurry Lab Report to Clean JSON | Extracting blood-test results from clinic PDFs | Planned |
| 22 | 4.4 Validation and retry loops | The JSON Was Valid. The Dose Was Wrong. | Feeding the error back for a second try | Planned |
| 23 | 4.5 Batch processing | 10,000 Reviews by Morning, at a Lower Price | Overnight analysis of owner reviews | Planned |
| 24 | 4.6 Multi-pass review | Why the Writer Shouldn't Check Its Own Work | Independent review of a big code change | Planned |
| **Domain 5** | **Context management and reliability (15%)** | | | |
| 25 | 5.1 Conversation context | Forty Messages In, It Forgot the Dog's Chicken Allergy | Keeping key facts pinned in a long chat | Planned |
| 26 | 5.2 Escalation and ambiguity | "Let Me Talk to a Vet." Now What? | Escalating on request, on risk, and when no rule fits; two pets named Max | Planned |
| 27 | 5.3 Error propagation | One Helper Failed. The Report Said "All Good". | The reviews helper timed out; the launch report went out anyway | Planned |
| 28 | 5.4 Large-codebase exploration | Lost in 3,000 Files | Finding how appointment reminders are scheduled | Planned |
| 29 | 5.5 Human review and confidence | Which Answers Need a Human Look? | Routing low-confidence lab-report extractions to a vet nurse | Planned |
| 30 | 5.6 Provenance | Two Sources, Two Protein Levels. Which One Wins? | Conflicting ingredient data in the research report | Planned |
| 31 | Finale | Exam Day: 30 Objectives on One Page | The whole TailWag system, and a revision checklist | Planned |

## Format for every write-up

- **One objective per write-up**, named at the top: "Exam objective 1.4: ..." (in my own words).
- **Length:** post at most 15 seconds (about 55 words), article at most 2 minutes (about 400 words).
- **Shape:** a TailWag moment that goes wrong → why → the right approach in plain words → one everyday analogy → 3 words to know → **"What the exam is really testing"** (one or two lines) → **one practice question** in my own words, answer at the end.
- **Course companion** (`NN-slug.course.md`): deeper notes, code sketch, 3 more practice questions, links to Anthropic's official documentation.
- **Links:** each write-up links to the related vendor-neutral series where one exists (for example 1.4 → Series 3, code decides).
- **Sources:** the official exam guide and Anthropic's documentation only. Course slides are used only to check coverage; no slide text, diagrams or examples are reused.
- **No affiliation:** every post says it isn't an official Anthropic resource.
