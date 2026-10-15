# Lesson 2.7: Testing Agents (course companion)

*Module 2: From answers to actions. Not for LinkedIn.*

## Learning objective

After this lesson, you can test an AI agent on both its outcome and its path, across repeated runs, and turn real failures into regression tests.

## The story

Use [07-two-paths.md](07-two-paths.md): two runs, the same correct claim, one of them submitted before checking the policy.

## Deep dive

**Outcome checks.** Compare the final state (the claim record) with expected values: amounts, dates, category, attachments. Use exact checks for fields, not an LLM's opinion.

**Path checks.** Record every tool call (name, arguments, order, result). Assert path rules:
- ordering rules (policy check before submit; upload before submit),
- safety rules (no duplicate write actions; no tool outside the allowed list),
- efficiency rules (fewer than N steps; cost under budget).

**Repeat runs.** Agents are non-deterministic. Run each scenario 10 to 30 times and report pass rate per scenario. Track it over versions; a drop from 95% to 80% is a regression even if a single run passes.

**Scenario set.** Cover routine claims, edge cases (foreign currency, missing merchant, blurry receipt, timeout) and adversarial ones. Seed it from real production traces (see #JustAddRAG write-up 13 on traces).

**LLM as judge, carefully.** For fuzzy qualities (was the summary to the approver clear?), a judge model can help, but calibrate it against human ratings first (Series 5 goes deeper on auditing judges).

**Simulated tools.** Test against mock versions of the claims system so tests are fast, cheap and can inject failures (timeouts, partial uploads).

## Hands-on lab

1. Log every tool call of your expense agent as a trajectory.
2. Write three path rules and one outcome check.
3. Run 5 scenarios x 10 runs each; produce a pass-rate table.
4. Break the prompt slightly; watch which pass rates drop.

## Quiz

1. Why isn't a correct final claim enough? *The path may break rules, like submitting before checking policy.*
2. Why run each test many times? *Agents vary between runs; one pass hides failures.*
3. Name one path rule. *Policy check must happen before submit.*

## Checklist line (for the module finale)

- [ ] Testing: are agents tested on result and path, over repeated runs, with real failures added as tests?

## Glossary

Trajectory, path rule, outcome check, pass rate, regression, mock tool.

## Further reading

- #JustAddRAG write-up 9 (evals) and 13 (observability).
- Series 5 (evals, one level deeper).

## Reader questions

*(Add good questions and answers from LinkedIn comments here.)*
