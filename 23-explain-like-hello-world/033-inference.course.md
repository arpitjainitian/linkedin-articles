# Lesson 23.33: Inference (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain inference with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

A student who has finished school sits an exam and answers one question. No more learning, just using what they know.

## One step further

The model reads your prompt as tokens (write-up 11), and then writes its answer one token at a time (write-up 12), using its frozen knobs. It doesn't learn from your chat.

Training happens once; inference happens billions of times a day, for every user. That's why cheaper, faster inference (quantization, caching, small models) gets so much attention.

## Exercise

Explain inference to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for inference? *That's inference: a frozen model answering. It isn't learning mid-exam.*
2. What is it not? *Inference isn't learning. If an AI seems to remember you, that's chat history on its desk (write-up 16) or a memory feature (write-up 81), not new training.*
3. Name one place you've already met it. *Every chatbot answer. "Price per million tokens" is mostly the price of inference.*

## Glossary

- **Inference:** using a trained model to produce an answer.
- **Frozen model:** a model whose knobs no longer change.
- **Knowledge cutoff:** the date its training data ends.

## Further reading

- The series plan: [README.md](README.md).
