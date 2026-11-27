"""Bygger cache/master.json: alla svenska texter som ska översättas.

Indata (skapas av extract.js och en genomkörning av appen):
  strings.json  texter ur källkoden  [[text, fil], ...]
  crawl.json    texter som syntes på skärmen  [[text, vy], ...]
Utdata: {'ui': [...], 'bank': [...], 'dyn': [...]}
  ui   – appens och webbplatsens texter
  bank – övningsbankens texter (läses in separat i appen)
  dyn  – texter som bara syntes på skärmen (namn, datum, siffror). De översätts aldrig rakt av,
         eftersom de kan vara namn på personer eller klubbar.
Kör:  python3 master.py <mapp med strings.json och crawl.json>
"""
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.normpath(H + '/../..')
S = sys.argv[1] if len(sys.argv) > 1 else '.'
st = set(t for t, _ in json.load(open(os.path.join(S, 'strings.json'))))
cr = set(t for t, _ in json.load(open(os.path.join(S, 'crawl.json'))))
bank = set()
for e in json.load(open(R + '/verktyg/film/data/bank.json')):
    for k in ['name', 'orig', 'org', 'rules', 'phase', 'stage', 'type']:
        if e.get(k): bank.add(e[k].strip())
    for p in e.get('points', []): bank.add(p.strip())
m = {'ui': sorted((st | cr) - bank), 'bank': sorted(bank), 'dyn': sorted(cr - st - bank)}
json.dump(m, open(H + '/cache/master.json', 'w'), ensure_ascii=False)
print(len(m['ui']), 'ui', len(m['bank']), 'bank', len(m['dyn']), 'dyn')
