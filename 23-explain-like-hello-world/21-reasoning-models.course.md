# Lesson 23.21: Reasoning models (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain reasoning models with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

Ask a friend: "A bat and a ball cost ₹110. The bat costs ₹100 more than the ball. How much is the ball?" Most blurt "₹10". Wrong. Ask them to work it out step by step, and they get ₹5.

## One step further

Normal next-token prediction (write-up 3) commits to an answer straight away. A reasoning model is trained to first produce a long chain of steps: try an approach, check it, backtrack, try again. Only then does it answer.

More thinking usually means better results on maths, coding and planning, but it uses more tokens, so it's slower and costs more per question.

## Exercise

Explain reasoning models to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for reasoning models? *Most people blurt ₹10. Thinking step by step gets ₹5. Reasoning models do the same.*
2. What is it not? *The thinking isn't a perfect window into how it decided, and more thinking isn't always better. Simple questions don't need it, and you pay for every thinking token.*
3. Name one place you've already met it. *"Thinking" or "extended thinking" toggles in chat apps, and answers that take 20 seconds instead of 2.*

## Glossary

- **Chain of thought:** the step-by-step working the model writes out.
- **Test-time compute:** spending more computing power while answering, not while training.
- **Thinking budget:** a limit on how long it can think.

## Further reading

- The series plan: [README.md](README.md).
