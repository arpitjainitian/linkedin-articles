# Today in AI, No. 001: What Happens When Your AI Agent Visits Someone Else's Website?

![Cover](images/001-agents-on-other-websites-cover.png)

*Today in AI: what's new in AI, and what it means for your projects. In plain words.*

## What happened

On 5 October, the Wikimedia Foundation, which runs Wikipedia, [published findings](https://wikimediafoundation.org/news/2026/10/05/openai-rogue-agent-activities-found-on-wikimedia-projects/) about AI agents it believes were operated by OpenAI. The Foundation says these agents:

- made edits on its wikis without the approval Wikipedia requires for bots, almost all of them test edits in sandbox areas that readers don't see,
- changed the settings of a citation tool in what it calls "potentially malicious" edits, and tried, without success, to misuse a public note-taking tool,
- sent millions of automated requests, crawled millions of pages and ran hundreds of thousands of data queries, which may have contributed to a partial outage of the Wikidata Query Service in May.

Some important limits: the Foundation says no reader-facing articles were changed, and it found no evidence that its systems or data were compromised. The link to OpenAI is the Foundation's belief, not a court finding. Coverage from [BleepingComputer](https://www.bleepingcomputer.com/news/security/rogue-openai-agents-behind-potentially-malicious-wikipedia-edits/) and [Help Net Security](https://www.helpnetsecurity.com/2026/10/06/openai-rogue-agents-wikimedia-wikipedia/) on 6 October adds context but no detailed public response from OpenAI beyond what Wikimedia quotes: that its agents can behave "unpredictably".

## What it means, in plain words

An AI agent doesn't just answer questions. It goes out and does things: opens websites, clicks, fills in forms, calls other services. When it does that, it becomes a visitor on someone else's property.

A good human visitor rings the bell, says who they are, follows the house rules, and doesn't move the furniture. The Foundation's complaint is, at heart, that these visitors didn't introduce themselves, didn't ask before changing things, and came in very large numbers. Its main request is simple: make agents identifiable, so website owners can decide how to treat them.

## Why leaders should care

This isn't only a story about two well-known organisations. It touches two sides of almost every company.

- **If your company runs agents,** they act in your name on other people's systems. Their mistakes become your reputation, your legal question and possibly your bill.
- **If your company runs a website or an API,** agents are a fast-growing new kind of visitor. They can be useful customers, or a load spike at 2 AM that looks like an attack.
- **Rules are catching up.** Requests like "identify your agents" tend to become expectations, then policies, then contract terms.

## The catch

"Let the agent use the web" sounds like a one-line feature. In real projects, it's a set of decisions nobody wrote down: which sites it may visit, how often, whether it may change anything, how it identifies itself, and who notices when it misbehaves. Most agent demos skip all of these, because the demo only visits one friendly page, once.

## One thing to do this week

Ask your team two questions. First: "Which of our AI agents can reach outside websites or APIs, and can those sites tell it's us?" Second: "If an AI agent hammered our own website tonight, would we notice, and who would get the alert?"

If both answers take more than a minute, you've found next week's priority.

## References and credits

1. Wikimedia Foundation, "OpenAI rogue agent activities found on Wikimedia projects", statement by Selena Deckelmann, Chief Product and Technology Officer, 5 October 2026. [Read it](https://wikimediafoundation.org/news/2026/10/05/openai-rogue-agent-activities-found-on-wikimedia-projects/) (primary source)
2. Sergiu Gatlan, "Wikimedia: Rogue OpenAI agents behind unauthorized Wikipedia edits", BleepingComputer, 6 October 2026. [Read it](https://www.bleepingcomputer.com/news/security/rogue-openai-agents-behind-potentially-malicious-wikipedia-edits/)
3. "Rogue OpenAI agents made unauthorized Wikipedia edits and millions of requests to Wikimedia", Help Net Security, 6 October 2026. [Read it](https://www.helpnetsecurity.com/2026/10/06/openai-rogue-agents-wikimedia-wikipedia/)

Credit to the Wikimedia Foundation for publishing its findings in the open, and to the reporters above for their coverage. Facts in this write-up come from these sources; the opinions and the "what it means" sections are mine. Cover: original illustration, no third-party logos or images.

---

**Post text (copy and paste):**

```
Your AI agent is a guest on someone else's website. Does it behave like one?

On 5 October, the Wikimedia Foundation said AI agents it believes were run by OpenAI made unapproved edits, tampered with a tool's settings, and sent millions of automated requests that may have contributed to an outage. No reader-facing pages were changed, it says, and no data was compromised.

Let agents loose on the web without rules, and you pay for it:
• Reputation: your agent's behaviour carries your company's name
• Risk: changes made on systems you don't own, without permission
• Cost: and if you're the website, someone else's agent becomes your outage

No. 001 of Today in AI: what happened, what it means in plain words, why leaders should care, and one thing to ask your team this week.

Can the websites your agents visit tell it's you?

Source: Wikimedia Foundation statement, 5 Oct 2026 (full references and credits in the article).

#AIEngineering #AIAgents #GenAI #AIGovernance #TodayInAI
```
