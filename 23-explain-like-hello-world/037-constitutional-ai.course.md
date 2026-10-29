# Lesson 23.37: Constitutional AI (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain constitutional AI with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

Give a student a short rulebook: "be helpful, be honest, don't help anyone cause harm". Ask them to write an answer, check it against the rulebook, and rewrite it if it breaks a rule.

## One step further

RLHF (write-up 36) relies on lots of human ratings. Constitutional AI, introduced by Anthropic in 2022, uses a written set of principles, the "constitution", and has the AI itself judge which answers follow them better. Those AI judgements then train the model.

It makes the rules visible and reduces how much harmful content human raters need to see.

## Exercise

Explain constitutional AI to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for constitutional AI? *Constitutional AI teaches a model to check its own answers against written principles.*
2. What is it not? *It isn't a legal constitution, and it doesn't make a model perfectly safe. It's one training method among several.*
3. Name one place you've already met it. *Claude was trained with this approach. Published model "constitutions" and behaviour guidelines from AI companies.*

## Glossary

- **Constitution:** a written list of principles.
- **Self-critique:** the model reviewing its own answer.
- **RLAIF:** reinforcement learning from AI feedback.

## Further reading

- The series plan: [README.md](README.md).
