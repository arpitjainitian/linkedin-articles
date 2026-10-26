# Lesson 23.31: LoRA (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain LoRA with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

Instead of retraining the chef (write-up 30), you clip a recipe card to their apron: "for our biryani, more saffron, less salt". The chef stays the same; the card changes a few dishes. Swap cards for different restaurants.

## One step further

Full fine-tuning adjusts all of a model's billions of knobs. LoRA freezes them and trains a tiny set of extra knobs alongside, often well under 1% of the size.

It's much cheaper, needs less memory, and you can keep many small add-ons for different tasks or customers and switch between them.

## Exercise

Explain LoRA to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for LoRA? *LoRA is that recipe card: a small, swappable add-on to an AI.*
2. What is it not? *LoRA isn't a different model. It only works on top of the model it was trained for. Swap the base model and the add-on usually won't fit.*
3. Name one place you've already met it. *Image apps that learn your face or art style from a few photos. Open-model communities sharing small style add-ons.*

## Glossary

- **Adapter:** a small add-on trained for a task.
- **LoRA:** a popular, efficient kind of adapter.
- **Frozen weights:** the original knobs, left unchanged.

## Further reading

- The series plan: [README.md](README.md).
