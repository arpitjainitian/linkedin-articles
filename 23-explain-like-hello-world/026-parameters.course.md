# Lesson 23.26: Parameters (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain parameters with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

Picture a mixing desk in a music studio, covered in tiny knobs. Turn the knobs one way and the song sounds muddy. Turn them right and it sounds great.

## One step further

Each knob is a number, called a **parameter** or **weight**. Nobody sets them by hand. During training, the AI guesses, sees how wrong it was, and every knob is nudged slightly to be less wrong next time, over and over across a huge amount of text.

More knobs can hold more patterns, but they also need more memory and more computing power to run.

## Exercise

Explain parameters to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for parameters? *70B means 70 billion tiny knobs, each tuned during training.*
2. What is it not? *More parameters isn't automatically better. Newer small models often beat older big ones, because training data and methods matter as much as size (write-up 38).*
3. Name one place you've already met it. *Model names like "Llama 3 70B" or "8B". When an AI runs on your phone, it's usually one with a few billion knobs, not hundreds of billions.*

## Glossary

- **Parameter:** one adjustable number inside the model.
- **Weights:** all those numbers together; the model's learned knowledge.
- **Model size:** how many parameters it has, like 8B or 70B.

## Further reading

- The series plan: [README.md](README.md).
