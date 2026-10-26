# Lesson 23.41: Quantization (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain quantization with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

Take a photo and save it as a smaller file. It's a bit less sharp, but you can still see everything that matters, and it takes a fraction of the space.

## One step further

Normally each knob is stored as a very precise number, like 0.73914. Quantization rounds it, say to 0.74, using fewer bits of memory. Going from 16 bits to 4 bits per knob makes the model roughly four times smaller and often faster.

Round too hard and quality drops, like an over-compressed photo turning blocky. Good methods keep most of the quality.

## Exercise

Explain quantization to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for quantization? *Quantization is saving the same photo as a smaller file.*
2. What is it not? *Quantization isn't free. Quality can slip, especially on maths, rare languages or long reasoning. Test the smaller version on your real tasks.*
3. Name one place you've already met it. *Running an AI on a laptop with apps like Ollama or LM Studio. Model downloads labelled "Q4" or "4-bit".*

## Glossary

- **Quantization:** storing a model's numbers with less precision.
- **Bit:** the basic unit of computer memory; fewer bits per number, smaller model.
- **Precision:** how many digits each number keeps.

## Further reading

- The series plan: [README.md](README.md).
