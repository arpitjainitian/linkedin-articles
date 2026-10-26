# Today in AI, No. 010: Your AI Agent Is Waiting. Are You Still Paying? | Agent Sandboxes

![Cover](images/010-agent-sandboxes-cover.png)

*Today in AI: what's new in AI, and what it means for you. In plain words.*

**In one line:** Google wants every AI agent to get its own small, locked computer that pauses while the agent waits.

## What happened

On 22 October 2026, Google Cloud announced **Agent Compute Engine**. [1]

A coding agent writes code, runs tests, then waits for the AI's next decision. Google gives it a tiny virtual computer, a **microVM**, that pauses while it waits. [1]

Pausing is like hibernating a laptop: memory, open programs and files are saved, and the server's processor and memory go to other agents' computers until it wakes up exactly where it left off. Other agents get the server's capacity, never its data: that stays private in the snapshot. It saves money (no machine kept running while the AI thinks), time (no rebuild before every step) and space (more agents fit on each server).

## How it's done today

- **On a laptop.** Simple, but next to your real files and passwords.
- **In a throwaway container.** Cheap, but rebuilt every step, with thinner walls.
- **In a machine left running.** Nothing rebuilt, but you pay while it waits.
- **In tiny virtual computers.** AWS's Firecracker starts one in under 125 ms [2]. E2B already pauses and resumes agent sandboxes [3].

## Today vs Google's approach

- **While waiting:** today, rebuilt or left running. Google: paused, resumed from a snapshot.
- **Walls:** today, often a shared core system. Google: each agent gets its own, hardware-isolated. [1]
- **Memory:** today, a full copy per agent. Google: shared, copying only what changes. [1]
- **Passwords:** today, often inside, where a tricked agent can read them. Google: kept outside. [1]
- **Who builds it:** today, mostly you. Google: managed, with an ID per agent. [1]

So the idea isn't new. The packaging and scale are.

## Who benefits

- **Teams building coding and data agents:** long tasks resume in place instead of starting over.
- **Security teams:** passwords out of reach, one ID per agent, every outbound call checked.
- **Teams running thousands of agents:** fewer idle machines.
- **Not everyone:** an agent that only calls a few APIs doesn't need its own computer.

## The catch

Not available yet: preview "in the coming months" [1]. Still unclear: how fast a pause and resume is, what it costs, and whether open connections survive a pause. The benefits are Google's claims, not yet tested by customers.

## One thing to do this week

- **Learners:** run an agent that writes code, and note what happens to its files after each step.
- **Leaders:** ask your team where your agents run code today, and where the passwords live.

## Words to know

- **Sandbox:** a walled-off space where an agent runs things safely.
- **Snapshot:** the saved copy made when it pauses.

## References and credits

1. Nirav Mehta, Michael Bachman and Kevin Hutchins, Google Cloud, "Introducing Agent Compute Engine and expanded agent governance", Google Cloud Blog, 22 October 2026. [Read it](https://cloud.google.com/blog/topics/ai-infrastructure/introducing-agent-compute-engine-and-expanded-agent-governance) (primary source)
2. Firecracker project, "Secure and fast microVMs for serverless computing" (boots in under 125 ms; powers AWS Lambda). [Read it](https://firecracker-microvm.github.io/) (primary source)
3. E2B, "Sandbox persistence" documentation (pause and resume with memory and files kept). [Read it](https://e2b.dev/docs/sandbox/persistence) (primary source)

Credit to the Google Cloud team for a clear write-up of the design, and to the Firecracker and E2B teams for their public documentation. This is a vendor announcement: the claims come from Google and haven't been independently tested. Facts come from these sources; the opinions and "what it means" sections are mine. Cover: original illustration, no third-party logos or images.

**Not sponsored.** This write-up is not sponsored by anyone. Nobody paid for it or reviewed it before publishing.

**Earlier issues of Today in AI:**

- [No. 001: What happens when your AI agent visits someone else's website?](https://www.linkedin.com/pulse/today-ai-001-what-happens-when-your-agent-visits-someone-arpit-jain-2vqmf/)
- [No. 002: What if your chatbot answered with buttons instead of paragraphs?](https://www.linkedin.com/pulse/today-ai-002-what-your-chatbot-answered-buttons-instead-arpit-jain-snkcf/)
- [No. 003: Why does Google's newest AI go to security teams first?](https://www.linkedin.com/pulse/today-ai-003-why-does-googles-newest-go-security-teams-arpit-jain-kpo3f)
- [No. 004: Why is Microsoft's new AI built to choose, not to chat?](https://www.linkedin.com/pulse/today-ai-004-why-microsofts-new-built-choose-chat-meet-arpit-jain-ypmkf/)
- [No. 005: If AI can build your dashboards, what's left for the data team?](https://www.linkedin.com/pulse/today-ai-005-can-build-your-dashboards-whats-left-data-arpit-jain-oukuf)
- [No. 006: Your AI made a decision. Can you prove why?](https://www.linkedin.com/pulse/today-ai-006-your-made-decision-can-you-prove-why-data-arpit-jain-vjenf)
- [No. 007: Should every question go to your most expensive AI?](https://www.linkedin.com/pulse/today-ai-007-should-every-question-go-your-most-expensive-arpit-jain-xjexf)
- [No. 008: Does using AI make you give up faster?](https://www.linkedin.com/pulse/today-ai-008-does-using-make-you-give-up-faster-learning-arpit-jain-ppghf/)
- [No. 009: Same AI, many clouds. Where does your data actually go?](https://www.linkedin.com/pulse/today-ai-009-same-many-clouds-where-does-your-data-actually-jain-zgc1f)

**Tags:** #AI #AIAgents #CloudComputing #AISecurity #TodayInAI

---

**People and pages to @mention** (type @ and pick from LinkedIn's list, in the article and the post): Google Cloud

**Post text (copy and paste):**

```
Your AI agent is waiting. Are you still paying?

Today: on a laptop, in a container rebuilt every step, or a machine left running while the agent waits.

Google's new Agent Compute Engine gives each agent its own small, locked computer that pauses while it waits, with passwords kept outside.

Like pausing a game instead of replaying the level.

Not available yet: preview "in the coming months".

No. 010 of Today in AI. Sources in the article. Not sponsored.

#AI #AIAgents #CloudComputing #AISecurity #TodayInAI
```
