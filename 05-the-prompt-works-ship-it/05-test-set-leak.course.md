# Lesson 5.5: Test-set leakage (course companion)

*Module 5: Evals. Not for LinkedIn.*

## Learning objective

After this lesson, you can split test questions into a tuning set and a held-back set, and set up a build check that catches held-back questions leaking into the prompt.

## The story

Read the article: [05-test-set-leak.md](05-test-set-leak.md). Running example: an HR policy assistant scores 98% on its test set, because all 50 test questions were pasted into the prompt as examples. It learned the test, not the policy.

## Deep dive

A **leak** happens when the questions used to measure the assistant influence how it is built. The score then measures memory of the test, not skill on new questions. A high test score is only useful if the test was kept out of the building.

**How leaks happen.** Leaks are usually accidental:

- **Copy-paste fixes:** a failing question is added to the prompt as an example, so it stops failing.
- **Shared examples:** few-shot examples in the prompt are drawn from the test set.
- **Repeated tuning:** the prompt is changed until the test score rises, and each change fits the test a little more.

**Two sets, two jobs.** Split the questions before tuning starts:

- **Tuning set:** questions the team looks at while improving the prompt. Its score guides changes, and it is expected to rise.
- **Held-back set:** questions nobody reads until release. Its score is the honest check.

Report the held-back score as the result. The tuning score is a guide, not proof.

**Keep it out of the prompt.** Store the held-back set where the prompt cannot read it, and keep it out of examples, daily runs and shared prompt notes. Refresh it with new real questions from time to time, so it does not go stale. A refreshed set still needs the same protection.

**Check for copies in the build.** A build check can search the prompt for the exact text of each held-back question, and fail when one appears. Exact matching misses paraphrases, so the held-back set should stay small and private. This check is a guard, not a full answer.

**Limits.** A held-back set is only useful if it resembles real questions. If it is too easy, the honest score is still inflated. Compare it with questions from real users now and then.

## Hands-on lab

1. Take 30 test questions for a small policy assistant. Split them into 20 tuning and 10 held-back questions.
2. Tune the prompt using only the tuning set. Record both scores after each change.
3. Write a build check that fails if any held-back question text appears in the prompt file.
4. Paste one held-back question into the prompt on purpose, run the check, and confirm it fails.

## Quiz

1. What is a leak in evals? *When the test questions influence how the assistant is built, so the test score no longer measures skill on new questions.*
2. Why keep a held-back set? *Because its score is the honest check, which the team has not tuned against.*
3. What does a text-match check miss? *Paraphrases of a held-back question.*
4. Why refresh the held-back set? *To keep it close to real questions, so it does not go stale.*

## Checklist line

- [ ] Held-back test questions are kept out of the prompt and the team's daily runs, and a build check fails when they appear.

## Glossary

- **Leak (test-set leak):** test questions that influence how a system is built, inflating its test score.
- **Tuning set:** the questions used while improving the prompt.
- **Held-back set:** the questions kept hidden until release, used for the honest score.
- **Paraphrase:** the same question in different words, which a text check can miss.

## Further reading

- Your own held-back set: the first place to check for leaks.
- Documentation for evaluation tools, such as RAGAS and OpenAI Evals, for splitting and tracking test sets.

## Reader questions

- Are any of your test questions currently pasted into the prompt or its examples?
- Which real user questions from last month would make a good refresh for the held-back set?
