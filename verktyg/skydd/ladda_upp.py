#!/usr/bin/env python3
"""Laddar upp appkoden och filmerna/bilderna till Supabase-lagringen 'skyddat' (bara det som saknas).
Körs automatiskt av GitHub Actions vid varje publicering, så att varje ny appversion alltid finns i lagringen.
Kräver miljövariablerna SUPABASE_URL och SUPABASE_SERVICE_ROLE_KEY (läggs som hemligheter i GitHub).
Utan nyckel körs ett torrtest som bara visar vad som skulle laddas upp."""
import json, os, sys, urllib.request, urllib.error
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'app', 'assets')
URL = os.environ.get('SUPABASE_URL', 'https://fwgvfmkdmrpmgririxpt.supabase.co').rstrip('/')
KEY = os.environ.get('SUPABASE_SERVICE_ROLE_KEY', '')
BUCKET = 'skyddat'
L = json.load(open(os.path.join(ROOT, 'skydd-lista.json')))

def req(method, path, data=None, headers=None):
    h = {'Authorization': 'Bearer ' + KEY, 'apikey': KEY}; h.update(headers or {})
    r = urllib.request.Request(URL + path, data=data, method=method, headers=h)
    with urllib.request.urlopen(r, timeout=120) as resp: return resp.read()

def existing(prefix):
    names, off = set(), 0
    while True:
        body = json.dumps({'prefix': prefix, 'limit': 1000, 'offset': off}).encode()
        rows = json.loads(req('POST', f'/storage/v1/object/list/{BUCKET}', body, {'Content-Type': 'application/json'}))
        names |= {r['name'] for r in rows if r.get('name')}
        if len(rows) < 1000: return names
        off += 1000

def upload(path, file, ctype, cache):
    with open(file, 'rb') as fh: data = fh.read()
    req('POST', f'/storage/v1/object/{BUCKET}/{path}', data, {'Content-Type': ctype, 'x-upsert': 'true', 'cache-control': cache})

app_name = L['app']['v'] + '.js'
if not KEY:
    print(f"Torrtest (ingen nyckel): appversion {app_name}, {len(L['media'])} mediafiler i listan."); sys.exit(0)
have_app, have_media = existing('app/'), existing('media/')
todo = [m['n'] for m in L['media'] if m['n'] not in have_media]
print(f"I lagringen: {len(have_media)} mediafiler, appversion {'finns' if app_name in have_app else 'saknas'}. Att ladda upp: {len(todo)} mediafiler.")
for i, n in enumerate(todo, 1):
    upload('media/' + n, os.path.join(ROOT, n), 'video/mp4' if n.endswith('.mp4') else 'image/jpeg', 'max-age=31536000')
    if i % 50 == 0: print(f'  {i}/{len(todo)}')
if app_name not in have_app:
    upload('app/' + app_name, os.path.join(ROOT, L['app']['fil']), 'text/javascript', 'max-age=31536000')
    print('Appversionen uppladdad:', app_name)
print('Klart.')
