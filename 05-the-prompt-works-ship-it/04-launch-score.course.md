# Lesson 5.4: Release gates per category (course companion)

*Module 5: Evals. Not for LinkedIn.*

## Learning objective

After this lesson, you can write a release gate per question category, tied to the risk of a wrong answer, and keep it in code so the release process enforces it.

## The story

Read the article: [04-launch-score.md](04-launch-score.md). Running example: an HR policy assistant. The overall score is 92%, but maternity leave questions score 60%. The average hid the one group where a wrong answer costs the most.

## Deep dive

An **average** tells you how the assistant does across all questions. A **release gate** tells you whether it is safe to ship. The two are different. A high average can sit on top of a failing category, because easy questions carry the score.

**Split by category first.** Group test questions by what they are about: leave, pay, office hours, and so on. Each category gets its own score. Without this split, no gate can see the failure.

**Set the gate from risk.** The threshold depends on what a wrong answer costs. A wrong office address is an inconvenience. A wrong leave entitlement can cost money and trust. Higher risk means a higher bar, and the owner of that risk should agree to the number.

**Block on the risky categories.** Decide which categories can block a release on their own. A failure there stops the launch, whatever the average says. Lower-risk categories can be reported without blocking.

**Write the gate before the test.** Set the thresholds before the first run, with the business owner. A gate written after the result tends to drift toward the score the team already has.

**Keep the gate in code.** Store thresholds in a config file that the release process reads. A failed gate fails the build. The number is then a fact, not a debate.

**Enough questions per category.** A category with a handful of questions produces a score that moves a lot from run to run. Add questions until the score is stable, before it can block a release. The exact count depends on your risk and tolerance; treat any tiny category as "not yet measured".

**Limits.** A gate is only as good as its questions. If a category has no test at all, the gate never sees it. List the categories first, then check that each one has a gate.

## Hands-on lab

1. List the question categories in a small policy assistant. Write the expected risk level (low, medium, high) for each.
2. Set a threshold for each category, with a note on why it is that number.
3. Write the thresholds in a small config file, and a check that fails when any high-risk category is below its threshold.
4. Make one change to the prompt that lowers one category. Run the check and confirm the build fails.

## Quiz

1. Why can an overall average hide a failure? *Because easy questions can carry the average, while one risky category fails.*
2. Why set the gate before the test? *To stop the gate from drifting toward the result the team already has.*
3. What should decide a category's threshold? *The cost of a wrong answer in that category.*
4. What happens if a category has no test questions? *The gate never sees it, so a failure there goes unnoticed.*

## Checklist line

- [ ] Each question category has a release gate, set from risk before testing, and a failed high-risk gate blocks the release.

## Glossary

- **Release gate:** a rule that allows a release only when the scores meet its threshold.
- **Category:** a group of test questions that share a topic or risk, such as leave or pay.
- **Blocking gate:** a gate whose failure stops the release on its own.
- **Average (overall score):** the score across all questions, which can hide weak categories.

## Further reading

- Your own risk register: the source of the gate levels.
- Documentation for evaluation tools, such as RAGAS and OpenAI Evals, for per-category reporting.

## Reader questions

- Which question category in your project would you never accept a failure in?
- Who should agree the threshold for that category?
