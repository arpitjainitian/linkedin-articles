# Lesson 23.83: Hallucination (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain hallucination with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

Ask an AI for a book by a real author on a niche topic. It might name a plausible-sounding title that doesn't exist, with confidence.

## One step further

The AI has no built-in "I don't know" signal. If its training text rarely covered something, it still produces the most likely-sounding words, and fluent text sounds sure.

Giving it the right source to read, asking it to cite, and allowing "I'm not sure" all help. (How this is handled in real systems is covered in #JustAddRAG 5.)

## Exercise

Explain hallucination to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for hallucination? *An AI guesses likely words. Likely isn't always true. That's a hallucination.*
2. What is it not? *It isn't lying (there's no intent) and it isn't a rare bug. It comes from how next-word guessing works, so it can be reduced, not fully removed.*
3. Name one place you've already met it. *Made-up citations, invented quotes, wrong dates said confidently, and fake legal cases that have landed lawyers in trouble.*

## Glossary

- **Hallucination:** fluent output that isn't true or isn't supported.
- **Grounding:** making answers rely on a given source.
- **Citation:** pointing to where a claim came from.

## Further reading

- The series plan: [README.md](README.md).
