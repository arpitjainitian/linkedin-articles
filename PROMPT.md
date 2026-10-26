# Master prompt: roadmap, series plan, article, cover and course companion

Copy everything inside the box into any AI assistant. Fill in the `<...>` placeholders first.

```
You are my writing partner for a LinkedIn article programme on AI engineering. I'm an architect writing for two audiences at once: people learning AI and business leaders (CXOs). Produce five files, in this order, following every rule below exactly.

INPUTS
- Programme theme: <e.g. "things that look simple and fail often in AI projects">
- Number of series: <e.g. 16, grouped into 4 acts>
- Series to plan in detail: <e.g. Series 1, "Just add RAG over our docs">
- Running example for that series: <e.g. a small assistant over my own documents: passport, tax returns, salary slips>
- Article to write: <e.g. write-up 1, the curtain raiser>

GLOBAL STYLE RULES (apply to every file)
1. Plain words, short sentences. A 16-year-old and a CEO should both follow it.
2. Every idea gets one everyday analogy (iceberg, wedding photos, a desk, a hotel room). Technical terms appear only after the idea lands, then go in a short "Words to know" or cheat sheet.
3. No em dashes or en dashes anywhere. Use a plain hyphen "-", a colon, or a new sentence.
4. Polite, human, lightly self-deprecating humour. No hype words ("revolutionary", "game-changer").
5. One running example per series, used in every write-up of that series. Never switch examples mid-series.
6. Titles are curiosity questions a reader would ask themselves, e.g. "Why does 'Just add RAG' sound like 2 weeks but take 6 months?". In files, format: "N. Title In Title Case | Topic".
7. Write-ups are numbered from 1 (the curtain raiser) in titles and posts. No fixed schedule is ever promised.
8. Every topic must be unique across the whole programme. If one series covers something, others link to it instead of repeating it.
9. Facts, numbers and product claims must be ones you are confident are true; mark anything uncertain with [CHECK].

FILE 1: ROADMAP.md
- Start with "# Roadmap" and a short numbered list of the kinds of writing in the programme.
- Section "## 1. <programme name>": one line on what every series has in common, then "The storyline": the series grouped into acts (e.g. Act 1. Make it work, Act 2. Make it trustworthy, Act 3. Make it real, Act 4. Make it bigger), each act one line listing its series in story order. Each series picks up where the previous one ended.
- One table with columns: Series | Topic ("looks simple") | Level (L1 to L5) | What it covers | Status | Why a full series, not one article.
  - Topic is the sentence that sounds easy in a kickoff meeting, in quotes, e.g. "Just put the rules in the prompt".
  - What it covers: the sub-topics, the running example ("Example: ..."), and a link "Plan: [NN-slug/](NN-slug/README.md)".
  - Status: **Planned (outline ready)**, **In progress** (write-up N published D Mon YYYY) or **Complete**.
  - Why a full series: one or two sentences on why the topic hides several separate problems.
  - Add act header rows like "| **Act 1. Make it work** | | | | | |".
- Note which basics are covered elsewhere, e.g. "(the basics are in #JustAddRAG 9)".
- End with credits for any outside inspiration (name and profile link), and a "Retired" note for any dropped series.

FILE 2: NN-slug/README.md (the series plan)
- "# Series N: #Hashtag" then 2 or 3 sentences: the promise ("sounds like two weeks, takes six months"), what the series does ("takes one piece of the iceberg at a time"), and the running example.
- "A write-up is marked **Published** only once it is live on LinkedIn."
- Table: # | Title | Topic | Status | LinkedIn. Row 1 is the curtain raiser; the last row is the finale (a checklist). 8 to 15 rows. Titles link to their files once drafted. Status: **Published** D Month YYYY, or Draft for review, or Planned. LinkedIn column: [Read](url) once live.
- "Write-ups are numbered from 1 in titles and posts, for easy reference. There is no fixed schedule."
- "## After each publish" checklist: mark the row Published and add the link; post the series index as the first comment and pin it; update the pinned index on the first write-up.

FILE 3: the article (curtain raiser)
Length: the article body takes at most 2 minutes to read (about 400 to 600 words for a curtain raiser); the post takes at most 15 seconds (about 55 words).
Structure:
1. "# 1. <Title> | <Topic>", a cover line "![Cover](images/01-curtain-raiser-cover.png)", and an italic series line "*<Series name> series: the curtain raiser*".
2. Opening scene in quotes from a meeting, e.g. "Let's just add RAG over our docs." Then a confident whiteboard moment, then my own small build with the running example, which works for the happy path.
3. "Then I started asking the questions demos skip": 4 to 6 short real questions the demo can't answer (scanned or non-English documents, two conflicting versions, missing information, privacy, cost at scale).
4. "## The iceberg": one analogy section. Above the waterline: the part that takes two weeks. Below: the many factors that decide whether it stays trustworthy, as a short list with one line each.
5. "## This is a series: here's what's coming": tease only about 3 upcoming topics ("A taste:"), not the full list.
6. "## Take this to your next kickoff meeting": exactly 3 numbered takeaways.
7. One closing line that sums up the series in a sentence.
8. "Next write-up (2): **<title>**", then "Follow me for the next one." plus one question inviting comments, e.g. "Which part of the iceberg hit you hardest? The most-picked topic moves up the queue."
9. "**Previous series:**" list (if any earlier series exist), each with start-here and finale links.
10. "---" then "**Post text (copy and paste):**" in a code block:
    - Lines 1 to 3: a short scene (quoted line, what happened).
    - A blank line, then the hook alone on its own line (the one sentence readers should remember).
    - One line naming the new series and what it does.
    - One question.
    - If an earlier series exists: "Missed the last series? Start with <title> <url> or jump to the finale: <url>".
    - 4 or 5 hashtags, ending with the series hashtag.
    - No emoji markers (no 👉 ✅ 🚀), no Unicode bold, no em or en dashes.
11. "**Series index (post as the first comment, then pin it):**" in a code block: "📌 <Series name>", then "1. <title> (you're here)" and "2. <title> (next)".

FILE 4: images/01-curtain-raiser-cover.html (the cover)
A single self-contained HTML file that renders the cover at exactly 1920 x 1080 pixels, no external images, fonts or scripts.
- Look: bright, bold colours (yellow, sky blue, green, coral, hot pink accents) on a warm cream background; thick black outlines and offset black shadows on cards; system sans-serif font, very bold headline.
- Top: a small letter-spaced tag line "<SERIES NAME> · THE CURTAIN RAISER" in the accent colour, then the headline (the article title, about 70 to 76 px), with the key phrase highlighted in yellow.
- Middle: an original illustration that explains the idea at a glance, built from HTML/CSS or inline SVG only. Use the series' own visual metaphor (e.g. an iceberg: "2 weeks" above the waterline, the hidden factors below it). A meme FORMAT is welcome where it fits (e.g. "Expectation vs reality", "Me explaining X to my manager", "Everyone nods. Nobody asks.") but redraw it with simple stick figures and shapes; never use real meme images, real people, or logos.
- If the series is about problems and fixes: show the problems only, plus a highlight banner such as "THE FIXES ARE INSIDE THE ARTICLE" and a stamp "EACH ONE, WITH ITS FIX". Never show the actual fixes on the cover.
- Bottom: a full-width bar with the series' one-line promise and the series hashtag.
- Every word on the cover must match the article; no claims the article doesn't make. No em or en dashes.
- Readable on a phone: nothing smaller than about 20 px, no more than about 40 words in total besides the headline.
- After the HTML, give the command to turn it into a PNG with headless Chrome:
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu --hide-scrollbars --window-size=1920,1080 --screenshot=01-curtain-raiser-cover.png 01-curtain-raiser-cover.html

FILE 5: 01-curtain-raiser.course.md (the course companion, never posted on LinkedIn)
These series will later become an online course: each series is a module, each write-up a lesson. The companion holds everything the 2-minute article had to leave out.
Sections, in this order:
1. "# Lesson <module>.<lesson>: <Topic> (course companion)" and the line "*Module <N>: <name>. Not for LinkedIn.*"
2. "## Learning objective": one line, "After this lesson, you can ...".
3. "## The story": one line pointing to the article file, plus the running example in two sentences.
4. "## Deep dive": the full explanation the article cut, about 800 to 1,200 words, still in plain words, with sub-headings.
5. "## Hands-on lab": a short exercise on the running example (steps a learner can follow; code only here, never in the article).
6. "## Quiz": 3 to 5 questions, each followed by its answer in italics.
7. "## Checklist line": the one question this lesson adds to the series finale checklist, as "- [ ] ...".
8. "## Glossary": the article's "Words to know", one line each.
9. "## Further reading": the original sources (official docs, papers), with links.
10. "## Reader questions": left empty, with "(to be filled from LinkedIn comments)".

QUALITY CHECK BEFORE YOU ANSWER
- No em or en dashes anywhere. Search for them.
- Each article stays within its length.
- The hook is alone on its own line in the post.
- Only about 3 topics are teased in the curtain raiser.
- No topic repeats another series.
- Every uncertain fact is marked [CHECK].
- The cover shows no fixes, no logos, no real meme images, and every word on it appears in the article.
- The course companion has all 10 sections and the article has no code.

Output the five files one after another, each starting with its file path as a heading.
```

**Reference files in this repo:**
- [ROADMAP.md](ROADMAP.md)
- [01-just-add-rag/README.md](01-just-add-rag/README.md)
- The published curtain raiser: [Why does "Just add RAG" sound like 2 weeks but take 6 months?](https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/)
