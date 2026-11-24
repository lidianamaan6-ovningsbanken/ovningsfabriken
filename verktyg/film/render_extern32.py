# Externa övningar, omgång 32 (tolv st). Regel: först d.mv, sedan d.carry; först mottagarens rörelse, sedan passningen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e9', __file__.replace('render_extern32.py', 'render_extern9.py'))
e9 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e9); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e9.finish, e9.rec, e9.chain, e9.wander, e9.counter, e9.arrivals
lab, hide, show, team, boxes, drive, shoot = e9.lab, e9.hide, e9.show, e9.team, e9.boxes, e9.drive, e9.shoot
factor, swap_color, stand, countdown, countup, win = e9.factor, e9.swap_color, e9.stand, e9.countdown, e9.countup, e9.win
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'

def no_ball_finish(*a, **k):
    g = finish.__globals__; old = g['_ball_last']; g['_ball_last'] = lambda balls: 99
    try: finish(*a, **k)
    finally: g['_ball_last'] = old

# ============ fb01 Funino zonspel med joker ============
d = Drill()
GL = [(30, 4), (70, 4), (30, 96), (70, 96)]
BP = [(30, 76), (66, 72), (48, 58)]; RP = [(34, 40), (64, 36), (52, 24)]
team(d, 'b', B, BP); team(d, 'r', R, RP); d.p('j', 'J', YEL, (50, 50))
for k in range(3): wander(d, f'r{k}', 0, 6, boxes([RP[k]], 4)[0], 9600 + k, 1.6)
b = d.newball(rec(d, 'b0', 0))
t = d.pas(b, 0.4, rec(d, 'b2', 1.2)); t = d.pas(b, t + 0.2, rec(d, 'j', t + 0.9)); tz = t                     # genom två zoner
d.mv('b1', t - 1.2, t + 0.6, (70, 22)); t = d.pas(b, t + 0.2, rec(d, 'b1', t + 1.0)); tg = d.pas(b, t + 0.1, (70, 4), 0.5); hide(d, b, tg + 0.3)
fp = [(0, 'Tre mot tre plus en joker', 'Fyra minimål, tre zoner.'),
      (tz - 0.8, 'Bollen genom minst två zoner', 'Jokern får inte göra mål.'),
      (tg - 0.4, 'Mål', 'Omgångar på 2–3 minuter.'),
      (tg + 0.4, 'U8: ingen zonregel', 'U11: max två eller tre touch.')]
finish(d, 'fb01', 'funino-zonspel-med-joker', ['Funino zonspel', 'Med joker'], 'Yta ca 20 × 25 m · Fyra minimål · Tre zoner',
       fp, 'SMÅLAGSSPEL', [('box', 14, 4, 86, 96), ('line', [(14, 34), (86, 34)]), ('line', [(14, 66), (86, 66)])] + [('smallgoal',) + g for g in GL])

# ============ fb02 Minifinter som lek ============
d = Drill()
GT = [(28, 26), (50, 22), (72, 26), (28, 74), (50, 78), (72, 74)]
ST = [(18, 50), (38, 44), (62, 56), (82, 50), (40, 64), (60, 36)]
for k, ps in enumerate(ST): d.p(f'p{k}', '', B, ps)
d.p('f', 'F', R, (50, 50))
balls = [d.newball(rec(d, f'p{k}', 0)) for k in range(6)]; ex = []
for k in range(6):
    t = 0.4 + 0.3 * k; pid = f'p{k}'
    for j in range(2):
        gx, gy = GT[(k + 2 * j) % 6]
        t1 = d.path(pid, t, [(gx - 6, gy + (6 if gy > 50 else -6)), (gx - 2, gy + (3 if gy > 50 else -3)), (gx + 6, gy - (6 if gy > 50 else -6))], 1.1)   # fint vid porten
        d.carry(balls[k], pid, t, t1)
        if k == 0: ex.append(lab(t1 - 0.6, t1 + 0.6, (gx, gy - 8 if gy < 50 else gy + 8), '+1'))
        t = t1 + 0.6
    d.carry(balls[k], pid, t - 0.6, 17.9)
wander(d, 'f', 3.0, 17.9, (36, 36, 64, 64), 9700, 1.6)
fp = [(0, 'Alla har boll – fri dribbling', 'Sex små portar.'),
      (2.0, 'Poäng för varje port med en synlig fint', ''),
      (5.0, 'Fångaren får bara peta bollen', 'Tappad boll: fem bollkontakter.'),
      (10.0, 'Byt fångare var 60–90 sekund', '')]
finish(d, 'fb02', 'minifinter-som-lek', ['Minifinter', 'som lek'], 'Yta 15 × 20 m · Sex små portar',
       fp, 'TEKNIK', [('box', 8, 8, 92, 92)] + [('cone', x + dx, y) for x, y in GT for dx in (-3, 3)], ex)

# ============ fb03 Restförsvaret – sexzonskontringen ============
d = Drill()
BP = [(30, 60), (70, 60), (50, 44), (36, 30), (64, 30), (50, 76)]; RP = [(34, 40), (66, 40), (50, 24), (40, 56), (60, 54), (50, 64)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b2', 0))
t = chain(d, b, 0.4, ['b3', 'b4'], 0.3)                                                                    # två bakom bollen: b5 och b0/b1
tl = win(d, b, 'r2', 'b4', t + 0.3, 0.6)                                                                   # bollförlust – kontring
d.mv('r4', tl, tl + 1.0, (58, 66)); t = d.pas(b, tl + 0.2, rec(d, 'r4', tl + 1.0))
d.mv('b5', tl, t + 0.4, (54, 72)); d.mv('b1', tl, t + 0.4, (62, 64))
tw = win(d, b, 'b5', 'r4', t + 0.4, 0.4); d.mv('b5', tw, tw + 1.4, (50, 80)); d.carry(b, 'b5', tw, tw + 1.4)   # restförsvaret vinner tillbaka
fp = [(0, 'Minst två försvarare bakom bollen', 'Sex mot sex i tre zoner.'),
      (tl - 0.2, 'Bollförlust – kontringen startar', ''),
      (tl + 0.6, 'Restförsvaret stoppar', ''),
      (tw - 0.2, 'Tillbaka inom fem sekunder: bonus', 'Progression: kontring bara genom mittkorridoren.')]
finish(d, 'fb03', 'restforsvaret-sexzonskontringen', ['Restförsvaret', 'Sexzonskontringen'], 'Yta 35 × 45 m i tre zoner · Minimål och kontringsmål',
       fp, 'OMSTÄLLNING', [('box', 6, 4, 94, 96), ('line', [(6, 34), (94, 34)]), ('line', [(6, 66), (94, 66)]), ('smallgoal', 30, 4), ('smallgoal', 70, 4), ('smallgoal', 50, 96)],
       countup(tl + 0.1, 3, (88, 50), (tw - tl) / 3) + [lab(tw, tw + 1.6, (60, 80), 'BONUS')])

# ============ wa01 Partybollen ============
d = Drill()
BP = [(24, 28), (76, 26), (26, 72), (74, 74), (50, 50)]; RP = [(40, 38), (60, 40), (40, 62), (60, 60), (50, 24)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
for k in range(5): wander(d, f'b{k}', 0, 17.9, boxes([BP[k]], 7)[0], 9800 + k, 1.6); wander(d, f'r{k}', 0, 9.0, boxes([RP[k]], 4)[0], 9810 + k, 1.6)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b1', 'b4', 'b2', 'b3', 'b4', 'b0', 'b1'], 0.3); cnt = arrivals(d, b)[:7]
tw = win(d, b, 'r1', 'b1', t + 0.3, 0.8)                                                                    # uppsnappning nollställer
for k in range(5): wander(d, f'r{k}', tw + 0.4, 17.9, boxes([RP[k]], 9)[0], 9820 + k, 1.6)
t = chain(d, b, tw + 0.5, ['r3', 'r0'], 0.3); cnt2 = arrivals(d, b)[-2:]
fp = [(0, 'Laget med bollen räknar högt', 'Alla tillsammans.'),
      (cnt[2], 'Passning – räkna!', ''),
      (tw - 0.2, 'Uppsnappning nollställer räkningen', ''),
      (tw + 0.6, 'Högsta serien vinner', 'Från ”Party Ball” i Kenya.')]
finish(d, 'wa01', 'partybollen-rakna-hogt', ['Partybollen', 'Räkna högt'], 'Ruta 20 × 20 m · Västar · En boll',
       fp, 'SMÅLAGSSPEL', [('box', 12, 12, 88, 88)], counter(cnt, pos=(26, 6), last=None) + counter(cnt2, pos=(74, 6), last=None))

# ============ wa02 2 mot 2-karusellen ============
d = Drill()
BX = [(14, 8, 40, 34), (60, 8, 86, 34), (70, 42, 96, 68), (40, 74, 66, 100), (4, 42, 30, 68)]
CEN = [((x1 + x2) / 2, (y1 + y2) / 2) for x1, y1, x2, y2 in BX]
for k, (cx, cy) in enumerate(CEN):
    d.p(f'b{k}a', '', B, (cx - 6, cy + 4)); d.p(f'b{k}b', '', B, (cx + 6, cy + 4)); d.p(f'r{k}a', '', R, (cx - 5, cy - 4)); d.p(f'r{k}b', '', R, (cx + 5, cy - 4))
balls = []
for k, (cx, cy) in enumerate(CEN):
    bb = d.newball(rec(d, f'b{k}a', 0)); balls.append(bb)
    for pid in (f'b{k}a', f'b{k}b', f'r{k}a', f'r{k}b'): wander(d, pid, 0, 7.0, (BX[k][0] + 3, BX[k][1] + 3, BX[k][2] - 3, BX[k][3] - 3), 9900 + k * 4 + ('ab'.index(pid[-1])) + (2 if pid[0] == 'r' else 0), 1.4)
    t = 0.4
    for rep in range(6): t = d.pas(bb, t + 0.3, rec(d, [f'b{k}b', f'b{k}a'][rep % 2], t + 1.0))
tb = 7.4
for k, (cx, cy) in enumerate(CEN):                                                                           # ”Byt!” – alla medurs till nästa ruta
    nx, ny = CEN[(k + 1) % 5]
    for pid, (dx, dy) in ((f'b{k}a', (-6, 4)), (f'b{k}b', (6, 4)), (f'r{k}a', (-5, -4)), (f'r{k}b', (5, -4))): d.mv(pid, tb, tb + 2.4, (nx + dx, ny + dy))
    hide(d, balls[k], tb); show(d, balls[k], tb + 2.6, (CEN[(k + 1) % 5][0] + 1.8 - 6, CEN[(k + 1) % 5][1] + 2.8))
    t = tb + 2.8
    for rep in range(4): t = d.pas(balls[k], t + 0.3, rec(d, [f'b{k}b', f'b{k}a'][rep % 2], t + 1.0))
fp = [(0, '2 mot 2 i fem rutor', 'Mål: dribbla över motståndarnas linje.'),
      (3.0, 'Spela i din ruta', ''),
      (tb, '”Byt!” – alla medurs', 'Spela vidare med läget som finns där.'),
      (tb + 3.0, 'Variant: laget utan boll moturs', 'Nya motståndare varje gång.')]
finish(d, 'wa02', '2-mot-2-karusellen', ['2 mot 2-', 'karusellen'], 'Fem rutor 10 × 10 m i en ring',
       fp, 'DUELL', [('box',) + bx for bx in BX], [lab(tb - 0.2, tb + 1.6, (50, 50), '”BYT!”')])

# ============ wa03 Rädda kompisen – passningskull ============
d = Drill(); d.p('k', 'K', R, (50, 50))
ST = [(22, 24), (48, 20), (76, 26), (24, 74), (50, 78), (76, 72), (34, 50), (66, 50)]
for k, ps in enumerate(ST): d.p(f'p{k}', '', B, ps)
for k in (0, 1, 2, 3, 4, 7): wander(d, f'p{k}', 0, 17.9, boxes([ST[k]], 6)[0], 10000 + k, 1.6)
b = d.newball(rec(d, 'p1', 0))
d.mv('p6', 0, 3.0, (30, 60)); d.mv('k', 0.3, 3.0, (38, 58))                                                  # kullaren jagar p6
t = d.pas(b, 1.6, rec(d, 'p6', 3.0), 1.2); ts = t                                                           # passa till den som jagas – räddad
d.carry(b, 'p6', t, t + 0.6); t = d.pas(b, t + 0.7, rec(d, 'p4', t + 1.6), 1.0)
d.mv('k', 3.4, 6.0, (68, 62)); d.mv('p5', 2.0, 6.0, (72, 64)); tk = 6.0                                       # kullad – springer ett varv
d.mv('p5', 6.2, 7.6, (94, 64)); d.mv('p5', 7.6, 9.6, (94, 94)); d.mv('p5', 9.6, 11.6, (76, 72))
wander(d, 'p6', ts + 0.6, 17.9, boxes([ST[6]], 6)[0], 10006, 1.6); wander(d, 'p5', 11.6, 17.9, boxes([ST[5]], 6)[0], 10005, 1.6)
wander(d, 'k', 6.2, 17.9, (34, 34, 66, 66), 10010, 1.6)
t = chain(d, b, t, ['p7', 'p2', 'p0', 'p3'], 0.4)
fp = [(0, 'Alla rör sig och passar', 'En kullare.'),
      (ts - 0.6, 'Passa till den som jagas', 'Den som har boll kan inte bli kullad.'),
      (tk - 0.2, 'Kullad – spring ett varv', ''),
      (11.6, 'Med igen', '')]
finish(d, 'wa03', 'radda-kompisen-passningskull', ['Rädda kompisen', 'Passningskull'], 'Ruta 20 × 20 m · 3–4 bollar',
       fp, 'LEK', [('box', 12, 12, 88, 88)], [lab(ts, ts + 1.4, (30, 70), 'RÄDDAD'), lab(tk, tk + 1.4, (70, 54), 'KULLAD')])

# ============ wa04 Led din kompis – blind dribbling ============
d = Drill()
LX = [32, 68]; CN = [(x, y) for x in LX for y in (74, 58, 42, 26)]
for li, x in enumerate(LX): d.p(f'd{li}', 'D', B, (x, 88)); d.p(f'g{li}', 'G', ORA, (x + 12, 92))
for li, x in enumerate(LX):
    bb = d.newball(rec(d, f'd{li}', 0)); t = 0.4
    pts = [(x + (5 if i % 2 == 0 else -5), y) for i, y in enumerate((74, 58, 42, 26))] + [(x, 12)]
    t2 = d.path(f'd{li}', t, [(x, 82)] + pts, 0.45); d.carry(bb, f'd{li}', t, t2)                                          # gående, ögonen täckta
    gtr = d.pl[f'd{li}']['tr']; d.pl[f'g{li}']['tr'] = [(0, (x + 12, 92))] + [(tt + 0.3, (px + 12, py + 4)) for tt, (px, py) in gtr if tt > 0]   # leder med rösten
fp = [(0, 'Ögonen täckta – kompisen leder med rösten', 'Ingen fysisk kontakt.'),
      (3.0, '”Vänster … rakt fram … stopp!”', ''),
      (8.0, 'Börja gående', 'Bara ett par per bana.'),
      (12.0, 'Byt roller efter ett varv', '')]
finish(d, 'wa04', 'led-din-kompis-blind-dribbling', ['Led din kompis', 'Blind dribbling'], 'En rad koner · Par · Ögonbindel',
       fp, 'TEKNIK', [('cone',) + c for c in CN], [lab(3.0, 6.0, (50, 8), '”VÄNSTER!”'), lab(6.4, 9.0, (50, 8), '”RAKT FRAM!”')])

# ============ wa05 Allt blir straff ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96))
BP = [(34, 66), (66, 64), (50, 48)]; RP = [(36, 34), (64, 36), (50, 56)]; team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b0', 0))
t = d.pas(b, 0.4, rec(d, 'b2', 1.1)); t = drive(d, b, 'b2', t, (52, 40), 14)
d.mv('r0', t - 1.0, t + 0.2, (50, 38)); tf = t + 0.3                                                         # frispark – straff
hide(d, b, tf + 0.2); d.mv('r2', tf, tf + 1.6, (50, 22)); d.mv('b2', tf, tf + 1.6, (30, 50)); d.mv('r0', tf, tf + 1.6, (36, 30))
b2 = d.newball((200, 200)); show(d, b2, tf + 1.8, (51.8, 18.8))
for k in (0, 1): d.mv(f'b{k}', tf, tf + 1.8, (30 + 40 * k, 30))
tg = d.pas(b2, tf + 2.6, (56, 1), 0.5)
fp = [(0, 'Två jämna lag med målvakter', 'Plan 15 × 25 m.'),
      (tf - 0.4, 'Frispark?', 'Allt blir straff.'),
      (tf + 1.8, 'Straff till motståndarna', 'Även hands och boll utanför.'),
      (tg + 0.2, 'Variant: en spelare är domare', 'Byts varje omgång.')]
finish(d, 'wa05', 'allt-blir-straff', ['Allt blir', 'straff'], 'Plan 15 × 25 m · Två mål med målvakter',
       fp, 'SMÅLAGSSPEL', [('box', 18, 2, 82, 98)], [lab(tf, tf + 1.6, (64, 40), 'STRAFF!')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ wa06 Fyrmålsspelet – starta direkt ============
d = Drill()
GL = [(30, 6), (70, 6), (30, 94), (70, 94)]
BP = [(30, 66), (66, 64), (48, 48)]; RP = [(34, 36), (62, 34), (52, 56)]; team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b0', 0))
t = d.pas(b, 0.4, rec(d, 'b2', 1.1)); t = drive(d, b, 'b2', t, (64, 16), 16); tg = d.pas(b, t + 0.1, (70, 6), 0.4); hide(d, b, tg + 0.2)
b2 = d.newball((200, 200)); show(d, b2, tg + 0.3, (71.8, 10)); d.mv('r1', tg - 0.6, tg + 0.3, (70, 12))       # motståndarna startar direkt
t = drive(d, b2, 'r1', tg + 0.4, (64, 50), 20); t = d.pas(b2, t + 0.1, rec(d, 'r2', t + 0.8)); t = drive(d, b2, 'r2', t, (34, 84), 20)
tg2 = d.pas(b2, t + 0.1, (30, 94), 0.4); hide(d, b2, tg2 + 0.3)
for k, ps in [(0, (40, 70)), (1, (60, 46))]: d.mv(f'b{k}', tg, tg2, ps)
fp = [(0, 'Försvara två mål, anfall två', 'Plan 15 × 15 m.'),
      (tg - 0.4, 'Mål', ''),
      (tg + 0.3, 'Motståndarna startar direkt', 'Ingen tid att jubla.'),
      (tg2 - 0.4, 'Snabb omställning', 'Variant: alla får anfalla alla mål.')]
finish(d, 'wa06', 'fyrmalsspelet-starta-direkt', ['Fyrmålsspelet', 'Starta direkt'], 'Plan 15 × 15 m · Fyra konmål',
       fp, 'SMÅLAGSSPEL', [('box', 12, 6, 88, 94)] + [('cone', x + dx, y) for x, y in GL for dx in (-4, 4)], [lab(tg + 0.3, tg + 1.6, (82, 16), 'DIREKT!')])

# ============ wa07 Gondi Sinya – tjuv och polis ============
d = Drill()
XS = [26, 42, 58, 74]; CN = [(x, 50) for x in XS]
for k, x in enumerate(XS): d.p(f't{k}', 'T', B, (x, 84)); d.p(f'p{k}', 'P', R, (x, 16))
cones = [d.newball((x, 50)) for x in XS]
for k, x in enumerate(XS):
    t0 = 0.8 + 1.6 * k; d.mv(f't{k}', t0, t0 + 1.2, (x, 53)); d.mv(f'p{k}', t0 + 0.3, t0 + 1.4, (x + 3, 48))
    d.carry(cones[k], f't{k}', t0 + 1.2, t0 + 2.6)
    if k in (1, 3):                                                                                           # fångad – lämnar tillbaka konen
        d.mv(f't{k}', t0 + 1.2, t0 + 2.0, (x, 62)); d.mv(f'p{k}', t0 + 1.4, t0 + 2.0, (x + 3, 60))
        d.balls[cones[k]] = [(tt, q) for tt, q in d.balls[cones[k]] if tt <= t0 + 2.0] + [(t0 + 2.6, (x, 50))]
        d.mv(f't{k}', t0 + 2.4, t0 + 3.6, (x, 84)); d.mv(f'p{k}', t0 + 2.4, t0 + 3.6, (x, 16))
    else:                                                                                                     # hinner hem – polisen ute
        d.mv(f't{k}', t0 + 1.2, t0 + 2.6, (x, 86)); d.mv(f'p{k}', t0 + 1.4, t0 + 2.6, (x, 76)); d.mv(f'p{k}', t0 + 3.0, t0 + 4.4, (x + 8, 98))
fp = [(0, 'Tjuvar på ena linjen, poliser på den andra', 'Leken kommer från Kenya.'),
      (1.0, 'Tjuven tar en kon och springer hem', ''),
      (3.6, 'Fångad – lämna tillbaka konen', 'Hinner tjuven hem är polisen ute.'),
      (8.0, 'Byt roller i halvtid', 'Variant: bollar i stället för koner.')]
d.newball((200, 200))
no_ball_finish(d, 'wa07', 'gondi-sinya-tjuv-och-polis', ['Gondi Sinya', 'Tjuv och polis'], 'Yta ca 20 × 5–10 m · Koner i mitten',
       fp, 'LEK', [('line', [(10, 86), (90, 86)]), ('line', [(10, 14), (90, 14)])],
       [lab(0.8 + 1.6 * k + 2.0, 0.8 + 1.6 * k + 3.4, (XS[k], 68 if k in (1, 3) else 94), 'FÅNGAD' if k in (1, 3) else 'HEMMA') for k in range(4)])

# ============ wa08 Tiden är ute – bollsamlarna ============
d = Drill()
HM = [(12, 12), (88, 12), (88, 88), (12, 88)]; COL = [B, R, YEL, WHITE]
for k, (x, y) in enumerate(HM): d.p(f'p{k}', '', COL[k], (x + (6 if x < 50 else -6), y + (6 if y < 50 else -6)))
piles = {k: [d.newball((x + dx, y + dy)) for dx, dy in ((-3, 0), (3, 0), (0, 3))] for k, (x, y) in enumerate(HM)}
t = 0.4
for k in range(4):
    tk = (k + 1) % 4; bb = piles[tk][0]; x, y = HM[tk]
    t1 = 0.4 + 0.4 * k; d.mv(f'p{k}', t1, t1 + 2.4, (x - 3 + (2 if x < 50 else -2), y + 2))                     # hämta en boll från ett annat hörn
    d.mv(f'p{k}', t1 + 2.6, t1 + 5.2, (HM[k][0] + (8 if HM[k][0] < 50 else -8), HM[k][1] + (8 if HM[k][1] < 50 else -8))); d.carry(bb, f'p{k}', t1 + 2.6, t1 + 5.2)
    bb2 = piles[(k + 2) % 4][1]; x2, y2 = HM[(k + 2) % 4]
    d.mv(f'p{k}', t1 + 5.6, t1 + 8.6, (x2 + 3 + (2 if x2 < 50 else -2), y2 + 2))
    d.mv(f'p{k}', t1 + 8.8, t1 + 11.8, (HM[k][0] + (10 if HM[k][0] < 50 else -10), HM[k][1] + (4 if HM[k][1] < 50 else -4))); d.carry(bb2, f'p{k}', t1 + 8.8, t1 + 11.8)
fp = [(0, 'Ett hörn per lag', 'Lika många bollar i varje.'),
      (2.0, 'Hämta en boll från ett annat hörn', 'En i taget – dribbla hem.'),
      (6.0, 'Ingen får vakta sitt eget hörn', ''),
      (12.0, 'Flest bollar vid slutsignalen vinner', 'Korta rundor: 60–90 sekunder.')]
finish(d, 'wa08', 'tiden-ar-ute-bollsamlarna', ['Tiden är ute', 'Bollsamlarna'], 'Ruta 20 × 20 m · Ett hörn per lag',
       fp, 'LEK MED BOLL', [('box', 4, 4, 96, 96)] + [('zone', x - 8, y - 8, x + 8, y + 8, (200, 220, 200), '') for x, y in HM], [lab(14.6, 17.6, (50, 50), 'TIDEN ÄR UTE!')])

# ============ wa09 Hopp – stort mål mot liten port ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
BP = [(30, 62), (70, 60), (50, 46), (50, 78)]; RP = [(34, 36), (66, 34), (50, 24), (50, 56)]; team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b3', 0))
t = chain(d, b, 0.4, ['b0', 'b2'], 0.3); t = d.pas(b, t + 0.2, rec(d, 'b1', t + 0.9)); tg = shoot(d, b, t + 0.1, (56, 1)); hide(d, b, tg + 0.3)   # stort mål
b2 = d.newball((200, 200)); show(d, b2, tg + 0.8, rec(d, 'mv', tg + 0.8))
t = d.pas(b2, tg + 1.0, rec(d, 'r0', tg + 2.0), 1.0); t = drive(d, b2, 'r0', t, (44, 84), 18)
d.mv('r0', t, t + 0.8, (50, 98)); d.carry(b2, 'r0', t, t + 0.8); tp = t + 0.6                                  # dribbla genom porten
d.mv('b3', tg, tp, (58, 84))
fp = [(0, 'Ett lag anfaller det stora målet', ''),
      (tg - 0.4, 'Mål med målvakt', ''),
      (tp - 1.2, 'Andra laget måste dribbla genom porten', ''),
      (tp, 'Byt sida i halvtid', 'Rotera målvakten varannan minut.')]
finish(d, 'wa09', 'hopp-stort-mal-mot-liten-port', ['Hopp', 'Stort mål mot liten port'], 'Plan 20 × 40 m · Stort mål och en liten dribbelport',
       fp, 'SPELÖVNING', [('cone', 46, 96), ('cone', 54, 96)], [lab(tp, tp + 1.6, (50, 88), 'PORT')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

if __name__ == '__main__': render(C, sys.argv)
