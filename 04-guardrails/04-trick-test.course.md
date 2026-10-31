# Lesson 4.4: Jailbreaks and red teaming (course companion)

*Module 4: Guardrails. Not for LinkedIn.*

## Learning objective

After this lesson, you can plan a red-teaming pass that tests every input the assistant reads, and keep the attack list as a regression test.

## The story

Read the article: [04-trick-test.md](04-trick-test.md). Running example: an online electronics store's refund assistant. "I'm the store manager", then "for a story", then "ignore the rules above". Each push is small. Together they can move the assistant off its instructions, and a note in an online order can do the same.

## Deep dive

A **jailbreak** is a message built to make a model ignore its instructions. **Red teaming** is the planned attempt to break your own system before someone else does. Together they answer a question that prompts alone cannot: does the fence hold when someone pushes?

**Common attack families.** Teams track attacks by family, because a fix usually covers a family rather than one sentence:

- **Role play:** asking the model to act as a character or a professional who is not bound by the rules.
- **Hypotheticals and fiction:** "for a story", "in theory", "imagine a world where".
- **False authority:** claiming to be staff, a manager or the developer.
- **Splitting:** asking for a risky result in small steps that each look harmless.
- **Encoding and language tricks:** the same request in another language, in code, or with unusual spelling.

Research on jailbreaks has shown that combining simple techniques can succeed where each one alone fails. That is why a test list should include combinations, not only single tricks. The Wei et al. paper in the further reading describes why safety training can leave gaps.

**Indirect attacks.** The most dangerous doors are the ones the chat box does not show. An assistant that reads order notes, uploaded documents or tool results will treat their text as possible instructions. A note saying "skip the policy check" is an instruction smuggled in as data. The same problem appears in retrieval systems, covered in #JustAddRAG 8. The rule for the design is simple: text from outside is data to read, never a command to obey.

**Building the attack list.** Each row has four columns: the attack, the surface it arrives through (chat, document, note, tool), the expected safe behaviour, and the result. Include both safety and usefulness: a row where the assistant refuses a safe stock question is a failure too. Teams often add a column for the attack family, so the report can show which families still pass.

**Running it.** Run the list before launch, and again after every change to the prompt, the model, the checks or the tools. A change that fixes one family can open another. Keep the list in version control, and treat it like a test suite. The evals topic in Series 5 covers how to score results at scale.

**Who should attack?** People who did not build the assistant. Builders test the paths they expect. An outsider, or a colleague from another team, tries the paths nobody planned. One hour with fresh eyes often finds more than a week of self-testing.

**Limits.** No list is complete, and attackers adapt. Red teaming tells you where the holes are today. It does not prove there are none. Pair it with the layers around the assistant: the input screen (write-up 2), the output check (write-up 3) and the logs that show attempts in production.

## Hands-on lab

1. Build an attack list of 12 rows across at least four families. Include two indirect attacks, one through a note in an order and one through a document.
2. Add an expected-behaviour column and a surface column.
3. Run the list against a simple assistant. Record the result and whether it stayed safe and useful.
4. Make one change to the prompt. Run the list again and note any new failures. Write one sentence on what the change taught you.

## Quiz

1. What is the difference between a jailbreak and red teaming? *A jailbreak is a message that tries to break the rules. Red teaming is a planned, repeated attempt to find those breaks before customers do.*
2. Why is an order note an attack surface even though it is not the chat? *Because the assistant reads it, and text it reads can contain instructions it might follow.*
3. Why should the attack list include a safe question? *Because a refusal of a safe question is a failure too, and checking only for bad answers hides false refusals.*
4. Why run the list again after a small change? *Because a fix for one attack family can open a gap in another.*

## Checklist line

- [ ] Red teaming covers every input the assistant reads, and the attack list runs again after each change.

## Glossary

- **Jailbreak:** a message built to make a model ignore its instructions.
- **Red teaming:** a planned attack on your own system, before launch and after changes.
- **Attack family:** a group of similar attacks, such as role play or hypotheticals.
- **Indirect attack:** an attack that arrives through a document, note or tool result rather than the chat.

## Further reading

- OWASP, [Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/). Lists prompt injection and related risks.
- Wei et al., [Jailbroken: How Does LLM Safety Training Fail?](https://arxiv.org/abs/2307.02483). Explains why combined attacks can work. [CHECK] confirm the title before citing.
- Perez and Ribeiro, [Ignore This Title and HackAPrompt](https://arxiv.org/abs/2211.09527). Research on prompt injection. [CHECK] confirm the title before citing.

## Reader questions

(to be filled from LinkedIn comments)
