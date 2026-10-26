# Lesson 23.9: Training vs inference (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain training vs inference with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

A student spends years at school. That's **training**: slow, expensive, done once.

## One step further

Training turns the knobs (write-up 8) using huge amounts of text and computing power, over weeks or months. Then the knobs are frozen and the model is released.

Every question you ask is inference: the frozen model makes its guesses. It doesn't change its knobs because of your chat. A company may later use chats (if its policy allows) to train the **next** version, but that's a separate, later step.

## Exercise

Explain training vs inference to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for training vs inference? *Training is school. Chatting is the exam. The AI isn't learning mid-exam.*
2. What is it not? *Inference isn't learning. If an AI seems to remember you, that's a separate memory feature or the chat history on its desk (write-up 6), not new training.*
3. Name one place you've already met it. *Chip news: some chips are built for training, others for inference. Privacy settings that ask "may we use your chats to improve our models?" That's about future training.*

## Glossary

- **Training:** teaching the model by adjusting its knobs on lots of data.
- **Inference:** using the trained, frozen model to answer.
- **Knowledge cutoff:** the date its training data ends.

## Further reading

- The series plan: [README.md](README.md).
