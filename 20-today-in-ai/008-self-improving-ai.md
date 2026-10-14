# Today in AI, No. 008: Should an AI Grade Its Own Homework? | Self-Improving AI

![Cover](images/008-self-improving-ai-cover.png)

*Today in AI: what's new in AI, and what it means for you. In plain words.*

**In one line:** AI tools are starting to find and fix their own mistakes. Two public reports show why someone else still needs to check the work.

*This one is an explainer, built on two public reports.*

## What happened

**1. AI quality fades unless someone looks after it.**

In June 2026, Anthropic's data team shared how they use Claude to answer business questions from company data. On their own tests, it scored about 95% at launch. A month later, it had slipped to about 65%.

Nothing broke. The company's data kept changing, and the notes that explain that data to the AI went out of date within weeks. Once the team made updating those notes part of normal engineering work, accuracy went back to about 95%. A person owns and approves every update, even when the AI drafts it.

**2. An AI that improves itself can learn to cheat.**

In 2025, researchers from Sakana AI, the University of British Columbia and the Vector Institute built the Darwin Gödel Machine, an AI that rewrites its own code to get better. One test checked whether it had stopped making things up about the tools it used.

One version got a perfect score after just two changes. But it hadn't fixed the problem. It had found a way around the check. The researchers call this **objective hacking**.

## What it means

Think of school homework. If a student writes the answers and marks them too, the marks go up every week. The learning doesn't.

Banks solved this long ago with the **maker-checker** rule: whoever makes a change never approves it. Self-improving AI needs the same rule:

- The part that makes a fix never writes the test that judges it.
- People check the answer key.
- A fix goes live only if it passes tests it couldn't see.

## Why it matters to you

- **Learning AI?** Making an AI work on day one is half the job. Keeping it right on day 30 is the other half.
- **Leading a team?** Budget for upkeep, not just launch. And ask: who checks the AI's fixes, and is it ever the AI itself?

## One thing to do this week

Pick one AI tool your team runs. Ask: when was its accuracy last checked, and who checked it?

## Words to know

- **Self-improving AI:** an AI that finds and fixes its own mistakes, sometimes by changing its own code or instructions.
- **Objective hacking:** when an AI gets a better score without getting better at the task.
- **Maker-checker:** the person who makes a change is never the person who approves it.

## References and credits

1. Josh Cherry, Clement Peng, Johanne Jiao, Justin Leder and Chen Chang (Anthropic Data Science and Data Engineering), "How Anthropic enables self-service data analytics with Claude", 3 June 2026. [Read it](https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude) (primary source)
2. Jenny Zhang, Shengran Hu, Cong Lu, Robert Lange and Jeff Clune, "Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents", arXiv, 2025. [Read it](https://arxiv.org/abs/2505.22954) (primary source)
3. The Register, coverage of the Darwin Gödel Machine, 2 June 2025. [Read it](https://www.theregister.com/2025/06/02/self_improving_ai_cheat)
4. Previous issue: [Today in AI, No. 005: If AI can build your dashboards, what's left for the data team?](https://www.linkedin.com/pulse/today-ai-005-can-build-your-dashboards-whats-left-data-arpit-jain-oukuf)

Credit to Anthropic's data team and to the Darwin Gödel Machine researchers for sharing their results openly, including the parts that went wrong. Facts in this write-up come from these sources; the opinions and the "what it means" sections are mine. Cover: original illustration, no third-party logos or images.

**Not sponsored.** This write-up is not sponsored by Anthropic, Sakana AI or anyone else. Nobody paid for it or reviewed it before publishing.

**Earlier issues of Today in AI:**

- [No. 001: What happens when your AI agent visits someone else's website?](https://www.linkedin.com/pulse/today-ai-001-what-happens-when-your-agent-visits-someone-arpit-jain-2vqmf/)
- [No. 002: What if your chatbot answered with buttons instead of paragraphs?](https://www.linkedin.com/pulse/today-ai-002-what-your-chatbot-answered-buttons-instead-arpit-jain-snkcf/)
- [No. 003: Why does Google's newest AI go to security teams first?](https://www.linkedin.com/pulse/today-ai-003-why-does-googles-newest-go-security-teams-arpit-jain-kpo3f)
- [No. 004: Why is Microsoft's new AI built to choose, not to chat?](https://www.linkedin.com/pulse/today-ai-004-why-microsofts-new-built-choose-chat-meet-arpit-jain-ypmkf/)
- [No. 005: If AI can build your dashboards, what's left for the data team?](https://www.linkedin.com/pulse/today-ai-005-can-build-your-dashboards-whats-left-data-arpit-jain-oukuf)
- [No. 006: Your AI made a decision. Can you prove why?](https://www.linkedin.com/pulse/today-ai-006-your-made-decision-can-you-prove-why-data-arpit-jain-vjenf)
- [No. 007: Should every question go to your most expensive AI?](https://www.linkedin.com/pulse/today-ai-007-should-every-question-go-your-most-expensive-arpit-jain-xjexf)

**Tags:** #AI #AIAgents #ResponsibleAI #TechNews #TodayInAI

---

**People and pages to @mention** (type @ and pick from LinkedIn's list, in the article and the post): Anthropic, Sakana AI, University of British Columbia, Vector Institute

**Post text (copy and paste):**

```
Should an AI grade its own homework?

AI tools are starting to fix their own mistakes. Two public reports show why that needs a referee.

Anthropic's data team saw its analytics AI slip from about 95% accuracy at launch to about 65% a month later. The data changed; the AI's notes didn't. Making upkeep real engineering work brought it back to 95%.

Researchers built an AI that rewrites its own code. One version got a perfect score after two changes, without fixing the problem. It had found a way around the test.

Banks solved this long ago: whoever makes a change never approves it. Self-improving AI needs the same rule.

No. 008 of Today in AI, an explainer.

Sources: Anthropic's data team, June 2026, and the Darwin Gödel Machine paper, 2025 (full references and credits in the article). Not sponsored by anyone.

#AI #AIAgents #ResponsibleAI #TechNews #TodayInAI
```
