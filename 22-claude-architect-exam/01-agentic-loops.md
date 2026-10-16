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

## Practice set: 10 more questions

*Exam-style: a real symptom, four plausible fixes. About 10 minutes. Answers and reasons below.*

**1.** Logs show that 8% of reschedule requests end with "All done!" but no confirmation email. The loop code ends when the reply text contains "done". What change most effectively fixes this?

- **A.** Add a system prompt rule: "Only say done after the confirmation email is sent."
- **B.** Keep looping while `stop_reason` is `"tool_use"`, end on `"end_turn"`, and keep a high step cap only as a safety net.
- **C.** Add few-shot examples showing the email being sent before the final reply.
- **D.** Before ending, check that the reply text also contains "email sent".

**2.** In about 5% of conversations, Claude books the same slot twice. The booking tool returns success. After running a tool, the code adds Claude's reply to the conversation and calls Claude again, but adds nothing else. What's the most likely cause?

- **A.** Random variation in the model; lower the temperature.
- **B.** The booking result is never returned as a tool result linked to Claude's tool request, so Claude doesn't know it succeeded.
- **C.** The booking tool's description is unclear.
- **D.** The booking system doesn't block duplicates.

**3.** To control cost, every loop ends after 4 rounds. Parents with multi-part requests (reschedule, change coach, ask for a refund) get no final answer about 20% of the time. What's the best change?

- **A.** Raise the limit to 12 rounds.
- **B.** End on `stop_reason: "end_turn"`, keep a much higher cap only for runaway loops, and track how many rounds requests really need.
- **C.** Split every multi-part request into separate conversations before the agent starts.
- **D.** Tell Claude in the prompt to finish within 4 tool calls.

**4.** Parents sometimes receive "Let me check the coach's calendar..." as the final reply. The code returns as soon as a response contains any text. What should change?

- **A.** Tell Claude not to narrate what it's about to do.
- **B.** Decide based on `stop_reason`. Text that comes with a tool request means the loop continues.
- **C.** Only treat replies longer than 50 characters as final.
- **D.** Wait a moment, then call Claude again for a "real" answer.

**5.** ParentPace's code runs the same fixed sequence for every message: check plan, check calendar, book, email. When a parent asks "How much is my plan?", the code still tries to book a session and fails. What's the best redesign?

- **A.** A model-driven loop where Claude chooses tools based on the request, with code-enforced checks only for steps that must always happen (like checking the plan before a paid booking).
- **B.** Add an if/else branch for each type of question.
- **C.** Add a classifier that routes each message to a different fixed sequence.
- **D.** Keep the sequence, but tell Claude in the prompt to skip steps that aren't needed.

**6.** *(Choose 2.)* Which make the loop's stopping decision reliable?

- **A.** Ending when `stop_reason` is `"end_turn"`.
- **B.** Ending when Claude's text includes "finished" or "all done".
- **C.** Keeping a maximum-rounds cap only as a safety net against runaway loops.
- **D.** Ending as soon as a response contains any text.

**7.** Claude's reply contains two tool requests: check the calendar and look up the parent's plan. The code runs only the first, returns its result, and calls Claude again. What should it do instead?

- **A.** Keep running only the first; Claude will ask again for the second.
- **B.** Run both, and return both results together before calling Claude again.
- **C.** Run both, but send each result in a separate call to Claude.
- **D.** Ask the parent which tool to run first.

**8.** Long coaching summaries are sometimes cut off mid-sentence. The loop treats every reply that isn't `"tool_use"` as finished, including ones that stop with `"max_tokens"`. What's the best fix?

- **A.** Handle `"max_tokens"` explicitly (allow more room or continue the response) instead of treating it as finished.
- **B.** Tell Claude in the prompt to write shorter summaries.
- **C.** Add a step cap so summaries end sooner.
- **D.** Remove the summary feature.

**9.** A nightly job always does the same three steps: fetch tomorrow's sessions, draft reminder texts, queue them. The team asks whether it should be a model-driven agent loop. What's the best answer?

- **A.** Yes. Model-driven loops are always better.
- **B.** No. A fixed sequence fits: the steps never change, and predictability matters more than flexibility here.
- **C.** Use several agents, one per step.
- **D.** Use a model-driven loop with a 3-round cap.

**10.** A loop sometimes runs 40+ rounds, calling `check_calendar` again and again. The calendar tool returns just the word "error" when the service is busy. What's the best first step?

- **A.** Lower the cap to 10 rounds.
- **B.** Return a clear tool result that says what failed and whether it's worth retrying, so Claude can decide to wait, try something else or tell the parent.
- **C.** Add a prompt rule: "Never call check_calendar more than twice."
- **D.** End the loop whenever the same tool is called twice in a row.

**Answers**

1. **B.** The root cause is how the loop decides to stop. A and C rely on the model's wording (probabilistic). D is the same mistake: reading text to decide.
2. **B.** Claude only knows what's in the conversation; without the tool result, it doesn't know the booking worked. D is a useful extra safeguard, but doesn't fix the cause. A and C don't match the symptom.
3. **B.** A still uses a cap as the main stop, just a bigger one. C is over-engineered. D is a prompt-based limit that would still cut real work short.
4. **B.** A reply can contain text and a tool request together. A, C and D are workarounds that ignore the real signal.
5. **A.** Fixed sequences break on requests they didn't expect. B and C keep growing rigid rules. D still forces a fixed path and relies on the prompt.
6. **A and C.** B and D are the classic anti-patterns: reading words, and treating any text as "finished".
7. **B.** Every tool request in a reply needs its result before the next call. A and D stall the work. C splits results that belong together.
8. **A.** `"max_tokens"` means "cut off", not "finished". B and C hide the problem. D removes value instead of fixing the loop.
9. **B.** Model-driven loops are for open-ended work. A fixed, repeatable job is simpler, cheaper and more predictable as a fixed sequence. C and D add complexity for no gain.
10. **B.** The model can only make good choices with useful information. A and D cut work short without fixing the cause. C is a brittle prompt rule. (Objective 2.2 goes deeper on error results.)

## Did this cover the exam objective?

| Exam statement | Covered in |
|---|---|
| K1 The loop: send, check stop_reason, run tools, return results | How it really works |
| K2 Tool results added to the conversation | How it really works, the moment |
| K3 Model-driven vs pre-set decision trees | How it really works |
| S1 Continue on "tool_use", stop on "end_turn" | How it really works, practice question |
| S2 Add tool results between rounds | The moment (booked twice) |
| S3 Avoid the three stopping anti-patterns | Exam traps |

*Answer to the first practice question: B. A and C treat symptoms. D stops too early, because text can come with a tool request.*

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
