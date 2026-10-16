# Series 3: "Just put the rules in the prompt"

**Theme:** LLMs are great with language and unreliable with rules. Know where the line is.

**Level:** L3. Written so anyone can follow it, with no domain knowledge needed.

**Running example:** **An airline's refund and cancellation assistant.** Refunds depend on fare type, timing and fees. Clear rules, real money.

**One example, used in every write-up of this series.** No switching mid-series.

**Hashtag:** #RulesNeedCode (proposal)

## Planned write-ups

Fewer, stronger write-ups (user rule): old "which decisions" and "how to split" merged into write-up 2; "how do you prove the right rule" dropped (covered by Today in AI No. 006, decision lineage); new: turning a long policy into rules.

| # | Title | The hook | What it covers | Example moment | Status |
|---|---|---|---|---|---|
| 1 | [Why Did the AI Promise a Full Refund on a Non-Refundable Ticket?](01-curtain-raiser.md) | AI is a lovely gate agent. It shouldn't be the rulebook. | Curtain raiser: why rules don't belong in a prompt | "Of course! Full refund, no fees" | Draft for review |
| 2 | [Code Decides. The AI Explains.](02-code-decides.md) | Code is the referee, AI is the commentator. | Code makes decisions via tools; the AI explains, never changes numbers; exceptions go to a person | Code says ₹1,240 in taxes; the AI explains it kindly | Draft for review |
| 3 | [The Policy Is 40 Pages. Who Turns It Into Rules?](03-policy-to-rules.md) | AI can draft the rules. People must approve them. | Policy to decision table; vague words; AI drafts with sources, the rule owner signs off; back-testing | "Exceptional circumstances"; 3 of 60 AI-drafted rules invented | Draft for review |
| 4 | [The Waiver Was in the Prompt. Not in the Code.](04-rule-changed.md) | Two price tags, one shirt. | One source of truth, effective dates, reviewed changes, no rules in prompts | Monsoon waiver in the prompt; code charges ₹3,000 | Draft for review |
| 5 | [So, Who Should Decide: the Code or the Model?](05-finale-checklist.md) | Code decides, AI explains, people own the rules. | Finale: 9-point checklist | The refund assistant, fixed | Draft for review |

## Format (same as #JustAddRAG)

- **Course companion:** every write-up also gets `NN-slug.course.md` (learning objective, deep dive, hands-on lab, quiz, checklist line, glossary, further reading, reader questions). See [COURSE.md](../COURSE.md). Never posted on LinkedIn.
- **Link back in every post:** Missed the last series? Start with "Your AI can answer. Now it has to act." <link> (add Series 2's finale link once it's published).
- **Length:** the post takes at most 15 seconds to read (about 55 words, 2 bullets max); the article at most 2 minutes (about 400 words). Crisp, simple, engaging for anybody.
- Curiosity-question titles, numbered from 1, "write-up" naming, no fixed schedule.
- Start with why the topic matters; plain-language analogies with technical names revealed at the end; light "Fix:" pointers.
- Polite humor, ONE real running example used in every write-up, cheat sheet at the end, three kickoff takeaways.
- Post text in a copy-paste block, with the "you pay for it" impact of the wrong choice.
- Cover: a completely new design for this series (its own layout, palette and visual idea, not the #JustAddRAG iceberg template). Starting idea: a football match. The LLM is the friendly commentator; the code is the referee with the rulebook. Humor stays.
