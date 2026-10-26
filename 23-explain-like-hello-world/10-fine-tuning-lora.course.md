# Lesson 23.10: Pretraining, fine-tuning and LoRA (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain pretraining, fine-tuning and LoRA with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

Think of a chef.

## One step further

Pretraining builds the model from scratch on huge amounts of text. Very few companies do it.

Fine-tuning continues training on a smaller, focused set of examples, adjusting the model's knobs (write-up 8) towards your style or task.

LoRA freezes the original knobs and trains a small add-on of extra knobs instead. It's much cheaper, and you can swap add-ons for different tasks.

## Exercise

Explain pretraining, fine-tuning and LoRA to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for pretraining, fine-tuning and LoRA? *Pretraining is chef school. Fine-tuning is a short course. LoRA is a recipe card.*
2. What is it not? *Fine-tuning is mainly for style, format and behaviour, not for adding fresh facts. For facts that change, looking them up at question time usually works better (#JustAddRAG).*
3. Name one place you've already met it. *Company chatbots that answer in a fixed brand tone. Image apps that learn your face from a handful of photos often use a LoRA-style add-on.*

## Glossary

- **Pretraining:** the first, huge training run that builds the model.
- **Fine-tuning:** extra training on focused examples.
- **LoRA:** a small trainable add-on; the main model stays frozen.

## Further reading

- The series plan: [README.md](README.md).
