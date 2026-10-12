# AI System Design, B1: Your AI Agent Is Accurate, But Token Usage Keeps Climbing. How Would You Fix It?

*System design series, part B: AI system design in production.*

**The question:** You have an AI agent in production. Its answers are accurate, but token usage keeps climbing every week. How would you fix it?

## First, what's really being asked

Tokens are what you pay for, and what you wait for. If usage keeps climbing while the work stays the same, the agent is getting more expensive and slower for no extra value.

The catch is in the word "accurate". The goal is not "use fewer tokens". It's "use fewer tokens **without losing accuracy**". Any fix that saves money but breaks answers is a bad fix.

## Step 1: Measure before you cut

Don't guess. Break every request into where its tokens go:

- **The instructions** (system prompt)
- **The chat history** carried from earlier turns
- **Retrieved documents** (if it uses RAG)
- **Tool results** fed back to the model
- **Agent steps** (how many times it thinks and acts per request)
- **The answer** it writes
- **Retries** after errors or timeouts

Then plot each one over time. The one that's growing is your problem. "Climbing every week" almost always means something grows with time or usage, not with the question.

## Step 2: The usual suspects, and their fixes

| What's growing | Why it happens | Fix |
|---|---|---|
| Chat history | Every turn resends the whole conversation | Keep the last few turns, summarise older ones |
| Agent steps | The agent loops, re-plans or re-checks | Set a step limit and stop when the task is done |
| Tool results | Full API responses dumped into the prompt | Return only the fields the agent needs |
| Retrieved documents | Too many chunks, no relevance cut-off | Fewer, better chunks: a minimum score, re-ranking |
| Instructions | Every bug fix adds another paragraph | Trim and test the prompt, remove dead rules |
| Repeated work | Same questions, same context, paid every time | Prompt caching for the fixed part, answer caching for repeats |
| Model choice | The biggest model does every step | Route simple steps to a smaller, cheaper model |
| Answer length | No limit on output | Set a max length, ask for structured output |
| Retries | Timeouts and errors resend the full prompt | Fix the root cause, back off, cap retries |

## Step 3: Protect accuracy

Before changing anything, freeze a test set of real questions with known good answers. After each fix, run it again.

- Accuracy holds and tokens drop: keep the change.
- Accuracy drops: roll it back, or apply the fix only to the easy cases.

Change one thing at a time, so you know which fix did what.

## Step 4: Stop it creeping back

- A **token budget** per request and per user, with an alert when it's crossed.
- A **dashboard** of tokens per request, split by part (instructions, history, tools, answer).
- **Evals in the release process**, so every prompt or model change shows its cost and accuracy side by side.

## The trade-off in one line

Cost vs accuracy. You're not trying to minimise tokens. You're trying to remove the tokens that don't help the answer.

## Simple diagram idea

One request split into stacked bars (instructions, history, retrieved docs, tool results, steps, answer), week 1 next to week 8. The bar that grew is the one to fix.

## What I'd say in the room

1. "First I'd measure where the tokens go per request, split by part, and see which one is growing week on week."
2. "Then I'd fix the growing part: trim history, cap agent steps, slim tool results, tighten retrieval, cache the stable prompt and route easy steps to a smaller model."
3. "And I'd guard accuracy with a fixed eval set run before and after every change, plus a token budget and alerts so it can't creep back."

## Related

- #JustAddRAG write-up 10: "A few cents per question: so why is finance calling?" (cost)
- Series 5, "What's a few cents between friends?" (AI cost, in depth)

## Source

S1: question shared by Arpit.

---

**Post text (copy and paste):**

```
System design question (AI in production):

Your AI agent's answers are accurate. But token usage keeps climbing every week. How would you fix it?

My answer in 3 steps:

1. Measure first. Split every request into instructions, chat history, retrieved docs, tool results, agent steps, answer and retries. Find the part that's growing.

2. Fix the growing part. Trim old history, cap agent steps, return only needed fields from tools, tighten retrieval, cache the stable prompt, route easy steps to a smaller model.

3. Guard accuracy. Run the same test set before and after every change. Add a token budget and alerts so it can't creep back.

The goal isn't fewer tokens. It's removing the tokens that don't help the answer.

How would you approach it?

#SystemDesign #AIEngineering #GenAI #LLMOps #AIAgents
```
