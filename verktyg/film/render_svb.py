# Egna animationsexempel för SvFF-övningarna i banken (svb*).
# Vi har bara namn, typ, fas, spelare och yta – inte originalets anvisningar.
# Därför byggs varje film från en mall per övningstyp och fas, med antal spelare,
# målvakter, mål och ytans form tagna ur övningens organisation.
# Användning: OF_FILM_OUTPUT=<ut> OF_LOGO_PNG=logo.png python3 render_svb.py <id> ...   (eller 'ALLA', 'BATCH:n:k')
import importlib.util, sys, os, json, re, random, unicodedata
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e9', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'render_extern9.py'))
e9 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e9); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e9.finish, e9.rec, e9.chain, e9.wander, e9.counter, e9.arrivals
lab, hide, show, team, boxes, drive, shoot = e9.lab, e9.hide, e9.show, e9.team, e9.boxes, e9.drive, e9.shoot
stand, countdown, countup, win = e9.stand, e9.countdown, e9.countup, e9.win
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; T_COL = '#1b211e'
HERE = os.path.dirname(os.path.abspath(__file__))

# ---------- text ----------
NUM = {'en': 1, 'ett': 1, 'två': 2, 'tre': 3, 'fyra': 4, 'fem': 5, 'sex': 6, 'sju': 7, 'åtta': 8, 'nio': 9, 'tio': 10, 'elva': 11, 'tolv': 12}
def num(w):
    w = w.lower(); return int(w) if w.isdigit() else NUM.get(w)

def fit(text, size, maxw, bold=True):
    f = F(size, bold); text = ' '.join(text.split())
    if f.getlength(text) <= maxw: return text
    while text and f.getlength(text + ' …') > maxw: text = text[:-1]
    return text.rstrip(' ,-–:(') + ' …'

def slugify(s):
    s = unicodedata.normalize('NFKD', s.lower()).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')

PREFIX = [r'^FS\s*-\s*', r'^Futsal\s*[-·]\s*', r'^MV\s*[A-C]?,?\s*', r'^Målvakt\s*[A-C]\s*-\s*', r'^Ö\d+,?\s*-?\s*', r'^TU\s*BU\s*[Pp]raktik\s*\d+:?\s*-?\s*',
          r'^TUBU\s*[Pp]raktik\s*\d+\s*-\s*', r'^Lek\s*-\s*']
def titles(name):
    n = name.strip()
    for _ in range(3):
        for p in PREFIX: n = re.sub(p, '', n).strip(' ,-–')
    n = n or name
    parts = [x.strip() for x in re.split(r'\s+[-–]\s+|:\s+', n) if x.strip()]
    if len(parts) >= 2: t1, t2 = parts[0], ' – '.join(parts[1:])
    else:
        w = n.split(); t1, t2 = (n, '') if F(44, True).getlength(n) < 900 else (' '.join(w[:len(w) // 2]), ' '.join(w[len(w) // 2:]))
    t1 = t1[0].upper() + t1[1:]; t2 = (t2[0].upper() + t2[1:]) if t2 else ''
    return [fit(t1, 44, 1000), fit(t2, 35, 1000)] if t2 else [fit(t1, 44, 1000)]

def setup_line(e):
    o = e.get('orig') or ''
    if 'Se organisationen' in o or not o: o = f"{e['type']} · {e['min']}–{e['max']} spelare"
    return fit(o.rstrip('.'), 18, 960)

def ph(t, h, s=''): return (t, fit(h, 26, 950), fit(s, 21, 950))

# ---------- organisation ----------
def parse(e):
    o = (e.get('orig') or '') + ' '; nm = e['name']
    W = r'(\d+|en|ett|två|tre|fyra|fem|sex|sju|åtta|nio|tio|elva|tolv)'
    gk = 0
    m = re.search(W + r'\s+målvakt', o, re.I)
    if m: gk = num(m.group(1)) or 1
    elif re.search(r'målvakt', o, re.I): gk = 1
    out = None
    m = re.search(W + r'\s+utespelare', o, re.I) or re.search(r'(\d+)(?:\s*[-–]\s*\d+)?\s+(?:spelare|barn)', o, re.I) or re.search(W + r'\s+(?:spelare|barn)', o, re.I)
    if m: out = num(m.group(1))
    m2 = re.search(r'(\d+)\s*(?:mot|v|vs)\s*(\d+)', nm, re.I)
    if m2 and not out: out = int(m2.group(1)) + int(m2.group(2))
    if not out: out = max(e.get('min') or 4, min(e.get('max') or 10, 10))
    m = re.search(r'(\d+)\s*(?:[-–]\s*\d+\s*)?[x×]\s*(\d+)', o)
    size = (int(m.group(1)), int(m.group(2))) if m else None
    goals = 0
    if re.search(r'(2|två)\s+(?:stora\s+)?mål\b', o, re.I): goals = 2
    elif re.search(r'(1|ett|med)\s+mål\b|\bmål\b', o, re.I): goals = 1
    small = bool(re.search(r'småmål|konmål|minimål|små mål', o + nm, re.I))
    if gk >= 2 and goals == 0: goals = 2
    if gk == 1 and goals == 0: goals = 1
    return dict(gk=gk, out=out, size=size, goals=goals, small=small)

def area(p):
    """Ytans ruta i filmens koordinater (0–100), längre sidan lodrätt."""
    if p['size']:
        a, b = sorted(p['size']); r = max(0.45, min(1.0, a / b))
    else: r = 0.75
    w = 84 * r; return (50 - w / 2, 6, 50 + w / 2, 94)

def has(e, *words):
    s = (e['name'] + ' ' + (e.get('orig') or '')).lower(); return any(w in s for w in words)

def keeperish(e):
    n = e['name'].lower() + ' ' + ' '.join(e.get('points') or []).lower()
    return e['name'].startswith('MV') or any(w in n for w in ('målvakt', 'rädda', 'palming', 'blockteknik', 'grundposition', 'utkast', 'utspark', 'fånga', 'kasta sig'))

# ---------- mallar ----------
def formation(n, x1, y1, x2, y2, rnd):
    """n spelare utspridda i en halva (rader framifrån)."""
    rows = [n] if n <= 3 else ([n - n // 2, n // 2] if n <= 6 else [3, n - 6, 3] if n <= 9 else [4, n - 7, 3])
    pts = []; ys = [y1 + (y2 - y1) * (i + 0.5) / len(rows) for i in range(len(rows))]
    for y, k in zip(ys, rows):
        for j in range(k): pts.append((x1 + (x2 - x1) * (j + 0.5) / k + rnd.uniform(-1.5, 1.5), y + rnd.uniform(-1.5, 1.5)))
    return pts

def nearest(d, ids, pid, t):
    px, py = at(d.pl[pid]['tr'], t)
    return min(ids, key=lambda i: (at(d.pl[i]['tr'], t)[0] - px) ** 2 + (at(d.pl[i]['tr'], t)[1] - py) ** 2)

def spread(d, ids, gap=4.0):
    """Flytta isär spelare (utan boll) som skulle stå ovanpå någon annan."""
    allp = list(d.pl)
    for i in ids:
        tr = d.pl[i]['tr']
        for k, (t, (x, y)) in enumerate(tr):
            for j in allp:
                if j == i: continue
                ox, oy = at(d.pl[j]['tr'], t)
                if ((ox - x) ** 2 + (oy - y) ** 2) ** .5 < gap:
                    x += gap if x < 50 else -gap
            tr[k] = (t, (x, y))

def game(e, p, rnd):
    """Smålagsspel och spelövningar: blått anfaller uppåt."""
    x1, y1, x2, y2 = area(p); d = Drill(); st = e['stage']
    per = max(2, min(6, p['out'] // 2)); extra = p['out'] - 2 * per if p['out'] - 2 * per in (1, 2) and p['out'] <= 14 else 0
    gk = p['gk'] > 0 and not p['small']; goals = p['goals'] or 2
    if gk: d.p('mvr', 'MV', R, (50, y1 + 2))
    if gk and goals >= 2: d.p('mvb', 'MV', B, (50, y2 - 2))
    BP = formation(per, x1 + 6, (y1 + y2) / 2 + 2, x2 - 6, y2 - 8, rnd); RP = formation(per, x1 + 6, y1 + 8, x2 - 6, (y1 + y2) / 2 - 2, rnd)
    BP.sort(key=lambda q: -q[1]); RP.sort(key=lambda q: q[1])
    team(d, 'b', B, BP); team(d, 'r', R, RP)
    if extra: team(d, 'j', YEL, [(x2 + 3, 50), (x1 - 3, 50)][:extra], ['J'] * extra)
    gx = 50; top = (gx + rnd.choice([-4, 4]), y1 - 1 if gk or goals else y1 + 1)
    shapes = [('box', x1, y1, x2, y2)]
    if p['small'] or not gk:
        shapes += [('smallgoal', 50, y1)] + ([('smallgoal', 50, y2)] if goals >= 2 else [])
    for k in range(per): wander(d, f'r{k}', 0, 3.0, boxes([RP[k]], 3)[0], rnd.randint(0, 99999), 1.5)
    ex = []
    start = 'mvb' if gk and goals >= 2 and st in ('Speluppbyggnad', 'Förhindra speluppbyggnad') else 'b0'
    b = d.newball(rec(d, start, 0))
    order = [f'b{k}' for k in range(per)]
    if st in ('Förhindra speluppbyggnad', 'Återerövring', 'Förhindra och rädda avslut'):
        # blått bygger, rött pressar och vinner bollen (återerövring: blått tappar och vinner tillbaka)
        seq = order[1:3] if per >= 3 else order[1:]
        t = chain(d, b, 0.4, seq, 0.3); h = seq[-1]
        if st == 'Återerövring':
            tl = win(d, b, 'r0', h, t + 0.6, 1.3); t = d.pas(b, tl + 0.3, rec(d, 'r1', tl + 1.0))
            th = nearest(d, [f'b{k}' for k in range(per)], 'r1', t + 0.6); tw = win(d, b, th, 'r1', t + 0.6, 1.2); t = drive(d, b, th, tw, (rnd.uniform(40, 60), y1 + 14), 20); tg = shoot(d, b, t, top); hide(d, b, tg + 0.3)
            fp = [ph(0, 'Spel med två lag', setup_line(e)), ph(tl - 0.2, 'Bollförlust – pressa direkt', 'Närmaste spelare pressar, övriga stänger.'),
                  ph(tw - 0.2, 'Återerövring!', e['points'][0] if e['points'] else ''), ph(tw + 0.4, 'Anfall direkt efter bollvinst', ' · '.join(e['points'][1:3]))]
            ex = countup(tl + 0.1, 3, (x2 - 4, (y1 + y2) / 2), (tw - tl) / 3) + [lab(tw, tw + 1.6, (60, (y1 + y2) / 2), 'VUNNEN!')]
        else:
            d.mv('r0', t - 1.2, t + 0.2, rec(d, h, t + 0.2)); d.mv('r1', t - 1.0, t + 0.4, (d.pos(h)[0] + 6, d.pos(h)[1] - 6))
            tw = win(d, b, 'r0', h, t + 0.6, 1.1); t = d.pas(b, tw + 0.3, rec(d, 'r1', tw + 1.0)); t = drive(d, b, 'r1', t, (rnd.uniform(42, 58), y2 - 12), 20)
            gb = (50, y2 + 1) if goals >= 2 or gk else (50, y2 - 1); tg = shoot(d, b, t, gb); hide(d, b, tg + 0.3)
            fp = [ph(0, 'Spel med två lag', setup_line(e)), ph(1.0, 'Försvaret: styr och stäng', e['points'][0] if e['points'] else ''),
                  ph(tw - 0.2, 'Bollvinst!', ' · '.join(e['points'][1:3])), ph(tg - 0.6, 'Snabbt anfall efter bollvinst', '')]
            ex = [lab(tw, tw + 1.6, (62, (y1 + y2) / 2), 'BOLLVINST')]
    elif st == 'Kontring':
        t = chain(d, b, 0.4, order[1:3] if per >= 3 else order[1:], 0.3)
        tw = win(d, b, 'r0', order[2] if per >= 3 else order[1], t + 0.6, 1.3)
        for k in range(1, min(per, 3)): d.mv(f'r{k}', tw - 0.4, tw + 2.0, (rnd.uniform(x1 + 8, x2 - 8), (y1 + y2) / 2 + 8 + 4 * k))
        t = d.pas(b, tw + 0.6, rec(d, 'r1', tw + 2.0), 1.2); t = drive(d, b, 'r1', t, (rnd.uniform(42, 58), y2 - 10), 24)
        tg = shoot(d, b, t, (50, y2 + 1)); hide(d, b, tg + 0.3)
        fp = [ph(0, 'Spel med två lag', setup_line(e)), ph(tw - 0.2, 'Bollvinst – kontra direkt!', e['points'][0] if e['points'] else ''),
              ph(tw + 1.0, 'Djupled och fart framåt', ' · '.join(e['points'][1:3])), ph(tg - 0.4, 'Avslut innan försvaret är på plats', '')]
        ex = countdown(tw, 5, (x2 - 4, (y1 + y2) / 2), (tg - tw) / 5) + [lab(tg, tg + 1.6, (50, y2 - 8), 'MÅL!')]
    else:
        seq = [s_ for s_ in order if s_ != start]; rnd.shuffle(seq); seq = seq[:min(4, per)]
        if extra: seq.insert(2, 'j0')
        for k in range(per): d.mv(f'b{k}', 0.4, 2.4 + 0.3 * k, (BP[k][0] + rnd.uniform(-3, 3), BP[k][1] - 6 - rnd.uniform(0, 5)))
        t = chain(d, b, 0.4, seq, 0.3); cnt = arrivals(d, b)
        h = seq[-1]; t = drive(d, b, h, t, (rnd.uniform(42, 58), y1 + 14), 20)
        if gk or goals: tg = shoot(d, b, t, top); hide(d, b, tg + 0.3); lb = 'MÅL!'
        else: tg = d.pas(b, t, (50, y1 + 1)); lb = '+1'
        for k in range(per): d.mv(f'r{k}', 3.0, tg, (RP[k][0] + rnd.uniform(-3, 3), RP[k][1] + 4))
        spread(d, [f'r{k}' for k in range(per)])
        head = {'Speluppbyggnad': 'Bygg spelet bakifrån', 'Komma till avslut och göra mål': 'Skapa lägen och avsluta'}.get(st, 'Spela tillsammans framåt')
        fp = [ph(0, 'Spel med två lag', setup_line(e)), ph(1.2, head, e['points'][0] if e['points'] else ''),
              ph(max(2.5, t - 3), ' · '.join(e['points'][1:2]) or 'Spelbarhet och rörelse', ' · '.join(e['points'][2:4])), ph(tg - 0.4, 'Avslut', '')]
        ex = [lab(tg, tg + 1.6, (50, y1 + 10), lb)]
    return d, fp, shapes, ex, 'SMÅLAGSSPEL'

def keeper(e, p, rnd):
    """Målvaktsövning: skyttar avslutar, målvakten räddar."""
    d = Drill(); d.p('mv', 'MV', YEL, (50, 6)); n = max(2, min(4, p['out'] if p['out'] < 8 else 3))
    SP = [(30 + 40 * k / max(1, n - 1), 40 + rnd.uniform(-3, 3)) for k in range(n)]
    team(d, 's', B, SP, ['', '', '', ''][:n]); t = 0.6; ex = []; tw = None
    sides = [38, 62, 44] if rnd.random() < 0.5 else [62, 38, 56]
    for k in range(min(n, 3)):
        bb = d.newball(rec(d, f's{k}', 0)); gx = sides[k]; save = k != 1
        tg = d.pas(bb, t + 0.3, (gx, 6.5) if save else (gx + (6 if gx > 50 else -6), 1.0), 0.6)
        d.mv('mv', t, tg, (gx - 1.8, 7.7) if save else (50 + (gx - 50) * 0.5, 6))
        if save: d.carry(bb, 'mv', tg, tg + 0.5); hide(d, bb, tg + 0.6); ex.append(lab(tg, tg + 1.2, (gx, 16), 'RÄDDNING'))
        else: hide(d, bb, tg + 0.3); ex.append(lab(tg, tg + 1.2, (gx, 16), 'MÅL'))
        t = tg + 1.0; tw = tw or tg
    pts = e['points'] or ['Grundposition', 'Förflyttning']
    fp = [ph(0, 'Målvaktsträning', setup_line(e)), ph(0.6, pts[0], 'Grundposition innan skottet.'),
          ph(tw + 0.6, pts[1] if len(pts) > 1 else 'Förflyttning i sidled', 'Snabb förflyttning mellan skotten.'), ph(t - 1.4, pts[2] if len(pts) > 2 else 'Nästa skott', 'Låt alla skyttar ta sin tur.')]
    return d, fp, [('box', 20, 4, 80, 60)], ex, 'MÅLVAKT'

def duel(e, p, rnd):
    if keeperish(e): return keeper(e, p, rnd)
    d = Drill(); two = has(e, '2 mot 2', '2v2', 'två mot två', '2 mot 1', '3 mot 2') ; x1, y1, x2, y2 = area(p)
    x1, x2 = max(x1, 20), min(x2, 80)
    gk = p['gk'] > 0 or p['goals'] > 0
    if gk: d.p('mv', 'MV', R, (50, y1 + 2))
    A = [(44, y2 - 10), (60, y2 - 6)] if two else [(50, y2 - 10)]; D = [(46, 50), (58, 44)] if two else [(50, 46)]
    team(d, 'a', B, A); team(d, 'f', R, D)
    for k in range(2): d.p(f'q{k}', '', B, (x1 - 4, y2 - 6 - 6 * k)); d.p(f'w{k}', '', R, (x2 + 4, y1 + 16 + 6 * k))
    b = d.newball(rec(d, 'a0', 0))
    t = drive(d, b, 'a0', 0.4, (50, 64), 12); d.mv('f0', 0.6, t, (48, 54))
    if two:
        d.mv('a1', 0.6, t + 0.6, (64, 46)); d.mv('f1', t - 0.4, t + 0.6, (60, 44))
        t = d.pas(b, t + 0.2, rec(d, 'a1', t + 0.9)); h = 'a1'
    else:
        t = drive(d, b, 'a0', t, (40, 58), 12); d.mv('f0', t - 0.8, t + 0.2, (42, 52)); h = 'a0'
    t = drive(d, b, h, t, (rnd.uniform(56, 64) if h == 'a1' else 34, 36), 14); d.mv('f0', t - 1.0, t, (d.pos(h)[0] - 4, 40))
    tg = shoot(d, b, t, (rnd.choice([44, 56]), y1 - 1) if gk else (50, y1 + 1)); hide(d, b, tg + 0.3)
    shapes = [('box', x1, y1, x2, y2)] + ([] if gk else [('cone', 44, y1), ('cone', 56, y1)])
    # andra försöket: försvararen vinner
    b2 = d.newball((200, 200)); show(d, b2, tg + 0.6, rec(d, 'q0', tg + 0.6))
    d.mv('a0', tg + 0.2, tg + 1.6, (x1 - 4, y2 - 18)); d.mv('f0', tg + 0.2, tg + 1.6, (50, 50))
    d.mv('q0', tg + 0.6, tg + 1.6, (50, y2 - 10)); d.carry(b2, 'q0', tg + 0.6, tg + 1.6)
    t = drive(d, b2, 'q0', tg + 1.7, (52, 62), 12); tw = win(d, b2, 'f0', 'q0', t + 0.5, 0.6)
    d.mv('f0', tw, tw + 1.2, (50, y2 - 4)); d.carry(b2, 'f0', tw, tw + 1.2)
    pts = e['points'] or ['Våga utmana', 'Försvara']
    fp = [ph(0, 'Duellspel', setup_line(e)), ph(0.6, pts[0], 'Anfallaren utmanar.'), ph(tg - 0.4, 'Avslut', pts[1] if len(pts) > 1 else ''),
          ph(tw - 0.2, 'Nästa försök – försvararen vinner bollen', pts[2] if len(pts) > 2 else 'Byt roller efter varje försök.')]
    return d, fp, shapes, [lab(tg, tg + 1.4, (50, y1 + 10), 'MÅL!'), lab(tw, tw + 1.4, (64, 60), 'BOLLVINST')], 'DUELL'

def passing(e, p, rnd):
    d = Drill(); n = p['out']
    if has(e, 'rondo', 'hålla bollen', 'behålla', 'possession', 'knock out', 'spelbarhet') or n >= 7:
        k = max(4, min(6, n - 2 if n >= 6 else n)); inn = 1 if k <= 4 else 2
        OU = [ring_pos(50, 50, 32, i, k) for i in range(k)]; team(d, 'b', B, OU); team(d, 'f', R, [(46, 48), (56, 54)][:inn], [''] * inn)
        b = d.newball(rec(d, 'b0', 0)); t = 0.4; cnt = []; cur = 0
        for _ in range(9):
            nk = (cur + rnd.choice([1, 2, k - 1, k - 2])) % k
            if nk == cur: nk = (cur + 1) % k
            tx, ty = OU[nk]
            if _ % 2 == 0: d.mv('f0', t, t + 1.4, ((tx + 50) / 2 + rnd.uniform(-3, 3), (ty + 50) / 2))
            if inn > 1: d.mv('f1', t, t + 0.7, ((OU[cur][0] + 50) / 2, (OU[cur][1] + 50) / 2))
            t = d.pas(b, t + 0.15, rec(d, f'b{nk}', t + 0.85)); cnt.append(t); cur = nk
        pts = e['points'] or ['Spelbarhet', 'Rörelse']
        fp = [ph(0, f'{k} mot {inn} – håll bollen', setup_line(e)), ph(1.0, pts[0], 'Rör dig så att du blir spelbar.'),
              ph(cnt[3], pts[1] if len(pts) > 1 else 'Passa bort från försvararen', ''), ph(cnt[6], pts[2] if len(pts) > 2 else 'Räkna passningarna', 'Byt försvarare vid bollvinst.')]
        return d, fp, [('box', 12, 12, 88, 88)], counter(cnt, pos=(90, 92), last=None), 'PASSNING'
    if n <= 4 or has(e, 'ta emot', 'mottagning', 'par'):
        PR = [(34, 26, 34, 74), (66, 26, 66, 74)]; cnt = []
        for k, (ax, ay, cx, cy) in enumerate(PR): d.p(f'a{k}', '', B, (ax, ay)); d.p(f'c{k}', '', B if k == 0 else R, (cx, cy))
        for k, (ax, ay, cx, cy) in enumerate(PR):
            b = d.newball(rec(d, f'a{k}', 0)); t = 0.4 + 0.3 * k; side = 1
            for rep in range(6):
                rcv, ry = (f'c{k}', cy) if rep % 2 == 0 else (f'a{k}', ay)
                t = d.pas(b, t + 0.2, rec(d, rcv, t + 1.0)); cnt.append(t) if k == 0 else None
                d.mv(rcv, t, t + 0.4, (ax + 4 * side, ry)); d.carry(b, rcv, t, t + 0.4); side = -side; t += 0.4
        pts = e['points'] or ['Mottagning', 'Passning']
        fp = [ph(0, 'Passningar i par', setup_line(e)), ph(1.2, pts[0], 'Ta emot åt sidan – bort från konen.'),
              ph(4.0, pts[1] if len(pts) > 1 else 'Passa tillbaka', 'Insida och lagom kraft.'), ph(8.0, pts[2] if len(pts) > 2 else 'Räkna lyckade passningar', '')]
        return d, fp, [('cone', 34, 50), ('cone', 66, 50)], counter(cnt, pos=(14, 50), last=None), 'PASSNING'
    # passningsruta – följ din passning
    Z = [(26, 74), (74, 74), (74, 26), (26, 26)]; BACK = [(20, 80), (80, 80), (80, 20), (20, 20)]
    for k, ps in enumerate(Z): d.p(f'a{k}', '', B, ps)
    d.p('a4', '', B, BACK[0]); at_c = {0: ['a0', 'a4'], 1: ['a1'], 2: ['a2'], 3: ['a3']}
    b = d.newball(rec(d, 'a0', 0)); t = 0.4; c = 0; cnt = []
    for step in range(8):
        nc = (c + 1) % 4; src = at_c[c].pop(0); rcv = at_c[nc][0]
        t2 = d.pas(b, t + 0.3, rec(d, rcv, t + 1.2)); cnt.append(t2)
        bx, by = BACK[nc]; q = len(at_c[nc]) - 1; d.mv(src, t + 0.4, t + 2.0, (bx + (bx - 50) * 0.08 * q, by + (by - 50) * 0.08 * q)); at_c[nc].append(src)
        if at_c[c]: d.mv(at_c[c][0], t + 0.6, t + 1.4, Z[c])
        t = t2; c = nc
    pts = e['points'] or ['Passning', 'Mottagning']
    fp = [ph(0, 'Passningsövning', setup_line(e)), ph(1.0, pts[0], 'Passa och följ din passning.'),
          ph(cnt[3], pts[1] if len(pts) > 1 else 'Mottagning i rörelse', ''), ph(cnt[6], pts[2] if len(pts) > 2 else 'Byt håll efter en stund', '')]
    return d, fp, [('cone', x, y) for x, y in Z], [], 'PASSNING'

def shooting(e, p, rnd):
    if keeperish(e) and not has(e, 'göra mål', 'avslut'): return keeper(e, p, rnd)
    d = Drill(); d.p('mv', 'MV', R, (50, 4)); d.p('v', 'V', YEL, (50, 40))
    for tm, x in (('a', 24), ('c', 76)):
        for k in range(3): d.p(f'{tm}{k}', '', B, (x + (-4 if x < 50 else 4) * k, 78 + 5 * k))
    t = 0.4; ex = []
    for rep, (tm, x) in enumerate([('a', 24), ('c', 76), ('a', 24)]):
        pid = f'{tm}{0 if rep < 2 else 1}'
        if rep == 2: d.mv(pid, 0.6, t - 0.2, (24, 78))
        bb = d.newball(rec(d, pid, 0) if rep < 2 else (200, 200))
        if rep == 2: show(d, bb, t - 0.1, rec(d, pid, t - 0.1))
        tp = d.pas(bb, t, rec(d, 'v', t + 0.8)); d.mv(pid, t + 0.1, tp + 0.9, (40 if x < 50 else 60, 26))
        tr = d.pas(bb, tp + 0.15, rec(d, pid, tp + 0.9)); gx = rnd.choice([42, 46, 54, 58])
        tg = shoot(d, bb, tr + 0.05, (gx, 1)); hide(d, bb, tg + 0.3); ex.append(lab(tg, tg + 1.2, (gx, 12), 'MÅL!'))
        d.mv(pid, tg + 0.3, tg + 2.4, (x + (-10 if x < 50 else 10), 92)); t = tr + 0.4
    pts = e['points'] or ['Avslut', 'Placering']
    fp = [ph(0, 'Avslutsövning', setup_line(e)), ph(1.2, pts[0], 'Passa in, få tillbaka bollen i löpningen.'),
          ph(3.4, pts[1] if len(pts) > 1 else 'Avslut med få touch', 'Nästa från andra ledet.'), ph(6.0, pts[2] if len(pts) > 2 else 'Följ upp returen', '')]
    return d, fp, [], ex, 'AVSLUT'

def play(e, p, rnd):
    d = Drill(); n = max(4, min(8, p['out']))
    if has(e, 'stafett', 'tävling', 'race'):
        ex = []
        for tm, x, col in (('b', 34, B), ('r', 66, R)):
            for k in range(3): d.p(f'{tm}{k}', '', col, (x - 6 + 6 * k, 88))
        for tm, x in (('b', 34), ('r', 66)):
            t = 0.4 + (0.25 if tm == 'r' else 0); bb = d.newball(rec(d, f'{tm}1', 0))
            for k in (1, 0, 2):
                pid = f'{tm}{k}'
                if k != 1: d.mv(pid, t - 0.8, t, (x, 84)); d.carry(bb, pid, t - 0.1, t)
                t1 = drive(d, bb, pid, t, (x, 22), 22 - (2 if tm == 'r' else 0)); t2 = drive(d, bb, pid, t1 + 0.1, (x, 82), 22 - (2 if tm == 'r' else 0))
                d.mv(pid, t2, t2 + 0.5, (x - 6 + 6 * k, 92)); t = t2 + 0.4
                if k != 2: nxt = {1: 0, 0: 2}[k]; tt = d.pas(bb, t2 + 0.05, rec(d, f'{tm}{nxt}', t2 + 0.4), 0.35); t = tt
            if tm == 'b': ex.append(lab(t, t + 1.6, (x, 70), 'FÖRST!'))
        pts = e['points'] or ['Ha kul', 'Bollen nära foten']
        fp = [ph(0, 'Stafett med boll', setup_line(e)), ph(1.0, pts[0], 'Dribbla runt konen och tillbaka.'), ph(4.0, 'Lämna över till nästa', pts[1] if len(pts) > 1 else ''), ph(8.0, 'Vilket lag blir först?', '')]
        return d, fp, [('cone', 34, 18), ('cone', 66, 18), ('line', [(20, 86), (80, 86)])], ex, 'LEK'
    KP = [(24 + 52 * ((i * 37) % 10) / 10, 24 + 52 * ((i * 61) % 10) / 10) for i in range(n)]
    team(d, 'k', B, KP, [''] * n); d.p('j', 'J', R, (50, 8))
    balls = [d.newball(rec(d, f'k{k}', 0)) for k in range(n)]
    for k in range(n):
        if k == 1:
            wander(d, 'k1', 0, 4.0, (12, 14, 88, 86), rnd.randint(0, 9999), 1.3); d.carry(balls[1], 'k1', 0, 4.0)
            d.mv('j', 0.4, 4.2, rec(d, 'k1', 4.2)); tp = d.pas(balls[1], 4.4, (8, 92), 0.7); hide(d, balls[1], tp + 0.3)
            d.mv('k1', 4.4, 6.6, (20, 80)); d.mv('j', 4.6, 6.4, (36, 60))
            wander(d, 'k1', 6.6, 17.9, (12, 14, 88, 86), rnd.randint(0, 9999), 1.3); wander(d, 'j', 6.4, 17.9, (12, 14, 88, 86), rnd.randint(0, 9999), 1.3)
        else:
            wander(d, f'k{k}', 0, 17.9, (12, 14, 88, 86), rnd.randint(0, 9999), 1.3); d.carry(balls[k], f'k{k}', 0, 17.9)
    pts = e['points'] or ['Huvudet upp', 'Byt riktning']
    fp = [ph(0, 'Lek med boll', setup_line(e)), ph(1.0, pts[0], 'Alla dribblar i ytan.'), ph(4.2, 'Jagaren petar bort en boll', pts[1] if len(pts) > 1 else 'Skydda bollen med kroppen.'), ph(8.0, pts[2] if len(pts) > 2 else 'Många bollkontakter', 'Byt jagare efter en stund.')]
    return d, fp, [('box', 8, 10, 92, 90)], [lab(4.4, 5.8, (16, 84), 'UT!')], 'LEK'

def keeper_moves(e, p, rnd):
    """Målvaktens fys och fotarbete: förflyttning mellan koner, fånga kast från tränaren."""
    d = Drill(); d.p('mv', 'MV', YEL, (50, 14)); d.p('t', 'T', T_COL, (50, 52))
    CN = [(36, 14), (64, 14), (42, 24), (58, 24)]; t = 0.4
    for q in [(36, 14), (64, 14), (42, 24), (58, 24), (50, 14)]: d.mv('mv', t, t + 0.9, q); t += 1.0
    ex = []
    for k, gx in enumerate([40, 60]):
        bb = d.newball(rec(d, 't', 0) if k == 0 else (200, 200))
        if k: show(d, bb, t, rec(d, 't', t))
        d.mv('mv', t + 0.1, t + 0.7, (gx - 1.8, 13.2)); tc = d.pas(bb, t + 0.1, (gx, 12), 0.6)
        d.carry(bb, 'mv', tc, tc + 0.5); hide(d, bb, tc + 0.6); ex.append(lab(tc, tc + 1.2, (gx, 26), 'FÅNGA')); t = tc + 1.0
        d.mv('mv', t - 0.4, t, (50, 14))
    pts = e['points'] or ['Snabba fötter', 'Grundposition']
    fp = [ph(0, 'Målvaktens fys och fotarbete', setup_line(e)), ph(0.6, pts[0], 'Förflytta dig mellan konerna.'),
          ph(5.4, pts[1] if len(pts) > 1 else 'Grundposition', 'Tränaren kastar – fånga.'), ph(t - 1.6, pts[2] if len(pts) > 2 else 'Kvalitet före tempo', '')]
    return d, fp, [('cone', x, y) for x, y in CN] + [('box', 20, 4, 80, 60)], ex, 'MÅLVAKT'

def fitness(e, p, rnd):
    if keeperish(e): return keeper_moves(e, p, rnd)
    d = Drill(); ball = has(e, 'boll', 'drivning', 'dribbl', 'teknik'); LN = [22, 41, 59, 78]; ex = []
    CN = [(x, y) for x in LN for y in (76, 62, 48, 34)]
    for k, x in enumerate(LN): d.p(f'p{k}', '', B if k % 2 == 0 else R, (x, 88))
    for k, x in enumerate(LN):
        pid = f'p{k}'; t = 0.4 + 0.35 * k; bb = d.newball(rec(d, pid, 0)) if ball else None
        pts = [(x + (3 if i % 2 == 0 else -3), y) for i, y in enumerate((76, 62, 48, 34))] + [(x, 18)]
        t1 = d.path(pid, t, pts, 1.3 if not ball else 1.0)
        if ball: d.carry(bb, pid, t, t1)
        d.mv(pid, t1 + 0.2, t1 + 2.6, (x, 88))
        if ball: d.carry(bb, pid, t1 + 0.2, t1 + 2.6)
    pts = e['points'] or ['Snabba fötter', 'Balans']
    fp = [ph(0, 'Fys och koordination', setup_line(e)), ph(0.8, pts[0], 'Slalom mellan konerna.'), ph(3.4, pts[1] if len(pts) > 1 else 'Sprint till linjen', 'Full fart sista biten.'), ph(6.2, pts[2] if len(pts) > 2 else 'Jogga tillbaka', 'Vila och upprepa.')]
    return d, fp, [('cone', x, y) for x, y in CN] + [('line', [(14, 16), (86, 16)])], ex, 'FYS'

def warmup(e, p, rnd):
    d = Drill(); LN = [(30, 86), (50, 86), (70, 86)]
    for k, ps in enumerate(LN): d.p(f'a{k}', '', B, ps); d.p(f'b{k}', '', B, (ps[0], 94))
    for rep in range(2):
        for k, (x, y) in enumerate(LN):
            pid = f'a{k}' if rep == 0 else f'b{k}'; t = 0.4 + 0.3 * k + 6.0 * rep
            if rep == 1: d.mv(pid, t - 0.8, t, (x, 86))
            zig = [(x + (3 if i % 2 else -3), 86 - 12 * (i + 1)) for i in range(5)] + [(x, 16)]
            t1 = d.path(pid, t, zig, 0.9); d.mv(pid, t1, t1 + 2.4, (x + 9, 50)); d.mv(pid, t1 + 2.4, t1 + 4.6, (x + 9 if rep else x, 94 if rep else 94))
    pts = e['points'] or ['Rätt teknik', 'Lugnt tempo']
    fp = [ph(0, 'Uppvärmning i korridorer', setup_line(e)), ph(0.8, pts[0], 'Rörelsen längs korridoren.'), ph(3.4, pts[1] if len(pts) > 1 else 'Jogga tillbaka på utsidan', ''), ph(6.4, pts[2] if len(pts) > 2 else 'Nästa par startar', 'Två varv per rörelse.')]
    return d, fp, [('line', [(x - 6, 90), (x - 6, 14)]) for x, _ in LN] + [('line', [(76, 90), (76, 14)])], [], 'UPPVÄRMNING'

TEMPLATE = {'Smålagsspel': game, 'Duell (1 mot 1, 2 mot 2)': duel, 'Passningsövning': passing, 'Avslutsövning': shooting,
            'Lek med boll': play, 'Fys och koordination': fitness, 'Skadeförebyggande uppvärmning': warmup}

def build(e):
    rnd = random.Random(e['id']); p = parse(e)
    e = dict(e, points=[x for x in (e.get('points') or []) if 'SvFF' not in x])
    d, fp, shapes, ex, label = TEMPLATE[e['type']](e, p, rnd)
    if not d.balls: d.balls.append([(0, (130, 0)), (14.0, (131, 0))])   # osynlig: utan boll ska övningen inte upprepas
    finish(d, e['id'], slugify(titles(e['name'])[0] + ' ' + (titles(e['name'])[1] if len(titles(e['name'])) > 1 else ''))[:60].strip('-') + '-' + e['id'], titles(e['name']),
           setup_line(e), fp, label, shapes, ex)
    c = C[-1]; c['svb'] = True
    if label in ('SMÅLAGSSPEL',) and (p['gk'] > 0 and not p['small']):
        x1, y1, x2, y2 = area(p); c['goals'] = [(50, y1 - 6)] + ([(50, y2 + 6)] if (p['goals'] or 2) >= 2 else []); c['keep_goals'] = True
    elif label in ('MÅLVAKT', 'AVSLUT') or (label == 'DUELL' and (p['gk'] > 0 or p['goals'] > 0)):
        c['goals'] = [(50, 0)]; c['keep_goals'] = True

def todo():
    import glob
    s = open(glob.glob(os.path.join(HERE, '..', '..', 'app', 'assets', 'app-*.js'))[0]).read()
    have = set(re.findall(r'"([^"]+)"', s[s.index('const OF_EXERCISE_FILM_IDS = new Set(['):].split('])')[0]))
    return [e for e in json.load(open(os.path.join(HERE, 'data', 'bank.json'))) if e['id'].startswith('svb') and e['id'] not in have]

BANK = {e['id']: e for e in json.load(open(os.path.join(HERE, 'data', 'bank.json')))}
args = sys.argv[1:]
if args and args[0] != 'NONE':
    if args[0] == 'ALLA': sel = todo()
    elif args[0].startswith('BATCH:'):
        _, n, k = args[0].split(':'); sel = [e for i, e in enumerate(todo()) if i % int(n) == int(k)]
    else: sel = [BANK[i] for i in args]
    for e in sel:
        try: build(e)
        except Exception as ex_: print('FEL', e['id'], type(ex_).__name__, ex_, file=sys.stderr)
    if os.environ.get('OF_ONLY_BUILD') != '1': render(C, ['x'] + [c['id'] for c in C])
