# Lesson 1.1: Agentic Loops (course companion)

*Claude Architect exam prep, Domain 1. Not for LinkedIn.*

## Learning objective

After this lesson, you can implement an agentic loop that runs tools while Claude asks for them, feeds every result back, and stops only when Claude signals it has finished.

## Deep dive

**The lifecycle.**
1. Send `messages` (and `tools`) to the Messages API.
2. Inspect `stop_reason` on the response.
3. If `"tool_use"`: append the assistant message as returned (it contains one or more `tool_use` blocks), run each requested tool, then append a `user` message containing a `tool_result` block for each, matched by `tool_use_id`. Loop.
4. If `"end_turn"`: Claude has finished; return the final answer.

**Why results must go back.** Claude has no memory between requests other than the messages you send. If a tool result isn't appended, Claude doesn't know the booking succeeded and may book again.

**Model-driven vs pre-configured.** In a model-driven loop, Claude decides which tool to call next from the context (calendar busy → offer alternatives; slot free → book). A pre-configured sequence (always check → book → email) is predictable but brittle when something unexpected happens. The exam favours model-driven loops for open-ended tasks, with code-enforced guardrails where guarantees are needed (see objective 1.4).

**The three anti-patterns.**
- Parsing natural-language signals ("done", "finished") to stop.
- An arbitrary iteration cap as the primary stop. A cap is fine as a safety net against runaway loops, not as the main signal.
- Treating "the reply contains text" as completion. A response can contain text and `tool_use` blocks together.

**Other stop reasons.** The API can also stop with reasons such as `"max_tokens"`. Handle them explicitly (for example, continue or raise an error) rather than treating them as "finished". The exam objective focuses on `"tool_use"` vs `"end_turn"`.

## Code sketch (Python, simplified)

```python
messages = [{"role": "user", "content": "Can we move Saturday's session to Sunday?"}]
for _ in range(MAX_SAFETY_ROUNDS):          # safety net only
    response = client.messages.create(model=MODEL, tools=TOOLS, messages=messages, max_tokens=1024)
    messages.append({"role": "assistant", "content": response.content})
    if response.stop_reason == "end_turn":
        break                                  # primary stop signal
    if response.stop_reason == "tool_use":
        results = []
        for block in response.content:
            if block.type == "tool_use":
                output = run_tool(block.name, block.input)
                results.append({"type": "tool_result", "tool_use_id": block.id, "content": output})
        messages.append({"role": "user", "content": results})
```

## Hands-on lab

1. Give Claude three tools: `check_calendar`, `book_session`, `send_confirmation`.
2. Build the loop above; log `stop_reason` each round.
3. Break it on purpose: stop on the word "done"; skip appending results; cap at 2 rounds. Observe each failure.
4. Fix it and confirm the email is always sent.

## More practice questions

The article itself now has a 10-question practice set. Three extra ones for the course:

1. Claude's reply contains "Let me check that for you." and a `tool_use` block. What should the loop do? *Run the tool, append the result, and continue. Text alone doesn't mean finished.*
2. A team caps loops at 3 rounds "to save cost", and complex requests fail. Best change? *Make `stop_reason` the primary stop; keep a higher cap only as a safety net, and control cost with other means.*
3. Why did the agent book the same slot twice? *The booking's tool result wasn't appended, so Claude didn't know it had succeeded.*

## Checklist line (for the domain checkpoint)

- [ ] Loop continues on "tool_use", stops on "end_turn", appends every tool result, and avoids the three anti-patterns.

## Further reading

- Anthropic documentation: tool use with Claude (handling `stop_reason`, `tool_use` and `tool_result` blocks).
- The official exam guide, objective 1.1.
