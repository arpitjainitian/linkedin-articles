# Series 2: "Beyond Just RAG: From Answers to Actions"

**Theme:** Answering is reading. Acting is doing: filling in a form, pressing submit, moving money. The moment AI starts doing things, every mistake gets more expensive.

**Where it starts:** where #JustAddRAG ended. That assistant could answer, with a source. This series is about the next step: AI that acts.

**Level:** L3. Written so anyone can follow it, with no domain knowledge needed.

**Running example:** **An expense-claims assistant at work.** It reads receipts, fills in the claim, submits it to the company's claims system and follows up with the approver. Priya is back from a three-day trip to Pune with 14 receipts: one crumpled, one in Marathi, one just a UPI screenshot.

**One example, used in every write-up of this series.** No switching mid-series.

**Hashtags:** #BeyondJustRAG (series tag, used in the index and every post) + #AnswersToActions (theme tag, in every post). Check both are free on LinkedIn before launch.

**Absorbs:** the old "Just ask it for JSON", "Give the agent the keys" and "Just make it agentic" series, now retired. Not repeated here, because #JustAddRAG already covered them: access (least privilege), prompt injection, and human approval (write-ups 5 and 8). Memory stays in Series 12.

## Planned write-ups

Fewer, stronger write-ups (user rule): every topic must be solid, catchy and unique. Keys, prompt injection and human approval were dropped because #JustAddRAG 5 and 8 already covered them; agent topics came in from the retired "Just make it agentic".

| # | Title | The hook | What it covers | Example moment | Status |
|---|---|---|---|---|---|
| 1 | [Your AI Can Answer. Now It Has to Act.](01-curtain-raiser.md) | Reading is free. Doing has consequences. | Curtain raiser: from answers to actions, bridging from #JustAddRAG | The AI totals 14 receipts correctly, then is asked to file the claim | [Published](https://www.linkedin.com/pulse/1-your-ai-can-answer-now-has-act-from-answers-actions-arpit-jain-po6lf/) 15 October 2026 |
| 2 | [The Receipt Says ₹1,180. Or Was It ₹118?](02-exact-data.md) | "About right" in a chat is wrong in a form. | Exact data from messy receipts; flag it, don't guess | A dropped zero; a UPI screenshot with no merchant name | Draft for review |
| 3 | It Filed the Same Claim Twice | A timeout isn't a "no". | Safe retries, checking status before trying again (idempotency) | The claims system times out; the AI submits again; finance pays twice | Planned |
| 4 | The Claim Was Filed. The Receipts Weren't Attached. | Half-done is worse than not done. | A step fails halfway: undo, resume, or finish | Claim submitted, upload of 14 receipts fails at number 9 | Planned |
| 5 | It Asked for the Same Receipt 40 Times | Loops need exits. | Agents stuck in loops: step limits, stop rules, budgets | It keeps re-checking one blurry taxi receipt | Planned |
| 6 | Does This Even Need an AI Agent? | Not every task needs freedom. | When a simple fixed workflow beats an agent | The same monthly phone bill claim, every month | Planned |
| 7 | Two Claims, Two Different Paths. Which One Was Right? | Same request, different steps. | Testing agents: judging the result and the path | Two runs of Priya's claim take different steps; are both fine? | Planned |
| 8 | So, Should Your AI Do Things, or Just Answer? | Seven write-ups, one checklist. | Finale: the from-answers-to-actions checklist (links back to #JustAddRAG 8 for access and injection) | Priya's claim, filed safely | Planned |

## Format (same as #JustAddRAG)

- **Course companion:** every write-up also gets `NN-slug.course.md` (learning objective, deep dive, hands-on lab, quiz, checklist line, glossary, further reading, reader questions). See [COURSE.md](../COURSE.md). Never posted on LinkedIn.
- **Length:** the post takes at most 15 seconds to read (about 55 words, 2 bullets max); the article at most 2 minutes (about 400 words). Crisp, simple, engaging for anybody.
- **Link back in every post:** every post ends (before the hashtags) with: Missed the first series? Start with "Why does Just add RAG sound like 2 weeks but take 6 months?" <link> or jump to the grand finale: <link>
- Curiosity-question titles, numbered from 1, "write-up" naming, no fixed schedule.
- Start with why the topic matters; plain-language analogies with technical names revealed at the end; light "Fix:" pointers.
- Polite humor, ONE real running example used in every write-up, cheat sheet at the end, three kickoff takeaways.
- Post text in a copy-paste block, with the "you pay for it" impact of the wrong choice.
- Cover: a new design for this series (not the iceberg). Curtain raiser cover bridges the two series: "Series 1: it answers" vs "Series 2: it acts".
