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

## Running example (fictional): ParentPace

**ParentPace** here is an invented coaching company **for parents themselves**: how to stay calm instead of yelling, talk so children listen, set boundaries, share parenting with a partner, and look after their own wellbeing. Parents chat with an AI coach in the app between 1:1 sessions with human coaches. It runs on subscriptions, with courses and booked sessions, and a 6-person tech team. It coaches the parent, never diagnoses anyone, and hands over to people when it matters.

> **Name note:** ParentPace is fictional. A web search (October 2026) found no app or company with this exact name; it was chosen to avoid clashing with existing parenting apps (for example "ParentPace"). Every post still carries a one-line "fictional company" note.

| ParentPace part | What it does | Exam scenario |
|---|---|---|
| **Parent-help agent** | Coaching chats about the parent's own reactions, routines and communication; books 1:1 sessions with human coaches; handles plans and billing; hands over to a human coach (and points to helplines) when a parent is in distress | Customer support agent |
| **Course research team** | A coordinator with helpers that research parenting studies, expert guidance and parent reviews for a new "Calm Parenting" course | Multi-agent research |
| **Intake paperwork** | Turns parent self-assessment forms and coach session notes into a clean parent profile: goals, stress triggers, family setup | Structured data extraction |
| **The tech team's Claude Code setup** | Six engineers building the ParentPace app | Code generation, developer productivity |
| **Pull-request reviews in CI** | Automated reviews and tests on every pull request | Claude Code in CI/CD |

## How many articles, and why

**38 in total: 1 per objective (30), 1 checkpoint per domain (5), a curtain raiser, a mock exam and an exam-day finale.**

- **One article per objective (30).** Every objective has 6 to 10 knowledge and skill points. A 2-minute article can cover all of them if each point gets one line in an "objective map", with the story carrying the 2 or 3 points the exam tests hardest. The course companion goes deep on every point.
- **One checkpoint per domain (5).** After each domain: 6 to 8 scenario questions in the exam's style, with answers and the "why". This is where confidence comes from: practising decisions, not just reading.
- **A mock exam (1)** across 4 ParentPace scenarios, timed like the real thing, with a score guide.
- **Domain size follows the exam weights:** Domain 1 (27%) gets 7 + 1, Domains 3 and 4 (20% each) get 6 + 1, Domain 5 (15%) 6 + 1, Domain 2 (18%) 5 + 1.

## Planned write-ups

| # | Objective | Title | ParentPace moment | Status |
|---|---|---|---|---|
| 0 | Curtain raiser | [Can a Parenting App Teach You the Claude Architect Exam?](00-curtain-raiser.md) | Meet ParentPace, the exam in one page, and why it tests judgement, not trivia | Draft for review |
| **Domain 1** | **Agentic architecture and orchestration (27%)** | | | |
| 1 | 1.1 Agentic loops | [How Does an Agent Know When to Stop?](01-agentic-loops.md) | A parent asks to move Saturday's coaching session. The agent checks the coach's calendar, books the new slot, and must know it's really finished, not just that it typed "All done!" | Draft for review |
| 2 | 1.2 Coordinator and subagents | One Coordinator, Three Helpers: Who Builds the Calm Parenting Course? | Studies, expert guidance and parent reviews researched by separate helpers | Planned |
| 3 | 1.3 Subagent context passing | The Helper Never Saw the Brief | The studies helper doesn't know the course is for parents of teenagers | Planned |
| 4 | 1.4 Enforcement and handoffs | The Prompt Said "Check the Plan First". The Agent Didn't. | A paid 1:1 session booked for a parent on the free plan; handing over to a human coach with a proper summary | Planned |
| 5 | 1.5 Agent SDK hooks | Who Checks the Agent Before It Presses Send? | A hook masks family names in logs and blocks refunds above the limit | Planned |
| 6 | 1.6 Task decomposition | One Big Ask or Five Small Ones? | "Build the Calm Parenting course" vs a step-by-step plan | Planned |
| 7 | 1.7 Session state | Pick Up Where You Left Off, or Try Two Ideas at Once? | Resuming yesterday's research; forking to compare two coaching approaches for bedtime battles | Planned |
| C1 | Domain 1 checkpoint | Domain 1 Checkpoint: Could You Pass This Part Today? | 6 to 8 exam-style ParentPace questions on Agentic architecture, with answers and the why | Planned |
| **Domain 2** | **Tool design and MCP (18%)** | | | |
| 8 | 2.1 Tool interfaces | Two Tools, Nearly the Same Name. Guess Which One It Picked. | get_parent vs get_parent_profile | Planned |
| 9 | 2.2 Structured errors | "Something Went Wrong" Tells the Agent Nothing | Calendar busy vs coach not found vs not allowed | Planned |
| 10 | 2.3 Tool distribution and tool_choice | Should Every Agent Get Every Tool? | The research helper accidentally holds the "issue refund" tool | Planned |
| 11 | 2.4 MCP integration | Plugging the Coaches' Calendar Into Claude | An MCP server for coach availability, set up for the whole team | Planned |
| 12 | 2.5 Built-in tools | Read, Grep, Glob or Edit: Which Tool for Which Job? | Finding every place session reminders are sent | Planned |
| C2 | Domain 2 checkpoint | Domain 2 Checkpoint: Could You Pass This Part Today? | 6 to 8 exam-style ParentPace questions on Tool design and MCP, with answers and the why | Planned |
| **Domain 3** | **Claude Code configuration and workflows (20%)** | | | |
| 13 | 3.1 CLAUDE.md | Stop Explaining the Codebase Every Morning | Team conventions, written once | Planned |
| 14 | 3.2 Slash commands and skills | The Release Checklist Everyone Forgets | A /release skill for the Friday deploy | Planned |
| 15 | 3.3 Path-specific rules | Coaching-Notes Rules for Coaching-Notes Files Only | Stricter privacy rules that load only in the session-notes code | Planned |
| 16 | 3.4 Plan mode vs direct execution | Plan First, or Just Build It? | Adding shared accounts for co-parents vs fixing a typo | Planned |
| 17 | 3.5 Iterative refinement | The First Draft Was Fine. The Third Was Right. | Tests first, then code; Claude asks the questions | Planned |
| 18 | 3.6 Claude Code in CI/CD | The Pull-Request Reviewer That Never Sleeps | Automated review and tests on every pull request | Planned |
| C3 | Domain 3 checkpoint | Domain 3 Checkpoint: Could You Pass This Part Today? | 6 to 8 exam-style ParentPace questions on Claude Code, with answers and the why | Planned |
| **Domain 4** | **Prompt engineering and structured output (20%)** | | | |
| 19 | 4.1 Explicit criteria | 40 Comments on One Pull Request | A vague review prompt vs clear criteria and severity | Planned |
| 20 | 4.2 Few-shot prompting | Show It Three Examples, Not Thirty Rules | Sorting parent messages consistently: distress, coaching question, billing | Planned |
| 21 | 4.3 Structured output with tools | From a Self-Assessment Form to a Clean Parent Profile | Extracting goals, stress triggers and family setup from intake forms | Planned |
| 22 | 4.4 Validation and retry loops | The JSON Was Valid. The Date Was Wrong. | 03/04 read as 3 April instead of 4 March; feeding the error back for a second try | Planned |
| 23 | 4.5 Batch processing | 10,000 Session Notes by Morning, at a Lower Price | Overnight summaries of coaching notes | Planned |
| 24 | 4.6 Multi-pass review | Why the Writer Shouldn't Check Its Own Work | An independent second review of a new course lesson | Planned |
| C4 | Domain 4 checkpoint | Domain 4 Checkpoint: Could You Pass This Part Today? | 6 to 8 exam-style ParentPace questions on Prompting and structured output, with answers and the why | Planned |
| **Domain 5** | **Context management and reliability (15%)** | | | |
| 25 | 5.1 Conversation context | Forty Messages In, It Forgot the Night Shifts | The parent works nights; forty messages later the advice assumes a 9-to-5 day | Planned |
| 26 | 5.2 Escalation and ambiguity | "I'm Close to Breaking Point." Should the AI Keep Coaching? | Handing over to a person on request, on distress, and when no rule fits; asking "which child?" in a family of three | Planned |
| 27 | 5.3 Error propagation | One Helper Failed. The Report Said "All Good". | The reviews helper timed out; the course report went out anyway | Planned |
| 28 | 5.4 Large-codebase exploration | Lost in 3,000 Files | Finding how coaching reminders are scheduled | Planned |
| 29 | 5.5 Human review and confidence | Which Answers Need a Human Look? | Routing low-confidence intake extractions to a human coach | Planned |
| 30 | 5.6 Provenance | Two Experts, Two Answers on Time-Outs. Which One Wins? | Conflicting sources in the research report | Planned |
| C5 | Domain 5 checkpoint | Domain 5 Checkpoint: Could You Pass This Part Today? | 6 to 8 exam-style ParentPace questions on Context and reliability, with answers and the why | Planned |
| M | Mock exam | 4 Scenarios, 20 Questions: Are You Ready? | A timed practice round across ParentPace's four systems, with a score guide | Planned |
| 31 | Finale | Exam Day: 30 Objectives on One Page | The whole ParentPace system, and a last-night revision checklist | Planned |

## The roadmap: every exam objective, with its write-up

Each objective is quoted from the official exam guide (Version 1.0, July 2026) so the write-up covers exactly what the exam expects. The write-ups themselves are in my own words, with ParentPace as the example.

### Domain 1: Agentic Architecture & Orchestration

#### Write-up 1 · Objective 1.1: Design and implement agentic loops for autonomous task execution

**Write-up:** [How Does an Agent Know When to Stop?](01-agentic-loops.md)  
**ParentPace moment:** A parent asks to move Saturday's coaching session. The agent checks the coach's calendar, books the new slot, and must know it's really finished, not just that it typed "All done!"  
**Status:** Planned

**Coverage map:** every knowledge (K) and skill (S) statement in this objective, and where the article covers it. Sections: Story, How it works, Objective map, Exam trap, Practice question.

| # | Exam statement (from the guide) | How our article covers it |
|---|---|---|
| K1 | **Knowledge:** The agentic loop lifecycle: sending requests to Claude, inspecting stop_reason ("tool_use" vs "end_turn"), executing requested tools, and returning results for the next iteration | **How it works:** the 4-step loop drawn on the reschedule request: ask Claude, read stop_reason, run check_calendar / book_session, send results back. |
| K2 | **Knowledge:** How tool results are appended to conversation history so the model can reason about the next action | **How it works:** each tool result (the coach's free slots) is added to the conversation so Claude can pick the next step. |
| K3 | **Knowledge:** The distinction between model-driven decision-making (Claude reasons about which tool to call next based on context) and pre-configured decision trees or tool sequences | **Story + trap:** why ParentPace lets Claude choose the next tool instead of a fixed if/else script, and when a fixed sequence is fine. |
| S1 | **Skill:** Implementing agentic loop control flow that continues when stop_reason is "tool_use" and terminates when stop_reason is "end_turn" | **Story:** the loop keeps going on "tool_use" (calendar, booking, email) and stops only on "end_turn". **Practice question** tests exactly this. |
| S2 | **Skill:** Adding tool results to conversation context between iterations so the model can incorporate new information into its reasoning | **Story:** the bug: the booking result was never sent back, so Claude booked the same slot twice. The fix appends every result. |
| S3 | **Skill:** Avoiding anti-patterns such as parsing natural language signals to determine loop termination, setting arbitrary iteration caps as the primary stopping mechanism, or checking for assistant text content as a completion indicator | **Exam trap:** the ParentPace code stopped on the word "done" in Claude's text; we show all three anti-patterns and why a step cap is only a safety net. |

#### Write-up 2 · Objective 1.2: Orchestrate multi-agent systems with coordinator-subagent patterns

**Write-up:** One Coordinator, Three Helpers: Who Builds the Calm Parenting Course?  
**ParentPace moment:** Studies, expert guidance and parent reviews researched by separate helpers  
**Status:** Planned

**Coverage map:** every knowledge (K) and skill (S) statement in this objective, and where the article covers it. Sections: Story, How it works, Objective map, Exam trap, Practice question.

| # | Exam statement (from the guide) | How our article covers it |
|---|---|---|
| K1 | **Knowledge:** Hub-and-spoke architecture where a coordinator agent manages all inter-subagent communication, error handling, and information routing | **How it works:** the Calm Parenting coordinator sits in the middle; studies, guidance and reviews helpers only talk to it. |
| K2 | **Knowledge:** How subagents operate with isolated context—they do not inherit the coordinator's conversation history automatically | **Story:** the reviews helper didn't see what the coordinator discussed earlier; context must be passed, not assumed. |
| K3 | **Knowledge:** The role of the coordinator in task decomposition, delegation, result aggregation, and deciding which subagents to invoke based on query complexity | **How it works:** the coordinator splits the course brief, picks helpers, and merges their findings. |
| K4 | **Knowledge:** Risks of overly narrow task decomposition by the coordinator, leading to incomplete coverage of broad research topics | **Exam trap:** splitting "calm parenting" too narrowly (only toddlers) misses parents of teenagers. |
| S1 | **Skill:** Designing coordinator agents that analyze query requirements and dynamically select which subagents to invoke rather than always routing through the full pipeline | **Story:** a simple question ("is this study from 2025?") goes to one helper, not the whole team. |
| S2 | **Skill:** Partitioning research scope across subagents to minimize duplication (e.g., assigning distinct subtopics or source types to each agent) | **How it works:** each helper gets a distinct slice: studies, expert guidance, parent reviews. No overlap. |
| S3 | **Skill:** Implementing iterative refinement loops where the coordinator evaluates synthesis output for gaps, re-delegates to search and analysis subagents with targeted queries, and re-invokes synthesis until coverage is sufficient | **Story:** the coordinator spots a gap (no evidence on teenagers), re-asks the studies helper, then re-runs synthesis. |
| S4 | **Skill:** Routing all subagent communication through the coordinator for observability, consistent error handling, and controlled information flow | **How it works:** every message goes through the coordinator, so logs and errors stay in one place. **Practice question** tests this. |

#### Write-up 3 · Objective 1.3: Configure subagent invocation, context passing, and spawning

**Write-up:** The Helper Never Saw the Brief  
**ParentPace moment:** The studies helper doesn't know the course is for parents of teenagers  
**Status:** Planned

**Coverage map:** every knowledge (K) and skill (S) statement in this objective, and where the article covers it. Sections: Story, How it works, Objective map, Exam trap, Practice question.

| # | Exam statement (from the guide) | How our article covers it |
|---|---|---|
| K1 | **Knowledge:** The Task tool as the mechanism for spawning subagents, and the requirement that allowedTools must include "Task" for a coordinator to invoke subagents | **How it works:** the coordinator spawns helpers through the Task tool, which must be in its allowed tools. |
| K2 | **Knowledge:** That subagent context must be explicitly provided in the prompt—subagents do not automatically inherit parent context or share memory between invocations | **Story:** the studies helper was never told the course is for parents of teenagers; we fix the brief. |
| K3 | **Knowledge:** The AgentDefinition configuration including descriptions, system prompts, and tool restrictions for each subagent type | **How it works:** each helper type is defined once: description, instructions, allowed tools. |
| K4 | **Knowledge:** Fork-based session management for exploring divergent approaches from a shared analysis baseline | **Objective map:** forking from a shared research baseline to try two directions (more in write-up 7). |
| S1 | **Skill:** Including complete findings from prior agents directly in the subagent's prompt (e.g., passing web search results and document analysis outputs to the synthesis subagent) | **Story:** the synthesis helper gets the full findings from the studies and reviews helpers in its prompt. |
| S2 | **Skill:** Using structured data formats to separate content from metadata (source URLs, document names, page numbers) when passing context between agents to preserve attribution | **How it works:** findings travel as structured data, with source, title and page kept separate from the content. |
| S3 | **Skill:** Spawning parallel subagents by emitting multiple Task tool calls in a single coordinator response rather than across separate turns | **Exam trap:** spawn helpers in parallel with several Task calls in one response, not one per turn. |
| S4 | **Skill:** Designing coordinator prompts that specify research goals and quality criteria rather than step-bystep procedural instructions, to enable subagent adaptability | **Practice question:** the coordinator states goals and quality bars ("3 peer-reviewed sources") rather than step-by-step orders. |

#### Write-up 4 · Objective 1.4: Implement multi-step workflows with enforcement and handoff patterns

**Write-up:** The Prompt Said "Check the Plan First". The Agent Didn't.  
**ParentPace moment:** A paid 1:1 session booked for a parent on the free plan; handing over to a human coach with a proper summary  
**Status:** Planned

**Coverage map:** every knowledge (K) and skill (S) statement in this objective, and where the article covers it. Sections: Story, How it works, Objective map, Exam trap, Practice question.

| # | Exam statement (from the guide) | How our article covers it |
|---|---|---|
| K1 | **Knowledge:** The difference between programmatic enforcement (hooks, prerequisite gates) and prompt-based guidance for workflow ordering | **Story:** "check the plan first" was only in the prompt; we compare that with a code gate that blocks booking. |
| K2 | **Knowledge:** When deterministic compliance is required (e.g., identity verification before financial operations), prompt instructions alone have a non-zero failure rate | **How it works:** why a prompt alone fails sometimes, and paid bookings need a guarantee. |
| K3 | **Knowledge:** Structured handoff protocols for mid-process escalation that include customer details, root cause analysis, and recommended actions | **Story:** the hand-over to a human coach carries a summary: parent ID, what happened, what to do next. |
| S1 | **Skill:** Implementing programmatic prerequisites that block downstream tool calls until prerequisite steps have completed (e.g., blocking process_refund until get_customer has returned a verified customer ID) | **Story:** book_paid_session is blocked until get_plan has returned "paid". **Practice question** tests this. |
| S2 | **Skill:** Decomposing multi-concern customer requests into distinct items, then investigating each in parallel using shared context before synthesizing a unified resolution | **How it works:** a message with three asks (reschedule, refund, change coach) is split, checked in parallel, answered once. |
| S3 | **Skill:** Compiling structured handoff summaries (customer ID, root cause, refund amount, recommended action) when escalating to human agents who lack access to the conversation transcript | **Exam trap:** the human coach can't see the chat, so the summary must stand on its own. |

#### Write-up 5 · Objective 1.5: Apply Agent SDK hooks for tool call interception and data normalization

**Write-up:** Who Checks the Agent Before It Presses Send?  
**ParentPace moment:** A hook masks family names in logs and blocks refunds above the limit  
**Status:** Planned

**Coverage map:** every knowledge (K) and skill (S) statement in this objective, and where the article covers it. Sections: Story, How it works, Objective map, Exam trap, Practice question.

| # | Exam statement (from the guide) | How our article covers it |
|---|---|---|
| K1 | **Knowledge:** Hook patterns (e.g., PostToolUse) that intercept tool results for transformation before the model processes them | **How it works:** a PostToolUse hook rewrites tool results (masks family names) before Claude reads them. |
| K2 | **Knowledge:** Hook patterns that intercept outgoing tool calls to enforce compliance rules (e.g., blocking refunds above a threshold) | **Story:** a hook on outgoing calls blocks refunds above the limit. |
| K3 | **Knowledge:** The distinction between using hooks for deterministic guarantees versus relying on prompt instructions for probabilistic compliance | **Exam trap:** hooks give guarantees; prompt instructions only make good behaviour likely. |
| S1 | **Skill:** Implementing PostToolUse hooks to normalize heterogeneous data formats (Unix timestamps, ISO 8601, numeric status codes) from different MCP tools before the agent processes them | **Story:** dates arrive as Unix time from billing and ISO from the calendar; the hook makes them one format. |
| S2 | **Skill:** Implementing tool call interception hooks that block policy-violating actions (e.g., refunds exceeding $500) and redirect to alternative workflows (e.g., human escalation) | **Story:** a $200 refund is blocked and turned into a hand-over to a human coach. **Practice question** tests this. |
| S3 | **Skill:** Choosing hooks over prompt-based enforcement when business rules require guaranteed compliance | **Objective map:** choose a hook whenever a business rule must never be broken. |

#### Write-up 6 · Objective 1.6: Design task decomposition strategies for complex workflows

**Write-up:** One Big Ask or Five Small Ones?  
**ParentPace moment:** "Build the Calm Parenting course" vs a step-by-step plan  
**Status:** Planned

**Coverage map:** every knowledge (K) and skill (S) statement in this objective, and where the article covers it. Sections: Story, How it works, Objective map, Exam trap, Practice question.

| # | Exam statement (from the guide) | How our article covers it |
|---|---|---|
| K1 | **Knowledge:** When to use fixed sequential pipelines (prompt chaining) versus dynamic adaptive decomposition based on intermediate findings | **How it works:** a fixed step-by-step chain vs a plan that changes with what's found, on the Calm Parenting course. |
| K2 | **Knowledge:** Prompt chaining patterns that break reviews into sequential steps (e.g., analyze each file individually, then run a cross-file integration pass) | **Objective map:** chaining for reviews: check each lesson alone, then one pass across the whole course. |
| K3 | **Knowledge:** The value of adaptive investigation plans that generate subtasks based on what is discovered at each step | **Story:** the research plan grows as helpers find new questions (screen time came up unexpectedly). |
| S1 | **Skill:** Selecting task decomposition patterns appropriate to the workflow: prompt chaining for predictable multi-aspect reviews, dynamic decomposition for open-ended investigation tasks | **Practice question:** pick chaining for a predictable review, adaptive planning for open research. |
| S2 | **Skill:** Splitting large code reviews into per-file local analysis passes plus a separate cross-file integration pass to avoid attention dilution | **Exam trap:** one giant review of 40 files misses issues; per-file passes plus an integration pass. |
| S3 | **Skill:** Decomposing open-ended tasks (e.g., "add comprehensive tests to a legacy codebase") by first mapping structure, identifying high-impact areas, then creating a prioritized plan that adapts as dependencies are discovered | **Story:** "add tests to the old booking code": map it first, find the risky parts, then a prioritised plan. |

#### Write-up 7 · Objective 1.7: Manage session state, resumption, and forking

**Write-up:** Pick Up Where You Left Off, or Try Two Ideas at Once?  
**ParentPace moment:** Resuming yesterday's research; forking to compare two coaching approaches for bedtime battles  
**Status:** Planned

**Coverage map:** every knowledge (K) and skill (S) statement in this objective, and where the article covers it. Sections: Story, How it works, Objective map, Exam trap, Practice question.

| # | Exam statement (from the guide) | How our article covers it |
|---|---|---|
| K1 | **Knowledge:** Named session resumption using --resume <session-name> to continue a specific prior conversation | **How it works:** resuming yesterday's research by its session name. |
| K2 | **Knowledge:** fork_session for creating independent branches from a shared analysis baseline to explore divergent approaches | **Story:** forking from the shared research to compare two bedtime-battle coaching approaches. |
| K3 | **Knowledge:** The importance of informing the agent about changes to previously analyzed files when resuming sessions after code modifications | **Exam trap:** tell a resumed session which files changed since it last looked. |
| K4 | **Knowledge:** Why starting a new session with a structured summary is more reliable than resuming with stale tool results | **Story:** when old tool results are stale, start a new session with a short summary instead. |
| S1 | **Skill:** Using --resume with session names to continue named investigation sessions across work sessions | **Objective map:** using --resume with a named session across days. |
| S2 | **Skill:** Using fork_session to create parallel exploration branches (e.g., comparing two testing strategies or refactoring approaches from a shared codebase analysis) | **Story:** two forks, same starting analysis, two approaches compared side by side. **Practice question** tests this. |
| S3 | **Skill:** Choosing between session resumption (when prior context is mostly valid) and starting fresh with injected summaries (when prior tool results are stale) | **How it works:** resume when the old context is still mostly right; start fresh with a summary when it isn't. |
| S4 | **Skill:** Informing a resumed session about specific file changes for targeted re-analysis rather than requiring full re-exploration | **Objective map:** point the resumed session at the 2 changed files rather than re-reading everything. |

#### Write-up 8 · Objective 2.1: Design effective tool interfaces with clear descriptions and boundaries

**Write-up:** Two Tools, Nearly the Same Name. Guess Which One It Picked.  
**ParentPace moment:** get_parent vs get_parent_profile  
**Status:** Planned

**Coverage map:** every knowledge (K) and skill (S) statement in this objective, and where the article covers it. Sections: Story, How it works, Objective map, Exam trap, Practice question.

| # | Exam statement (from the guide) | How our article covers it |
|---|---|---|
| K1 | **Knowledge:** Tool descriptions as the primary mechanism LLMs use for tool selection; minimal descriptions lead to unreliable selection among similar tools | **Story:** get_parent and get_parent_profile had one-line descriptions, so Claude picked the wrong one. |
| K2 | **Knowledge:** The importance of including input formats, example queries, edge cases, and boundary explanations in tool descriptions | **How it works:** a good description: input format, an example request, edge cases, and when not to use it. |
| K3 | **Knowledge:** How ambiguous or overlapping tool descriptions cause misrouting (e.g., analyze_content vs analyze_document with near-identical descriptions) | **Exam trap:** two tools with near-identical descriptions get mixed up; the article shows the before and after. |
| K4 | **Knowledge:** The impact of system prompt wording on tool selection: keyword-sensitive instructions can create unintended tool associations | **Objective map:** a word in the system prompt ("always check the profile") pulling Claude to the wrong tool. |
| S1 | **Skill:** Writing tool descriptions that clearly differentiate each tool's purpose, expected inputs, outputs, and when to use it versus similar alternatives | **How it works:** rewritten descriptions that say what each tool does, takes, returns and when to prefer it. |
| S2 | **Skill:** Renaming tools and updating descriptions to eliminate functional overlap (e.g., renaming analyze_content to extract_web_results with a web-specific description) | **Story:** renaming get_parent to get_billing_contact removes the overlap. |
| S3 | **Skill:** Splitting generic tools into purpose-specific tools with defined input/output contracts (e.g., splitting a generic analyze_document into extract_data_points, summarize_content, and verify_claim_against_source) | **Objective map:** splitting a generic analyze_notes into clear tools with fixed inputs and outputs. |
| S4 | **Skill:** Reviewing system prompts for keyword-sensitive instructions that might override well-written tool descriptions | **Practice question:** spotting a system-prompt keyword that overrides a good tool description. |

#### Write-up 9 · Objective 2.2: Implement structured error responses for MCP tools

**Write-up:** "Something Went Wrong" Tells the Agent Nothing  
**ParentPace moment:** Calendar busy vs coach not found vs not allowed  
**Status:** Planned

**Coverage map:** every knowledge (K) and skill (S) statement in this objective, and where the article covers it. Sections: Story, How it works, Objective map, Exam trap, Practice question.

| # | Exam statement (from the guide) | How our article covers it |
|---|---|---|
| K1 | **Knowledge:** The MCP isError flag pattern for communicating tool failures back to the agent | **How it works:** the isError flag tells Claude "the tool ran, but failed". |
| K2 | **Knowledge:** The distinction between transient errors (timeouts, service unavailability), validation errors (invalid input), business errors (policy violations), and permission errors | **Story:** calendar busy (transient), bad date (validation), refund over the policy limit (business), coach-only data (permission). |
| K3 | **Knowledge:** Why uniform error responses (generic "Operation failed") prevent the agent from making appropriate recovery decisions | **Story:** "Something went wrong" left the agent guessing; it retried a policy refusal three times. |
| K4 | **Knowledge:** The difference between retryable and non-retryable errors, and how returning structured metadata prevents wasted retry attempts | **How it works:** retryable vs not; structured details stop pointless retries. |
| S1 | **Skill:** Returning structured error metadata including errorCategory (transient/validation/permission), isRetryable boolean, and human-readable descriptions | **Objective map:** the error shape: category, isRetryable, a readable message. |
| S2 | **Skill:** Including retriable: false flags and customer-friendly explanations for business rule violations so the agent can communicate appropriately | **Story:** the refund refusal says "not retryable" and gives a kind explanation the agent can pass on. |
| S3 | **Skill:** Implementing local error recovery within subagents for transient failures, propagating to the coordinator only errors that cannot be resolved locally along with partial results and what was attempted | **Objective map:** a helper retries a busy calendar itself and only reports what it couldn't fix, with partial results. |
| S4 | **Skill:** Distinguishing between access failures (needing retry decisions) and valid empty results (representing successful queries with no matches) | **Exam trap + practice question:** "no sessions found" is a valid empty answer, not a failure. |

#### Write-up 10 · Objective 2.3: Distribute tools appropriately across agents and configure tool choice

**Write-up:** Should Every Agent Get Every Tool?  
**ParentPace moment:** The research helper accidentally holds the "issue refund" tool  
**Status:** Planned

**Coverage map:** every knowledge (K) and skill (S) statement in this objective, and where the article covers it. Sections: Story, How it works, Objective map, Exam trap, Practice question.

| # | Exam statement (from the guide) | How our article covers it |
|---|---|---|
| K1 | **Knowledge:** The principle that giving an agent access to too many tools (e.g., 18 instead of 4-5) degrades tool selection reliability by increasing decision complexity | **How it works:** why 18 tools confuse an agent and 4 or 5 work better. |
| K2 | **Knowledge:** Why agents with tools outside their specialization tend to misuse them (e.g., a synthesis agent attempting web searches) | **Story:** the research helper held the "issue refund" tool and nearly used it. |
| K3 | **Knowledge:** Scoped tool access: giving agents only the tools needed for their role, with limited cross-role tools for specific high-frequency needs | **How it works:** each role gets only its tools, plus a few shared ones it needs often. |
| K4 | **Knowledge:** tool_choice configuration options: "auto", "any", and forced tool selection ({"type": "tool", "name": "..."}) | **Objective map:** tool_choice options: auto, any, or one named tool. |
| S1 | **Skill:** Restricting each subagent's tool set to those relevant to its role, preventing cross-specialization misuse | **Story:** the fix: research helpers get research tools only. |
| S2 | **Skill:** Replacing generic tools with constrained alternatives (e.g., replacing fetch_url with load_document that validates document URLs) | **Objective map:** swapping a general fetch_url for a load_study tool that only accepts approved sources. |
| S3 | **Skill:** Providing scoped cross-role tools for high-frequency needs (e.g., a verify_fact tool for the synthesis agent) while routing complex cases through the coordinator | **Objective map:** a small verify_fact tool for the synthesis helper; harder checks go via the coordinator. |
| S4 | **Skill:** Using tool_choice forced selection to ensure a specific tool is called first (e.g., forcing extract_metadata before enrichment tools), then processing subsequent steps in follow-up turns | **Practice question:** forcing extract_profile to run first, then letting Claude choose the rest. |
| S5 | **Skill:** Setting tool_choice: "any" to guarantee the model calls a tool rather than returning conversational text | **Exam trap:** "any" guarantees a tool call instead of a chatty text answer. |

#### Write-up 11 · Objective 2.4: Integrate MCP servers into Claude Code and agent workflows

**Write-up:** Plugging the Coaches' Calendar Into Claude  
**ParentPace moment:** An MCP server for coach availability, set up for the whole team  
**Status:** Planned

**Coverage map:** every knowledge (K) and skill (S) statement in this objective, and where the article covers it. Sections: Story, How it works, Objective map, Exam trap, Practice question.

| # | Exam statement (from the guide) | How our article covers it |
|---|---|---|
| K1 | **Knowledge:** MCP server scoping: project-level (.mcp.json) for shared team tooling vs user-level (~/.claude.json) for personal/experimental servers | **Story:** the coaches' calendar server goes in the project's .mcp.json for the whole team; a test server stays personal. |
| K2 | **Knowledge:** Environment variable expansion in .mcp.json (e.g., ${GITHUB_TOKEN}) for credential management without committing secrets | **How it works:** ${CALENDAR_TOKEN} in .mcp.json, so no secret is committed. |
| K3 | **Knowledge:** That tools from all configured MCP servers are discovered at connection time and available simultaneously to the agent | **Objective map:** tools from every connected server are all available at once. |
| K4 | **Knowledge:** MCP resources as a mechanism for exposing content catalogs (e.g., issue summaries, documentation hierarchies, database schemas) to reduce exploratory tool calls | **How it works:** MCP resources list what exists (coach list, course catalogue) so Claude doesn't have to go looking. |
| S1 | **Skill:** Configuring shared MCP servers in project-scoped .mcp.json with environment variable expansion for authentication tokens | **Story:** the shared .mcp.json with the token variable, step by step. |
| S2 | **Skill:** Configuring personal/experimental MCP servers in user-scoped ~/.claude.json | **Objective map:** personal experiments in ~/.claude.json. |
| S3 | **Skill:** Enhancing MCP tool descriptions to explain capabilities and outputs in detail, preventing the agent from preferring built-in tools (like Grep) over more capable MCP tools | **Exam trap:** a vague MCP description makes Claude fall back to Grep; better descriptions fix it. |
| S4 | **Skill:** Choosing existing community MCP servers over custom implementations for standard integrations (e.g., Jira), reserving custom servers for team-specific workflows | **Practice question:** use an existing community server for the team's ticket tracker; build custom only for ParentPace's calendar. |
| S5 | **Skill:** Exposing content catalogs as MCP resources to give agents visibility into available data without requiring exploratory tool calls | **Story:** exposing the course catalogue as a resource. |

#### Write-up 12 · Objective 2.5: Select and apply built-in tools (Read, Write, Edit, Bash, Grep, Glob) effectively

**Write-up:** Read, Grep, Glob or Edit: Which Tool for Which Job?  
**ParentPace moment:** Finding every place session reminders are sent  
**Status:** Planned

**Coverage map:** every knowledge (K) and skill (S) statement in this objective, and where the article covers it. Sections: Story, How it works, Objective map, Exam trap, Practice question.

| # | Exam statement (from the guide) | How our article covers it |
|---|---|---|
| K1 | **Knowledge:** Grep for content search (searching file contents for patterns like function names, error messages, or import statements) | **How it works:** Grep searches inside files (where reminder emails are sent). |
| K2 | **Knowledge:** Glob for file path pattern matching (finding files by name or extension patterns) | **How it works:** Glob finds files by name pattern (all reminder test files). |
| K3 | **Knowledge:** Read/Write for full file operations; Edit for targeted modifications using unique text matching | **How it works:** Read/Write for whole files, Edit for a precise change. |
| K4 | **Knowledge:** When Edit fails due to non-unique text matches, using Read + Write as a fallback for reliable file modifications | **Exam trap:** Edit fails when the text isn't unique; Read then Write is the fallback. |
| S1 | **Skill:** Selecting Grep for searching code content across a codebase (e.g., finding all callers of a function, locating error messages) | **Story:** Grep finds every place session reminders are sent. |
| S2 | **Skill:** Selecting Glob for finding files matching naming patterns (e.g., **/*.test.tsx) | **Objective map:** Glob with **/*.test.ts to list the tests. |
| S3 | **Skill:** Using Read to load full file contents followed by Write when Edit cannot find unique anchor text | **Practice question:** Edit can't find a unique match; what next? |
| S4 | **Skill:** Building codebase understanding incrementally: starting with Grep to find entry points, then using Read to follow imports and trace flows, rather than reading all files upfront | **Story:** start with Grep, then Read along the imports, instead of opening every file. |
| S5 | **Skill:** Tracing function usage across wrapper modules by first identifying all exported names, then searching for each name across the codebase | **Objective map:** find all exported names of a wrapper module, then search for each one. |

#### Write-up 13 · Objective 3.1: Configure CLAUDE.md files with appropriate hierarchy, scoping, and modular organization

**Write-up:** Stop Explaining the Codebase Every Morning  
**ParentPace moment:** Team conventions, written once  
**Status:** Planned

**Coverage map:** every knowledge (K) and skill (S) statement in this objective, and where the article covers it. Sections: Story, How it works, Objective map, Exam trap, Practice question.

| # | Exam statement (from the guide) | How our article covers it |
|---|---|---|
| K1 | **Knowledge:** The CLAUDE.md configuration hierarchy: user-level (~/.claude/CLAUDE.md), project-level (.claude/CLAUDE.md or root CLAUDE.md), and directory-level (subdirectory CLAUDE.md files) | **How it works:** the three levels: user, project, folder. |
| K2 | **Knowledge:** That user-level settings apply only to that user—instructions in ~/.claude/CLAUDE.md are not shared with teammates via version control | **Story:** a new engineer didn't get the team rules because they lived in someone's user-level file. |
| K3 | **Knowledge:** The @import syntax for referencing external files to keep CLAUDE.md modular (e.g., importing specific standards files relevant to each package) | **Objective map:** @import pulls in the right standards file for each part of the app. |
| K4 | **Knowledge:** .claude/rules/ directory for organizing topic-specific rule files as an alternative to a monolithic CLAUDE.md | **How it works:** .claude/rules/ as a tidier alternative to one huge CLAUDE.md. |
| S1 | **Skill:** Diagnosing configuration hierarchy issues (e.g., a new team member not receiving instructions because they're in user-level rather than project-level configuration) | **Story:** moving the rules to project level fixes the new joiner. **Practice question** tests this. |
| S2 | **Skill:** Using @import to selectively include relevant standards files in each package's CLAUDE.md based on maintainer domain knowledge | **Objective map:** each package imports only the standards it needs. |
| S3 | **Skill:** Splitting large CLAUDE.md files into focused topic-specific files in .claude/rules/ (e.g., testing.md, api-conventions.md, deployment.md) | **Objective map:** splitting the big file into testing.md, api-conventions.md, deployment.md. |
| S4 | **Skill:** Using the /memory command to verify which memory files are loaded and diagnose inconsistent behavior across sessions | **Exam trap:** /memory shows which files are actually loaded. |

#### Write-up 14 · Objective 3.2: Create and configure custom slash commands and skills

**Write-up:** The Release Checklist Everyone Forgets  
**ParentPace moment:** A /release skill for the Friday deploy  
**Status:** Planned

**Coverage map:** every knowledge (K) and skill (S) statement in this objective, and where the article covers it. Sections: Story, How it works, Objective map, Exam trap, Practice question.

| # | Exam statement (from the guide) | How our article covers it |
|---|---|---|
| K1 | **Knowledge:** Project-scoped commands in .claude/commands/ (shared via version control) vs user-scoped commands in ~/.claude/commands/ (personal) | **How it works:** team commands in .claude/commands/ (shared in git) vs personal ones in ~/.claude/commands/. |
| K2 | **Knowledge:** Skills in .claude/skills/ with SKILL.md files that support frontmatter configuration including context: fork, allowed-tools, and argument-hint | **How it works:** skills in .claude/skills/ with a SKILL.md and settings like context: fork, allowed-tools, argument-hint. |
| K3 | **Knowledge:** The context: fork frontmatter option for running skills in an isolated sub-agent context, preventing skill outputs from polluting the main conversation | **Story:** the /release skill runs with context: fork so its long output stays out of the main chat. |
| K4 | **Knowledge:** Personal skill customization: creating personal variants in ~/.claude/skills/ with different names to avoid affecting teammates | **Objective map:** personal variants in ~/.claude/skills/ under a different name. |
| S1 | **Skill:** Creating project-scoped slash commands in .claude/commands/ for team-wide availability via version control | **Story:** /release lives in the project, so the whole team has it. |
| S2 | **Skill:** Using context: fork to isolate skills that produce verbose output (e.g., codebase analysis) or exploratory context (e.g., brainstorming alternatives) from the main session | **Objective map:** fork for verbose analysis or brainstorming skills. |
| S3 | **Skill:** Configuring allowed-tools in skill frontmatter to restrict tool access during skill execution (e.g., limiting to file write operations to prevent destructive actions) | **Exam trap:** allowed-tools limits what the skill may touch during its run. |
| S4 | **Skill:** Using argument-hint frontmatter to prompt developers for required parameters when they invoke the skill without arguments | **Objective map:** argument-hint asks for the version number if it's missing. |
| S5 | **Skill:** Choosing between skills (on-demand invocation for task-specific workflows) and CLAUDE.md (always-loaded universal standards) | **Practice question:** skill (on demand) or CLAUDE.md (always loaded)? |

#### Write-up 15 · Objective 3.3: Apply path-specific rules for conditional convention loading

**Write-up:** Coaching-Notes Rules for Coaching-Notes Files Only  
**ParentPace moment:** Stricter privacy rules that load only in the session-notes code  
**Status:** Planned

**Coverage map:** every knowledge (K) and skill (S) statement in this objective, and where the article covers it. Sections: Story, How it works, Objective map, Exam trap, Practice question.

| # | Exam statement (from the guide) | How our article covers it |
|---|---|---|
| K1 | **Knowledge:** .claude/rules/ files with YAML frontmatter paths fields containing glob patterns for conditional rule activation | **How it works:** rule files with a paths: field of file patterns. |
| K2 | **Knowledge:** How path-scoped rules load only when editing matching files, reducing irrelevant context and token usage | **Story:** the session-notes privacy rules load only when editing session-notes files, saving context. |
| K3 | **Knowledge:** The advantage of glob-pattern rules over directory-level CLAUDE.md files for conventions that span multiple directories (e.g., test files spread throughout a codebase) | **Exam trap:** test files are everywhere, so a pattern beats a folder CLAUDE.md. |
| S1 | **Skill:** Creating .claude/rules/ files with YAML frontmatter path scoping (e.g., paths: ["terraform/**/*"]) so rules load only when editing matching files | **Story:** paths: ["src/notes/**/*"] on the privacy rules. |
| S2 | **Skill:** Using glob patterns in path-specific rules to apply conventions to files by type regardless of directory location (e.g., **/*.test.tsx for all test files) | **Objective map:** **/*.test.ts for all tests, wherever they live. |
| S3 | **Skill:** Choosing path-specific rules over subdirectory CLAUDE.md files when conventions must apply to files spread across the codebase | **Practice question:** rules for files spread across folders: pattern rule or folder CLAUDE.md? |

#### Write-up 16 · Objective 3.4: Determine when to use plan mode vs direct execution

**Write-up:** Plan First, or Just Build It?  
**ParentPace moment:** Adding shared accounts for co-parents vs fixing a typo  
**Status:** Planned

**Coverage map:** every knowledge (K) and skill (S) statement in this objective, and where the article covers it. Sections: Story, How it works, Objective map, Exam trap, Practice question.

| # | Exam statement (from the guide) | How our article covers it |
|---|---|---|
| K1 | **Knowledge:** Plan mode is designed for complex tasks involving large-scale changes, multiple valid approaches, architectural decisions, and multi-file modifications | **How it works:** plan mode for big, many-file, many-option changes. |
| K2 | **Knowledge:** Direct execution is appropriate for simple, well-scoped changes (e.g., adding a single validation check to one function) | **Story:** fixing a typo: just do it. |
| K3 | **Knowledge:** Plan mode enables safe codebase exploration and design before committing to changes, preventing costly rework | **How it works:** planning explores safely before anything changes. |
| K4 | **Knowledge:** The Explore subagent for isolating verbose discovery output and returning summaries to preserve main conversation context | **Objective map:** the Explore helper keeps noisy discovery out of the main chat. |
| S1 | **Skill:** Selecting plan mode for tasks with architectural implications (e.g., microservice restructuring, library migrations affecting 45+ files, choosing between integration approaches with different infrastructure requirements) | **Story:** shared co-parent accounts touch 30 files and two designs: plan mode. **Practice question** tests this. |
| S2 | **Skill:** Selecting direct execution for well-understood changes with clear scope (e.g., a single-file bug fix with a clear stack trace, adding a date validation conditional) | **Objective map:** a one-file bug with a clear error: direct. |
| S3 | **Skill:** Using the Explore subagent for verbose discovery phases to prevent context window exhaustion during multi-phase tasks | **Objective map:** use Explore during long discovery so context doesn't run out. |
| S4 | **Skill:** Combining plan mode for investigation with direct execution for implementation (e.g., planning a library migration, then executing the planned approach) | **Exam trap:** plan first, then execute the agreed plan directly. |

#### Write-up 17 · Objective 3.5: Apply iterative refinement techniques for progressive improvement

**Write-up:** The First Draft Was Fine. The Third Was Right.  
**ParentPace moment:** Tests first, then code; Claude asks the questions  
**Status:** Planned

**Coverage map:** every knowledge (K) and skill (S) statement in this objective, and where the article covers it. Sections: Story, How it works, Objective map, Exam trap, Practice question.

| # | Exam statement (from the guide) | How our article covers it |
|---|---|---|
| K1 | **Knowledge:** Concrete input/output examples as the most effective way to communicate expected transformations when prose descriptions are interpreted inconsistently | **How it works:** 2 or 3 examples beat a paragraph of description. |
| K2 | **Knowledge:** Test-driven iteration: writing test suites first, then iterating by sharing test failures to guide progressive improvement | **Story:** tests first; share failures with Claude until they pass. |
| K3 | **Knowledge:** The interview pattern: having Claude ask questions to surface considerations the developer may not have anticipated before implementing | **Story:** the interview pattern: Claude asks about reminders and time zones before coding. |
| K4 | **Knowledge:** When to provide all issues in a single message (interacting problems) versus fixing them sequentially (independent problems) | **Exam trap:** related problems in one message, unrelated ones one at a time. |
| S1 | **Skill:** Providing 2-3 concrete input/output examples to clarify transformation requirements when natural language descriptions produce inconsistent results | **Objective map:** examples for the date-format change. |
| S2 | **Skill:** Writing test suites covering expected behavior, edge cases, and performance requirements before implementation, then iterating by sharing test failures | **Objective map:** tests for normal cases, edge cases and speed, written before the code. |
| S3 | **Skill:** Using the interview pattern to surface design considerations (e.g., cache invalidation strategies, failure modes) before implementing solutions in unfamiliar domains | **Story:** the interview surfaced a missed failure mode (a coach in another time zone). |
| S4 | **Skill:** Providing specific test cases with example input and expected output to fix edge case handling (e.g., null values in migration scripts) | **Practice question:** a null-value edge case fixed by giving an exact input and expected output. |
| S5 | **Skill:** Addressing multiple interacting issues in a single detailed message when fixes interact, versus sequential iteration for independent issues | **Objective map:** batch interacting fixes into one detailed message. |

#### Write-up 18 · Objective 3.6: Integrate Claude Code into CI/CD pipelines

**Write-up:** The Pull-Request Reviewer That Never Sleeps  
**ParentPace moment:** Automated review and tests on every pull request  
**Status:** Planned

**Coverage map:** every knowledge (K) and skill (S) statement in this objective, and where the article covers it. Sections: Story, How it works, Objective map, Exam trap, Practice question.

| # | Exam statement (from the guide) | How our article covers it |
|---|---|---|
| K1 | **Knowledge:** The -p (or --print) flag for running Claude Code in non-interactive mode in automated pipelines | **How it works:** -p runs Claude Code without waiting for input. |
| K2 | **Knowledge:** --output-format json and --json-schema CLI flags for enforcing structured output in CI contexts | **How it works:** --output-format json and --json-schema for machine-readable findings. |
| K3 | **Knowledge:** CLAUDE.md as the mechanism for providing project context (testing standards, fixture conventions, review criteria) to CI-invoked Claude Code | **Objective map:** CLAUDE.md gives the CI review the team's testing and review rules. |
| K4 | **Knowledge:** Session context isolation: why the same Claude session that generated code is less effective at reviewing its own changes compared to an independent review instance | **Exam trap:** the session that wrote the code reviews it poorly; use a fresh instance. |
| S1 | **Skill:** Running Claude Code in CI with the -p flag to prevent interactive input hangs | **Story:** the pipeline hung waiting for input until -p was added. |
| S2 | **Skill:** Using --output-format json with --json-schema to produce machine-parseable structured findings for automated posting as inline PR comments | **Story:** findings posted as inline pull-request comments from the JSON. |
| S3 | **Skill:** Including prior review findings in context when re-running reviews after new commits, instructing Claude to report only new or still-unaddressed issues to avoid duplicate comments | **Objective map:** after new commits, pass earlier findings and report only new or unfixed ones. |
| S4 | **Skill:** Providing existing test files in context so test generation avoids suggesting duplicate scenarios already covered by the test suite | **Objective map:** give existing tests so suggestions don't duplicate them. |
| S5 | **Skill:** Documenting testing standards, valuable test criteria, and available fixtures in CLAUDE.md to improve test generation quality and reduce low-value test output | **Practice question:** document fixtures and test standards in CLAUDE.md to get better tests. |

#### Write-up 19 · Objective 4.1: Design prompts with explicit criteria to improve precision and reduce false positives

**Write-up:** 40 Comments on One Pull Request  
**ParentPace moment:** A vague review prompt vs clear criteria and severity  
**Status:** Planned

**Coverage map:** every knowledge (K) and skill (S) statement in this objective, and where the article covers it. Sections: Story, How it works, Objective map, Exam trap, Practice question.

| # | Exam statement (from the guide) | How our article covers it |
|---|---|---|
| K1 | **Knowledge:** The importance of explicit criteria over vague instructions (e.g., "flag comments only when claimed behavior contradicts actual code behavior" vs "check that comments are accurate") | **Story:** "review this" produced 40 comments; "flag only bugs and security issues" produced 4 real ones. |
| K2 | **Knowledge:** How general instructions like "be conservative" or "only report high-confidence findings" fail to improve precision compared to specific categorical criteria | **Exam trap:** "be conservative" doesn't improve precision; specific categories do. |
| K3 | **Knowledge:** The impact of false positive rates on developer trust: high false positive categories undermine confidence in accurate categories | **How it works:** one noisy category makes the team ignore the good ones. |
| S1 | **Skill:** Writing specific review criteria that define which issues to report (bugs, security) versus skip (minor style, local patterns) rather than relying on confidence-based filtering | **Objective map:** what to report (bugs, security) and what to skip (minor style). |
| S2 | **Skill:** Temporarily disabling high false-positive categories to restore developer trust while improving prompts for those categories | **Story:** switching off the noisy style category while that prompt is fixed. |
| S3 | **Skill:** Defining explicit severity criteria with concrete code examples for each severity level to achieve consistent classification | **Practice question:** severity levels defined with a code example each. |

#### Write-up 20 · Objective 4.2: Apply few-shot prompting to improve output consistency and quality

**Write-up:** Show It Three Examples, Not Thirty Rules  
**ParentPace moment:** Sorting parent messages consistently: distress, coaching question, billing  
**Status:** Planned

**Coverage map:** every knowledge (K) and skill (S) statement in this objective, and where the article covers it. Sections: Story, How it works, Objective map, Exam trap, Practice question.

| # | Exam statement (from the guide) | How our article covers it |
|---|---|---|
| K1 | **Knowledge:** Few-shot examples as the most effective technique for achieving consistently formatted, actionable output when detailed instructions alone produce inconsistent results | **How it works:** examples beat long instructions for consistent output. |
| K2 | **Knowledge:** The role of few-shot examples in demonstrating ambiguous-case handling (e.g., tool selection for ambiguous requests, branch-level test coverage gaps) | **Story:** examples show how to handle unclear messages (is "I'm exhausted" distress or a coaching question?). |
| K3 | **Knowledge:** How few-shot examples enable the model to generalize judgment to novel patterns rather than matching only pre-specified cases | **Objective map:** good examples teach the judgement, so new cases are handled too. |
| K4 | **Knowledge:** The effectiveness of few-shot examples for reducing hallucination in extraction tasks (e.g., handling informal measurements, varied document structures) | **Objective map:** examples of missing information reduce made-up answers in extraction. |
| S1 | **Skill:** Creating 2-4 targeted few-shot examples for ambiguous scenarios that show reasoning for why one action was chosen over plausible alternatives | **Story:** 3 examples, each with the reason one label was chosen over another. |
| S2 | **Skill:** Including few-shot examples that demonstrate specific desired output format (location, issue, severity, suggested fix) to achieve consistency | **Objective map:** examples that show the exact output shape. |
| S3 | **Skill:** Providing few-shot examples distinguishing acceptable code patterns from genuine issues to reduce false positives while enabling generalization | **Exam trap:** examples of acceptable vs real problems cut false alarms. |
| S4 | **Skill:** Using few-shot examples to demonstrate correct handling of varied document structures (inline citations vs bibliographies, methodology sections vs embedded details) | **Objective map:** examples covering differently laid-out intake forms. |
| S5 | **Skill:** Adding few-shot examples showing correct extraction from documents with varied formats to address empty/null extraction of required fields | **Practice question:** required fields coming back empty: add examples of correct extraction. |

#### Write-up 21 · Objective 4.3: Enforce structured output using tool use and JSON schemas

**Write-up:** From a Self-Assessment Form to a Clean Parent Profile  
**ParentPace moment:** Extracting goals, stress triggers and family setup from intake forms  
**Status:** Planned

**Coverage map:** every knowledge (K) and skill (S) statement in this objective, and where the article covers it. Sections: Story, How it works, Objective map, Exam trap, Practice question.

| # | Exam statement (from the guide) | How our article covers it |
|---|---|---|
| K1 | **Knowledge:** Tool use (tool_use) with JSON schemas as the most reliable approach for guaranteed schemacompliant structured output, eliminating JSON syntax errors | **How it works:** a tool with a JSON schema gives guaranteed valid JSON. |
| K2 | **Knowledge:** The distinction between tool_choice: "auto" (model may return text instead of calling a tool), "any" (model must call a tool but can choose which), and forced tool selection (model must call a specific named tool) | **Exam trap:** auto (may answer in text), any (must call some tool), or one forced tool. |
| K3 | **Knowledge:** That strict JSON schemas via tool use eliminate syntax errors but do not prevent semantic errors (e.g., line items that don't sum to total, values in wrong fields) | **Story:** valid JSON can still be wrong: the parent's stated goal ended up in the wrong field. |
| K4 | **Knowledge:** Schema design considerations: required vs optional fields, enum fields with "other" + detail string patterns for extensible categories | **Objective map:** required vs optional fields; enums with "other" plus a detail field. |
| S1 | **Skill:** Defining extraction tools with JSON schemas as input parameters and extracting structured data from the tool_use response | **Story:** the extract_profile tool and reading its result. |
| S2 | **Skill:** Setting tool_choice: "any" to guarantee structured output when multiple extraction schemas exist and the document type is unknown | **Objective map:** "any" when the form type is unknown. |
| S3 | **Skill:** Forcing a specific tool with tool_choice: {"type": "tool", "name": "extract_metadata"} to ensure a particular extraction runs before enrichment steps | **Practice question:** forcing extract_profile to run before enrichment. |
| S4 | **Skill:** Designing schema fields as optional (nullable) when source documents may not contain the information, preventing the model from fabricating values to satisfy required fields | **Story:** optional fields so the model doesn't invent a partner's name that isn't on the form. |
| S5 | **Skill:** Adding enum values like "unclear" for ambiguous cases and "other" + detail fields for extensible categorization | **Objective map:** "unclear" and "other + detail" values. |
| S6 | **Skill:** Including format normalization rules in prompts alongside strict output schemas to handle inconsistent source formatting | **Objective map:** normalisation rules (dates, durations) in the prompt alongside the schema. |

#### Write-up 22 · Objective 4.4: Implement validation, retry, and feedback loops for extraction quality

**Write-up:** The JSON Was Valid. The Date Was Wrong.  
**ParentPace moment:** 03/04 read as 3 April instead of 4 March; feeding the error back for a second try  
**Status:** Planned

**Coverage map:** every knowledge (K) and skill (S) statement in this objective, and where the article covers it. Sections: Story, How it works, Objective map, Exam trap, Practice question.

| # | Exam statement (from the guide) | How our article covers it |
|---|---|---|
| K1 | **Knowledge:** Retry-with-error-feedback: appending specific validation errors to the prompt on retry to guide the model toward correction | **Story:** the retry includes the exact error: "date 03/04 conflicts with the form's signing date". |
| K2 | **Knowledge:** The limits of retry: retries are ineffective when the required information is simply absent from the source document (vs format or structural errors) | **Exam trap:** retrying is useless when the information isn't in the document at all. |
| K3 | **Knowledge:** Feedback loop design: tracking which code constructs trigger findings (detected_pattern field) to enable systematic analysis of dismissal patterns | **Objective map:** a detected_pattern field to learn why reviewers dismiss findings. |
| K4 | **Knowledge:** The difference between semantic validation errors (values don't sum, wrong field placement) and schema syntax errors (eliminated by tool use) | **How it works:** schema errors (gone with tool use) vs meaning errors (wrong date, wrong field). |
| S1 | **Skill:** Implementing follow-up requests that include the original document, the failed extraction, and specific validation errors for model self-correction | **Story:** the follow-up request sends the form, the failed result and the specific errors. |
| S2 | **Skill:** Identifying when retries will be ineffective (e.g., information exists only in an external document not provided) versus when they will succeed (format mismatches, structural output errors) | **Practice question:** will a retry help here, or is the data missing? |
| S3 | **Skill:** Adding detected_pattern fields to structured findings to enable analysis of false positive patterns when developers dismiss findings | **Objective map:** add detected_pattern to findings. |
| S4 | **Skill:** Designing self-correction validation flows: extracting "calculated_total" alongside "stated_total" to flag discrepancies, adding "conflict_detected" booleans for inconsistent source data | **How it works:** calculated vs stated values, plus a conflict_detected flag. |

#### Write-up 23 · Objective 4.5: Design efficient batch processing strategies

**Write-up:** 10,000 Session Notes by Morning, at a Lower Price  
**ParentPace moment:** Overnight summaries of coaching notes  
**Status:** Planned

**Coverage map:** every knowledge (K) and skill (S) statement in this objective, and where the article covers it. Sections: Story, How it works, Objective map, Exam trap, Practice question.

| # | Exam statement (from the guide) | How our article covers it |
|---|---|---|
| K1 | **Knowledge:** The Message Batches API: 50% cost savings, up to 24-hour processing window, no guaranteed latency SLA | **How it works:** batches: about half the cost, results within 24 hours, no speed promise. |
| K2 | **Knowledge:** Batch processing is appropriate for non-blocking, latency-tolerant workloads (overnight reports, weekly audits, nightly test generation) and inappropriate for blocking workflows (pre-merge checks) | **Story:** overnight summaries of session notes: yes. A check that blocks a merge: no. |
| K3 | **Knowledge:** The batch API does not support multi-turn tool calling within a single request (cannot execute tools mid-request and return results) | **Exam trap:** a batch request can't run tools in the middle of a request. |
| K4 | **Knowledge:** custom_id fields for correlating batch request/response pairs | **Objective map:** custom_id links each result back to its note. |
| S1 | **Skill:** Matching API approach to workflow latency requirements: synchronous API for blocking pre-merge checks, batch API for overnight/weekly analysis | **Practice question:** synchronous for blocking checks, batch for overnight work. |
| S2 | **Skill:** Calculating batch submission frequency based on SLA constraints (e.g., 4-hour windows to guarantee 30-hour SLA with 24-hour batch processing) | **Objective map:** working out how often to submit to meet a deadline. |
| S3 | **Skill:** Handling batch failures: resubmitting only failed documents (identified by custom_id) with appropriate modifications (e.g., chunking documents that exceeded context limits) | **Story:** resend only the failed notes (found by custom_id), split if too long. |
| S4 | **Skill:** Using prompt refinement on a sample set before batch-processing large volumes to maximize firstpass success rates and reduce iterative resubmission costs | **Objective map:** test the prompt on a sample first, then run the full batch. |

#### Write-up 24 · Objective 4.6: Design multi-instance and multi-pass review architectures

**Write-up:** Why the Writer Shouldn't Check Its Own Work  
**ParentPace moment:** An independent second review of a new course lesson  
**Status:** Planned

**Coverage map:** every knowledge (K) and skill (S) statement in this objective, and where the article covers it. Sections: Story, How it works, Objective map, Exam trap, Practice question.

| # | Exam statement (from the guide) | How our article covers it |
|---|---|---|
| K1 | **Knowledge:** Self-review limitations: a model retains reasoning context from generation, making it less likely to question its own decisions in the same session | **How it works:** the writer remembers its own reasoning, so it rarely questions itself. |
| K2 | **Knowledge:** Independent review instances (without prior reasoning context) are more effective at catching subtle issues than self-review instructions or extended thinking | **Story:** a fresh, independent instance found two problems in the new course lesson that self-review missed. |
| K3 | **Knowledge:** Multi-pass review: splitting large reviews into per-file local analysis passes plus cross-file integration passes to avoid attention dilution and contradictory findings | **Objective map:** per-file passes plus an integration pass for big reviews. |
| S1 | **Skill:** Using a second independent Claude instance to review generated code without the generator's reasoning context | **Story:** the second instance reviews without seeing the writer's reasoning. |
| S2 | **Skill:** Splitting large multi-file reviews into focused per-file passes for local issues plus separate integration passes for cross-file data flow analysis | **Practice question:** split a big review into local and cross-file passes. |
| S3 | **Skill:** Running verification passes where the model self-reports confidence alongside each finding to enable calibrated review routing | **Exam trap:** confidence per finding helps route reviews, but doesn't replace an independent check. |

#### Write-up 25 · Objective 5.1: Manage conversation context to preserve critical information across long interactions

**Write-up:** Forty Messages In, It Forgot the Night Shifts  
**ParentPace moment:** The parent works nights; forty messages later the advice assumes a 9-to-5 day  
**Status:** Planned

**Coverage map:** every knowledge (K) and skill (S) statement in this objective, and where the article covers it. Sections: Story, How it works, Objective map, Exam trap, Practice question.

| # | Exam statement (from the guide) | How our article covers it |
|---|---|---|
| K1 | **Knowledge:** Progressive summarization risks: condensing numerical values, percentages, dates, and customerstated expectations into vague summaries | **Story:** the summary turned "works nights, 10pm to 6am" into "busy schedule". |
| K2 | **Knowledge:** The "lost in the middle" effect: models reliably process information at the beginning and end of long inputs but may omit findings from middle sections | **How it works:** facts in the middle of long inputs get missed (lost in the middle). |
| K3 | **Knowledge:** How tool results accumulate in context and consume tokens disproportionately to their relevance (e.g., 40+ fields per order lookup when only 5 are relevant) | **Objective map:** long tool results fill the context with fields nobody needs. |
| K4 | **Knowledge:** The importance of passing complete conversation history in subsequent API requests to maintain conversational coherence | **Exam trap:** send the full conversation history with each request. |
| S1 | **Skill:** Extracting transactional facts (amounts, dates, order numbers, statuses) into a persistent "case facts" block included in each prompt, outside summarized history | **Story:** a "case facts" block (night shifts, two children, goal: fewer bedtime fights) kept in every prompt. |
| S2 | **Skill:** Extracting and persisting structured issue data (order IDs, amounts, statuses) into a separate context layer for multi-issue sessions | **Objective map:** separate facts for each topic when a parent raises several. |
| S3 | **Skill:** Trimming verbose tool outputs to only relevant fields before they accumulate in context (e.g., keeping only return-relevant fields from order lookups) | **Objective map:** trim tool results to the relevant fields. |
| S4 | **Skill:** Placing key findings summaries at the beginning of aggregated inputs and organizing detailed results with explicit section headers to mitigate position effects | **How it works:** key findings first, clear headings for details. |
| S5 | **Skill:** Requiring subagents to include metadata (dates, source locations, methodological context) in structured outputs to support accurate downstream synthesis | **Objective map:** helpers include dates, sources and context in what they return. |
| S6 | **Skill:** Modifying upstream agents to return structured data (key facts, citations, relevance scores) instead of verbose content and reasoning chains when downstream agents have limited context budgets | **Practice question:** upstream helpers return structured facts, not long reasoning. |

#### Write-up 26 · Objective 5.2: Design effective escalation and ambiguity resolution patterns

**Write-up:** "I'm Close to Breaking Point." Should the AI Keep Coaching?  
**ParentPace moment:** Handing over to a person on request, on distress, and when no rule fits; asking "which child?" in a family of three  
**Status:** Planned

**Coverage map:** every knowledge (K) and skill (S) statement in this objective, and where the article covers it. Sections: Story, How it works, Objective map, Exam trap, Practice question.

| # | Exam statement (from the guide) | How our article covers it |
|---|---|---|
| K1 | **Knowledge:** Appropriate escalation triggers: customer requests for a human, policy exceptions/gaps (not just complex cases), and inability to make meaningful progress | **How it works:** hand over on request, on policy gaps, or when there's no progress. |
| K2 | **Knowledge:** The distinction between escalating immediately when a customer explicitly demands it versus offering to resolve when the issue is straightforward | **Story:** "I want to talk to a person": hand over now. A simple booking question: offer to help first. |
| K3 | **Knowledge:** Why sentiment-based escalation and self-reported confidence scores are unreliable proxies for actual case complexity | **Exam trap:** tone of voice and the AI's own confidence are poor signals for when to hand over. |
| K4 | **Knowledge:** How multiple customer matches require clarification (requesting additional identifiers) rather than heuristic selection | **Objective map:** several matches need a clarifying question, not a guess. |
| S1 | **Skill:** Adding explicit escalation criteria with few-shot examples to the system prompt demonstrating when to escalate versus resolve autonomously | **How it works:** escalation rules in the system prompt, with examples. |
| S2 | **Skill:** Honoring explicit customer requests for human agents immediately without first attempting investigation | **Story:** "I'm close to breaking point. Can I talk to someone?" goes straight to a human coach. |
| S3 | **Skill:** Acknowledging frustration while offering resolution when the issue is within the agent's capability, escalating only if the customer reiterates their preference | **Objective map:** acknowledge frustration, offer help, escalate if the parent asks again. |
| S4 | **Skill:** Escalating when policy is ambiguous or silent on the customer's specific request (e.g., competitor price matching when policy only addresses own-site adjustments) | **Practice question:** the policy doesn't cover a request (a sibling discount); escalate. |
| S5 | **Skill:** Instructing the agent to ask for additional identifiers when tool results return multiple matches, rather than selecting based on heuristics | **Story:** "which child?" in a family of three, instead of guessing. |

#### Write-up 27 · Objective 5.3: Implement error propagation strategies across multi-agent systems

**Write-up:** One Helper Failed. The Report Said "All Good".  
**ParentPace moment:** The reviews helper timed out; the course report went out anyway  
**Status:** Planned

**Coverage map:** every knowledge (K) and skill (S) statement in this objective, and where the article covers it. Sections: Story, How it works, Objective map, Exam trap, Practice question.

| # | Exam statement (from the guide) | How our article covers it |
|---|---|---|
| K1 | **Knowledge:** Structured error context (failure type, attempted query, partial results, alternative approaches) as enabling intelligent coordinator recovery decisions | **How it works:** a useful error says what failed, what was tried, partial results and alternatives. |
| K2 | **Knowledge:** The distinction between access failures (timeouts needing retry decisions) and valid empty results (successful queries with no matches) | **Exam trap:** a timeout isn't the same as "no results found". |
| K3 | **Knowledge:** Why generic error statuses ("search unavailable") hide valuable context from the coordinator | **Story:** "reviews unavailable" hid that the helper had half the reviews. |
| K4 | **Knowledge:** Why silently suppressing errors (returning empty results as success) or terminating entire workflows on single failures are both anti-patterns | **Story:** the report said "all good" because the failure was swallowed; the opposite mistake is stopping everything. |
| S1 | **Skill:** Returning structured error context including failure type, what was attempted, partial results, and potential alternatives to enable coordinator recovery | **Objective map:** the structured error the helper should return. |
| S2 | **Skill:** Distinguishing access failures from valid empty results in error reporting so the coordinator can make appropriate decisions | **Practice question:** timeout vs valid empty result. |
| S3 | **Skill:** Having subagents implement local recovery for transient failures and only propagate errors they cannot resolve, including what was attempted and partial results | **Objective map:** retry locally, pass up only what can't be fixed. |
| S4 | **Skill:** Structuring synthesis output with coverage annotations indicating which findings are wellsupported versus which topic areas have gaps due to unavailable sources | **Story:** the final report marks which parts are well supported and where sources were missing. |

#### Write-up 28 · Objective 5.4: Manage context effectively in large codebase exploration

**Write-up:** Lost in 3,000 Files  
**ParentPace moment:** Finding how coaching reminders are scheduled  
**Status:** Planned

**Coverage map:** every knowledge (K) and skill (S) statement in this objective, and where the article covers it. Sections: Story, How it works, Objective map, Exam trap, Practice question.

| # | Exam statement (from the guide) | How our article covers it |
|---|---|---|
| K1 | **Knowledge:** Context degradation in extended sessions: models start giving inconsistent answers and referencing "typical patterns" rather than specific classes discovered earlier | **Story:** after an hour, Claude talks about "typical patterns" instead of the actual reminder classes it found. |
| K2 | **Knowledge:** The role of scratchpad files for persisting key findings across context boundaries | **How it works:** a scratchpad file keeps key findings. |
| K3 | **Knowledge:** Subagent delegation for isolating verbose exploration output while the main agent coordinates highlevel understanding | **Objective map:** helpers do the noisy exploring; the main agent keeps the big picture. |
| K4 | **Knowledge:** Structured state persistence for crash recovery: each agent exports state to a known location, and the coordinator loads a manifest on resume | **Objective map:** each agent saves its state; the coordinator reloads it after a crash. |
| S1 | **Skill:** Spawning subagents to investigate specific questions (e.g., "find all test files," "trace refund flow dependencies") while the main agent preserves high-level coordination | **Story:** helpers answer narrow questions ("find all reminder jobs"). |
| S2 | **Skill:** Having agents maintain scratchpad files recording key findings, referencing them for subsequent questions to counteract context degradation | **Objective map:** keep and reuse the scratchpad. |
| S3 | **Skill:** Summarizing key findings from one exploration phase before spawning sub-agents for the next phase, injecting summaries into initial context | **How it works:** summarise one phase before starting the next. |
| S4 | **Skill:** Designing crash recovery using structured agent state exports (manifests) that the coordinator loads on resume and injects into agent prompts | **Objective map:** crash recovery from a manifest. |
| S5 | **Skill:** Using /compact to reduce context usage during extended exploration sessions when context fills with verbose discovery output | **Practice question:** when context fills up, use /compact. |

#### Write-up 29 · Objective 5.5: Design human review workflows and confidence calibration

**Write-up:** Which Answers Need a Human Look?  
**ParentPace moment:** Routing low-confidence intake extractions to a human coach  
**Status:** Planned

**Coverage map:** every knowledge (K) and skill (S) statement in this objective, and where the article covers it. Sections: Story, How it works, Objective map, Exam trap, Practice question.

| # | Exam statement (from the guide) | How our article covers it |
|---|---|---|
| K1 | **Knowledge:** The risk that aggregate accuracy metrics (e.g., 97% overall) may mask poor performance on specific document types or fields | **Story:** 97% overall accuracy hid that one form type failed half the time. |
| K2 | **Knowledge:** Stratified random sampling for measuring error rates in high-confidence extractions and detecting novel error patterns | **How it works:** random samples by type keep checking even the high-confidence results. |
| K3 | **Knowledge:** Field-level confidence scores calibrated using labeled validation sets for routing review attention | **Objective map:** per-field confidence, calibrated on a labelled set. |
| K4 | **Knowledge:** The importance of validating accuracy by document type and field segment before automating highconfidence extractions | **Exam trap:** check accuracy by form type and field before cutting human review. |
| S1 | **Skill:** Implementing stratified random sampling of high-confidence extractions for ongoing error rate measurement and novel pattern detection | **Objective map:** ongoing stratified sampling. |
| S2 | **Skill:** Analyzing accuracy by document type and field to verify consistent performance across all segments before reducing human review | **Story:** accuracy by form type and field, before trusting automation. |
| S3 | **Skill:** Having models output field-level confidence scores, then calibrating review thresholds using labeled validation sets | **Practice question:** calibrate review thresholds with a labelled set. |
| S4 | **Skill:** Routing extractions with low model confidence or ambiguous/contradictory source documents to human review, prioritizing limited reviewer capacity | **Story:** low-confidence or contradictory forms go to a human coach first. |

#### Write-up 30 · Objective 5.6: Preserve information provenance and handle uncertainty in multisource synthesis

**Write-up:** Two Experts, Two Answers on Time-Outs. Which One Wins?  
**ParentPace moment:** Conflicting sources in the research report  
**Status:** Planned

**Coverage map:** every knowledge (K) and skill (S) statement in this objective, and where the article covers it. Sections: Story, How it works, Objective map, Exam trap, Practice question.

| # | Exam statement (from the guide) | How our article covers it |
|---|---|---|
| K1 | **Knowledge:** How source attribution is lost during summarization steps when findings are compressed without preserving claim-source mappings | **Story:** after summarising, nobody knew which study said what. |
| K2 | **Knowledge:** The importance of structured claim-source mappings that the synthesis agent must preserve and merge when combining findings | **How it works:** every claim keeps its source through every step. |
| K3 | **Knowledge:** How to handle conflicting statistics from credible sources: annotating conflicts with source attribution rather than arbitrarily selecting one value | **Story:** two experts disagree on time-outs; the report shows both, with sources, instead of picking one. |
| K4 | **Knowledge:** Temporal data: requiring publication/collection dates in structured outputs to prevent temporal differences from being misinterpreted as contradictions | **Exam trap:** a 2015 and a 2025 figure aren't a contradiction; dates must travel with the data. |
| S1 | **Skill:** Requiring subagents to output structured claim-source mappings (source URLs, document names, relevant excerpts) that downstream agents preserve through synthesis | **Objective map:** helpers return claim, source and excerpt together. |
| S2 | **Skill:** Structuring reports with explicit sections distinguishing well-established findings from contested ones, preserving original source characterizations and methodological context | **How it works:** the report separates settled findings from debated ones. |
| S3 | **Skill:** Completing document analysis with conflicting values included and explicitly annotated, letting the coordinator decide how to reconcile before passing to synthesis | **Objective map:** conflicting values are kept and flagged; the coordinator decides. |
| S4 | **Skill:** Requiring subagents to include publication or data collection dates in structured outputs to enable correct temporal interpretation | **Practice question:** require publication dates in helper output. |
| S5 | **Skill:** Rendering different content types appropriately in synthesis outputs—financial data as tables, news as prose, technical findings as structured lists—rather than converting everything to a uniform format | **Objective map:** numbers as tables, news as prose, findings as lists. |

## Format for every write-up (example: objective 1.1)

Every objective article follows the same shape, so readers always know where they are:

1. **Title + objective line.** "Exam objective 1.1: Design and implement agentic loops for autonomous task execution" (exact wording from the guide).
2. **The ParentPace moment (3 to 4 lines).** *A parent asks to move Saturday's coaching session. The agent checks the coach's calendar, books the new slot, and replies "All done!" ... but the code stopped the loop the moment it saw the word "done", before the confirmation email tool ran.*
3. **How it really works (plain words, one analogy).** *The loop: ask Claude → it asks for a tool (stop_reason "tool_use") → run the tool, add the result to the conversation → ask again → until stop_reason is "end_turn". Like a waiter who keeps coming back to the kitchen until the order is complete, and only the order slip says when it's complete.*
4. **The objective map + coverage table.** At the end of every article, a short table lists each knowledge and skill statement from the guide (K1, K2, S1...) and the section that covers it, so readers can see nothing was skipped.
   **Objective map.** One line for every knowledge and skill point in the guide, so nothing is missed. *For 1.1: the lifecycle; adding tool results to history; model-driven vs fixed sequences; continue on tool_use, stop on end_turn; avoid the three anti-patterns: reading "done" in the text, iteration caps as the main stop, checking for text as a finish signal.*
5. **Exam traps (2 or 3 lines).** What a tempting wrong answer looks like. *"Add a 10-step cap" sounds safe; the exam expects stop_reason as the primary signal, with caps only as a safety net.*
6. **One practice question** in the exam's style, plus a **practice set of 10 questions** (about 10 minutes), with answers and reasons at the end.
   **Difficulty: as hard as the official sample questions, never easier.** Each question starts from a production symptom (logs, percentages, a failing case) and asks for the "most effective change" or "best first step". All four options must sound plausible: the usual distractors are prompt-only fixes, over-engineering (classifiers, routing layers, extra agents), symptom patches (bigger caps, more retries) and fixes for a different problem. Include one or two "choose 2" items. Every answer names the root cause and says why each wrong option fails.
7. **Confidence line.** "You can now: ..." in one sentence.

**Lengths:** post at most 15 seconds (about 55 words); the main article at most 2 minutes (about 400 words). The 10-question practice set and coverage table come after the main read and don't count.

**Course companion** (`NN-slug.course.md`): every knowledge and skill point explained, a short code sketch, 3 more practice questions, and links to Anthropic's documentation.

**Sources:** the official exam guide and Anthropic's documentation only. Course slides are used only to check coverage; no slide text, diagrams or examples are reused. Every post says it isn't an official Anthropic resource and that ParentPace here is fictional.
