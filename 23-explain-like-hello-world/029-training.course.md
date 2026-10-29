# Lesson 23.29: Training (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain training with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

A child learning to spell: they guess, a teacher marks it, they adjust, and try again. Thousands of times, they get better.

## One step further

For an LLM, the "test" is hiding the next word in real text and asking the AI to guess it (write-up 12). After every guess, each of its billions of knobs is nudged slightly. This needs huge amounts of text and computing power, running for weeks or months on thousands of GPUs (write-up 51).

At the end, the knobs are frozen. That frozen model is what you use.

## Exercise

Explain training to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for training? *Training is an AI doing that billions of times.*
2. What is it not? *Training isn't happening while you chat. That's inference (write-up 31). Your chats only matter if they're later used to train the next version.*
3. Name one place you've already met it. *Announcements of how long and how expensive a model was to train. Privacy settings asking whether your data may be used to train future models.*

## Glossary

- **Training:** teaching a model by adjusting its knobs on examples.
- **Loss:** how wrong the model's guesses are.
- **Training run:** one full training process.

## Further reading

- The series plan: [README.md](README.md).
