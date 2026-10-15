# Lesson 2.6: Workflow vs Agent (course companion)

*Module 2: From answers to actions. Not for LinkedIn.*

## Learning objective

After this lesson, you can decide, for any task, whether it needs a fixed workflow, an agent, or a mix, and justify the choice with cost, speed and consistency.

## The story

Use [06-need-an-agent.md](06-need-an-agent.md): the monthly phone bill, 12 agent steps, filed under "Travel" twice.

## Deep dive

**Two designs.**
- *Workflow:* code defines the steps; the model is called at specific points (extract fields, classify). Predictable, cheap, easy to test and audit.
- *Agent:* the model chooses the next step and tools in a loop. Flexible for unknown paths, but slower, costlier and less consistent.

**Decision questions.**
1. Can you write the steps down in advance? If yes, workflow.
2. How often does the path change? Rarely: workflow. Often and unpredictably: agent.
3. What does a mistake cost? High cost and compliance needs favour workflows.
4. Is speed or cost critical at volume? Favour workflows.

**Hybrid pattern.** A router or simple rules send routine cases (known vendor, single receipt, within policy) to the workflow and exceptions (foreign currency, missing receipts, unusual vendor) to the agent. Measure the share of each; aim to move recurring exceptions into the workflow over time.

**Common patterns between the two extremes.** Prompt chaining (fixed sequence of model calls), routing (classify then branch), and parallel steps are all workflows with AI inside, and cover most business needs.

**Consistency.** A workflow gives the same category for the same input; an agent may not. For classification inside a workflow, constrain outputs to an allowed list.

## Hands-on lab

1. Implement the phone-bill claim as a workflow: extract fields with structured output, validate, submit.
2. Implement the same as an agent with tools.
3. Run both on 20 similar bills; compare steps, time, cost and category consistency.
4. Add a router: workflow for known vendors, agent for the rest.

## Quiz

1. When is a workflow the better choice? *When the steps are known in advance and consistency matters.*
2. Name one cost of an agent's freedom. *Slower, more expensive, less predictable.*
3. What is a hybrid design? *Workflow for routine cases, agent for exceptions.*

## Checklist line (for the module finale)

- [ ] Agent or workflow: have you justified why each task needs an agent, and used a workflow everywhere else?

## Glossary

Workflow, agent, hybrid, prompt chaining, routing.

## Further reading

- Engineering guides on building effective agents (workflows vs agents).
- Today in AI No. 007 (AI routers).

## Reader questions

*(Add good questions and answers from LinkedIn comments here.)*
