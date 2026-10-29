import sys, importlib.util, os, re, glob
SP=sys.argv[1]; OUT=sys.argv[2]
def load(name):
    spec=importlib.util.spec_from_file_location(name, f'{SP}/{name}.py'); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m.A
OLD={2:10,3:11,4:12,5:13,6:15,7:16,8:26,10:30,11:32,12:34,13:35,14:38,15:41,16:42,17:43,18:45,19:46,20:49,21:71,22:72,23:73,24:74,25:80,26:65,27:68,28:81,29:97,30:83,31:93,32:98}
TOPIC={3:"LLM",19:"GPU",21:"Reasoning model",22:"Multimodal AI",23:"Diffusion model",25:"Open-weight model",26:"A2A",28:"World model",31:"Watermarking"}
SLUG={3:"llm",19:"gpu",21:"reasoning-model",22:"multimodal-ai",23:"diffusion-model",25:"open-weight-model",28:"world-model",29:"benchmarks",31:"watermarking"}
def remap(t):
    return re.sub(r'write-up (\d+)', lambda m: f"write-up {OLD.get(int(m.group(1)), int(m.group(1)))}", t)
arts=[]
for b in ['b1','b2','b3','b4']:
    for a in load(b):
        o=a['n']
        if o in (9,10,20): continue
        a=dict(a); a['n']=OLD[o]
        if o in TOPIC: a['topic']=TOPIC[o]
        if o in SLUG: a['slug']=SLUG[o]
        for k,v in list(a.items()):
            if isinstance(v,str): a[k]=remap(v).replace('👍 or 👎','thumbs up or thumbs down')
            elif isinstance(v,list): a[k]=[remap(x) if isinstance(x,str) else (x[0],remap(x[1])) for x in v]
        arts.append(a)
for c in ['c1','c2','c3','c4','c5','c6','c7','c8','c9']: arts+=load(c)
arts.sort(key=lambda a:a['n'])
sys.path.insert(0,SP)
from titles import T as NEWT, KEY
for a in arts: a['title']=NEWT[a['n']]
miss=[a['n'] for a in arts if KEY[a['n']] not in (a['scene']+' '+a['hook']+' '+a['extra']).lower()]
print('post missing word:',miss)
from published import TIA, TIA_LATEST
EXTRA={61:" My Today in AI No. 001 asks what happens when your agent visits someone else's website.",
50:" My Today in AI No. 011 covers a text-to-speech model small enough for a phone.",
69:" My Today in AI No. 008 asks whether using AI makes you give up faster.",
91:" My Today in AI No. 006 asks how you prove why an AI made a decision."}
def tia(t): return re.sub(r'Today in AI No\. 0*(\d+)', lambda m: f"[Today in AI No. {int(m.group(1)):03d}]({TIA[int(m.group(1))]})" if int(m.group(1)) in TIA else m.group(0), t)
for a in arts:
    if a['n'] in EXTRA: a['met']+=EXTRA[a['n']]
    for k in ('hw','step','met','notit'): a[k]=tia(a[k])
ns=[a['n'] for a in arts]; assert ns==list(range(2,105)), [x for x in range(2,105) if x not in ns]
# Season 1 additions (c10.py): insert after their 'after' write-up, renumber, remap cross-references
P0=[(2,9),(10,16),(17,25),(26,40),(41,52),(53,60),(61,70),(71,82),(83,96),(97,104)]
pidx=lambda n:[i for i,(lo,hi) in enumerate(P0) if lo<=n<=hi][0]
for a in arts: a['key']=KEY[a['n']]; a['pi']=pidx(a['n']); a['ord']=(a['n'],0)
for j,a in enumerate(load('c10')):
    a=dict(a); a['ord']=(a['after'],1+j); a['pi']=pidx(a['after'])
    for k in ('hw','step','met','notit'): a[k]=tia(a[k])
    arts.append(a)
pre={a['slug']:a['n'] for a in arts if 'after' not in a}
for j,a in enumerate(load('c11')):
    a=dict(a); a['after']=pre[a.pop('after_slug')]; a['ord']=(a['after'],100+j); a['pi']=pidx(a['after'])
    for k in ('hw','step','met','notit'): a[k]=tia(a[k])
    arts.append(a)
arts.sort(key=lambda a:a['ord'])
REN={a['n']:i+2 for i,a in enumerate(arts) if 'after' not in a}
for i,a in enumerate(arts): a['n']=i+2
def ren(t): return re.sub(r'(write-ups? )(\d+)( and )?(\d+)?', lambda m: m.group(1)+str(REN.get(int(m.group(2)),int(m.group(2))))+((m.group(3)+str(REN.get(int(m.group(4)),int(m.group(4))))) if m.group(4) else (m.group(3) or '')), t)
for a in arts:
    for k,v in list(a.items()):
        if isinstance(v,str) and k not in ('slug','title','key'): a[k]=ren(v)
        elif isinstance(v,list): a[k]=[ren(x) if isinstance(x,str) else (x[0],ren(x[1])) for x in v]
miss=[a['n'] for a in arts if a['key'] not in (a['scene']+' '+a['hook']+' '+a['extra']).lower() or a['key'] not in a['title'].lower()]
print('missing key word (post or title):',miss)
NF=len(arts)+2
import json
PN=["The basics","How an AI reads and writes","Talking to an AI","How an AI is made","Smaller, faster, cheaper","Giving AI knowledge","AI that acts","New kinds of AI","Trust, safety and rules","Reading the headlines"]
json.dump([dict(n=a['n'],slug=a['slug'],title=a['title'],key=a['key'],topic=a['topic'],scene=a['scene'],hook=a['hook'],close=a['close'],part=PN[a['pi']].upper()) for a in arts],open(f'{SP}/final.json','w'),indent=0)
# fix old-text specifics
for a in arts:
    if a['n']==83: a['notit']=a['notit']; 
    if a['n']==11: a['notit']=a['notit'].replace('(more in write-up 83)','(more in write-up 83)')
FIN=dict(n=NF, slug="finale-ai-dictionary", title="Your AI Dictionary, One Line per Word", topic="The finale")
allw=arts+[FIN]
PARTS=[(min(a['n'] for a in arts if a['pi']==i),max(a['n'] for a in arts if a['pi']==i)+(1 if i==9 else 0),f"Part {i}: {nm}") for i,nm in enumerate(PN)]
from published import TIA, TIA_LATEST
PREV='''**Previous series:**

- **Series 1, #JustAddRAG:** [start here](https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/) or jump to [the grand finale](https://www.linkedin.com/pulse/15-so-should-you-really-just-add-rag-grand-finale-arpit-jain-ninmf/)
- **Series 2, Beyond Just RAG: From Answers to Actions:** [start here](https://www.linkedin.com/pulse/1-your-ai-can-answer-now-has-act-from-answers-actions-arpit-jain-po6lf/) or jump to [the finale](https://www.linkedin.com/pulse/8-so-should-your-ai-do-things-just-answer-finale-arpit-jain-x7cxf)
- **Series 20, Today in AI** (ongoing): [start here]('''+TIA[1]+''') or read [the latest issue]('''+TIA[TIA_LATEST]+''')'''
TAGS='#AI #GenAI #LearnAI #ExplainItLikeHelloWorld'
sys.path.insert(0,SP)
from published import PUB
def lc(t):
    w=t.split()[0]
    return t if (w.isupper() or any(c.isdigit() for c in w) or w in ('GraphRAG','LoRA','RAG','LLM')) else t[0].lower()+t[1:]
def publine(a):
    return f"\n**Published:** {PUB[a['n']][1]} on [LinkedIn]({PUB[a['n']][0]})\n" if a['n'] in PUB else ''
def fn(a): return f"{a['n']:03d}-{a['slug']}"
def earlier(n):
    L=['1. [AI words everyone uses. Nobody explains.](https://lnkd.in/p/d8abaPhq) (the curtain raiser post)']
    L+= [(f"{x['n']}. [{x['title']}]({PUB[x['n']][0]})" if x['n'] in PUB else f"{x['n']}. {x['title']} *(link added when published)*") for x in allw if x['n']<n]
    return '\n'.join(L)
def index(a,nxt):
    prev=[x for x in allw if x['n']==a['n']-1]
    s='Explain It Like Hello World\n\nStart here: AI words everyone uses. Nobody explains. https://lnkd.in/p/d8abaPhq\n'
    if prev: s+=f"Previous: {prev[0]['n']}. {prev[0]['title']} {PUB[prev[0]['n']][0] if prev[0]['n'] in PUB else '[link]'}\n"
    s+=f"You're here: {a['n']}. {a['title']}\n"
    if nxt: s+=f"Next: {nxt['n']}. {nxt['title']}\n"
    return s+'\nFull list: in the curtain raiser post.'
for f in glob.glob(f'{OUT}/[0-9]*.md'):
    if 'curtain-raiser' not in f: os.remove(f)
for i,a in enumerate(allw):
    nxt=allw[i+1] if i+1<len(allw) else None
    if a['n']==NF:
        dic=''
        for lo,hi,pn in PARTS:
            items=[x for x in arts if lo<=x['n']<=hi]
            if items: dic+=f"\n**{pn.split(': ')[1]}**\n\n"+'\n'.join(f"- **{x['topic']}** ({x['n']}): {x['hook']}" for x in items)+'\n'
        body=f'''# {a['n']}. {a['title']} | The Finale

![Cover](images/{fn(a)}-cover.png)

*Explain It Like Hello World series: the finale*

Remember the meeting from the curtain raiser? "We'll use a quantized mixture-of-experts model with a bigger context window."

Now you can explain every word in it. Quantized: the same photo saved as a smaller file. Mixture of experts: a hospital where you only see the specialists you need. Context window: the AI's desk.

That was the whole idea of this series: every AI word has a hello world, a tiny example that makes it click. Here are all {len(arts)}, one line each.

## Your AI dictionary
{dic}
## How to learn the next AI word

1. Find the smallest example that shows it working.
2. Add one step to get to the real thing.
3. Find it in a product you already use.
4. Only then learn the technical name.

## Take this to your next meeting

1. Save this list. Share it with whoever nods along the most.
2. When a new AI word appears, ask for its hello world.
3. Send me the words this series missed. They might start the next season.

The words sound hard. The ideas never were.

Thank you for reading, commenting and sharing along the way.

Which word finally clicked for you?

**Earlier in this series:**

{earlier(NF)}

{PREV}

---

**Post text (copy and paste):**

```
"We'll use a quantized mixture-of-experts model with a bigger context window."

At the start of this series, everyone nodded. Nobody asked.

Every AI word has a hello world: one tiny example that makes it click.

The finale: {len(arts)} AI words, one line each. Save it. Share it with whoever nods along the most.

Which word finally clicked for you?

{TAGS}
```

**Series index (post as the first comment):**

```
{index(a,None)}
```
'''
        comp=f'''# Lesson 23.{a['n']}: Your AI Dictionary (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain every AI term in this series with a one-line hello world, and apply the method to new terms.

## Review exercise

Cover the explanations in the finale's dictionary and explain each term aloud in one sentence, with one everyday example. Do one part per day.

## Capstone

Pick one AI term that isn't in the series. Write its hello world, one step further, where you've met it, and what it's not.

## Further reading

- The series plan: [README.md](README.md).
'''
    else:
        words='\n'.join(f"- **{w}:** {d}" for w,d in a['words'])
        take='\n'.join(f"{k+1}. {t}" for k,t in enumerate(a['take']))
        nxtline=f"Next write-up ({nxt['n']}): **{nxt['title']}**" + (" (the finale)" if nxt['n']==NF else "")
        body=f'''# {a['n']}. {a['title']} | {a['topic']}

![Cover](images/{fn(a)}-cover.png)

*Explain It Like Hello World series: {a['topic']}*
{publine(a)}
{a['buzz']}

## The hello world

{a['hw']}

## One step further

{a['step']}

## Where you've already met it

{a['met']}

## The real name

{a['name']}

{words}

## What it's not

{a['notit']}

## Take this to your next meeting

{take}

{a['close']}

{nxtline}

Follow me for the next one. {a['q']}

**Earlier in this series:**

{earlier(a['n'])}

{PREV}

---

**Post text (copy and paste):**

```
{a['scene']}

{a['hook']}

{a['extra']}

{a['q']}

{TAGS}
```

**Series index (post as the first comment):**

```
{index(a,nxt)}
```
'''
        gl='\n'.join(f"- **{w}:** {d}" for w,d in a['words'])
        hw1=a['hw'].split('\n\n')[0]
        comp=f'''# Lesson 23.{a['n']}: {a['topic']} (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain {lc(a['topic'])} with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

{hw1}

## One step further

{a['step']}

## Exercise

Explain {lc(a['topic'])} to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for {lc(a['topic'])}? *{a['hook']}*
2. What is it not? *{a['notit']}*
3. Name one place you've already met it. *{a['met']}*

## Glossary

{gl}

## Further reading

- The series plan: [README.md](README.md).
'''
    open(f"{OUT}/{fn(a)}.md",'w').write(body)
    open(f"{OUT}/{fn(a)}.course.md",'w').write(comp)
# README write-ups section
f=f'{OUT}/README.md'; s=open(f).read()
head=s[:s.index('## Write-ups')]
tbl='## Write-ups\n\nOne word per write-up. Season 1 covers the AI words in use so far; later seasons add new words as they appear.\n\n| # | Write-up | Hello-world angle | Status |\n|---|---|---|---|\n| 1 | Curtain raiser: [AI Words Everyone Uses. Nobody Explains.](01-curtain-raiser-post.md) (post with cover only, no article) | Hello world, but for AI ideas | [Published](https://lnkd.in/p/d8abaPhq) 27 October 2026 |\n'
for lo,hi,pn in PARTS:
    tbl+=f'| | **{pn}** | | |\n'
    for x in allw:
        if lo<=x['n']<=hi:
            ang=x.get('hook','Every word from the series, one line each')
            st=f"[Published]({PUB[x['n']][0]}) {PUB[x['n']][1]}" if x['n'] in PUB else 'Draft for review'
            tbl+=f"| {x['n']} | [{x['title']}]({fn(x)}.md) ({x['topic']}) | {ang} | {st} |\n"
s=head+tbl+'\n*Order can change with what\'s trending; Part 0 and Part 1 go first because they unlock the rest.*\n'
s=s.replace('- Topics already explained elsewhere are left out and linked instead: RAG (#JustAddRAG), MCP (Series 11), agents and agent loops (Series 2, 15), guardrails (Series 4), memory (Series 12), evals (Series 5), cost and caching (Series 8).',
 '- Words that other series cover in depth (RAG, MCP, agents, guardrails, memory, evals, gateways, cost) are explained here only at hello-world level, and each links to the series that covers what goes wrong in production.')
open(f,'w').write(s)
print(len(allw))
