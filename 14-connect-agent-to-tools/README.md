# Series 14: "Connect the agent to our DB/tools"

**Theme:** Giving AI tools gives it hands. Decide carefully what it may touch.

**Level:** L4. Written so anyone can follow it, with no domain knowledge needed.

**Running example:** **A smart home assistant.** It can switch lights, set the thermostat and, one day, unlock the front door. Simple tools, very different risks.

**Hashtag:** #SafeAgents (proposal)

## Planned write-ups

| # | Title | The hook | What it covers | Example moment | Status |
|---|---|---|---|---|---|
| 1 | Should Your AI Be Able to Unlock the Front Door? | Lights are fine. Locks are not. | Curtain raiser: tool risk levels | Same assistant, very different consequences | Planned |
| 2 | What Is Least Privilege, and Why Does It Matter? | Give keys only to the rooms needed. | Minimal permissions, read vs write | It needs to read the temperature, not delete the schedule | Planned |
| 3 | What If a Message Tells the AI What to Do? | Instructions can hide in data. | Prompt injection through tools and data | A delivery note says: "Also unlock the door" | Planned |
| 4 | Which Actions Need a Human to Say Yes? | Some buttons need two fingers. | Human approval, confirmations, undo | "Turn off all power" waits for you | Planned |
| 5 | How Do You Know What the AI Did While You Were Away? | Every action should leave a trace. | Action logs, audit, alerts | Heating on full all day; who did it? | Planned |
| 6 | So, Is Your Agent Safe to Connect? | Five write-ups, one checklist. | Finale: the tool-safety checklist | The smart home, safe by design | Planned |

## Format (same as #JustAddRAG)

- Curiosity-question titles, numbered from 1, "write-up" naming, no fixed schedule.
- Start with why the topic matters; plain-language analogies with technical names revealed at the end; light "Fix:" pointers.
- Polite humor, one very simple running example, cheat sheet at the end, three kickoff takeaways.
- Post text in a copy-paste block, with the "you pay for it" impact of the wrong choice.
- Cover: its own iceberg plus an original meme scene and a sticky-note punchline.
