# Lesson 23.15: Transformer (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain transformer with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

Old AI read a sentence like someone reading through a keyhole: one word at a time, left to right, forgetting the start by the end.

## One step further

A transformer is a stack of layers. In each layer, every token (write-up 11) gathers information from the others through attention, then refines it. Dozens of layers later, the model has a rich picture of the text and predicts the next token.

Because all words are processed together, transformers train well on GPUs (write-up 51), which is why they could be scaled to today's huge models. The design was published by Google researchers in 2017 in a paper called "Attention Is All You Need".

## Exercise

Explain transformer to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for transformer? *A transformer lays the whole sentence out and reads it all at once.*
2. What is it not? *A transformer isn't a specific product or a robot. It's a design, like "suspension bridge" is a design, used by many different models.*
3. Name one place you've already met it. *Every major chatbot, translator and coding assistant. Many image, speech and video models use transformers too.*

## Glossary

- **Architecture:** the overall design of a model.
- **Layer:** one round of attention and refinement.
- **GPT:** Generative Pre-trained Transformer.

## Further reading

- The series plan: [README.md](README.md).
