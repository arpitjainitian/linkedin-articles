# Lesson 23.100: LLM-as-a-judge (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain lLM-as-a-judge with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

A teacher has 5,000 essays to mark. Instead of marking every one, they write a clear marking guide and ask a teaching assistant to apply it, then spot-check the assistant.

## One step further

Many answers can't be checked by exact match: summaries, explanations, tone. So a judge model gets the question, the answer, sometimes a reference answer, and a rubric ("is it accurate, complete, polite?") and gives a score.

Judges have biases: they may prefer longer answers, the first answer shown, or answers in their own style. So teams check the judge against human marks and swap answer order in comparisons.

## Exercise

Explain lLM-as-a-judge to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for lLM-as-a-judge? *LLM-as-a-judge: one AI marking another, with a guide.*
2. What is it not? *A judge AI isn't ground truth. It's a fast, imperfect marker that needs checking against human judgement regularly.*
3. Name one place you've already met it. *Behind most AI quality dashboards and many public leaderboards.*

## Glossary

- **Rubric:** the marking guide the judge follows.
- **Calibration:** checking the judge agrees with people.
- **Position bias:** favouring the first or second answer shown.

## Further reading

- The series plan: [README.md](README.md).
