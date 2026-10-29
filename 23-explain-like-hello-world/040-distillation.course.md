# Lesson 23.40: Distillation (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain distillation with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

A senior doctor (the big AI) and a junior doctor (the small AI) see the same patients. The junior doesn't just learn the final diagnosis. They learn how the senior weighs every option: "probably flu, maybe a cold, unlikely anything worse".

## One step further

The teacher answers a large set of questions. The student is trained to match the teacher's outputs, including how likely it thought each option was, which carries more information than a single right answer.

The student ends up much smaller and cheaper, keeping much of the teacher's skill on the tasks it was taught.

## Exercise

Explain distillation to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for distillation? *What if the big one taught the small one? That's distillation.*
2. What is it not? *The student isn't a full copy. It loses some skill, especially outside what it was taught. Also check licences: some providers forbid using their outputs to train other models.*
3. Name one place you've already met it. *The "mini", "flash" or "lite" versions of popular models are often built this way. Fast on-device assistants too (write-up 56).*

## Glossary

- **Teacher model:** the big model being learned from.
- **Student model:** the small model doing the learning.
- **Distilled model:** the small model that results.

## Further reading

- The series plan: [README.md](README.md).
