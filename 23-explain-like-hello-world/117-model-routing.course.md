# Lesson 23.117: Model routing (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain model routing with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

A hospital doesn't send every patient to the top surgeon. A nurse handles a sore throat; the specialist handles the complicated case.

## One step further

A router looks at each request (by rules, a small classifier, or a quick AI check) and picks a model. Easy questions go to a small model (write-up 54); hard ones go to a big or reasoning model (write-up 79). Some routers try the small model first and escalate if its answer isn't good enough.

Done well, most requests go to cheap models and quality holds. Done badly, hard questions get weak answers. Evals (write-up 99) keep it honest.

## Exercise

Explain model routing to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for model routing? *Model routing sends each AI question to the right-sized model.*
2. What is it not? *Routing isn't just "always use the cheapest". It's matching each question to a good-enough model, and checking that quality didn't drop. (My [Today in AI No. 007](https://www.linkedin.com/pulse/today-ai-007-should-every-question-go-your-most-expensive-arpit-jain-xjexf) covers AI routers.)*
3. Name one place you've already met it. *AI apps with an "auto" model setting. Chatbots that quickly answer simple questions and take longer on hard ones.*

## Glossary

- **Router:** the component that picks a model per request.
- **Escalation:** passing a request up to a stronger model.
- **Cost per answer:** what each answer costs, on average.

## Further reading

- The series plan: [README.md](README.md).
