# Series 6: "The prompt works, ship it"

**Theme:** A prompt that works once is a demo. Evals prove it keeps working.

**Level:** L2. Written so anyone can follow it, with no domain knowledge needed.

**Running example:** **A library's book-finder bot.** "Find me a mystery novel for a 12-year-old." Easy to check if the answer is right, hard to check every time.

**Hashtag:** #TestYourAI (proposal)

## Planned write-ups

| # | Title | The hook | What it covers | Example moment | Status |
|---|---|---|---|---|---|
| 1 | It Worked When You Tried It. Will It Work Tomorrow? | "I tried it and it worked" isn't a test. | Curtain raiser: why AI needs evals | Recommends a horror book to a 12-year-old | Planned |
| 2 | What Should Your Test Questions Look Like? | Ten easy questions prove nothing. | Building a real test set, edge cases, tricky questions | "A sad book with a happy ending, not too long" | Planned |
| 3 | Who Writes the Right Answers? | A test needs an answer key. | Ground truth, expert time, keeping it current | The librarian is the only one who knows | Planned |
| 4 | Can an AI Grade Another AI? | Fast marking, if you check the marker. | LLM-as-judge, rubrics, calibration | The judge gives every answer 10/10 | Planned |
| 5 | Why Did a Tiny Prompt Change Break Everything? | Fix one thing, break another. | Regression testing, running tests on every change | "Be more friendly" made it forget age limits | Planned |
| 6 | What Happens When the Model Changes Under You? | Same prompt, new model, different answers. | Version pinning, re-testing before upgrades | Vendor upgrade, suddenly no more children's books | Planned |
| 7 | So, Is Your AI Tested or Just Tried? | Six write-ups, one checklist. | Finale: the evals checklist | The book bot, with a real scorecard | Planned |

## Format (same as #JustAddRAG)

- Curiosity-question titles, numbered from 1, "write-up" naming, no fixed schedule.
- Start with why the topic matters; plain-language analogies with technical names revealed at the end; light "Fix:" pointers.
- Polite humor, one very simple running example, cheat sheet at the end, three kickoff takeaways.
- Post text in a copy-paste block, with the "you pay for it" impact of the wrong choice.
- Cover: its own iceberg plus an original meme scene and a sticky-note punchline.
