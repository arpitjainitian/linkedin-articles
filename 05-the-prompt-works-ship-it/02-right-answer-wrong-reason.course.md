# Lesson 5.2: Grading each layer (course companion)

*Module 5: Evals. Not for LinkedIn.*

## Learning objective

After this lesson, you can split an assistant's answer into search, rules and answer layers, and write a test that fails when the right answer comes from the wrong source.

## The story

Read the article: [02-right-answer-wrong-reason.md](02-right-answer-wrong-reason.md). Running example: an HR policy assistant. "What's the notice period for my team?" The answer "30 days" is correct for the Mumbai policy, but the employee is in Bengaluru.

## Deep dive

An assistant's answer is the end of a chain. It retrieves passages, applies rules about the person and the context, and then writes the answer. A test that checks only the final text cannot see a broken link in the middle. The score can stay green while the method is wrong.

**Three layers, three scores.**

- **Retrieval:** did the right document appear in the top results? Measure this as a rank, such as "correct passage in the top 3".
- **Rules and context:** was the correct version and location used? This is a check in code. The expected version is known, so the test compares it directly.
- **Answer:** is each claim supported by the passage it relies on, and is anything important missing? This needs a grader, which write-up 3 covers.

**Why a right answer can hide a wrong method.** A policy that never changed, or a question that a general answer covers, can hide the gap. The answer is right today and wrong after the next policy update. Testing only the final text rewards luck.

**Build the test around the source.** Each test case stores the question, the expected answer and the expected source. A case passes only when the answer is right and the source matches. Add pairs of questions that differ only by location, so a wrong location cannot pass by chance.

**Log the path.** In production, log the passage ids and rule versions each answer used. When an answer is later questioned, the log shows whether the method or the luck was at fault.

**Limits.** Source checks need stable ids for passages and policy versions. Without them, the test has nothing to compare. Setting those ids is the first job, before the scores.

## Hands-on lab

1. Write 10 test questions for a small policy set. Include 4 pairs that differ only by location or date.
2. For each question, store the expected answer and the expected source passage.
3. Run the assistant and record three scores: correct passage in the top 3, correct version used, and answer matches the expected facts.
4. Find one case where the answer is right but the source is wrong. Write one sentence on why a final-text test would have missed it.

## Quiz

1. Why can a final-answer test miss a broken retrieval step? *Because a wrong passage can still produce a right-looking answer by luck, and the test only sees the answer.*
2. What should a test case store besides the expected answer? *The expected source, such as the passage or policy version.*
3. Why add question pairs that differ only by location? *Because the pair shows whether the assistant picked the right version for each place.*
4. What must exist before source checks work? *Stable ids for passages and policy versions.*

## Checklist line

- [ ] Every test case checks the answer and the source it relies on.

## Glossary

- **Retrieval:** finding the passages that might answer a question.
- **Right for the wrong reason:** an answer that is correct by luck, from the wrong source.
- **Layer score:** a separate score for search, rules or the final answer.
- **Source id:** a stable name for a passage or policy version, used in tests and logs.

## Further reading

- Your own retrieval logs: they show which passages answers used.
- Documentation for evaluation tools, such as RAGAS and OpenAI Evals, for layer-by-layer metrics.

## Reader questions

- Which of your current tests would still pass if the source were wrong?
- Which two policies in your work differ only by location or date?
