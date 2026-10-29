# Lesson 23.41: Overfitting (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain overfitting with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

A student memorises the exact answers to last year's exam paper. They score 100% on that paper. Then the real exam has different questions, and they fail.

## One step further

A model can get so good at its training data that it learns the noise too: accidental details that won't repeat. It looks brilliant in testing on familiar data and disappoints on new cases.

The fix is to always test on data it has never seen, use more varied examples, and stop training before it starts memorising.

## Exercise

Explain overfitting to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for overfitting? *That's overfitting: memorising examples instead of learning the pattern.*
2. What is it not? *Overfitting isn't the model being too smart. It's the model learning the wrong lesson: the examples, not the pattern.*
3. Name one place you've already met it. *AI projects that worked perfectly in the demo and stumbled on real customers. Benchmark scores that don't match real-world performance (write-up 109).*

## Glossary

- **Overfitting:** memorising examples instead of learning patterns.
- **Test set:** data held back to check the model fairly.
- **Generalisation:** doing well on new, unseen cases.

## Further reading

- The series plan: [README.md](README.md).
