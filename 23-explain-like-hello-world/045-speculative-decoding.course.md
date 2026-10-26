# Lesson 23.45: Speculative decoding (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain speculative decoding with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

A fast intern drafts the next five words of a letter. The expert reads the draft and says: "first three are fine, fix the fourth." The expert checked five words in about the time it takes to write one.

## One step further

Writing normally means the big model produces one token at a time (write-up 11), which is slow. Checking several tokens at once is much faster for it than writing them one by one.

So the small model drafts a few tokens, the big model verifies them together, keeps the ones it agrees with, and corrects the first one it doesn't. The final text is what the big model would have written anyway, just faster.

## Exercise

Explain speculative decoding to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for speculative decoding? *That's speculative decoding: guess ahead, check in one go.*
2. What is it not? *It doesn't lower quality or change the answer; the big model still has the final say. It only helps when the small model's guesses are often right.*
3. Name one place you've already met it. *AI apps that suddenly got noticeably faster without changing models. Many serving systems use this or similar tricks.*

## Glossary

- **Draft model:** the small, fast model that guesses ahead.
- **Target model:** the big model that checks and decides.
- **Decoding:** producing the output, token by token.

## Further reading

- The series plan: [README.md](README.md).
