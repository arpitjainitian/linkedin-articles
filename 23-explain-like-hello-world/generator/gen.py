import sys, importlib.util, os, re
SP=sys.argv[1]; OUT=sys.argv[2]
arts=[]
for b in ['b1','b2','b3','b4']:
    spec=importlib.util.spec_from_file_location(b, f'{SP}/{b}.py'); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); arts+=m.A
arts.sort(key=lambda a:a['n'])
for a in arts:
    for k,v in list(a.items()):
        if isinstance(v,str): a[k]=v.replace('👍 or 👎','thumbs up or thumbs down')
FIN=dict(n=33, slug="finale-ai-dictionary", title="Your AI Dictionary, One Line per Word", topic="The finale")
allw=arts+[FIN]
PREV='''**Previous series:**

- **Series 1, #JustAddRAG:** [start here](https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/) or jump to [the grand finale](https://www.linkedin.com/pulse/15-so-should-you-really-just-add-rag-grand-finale-arpit-jain-ninmf/)
- **Series 2, Beyond Just RAG: From Answers to Actions:** [start here](https://www.linkedin.com/pulse/1-your-ai-can-answer-now-has-act-from-answers-actions-arpit-jain-po6lf/) or jump to [the finale](https://www.linkedin.com/pulse/8-so-should-your-ai-do-things-just-answer-finale-arpit-jain-x7cxf)'''
TAGS='#AI #GenAI #LearnAI #ExplainItLikeHelloWorld'
def short(t): return t[0].upper()+t[1:] if t else t
def lc(t):
    w=t.split()[0]
    return t if (w.isupper() or any(c.isdigit() for c in w)) else t[0].lower()+t[1:]
def earlier(n):
    L=['1. AI words everyone uses. Nobody explains. (the curtain raiser post) *(link added when published)*']
    for x in allw:
        if x['n']<n: L.append(f"{x['n']}. {x['title']} *(link added when published)*")
    return '\n'.join(L)
def index(a,nxt):
    prev=[x for x in allw if x['n']==a['n']-1]
    s='Explain It Like Hello World\n\nStart here: 1. AI words everyone uses. Nobody explains. [link]\n'
    if prev and prev[0]['n']>1: s+=f"Previous: {prev[0]['n']}. {prev[0]['title']} [link]\n"
    s+=f"You're here: {a['n']}. {a['title']}\n"
    if nxt: s+=f"Next: {nxt['n']}. {nxt['title']}\n"
    s+='\nFull list: in the curtain raiser post.'
    return s
for i,a in enumerate(allw):
    nxt=allw[i+1] if i+1<len(allw) else None
    nn=f"{a['n']:02d}"
    if a['n']==33:
        dic='\n'.join(f"- **{x['topic']}** ({x['n']}): {x['hook']}" for x in arts)
        body=f'''# {a['n']}. {a['title']} | The Finale

![Cover](images/{nn}-{a['slug']}-cover.png)

*Explain It Like Hello World series: the finale*

Remember the meeting from the curtain raiser? "We'll use a quantized mixture-of-experts model with a bigger context window."

Now you can explain every word in it. Quantized: the same photo saved as a smaller file. Mixture of experts: a hospital where you only see the specialists you need. Context window: the AI's desk.

That was the whole idea of this series: every AI word has a hello world, a tiny example that makes it click.

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
3. Send me the words this series missed. They might start the next one.

The words sound hard. The ideas never were.

Thank you for reading, commenting and sharing along the way.

Which word finally clicked for you?

**Earlier in this series:**

{earlier(33)}

{PREV}

---

**Post text (copy and paste):**

```
"We'll use a quantized mixture-of-experts model with a bigger context window."

At the start of this series, everyone nodded. Nobody asked.

Every AI word has a hello world: one tiny example that makes it click.

The finale: 31 AI words, one line each. Save it, share it with whoever nods along the most.

Which word finally clicked for you?

{TAGS}
```

**Series index (post as the first comment):**

```
{index(a,None)}
```
'''
    else:
        words='\n'.join(f"- **{w}:** {d}" for w,d in a['words'])
        take='\n'.join(f"{k+1}. {t}" for k,t in enumerate(a['take']))
        nxtline=f"Next write-up ({nxt['n']}): **{nxt['title']}**" + (" (the finale)" if nxt['n']==33 else "")
        body=f'''# {a['n']}. {a['title']} | {a['topic']}

![Cover](images/{nn}-{a['slug']}-cover.png)

*Explain It Like Hello World series: {a['topic']}*

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
    open(f"{OUT}/{nn}-{a['slug']}.md",'w').write(body)
    # course companion
    if a['n']==33:
        comp=f'''# Lesson 23.33: Your AI Dictionary (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain every AI term in this series with a one-line hello world, and apply the method to new terms.

## Review exercise

Cover the right-hand side of the dictionary in the finale and explain each term aloud in one sentence, with one everyday example.

## Capstone

Pick one AI term that isn't in the series. Write its hello world, one step further, where you've met it, and what it's not.

## Further reading

- The series plan: [README.md](README.md).
'''
    else:
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
    open(f"{OUT}/{nn}-{a['slug']}.course.md",'w').write(comp)
# README update
f=f'{OUT}/README.md'; s=open(f).read()
for a in allw:
    nn=f"{a['n']:02d}"
    s=re.sub(rf"^\| {a['n']} \| ([^|]*?) \|([^|]*)\| [^|]*\|$", lambda m: f"| {a['n']} | [{a['title']}]({nn}-{a['slug']}.md) ({a['topic']}) |{m.group(2)}| Draft for review |", s, flags=re.M)
open(f,'w').write(s)
print(len(allw))
