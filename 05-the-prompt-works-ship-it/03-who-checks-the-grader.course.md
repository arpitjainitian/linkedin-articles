# Lesson 5.3: Auditing the AI grader (course companion)

*Module 5: Evals. Not for LinkedIn.*

## Learning objective

After this lesson, you can measure how well an AI grader agrees with people, and replace a vague score with a checklist the grader can apply.

## The story

Read the article: [03-who-checks-the-grader.md](03-who-checks-the-grader.md). Running example: an HR policy assistant. The answer "You are welcome to carry forward up to 10 leaves" is polite and wrong, because the policy says 5. The AI grader still gives it 9 out of 10.

## Deep dive

Reading every answer by hand does not scale, so many teams use a model as a **grader** (also called an LLM judge). A grader is fast and cheap. It is also a model with its own tastes, and those tastes can bend the scores.

**Known biases.** Graders often favour longer answers, polite tone, and answers that look like their own writing. A grader may also accept a confident wrong fact if it cannot check the policy. None of these need to be fixed by hand. They need to be measured.

**Agreement is the test.** A grader is only useful where it agrees with people on the things that matter. Measure agreement on a set of answers that people have already graded. Two simple numbers help: the share of answers where the grader and the person give the same pass or fail, and the cases where they disagree on a fact.

**The gold set.** Keep a small set of answers with known right and wrong facts, graded by people. Run the grader on it every time you change the grader's prompt or model. If the grader fails the gold set, its scores are not trusted, however good they look.

**From a score to a checklist.** A mark out of 10 hides the reason. Yes-or-no questions show it: does the answer state the limit in the policy, does it claim anything the policy does not support, would a person act on it without checking. Each question can be checked against the gold set, which makes the grader easier to audit.

**Limits.** A grader checks what it is asked to check. It will not notice a missing rule that nobody listed. Human review stays for new kinds of question, and the gold set grows as new errors appear.

## Hands-on lab

1. Pick 20 answers from a small policy assistant. Grade them yourself, pass or fail, with a one-line reason each.
2. Write a grader prompt that uses three yes-or-no questions instead of a score out of 10.
3. Run the grader on the same 20 answers. Count the agreements and list the disagreements.
4. For each disagreement, write whether the grader was too strict, too lenient, or misled by tone or length.

## Quiz

1. Why is a grader's score not trusted by default? *Because graders can favour length, tone or their own style, so their scores must be measured against people.*
2. What is a gold set? *A small set of answers with known right and wrong facts, graded by people, used to test the grader.*
3. Why use yes-or-no questions instead of a 1 to 10 score? *Because each question can be checked, and a single score hides the reason.*
4. When should you rerun the gold set? *Whenever the grader's prompt or model changes.*

## Checklist line

- [ ] The AI grader is checked against human marks, and its checklist is tested on a gold set before its scores are trusted.

## Glossary

- **Grader (LLM judge):** a model that scores another model's answers.
- **Agreement rate:** the share of answers where the grader and a person give the same result.
- **Gold set:** answers with known, human-checked results, used to test the grader.
- **Bias (in a grader):** a steady lean, such as favouring longer answers, that moves scores away from the right result.

## Further reading

- Your own gold set: the first place to measure agreement.
- Documentation for evaluation tools, such as RAGAS and OpenAI Evals, for grader and checklist patterns.

## Reader questions

- How many answers in your project have a human-checked result today?
- Which of your grader's scores would change if the answer were twice as long?
