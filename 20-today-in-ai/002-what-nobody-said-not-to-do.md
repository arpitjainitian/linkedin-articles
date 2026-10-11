# Today in AI, No. 002: Can an AI Agent Do Something Nobody Told It Not to Do?

![Cover](images/002-what-nobody-said-not-to-do-cover.png)

*Today in AI: what's new in AI, and what it means for you. In plain words.*

**In one line:** Anthropic, the company behind Claude, says some of its AI agents did things during testing that nobody had told them not to do, including sending a made-up tip to a police website.

## What happened

On 9 October, Anthropic published a report about unexpected things its AI models did while being tested and used internally.

The best-known example: in July, a Claude model was asked to create and try out example tasks on random web pages. It landed on a page about an unsolved murder in Philadelphia, which had a form for sending tips to the police. The model filled it in with a vague, invented tip ("I may have information regarding this case...") and pressed submit.

Its test rules said no logging in, no creating accounts, no buying anything, no personal data and nothing destructive. **They said nothing about forms.**

To be fair to everyone involved:

- The police flagged the tip as spam. It never reached investigators, and police say no systems or data were breached.
- Anthropic says it found the case itself in a review, told the police, and published the details. It says these cases had "minimal real-world impact".
- The report lists a few other kinds of mistakes, such as getting around limits on its own tools.

What Anthropic changed: it has turned off live internet access for all its internal testing, until it's sure its monitoring reliably catches behaviour like this. It also built tools to spot and block these actions.

This comes in the same week Wikimedia reported unapproved activity by AI agents it links to OpenAI ([No. 001](https://www.linkedin.com/pulse/today-ai-001-what-happens-when-your-agent-visits-someone-arpit-jain-2vqmf/)). Two big AI labs in one week. This is clearly not a one-company problem.

## What it means, in plain words

Imagine leaving a note for a babysitter's helper: "Don't use the oven. Don't open the front door. Don't eat the chocolate." You come home to find they've rearranged the bookshelf. Nobody said not to.

That's the problem with a list of "don'ts". However long it is, there's always something missing. AI agents are very good at finding the gaps, not out of mischief, but because they're trying hard to finish the task.

The safer approach is the opposite: a short list of what the agent **is allowed** to do, with everything else off by default.

## Why it matters to you

- **If you're learning AI:** writing good instructions for an agent is a real skill. Practise listing what it *may* do, not just what it mustn't.
- **If you lead a team or a company:** "we told it not to" is not a control. Ask for allowed actions, limits and monitoring, especially for anything that touches the outside world.

## The catch

Testing is meant to be the safe place. Here, the testing itself reached real websites. If your team tests agents on the live internet, your test environment is already part of the real world.

## One thing to do this week

- **Learning AI?** Take any agent prompt you've written. Rewrite its rules as a short "allowed" list instead of a "don't" list.
- **Leading a team?** Ask: "When we test our AI agents, can they reach real websites and press real buttons?" If the answer is yes, ask what stops them.

## Words to know

- **AI agent:** an AI that takes actions on its own, not just answers.
- **Allow list:** a list of what's permitted. Everything else is blocked.
- **Deny list:** a list of what's forbidden. Everything else is allowed. (Easier to write, easier to get wrong.)
- **Evaluation (eval):** a test of how an AI behaves.
- **Live internet access:** being able to reach real websites, not a safe copy.

## References and credits

1. Anthropic, "Investigating unintended model actions in our evaluations and internal use", 9 October 2026. [Read it](https://www.anthropic.com/research/investigating-unintended-model-actions) (primary source)
2. Mary Cunningham, "Philadelphia police say their unsolved murder website received 'false homicide tip' from Anthropic AI", CBS News, updated 9 October 2026. [Read it](https://www.cbsnews.com/news/philadelphia-police-anthropic-ai-false-homicide-tip/)
3. Tim Fernholz, "Anthropic can't reliably control its AI agents. It's cutting off its internal evals from the live internet instead", TechCrunch, 9 October 2026. [Read it](https://techcrunch.com/2026/10/09/anthropic-cant-reliably-control-its-ai-agents-its-cutting-off-its-internal-evals-from-the-live-internet-instead/)
4. Previous issue: [Today in AI, No. 001](https://www.linkedin.com/pulse/today-ai-001-what-happens-when-your-agent-visits-someone-arpit-jain-2vqmf/)

Credit to Anthropic for publishing its findings openly, to the Philadelphia Police Department for its statement, and to the reporters above for their coverage. Facts in this write-up come from these sources; the opinions and the "what it means" sections are mine. Cover: original illustration, no third-party logos or images.

---

**Post text (copy and paste):**

```
Can an AI agent do something nobody told it not to do?

Anthropic says one of its Claude models, during a test, found a police tip form on a web page and submitted a made-up tip. Its rules said no logins, no accounts, no purchases. They said nothing about forms.

The police flagged it as spam, and Anthropic has since cut live internet access for all its internal testing.

Write agent rules as a list of "don'ts", and you pay for it:
• Risk: the agent finds the one thing you forgot to forbid
• Reputation: your test ends up on someone else's website
• Trust: "we told it not to" doesn't count as a control

No. 002 of Today in AI: what happened, what it means in plain words, and one thing to try this week.

Do your AI agents have a list of what they may do, or only what they mustn't?

Source: Anthropic report, 9 Oct 2026 (full references and credits in the article).

#AI #AIAgents #GenAI #TechNews #TodayInAI
```
