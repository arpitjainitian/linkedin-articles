# Curtain raiser "sneak peek" for unpublished series.
# Replaces each series' curtain raiser article with a post-only file (post text + cover + series index),
# and renders a cover that lists every topic of the series.
# Usage: python3 tools/sneak_peek.py <linkedin-articles root> <work dir>   (run from the repo root)
import sys, os, re, html, subprocess
ROOT, WORK = sys.argv[1], sys.argv[2]
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
PAL = ['#F7B7C5', '#FFE8A3', '#8EC5E8', '#A8E6CF', '#C3B1E1']
SERIES = [
 ("04-guardrails", "Just tell it not to", ["Prompts vs guardrails", "Input checks", "Output checks", "Red teaming", "Staff exceptions", "Safety vs usefulness", "Guardrails checklist"]),
 ("05-the-prompt-works-ship-it", "Works on my prompt", ["Trying it vs testing it", "Right answer, wrong reason", "AI graders", "Launch score", "Test-set leaks", "Tested or just tried"]),
 ("06-observability", "We'll know when it breaks", ["Tracing a slow answer", "The surprise bill", "Wrong answers nobody reported", "Breaking it on purpose", "Up vs correct", "Seeing inside your AI"]),
 ("07-poc-to-production", "It worked in the demo", ["Demo to production", "10 invoices vs 10,000", "Owner after launch", "Peak load", "Realistic timelines", "Audit review", "Rollout plan", "Kill switch", "Production ready?"]),
 ("08-few-cents-per-call", "What's a few cents between friends?", ["Sale-day bills", "Pricing your feature", "API vs own GPUs", "Now vs later answers", "Which features pay off", "Forecasting the bill", "What it will really cost"]),
 ("09-ai-transformation", "We bought AI, so we're AI-first now", ["Adoption vs change", "Defining the problem", "Old and new side by side", "Fear and resistance", "Tools vs habits", "Changing jobs", "Rules for AI use", "Measuring it works", "Transforming or subscribing?"]),
 ("10-ai-gateway", "Everyone gets an API key", ["Shared keys and risks", "Model access rules", "One team floods the provider", "Provider outages", "Cost by team", "Do you need a front door?"]),
 ("11-mcp-server", "Just plug it in", ["What MCP is", "Whose login?", "Trusting other servers", "Tools that change", "Picking the right tool", "Is MCP plug-and-play?"]),
 ("12-ai-memory", "It should just remember me", ["Forgetting ten minutes later", "Remembering next week", "What to forget", "Who can see memory", "More memory, better advice", "What should it remember?"]),
 ("13-knowledge-graph", "Just connect the dots", ["Which products are at risk?", "What a graph really is", "Building the graph", "Suppliers change", "When a graph is worth it", "Should you add one?"]),
 ("14-agentic-rag", "Let it do its own research", ["Searching more than once", "Choosing the next search", "Why simple questions are slow", "Knowing research is done", "When plain RAG is enough", "Should your agent research?"]),
 ("15-multi-agent", "More agents, more brains", ["Do more agents mean smarter AI?", "Who is in charge?", "What each agent needs", "Small mistakes that grow", "Extra cost and time", "Should you add more agents?"]),
 ("16-agent-harness", "We bought the brain, we're done", ["The system around the model", "Where the agent keeps its place", "Practice before real claims", "The worst allowed action", "What the model sees", "Five small gaps", "Building the whole system"]),
]
DOMAINS = [
 ("Agentic architecture", "27%", ["Agentic loops", "Coordinator and subagents", "Subagent spawning", "Multi-step workflows", "Agent SDK hooks", "Task decomposition", "Session state and forking"]),
 ("Tool design and MCP", "18%", ["Tool interface design", "MCP error responses", "Tool distribution", "MCP in Claude Code", "Built-in tools"]),
 ("Claude Code setup", "20%", ["CLAUDE.md hierarchy", "Slash commands and skills", "Path-specific rules", "Plan mode vs direct", "Iterative refinement", "CI/CD integration"]),
 ("Prompts and output", "20%", ["Explicit criteria", "Few-shot prompting", "Structured output", "Validation and retry", "Batch processing", "Multi-pass review"]),
 ("Context and reliability", "15%", ["Long conversations", "Escalation patterns", "Error propagation", "Large codebases", "Human review", "Provenance and doubt"]),
]
CSS = '''*{box-sizing:border-box;margin:0;padding:0}html,body{width:1920px;height:1080px;overflow:hidden}
body{font-family:-apple-system,"Helvetica Neue",Arial,sans-serif;color:#2E2A4F;position:relative;background:linear-gradient(180deg,#D9CCF2 0%,#EAE4F7 45%,#F1F8F4 100%)}
.pill{position:absolute;left:110px;top:60px;background:#fff;border-radius:999px;padding:14px 30px;font-size:22px;font-weight:900;letter-spacing:4px}
h1{position:absolute;left:110px;top:110px;width:1700px;font-size:84px;line-height:1.05;font-weight:900;letter-spacing:-1px}
.sub{position:absolute;left:110px;top:262px;width:1700px;font-size:32px;font-weight:700;color:#7B5BC4}
.grid{position:absolute;left:110px;top:360px;width:1700px;display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.chip{background:#fff;border-radius:18px;box-shadow:0 12px 28px rgba(46,42,79,.14);border-left:14px solid var(--c);padding:22px 26px;height:150px;display:flex;flex-direction:column;justify-content:center}
.chip .n{font-size:22px;font-weight:900;letter-spacing:3px;color:#7B5BC4}
.chip .t{font-size:32px;font-weight:800;margin-top:8px;line-height:1.15}
.chip.fin{border-style:dashed;border-width:3px;border-color:#7B5BC4;border-left-width:3px;background:#F6F2FD}
.doms{position:absolute;left:110px;top:360px;width:1700px;display:grid;grid-template-columns:repeat(5,1fr);gap:18px}
.dom{background:#fff;border-radius:18px;box-shadow:0 12px 28px rgba(46,42,79,.14);overflow:hidden}
.dom .h{color:#fff;padding:18px 18px;font-size:22px;font-weight:900;background:var(--c);color:#2E2A4F}
.dom .h small{display:block;font-size:18px;font-weight:700;margin-top:4px}
.dom ul{list-style:none;padding:12px 14px}
.dom li{font-size:22px;font-weight:700;padding:10px 8px;border-bottom:1px dashed #C9C2E0;line-height:1.2}
.dom li:last-child{border-bottom:none}
.bar{position:absolute;left:0;top:990px;width:1920px;height:90px;background:#3E3A6B;color:#fff;font-size:28px;font-weight:800;display:flex;justify-content:space-between;align-items:center;padding:0 110px}
'''
def clean_title(t):
    t = re.sub(r'^\d+\.\s*', '', t).split(' | ')[0]
    return t.strip()
def block(text, marker):
    i = text.index(marker)
    j = text.index('```', i) + 3
    k = text.index('```', j)
    return text[j:k].strip('\n')
def page(name, sub, items, tag, dom=False):
    if dom:
        cols = ''
        for idx, (d, w, objs) in enumerate(DOMAINS):
            lis = ''.join(f'<li>{html.escape(o)}</li>' for o in objs)
            cols += f'<div class="dom"><div class="h" style="--c:{PAL[idx]}">{html.escape(d)}<small>{w} of the exam</small></div><ul>{lis}</ul></div>'
        body = f'<div class="doms">{cols}</div>'
        count = sum(len(o) for _, _, o in DOMAINS)
    else:
        chips = ''
        for i, t in enumerate(items):
            fin = ' fin' if i == len(items) - 1 else ''
            label = 'FINALE' if fin else f'{i+1:02d}'
            chips += f'<div class="chip{fin}" style="--c:{PAL[i % 5]}"><span class="n">{label}</span><span class="t">{html.escape(t)}</span></div>'
        body = f'<div class="grid">{chips}</div>'
        count = len(items)
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="pill">CURTAIN RAISER · ALL TOPICS</div>
<h1>{html.escape(name)}</h1>
<div class="sub">{html.escape(sub)}</div>
{body}
<div class="bar"><span>Sneak peek: all {count} topics</span><span>#{html.escape(tag)}</span></div>
</body></html>'''
os.makedirs(WORK, exist_ok=True)
def render(html_text, out_png, name):
    hp = f'{WORK}/{name}.html'; open(hp, 'w').write(html_text)
    subprocess.run([CHROME,'--headless','--disable-gpu','--hide-scrollbars','--window-size=1920,1080',f'--screenshot={out_png}',f'file://{hp}'],stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL,timeout=60)
def process(folder, name, topics, art, dom=False):
    path = f'{ROOT}/{folder}/{art}'
    text = open(path).read()
    title = clean_title(re.search(r'^# (.*)$', text, re.M).group(1))
    post = block(text, '**Post text (copy and paste):**')
    index = block(text, '**Series index') if '**Series index' in text else ''
    tag = post.strip().split()[-1].lstrip('#')
    if not dom:
        lines = post.split('\n')
        k = next((i for i, l in enumerate(lines) if l.startswith('Write-up 1 in my new series')), None)
        if k is not None:
            lines.insert(k + 1, f'Coming up: all {len(topics)} write-ups are on the cover.')
            lines.insert(k + 1, '')
            post = '\n'.join(lines)
    stem = art.replace('.md', '')
    cover_name = stem.replace('-curtain-raiser', '-curtain-raiser') 
    prefix = 'curtain-raiser'
    cover = f'images/{stem[:2]}-curtain-raiser-cover.png'
    html_text = page(name, title, topics, tag, dom)
    render(html_text, f'{ROOT}/{folder}/{cover}', f'{folder}-cover')
    body = f'''# Curtain raiser post: {name}

*Post with cover only. No article. The cover lists every topic in the series.*

![Cover](images/{stem[:2]}-curtain-raiser-cover.png)

**Post text (copy and paste):**

```
{post}
```
'''
    if index:
        body += f'''
**Series index (post as the first comment, then pin it):**

```
{index}
```
'''
    newpath = f'{ROOT}/{folder}/{stem[:2]}-curtain-raiser-post.md'
    open(newpath, 'w').write(body)
    print('ok', folder, len(topics))
if __name__ == '__main__':
    for folder, name, topics in SERIES:
        art = '01-curtain-raiser.md'
        process(folder, name, topics, art)
    process('22-claude-architect-exam', 'Claude Architect, one objective at a time', [], '00-curtain-raiser.md', dom=True)
