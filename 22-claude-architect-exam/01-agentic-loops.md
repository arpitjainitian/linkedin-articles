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
2. **Read `stop_reason`.** `"tool_use"` means Claude wants a tool. Claude only asks. **Your code** runs the tool (check the calendar, book the slot, send the email).
3. **Add Claude's reply, then the tool's result**, linked to the request by its ID (`tool_use_id`). Send it all again.
4. **Stop** only on `"end_turn"`. Claude has finished.

Like a waiter going back and forth to the kitchen. The order slip says when the order is complete, not the waiter's cheerful "nearly there!".

Claude remembers nothing between calls. If a result isn't in the conversation, as far as Claude knows, it never happened.

## Four details the exam checks

- **Two tool requests in one reply?** Run both. Send both results back together.
- **`"max_tokens"`** means cut off, not finished. Continue, or give it more room.
- **Model-driven beats a fixed script** for open-ended requests: Claude picks the next tool from what it just learned. But a job whose steps never change (nightly reminders) is simpler as plain code.
- **Steps that must always happen** (check the plan before a paid booking) are enforced in code, not in the prompt. More in objective 1.4.

## Exam traps

The exam loves three wrong ways to stop:

- **Reading the words.** Stopping because the text says "done".
- **A step cap as the main stop.** "Stop after 5 rounds" ends real work early. Keep a cap only as a safety net.
- **"There's text, so it's finished."** Claude can write text *and* ask for a tool in the same reply.

If the loop's logic is wrong, a prompt rule won't fix it. Fix the code.

## Practice question

ParentPace's agent sometimes ends without sending the confirmation email. The loop exits when the reply contains "done", or after 5 rounds. What's the most effective fix?

- **A.** Raise the cap to 15 rounds, since logs show the longest requests need about 12.
- **B.** Add a rule to the system prompt and the tool description: never say "done" until the confirmation email is sent.
- **C.** Continue while `stop_reason` is `"tool_use"`, stop on `"end_turn"`, and keep a high cap only as a safety net.
- **D.** End the loop on the first reply that has no tool request, since that means Claude has finished.

*Answer at the end.*

## Words to know

- **Agentic loop:** ask, run tools, add results, repeat, until the model finishes.
- **stop_reason:** the field that says why Claude stopped this turn. *"tool_use" or "end_turn".*
- **Tool result:** what a tool returned, sent back so Claude can decide the next step.
- **tool_use_id:** the ID that links each tool result to the request it answers.

**You can now:** design a loop that stops for the right reason.

## Practice set: 10 more questions

*Exam-level: every option sounds reasonable; pick the best one. About 12 minutes. Answers and reasons below.*

**1.** After adding tool results, every second round fails with an API error: a tool result has no matching tool request. The code adds a user message with the `tool_result` blocks, but nothing else, after each tool runs. What's the fix?

- **A.** Generate `tool_use_id` values in ParentPace's code, so the IDs on the results are always valid.
- **B.** Send the result as plain text in a user message instead of a `tool_result` block, so no ID matching is needed.
- **C.** Add Claude's full reply (with its `tool_use` blocks) to the history first, then the user message with the matching `tool_result` blocks.
- **D.** Send the tool definitions again with every request, so the API can match each result to its tool.

**2.** In about 5% of conversations, Claude books the same slot twice. The booking tool returns success every time. After a tool runs, the code adds Claude's reply to the history and calls Claude again, and adds nothing else. What's the root cause?

- **A.** Sampling randomness makes the model repeat actions now and then; setting temperature to 0 would make the booking decision deterministic.
- **B.** The `book_session` description doesn't say that a second call creates a second booking, so the model treats retries as harmless.
- **C.** The booking service has no duplicate check, so it accepts the second request instead of rejecting it.
- **D.** The booking result never reaches the conversation as a tool result linked to the request, so Claude has no evidence that the booking happened.

**3.** To control cost, every loop ends after 4 rounds. Parents with multi-part requests (reschedule, change coach, ask for a refund) get no final answer about 20% of the time. Finance still wants spending kept in check. What's the best change?

- **A.** Make `"end_turn"` the main stop, set the cap well above normal use as a safety net for runaway loops, and track rounds per request.
- **B.** Raise the cap to 12 rounds, which covers the longest requests in last month's logs and still limits cost per conversation.
- **C.** Split each multi-part message into separate single-issue conversations first, so each one fits within 4 rounds.
- **D.** Keep the 4-round cap and tell Claude in the system prompt to group its work so it finishes within four tool calls.

**4.** Parents sometimes get "Let me check the coach's calendar..." as the final reply. The code returns the first response that contains a text block. What should change?

- **A.** Tell Claude in the system prompt not to write text in a reply that also asks for a tool, so text only appears in the final answer.
- **B.** Decide with `stop_reason`: a reply with text and a tool request has `"tool_use"`, so run the tool and keep looping.
- **C.** Treat text as final only when it's longer than a few sentences, since progress notes are short and real answers are longer.
- **D.** Filter out progress phrases such as "Let me check" before replying, and send the rest of the text to the parent.

**5.** ParentPace's code runs the same steps for every message: check plan, check calendar, book, email. When a parent asks "How much is my plan?", it still tries to book and fails. The plan must always be checked before any paid booking. What's the best redesign?

- **A.** Add a classifier in front of the agent that sends each message to one of several fixed sequences, one per type of request.
- **B.** Keep the fixed sequence, and add a system prompt rule telling Claude to skip any step the request doesn't need.
- **C.** Switch to a model-driven loop, with a strong system prompt rule that the plan must always be checked before a paid booking.
- **D.** Switch to a model-driven loop where Claude picks tools from context, and enforce "plan checked before paid booking" in code.

**6.** *(Choose 2.)* The team is reviewing loop designs. Which TWO describe correct stopping behaviour?

- **A.** End when Claude's text includes a phrase like "Your session is booked", since it only appears after a successful booking.
- **B.** Continue while `stop_reason` is `"tool_use"`, and end when it is `"end_turn"`.
- **C.** End on the first reply that has no tool request, whatever its `stop_reason`.
- **D.** End after a fixed number of rounds, set from logs to match the average request.
- **E.** Keep a maximum-round cap well above normal use, only to catch runaway loops.

**7.** One of Claude's replies asks for two tools: `check_calendar` and `get_plan`. The code runs only the first. What should it do?

- **A.** Run only the first and return its result; if Claude still needs the second, it will ask again next round.
- **B.** Run both, then send each result back in its own request, so Claude handles them one at a time.
- **C.** Run both, and return both `tool_result` blocks, each with its matching `tool_use_id`, together in the next message.
- **D.** Tell Claude in the system prompt to ask for only one tool per reply, so the loop stays simple.

**8.** Long coaching summaries are sometimes cut off mid-sentence. The loop treats every reply that isn't `"tool_use"` as finished. What's the best fix?

- **A.** Handle `"max_tokens"` on its own: continue the reply or retry with more room, instead of treating it as finished.
- **B.** Tell Claude in the system prompt to keep summaries under 300 words, so they never reach the limit.
- **C.** Treat any reply that doesn't end with a full stop as unfinished, and ask Claude to complete it.
- **D.** Set `max_tokens` to the model's maximum on every request, so summaries can never be cut off.

**9.** A nightly job always does the same three steps: fetch tomorrow's sessions, draft reminder texts, queue them. The team asks how it should be built. What's the best answer?

- **A.** A model-driven loop, because letting Claude choose the steps makes the job robust to future changes.
- **B.** A fixed sequence in code: the steps never change, and a fixed path is cheaper, faster and easier to test.
- **C.** Three subagents and a coordinator, one per step, so each step can scale on its own.
- **D.** A model-driven loop with a 3-round cap, which keeps it flexible and still ends on time.

**10.** A developer moves tool work to a background queue. The loop sends Claude's tool request to the queue, then immediately calls Claude again with "The result is on its way." Claude replies with a made-up calendar slot. Why?

- **A.** The model needs extended thinking turned on, so it can wait for results that arrive later.
- **B.** The tool's description doesn't say it runs in the background, so Claude didn't know it had to wait.
- **C.** The queue should push the result into the running request when it finishes, and it didn't.
- **D.** Claude can only use what's in the messages it receives; no tool result was there, so it answered without the data.

**Answers**

1. **C.** Every tool result must answer a request that is already in the history. A misunderstands IDs: the API creates them. B throws away the link between request and result. D is unrelated.
2. **D.** Claude only knows what's in the conversation. C is a good extra safeguard, but Claude still wouldn't know the booking worked. A and B don't match the cause.
3. **A.** B still uses a cap as the main stop; the next longer request breaks it. C is over-engineering and loses shared context. D is a prompt rule that still cuts real work short.
4. **B.** A reply can hold text and a tool request together. A relies on the prompt. C and D still treat text as the finish signal; the tool never runs.
5. **D.** Open-ended requests need Claude choosing tools, and a must-happen step needs code. C is close but relies on the prompt for a guarantee. A and B keep rigid scripts.
6. **B and E.** A reads words. C treats a cut-off (`"max_tokens"`) reply as finished. D makes a cap the main stop.
7. **C.** All results for one reply go back together, each linked to its request. A stalls the work. B splits results that belong together. D gives up useful parallel work.
8. **A.** The loop wrongly treats "cut off" as "finished". B and D make it less likely but don't fix the loop. C is a fragile guess based on the text.
9. **B.** Model-driven loops are for open-ended work. A and D add cost and unpredictability for no gain. C is over-engineering.
10. **D.** Claude remembers nothing between calls; the result must be in the messages. C describes something the API doesn't do. A and B don't address the cause.

## Did this cover the exam objective?

| Exam statement | Covered in |
|---|---|
| K1 The loop: send, check stop_reason, run tools, return results | How it really works |
| K2 Tool results added to the conversation | How it really works, the moment |
| K3 Model-driven vs pre-set decision trees | How it really works |
| S1 Continue on "tool_use", stop on "end_turn" | How it really works, practice question |
| S2 Add tool results between rounds | The moment (booked twice) |
| S3 Avoid the three stopping anti-patterns | Exam traps |

*Answer to the first practice question: C. A still makes a cap the main stop. B relies on the model's wording. D treats a cut-off ("max_tokens") reply as finished.*

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
