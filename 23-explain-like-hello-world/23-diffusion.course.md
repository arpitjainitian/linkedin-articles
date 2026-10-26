# Lesson 23.23: Diffusion (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain diffusion with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

Take a clear photo of a cat. Add a little static. Then more. Then more, until it's pure TV snow.

## One step further

During training, the AI sees millions of images being turned into noise and learns to predict the noise so it can remove it.

To create something new, it starts from fresh random noise and repeats the cleaning dozens of times. Your text prompt, "a cat in a spacesuit", steers each step, so the picture that emerges matches the words.

## Exercise

Explain diffusion to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for diffusion? *Now run it backwards. That's how AI draws: diffusion.*
2. What is it not? *The AI isn't searching for an existing picture and copying it. But it learned from existing images, which is why copyright and artist consent are real debates.*
3. Name one place you've already met it. *AI image generators and the newer AI video tools. "Remove background" and "fill in this area" photo features often use the same idea.*

## Glossary

- **Noise:** random static, like a detuned TV.
- **Denoising:** removing noise a little at a time.
- **Prompt guidance:** the text steering each cleaning step.

## Further reading

- The series plan: [README.md](README.md).
