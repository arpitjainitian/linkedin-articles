# Series 7: "Just ask it for JSON"

**Theme:** Getting text from an LLM is easy. Getting reliable data out of it is engineering, and here, mistakes affect real people.

**Level:** L3. Written so anyone can follow it, with no domain knowledge needed.

**Running example:** **Resume screening.** AI turns CVs into structured candidate profiles: name, skills, years of experience, last company.

**One example, used in every write-up of this series.** No switching mid-series.

**Hashtag:** #JustAskForJSON (proposal)

## Planned write-ups

| # | Title | The hook | What it covers | Example moment | Status |
|---|---|---|---|---|---|
| 1 | Why Does the "Perfect" Candidate Profile Break One Time in Fifty? | Mostly right is still broken for a computer. | Curtain raiser: structured output | One missing field and the candidate vanishes from the shortlist | Planned |
| 2 | What If the Model Invents a Skill? | "Kubernetes expert" isn't on the CV. | Schemas, validation, strict output modes | A skill the candidate never mentioned | Planned |
| 3 | What Do You Do With "5+ Years, Approx"? | Real CVs are vague. | Missing, ambiguous and partial data, flagging for review | "2019 to present" or "5 years"? | Planned |
| 4 | Should You Retry, Repair or Send It to a Human? | Every bad output needs a plan. | Retries, repair, fallbacks, human review | Two jobs in the same years, read as 10 years' experience | Planned |
| 5 | What Happens When the Profile Format Changes? | Schemas grow. Old prompts don't know. | Versioning, backwards compatibility | New field "notice period"; old profiles break the dashboard | Planned |
| 6 | So, Can You Trust Your Model's Output? | Five write-ups, one checklist. | Finale: the structured-output checklist | A CV, validated end to end | Planned |

## Format (same as #JustAddRAG)

- Curiosity-question titles, numbered from 1, "write-up" naming, no fixed schedule.
- Start with why the topic matters; plain-language analogies with technical names revealed at the end; light "Fix:" pointers.
- Polite humor, ONE real running example used in every write-up, cheat sheet at the end, three kickoff takeaways.
- Post text in a copy-paste block, with the "you pay for it" impact of the wrong choice.
- Cover: a completely new design for this series (its own layout, palette and visual idea, not the #JustAddRAG iceberg template). Starting idea: a sorting line. Messy CVs go in, neat labelled boxes come out, a few fall off the belt. Humor stays.
