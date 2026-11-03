# Lesson 6.5: Service targets and incidents for AI answers (course companion)

*Module 6: Observability. Not for LinkedIn.*

## Learning objective

After this lesson, you can set service targets for both availability and correctness, and write an incident plan that treats a wrong answer as an incident.

## The story

Read the article: [05-up-or-right.md](05-up-or-right.md). Running example: a food-delivery support bot with 99.9% uptime over 30 days, while 12% of its delivery-time answers are wrong. The dashboard is green and the bot is still failing its customers.

## Deep dive

**Uptime measures response, not correctness.** A service can answer on time and still give the wrong result. For AI systems, uptime is necessary but not enough. A dashboard that shows only availability will look healthy during the failures customers notice most.

**Service targets.** A target is a number the team promises and measures. For an AI assistant, useful targets include:

- **Availability:** the share of requests that get a response.
- **Correctness:** the share of canary and gold-set checks that pass.
- **Refusal balance:** over-refusal and under-refusal rates, each with an agreed limit.

Show all targets together. A green availability bar should never be the only thing a manager sees.

**Incidents for wrong answers.** An incident is any event that affects customers. For an AI assistant, a cluster of wrong answers counts, even when every server is up. A simple plan has four steps:

1. **Detect:** a canary, an alert or a complaint raises the flag.
2. **Contain:** switch the risky answer path off, or hand customers to a person.
3. **Find the cause:** check the logs for what the assistant read and which change came first.
4. **Learn:** add a canary, a test or a check for the failure, so it is caught next time.

**Who owns it.** Name a person who can switch the risky path off on the same day. Without an owner, containment waits for a meeting.

**Limits.** Targets set too high create constant alerts, and teams learn to ignore them. Set the first targets from current performance, then tighten them as the system improves.

## Hands-on lab

1. Measure availability and a correctness check for a small assistant over one day.
2. Set one target for each, based on the measured value, and write one sentence on why that level is right.
3. Write the four-step incident plan for a wrong delivery-time answer, with one named owner.
4. Run a tabletop exercise: a teammate reads out a wrong answer, and you walk through the four steps.

## Quiz

1. Why is uptime not enough to judge an AI assistant? *Because an assistant can respond on time and still give wrong answers.*
2. What are the three kinds of target in the lesson? *Availability, correctness and refusal balance.*
3. Why treat a wrong answer as an incident? *Because it affects customers, even when every server is up.*
4. Why set early targets from current performance? *So the targets are reachable and alerts stay useful.*

## Checklist line

- [ ] Availability and correctness targets sit on the same dashboard, and a four-step incident plan with a named owner covers wrong answers.

## Glossary

- **Service target:** a number the team promises and measures, such as availability or correctness.
- **Incident:** any event that affects customers, including a cluster of wrong answers.
- **Containment:** the step that limits customer harm while the cause is found.
- **Tabletop exercise:** a practice run of an incident, talked through without a real failure.

## Further reading

- Your team's existing incident process: extend it for wrong answers.
- Your own dashboard: check which targets it shows today.

## Reader questions

- Who could switch your assistant's risky answer path off today, and how fast?
- Which of your dashboard numbers measures correctness rather than uptime?
