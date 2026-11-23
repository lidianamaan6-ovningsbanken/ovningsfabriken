# Externa övningar, omgång 19 (tolv st). Regel: först d.mv, sedan d.carry; först mottagarens rörelse, sedan passningen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e9', __file__.replace('render_extern19.py', 'render_extern9.py'))
e9 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e9); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e9.finish, e9.rec, e9.chain, e9.wander, e9.counter, e9.arrivals
lab, hide, show, team, boxes, drive, shoot = e9.lab, e9.hide, e9.show, e9.team, e9.boxes, e9.drive, e9.shoot
factor, swap_color, stand, countdown, countup, win = e9.factor, e9.swap_color, e9.stand, e9.countdown, e9.countup, e9.win
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'

# ============ sr02 Konkamp ============
d = Drill()
CN = [(30, 50), (42, 46), (50, 54), (58, 46), (70, 50)]
BP = [(22, 84), (40, 86), (60, 86), (78, 84)]; RP = [(22, 16), (40, 14), (60, 14), (78, 16)]
team(d, 'b', B, BP, [''] * 4); team(d, 'r', R, RP, [''] * 4)
bb = [d.newball(rec(d, f'b{k}', 0)) for k in range(4)]; rb = [d.newball(rec(d, f'r{k}', 0)) for k in range(4)]
hits = []
for k, (ci, side) in enumerate([(1, 'b'), (3, 'r'), (0, 'b'), (4, 'r')]):
    t = 0.6 + 2.2 * k; pid = f'{side}{k}'; ball = (bb if side == 'b' else rb)[k]
    y0 = 74 if side == 'b' else 26
    d.mv(pid, t, t + 0.6, (d.pos(pid)[0], y0)); d.carry(ball, pid, 0, t + 0.6)
    th = d.pas(ball, t + 0.7, CN[ci], 0.8); hits.append((th, ci))
    tb = d.pas(ball, th, (CN[ci][0] + 4, CN[ci][1] + (-10 if side == 'b' else 10)), 0.5); hide(d, ball, tb + 0.2)
fp = [(0, 'Skjut ner konerna', 'Koner i mitten.'),
      (1.4, 'Bara bakom linjen', 'Hämta bollar i ert område.'),
      (hits[1][0], 'Rött träffar', ''),
      (hits[3][0], 'Flest fällda koner vinner', '')]
fallen = [lab(th, 18, (CN[ci][0], CN[ci][1] - 5), 'X') for th, ci in hits]
finish(d, 'sr02', 'konkamp', ['Konkamp', 'Lek och reaktion'], 'Koner i mitten · En linje att skjuta bakom',
       fp, 'LEK', [('cone',) + c for c in CN] + [('line', [(8, 70), (92, 70)]), ('line', [(8, 30), (92, 30)])], fallen)

# ============ fc01 Spegeldribbling ============
d = Drill()
PAIRS = [((26, 30), (26, 42)), ((70, 30), (70, 42)), ((26, 64), (26, 76)), ((70, 64), (70, 76))]
for k, (a, c) in enumerate(PAIRS): d.p(f'l{k}', 'L', B, a); d.p(f'k{k}', 'K', ORA, c)
lb = [d.newball(rec(d, f'l{k}', 0)) for k in range(4)]; kb = [d.newball(rec(d, f'k{k}', 0)) for k in range(4)]
for k, (a, c) in enumerate(PAIRS):
    wander(d, f'l{k}', 0, 17.9, (a[0] - 10, a[1] - 6, a[0] + 10, a[1] + 2), 3600 + k, 1.4)
    tr = d.pl[f'l{k}']['tr']; d.pl[f'k{k}']['tr'] = [(t + 0.4, (x, y + 12)) for t, (x, y) in tr]; d.pl[f'k{k}']['tr'].insert(0, (0, c))   # kopierar
    d.carry(lb[k], f'l{k}', 0, 17.9); d.carry(kb[k], f'k{k}', 0, 17.9)
fp = [(0, 'Ena dribblar – kompisen kopierar', 'Par, en boll var.'),
      (3.0, 'Byt riktning och tempo', 'Kompisen speglar allt.'),
      (8.0, 'Byt roller efter två minuter', ''),
      (13.0, 'Avsluta med rörlighet med boll', 'Höga knän, hälkick, sidosteg.')]
finish(d, 'fc01', 'spegeldribbling', ['Spegel-', 'dribbling'], 'Par · En boll var',
       fp, 'TEKNIK', [])

# ============ fc02 Passningsruta 8 × 8 ============
d = Drill()
SQ = [(26, 74), (26, 26), (74, 26), (74, 74)]
for k, ps in enumerate(SQ): d.p(f'p{k}', '', B, ps)
b = d.newball(rec(d, 'p0', 0)); t = 0.4; marks = []
for rep in range(12):
    nk = (rep + 1) % 4; h = f'p{rep % 4}'
    t = d.pas(b, t + 0.05, rec(d, f'p{nk}', t + 0.85)); marks.append(t)
    if rep < 6:
        x, y = SQ[nk]; nn = SQ[(nk + 1) % 4]
        d.carry(b, f'p{nk}', t, t + 0.35); t += 0.35                                                       # mottagning med första touchen
fp = [(0, 'Bollen går runt rutan', 'En spelare vid varje kon.'),
      (1.2, 'Mottagning med första touchen', 'Mot nästa spelare.'),
      (marks[6] - 0.4, 'U9: ett touch', ''),
      (marks[9], 'U8: två touch', 'Byt håll efter en stund.')]
finish(d, 'fc02', 'passningsruta-8x8', ['Passningsruta', '8 × 8'], 'Fyra koner i en kvadrat 8 × 8 m',
       fp, 'PASSNINGSÖVNING', [('cone', x + (-4 if x < 50 else 4), y + (4 if y > 50 else -4)) for x, y in SQ],
       [lab(0.4, marks[6] - 0.4, (50, 50), '2 TOUCH'), lab(marks[6] - 0.4, 17, (50, 50), '1 TOUCH')])

# ============ fc03 1 mot 1 med två minimål ============
d = Drill()
d.p('a', 'A', B, (50, 74)); d.p('f', 'F', R, (40, 22)); d.p('a2', 'A', B, (36, 90)); d.p('f2', 'F', R, (64, 8))
b = d.newball(rec(d, 'a', 0)); t0 = 0.4
t = drive(d, b, 'a', t0, (52, 54), 14); d.mv('f', t0, t, (50, 40))
d.mv('a', t, t + 0.8, (62, 36)); d.carry(b, 'a', t, t + 0.8); d.mv('f', t, t + 0.8, (56, 36)); t += 0.8
tg = shoot(d, b, t + 0.1, (50, 11)); hide(d, b, tg + 0.3)                                                    # mål
d.mv('a', tg, tg + 2.2, (64, 92)); d.mv('f', tg, tg + 2.2, (36, 8))
d.mv('a2', tg - 0.6, tg + 1.0, (50, 74)); d.mv('f2', tg - 0.6, tg + 1.0, (60, 22))
b2 = d.newball((200, 200)); show(d, b2, tg + 1.1, rec(d, 'a2', tg + 1.1)); t1 = tg + 1.3
t = drive(d, b2, 'a2', t1, (48, 50), 14); d.mv('f2', t1, t, (50, 44))
tw = win(d, b2, 'f2', 'a2', t + 0.2, 0.3)
t = drive(d, b2, 'f2', tw, (52, 80), 20); tg2 = shoot(d, b2, t, (50, 89)); d.mv('a2', tw, tg2, (44, 64))   # i det andra målet
fp = [(0, 'Anfallaren startar med boll', 'Försvararen från målets sida.'),
      (tg - 0.6, 'Mål', 'Max åtta sekunder per duell.'),
      (t1, 'Nästa par', ''),
      (tw - 0.2, 'Försvararen vinner – mål i andra målet', '')]
finish(d, 'fc03', '1-mot-1-med-tva-minimal', ['1 mot 1', 'Med två minimål'], 'Två minimål 12 m isär',
       fp, 'DUELL', [('smallgoal', 50, 10), ('smallgoal', 50, 90)], countdown(t0, 8, (86, 50), (tg - t0) / 6)[:6] + countdown(t1, 8, (86, 50), (tg2 - t1) / 6)[:6])

# ============ fc04 Avslut och jubel ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
XS = [30, 42, 54, 66]
for k, x in enumerate(XS): d.p(f'p{k}', '', B, (x, 36))
balls = [d.newball(rec(d, f'p{k}', 0)) for k in range(4)]
t = 0.4; ex = []; OUT = ['MÅL', 'RÄDDNING', 'MÅL', 'MISS']
for k in range(4):
    tg = d.pas(balls[k], t, (44 + 4 * k if OUT[k] != 'MISS' else 66, 1 if OUT[k] != 'MISS' else -2), 0.6)
    if OUT[k] == 'RÄDDNING': d.mv('mv', t, tg, (48, 5))
    hide(d, balls[k], tg + 0.3); ex.append(lab(tg, tg + 1.2, (76, 16), OUT[k])); t = tg + 0.6
t2 = t
for k in (0, 2): d.mv(f'p{k}', t2, t2 + 1.2, (XS[k] + 2, 26))                                                 # går vidare
for k in (1, 3):
    jb = d.newball((200, 200)); show(d, jb, t2 + 0.2, (XS[k] + 1.8, 40)); tr = d.balls[jb]; tt = t2 + 0.4
    d.mv(f'p{k}', t2, t2 + 0.6, (XS[k], 42))
    for j in range(5): tr += [(tt, (XS[k] + 1.8, 40)), (tt + 0.3, (XS[k] + 1.8, 35)), (tt + 0.6, (XS[k] + 1.8, 40))]; tt += 0.6   # fem jongleringsförsök
    hide(d, jb, tt + 0.1)
for k in range(4): d.mv(f'p{k}', t2 + 4.0, t2 + 5.0, (50 + (k - 1.5) * 4, 30))                              # jubel och high five
fp = [(0, 'Alla skjuter mot mål', 'Avstånd 8 m.'),
      (t2, 'Mål – gå vidare', 'Övriga gör fem jongleringsförsök.'),
      (t2 + 2.0, 'Fem jongleringsförsök', 'Innan nästa runda.'),
      (t2 + 4.0, 'Avsluta med jubel och high five', '')]
finish(d, 'fc04', 'avslut-och-jubel', ['Avslut och', 'jubel'], 'Mål · Avstånd 8 m',
       fp, 'AVSLUT', [], ex + [lab(t2 + 5.0, t2 + 7.0, (50, 20), 'HIGH FIVE!')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ ve01 Skuggförsvar ============
d = Drill()
LX = [28, 72]
for li, x in enumerate(LX): d.p(f'a{li}', 'A', B, (x, 84)); d.p(f'f{li}', 'F', R, (x, 72))
balls = [d.newball(rec(d, f'a{li}', 0)) for li in range(2)]
for li, x in enumerate(LX):
    t = 0.4; y = 84
    for rep in range(5):
        dx = 6 if rep % 2 == 0 else -6
        ny = y - 12
        d.mv(f'a{li}', t, t + 1.4, (x + dx, ny)); d.carry(balls[li], f'a{li}', t, t + 1.4)
        d.mv(f'f{li}', t + 0.2, t + 1.6, (x + dx, ny - 10))                                                   # speglar 1–2 m framför
        t += 1.6; y = ny
fp = [(0, 'Anfallaren går framåt med bollen', 'Korridor 5 × 10 m.'),
      (1.6, 'Försvararen speglar', 'Mellan anfallaren och målet.'),
      (4.0, 'Håll 1–2 m avstånd', 'Tyngden lätt bakåt.'),
      (7.0, 'Ingen tackling', 'Fem repetitioner, sedan byte.')]
finish(d, 've01', 'skuggforsvar', ['Skugg-', 'försvar'], 'Korridor 5 × 10 m · Par',
       fp, 'DUELL', [('box', x - 12, 6, x + 12, 92) for x in LX])

# ============ ve02 Press på utlösare ============
d = Drill(); d.p('mv', 'MV', R, (50, 6)); d.p('t', 'T', T_COL, (90, 30))
team(d, 'f', R, [(34, 24), (66, 22)]); team(d, 'a', B, [(32, 52), (50, 58), (68, 52)])
b = d.newball(rec(d, 't', 0))
t = d.pas(b, 0.6, rec(d, 'f1', 1.5)); tu = t                                                                # utlösaren
for k, ps in enumerate([(52, 26), (62, 30), (70, 28)]): d.mv(f'a{k}', tu, tu + 1.4, ps)                    # tre pressar direkt
d.carry(b, 'f1', tu, tu + 0.8); d.mv('f1', tu, tu + 0.8, (68, 18))
tw = win(d, b, 'a2', 'f1', tu + 1.6, 0.4)
tg = shoot(d, b, tw + 0.3, (46, 1))
fp = [(0, 'Tränaren passar till en försvarare', 'Det är utlösaren.'),
      (tu, 'Tre anfallare pressar direkt', 'Tillsammans.'),
      (tw - 0.2, 'Misstag inom fem sekunder', 'Anfallarna vinner bollen.'),
      (tg - 0.3, 'Vinner de bollen får de göra mål', 'Spelar försvararna ut fortsätter spelet.')]
finish(d, 've02', 'press-pa-utlosare', ['Press på', 'utlösare'], 'Yta 20 × 15 m · Målvakt, två försvarare, tre anfallare',
       fp, 'PRESS', [('box', 14, 2, 86, 70)], [lab(tu - 0.4, tu + 1.2, (76, 40), 'UTLÖSARE!')] + countup(tu, 5, (20, 40), (tw - tu) / 4)[:4])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ ve03 1 mot 1-försvar i korridor ============
d = Drill()
d.p('a', 'A', B, (50, 80)); d.p('f', 'F', R, (50, 66)); d.p('o', 'O', YEL, (82, 50))
b = d.newball(rec(d, 'a', 0))
t = drive(d, b, 'a', 0.4, (48, 70), 10); d.mv('f', 0.4, t, (48, 60))
d.mv('a', t, t + 0.8, (58, 56)); d.carry(b, 'a', t, t + 0.8); d.mv('f', t, t + 0.8, (60, 52)); t += 0.8      # försvararen tvingar ut
d.mv('a', t, t + 0.8, (64, 44)); d.carry(b, 'a', t, t + 0.8); d.mv('f', t, t + 0.8, (62, 42)); t += 0.8
tout = d.pas(b, t + 0.1, (72, 40), 0.5); hide(d, b, tout + 0.2)                                              # bollen ut
d.mv('a', tout, tout + 2.0, (50, 66)); d.mv('f', tout, tout + 2.0, (50, 80))                                # byt roller
b2 = d.newball((200, 200)); show(d, b2, tout + 2.1, rec(d, 'f', tout + 2.1))
t = drive(d, b2, 'f', tout + 2.3, (50, 70), 10); d.mv('a', tout + 2.3, t, (50, 60))
d.mv('f', t, t + 1.4, (42, 30)); d.carry(b2, 'f', t, t + 1.4); d.mv('a', t, t + 1.4, (48, 34)); t += 1.4
tg = shoot(d, b2, t + 0.1, (50, 9)); hide(d, b2, tg + 0.3)
fp = [(0, 'Anfallaren startar med bollen', 'Försvararen 3 m framför.'),
      (1.4, 'Tvinga ut bollen', 'Förhindra skott.'),
      (tout + 0.2, 'Byt roller', 'Observatören ger feedback.'),
      (tg - 0.6, 'Anfallaren förbi – mål', '')]
finish(d, 've03', '1-mot-1-forsvar-i-korridor', ['1 mot 1-försvar', 'I korridor'], 'Korridor 5 × 15 m med mål i varje ände',
       fp, 'DUELL', [('box', 34, 8, 66, 92), ('smallgoal', 50, 8), ('smallgoal', 50, 92)], [lab(tout, tout + 1.6, (78, 36), 'UT')])

# ============ ve04 Avslut efter inlägg ============
d = Drill(); d.p('mv', 'MV', R, (50, 4)); d.p('i', 'I', WHITE, (88, 18)); d.p('i2', 'I', WHITE, (12, 18))
team(d, 'a', B, [(46, 32), (58, 34)])
b = d.newball(rec(d, 'i', 0))
d.mv('a1', 0.6, 2.2, (58, 8)); d.mv('a0', 0.6, 2.2, (48, 16))                                              # främre stolpen och straffpunkten
t = d.pas(b, 1.4, rec(d, 'a0', 2.4), 1.0); tg = shoot(d, b, t + 0.05, (44, 1)); hide(d, b, tg + 0.4)
d.mv('a0', tg, tg + 1.8, (54, 32)); d.mv('a1', tg, tg + 1.8, (42, 34))
b2 = d.newball(rec(d, 'i2', 0)); t0 = tg + 1.6                                                              # byt sida
d.mv('a1', t0, t0 + 1.6, (42, 8)); d.mv('a0', t0, t0 + 1.6, (52, 16))
t = d.pas(b2, t0 + 0.8, rec(d, 'a1', t0 + 1.8), 1.0); tg2 = shoot(d, b2, t + 0.05, (54, 1))
fp = [(0, 'En löper mot främre stolpen', 'En mot straffpunkten.'),
      (1.4, 'Inlägg', 'Båda försöker avsluta.'),
      (t0, 'Byt sida var femte boll', ''),
      (tg2 - 0.4, 'För yngre: lägre och långsammare inlägg', '')]
finish(d, 've04', 'avslut-efter-inlagg', ['Avslut efter', 'inlägg'], 'Straffområdet · Inläggare, två anfallare och målvakt',
       fp, 'AVSLUT', [])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ ve05 Färgportar ============
d = Drill()
GCOL = {'cone': ORA, 'redcone': '#e5483b', 'yellowcone': YEL}
GATES = [((26, 26), 'cone'), ((74, 26), 'redcone'), ((50, 50), 'yellowcone'), ((26, 74), 'redcone'), ((74, 74), 'cone'), ((50, 18), 'yellowcone')]
PAIRS = [((14, 26), (38, 26)), ((62, 74), (86, 74))]
for k, (a, c) in enumerate(PAIRS): d.p(f'a{k}', '', B, a); d.p(f'c{k}', '', B, c)
ROUTE = {0: [0, 3, 5], 1: [4, 1, 2]}
for k in range(2):
    bl = d.newball(rec(d, f'a{k}', 0)); t = 0.4 + 0.3 * k; h, o = f'a{k}', f'c{k}'
    for gi in ROUTE[k] * 2:
        (gx, gy), _ = GATES[gi]
        d.mv(h, t, t + 2.0, (gx - 10, gy)); d.mv(o, t, t + 2.0, (gx + 10, gy)); d.carry(bl, h, t, t + 2.0)
        t = d.pas(bl, t + 2.1, rec(d, o, t + 2.7)) + 0.1; h, o = o, h
fp = [(0, 'Passa genom så många portar som möjligt', 'Par, sex portar i olika färger.'),
      (3.0, 'Byt port efter varje passning', ''),
      (8.0, 'Variant: tränaren ropar en färg', 'Bara de portarna gäller.'),
      (13.0, 'Tre minuter per omgång', '')]
shapes = []
for (x, y), k in GATES: shapes += [(k, x, y - 4), (k, x, y + 4)]
finish(d, 've05', 'fargportar', ['Färgportar', 'Passningsövning'], 'Yta 20 × 20 m · Sex portar i olika färger',
       fp, 'PASSNINGSÖVNING', [('box', 8, 8, 92, 92)] + shapes, [lab(8.0, 11.0, (50, 90), '”GUL!”')])

# ============ ve06 Mottagning under press ============
d = Drill()
BP = [(24, 26), (76, 28), (26, 74), (74, 72)]; RP = [(42, 40), (58, 42), (42, 60), (58, 58)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
for k in range(4): wander(d, f'b{k}', 0, 17.9, boxes([BP[k]], 6)[0], 3700 + k, 1.6); wander(d, f'r{k}', 0, 7.0, boxes([RP[k]], 4)[0], 3710 + k, 1.4)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b1', 'b3', 'b2', 'b0'], 0.4)
d.mv('r0', t - 0.8, t + 0.4, (38, 34)); t1 = d.pas(b, t + 0.3, (34, 32), 0.6); tw = t1                       # bryter passningen – utan tackling
d.carry(b, 'r0', tw, tw + 0.4)
for k in range(4): wander(d, f'r{k}', tw + 0.4, 17.9, boxes([RP[k]], 7)[0], 3720 + k, 1.4)
t = chain(d, b, tw + 0.5, ['r1', 'r3', 'r2'], 0.4)
fp = [(0, 'Ett lag passar bollen', 'Två lag om fyra.'),
      (2.0, 'Ta emot under press', 'Kroppen mellan bollen och motståndaren.'),
      (tw - 0.3, 'Bryt passningen – utan tackling', ''),
      (tw + 0.6, 'Bollinnehavet byts varannan minut', '')]
finish(d, 've06', 'mottagning-under-press', ['Mottagning', 'under press'], 'Yta 15 × 15 m · Två lag om fyra',
       fp, 'POSITIONSSPEL', [('box', 14, 14, 86, 86)])

# ============ ve07 Tredje man till avslut ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
d.p('a', 'A', B, (30, 70)); d.p('bb', 'B', B, (50, 40)); d.p('c', 'C', B, (70, 66)); d.p('f', 'F', R, (50, 30))
b = d.newball(rec(d, 'a', 0))
d.mv('bb', 0.4, 1.2, (50, 46)); t = d.pas(b, 0.6, rec(d, 'bb', 1.4))
d.mv('c', 1.0, t + 1.0, (58, 32)); t = d.pas(b, t + 0.1, rec(d, 'c', t + 1.0))                                 # lägger av till C som löper in
tg = shoot(d, b, t + 0.05, (46, 1)); hide(d, b, tg + 0.4); tc = t
d.mv('f', 0.8, tc, (52, 36))
for pid, ps in (('a', (30, 70)), ('bb', (50, 40)), ('c', (70, 66))): d.mv(pid, tg + 0.2, tg + 2.2, ps)
b2 = d.newball((200, 200)); show(d, b2, tg + 2.3, rec(d, 'a', tg + 2.3))
d.mv('bb', tg + 2.3, tg + 3.1, (50, 46)); d.mv('f', tg + 2.3, tg + 3.2, rec(d, 'bb', tg + 3.2))             # försvararen pressar aktivt
t = d.pas(b2, tg + 2.5, rec(d, 'bb', tg + 3.3)); d.mv('c', tg + 2.8, t + 1.0, (60, 30)); t = d.pas(b2, t + 0.1, rec(d, 'c', t + 1.0))
tg2 = shoot(d, b2, t + 0.05, (54, 1))
fp = [(0, 'A passar till B', 'Tre spelare, mål med målvakt.'),
      (1.4, 'B lägger av till C', 'Som löper in från djupet.'),
      (tc - 0.2, 'C skjuter med första touchen', ''),
      (tg + 2.3, 'Variant: försvararen pressar', 'Först passivt, sedan aktivt.')]
finish(d, 've07', 'tredje-man-till-avslut', ['Tredje man', 'till avslut'], 'Tre spelare · Mål med målvakt',
       fp, 'AVSLUT', [])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

if __name__ == '__main__': render(C, sys.argv)
