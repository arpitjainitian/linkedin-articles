# Lesson 23.94: Guardrails (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain guardrails with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

A mountain road has guardrails at the edges. You still drive; the rails just stop you going over the cliff.

## One step further

Input guardrails check what comes in: off-topic questions, personal data, attempts to trick the AI (write-ups 96 and 97). Output guardrails check what goes out: medical or legal advice, toxic language, leaked data, wrong formats.

They can be simple rules, small classifier models, or another AI checking the answer. The art is balance: too loose is risky, too strict and the AI refuses useful questions.

## Exercise

Explain guardrails to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for guardrails? *AI guardrails are checks on what goes in and what comes out.*
2. What is it not? *A guardrail isn't one line in the prompt saying "don't do bad things". Real guardrails are separate checks, in layers. (Series 4 covers them in depth.)*
3. Name one place you've already met it. *Chatbots that say "I can't help with that". Company assistants that won't discuss topics outside their job.*

## Glossary

- **Input guardrail:** a check before the question reaches the AI.
- **Output guardrail:** a check before the answer reaches the person.
- **False refusal:** blocking a question that was actually fine.

## Further reading

- The series plan: [README.md](README.md).
