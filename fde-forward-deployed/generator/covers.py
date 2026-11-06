"""Generate the FDE series covers as HTML, then render each one to PNG with headless Chrome.

Run from the fde-forward-deployed folder:
    python3 generator/covers.py

Each cover shows the customer's problems only. The fixes stay in the article.
Every cover word, and the headline, must appear in the matching article.
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

# (number, tag, headline = the article title, demo card 1, demo card 2,
#  problem chips, customer card 1, customer card 2)
# Every text here appears word for word in the matching article.
COVERS = [
    (2, "WRITE-UP 2 · WEEK 1",
     "What Should You Learn From the Customer Before You Build Anything?",
     "A working assistant", "Nobody had measured the answer",
     ["No baseline", "Value unclear", "Wrong workflow", "Three owners"],
     "What would make this worth paying for?", "Who says it worked?"),
    (3, "WRITE-UP 3 · WEEK 2",
     "How Do You Turn the Customer's Rules Into Something You Can Test?",
     "The rules lived in a document", "Nobody had checked them against the system",
     ["Unwritten rules", "Changing APIs", "No tests"],
     "Each example becomes a test", "A failed test tells you the rule and the system disagree"),
    (4, "WRITE-UP 4 · WEEK 3",
     "Where Does the Customer's Data Hide, and Which Copy Is True?",
     "The stock file says 40 units", "Clean and easy to read",
     ["Three copies", "Duplicate customers", "No owner", "Stale prices"],
     "Which system is the record, and which ones are copies?", "Ask who fixes a bad row"),
    (5, "WRITE-UP 5 · WEEK 4",
     "What Happens When Two of the Customer's Systems Disagree?",
     "One system sent an order", "The message arrived",
     ["Two systems", "Timeouts", "Duplicate events", "Retries"],
     "The order says shipped", "Who sees a mismatch first"),
    (6, "WRITE-UP 6 · WEEK 5",
     "How Do You Let a Model Act in the Customer's Systems Without Breaking Their Records?",
     "Done. I've updated", "The record had not changed",
     ["Writes to live records", "Unchecked fields", "No approval step"],
     "Decide which changes need a person to approve them", "Who can undo a wrong change"),
    (7, "WRITE-UP 7 · PHASE 2",
     "How Do You Write Prompts the Customer's Security Team Will Sign Off?",
     "It worked on our sample orders", "The prompt looked clever",
     ["Ignored rules", "Leaks data", "Fails security review"],
     "What the prompt must never say or reveal", "The owner who signs each prompt change"),
    (8, "WRITE-UP 8 · WEEK 6",
     "How Do You Make Answers Point to the Customer's Own Documents?",
     "Said it with full confidence", "Sounded just as sure",
     ["Old policy", "Wrong document", "No source", "Missing access check"],
     "The answer is not ready for a customer", "Only see the documents the person asking is allowed to see"),
    (9, "WRITE-UP 9 · PHASE 1",
     "Fine-Tune, Retrieve or Prompt: Which Fits the Customer's Problem?",
     "Train the model on our own style", "It looked like a training job",
     ["Costly retraining", "Stale knowledge", "Unclear gain"],
     "Ask what kind of change is needed", "The cost per answer"),
    (10, "WRITE-UP 10 · WEEK 7",
     "What Happens When an Agent Stops Halfway Through the Customer's Job?",
     "The agent processed a claim from start to finish", "In under a minute",
     ["Stops halfway", "Repeats steps", "No one approves"],
     "Name the approver for each", "Resumes from the last saved step"),
    (11, "WRITE-UP 11 · PHASE 3",
     "Who Decides When Several Agents Work on the Customer's Case?",
     "Pick one agent to own the customer's case", "The specialists answer questions",
     ["Agents disagree", "Unclear owner", "Costs stack up"],
     "Who writes the final answer", "Stop and send the case to a person"),
    (12, "WRITE-UP 12 · PHASE 3",
     "How Do You Test the Customer's Assistant Before a Stranger Does?",
     "The happy customer was served well", "Our tests only ever used friendly questions",
     ["Clever wording", "Biased answers", "Hidden instructions"],
     "Get a refund outside the limit", "Agree who runs the attack tests"),
    (13, "WRITE-UP 13 · WEEK 8",
     "How Do You Show the Customer It Is Good Enough, and What It Will Cost Them?",
     "It worked on ten questions", "The team had tested the assistant",
     ["No test set", "Unknown cost per answer", "Slow replies", "Judge bias"],
     "The accuracy the desk accepts", "Who signs the release"),
    (14, "WRITE-UP 14 · WEEK 9",
     "Who at the Customer May Do What, and Can You Prove It Later?",
     "Set up on a shared admin login", "The one everybody used to test",
     ["Shared access", "No audit trail", "Personal data exposed"],
     "Each person gets their own login", "Prove it a year later"),
    (15, "WRITE-UP 15 · WEEK 10",
     "Where Should It Run in the Customer's Cloud, and Who Restarts It at 2 am?",
     "Works on my laptop", "Did work on the laptop",
     ["Wrong region", "Secrets in code", "No restart plan", "Network gaps"],
     "Which regions, networks and clouds their data may use", "Who restarts it at 2 am"),
    (16, "WRITE-UP 16 · WEEK 11",
     "How Does the Customer Know It Is Working on a Tuesday Afternoon?",
     "The dashboard is green", "The server was up",
     ["No alerts", "Silent failures", "Slow answers", "No owner"],
     "Name who is told first", "No one saw the trend"),
    (17, "WRITE-UP 17 · WEEK 12",
     "How Do You Run a Pilot With Real Users Without Betting the Customer's Business?",
     "Demo day went well", "The room cheered",
     ["Real users", "Old data", "No rollback", "Unhappy branch"],
     "Where the desk had to step in", "Write the rollback down before the pilot starts"),
    (18, "WRITE-UP 18 · WEEK 13",
     "What Does the Customer's Team Need to Run This Without You?",
     "Built by one person", "The knowledge had never left that person's head",
     ["No runbook", "Unknown owner", "No feedback loop"],
     "Who will own the assistant after the handover", "Does the restart themselves"),
    (19, "WRITE-UP 19 · PHASE 4",
     "Which AI Bet Should the Customer Make First, and How Do You Score the Risk?",
     "Ten AI ideas", "Each one sounded exciting",
     ["No priority", "Unclear value", "Hidden risks", "No roadmap"],
     "Which problem was worth the money", "What would happen if they waited a year"),
    (20, "FINALE · CAPSTONE",
     "Is It Ready for the Customer, or Only for the Demo?",
     "The demo is ready", "The team was confident",
     ["Not tested", "Not owned", "Not measured", "Not handed over"],
     "The demo is not ready", "Would the customer keep using it"),
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
