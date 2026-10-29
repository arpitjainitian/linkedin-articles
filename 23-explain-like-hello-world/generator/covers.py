import sys, importlib.util, re, os, html, subprocess
SRC=os.path.dirname(os.path.abspath(__file__)); OUT=sys.argv[1]; WORK=sys.argv[2]
sys.path.insert(0,SRC)
import json
arts=json.load(open(f'{SRC}/final.json'))
COL=['#FFD93D','#6EC6FF','#5CE18A','#FF9F80','#C9A7FF']
def hl(title,key):
    t=html.escape(title); i=t.lower().find(key)
    if i<0: return t
    # extend to word end
    j=i+len(key)
    while j<len(t) and (t[j].isalnum() or t[j]=='-'): j+=1
    return t[:i]+'<em>'+t[i:j]+'</em>'+t[j:]
ONLY=set(map(int,sys.argv[3].split(','))) if len(sys.argv)>3 else None
for a in arts:
    if ONLY and a['n'] not in ONLY: continue
    n=a['n']; title=a['title']; part=a['part']; c=COL[n%5]
    hw=html.escape(a['scene']).replace('\n','<br>')
    page=f'''<!doctype html><html><head><meta charset="utf-8"><style>
*{{box-sizing:border-box;margin:0;padding:0}}html,body{{width:1920px;height:1080px;overflow:hidden}}
body{{font-family:-apple-system,"Helvetica Neue",Arial,sans-serif;background:#FFF8E7;color:#111;position:relative}}
.tag{{position:absolute;left:110px;top:62px;font-weight:900;letter-spacing:4px;font-size:22px;color:#FF3D7F}}
h1{{position:absolute;left:110px;top:104px;width:1700px;font-size:{68 if len(title)<55 else 58 if len(title)<75 else 50}px;line-height:1.08;font-weight:900;letter-spacing:-1px}}
h1 em{{font-style:normal;background:#FFD93D;padding:0 10px;border-radius:10px}}
.word{{position:absolute;left:110px;top:{330 if len(title)<55 else 360}px;width:760px;height:460px;background:{c};border:4px solid #111;border-radius:24px;box-shadow:12px 12px 0 #111;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:30px}}
.word small{{font-size:22px;font-weight:900;letter-spacing:4px}}
.word b{{font-size:{110 if len(a['topic'])<12 else 84 if len(a['topic'])<18 else 66}px;line-height:1.05;font-weight:900;margin-top:18px}}
.hw{{position:absolute;left:930px;top:{330 if len(title)<55 else 360}px;width:880px;height:460px;background:#111;color:#fff;border-radius:24px;box-shadow:12px 12px 0 #FF3D7F;padding:34px 40px}}
.hw h3{{font-family:Menlo,monospace;color:#5CE18A;font-size:26px}}
.hw .s{{font-size:31px;font-weight:700;line-height:1.35;margin-top:22px;color:#ddd}}
.hw .k{{font-size:34px;font-weight:900;line-height:1.3;margin-top:24px;color:#FFD93D}}
.foot{{position:absolute;left:110px;top:900px;width:1700px;background:#FF3D7F;color:#fff;border:3px solid #111;border-radius:18px;padding:20px 30px;font-size:29px;font-weight:900;box-shadow:8px 8px 0 #111;display:flex;justify-content:space-between}}
.foot span{{color:#111}}
</style></head><body>
<div class="tag">EXPLAIN IT LIKE HELLO WORLD · {n} · {part}</div>
<h1>{hl(title,a['key'])}</h1>
<div class="word"><small>TODAY'S WORD</small><b>{html.escape(a['topic'])}</b></div>
<div class="hw"><h3>&gt; hello, world</h3><div class="s">{hw}</div><div class="k">{html.escape(a['hook'])}</div></div>
<div class="foot"><span>{html.escape(a['close'])}</span>#ExplainItLikeHelloWorld</div>
</body></html>'''
    fn=f"{n:03d}-{a['slug']}"
    hp=f'{WORK}/{fn}.html'; open(hp,'w').write(page)
    subprocess.run(['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome','--headless','--disable-gpu','--hide-scrollbars','--window-size=1920,1080',f'--screenshot={OUT}/{fn}-cover.png',f'file://{hp}'],stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
print(len(arts))
