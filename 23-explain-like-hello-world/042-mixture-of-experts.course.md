# Lesson 23.42: Mixture of experts (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain mixture of experts with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

Walk into a hospital with a broken arm. You don't see every doctor. A receptionist sends you to orthopaedics, and only those specialists get involved.

## One step further

For every token (write-up 10), a small router picks a handful of experts, often 2 out of 8, or a few out of hundreds. The others stay idle.

So a model can have a huge total size but use only a small part for each word. Mixtral 8x7B, for example, uses 2 of its 8 experts per token. It gets the knowledge of a big model at closer to the running cost of a small one.

## Exercise

Explain mixture of experts to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for mixture of experts? *A mixture of experts sends each word to only a few specialists.*
2. What is it not? *The experts aren't neat topics like "maths" or "law". They specialise in patterns the model found on its own. And all experts still have to be loaded in memory.*
3. Name one place you've already met it. *Several well-known open models (like Mixtral and DeepSeek) use this design, and many big commercial models are widely reported to.*

## Glossary

- **Expert:** one specialist part of the model.
- **Router:** the part that picks which experts handle each token.
- **Active parameters:** the knobs actually used for each token.

## Further reading

- The series plan: [README.md](README.md).
