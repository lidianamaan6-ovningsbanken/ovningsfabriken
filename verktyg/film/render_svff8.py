# SvFF-övningar efter skickade PDF:er, del 8. Regel: först d.mv, sedan d.carry; först mottagarens rörelse, sedan passningen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e9', __file__.replace('render_svff8.py', 'render_extern9.py'))
e9 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e9); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e9.finish, e9.rec, e9.chain, e9.wander, e9.counter, e9.arrivals
lab, hide, show, team, boxes, drive, shoot = e9.lab, e9.hide, e9.show, e9.team, e9.boxes, e9.drive, e9.shoot
factor, swap_color, stand, countdown, countup, win = e9.factor, e9.swap_color, e9.stand, e9.countdown, e9.countup, e9.win
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'

# ============ wj05 Spelarna först – lekmatch utan coachning ============
SV = ('svb',)
import math
_finish = finish
def finish(d, *a, **k):
    if not d.balls: d.balls.append([(0, (130, 0)), (14.0, (131, 0))])   # osynlig boll: utan boll ska övningen inte upprepas
    return _finish(d, *a, **k)
def tails(idx, fn): C[-1]['players'][idx]['tails'] = fn
def color_at(idx, fn): C[-1]['players'][idx]['color'] = fn
BOX = (10, 12, 90, 88)
BOX = (10, 12, 90, 88)

# ============ svb48723 Ta bollen (framåt) – spelform 5v5 ============
d = Drill(); d.p('t', 'T', T_COL, (96, 50))
PR = [(24, 88), (44, 88), (64, 88)]
for k, (x, y) in enumerate(PR): d.p(f'a{k}', '', B, (x - 4, y)); d.p(f'c{k}', '', B, (x + 4, y))
balls = [d.newball(rec(d, f'a{k}', 0)) for k in range(3)]
for k, (x, y) in enumerate(PR):                                                                                       # paren tar sig över – passa eller driva
    t = 0.5 + 0.2 * k; d.mv(f'c{k}', t, t + 1.4, (x + 8, 66)); t = drive(d, balls[k], f'a{k}', t, (x - 4, 72), 12)
    t = d.pas(balls[k], t + 0.1, rec(d, f'c{k}', t + 0.8)); d.mv(f'a{k}', t - 0.6, t + 1.2, (x - 2, 40)); t = drive(d, balls[k], f'c{k}', t, (x + 6, 50), 12)
    t = d.pas(balls[k], t + 0.1, rec(d, f'a{k}', t + 0.8)); t = drive(d, balls[k], f'a{k}', t, (x - 2, 12), 14); d.mv(f'c{k}', t - 1.6, t, (x + 6, 12))
T3 = 7.6; team(d, 'f', R, [(40, 56), (62, 56)], ['F', 'F'])
for k, (x, y) in enumerate(PR):                                                                                       # progression 3: försvarare bakom mittlinjen
    d.mv(f'a{k}', T3 - 1.0, T3, (x - 4, 14)); d.carry(balls[k], f'a{k}', T3 - 1.0, T3); d.mv(f'c{k}', T3 - 1.0, T3, (x + 4, 14))
    if k == 1:
        t = drive(d, balls[k], 'a1', T3 + 0.2, (42, 44), 12); tw = win(d, balls[k], 'f0', 'a1', t + 0.3, 0.6); t2 = drive(d, balls[k], 'f0', tw, (40, 10), 16)
    else:
        t = drive(d, balls[k], f'a{k}', T3 + 0.2, (x - 4 + (6 if k == 2 else -4), 52), 12); d.mv(f'c{k}', T3 + 0.2, t, (x + 6, 46))
        t = d.pas(balls[k], t + 0.1, rec(d, f'c{k}', t + 0.8)); t = drive(d, balls[k], f'c{k}', t, (x + 6, 88), 14)
d.mv('f1', T3 + 0.4, T3 + 2.4, (66, 50))
fp = [(0, 'Två och två med en boll', 'Ta er över till andra kortsidan – passa eller driv.'), (1.6, 'Ta bollen framåt mot fri yta', 'Tempoväxla och riktningsförändra, var spelbar.'),
      (T3, 'Progression: försvarare bakom mittlinjen', 'Bryter och driver över anfallarnas kortsida.'), (tw + 0.4, 'Tappar du bollen – ta tillbaka den', 'Fler progressioner: mötas, byta riktning, rulla och fånga.')]
finish(d, 'svb48723', 'ta-bollen-framat-spelform-5v5-svb48723', ['Ta bollen (framåt)', 'Spelform 5 mot 5'], '6–11 spelare · Yta 20 × 15 m · En boll per par', fp, 'SPELUPPBYGGNAD',
       [('box', *BOX), ('line', [(10, 50), (90, 50)])], [lab(tw, tw + 1.2, (52, 40), 'BRYT')])

# ============ svb140477 Futsal – Springa och driva (stafett) ============
d = Drill(); ex = []
for tm, x, col in (('b', 34, B), ('r', 66, R)):
    for k in range(3): d.p(f'{tm}{k}', '', col, (x, 82 + 5 * k))
for tm, x in (('b', 34), ('r', 66)):
    t = 0.5 + (0.25 if tm == 'r' else 0)
    for k in range(3):
        pid = f'{tm}{k}'
        if k: d.mv(pid, t - 0.8, t, (x, 82))
        t1 = d.path(pid, t, [(x, 20)], 1.6 if tm == 'b' else 1.5); d.mv(pid, t1, t1 + 0.3, (x + 2, 18)); t2 = d.path(pid, t1 + 0.3, [(x + 2, 80)], 1.6 if tm == 'b' else 1.5)
        d.mv(pid, t2, t2 + 0.6, (x + 10, 92 - 5 * k)); t = t2 + 0.1
    if tm == 'b': tb = t
TB = tb + 1.0; bb = d.newball((200, 200)); show(d, bb, TB, rec(d, 'b0', TB))                                         # progression: driva bollen
for k in range(1):
    d.mv('b0', TB - 0.8, TB, (34, 82)); t = drive(d, bb, 'b0', TB + 0.2, (34, 20), 16); d.mv('b0', t, t + 0.4, (36, 18)); d.carry(bb, 'b0', t, t + 0.4); t = drive(d, bb, 'b0', t + 0.4, (34, 80), 16)
fp = [(0, 'Spring till linjen och tillbaka', 'Nästa i ledet tar över.'), (1.2, 'Korta steg först – sedan längre', 'Främre delen av foten, hjälp till med armarna.'),
      (tb - 1.0, 'Laget klart när alla sprungit', 'Ta tid och slå er egen tid.'), (TB, 'Progression: driv bollen fram och tillbaka', 'Vristen eller utsidan – vänd med sulan.')]
finish(d, 'svb140477', 'futsal-springa-och-driva-stafett-u7-u10-svb140477', ['Futsal – Springa och driva', 'Stafett · U7–U10'], 'Spelare och bollar · Yta ca 15 × 15 m', fp, 'LEK',
       [('line', [(20, 16), (80, 16)]), ('line', [(20, 84), (80, 84)])], [lab(tb, tb + 1.4, (34, 70), 'KLART!')])

# ============ svb140480 Futsal – Nummerboll ============
d = Drill()
G = [[(22, 28), (40, 22), (36, 44), (18, 46)], [(62, 56), (82, 54), (78, 78), (58, 76)]]
for g, pts in enumerate(G):
    for k, q in enumerate(pts): d.p(f'g{g}{k}', str(k + 1), B if g == 0 else R, q)
for g, pts in enumerate(G):
    b = d.newball(rec(d, f'g{g}0', 0)); t = 0.4 + 0.3 * g
    for rep in range(9):
        nk = (rep + 1) % 4; nx, ny = pts[nk]; d.mv(f'g{g}{nk}', t, t + 0.7, (nx + (3 if rep % 2 else -3), ny + (2 if rep % 3 else -2)))
        t = d.pas(b, t + 0.2, rec(d, f'g{g}{nk}', t + 0.9))
        if g == 0 and rep >= 5: pk = f'g{g}{(rep) % 4}'; d.mv(pk, t - 0.9, t + 0.2, rec(d, f'g{g}{nk}', t + 0.2)[:1] + (rec(d, f'g{g}{nk}', t + 0.2)[1] + 4,))
fp = [(0, 'Grupper om fyra med nummer', 'Passa i nummerordning: 1–2–3–4.'), (1.2, 'Rör dig och var spelbar', 'Ta emot med sulan.'),
      (4.4, 'Kommunicera', 'Vet var nästa passning ska innan du tar emot.'), (7.6, 'Progression: passaren pressar mottagaren', 'Backa ut och bli spelbar längre bort.')]
finish(d, 'svb140480', 'futsal-nummerboll-u9-u12-svb140480', ['Futsal – Nummerboll', 'U9–U12'], 'Spelare och bollar · Yta ca 15 × 12 m', fp, 'PASSNING', [('box', *BOX)], [])

# ============ svb140453 Futsal – Nummerspel (U9–U12) ============
d = Drill(); d.p('t', 'T', T_COL, (50, 96))
for k in range(3): d.p(f'b{k}', str(k + 1), B, (6, 38 + 12 * k)); d.p(f'r{k}', str(k + 1), R, (94, 38 + 12 * k))
b = d.newball((200, 200)); show(d, b, 1.0, rec(d, 't', 1.0))
d.mv('b2', 1.0, 2.4, (40, 56)); d.mv('r2', 1.0, 2.4, (60, 50))
t = d.pas(b, 1.2, rec(d, 'b2', 2.4), 1.2); t = drive(d, b, 'b2', t, (36, 30), 12); d.mv('r2', t - 1.2, t, (38, 22))
t = drive(d, b, 'b2', t, (54, 56), 14); t = drive(d, b, 'b2', t, (64, 78), 16); d.mv('r2', t - 1.8, t, (52, 66)); t = drive(d, b, 'b2', t, (68, 90), 16); tg = t
d.carry(b, 'b2', tg, tg + 0.3); hide(d, b, tg + 0.5)
for k in range(3): d.mv(f'b{k}', tg + 0.4, tg + 2.0, [(30, 64), (40, 40), (66, 52)][k]); d.mv(f'r{k}', tg + 0.4, tg + 2.0, [(70, 36), (60, 60), (34, 48)][k])
b2 = d.newball((200, 200)); show(d, b2, tg + 1.8, rec(d, 't', tg + 1.8)); t = d.pas(b2, tg + 2.0, rec(d, 'r1', tg + 3.0), 1.0); t = d.pas(b2, t + 0.3, rec(d, 'r0', t + 1.0))
fp = [(0, 'Två lag med nummer', 'Tränaren ropar vilka som spelar.'), (1.0, '”3!” – in och spela', 'Mål genom att driva genom konmålen, åt båda hållen.'),
      (3.6, 'Vänd spelet till det lediga målet', 'Titta upp efter fria ytor.'), (tg + 0.6, 'Progression: alla på planen', 'Båda lagen gör mål i båda målen.')]
finish(d, 'svb140453', 'futsal-nummerspel-u9-u12-svb140453', ['Futsal – Nummerspel', 'U9–U12'], 'Yta ca 15 × 12 m · Konmål i båda ändar · Två lag med nummer', fp, 'SPELUPPBYGGNAD',
       [('box', 12, 10, 88, 90)] + [('cone', x + dx, y) for x in (32, 68) for y in (10, 90) for dx in (-5, 5)],
       [lab(1.0, 2.4, (78, 92), '”3!”'), lab(tg, tg + 1.4, (68, 82), 'MÅL'), lab(tg + 0.6, tg + 2.2, (74, 92), '”ALLA!”')])

# ============ svb140473 Futsal – Reaktionsjage ============
d = Drill(); d.p('t', 'T', T_COL, (50, 96)); ROWS = [30, 46, 62, 78]
for k, y in enumerate(ROWS): d.p(f'g{k}', '', R, (44, y)); d.p(f'h{k}', '', B, (56, y))
for k, y in enumerate(ROWS):
    d.mv(f'g{k}', 1.2 + 0.05 * k, 2.6, (12, y)); d.mv(f'h{k}', 1.35 + 0.05 * k, 2.6, (18 + (6 if k == 1 else 0), y))
    d.mv(f'g{k}', 3.6, 5.2, (44, y)); d.mv(f'h{k}', 3.6, 5.2, (56, y))
balls = [d.newball((200, 200)) for _ in ROWS]
for k, y in enumerate(ROWS):
    show(d, balls[k], 5.6, rec(d, f'g{k}', 5.6)); d.carry(balls[k], f'g{k}', 5.6, 6.6)
    t = drive(d, balls[k], f'g{k}', 6.8 + 0.06 * k, (12, y), 22); d.mv(f'h{k}', 6.95 + 0.06 * k, t, (20 if k != 2 else 14, y))
fp = [(0, 'Två och två mittemot varandra', 'Halva gruppen röd, halva blå. Kon bakom varje spelare.'), (1.2, '”RÖD!” – spring förbi konen bakom dig', 'Innan den blåa hinner nudda din rygg.'),
      (3.6, 'Progression: den uppropade jagar i stället', 'Korta steg först, främre delen av foten.'), (6.6, 'Progression: med boll', 'Ta med bollen med sulan, driv med vristen.')]
finish(d, 'svb140473', 'futsal-reaktionsjage-u7-u10-svb140473', ['Futsal – Reaktionsjage', 'U7–U10'], 'Spelare två och två · Yta ca 15 × 15 m · Koner och västar', fp, 'FYS',
       [('redcone', 8, y) for y in ROWS] + [('cone', 92, y) for y in ROWS], [lab(1.0, 2.2, (70, 92), '”RÖD!”'), lab(6.4, 7.6, (70, 92), '”RÖD!”')])

# ============ svb141966 Futsal – Kompis kom och hjälp ============
d = Drill(); BX = (14, 22, 86, 78)
KP = [(28, 34), (70, 30), (30, 68), (72, 70), (52, 60), (46, 36)]; team(d, 'k', B, KP, [''] * 6); d.p('j', 'J', R, (50, 48))
for k in (0, 1, 5): wander(d, f'k{k}', 0, 17.9, BX, 980 + k, 1.2)
d.mv('j', 0.4, 2.6, (40, 60)); d.mv('k2', 0, 2.2, (42, 64)); d.mv('k4', 0, 2.2, (46, 64)); tp = 2.2                       # bildar par – säkra
d.mv('j', 2.6, 4.8, (46, 58)); TC = 4.8                                                                                    # klappar fem gånger
for i in range(5): d.mv('j', TC + i * 0.25, TC + i * 0.25 + 0.12, (47, 60)); d.mv('j', TC + i * 0.25 + 0.12, TC + (i + 1) * 0.25, (46, 58))
ts = TC + 1.4; d.mv('k2', ts, ts + 1.4, (24, 50)); d.mv('k4', ts, ts + 1.4, (66, 52)); d.mv('j', ts, ts + 1.6, (68, 52)); d.mv('k3', 0, ts + 1.6, (72, 56)) if False else None
d.mv('k3', 0, ts + 1.6, (74, 60)); tk = ts + 1.6; d.mv('j', tk, tk + 0.2, (72, 58))
wander(d, 'k2', ts + 1.4, 17.9, BX, 990, 1.2); wander(d, 'k4', ts + 1.4, 17.9, BX, 991, 1.2)
wander(d, 'j', tk + 0.4, 17.9, BX, 992, 1.3); wander(d, 'k3', tk + 0.4, 17.9, BX, 993, 1.3)
fp = [(0, 'En jägare med väst i handen', 'Kulla de andra.'), (tp - 0.4, 'Ta en kompis i handen – då är ni säkra', ''),
      (TC, 'Jägaren klappar paret fem gånger', 'Då måste de skiljas och hitta nya kompisar.'), (tk - 0.2, 'Kullad? Du blir ny jägare', 'Rör dig mot fria ytor, ändra riktning och tempo.')]
finish(d, 'svb141966', 'futsal-kompis-kom-och-hjalp-u7-u12-svb141966', ['Futsal – Kompis kom och hjälp', 'U7–U12'], 'Spelare · Yta 12–15 × 7–10 m', fp, 'LEK', [('box', *BX)],
       countup(TC, 5, (46, 50), 0.25) + [lab(tp, tp + 1.4, (44, 72), 'PAR!'), lab(tk, tk + 1.2, (74, 48), 'KULLAD!')])
fc = factor(fp); color_at(4 + 0, lambda tt: B); color_at(3, lambda tt, a=tk * fc: R if tt >= a else B); color_at(6, lambda tt, a=tk * fc: B if tt >= a else R)

# ============ svb140455 Futsal – Kvadraten ============
d = Drill(); OU = [(30, 30), (70, 30), (70, 70), (30, 70)]; team(d, 'b', B, OU)
b = d.newball(rec(d, 'b0', 0)); t = 0.4; cnt = []; cur = 0
for nk in [1, 2, 3, 0, 1]: t = d.pas(b, t + 0.25, rec(d, f'b{nk}', t + 0.9)); cnt.append(t); cur = nk
T2 = t + 0.4; d.p('f', '', R, (200, 200)); d.pl['f']['tr'] = [(0, (200, 200)), (T2 - 0.01, (200, 200)), (T2, (50, 50))]
for nk in [2, 3, 0, 2, 1]:
    tx, ty = OU[nk]; d.mv('f', t, t + 0.8, ((tx + 50) / 2, (ty + 50) / 2)) if t > T2 else None
    t = d.pas(b, t + 0.25, rec(d, f'b{nk}', t + 0.95)); cur = nk
tw = win(d, b, 'f', f'b{cur}', t + 0.5, 0.6); d.mv('f', tw + 0.3, tw + 1.4, OU[cur]); d.mv(f'b{cur}', tw + 0.3, tw + 1.4, (50, 50))
fp = [(0, 'Start: 4 mot 0 med koner i mitten', 'Mottagning med sulan och bra passningar.'), (1.6, 'Öppen kroppsställning', 'Kunna spela åt båda sidor och framåt.'),
      (T2, 'Stegring: 4 mot 1', 'Titta upp och kommunicera mer.'), (tw - 0.2, 'Bryter försvararen – byt plats', 'Variera ytan och antal tillslag.')]
finish(d, 'svb140455', 'futsal-kvadraten-u9-u12-svb140455', ['Futsal – Kvadraten', 'U9–U12'], '4–5 spelare · Yta 7–10 × 7–10 m · Koner', fp, 'PASSNING',
       [('box', 22, 22, 78, 78), ('cone', 46, 46), ('cone', 54, 54)], counter(cnt, pos=(88, 50), last=None) + [lab(tw, tw + 1.4, (50, 16), 'BRUTEN')])
C[-1]['players'][4]['tr'] = [(0, (200, 200)), (T2 * factor(fp) - 0.01, (200, 200))] + [(tt, q) for tt, q in C[-1]['players'][4]['tr'] if tt >= T2 * factor(fp)]

# ============ svb140077 Futsal – Knock out ============
d = Drill(); BX = (16, 18, 84, 82)
KP = [(28, 32), (70, 30), (30, 68), (72, 70), (50, 50), (50, 28)]; team(d, 'k', B, KP, [''] * 6)
balls = [d.newball(rec(d, f'k{k}', 0)) for k in range(6)]
for k in (0, 1, 3, 5): wander(d, f'k{k}', 0, 17.9, BX, 1000 + k, 1.1); d.carry(balls[k], f'k{k}', 0, 17.9)
wander(d, 'k4', 0, 3.0, BX, 1004, 1.1); d.carry(balls[4], 'k4', 0, 3.0); d.mv('k4', 3.0, 3.8, (40, 62)); d.carry(balls[4], 'k4', 3.0, 3.8)
wander(d, 'k2', 0, 3.4, BX, 1002, 1.1); d.carry(balls[2], 'k2', 0, 3.4); tk = d.pas(balls[2], 3.6, (6, 74), 0.7)        # sparkas ut
d.mv('k4', 3.8, 4.4, (42, 66)); d.carry(balls[4], 'k4', 3.8, 4.4)
t = 4.6
for i in range(10): d.mv('k2', t, t + 0.25, (max(8, 30 - 2.4 * (i + 1)), 70 + (1 if i % 2 else -1))); t += 0.3      # hoppar på ett ben
d.carry(balls[2], 'k2', t, t + 0.2) if False else None
d.pl['k2']['tr'].append((t + 0.2, (8, 73))); d.balls[balls[2]] += [(t + 0.3, rec(d, 'k2', t + 0.3))]; th = t + 0.3
for i in range(8): d.mv('k2', th + i * 0.3, th + i * 0.3 + 0.25, (8 + 2.6 * (i + 1), 72 + (1 if i % 2 else -1)))
d.carry(balls[2], 'k2', th, th + 2.4); wander(d, 'k2', th + 2.6, 17.9, BX, 1010, 1.1); d.carry(balls[2], 'k2', th + 2.6, 17.9)
wander(d, 'k4', 4.4, 17.9, BX, 1011, 1.1); d.carry(balls[4], 'k4', 4.4, 17.9)
fp = [(0, 'Alla driver med var sin boll', 'Skydda bollen – och slå ut de andras.'), (3.2, 'Utslagen! Hoppa på ett ben och hämta bollen', 'Hoppa på andra benet tillbaka in.'),
      (6.0, 'Kroppen mellan motspelare och boll', 'Snedställd, sulan för kontroll.'), (10.0, 'Våga ta chansen', 'När någon tappar kontrollen över sin boll.')]
finish(d, 'svb140077', 'futsal-knock-out-u9-u15-svb140077', ['Futsal – Knock out', 'U9–U15'], 'Ca 6 spelare · Yta ca 10 × 8 m · Bollar', fp, 'SPELUPPBYGGNAD',
       [('box', *BX)], [lab(tk - 0.4, tk + 1.0, (30, 58), 'UTE!')])

# ============ svb140441 Futsal – Driva över linje ============
d = Drill(); BP = [(30, 70), (70, 70), (50, 56)]; RP = [(34, 34), (66, 32), (50, 46)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b0', 0)); ex = []
d.mv('r0', 0.4, 1.6, (30, 30)); t = d.pas(b, 0.4, rec(d, 'b2', 1.2)); d.mv('b1', 0.6, t + 0.6, (74, 46)); t = d.pas(b, t + 0.3, rec(d, 'b1', t + 1.1))   # vänd spelet
d.mv('r1', t - 0.6, t + 0.6, (70, 30)); t = drive(d, b, 'b1', t, (78, 24), 16); t = drive(d, b, 'b1', t, (80, 6), 16); tl = t; d.carry(b, 'b1', tl, tl + 0.4)
hide(d, b, tl + 0.5); b2 = d.newball((200, 200)); show(d, b2, tl + 0.8, rec(d, 'r2', tl + 0.8))
for k, q in enumerate(BP): d.mv(f'b{k}', tl, tl + 1.6, q)
t = drive(d, b2, 'r2', tl + 1.0, (50, 66), 14); tw = win(d, b2, 'b2', 'r2', t + 0.3, 0.6); t = drive(d, b2, 'b2', tw, (46, 40), 16)
fp = [(0, 'Spel 3 mot 3', 'Mål: driv bollen med kontroll över motspelarnas kortsida.'), (1.2, 'Hitta och attackera fria ytor', 'Driv eller passa till spelare i fri yta.'),
      (tl - 0.4, 'Över linjen – poäng', ''), (tw - 0.2, 'Ta tillbaka bollen och ställ om', 'Progression: byt spelriktning – bredare och kortare plan.')]
finish(d, 'svb140441', 'futsal-driva-over-linje-u9-u15-svb140441', ['Futsal – Driva över linje', 'U9–U15'], '6 spelare · Yta ca 20 × 12 m · Platta koner', fp, 'SPELUPPBYGGNAD',
       [('box', 14, 6, 86, 94), ('line', [(14, 6), (86, 6)]), ('line', [(14, 94), (86, 94)])], [lab(tl, tl + 1.4, (70, 14), 'ÖVER!'), lab(tw, tw + 1.2, (64, 60), 'BOLLVINST')])

# ============ svb140076 Futsal – En mot en i yta (U9+) ============
d = Drill(); BX = (12, 14, 88, 86)
PR = [((28, 30), (34, 36)), ((70, 28), (64, 34)), ((30, 70), (36, 64)), ((70, 72), (64, 66))]
for k, (a, f) in enumerate(PR): d.p(f'a{k}', '', B, a); d.p(f'f{k}', '', R, f)
balls = [d.newball(rec(d, f'a{k}', 0)) for k in range(4)]
for k, ((ax, ay), _) in enumerate(PR):
    box = (max(BX[0], ax - 16), max(BX[1], ay - 14), min(BX[2], ax + 16), min(BX[3], ay + 14))
    if k == 3:
        wander(d, 'a3', 0, 3.6, box, 1020, 1.1); d.carry(balls[3], 'a3', 0, 3.6); d.mv('f3', 0.3, 3.4, rec(d, 'a3', 3.6))
        tw = d.pas(balls[3], 3.8, rec(d, 'f3', 4.1), 0.3); wander(d, 'f3', 4.1, 17.9, box, 1021, 1.1); d.carry(balls[3], 'f3', 4.1, 17.9)
        d.pl['a3']['tr'] += [(tt + 0.6, (x - 4, y + 3)) for tt, (x, y) in d.pl['f3']['tr'] if tt > 4.1]
    else:
        wander(d, f'a{k}', 0, 17.9, box, 1030 + k, 1.1); d.carry(balls[k], f'a{k}', 0, 17.9)
        tr = d.pl[f'a{k}']['tr']; d.pl[f'f{k}']['tr'] = [(0, PR[k][1])] + [(tt + 0.6, (x + 4, y + 4)) for tt, (x, y) in tr if tt > 0]
fp = [(0, 'Två och två med en boll', 'Behåll bollen – täck, driv och finta.'), (1.0, 'Kroppen mellan motspelaren och bollen', 'Snedställd, sulan för kontroll.'),
      (tw - 0.2, 'Bryter försvararen – byt roller', 'Finta för att skapa tid, titta upp.'), (tw + 2.0, 'Progression: två lag', 'Flest bollar under kontroll efter en viss tid vinner.')]
finish(d, 'svb140076', 'futsal-en-mot-en-i-yta-u9-svb140076', ['Futsal – En mot en i yta', 'U9+'], 'Cirka 8 spelare · Yta ca 15 × 12 m', fp, 'SPELUPPBYGGNAD',
       [('box', *BX)], [lab(tw, tw + 1.4, (60, 58), 'BYT ROLL')])

# ============ svb142819 Futsal – Vem är rädd för...? ============
d = Drill(); RUN = [(24, 90), (38, 90), (52, 90), (66, 90), (80, 90)]
team(d, 'k', B, RUN, [''] * 5); team(d, 'j', R, [(40, 50), (60, 50)], ['J', 'J'])
for k, (x, y) in enumerate(RUN): d.path(f'k{k}', 2.4 + 0.1 * k, [(x + (8 if k % 2 else -8), 62), (x + (-6 if k % 2 else 6), 36), (x, 10)], 1.2)
d.mv('j0', 2.6, 4.2, rec(d, 'k1', 4.2)); tk = 4.2; d.mv('j1', 2.8, 4.6, (64, 40))
d.mv('k1', tk + 0.3, tk + 1.6, (40, 50)); d.mv('j0', tk + 0.3, tk + 1.4, (36, 46)); d.mv('j1', tk + 0.4, tk + 1.8, (60, 50))
for k, (x, y) in enumerate(RUN):
    if k == 1: continue
    d.path(f'k{k}', 7.6 + 0.1 * k, [(x + (6 if k % 2 else -6), 36), (x + (-6 if k % 2 else 6), 64), (x, 90)], 1.2)
d.mv('k1', 7.8, 9.4, rec(d, 'k3', 9.4)); d.mv('j1', 7.8, 9.4, (56, 66)); d.mv('j0', 7.8, 9.4, (32, 62)); tk2 = 9.4
fp = [(0, '”Vem är rädd för … Messi?”', '– ”Inte jag!”'), (2.4, 'Ta dig till andra kortsidan', 'Riktningsförändring, finter och snabbhet.'),
      (tk - 0.2, 'Kullad? Du blir jägare nästa omgång', ''), (7.6, 'Fortsätt tills alla är tagna', 'Jägarna: reagera snabbt och kom upp i fart.')]
finish(d, 'svb142819', 'futsal-vem-ar-radd-for-u7-u10-svb142819', ['Futsal – Vem är rädd för …?', 'U7–U10'], 'Ca 6 spelare · Yta 15 × 8 m · Västar', fp, 'LEK',
       [('box', 12, 6, 88, 94), ('line', [(12, 84), (88, 84)]), ('line', [(12, 16), (88, 16)])],
       [lab(0.4, 1.4, (50, 40), '”VEM ÄR RÄDD FÖR …”'), lab(1.4, 2.4, (50, 80), '”INTE JAG!”'), lab(tk, tk + 1.2, (36, 40), 'KULLAD!'), lab(tk2, tk2 + 1.2, (66, 54), 'KULLAD!')])
fc = factor(fp); color_at(1, lambda tt, a=tk * fc: R if tt >= a else B)

# ============ svb140458 Futsal – En mot en (U7–U15) ============
d = Drill(); d.p('t', 'T', T_COL, (50, 98)); d.p('a', 'A', B, (36, 86)); d.p('f', 'F', R, (50, 8))
for k in range(2): d.p(f'qa{k}', '', B, (28 - 6 * k, 94)); d.p(f'qf{k}', '', R, (60 + 6 * k, 4))
b = d.newball(rec(d, 't', 0))
t = d.pas(b, 0.6, rec(d, 'a', 1.4), 0.8); d.mv('f', 0.7, t + 1.4, (48, 40))
d.mv('a', t, t + 0.4, (40, 80)); d.carry(b, 'a', t, t + 0.4); t = drive(d, b, 'a', t + 0.4, (42, 56), 18)                   # sulan – direkt fart
t = drive(d, b, 'a', t, (58, 42), 18); d.mv('f', t - 0.8, t, (52, 38)); tw = win(d, b, 'f', 'a', t + 0.4, 0.5)
t = drive(d, b, 'f', tw, (44, 70), 18); t = drive(d, b, 'f', t, (46, 94), 18); tl = t; d.mv('a', tw, tl, (50, 80))
fp = [(0, 'Tränaren passar till anfallaren', 'Försvararen startar när bollen lämnar tränarens fot.'), (1.4, 'Attackera bollen med sulan – direkt fart', 'Utmana, finta och dribbla.'),
      (tw - 0.2, 'Brytning – driv över andra kortsidan', 'Försvararen: press och styr åt ett håll.'), (tl, 'Byt uppgifter', 'Spela tills bollen är ur spel.')]
finish(d, 'svb140458', 'futsal-en-mot-en-u7-u15-svb140458', ['Futsal – En mot en', 'U7–U15'], 'Spelare och bollar · Yta 20 × 12 m · Koner', fp, 'KONTRING',
       [('box', 16, 6, 84, 94), ('line', [(16, 6), (84, 6)]), ('line', [(16, 94), (84, 94)])], [lab(tw, tw + 1.2, (66, 40), 'BRYT'), lab(tl, tl + 1.4, (60, 86), 'ÖVER!')])

# ============ svb140444 Futsal – Driva i olika riktningar ============
d = Drill(); d.p('t', 'T', T_COL, (96, 96))
ST = [(50, 14), (86, 50), (50, 86), (14, 50)]; DIRS = [(0, 1), (-1, 0), (0, -1), (1, 0)]
for k, q in enumerate(ST): d.p(f'p{k}', '', B, q)
balls = [d.newball(rec(d, f'p{k}', 0)) for k in range(4)]
CALLS = [(0.8, '”FRAMÅT!”', 1), (3.6, '”HÖGER!”', 'r'), (6.4, '”BAKÅT!”', -1), (9.2, '”VÄNSTER!”', 'l')]
for k in range(4):
    for ci, (tc, _, kind) in enumerate(CALLS):
        x, y = d.pos(f'p{k}'); dx, dy = DIRS[k]
        if kind == 1: q = (x + dx * 22, y + dy * 22)
        elif kind == -1: q = (x - dx * 22, y - dy * 22)
        elif kind == 'r': q = (x - dy * 12, y + dx * 12)
        else: q = (x + dy * 12, y - dx * 12)
        q = (min(86, max(14, q[0])), min(86, max(14, q[1]))); drive(d, balls[k], f'p{k}', tc + 0.3, q, 12)
fp = [(0, 'Alla med var sin boll på ytans fyra sidor', 'Driv åt det håll tränaren säger.'), (0.8, 'Framåt, bakåt, höger eller vänster', 'Bollen nära foten – vristen eller utsidan.'),
      (3.6, 'Vänd med sulan, utsidan eller insidan', ''), (6.4, 'Blicken uppe', 'Se var de andra spelarna är.')]
finish(d, 'svb140444', 'futsal-driva-i-olika-riktningar-u9-u15-svb140444', ['Futsal – Driva i olika riktningar', 'U9–U15'], 'Yta ca 12 × 12 m · Var sin boll', fp, 'SPELUPPBYGGNAD',
       [('box', 10, 10, 90, 90)], [lab(tc, tc + 1.6, (70, 96), txt) for tc, txt, _ in CALLS])

if __name__ == '__main__': render(C, sys.argv)
