# Lesson 23.82: Checkpoint (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain checkpoint with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

A video game with save points. Lose a level and you return to the last save, not to the title screen, and you keep your progress.

## One step further

A long agent task might take an hour and many tool calls. The harness saves the state at key steps: what has been done, what the results were, and what comes next. If the network fails or a person pauses the task, the agent loads the last checkpoint and continues.

Checkpoints also allow a human to inspect the state, correct it and resume. Saving everything costs storage, so teams choose the steps that matter.

## Exercise

Explain checkpoint to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for checkpoint? *A checkpoint lets an agent resume from its last saved step.*
2. What is it not? *A checkpoint isn't a backup of the whole system. It saves the agent's progress, so a restart doesn't repeat finished steps or the actions it already took.*
3. Name one place you've already met it. *An agent that picks up a long report where it left off after a crash, and a "continue from here" button in AI tools.*

## Glossary

- **Checkpoint:** a saved snapshot of an agent's progress.
- **Resume:** continuing a task from a saved point.
- **State:** everything an agent needs to know to continue.

## Further reading

- The series plan: [README.md](README.md).
