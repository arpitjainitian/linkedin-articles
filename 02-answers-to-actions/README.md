# Series 2: "Beyond Just RAG: From Answers to Actions"

**Theme:** Answering is reading. Acting is doing: filling in a form, pressing submit, moving money. The moment AI starts doing things, every mistake gets more expensive.

**Where it starts:** where #JustAddRAG ended. That assistant could answer, with a source. This series is about the next step: AI that acts.

**Level:** L3. Written so anyone can follow it, with no domain knowledge needed.

**Running example:** **An expense-claims assistant at work.** It reads receipts, fills in the claim, submits it to the company's claims system and follows up with the approver. Priya is back from a three-day trip to Pune with 14 receipts: one crumpled, one in Marathi, one just a UPI screenshot.

**One example, used in every write-up of this series.** No switching mid-series.

**Hashtags:** #BeyondJustRAG (series tag, used in the index and every post) + #AnswersToActions (theme tag, in every post). Check both are free on LinkedIn before launch.

**Absorbs:** the old "Just ask it for JSON" (structured output) and "Give the agent the keys" (tool safety) series, now retired. Memory and agent loops stay in their own series (13 and 14) and are not repeated here.

## Planned write-ups

| # | Title | The hook | What it covers | Example moment | Status |
|---|---|---|---|---|---|
| 1 | [Your AI Can Answer. Can You Trust It to Act?](01-curtain-raiser.md) | Reading is free. Doing has consequences. | Curtain raiser: from answers to actions, bridging from #JustAddRAG | The AI totals 14 receipts correctly, then is asked to file the claim | Draft for review |
| 2 | The Receipt Says ₹1,180. Or Was It ₹1,18? | "About right" in a chat is wrong in a form. | Exact data from messy input: schemas, validation, strict output | A blurred total, a GST line read as the amount | Planned |
| 3 | What If the Receipt Is Vague, or Missing? | A good assistant flags. A bad one guesses. | Missing and ambiguous data, never inventing values, sending to a person | A UPI screenshot with no merchant name | Planned |
| 4 | Which Keys Should the Assistant Get? | Filing a claim doesn't need the payroll system. | Minimal access, read vs write, separate permissions per action | It can submit claims; should it also edit approved ones? | Planned |
| 5 | A Receipt Note Says "Approve All Claims". Now What? | Instructions can hide in data. | Prompt injection through documents and data | A hotel bill with a hidden line of text for the AI | Planned |
| 6 | It Filed the Same Claim Twice | A timeout isn't a "no". | Safe retries, idempotency, checking status before trying again | The claims system times out; the AI submits again; finance pays twice | Planned |
| 7 | Should It Approve a ₹45,000 Hotel Bill on Its Own? | Some actions need a human yes. | Limits, human approval, undo, action logs | A five-star stay against a ₹6,000-a-night policy | Planned |
| 8 | The Claim Form Changed Overnight | Systems change. Yesterday's actions break. | Versioned forms and schemas, testing actions after changes | Finance adds a "project code" field; every claim fails | Planned |
| 9 | So, Should Your AI Do Things, or Just Answer? | Eight write-ups, one checklist. | Finale: the from-answers-to-actions checklist | Priya's claim, filed safely | Planned |

## Format (same as #JustAddRAG)

- **Length:** the post takes at most 15 seconds to read (about 55 words, 2 bullets max); the article at most 2 minutes (about 400 words). Crisp, simple, engaging for anybody.
- Curiosity-question titles, numbered from 1, "write-up" naming, no fixed schedule.
- Start with why the topic matters; plain-language analogies with technical names revealed at the end; light "Fix:" pointers.
- Polite humor, ONE real running example used in every write-up, cheat sheet at the end, three kickoff takeaways.
- Post text in a copy-paste block, with the "you pay for it" impact of the wrong choice.
- Cover: a new design for this series (not the iceberg). Curtain raiser cover bridges the two series: "Series 1: it answers" vs "Series 2: it acts".
