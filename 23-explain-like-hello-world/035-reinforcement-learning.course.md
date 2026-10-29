# Lesson 23.35: Reinforcement learning (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain reinforcement learning with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

Teaching a dog a trick: no instruction manual, just a treat when it does the right thing. Over many tries, it works out what earns the treat.

## One step further

The AI tries an action, gets a score (the reward), and adjusts to score higher next time. Repeat millions of times. That's how AI learned to play Go at champion level.

For language models, RL rewards good answers. With human ratings, it's RLHF (write-up 36). With answers that can be checked, like maths or code that passes tests, it helps train reasoning models (write-up 79).

## Exercise

Explain reinforcement learning to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for reinforcement learning? *Reinforcement learning is AI learning by trial, error and reward.*
2. What is it not? *It isn't magic self-improvement. If the reward is badly designed, the AI learns the loophole, not the goal.*
3. Name one place you've already met it. *Game-playing AIs, robots trained in simulation, and the reasoning models in today's chatbots.*

## Glossary

- **Reward:** the score that says how good an action was.
- **Agent:** the learner taking actions.
- **Reward hacking:** finding a loophole that scores well without doing the job.

## Further reading

- The series plan: [README.md](README.md).
