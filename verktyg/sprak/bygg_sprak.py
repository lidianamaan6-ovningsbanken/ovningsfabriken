#!/usr/bin/env python3
"""Bygger språkfilerna app/assets/sprak/<språk>.json och bank-<språk>.json.

Källor (verktyg/sprak/cache/):
  master.json          svenska texter: {'ui': [...], 'bank': [...]}
  sv-en.json           maskinöversättning svenska → engelska
  tpl-sv.json          mallar: '{} spelare' → '4711 spelare' (siffror som platshållare)
  tpl-sv-en.json       mallarna översatta till engelska
  en-<språk>.json      maskinöversättning engelska → övriga språk (via mt_run.py)
Handöversättningar: verktyg/sprak/<språk>_hand.tsv går alltid före maskinen.
Skriver också versionsnumren i app/assets/sprak.js.
"""
import json, os, re, hashlib, subprocess, sys
H = os.path.dirname(os.path.abspath(__file__)); C = H + '/cache'; R = os.path.normpath(H + '/../..')
OUT = R + '/app/assets/sprak'; os.makedirs(OUT, exist_ok=True)
J = lambda f: json.load(open(f, encoding='utf-8'))
M = J(C + '/master.json'); UI, BANK = set(M['ui']), set(M['bank'])
DYN = set(M.get('dyn', []))   # texter som bara sågs på skärmen (namn, datum, siffror) – översätts aldrig rakt av
NUMRE = re.compile(r'\d+(?:[.,:]\d+)*')
NAMN = re.compile(r'^[A-ZÅÄÖ0-9][\w&åäöÅÄÖ.\-]*(?: [A-ZÅÄÖ0-9][\w&åäöÅÄÖ.\-]*)+$')
REP = re.compile(r'\b(\w+)(?:\W+\1\b){2,}', re.I | re.U)
def ok_val(k, v):
    """Släng uppenbart trasiga maskinöversättningar (upprepade ord, svällande text)."""
    if not v or REP.search(v) and not REP.search(k): return False
    return len(v) <= 3 * len(k) + 20
def ok_key(k, hn):
    if k in DYN or len(k) <= 2: return False
    if NAMN.match(k): return False              # Järfälla FA, Sam Nouman …
    if NUMRE.sub('#', k.replace('\xa0', ' ')) in hn: return False
    return True
TOK = re.compile(r'47(1\d|2\d)')   # 4711, 4712 … = platshållare i mallarna

def hand(lang):
    f = f'{H}/{lang}_hand.tsv'; t, n, p = {}, {}, {}
    if not os.path.exists(f): return t, n, p
    for line in open(f, encoding='utf-8'):
        line = line.rstrip('\n')
        if not line or line.startswith('#') and '\t' not in line: continue
        if '\t' not in line: continue
        sv, tr = line.split('\t', 1)
        if sv.startswith('@'): t['@' + sv[1:]] = tr
        elif '{}' in sv: p[sv] = tr
        elif '#' in sv: n[sv] = tr
        else: t[sv] = tr
    return t, n, p

def kort(lang):
    """kort.tsv: de viktigaste orden (meny, knappar), handöversatta till alla språk."""
    rows = [l.rstrip('\n').split('\t') for l in open(H + '/kort.tsv', encoding='utf-8') if l.strip()]
    head = rows[0]
    if lang not in head: return {}
    i = head.index(lang)
    return {r[0]: r[i] for r in rows[1:] if len(r) > i and r[i]}

def tok2idx(s):
    """'Adapted for 4711 players' → 'Adapted for {1} players'"""
    return TOK.sub(lambda m: '{' + str(int(m.group(0)) - 4710) + '}', s)

def words(lang):
    js = ("const L=process.argv[1];const o={};const f=(l,opt,d)=>new Intl.DateTimeFormat(l,opt).format(d);"
          "for(let i=0;i<7;i++){const d=new Date(Date.UTC(2024,0,1+i,12));o[f('sv',{weekday:'long'},d)]=f(L,{weekday:'long'},d);o[f('sv',{weekday:'short'},d).replace('.','')]=f(L,{weekday:'short'},d).replace('.','');}"
          "for(let i=0;i<12;i++){const d=new Date(Date.UTC(2024,i,10,12));o[f('sv',{month:'long'},d)]=f(L,{month:'long'},d);o[f('sv',{month:'short'},d).replace('.','')]=f(L,{month:'short'},d).replace('.','');}"
          "o.tors=o.tors||f(L,{weekday:'short'},new Date(Date.UTC(2024,0,4,12))).replace('.','');console.log(JSON.stringify(o))")
    w = json.loads(subprocess.check_output(['node', '-e', js, lang]))
    week = {'en': 'week', 'ar': 'أسبوع', 'fa': 'هفته', 'fi': 'viikko', 'es': 'semana', 'de': 'Woche', 'fr': 'semaine', 'pl': 'tydzień', 'tr': 'hafta', 'uk': 'тиждень', 'ru': 'неделя', 'pt': 'semana', 'it': 'settimana'}
    w['vecka'] = week.get(lang, 'week'); w['v'] = w['vecka'][:1]
    return w

def english():
    mt = J(C + '/sv-en.json'); ht, hn, hp = hand('en')
    fix = lambda v: re.sub(r'(?i)\b(the )?(exercise|practice) factory\b', 'Övningsfabriken', v)
    d = {k: fix(v) for k, v in mt.items() if ok_key(k, hn) and ok_val(k, v)}; d.update(kort('en')); d.update(ht)
    sv_tok = J(C + '/tpl-sv.json'); tpl_en = J(C + '/tpl-sv-en.json')
    p = {}
    for k, tk in sv_tok.items():
        en = tpl_en.get(tk)
        if not en: continue
        need = set(TOK.findall(tk)); got = set(TOK.findall(en))
        if need != got: continue
        lit = re.sub(r'[^A-Za-zÅÄÖåäö]', '', k.replace('{}', ''))
        if len(lit) < 8: continue          # för allmänna mallar (”{} mot {}”) ger fel träffar
        p[k] = tok2idx(en)
    p.update(hp)
    return d, hn, p

EN_D, EN_N, EN_P = english()
EN_W = {k[1:]: v for k, v in EN_D.items() if k.startswith('@')}

def build(lang):
    if lang == 'en': d, n, p = EN_D, EN_N, EN_P
    else:
        mt = J(f'{C}/en-{lang}.json'); ht, hn, hp = hand(lang)
        d = {sv: mt[en] for sv, en in EN_D.items() if en in mt and ok_val(en, mt[en])}; d.update(kort(lang)); d.update(ht)
        n = {}
        for sv, en in EN_N.items():
            i = [0]
            def r(m): i[0] += 1; return str(4710 + i[0])
            tk = re.sub('#', r, en); x = mt.get(tk)
            if x and set(TOK.findall(x)) == set(TOK.findall(tk)): n[sv] = tok2idx(x)
        n.update(hn)
        p = {}
        for sv, en in EN_P.items():
            tk = re.sub(r'\{(\d)\}', lambda m: str(4710 + int(m.group(1))), en); x = mt.get(tk)
            if x and set(TOK.findall(x)) == set(TOK.findall(tk)): p[sv] = tok2idx(x)
        p.update(hp)
    extra = {k[1:]: v for k, v in d.items() if k.startswith('@')}
    d = {k: v for k, v in d.items() if not k.startswith('@')}
    if lang != 'en':
        extra = {k: mt.get(v, v) if v not in ('v',) else v for k, v in EN_W.items()}
    ui = {k: v for k, v in d.items() if k not in BANK and v and v != k}
    bank = {k: v for k, v in d.items() if k in BANK and v and v != k}
    files = {}
    for name, obj in [(lang, {'t': ui, 'n': n, 'p': sorted(p.items()), 'w': {**words(lang), **extra}}), ('bank-' + lang, {'t': bank})]:
        s = json.dumps(obj, ensure_ascii=False, separators=(',', ':'))
        open(f'{OUT}/{name}.json', 'w', encoding='utf-8').write(s)
        files[name] = hashlib.sha1(s.encode()).hexdigest()[:8]
    print(f'{lang}: {len(ui)} texter, {len(bank)} övningstexter, {len(n)} siffermallar, {len(p)} mallar')
    return files

def source_for_others():
    """Engelska texter som ska maskinöversättas vidare (med platshållare för siffror och mallar)."""
    out = set(v for v in EN_D.values() if v)  # @ord ingår också
    for en in EN_N.values():
        i = [0]
        def r(m): i[0] += 1; return str(4710 + i[0])
        out.add(re.sub('#', r, en))
    for en in EN_P.values(): out.add(re.sub(r'\{(\d)\}', lambda m: str(4710 + int(m.group(1))), en))
    return sorted(out)

if __name__ == '__main__':
    if sys.argv[1:2] == ['--kalla']:
        json.dump(source_for_others(), open(C + '/en-kalla.json', 'w', encoding='utf-8'), ensure_ascii=False); print('en-kalla.json skriven'); sys.exit()
    langs = ['en'] + sorted(f[3:-5] for f in os.listdir(C) if re.match(r'en-[a-z]{2}\.json$', f))
    V = {}
    for l in langs:
        f = build(l); V[l] = f[l]; V['bank-' + l] = f['bank-' + l]
    js = R + '/app/assets/sprak.js'; s = open(js, encoding='utf-8').read()
    s = re.sub(r'const V = \{[^}]*\};', 'const V = ' + json.dumps(V, separators=(',', ':')) + ';', s, count=1)
    open(js, 'w', encoding='utf-8').write(s)
    print('Versioner skrivna i sprak.js:', ', '.join(langs))
    v = hashlib.sha1(s.encode()).hexdigest()[:8]
    for f in ['app/app.html', 'index.html', 'integritet.html', 'om-sam.html']:
        p = R + '/' + f; h = open(p, encoding='utf-8').read()
        open(p, 'w', encoding='utf-8').write(re.sub(r'sprak\.js\?v=[0-9a-z]+"', 'sprak.js?v=' + v + '"', h))
    print('sprak.js?v=' + v)
