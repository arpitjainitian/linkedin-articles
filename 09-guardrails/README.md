# Series 9: "Just tell it not to"

**Theme:** A prompt is a polite request. Guardrails are the fence.

**Level:** L3. Written so anyone can follow it, with no domain knowledge needed.

**Running example:** **An online pharmacy's medicine-question assistant.** "Can I take this with my BP tablet?" It must never prescribe or set doses.

**One example, used in every write-up of this series.** No switching mid-series.

**Hashtag:** #JustTellItNot (proposal)

## Planned write-ups

| # | Title | The hook | What it covers | Example moment | Status |
|---|---|---|---|---|---|
| 1 | [Why Didn't "Please Don't Give Medical Advice" Work?](01-curtain-raiser.md) | Instructions are suggestions to a model. | Curtain raiser: prompts vs guardrails | "Take two tablets twice a day" | Draft for review |
| 2 | What Should You Check Before the Question Reaches the Model? | Not every question deserves an answer. | Input filters, topic limits, risky intents | "How many of these would be dangerous?" | Planned |
| 3 | What Should You Check Before the Answer Reaches the Customer? | The last line of defence is the output. | Output filters, medical-safety checks, tone | An answer that quietly suggests a dose | Planned |
| 4 | What If Someone Tries to Trick It? | Clever wording can talk a model out of its rules. | Jailbreaks, prompt injection, red teaming | "Pretend you're my doctor" | Planned |
| 5 | Who Protects the Customer's Health Details? | Health data is the most sensitive data there is. | Personal data, redaction, what never to store | Prescription details sitting in chat logs | Planned |
| 6 | How Strict Is Too Strict? | A bot that refuses everything is useless too. | Balancing safety and usefulness, false refusals | Refuses to say whether paracetamol is in stock | Planned |
| 7 | So, Is Your AI Fenced or Just Asked Nicely? | Six write-ups, one checklist. | Finale: the guardrails checklist | The pharmacy assistant, safe by design | Planned |

## Format (same as #JustAddRAG)

- Curiosity-question titles, numbered from 1, "write-up" naming, no fixed schedule.
- Start with why the topic matters; plain-language analogies with technical names revealed at the end; light "Fix:" pointers.
- Polite humor, ONE real running example used in every write-up, cheat sheet at the end, three kickoff takeaways.
- Post text in a copy-paste block, with the "you pay for it" impact of the wrong choice.
- Cover: a completely new design for this series (its own layout, palette and visual idea, not the #JustAddRAG iceberg template). Starting idea: a castle. The polite "please don't" sign on the gate vs the walls, moat and guards. Humor stays.
