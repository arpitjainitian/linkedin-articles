# Lesson 2.5: Agents Stuck in Loops (course companion)

*Module 2: From answers to actions. Not for LinkedIn.*

## Learning objective

After this lesson, you can bound any agent with step limits, stop conditions and budgets, and design a clean handover when it gets stuck.

## The story

Use [05-forty-times.md](05-forty-times.md): one blurry receipt, 40 re-upload requests, a pending claim, a bill bigger than the taxi fare.

## Deep dive

**Why loops happen.** An agent repeats think, act, observe. If the observation never changes (a blurry image stays blurry), and the instructions say "make sure the amount is correct", the model keeps trying. Each step is locally reasonable; the system has no global sense of progress.

**Bounds every agent needs.**
- *Step limit:* a hard cap on tool calls per task.
- *Repetition detection:* the same tool with the same arguments, or the same result twice, ends that line of attack.
- *Budgets:* time and token/cost caps per task, checked by code, not by the model.
- *Progress check:* after N steps, require evidence of progress (a new field filled, a new receipt processed).

**Graceful exit.** Hitting a limit is a normal outcome, not a crash. Return a structured handover: what was done, what failed, what was tried, and the suggested next step. Route it to a person or a review queue.

**Prompts help, code decides.** Tell the agent about its limits, but enforce them in the harness. The model can't be trusted to count reliably.

**Related.** AI system design question 2 ("your agent keeps calling the same tool") goes deeper on debugging loops.

## Hands-on lab

1. Give an agent a tool that always returns "amount unclear" for one receipt.
2. Run without limits; record steps and cost.
3. Add a step limit, repetition detection and a cost budget in code; run again.
4. Make the agent return a structured handover when stopped.

## Quiz

1. Why can't the model be trusted to stop itself? *Each step looks reasonable locally; it has no reliable sense of overall progress or cost.*
2. Name two stop conditions. *Step limit; same tool and input repeated; budget exceeded.*
3. What should happen when a limit is hit? *A clean handover to a person with what was tried.*

## Checklist line (for the module finale)

- [ ] Loops: does every task have a step limit, a budget and a handover when it hits them?

## Glossary

Agent loop, step limit, stop condition, budget, repetition detection, handover.

## Further reading

- Agent framework documentation on max iterations and recursion limits.
- AI system design question 2 (21-system-design).

## Reader questions

*(Add good questions and answers from LinkedIn comments here.)*
