"""Generate the FDE series covers as HTML, then render each one to PNG with headless Chrome.

Run from the fde-forward-deployed folder:
    python3 generator/covers.py

Each cover shows the customer's problems only. The fixes stay in the article.
Check every cover's words against its article once the article is written.
"""
import pathlib
import subprocess

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
IMAGES = pathlib.Path(__file__).resolve().parent.parent / "images"

CSS = """
  :root { --navy: #0f1d3a; --navy-2: #17294f; --pink: #f9b8d4; --mint: #b8f2d8;
          --lilac: #cdb8f9; --butter: #fbe9a6; --text: #f4f7ff; --muted: #b9c4e0; }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { width: 1920px; height: 1080px; background: var(--navy); color: var(--text);
         font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", Arial, sans-serif;
         overflow: hidden; position: relative; }
  .tag { position: absolute; left: 110px; top: 80px; font-size: 26px; letter-spacing: 6px;
         color: var(--mint); font-weight: 700; }
  h1 { position: absolute; left: 110px; top: 130px; width: 1700px; line-height: 1.08;
       font-weight: 800; font-size: @@SIZE@@px; }
  h1 mark { background: var(--butter); color: var(--navy); padding: 0 12px; border-radius: 10px; }
  .panel { position: absolute; top: 400px; width: 640px; height: 500px; border-radius: 28px;
           padding: 44px 48px; background: var(--navy-2); border: 3px solid; }
  .demo { left: 110px; border-color: var(--mint); }
  .monday { left: 1170px; border-color: var(--pink); }
  .label { font-size: 30px; letter-spacing: 4px; font-weight: 800; margin-bottom: 26px; }
  .demo .label { color: var(--mint); }
  .monday .label { color: var(--pink); }
  .card { background: var(--navy); border-radius: 18px; padding: 26px 30px; font-size: 30px;
          line-height: 1.4; color: var(--text); margin-bottom: 14px; }
  .ok { color: var(--mint); font-weight: 800; }
  .chip { display: inline-block; font-size: 26px; padding: 12px 22px; border-radius: 999px;
          margin: 0 12px 12px 0; font-weight: 700; color: var(--navy); }
  .c1 { background: var(--pink); } .c2 { background: var(--lilac); }
  .c3 { background: var(--butter); } .c4 { background: var(--mint); }
  .arrow { position: absolute; left: 790px; top: 620px; width: 340px; font-size: 40px;
           color: var(--muted); text-align: center; font-weight: 700; letter-spacing: 2px; }
  .bar { position: absolute; left: 0; right: 0; bottom: 0; height: 150px; background: var(--lilac);
         color: var(--navy); display: flex; align-items: center; justify-content: space-between;
         padding: 0 110px; font-size: 44px; font-weight: 800; }
  .bar span:last-child { font-size: 36px; font-weight: 700; }
"""

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<style>{css}</style>
</head>
<body>
  <div class="tag">{tag}</div>
  <h1>{title}</h1>
  <div class="panel demo">
    <div class="label">THE DEMO</div>
    <div class="card">{demo_1}</div>
    <div class="card">{demo_2}</div>
  </div>
  <div class="arrow">SAME ASSISTANT,<br>NEW WORLD</div>
  <div class="panel monday">
    <div class="label">THE CUSTOMER</div>
    <div>{chips}</div>
    <div class="card">{q_1}</div>
    <div class="card">{q_2}</div>
  </div>
  <div class="bar">
    <span>The demo is the easy part.</span>
    <span>#ForwardDeployed</span>
  </div>
</body>
</html>
"""

# (number, tag, title, demo card 1, demo card 2, problem chips, question 1, question 2)
COVERS = [
    (2, "WRITE-UP 2 · WEEK 1",
     "What should you learn from the customer before you build anything?",
     "Built first", "Asked later",
     ["No baseline", "Value unclear", "Wrong workflow", "Three owners"],
     "What would make this worth paying for?", "Who says it worked?"),
    (3, "WRITE-UP 3 · WEEK 2",
     "How do you turn the customer's rules into something you can test?",
     "Rules in a document", "Nobody checked them",
     ["Unwritten rules", "Changing APIs", "No tests"],
     "Which rules must the system follow?", "How will we know it does?"),
    (4, "WRITE-UP 4 · WEEK 3",
     "Where does the customer's data hide, and which copy is true?",
     "One clean file", "Looks perfect",
     ["Three copies", "Duplicate customers", "No owner", "Stale prices"],
     "Which system is the record of truth?", "Who fixes the bad rows?"),
    (5, "WRITE-UP 5 · WEEK 4",
     "What happens when two of the customer's systems disagree?",
     "One system, one answer", "Simple",
     ["Two systems", "Timeouts", "Duplicate events", "Retries"],
     "What happens to an order when the systems disagree?", "Who sees the mismatch first?"),
    (6, "WRITE-UP 6 · WEEK 5",
     "How do you let a model act in the customer's systems without breaking their records?",
     "Chat says: done", "Record not changed",
     ["Writes to live records", "Unchecked fields", "No approval step"],
     "Which actions may the assistant take on its own?", "Who can undo a wrong change?"),
    (7, "WRITE-UP 7 · PHASE 2",
     "How do you write prompts the customer's security team will sign off?",
     "Prompt works in the demo", "Looks clever",
     ["Ignored rules", "Leaks data", "Fails security review"],
     "What must the prompts never do in this business?", "Who signs off the wording?"),
    (8, "WRITE-UP 8 · WEEK 6",
     "How do you make answers point to the customer's own documents?",
     "Answer sounds sure", "Confident tone",
     ["Old policy", "Wrong document", "No source", "Missing access check"],
     "Can the customer check every answer?", "Who sees which document?"),
    (9, "WRITE-UP 9 · PHASE 1",
     "Fine-tune, retrieve or prompt: which fits the customer's problem?",
     "Model learns our style", "Looks trained",
     ["Costly retraining", "Stale knowledge", "Unclear gain"],
     "Does the customer need new knowledge or new behaviour?", "What does each option cost?"),
    (10, "WRITE-UP 10 · WEEK 7",
     "What happens when an agent stops halfway through the customer's job, and who steers it?",
     "Job finished in the demo", "Smooth run",
     ["Stops halfway", "Repeats steps", "No one approves"],
     "Who approves a step?", "Where does the job resume?"),
    (11, "WRITE-UP 11 · PHASE 3",
     "Who decides when several agents work on the customer's case?",
     "One agent, clear task", "Easy to follow",
     ["Agents disagree", "Unclear owner", "Costs stack up"],
     "Which agent owns which part of the case?", "Who stops a loop?"),
    (12, "WRITE-UP 12 · PHASE 3",
     "How do you test the customer's assistant before a stranger does?",
     "Works for the happy customer", "Friendly test",
     ["Clever wording", "Biased answers", "Hidden instructions"],
     "How could someone misuse this against the customer?", "Who checks the attacks?"),
    (13, "WRITE-UP 13 · WEEK 8",
     "How do you show the customer it is good enough, and what it will cost them?",
     "Works on ten questions", "Team is happy",
     ["No test set", "Unknown cost per answer", "Slow replies", "Judge bias"],
     "What quality and cost are acceptable?", "Who signs the release?"),
    (14, "WRITE-UP 14 · WEEK 9",
     "Who at the customer may do what, and can you prove it later?",
     "One shared admin login", "Works for now",
     ["Shared access", "No audit trail", "Personal data exposed"],
     "Who is accountable for each decision?", "Can you prove it a year later?"),
    (15, "WRITE-UP 15 · WEEK 10",
     "Where should it run in the customer's cloud, and who restarts it at 2 am?",
     "Runs on my laptop", "Works fine here",
     ["Wrong region", "Secrets in code", "No restart plan", "Network gaps"],
     "Which cloud may the customer's data touch?", "Who restarts it at 2 am?"),
    (16, "WRITE-UP 16 · WEEK 11",
     "How does the customer know it is working on a Tuesday afternoon?",
     "Green dashboard", "Everything up",
     ["No alerts", "Silent failures", "Slow answers", "No owner"],
     "Who is told first when it degrades?", "How long until someone notices?"),
    (17, "WRITE-UP 17 · WEEK 12",
     "How do you run a pilot with real users without betting the customer's business?",
     "Demo day went well", "Team cheered",
     ["Real users", "Old data", "No rollback", "Unhappy branch"],
     "What must the team see before switching over?", "What happens if we roll back?"),
    (18, "WRITE-UP 18 · WEEK 13",
     "What does the customer's team need to run this without you?",
     "Built by one person", "Known only to you",
     ["No runbook", "Unknown owner", "No feedback loop"],
     "Who owns it after you leave?", "What does the team do on day one?"),
    (19, "WRITE-UP 19 · PHASE 4",
     "Which AI bets should the customer make first, and how do you score the risk?",
     "Ten AI ideas", "All exciting",
     ["No priority", "Unclear value", "Hidden risks", "No roadmap"],
     "Which problem is worth the money first?", "What is the risk if we wait?"),
    (20, "FINALE · CAPSTONE",
     "Is it ready for the customer, or only for the demo?",
     "Demo ready", "Team confident",
     ["Not tested", "Not owned", "Not measured", "Not handed over"],
     "Would the customer accept this?", "Would the customer keep using it?"),
]


def title_size(title):
    """Shrink long headlines so they stay inside two lines above the panels."""
    if len(title) <= 70:
        return 84
    if len(title) <= 95:
        return 68
    return 60


def build(number, tag, title, demo_1, demo_2, chips, q_1, q_2):
    chip_html = "".join(
        f'<span class="chip c{(i % 4) + 1}">{chip}</span>' for i, chip in enumerate(chips)
    )
    css = CSS.replace("@@SIZE@@", str(title_size(title)))
    return TEMPLATE.format(
        css=css, tag=tag, title=title, demo_1=demo_1, demo_2=demo_2,
        chips=chip_html, q_1=q_1, q_2=q_2,
    )


def main():
    for row in COVERS:
        number = row[0]
        stem = f"{number:02d}-cover"
        html_path = IMAGES / f"{stem}.html"
        png_path = IMAGES / f"{stem}.png"
        html_path.write_text(build(*row), encoding="utf-8")
        subprocess.run(
            [CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
             "--window-size=1920,1080", f"--screenshot={png_path}", str(html_path)],
            check=True, stderr=subprocess.DEVNULL,
        )
        print("wrote", png_path.name)


if __name__ == "__main__":
    main()
