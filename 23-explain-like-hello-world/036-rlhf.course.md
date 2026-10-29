# Lesson 23.36: RLHF (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain RLHF with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

Ask a freshly trained AI "How do I boil an egg?" It might continue with three more questions, because it learned to continue text, not to answer.

## One step further

First, people write example answers to teach the basic "question, then answer" habit. Then they compare pairs of AI answers and rank them. A second model learns to predict which answers people prefer, and the main AI is trained to score well with it.

Newer methods skip the second model and learn from the comparisons directly, but the idea is the same: human preferences shape behaviour.

## Exercise

Explain RLHF to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for RLHF? *Thumbs up, thumbs down, thousands of times. That's how AIs learned to answer.*
2. What is it not? *RLHF doesn't teach new facts, and it isn't a guarantee of truth. It teaches what answers people like, which can include sounding confident.*
3. Name one place you've already met it. *The thumbs up and down buttons under chatbot answers. Chatbots that politely decline harmful requests.*

## Glossary

- **Human feedback:** people choosing which answer is better.
- **Reward model:** a model that learns to predict those choices.
- **Alignment:** shaping an AI to be helpful, honest and safe.

## Further reading

- The series plan: [README.md](README.md).
