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

## Running example (fictional): DabbaNow

**DabbaNow** is a made-up home-cooked tiffin delivery startup in Pune: 40 home cooks, 3,000 office lunches a day, a small tech team. Every objective is shown inside one part of DabbaNow, so the series follows one company end to end. It deliberately doesn't reuse the examples from any course material.

| DabbaNow part | What it is | Covers the exam's scenarios on |
|---|---|---|
| **Lunch-help agent** | A support agent for missed or wrong tiffins, wallet credits and subscriptions, with escalation to the ops team | Customer support agents |
| **Menu research team** | A coordinator with helpers that research ingredient prices, nutrition and supplier reviews for next week's menu | Multi-agent research |
| **Supplier paperwork** | Pulling clean data from supplier bills and food-safety licences | Structured data extraction |
| **The tech team's Claude Code setup** | How the 6-person team uses Claude Code on the DabbaNow app | Code generation, developer productivity |
| **Pull-request reviews in CI** | Automated reviews and tests on every pull request | Claude Code in CI/CD |

## Planned write-ups

| # | Objective | Title | DabbaNow moment | Status |
|---|---|---|---|---|
| 0 | Curtain raiser | Can You Pass an Architect Exam One Lunchbox at a Time? | Meet DabbaNow, and why the exam tests judgement, not trivia | Planned |
| **Domain 1** | **Agentic architecture and orchestration (27%)** | | | |
| 1 | 1.1 Agentic loops | How Does an Agent Know When to Stop? | The lunch-help agent checks a delivery, credits the wallet, and must know it's finished | Planned |
| 2 | 1.2 Coordinator and subagents | One Coordinator, Three Helpers: Who Plans Next Week's Menu? | Prices, nutrition and reviews researched by separate helpers | Planned |
| 3 | 1.3 Subagent context passing | The Helper Never Saw the Brief | The nutrition helper doesn't know the menu is for diabetics | Planned |
| 4 | 1.4 Enforcement and handoffs | The Prompt Said "Check the Account First". The Agent Didn't. | A credit given before the customer was verified | Planned |
| 5 | 1.5 Agent SDK hooks | Who Checks the Agent Before It Presses Send? | A hook blocks credits above ₹500 and masks phone numbers | Planned |
| 6 | 1.6 Task decomposition | One Big Ask or Five Small Ones? | "Plan October's menu" vs a step-by-step plan | Planned |
| 7 | 1.7 Session state | Pick Up Where You Left Off, or Try Two Ideas at Once? | Resuming yesterday's menu research; forking to test a veg-only week | Planned |
| **Domain 2** | **Tool design and MCP (18%)** | | | |
| 8 | 2.1 Tool interfaces | Two Tools, Nearly the Same Name. Guess Which One It Picked. | get_tiffin vs fetch_tiffin_status | Planned |
| 9 | 2.2 Structured errors | "Something Went Wrong" Tells the Agent Nothing | Kitchen system busy vs order not found vs not allowed | Planned |
| 10 | 2.3 Tool distribution and tool_choice | Should Every Agent Get Every Tool? | The research helper accidentally holds the "issue credit" tool | Planned |
| 11 | 2.4 MCP integration | Plugging the Kitchen Into Claude | An MCP server for the cooks' daily capacity | Planned |
| 12 | 2.5 Built-in tools | Read, Grep, Glob or Edit: Which Tool for Which Job? | Finding every place the delivery fee is calculated | Planned |
| **Domain 3** | **Claude Code configuration and workflows (20%)** | | | |
| 13 | 3.1 CLAUDE.md | Stop Explaining the Codebase Every Morning | Team conventions, written once | Planned |
| 14 | 3.2 Slash commands and skills | The Release Checklist Everyone Forgets | A /release skill for the Friday deploy | Planned |
| 15 | 3.3 Path-specific rules | Payment Rules for Payment Files Only | Stricter rules that load only in the wallet code | Planned |
| 16 | 3.4 Plan mode vs direct execution | Plan First, or Just Build It? | Adding subscriptions vs fixing a typo | Planned |
| 17 | 3.5 Iterative refinement | The First Draft Was Fine. The Third Was Right. | Tests first, then code; Claude asks the questions | Planned |
| 18 | 3.6 Claude Code in CI/CD | The Pull-Request Reviewer That Never Sleeps | Automated review and tests on every pull request | Planned |
| **Domain 4** | **Prompt engineering and structured output (20%)** | | | |
| 19 | 4.1 Explicit criteria | 40 Comments on One Pull Request | A vague review prompt vs clear criteria and severity | Planned |
| 20 | 4.2 Few-shot prompting | Show It Three Examples, Not Thirty Rules | Classifying customer complaints consistently | Planned |
| 21 | 4.3 Structured output with tools | From a Crumpled Supplier Bill to Clean JSON | Extracting vegetable-supplier bills | Planned |
| 22 | 4.4 Validation and retry loops | The JSON Was Valid. The Total Was Wrong. | Feeding the error back for a second try | Planned |
| 23 | 4.5 Batch processing | 10,000 Reviews by Morning, at a Lower Price | Overnight analysis of customer reviews | Planned |
| 24 | 4.6 Multi-pass review | Why the Writer Shouldn't Check Its Own Work | Independent review of a big code change | Planned |
| **Domain 5** | **Context management and reliability (15%)** | | | |
| 25 | 5.1 Conversation context | Forty Messages In, It Forgot the Peanut Allergy | Keeping key facts pinned in a long chat | Planned |
| 26 | 5.2 Escalation and ambiguity | "Let Me Talk to a Person." Now What? | Escalating on request, on risk, and when no rule fits | Planned |
| 27 | 5.3 Error propagation | One Helper Failed. The Report Said "All Good". | The price helper timed out; the menu went out anyway | Planned |
| 28 | 5.4 Large-codebase exploration | Lost in 3,000 Files | Finding how a delivery slot is assigned | Planned |
| 29 | 5.5 Human review and confidence | Which Answers Need a Human Look? | Routing low-confidence bill extractions to finance | Planned |
| 30 | 5.6 Provenance | Two Sources, Two Prices. Which One Wins? | Conflicting onion prices in the research report | Planned |
| 31 | Finale | Exam Day: 30 Objectives on One Page | The whole DabbaNow system, and a revision checklist | Planned |

## Format for every write-up

- **One objective per write-up**, named at the top: "Exam objective 1.4: ..." (in my own words).
- **Length:** post at most 15 seconds (about 55 words), article at most 2 minutes (about 400 words).
- **Shape:** a DabbaNow moment that goes wrong → why → the right approach in plain words → one everyday analogy → 3 words to know → **"What the exam is really testing"** (one or two lines) → **one practice question** in my own words, answer at the end.
- **Course companion** (`NN-slug.course.md`): deeper notes, code sketch, 3 more practice questions, links to Anthropic's official documentation.
- **Links:** each write-up links to the related vendor-neutral series where one exists (for example 1.4 → Series 3, code decides).
- **Sources:** the official exam guide and Anthropic's documentation only. Course slides are used only to check coverage; no slide text, diagrams or examples are reused.
- **No affiliation:** every post says it isn't an official Anthropic resource.
