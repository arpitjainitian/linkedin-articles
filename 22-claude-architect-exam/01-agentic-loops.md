# 1. How Does an Agent Know When to Stop? | Agentic Loops

![Cover](images/01-agentic-loops-cover.png)

*Claude Architect, One Objective at a Time: objective 1.1*

**Exam objective 1.1:** Design and implement agentic loops for autonomous task execution.

## The ParentPace moment

A parent writes: "Can we move Saturday's coaching session to Sunday?"

The AI coach checks the coach's calendar, books Sunday at 10, and replies: "All done!"

But the confirmation email never went out. ParentPace's code stopped the loop the moment Claude's reply contained the word "done". And on another day, the booking result was never sent back to Claude, so it booked the same slot twice.

## How it really works

An agent isn't one question and one answer. It's a loop:

1. **Send** the conversation to Claude.
2. **Read `stop_reason`.** If it's `"tool_use"`, Claude wants a tool: run it (check the calendar, book the slot, send the email).
3. **Add the tool's result** to the conversation, and send it again.
4. **Stop** only when `stop_reason` is `"end_turn"`. Claude has finished.

Like a waiter going back and forth to the kitchen. The order slip says when the order is complete, not the waiter's cheerful "nearly there!".

Claude also chooses which tool comes next, based on what it has learned so far. That's **model-driven**, not a fixed script of if/else steps.

## Exam traps

The exam loves three wrong ways to stop:

- **Reading the words.** Stopping because the text says "done".
- **A step cap as the main stop.** "Stop after 5 rounds" ends real work early. Keep a cap only as a safety net.
- **"There's text, so it's finished."** Claude can write text *and* ask for a tool in the same reply.

## Practice question

ParentPace's agent sometimes finishes without sending the confirmation email. The loop exits when the reply contains "done", or after 5 rounds. What's the best fix?

- **A.** Raise the limit to 15 rounds.
- **B.** Keep looping while `stop_reason` is `"tool_use"`, stop on `"end_turn"`, and keep a cap only as a safety net.
- **C.** Add "never say done until the email is sent" to the prompt.
- **D.** Stop as soon as the reply contains any text.

*Answer at the end.*

## Words to know

- **Agentic loop:** ask, run tools, add results, repeat, until the model finishes.
- **stop_reason:** the field that says why Claude stopped this turn. *"tool_use" or "end_turn".*
- **Tool result:** what a tool returned, sent back so Claude can decide the next step.

**You can now:** design a loop that stops for the right reason.

## Did this cover the exam objective?

| Exam statement | Covered in |
|---|---|
| K1 The loop: send, check stop_reason, run tools, return results | How it really works |
| K2 Tool results added to the conversation | How it really works, the moment |
| K3 Model-driven vs pre-set decision trees | How it really works |
| S1 Continue on "tool_use", stop on "end_turn" | How it really works, practice question |
| S2 Add tool results between rounds | The moment (booked twice) |
| S3 Avoid the three stopping anti-patterns | Exam traps |

*Answer: B. A and C treat symptoms. D stops too early, because text can come with a tool request.*

Next write-up (2): **One coordinator, three helpers: who builds the Calm Parenting course?** (Objective 1.2)

Follow me for the next one. Which of the three traps have you seen in real code?

*ParentPace is fictional. These are my own study notes, not an official Anthropic resource.*

---

**Post text (copy and paste):**

```
"Can we move Saturday's session?"

The AI coach booked Sunday and replied: "All done!"

The confirmation email never went out. The code stopped on the word "done".

Exam objective 1.1: an agent stops on stop_reason "end_turn". Not on its own words. Not on a step count.

Which trap have you seen in real code?

Not an official Anthropic resource. ParentPace is fictional.

#ClaudeCertifiedArchitect #ClaudeArchitectPrep #AIEngineering #AIAgents #Claude
```

**Series index (post as the first comment; also update the pinned comment on write-up 0):**

```
📌 Claude Architect, One Objective at a Time

0. Can a parenting app teach you the Claude Architect exam? [link]
1. How does an agent know when to stop? (you're here, objective 1.1)
2. One coordinator, three helpers: who builds the Calm Parenting course? (next, objective 1.2)
```
