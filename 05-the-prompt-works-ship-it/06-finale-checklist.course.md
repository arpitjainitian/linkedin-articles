# Lesson 5.6: The evals checklist (course companion)

*Module 5: Evals, finale. Not for LinkedIn.*

## Learning objective

After this lesson, you can apply the five evals checks to an AI assistant, and say what evidence each check needs before a launch decision.

## The story

Read the article: [06-finale-checklist.md](06-finale-checklist.md). Running example: an HR policy assistant that began with "we tried it, it works", and ended with a scorecard the team can check.

## Deep dive

The five checks from this module work together. Each one closes a gap that the others cannot see.

1. **Sources (write-up 2).** A right answer from the wrong source is a failure. Store the expected source in each test case.
2. **Grader (write-up 3).** An AI grader is a model with its own tastes. Measure it against people on a gold set, and use yes-or-no checks.
3. **Gates (write-up 4).** An average can hide a failing high-risk category. Set a threshold per category, from risk, before testing.
4. **Held-back set (write-up 5).** A test you have studied measures memory. Keep some questions out of the prompt, and guard them with a build check.
5. **Every change.** Each prompt, model or data change can move any of the above. Run the same tests again every time.

**Why all five.** Each check fails alone in a familiar way. Sources alone miss a grader that favours polite wrong answers. A grader alone misses a category nobody gates. Gates alone can be gamed by tuning to the test. Together they give evidence that is hard to fake by accident.

**What to bring to a launch meeting.** A short scorecard: the gate per category with results, the held-back score, the grader's agreement rate, and the list of source checks. Anyone should be able to read it in five minutes.

**Limits.** No checklist proves an assistant is safe. Evals show how it performs on the questions you tested. New kinds of question still need new tests, and production logs show what the tests missed.

## Hands-on lab

1. Build a one-page scorecard for a small policy assistant with the five checks as rows.
2. For each row, write the current evidence, or "none" if there is none.
3. Pick the one row with "none" that carries the most risk. Write the first test that would fill it.
4. Share the scorecard with one person outside the build team and note the questions they ask.

## Quiz

1. Why are the five checks used together? *Because each check misses a failure the others can catch, such as a biased grader or a gated category that was never tested.*
2. What should a launch meeting see? *A short scorecard with the gates, the held-back score, the grader agreement and the source checks.*
3. Does passing the checklist prove the assistant is safe? *No. It shows performance on the tested questions, and new kinds of question still need new tests.*

## Checklist line

- [ ] Before launch: sources, grader, gates, held-back set and repeat runs are all in place, and the scorecard is readable by someone outside the team.

## Glossary

- **Scorecard:** a one-page summary of the evals evidence for a launch decision.
- **Gold set:** human-checked answers used to test the grader.
- **Held-back set:** questions kept out of the prompt, used for the honest score.
- **Release gate:** a threshold that must be met before a category can ship.

## Further reading

- Your own scorecard: the artefact to keep current.
- Documentation for evaluation tools, such as RAGAS and OpenAI Evals, for reporting patterns.

## Reader questions

- Which of the five checks does your project have least evidence for?
- Who outside the build team would you ask to read your scorecard?
