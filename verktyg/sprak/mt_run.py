import json, re, sys, os
from mt import load, tr
src, dst, model = sys.argv[1], sys.argv[2], sys.argv[3]   # src: json list or {key:text}; dst: cache json
lang = sys.argv[4] if len(sys.argv)>4 else 'sv'
items = json.load(open(src))
if isinstance(items, dict): items = list(items.values())
cache = json.load(open(dst)) if os.path.exists(dst) else {}
PRE_SV = [(r'\bpasset\b','träningspasset'),(r'\bPasset\b','Träningspasset'),(r'\bpassen\b','träningspassen'),(r'\bpassens\b','träningspassens'),(r'\bpass\b','träningspass'),(r'\bPass\b','Träningspass'),
  (r'\bsmålagsspel','spel med små lag'),(r'\bSmålagsspel','Spel med små lag'),(r'\bsmåmål\b','små mål'),(r'\bsmåmålen\b','de små målen'),(r'\bavslut\b','skott'),(r'\bAvslut\b','Skott'),(r'\bavsluten\b','skotten'),
  (r'\båtererövring','återvinning av bollen'),(r'\bÅtererövring','Återvinning av bollen'),(r'\bfasta situationer','fasta situationer'),(r'\bkoner\b','koner'),(r'\bkon\b','kon')]
POST_EN = [(r'\bworkouts\b','sessions'),(r'\bworkout\b','session'),(r'\bWorkout\b','Session'),(r'\b(\d+) (?:to|against|vs\.?|towards|on) (\d+)\b',r'\1 v \2'),(r'\bFixed situations\b','Set pieces'),(r'\bfixed situations\b','set pieces'),
  (r'\bcones?\b', lambda m: m.group(0)),(r'\bball holder\b','player on the ball'),(r'\bthe passport\b','the session'),(r'\bpassport\b','session')]
def split(t):
    parts = re.split(r'(\n+)', t); out=[]
    for p in parts:
        if p.startswith('\n') or not p.strip(): out.append(('k',p)); continue
        for i,s in enumerate(re.split(r'(?<=[.!?:;])\s+(?=[A-ZÅÄÖ0-9"„(–-])', p)):
            if i: out.append(('k',' '))
            out.append(('t',s))
    return out
todo=[t for t in items if t not in cache]
print('att översätta', len(todo), 'av', len(items), flush=True)
m = load(model, lang, os.path.basename(dst).replace('.json','')[-2:])
segs=set()
plan={}
for t in todo:
    sp=split(t); plan[t]=sp
    for k,s in sp:
        if k=='t': segs.add(s)
segs=sorted(segs); 
def pre(s):
    s = s.replace('Övningsfabriken', '4799').replace('Sam Nouman', '4798')   # namn ska aldrig översättas
    if lang!='sv': return s
    for a,b in PRE_SV: s=re.sub(a,b,s)
    return s
def post(s):
    s = s.replace('4799', 'Övningsfabriken').replace('4798', 'Sam Nouman')
    if not dst.endswith('_en.json'): return s
    for a,b in POST_EN: s=re.sub(a,b,s)
    return s
res={}
B=400
for i in range(0,len(segs),B):
    chunk=segs[i:i+B]
    outs=tr(m,[pre(x) for x in chunk])
    for a,b in zip(chunk,outs): res[a]=post(b)
    print(i+len(chunk),'/',len(segs),flush=True)
for t,sp in plan.items():
    cache[t]=''.join(res[s] if k=='t' else s for k,s in sp)
json.dump(cache,open(dst,'w'),ensure_ascii=False)
print('klart',len(cache))
