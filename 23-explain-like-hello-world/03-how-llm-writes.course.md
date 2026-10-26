# Lesson 23.3: How an LLM writes (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain how an LLM writes with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

Finish this: "The cat sat on the ___".

## One step further

The AI doesn't pick one answer. For every next piece it gives each option a score: "mat" very likely, "sofa" likely, "moon" unlikely. Then one is picked, and the loop continues.

It learned those scores by reading a huge amount of text and practising this exact game: hide the next word, guess it, get corrected, billions of times.

## Exercise

Explain how an LLM writes to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for how an LLM writes? *An AI writes by guessing the next word, again and again.*
2. What is it not? *It's not looking answers up in a database, and it doesn't plan the whole paragraph first. That's why it can sound fluent and still be wrong (more in write-up 30).*
3. Name one place you've already met it. *Your phone keyboard suggesting the next word. Same idea, far smaller. And the way ChatGPT or Claude types its answer bit by bit on screen: you're watching the guesses happen.*

## Glossary

- **LLM:** a model trained to predict the next token in text.
- **Next-token prediction:** guessing the most likely next piece, again and again.
- **Probability:** the score the AI gives each possible next piece.

## Further reading

- The series plan: [README.md](README.md).
