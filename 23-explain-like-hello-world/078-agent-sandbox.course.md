# Lesson 23.78: Agent sandbox (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain agent sandbox with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

A child learning chemistry gets a toy lab kit in a tray, not the keys to the school's chemical store. If something spills, it stays in the tray.

## One step further

When an agent writes code, installs packages or browses websites (write-up 76), anything could go wrong: a bad command, a malicious web page, a runaway loop. In a sandbox, the damage stays inside: separate files, limited network access, no real passwords.

Newer designs give each agent its own small virtual computer that can pause while the agent waits (my [Today in AI No. 010](https://www.linkedin.com/pulse/today-ai-010-your-agent-waiting-you-still-paying-sandboxes-arpit-jain-07qvf) covers Google's approach).

## Exercise

Explain agent sandbox to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for agent sandbox? *An agent sandbox is that tray, for AI agents running code.*
2. What is it not? *A sandbox isn't permission to give the agent everything inside it. If you put real passwords or production data in the sandbox, they're at risk too. (Series 16 covers what agents should be allowed to do.)*
3. Name one place you've already met it. *Coding assistants that run code in a separate environment. "Code interpreter" features that run your data analysis safely.*

## Glossary

- **Sandbox:** an isolated space for running untrusted actions.
- **Isolation:** keeping the sandbox separate from real systems.
- **Least privilege:** giving only the access needed.

## Further reading

- The series plan: [README.md](README.md).
