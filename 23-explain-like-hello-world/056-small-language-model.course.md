# Lesson 23.56: Small language model (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain small language model with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

A library has every book. A pocket dictionary is small, but for most quick look-ups, it's all you need, and it fits in your pocket.

## One step further

Small models are made capable with high-quality training data and distillation from bigger models (write-up 40), then shrunk further with quantization (write-up 47).

They're cheaper, faster and can run on a laptop or phone. The trade-off: less knowledge and weaker reasoning on hard problems. Many systems route easy questions to a small model and hard ones to a big model (write-up 125).

## Exercise

Explain small language model to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for small language model? *A small language model is the pocket dictionary.*
2. What is it not? *Small doesn't mean bad. For narrow, well-defined tasks, a small model can match a big one at a fraction of the cost.*
3. Name one place you've already met it. *Phone keyboards, offline assistants, and the "mini" or "small" versions of popular models.*

## Glossary

- **SLM:** a language model small enough to run cheaply or locally.
- **Model size:** number of parameters, like 3B or 8B.
- **Routing:** sending each request to the right-sized model.

## Further reading

- The series plan: [README.md](README.md).
