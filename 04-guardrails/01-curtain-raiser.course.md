# Lesson 4.1: Prompts vs guardrails (course companion)

*Module 4: Guardrails. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain why a prompt instruction is a request rather than a rule, and name the layers a real guardrail needs.

## The story

Read the article: [01-curtain-raiser.md](01-curtain-raiser.md). Running example: an online pharmacy's medicine-question assistant. The prompt says "never give medical advice, never suggest doses", and a customer's "pretend you're my doctor" gets a dose suggested anyway.

## Deep dive

A system prompt is text the model reads before the conversation. The model tries to follow it, and usually does. That is the problem: "usually" is not a guarantee, and the failure is silent. The model does not raise an error when it breaks an instruction. It just answers.

Four things make a prompt weaker than a rule.

**First, the model weighs instructions against each other.** A prompt says "be helpful" and "never advise on doses". When a customer's request pulls hard toward helpfulness, the balance can tip. Nothing in the prompt says which instruction wins in every case.

**Second, wording changes behaviour.** Role play ("pretend you're my doctor"), hypotheticals ("for a story I'm writing") and claims of authority ("I'm the pharmacist") are common ways to move a model away from its instructions. Researchers have documented many of these patterns, and some work better when combined. The OWASP list in the further reading names prompt injection and jailbreaks as leading risks.

**Third, risk can be subtle.** A safety rule written as "don't suggest doses" catches "take two tablets" but not "your usual amount should be fine". The unsafe part is the implication, and a keyword rule cannot see implications.

**Fourth, the opposite failure is real.** A fence set to block every medical topic also blocks "is paracetamol in stock?". Safety is measured in both directions, and a guardrail that over-refuses fails its users just as surely.

So what is a guardrail? It is a check that runs outside the model's free choice. It can be code that screens the input, a rule that checks the output, a second model acting as a judge, or a permission that the system enforces no matter what the text says. The model still does the writing. The fence decides what leaves the building.

The layered picture in the article is the practical version. The question is screened before the model (write-up 2). The answer is checked before the customer (write-up 3). Tricks are tested before launch (write-up 4). Staff get a verified exception path (write-up 5). Strictness is set per topic and measured in both directions (write-up 6). The finale (write-up 7) turns the layers into a checklist.

One design habit ties these together: put the rules where they can be enforced and tested. A sentence in a prompt can be tested only by asking the model. A check in code can be tested with a list of inputs that must be blocked and a list that must pass.

## Hands-on lab

1. Write a prompt for a small pharmacy assistant with three rules: no doses, no diagnoses, and always point to a pharmacist for medical questions.
2. Create a test list of 10 messages: 5 that must be refused (including role play and hypotheticals) and 5 that must be answered (stock, opening hours, storage advice).
3. Run each message through the assistant and record the result in a table: message, expected, actual, pass or fail.
4. Count the failures. Write one sentence per failure saying whether the fix belongs in the prompt, a check in code, or a permission.

## Quiz

1. Why is a prompt instruction described as a request rather than a rule? *Because the model tries to follow it, usually succeeds, and cannot guarantee it, so the failure is silent.*
2. Name two wording patterns that can move a model away from its instructions. *Role play ("pretend") and hypotheticals ("for a story"). Claims of authority also count.*
3. Why is a keyword rule weak against unsafe advice? *Because the risk is often in the implication, such as "your usual amount should be fine", and a keyword rule cannot see implications.*
4. What is the cost of a guardrail that is too strict? *It blocks safe requests, so customers leave and the team learns to ignore the bot.*

## Checklist line

- [ ] The most important rules are enforced by a check outside the model, not only by the prompt.

## Glossary

- **Guardrail:** a check outside the model's free choice that limits what goes in or comes out.
- **Jailbreak:** a prompt that tries to make a model ignore its instructions.
- **Prompt injection:** text, often hidden in a document or note, that tries to change the model's instructions.
- **Layered defence:** several checks at different points, so one miss does not reach the customer.

## Further reading

- OWASP, [Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/). Official list of the main LLM risks, including prompt injection.
- NIST, [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework). Official framework for managing AI risk, including testing and oversight.
- Perez and Ribeiro, [Ignore This Title and HackAPrompt](https://arxiv.org/abs/2211.09527) (research paper on prompt injection attacks). [CHECK] confirm the title before citing.
- Wei et al., [Jailbroken: How Does LLM Safety Training Fail?](https://arxiv.org/abs/2307.02483) (research paper on how safety training can be bypassed). [CHECK] confirm the title before citing.

## Reader questions

(to be filled from LinkedIn comments)
