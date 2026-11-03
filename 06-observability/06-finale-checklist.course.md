# Lesson 6.6: The observability checklist (course companion)

*Module 6: Observability, finale. Not for LinkedIn.*

## Learning objective

After this lesson, you can apply the five observability checks to an AI assistant, and show what evidence each check needs before a launch decision.

## The story

Read the article: [06-finale-checklist.md](06-finale-checklist.md). Running example: a food-delivery support bot that said "arriving today" for an order delivered a week later. The team learned about it from a complaint. The finale shows the same bot with the signals in place.

## Deep dive

The five checks cover different blind spots. Each one catches a failure the others can miss.

1. **Traces (write-up 1).** Record what the assistant read and which rules applied. Without this, a wrong answer cannot be explained.
2. **Cost and cache (write-up 2).** Silent changes often show first in cost and cache reuse. Alert on both.
3. **Canaries (write-up 3).** Known questions in production catch quiet wrong answers. Watch refusals in both directions.
4. **Faults (write-up 4).** Each key dependency needs a tested timeout, a retry limit and a safe fallback, so one slow service does not fill the queue.
5. **Targets and incidents (write-up 5).** Uptime is necessary but not enough. Put correctness next to it, and give wrong answers an incident plan with a named owner.

**Why all five.** Traces explain a failure after it happens. Cost and canaries reveal it sooner. Fault tests prepare for the failures you can predict. Targets and incidents decide what happens next. Missing any one leaves a gap that customers will find first.

**What to bring to a launch meeting.** A short view of the signals: the trace sample, the cost and cache trend, the canary pass rate, the fault test results, and the two targets with the named incident owner.

**Limits.** Monitoring shows what you chose to measure. A new kind of failure needs a new signal. Review the signals after each incident, and add the one that would have caught it.

## Hands-on lab

1. Draw a one-page signal map for a small assistant, with the five checks as rows.
2. For each row, write what exists today, or "none".
3. Pick the row with "none" that carries the most customer risk. Write the first signal you would add.
4. Run a tabletop incident for one wrong answer. Note which of the five checks would have caught it first.

## Quiz

1. Why use all five checks together? *Because each covers a blind spot the others miss, such as a silent cost change or a dependency that stalls.*
2. What does a launch meeting need to see? *A short view of the traces, cost and cache trend, canary results, fault tests, and the targets with an owner.*
3. Does passing the checklist mean nothing can go wrong? *No. New kinds of failure need new signals, and each incident should add one.*

## Checklist line

- [ ] Before launch: traces, cost and cache alerts, canaries, tested faults, and correctness targets with an incident owner are all in place.

## Glossary

- **Trace:** a record of what an assistant read and which rules it applied for one answer.
- **Canary question:** a known question run in production to detect a change.
- **Incident owner:** the named person who can switch a risky answer path off.
- **Signal map:** a one-page list of the monitoring signals for a system.

## Further reading

- Your own signal map: keep it current after each incident.
- Your team's incident notes: the signals that would have caught past failures.

## Reader questions

- Which of the five checks does your current assistant have the least evidence for?
- Who would you ask to walk through your signal map with you?
