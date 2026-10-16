# Lesson 0: The Exam, Mapped (course companion)

*Claude Architect exam prep. Not for LinkedIn.*

## Learning objective

After this lesson, you know the exam's format, weights and scenario style, and have a study plan that covers all 30 objectives.

## Exam facts (official exam guide, Version 1.0, July 2026)

| | |
|---|---|
| Exam code | CCAR-F |
| Questions | 60; multiple choice and multiple response (each says how many to pick) |
| Scenarios | 4 per exam, drawn from a bank of 6 |
| Time | 120 minutes |
| Pass mark | Scaled 720 (100 to 1,000) |
| Weights | D1 27% · D2 18% · D3 20% · D4 20% · D5 15% |

Check the latest guide before booking; details can change.

## The six scenario types, and where ParentPace covers them

| Scenario type in the guide | ParentPace part |
|---|---|
| Customer support resolution agent | Parent-help agent |
| Code generation with Claude Code | Tech team's Claude Code setup |
| Multi-agent research system | Course research team |
| Developer productivity with Claude | Tech team's Claude Code setup |
| Claude Code for continuous integration | Pull-request reviews in CI |
| Structured data extraction | Intake paperwork |

## A 6-week study plan

| Week | Objectives | Plus |
|---|---|---|
| 1 | 1.1 to 1.4 | Build a small agent loop yourself |
| 2 | 1.5 to 1.7, 2.1 to 2.2 | Domain 1 checkpoint |
| 3 | 2.3 to 2.5, 3.1 to 3.3 | Domain 2 checkpoint; set up CLAUDE.md in a real repo |
| 4 | 3.4 to 3.6, 4.1 to 4.2 | Domain 3 checkpoint; run Claude Code with -p in a script |
| 5 | 4.3 to 4.6, 5.1 to 5.2 | Domain 4 checkpoint; build an extraction tool with a JSON schema |
| 6 | 5.3 to 5.6 | Domain 5 checkpoint, mock exam, exam-day sheet |

## How to answer scenario questions

1. Find the constraint in the question: a guarantee is required, cost matters, the reviewer lacks context, and so on.
2. Prefer answers that enforce in code over answers that only "instruct the model better", when a guarantee is required.
3. Distrust answers that fix symptoms (more retries, bigger caps) instead of causes.
4. For multiple-response items, check each option independently.

## Further reading

- The official exam guide (Anthropic Partner Academy).
- Anthropic documentation for the Claude API, Agent SDK and Claude Code.
