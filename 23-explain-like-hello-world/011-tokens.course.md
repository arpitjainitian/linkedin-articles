# Lesson 23.11: Tokens (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain tokens with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

Give an AI the word "unbelievable". It doesn't see one word. It might see three pieces: **un**, **believ**, **able**.

## One step further

Before training, the AI's makers build a fixed "brick set": a vocabulary of tens of thousands of pieces, chosen because they appear often in text. Every sentence you type is cut into those bricks, and each brick gets a number. The AI only ever works with the numbers.

A rough rule of thumb: in English, one token is about four letters, so 100 words is roughly 130 to 150 tokens. Many other languages, and code, need more tokens for the same meaning.

## Exercise

Explain tokens to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for tokens? *An AI doesn't read words. It reads pieces, called tokens.*
2. What is it not? *A token is not a word, and not a letter. Two AIs can split the same sentence differently, so "1,000 tokens" isn't the same amount of text everywhere.*
3. Name one place you've already met it. *Every AI price list ("per million tokens"), every "message too long" error, and every time an AI miscounted the letters in a word. It sees bricks, not letters.*

## Glossary

- **Token:** one piece of text the AI reads, often part of a word.
- **Tokenizer:** the tool that cuts text into tokens.
- **Vocabulary:** the fixed set of pieces a model knows.

## Further reading

- The series plan: [README.md](README.md).
