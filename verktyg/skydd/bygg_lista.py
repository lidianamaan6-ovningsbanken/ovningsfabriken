#!/usr/bin/env python3
"""Bygger app/assets/skydd-lista.json: vilka filer som ska ligga i Supabase-lagringen 'skyddat'.
Körs vid varje publicering. Utvecklarfliken använder listan för att ladda upp det som saknas."""
import json, os, re, sys
ROOT = os.path.join(os.path.dirname(__file__), '..', '..', 'app')
js_name = 'app-17bb85c3132c2bc2.js'
src = open(os.path.join(ROOT, 'assets', js_name), encoding='utf-8').read()
first, rest = src.split('\n', 1)
names = set(re.findall(r'data-skydd-(?:poster|src|href)="([^"\'+]+)"', src))
posters = json.loads(first[first.index('{'):first.rindex('}') + 1])
names |= {v.split('/', 1)[1].split('?')[0] for v in posters.values()}
html = open(os.path.join(ROOT, 'app.html'), encoding='utf-8').read()
ver = re.search(r'name="of-app" content="[^"?]+\?v=([^"]+)"', html)
# Filer som redan ligger i den låsta lagringen är borttagna från det öppna förrådet – då används storleken från förra listan
prev = {}
try: prev = {m['n']: m['s'] for m in json.load(open(os.path.join(ROOT, 'assets', 'skydd-lista.json')))['media']}
except Exception: pass
media = []
for n in sorted(names):
    f = os.path.join(ROOT, 'assets', n)
    if os.path.exists(f): media.append({'n': n, 's': os.path.getsize(f)})
    elif n in prev: media.append({'n': n, 's': prev[n]})
    else: sys.exit('Saknas på disk och i lagringslistan: ' + n)
out = {'app': {'fil': js_name, 'v': ver.group(1) if ver else '', 's': os.path.getsize(os.path.join(ROOT, 'assets', js_name))}, 'media': media}
json.dump(out, open(os.path.join(ROOT, 'assets', 'skydd-lista.json'), 'w'), separators=(',', ':'))
print('skydd-lista.json:', len(media), 'mediafiler,', round(sum(m['s'] for m in media) / 1e6), 'MB, app v=' + out['app']['v'])
