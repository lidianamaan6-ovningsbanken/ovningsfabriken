# Externa övningar, omgång 4 (tolv st). Regel: först d.mv, sedan d.carry; hide före show.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e1', __file__.replace('render_extern4.py', 'render_extern1.py'))
e1 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e1); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e1.finish, e1.rec, e1.chain, e1.wander, e1.counter, e1.arrivals
lab, hide, show, team, boxes, drive, shoot = e1.lab, e1.hide, e1.show, e1.team, e1.boxes, e1.drive, e1.shoot
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; GRN = '#3fbf5f'; RED = '#e5483b'; T_COL = '#1b211e'

def factor(phases):
    """Hur mycket finish() sträckte ut tiden (behövs för färgbyten och svansar)."""
    return C[-1]['phases'][1][0] / phases[1][0]
def swap_color(idx, t, before, after):
    C[-1]['players'][idx]['color'] = (lambda tt, t=t, a=before, b=after: a if tt < t else b)
def stand(d, pid, t0, t1):
    d.mv(pid, t0, t1, d.pos(pid))

# ============ f01 3 mot 1 med jagare som kommer in ============
d = Drill(); d.p('t', 'T', T_COL, (50, 14))
LB = [(17, 36), (39, 36), (28, 56)]; RB = [(61, 36), (83, 36), (72, 56)]
team(d, 'b', B, LB); team(d, 'w', B, RB); team(d, 'r', R, [(50, 80), (50, 86), (50, 92)])
b = d.newball(rec(d, 't', 0))
t = d.pas(b, 0.4, rec(d, 'b0', 1.2))
d.mv('r0', 0.5, 1.7, (28, 45)); d.mv('r1', 0.9, 1.6, (50, 80)); d.mv('r2', 1.2, 1.9, (50, 86))   # först i kön sprintar in
t = chain(d, b, t, ['b1', 'b2', 'b0', 'b1'], 0.25); cnt = arrivals(d, b)[1:5]
d.mv('r0', t - 0.5, t + 0.3, (32, 40)); d.mv('r0', t + 0.3, t + 0.9, rec(d, 'b2', t + 0.9))
tw = d.pas(b, t + 0.35, rec(d, 'r0', t + 0.9), 0.55)                                    # brytning
t = d.pas(b, tw + 0.3, rec(d, 't', tw + 1.2))                                           # bollen tillbaka till tränaren
d.mv('r0', tw + 0.3, tw + 1.5, (56, 80)); tt = tw + 1.5                                 # sprintar ut och klappar nästa
stand(d, 'r0', tt, tt + 0.4); d.mv('r0', tt + 0.4, tt + 1.2, (50, 92)); d.mv('r2', tt + 0.6, tt + 1.0, (50, 86))
d.mv('r1', tt + 0.2, tt + 1.4, (72, 45))
t = d.pas(b, tt + 0.3, rec(d, 'w0', tt + 1.1))
t = chain(d, b, t, ['w1', 'w2', 'w0', 'w2'], 0.25)
d.mv('r1', t - 0.6, t + 0.2, (70, 50))
fp = [(0, 'Tränaren spelar in en boll', 'Tre spelare i rutan, max två touch.'),
      (0.6, 'Först i kön sprintar in och pressar', 'Tre mot en i rutan på 5 × 5 m.'),
      (tw - 0.2, 'Bollen vinns', 'Pressaren sprintar ut ur rutan.'),
      (tt - 0.2, 'Klappa nästa i kön', 'Den nya pressaren sprintar in i andra rutan.'),
      (tt + 2.4, 'Byt roller efter fyra brytningar', 'Hela tiden: sprint in, press, sprint ut.')]
finish(d, 'f01', '3-mot-1-med-jagare-som-kommer-in', ['3 mot 1', 'Med jagare som kommer in'], 'Två rutor på 5 × 5 m · Kö bakom en kon 3 m från rutorna',
       fp, 'ÅTERERÖVRING', [('box', 12, 30, 44, 62), ('box', 56, 30, 88, 62), ('cone', 50, 74)],
       [lab(tw, tw + 1.6, (28, 24), 'BRYTNING')])

# ============ f02 4 mot 4 + 2 i fyra zoner ============
d = Drill()
X1, Y1, X2, Y2 = 8, 14, 92, 86
BL = [(14, 20), (44, 20), (14, 46), (44, 46)]; JL = [(29, 16), (29, 48)]; RL = [(22, 28), (36, 28), (22, 38), (36, 38)]
team(d, 'b', B, BL); team(d, 'j', G, JL, ['J', 'J']); team(d, 'r', R, RL); team(d, 'w', WHITE, [(20, 94), (34, 94), (66, 94), (80, 94)])
for k in range(4): wander(d, f'r{k}', 0, 8.6, boxes([RL[k]], 3)[0], 600 + k, 1.6)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.3, ['j0', 'b1', 'b3', 'j1', 'b2', 'b0', 'j0', 'b1', 'b3', 'j1'], 0.2); cnt = arrivals(d, b)[:10]; tp = cnt[-1]
d.mv('r3', t - 0.6, t + 0.3, rec(d, 'b2', t + 0.4)); tl = d.pas(b, t + 0.2, rec(d, 'r3', t + 0.6), 0.4)       # bollförlust
d.mv('b2', tl, tl + 0.5, rec(d, 'r3', tl + 0.5)); tw = d.pas(b, tl + 0.6, rec(d, 'b2', tl + 0.9), 0.3)          # vinner direkt: kvar
d.mv('r3', tw, tw + 0.6, (32, 40))
t = chain(d, b, tw, ['b0', 'j1'], 0.25)
d.mv('r1', t - 0.7, t + 0.2, rec(d, 'j1', t + 0.3)); tl2 = d.pas(b, t + 0.2, rec(d, 'r1', t + 0.5), 0.35)   # förlust igen
MV_B = [(64, 28), (78, 28), (64, 38), (78, 38)]; MV_R = [(56, 20), (86, 20), (56, 46), (86, 46)]; MV_J = [(71, 16), (71, 48)]
for k in range(4): d.mv(f'b{k}', tl2 + 0.2, tl2 + 1.8, MV_B[k])
for k, pid in enumerate(['r0', 'r2', 'r3']): d.mv(pid, tl2 + 0.2, tl2 + 1.8, MV_R[[0, 2, 3][k]])
for k in range(2): d.mv(f'j{k}', tl2 + 0.2, tl2 + 1.8, MV_J[k])
d.mv('r1', tl2 + 0.2, tl2 + 1.8, MV_R[1]); d.carry(b, 'r1', tl2 + 0.2, tl2 + 1.8)
t = chain(d, b, tl2 + 1.9, ['j0', 'r0', 'r2', 'j1'], 0.25)
fp = [(0, 'Blått och jokrarna håller bollen i en zon', '6 mot 4 med två touch. Vitt väntar utanför.'),
      (tp - 0.3, 'Tio passningar: 1 poäng', 'Laget behåller bollen och spelar vidare.'),
      (tl - 0.2, 'Bollförlust – vinn tillbaka direkt', 'Vinner laget bollen direkt stannar spelet kvar.'),
      (tl2 - 0.2, 'Bollförlust igen', 'Nu flyttar spelet till en angränsande zon.'),
      (tl2 + 1.9, 'Rött och jokrarna håller bollen', 'Blått försvarar i den nya zonen.')]
finish(d, 'f02', '4-mot-4-plus-2-i-fyra-zoner', ['4 mot 4 + 2', 'I fyra zoner'], 'Tre lag om fyra och två jokrar · Ruta 20 × 20 m i fyra zoner',
       fp, 'OMSTÄLLNING', [('box', X1, Y1, X2, Y2), ('line', [(50, Y1), (50, Y2)]), ('line', [(X1, 50), (X2, 50)])],
       counter(cnt, pos=(29, 9)) + [lab(tw, tw + 1.4, (29, 56), 'KVAR'), lab(tl2 + 0.3, tl2 + 1.9, (50, 56), 'NY ZON')])

# ============ f03 7 mot 7 med kontrapress och två mål ============
d = Drill(); d.p('mv', 'MV', ORA, (50, 6))
OP = [(24, 22), (50, 20), (76, 22), (32, 42), (68, 42), (50, 54)]
BP = [(30, 86), (70, 86), (50, 76), (34, 64), (66, 64), (18, 52), (82, 52)]
team(d, 'o', ORA, OP); team(d, 'b', B, BP)
b = d.newball(rec(d, 'mv', 0))
t = d.pas(b, 0.4, rec(d, 'o0', 1.1)); t = chain(d, b, t, ['o3', 'o5', 'o4'], 0.25)
d.mv('b4', t - 0.6, t + 0.6, (66, 56))
t = drive(d, b, 'o4', t + 0.1, (60, 80)); t = shoot(d, b, t, (72, 99)); tg = t                         # avslut efter konlinjen
hide(d, b, tg + 0.3)
for k in range(6): d.mv(f'o{k}', tg, tg + 1.8, OP[k])
d.mv('b4', tg, tg + 1.8, BP[4])
show(d, b, tg + 1.9, rec(d, 'mv', tg + 1.9))
t = d.pas(b, tg + 2.1, rec(d, 'o2', tg + 2.8)); t = d.pas(b, t + 0.25, rec(d, 'o4', t + 0.9))
d.mv('b4', t - 0.8, t + 0.2, rec(d, 'o4', t + 0.3)); tl = d.pas(b, t + 0.25, rec(d, 'b4', t + 0.5), 0.3)   # blått vinner bollen
d.mv('o4', tl, tl + 0.6, rec(d, 'b4', tl + 0.7)); d.mv('o5', tl, tl + 0.8, (60, 52))                   # kontrapress
tw = d.pas(b, tl + 0.7, rec(d, 'o4', tl + 1.0), 0.3)                                                     # snabb återerövring
t = d.pas(b, tw + 0.25, rec(d, 'o5', tw + 0.9)); d.mv('o5', t, t + 1.2, (46, 80)); d.carry(b, 'o5', t, t + 1.2); t += 1.2
t = shoot(d, b, t, (28, 99)); tg2 = t
fp = [(0, 'Orange bygger upp från målvakten', 'Och anfaller de två målen.'),
      (tg - 1.2, 'Avslut först efter konlinjen', 'Konlinjen 15 m från de två målen.'),
      (tg + 0.4, 'Nytt anfall från målvakten', 'Blått försvarar och vill kontra mot det ensamma målet.'),
      (tl - 0.2, 'Blått vinner bollen', 'Orange sätter kontrapress direkt.'),
      (tw - 0.1, 'Snabb återerövring: nytt anfall', 'Vinner blått bollen kontrar de direkt mot det ensamma målet.')]
finish(d, 'f03', '7-mot-7-med-kontrapress-och-tva-mal', ['7 mot 7', 'Med kontrapress och två mål'], 'Halvplan · Ett stort mål och två stora mål · Konlinje 15 m från de två målen',
       fp, 'OMSTÄLLNING', [('cone', x, 74) for x in range(10, 95, 12)])
C[-1]['goals'] = [(50, 0), (28, 100), (72, 100)]; C[-1]['keep_goals'] = True

# ============ w01 Trafikljus ============
d = Drill(); d.p('t', 'T', T_COL, (50, 93))
ST = [(22, 26), (42, 24), (62, 26), (80, 30), (22, 60), (42, 72), (62, 62), (80, 72)]
team(d, 'b', B, ST); BX = [(14, 18, 30, 44), (34, 18, 50, 44), (54, 18, 70, 44), (74, 18, 88, 44),
                          (14, 50, 30, 80), (34, 52, 50, 80), (54, 50, 70, 80), (74, 52, 88, 80)]
balls = [d.newball(rec(d, f'b{k}', 0)) for k in range(8)]
LAST = 5
for k in range(8):
    pid = f'b{k}'
    wander(d, pid, 0, 4.5, BX[k], 700 + k, 1.0)            # grönt: full fart
    wander(d, pid, 4.5, 9, BX[k], 710 + k, 2.0)            # gult: sakta, små touch
    if k == LAST: wander(d, pid, 9, 10.2, BX[k], 720 + k, 0.6)
    stand(d, pid, d.pl[pid]['tr'][-1][0], 13.5)            # rött: sulan på bollen och frys
    wander(d, pid, 13.5, 17.9, BX[k], 730 + k, 1.0)        # grönt igen
    d.carry(balls[k], pid, 0, 17.9)
fp = [(0, 'Grönt: dribbla i full fart', 'Alla har en boll. Tränaren håller upp en färg.'),
      (4.5, 'Gult: sakta, små touch', 'Bollen nära foten.'),
      (9, 'Rött: stoppa med sulan och frys', 'Den som är sist att stanna gör en uppgift.'),
      (10.4, 'Sist att stanna: tio tåtoucher', 'Sedan är spelaren med igen.'),
      (13.5, 'Grönt igen: full fart', 'Tränaren kan också ropa färgen.')]
finish(d, 'w01', 'trafikljus', ['Trafikljus', 'Lek med boll'], 'Ruta med koner · Alla har en boll · Tränaren visar färger',
       fp, 'LEK MED BOLL', [('box', 10, 14, 92, 84)],
       [dict(kind='signal', t0=0, t1=4.5, pos=(50, 93), color=GRN), dict(kind='signal', t0=4.5, t1=9, pos=(50, 93), color=YEL),
        dict(kind='signal', t0=9, t1=13.5, pos=(50, 93), color=RED), dict(kind='signal', t0=13.5, t1=18, pos=(50, 93), color=GRN),
        lab(10.4, 13.4, (ST[LAST][0], 89), '10 TÅTOUCHER')])

# ============ w02 Pirater ============
d = Drill()
ST = [(22, 26), (50, 22), (78, 26), (22, 72), (50, 76), (78, 72)]
team(d, 'b', B, ST); team(d, 'p', R, [(40, 50), (62, 50)], ['P', 'P'])
BX = [(14, 18, 34, 40), (40, 16, 60, 34), (66, 18, 86, 40), (14, 58, 34, 82), (40, 66, 60, 82), (66, 58, 86, 82)]
balls = [d.newball(rec(d, f'b{k}', 0)) for k in range(6)]
# händelse 1: pirat p0 sparkar ut bollen för b0
for k in range(6):
    if k != 0: wander(d, f'b{k}', 0, 3.4 if k == 2 else (9.6 if k == 3 else 17.9), BX[k], 740 + k, 1.6)
d.mv('b0', 0, 2.0, (26, 30)); stand(d, 'b0', 2.0, 2.6)
d.mv('p0', 0.4, 2.4, (30, 32)); d.carry(balls[0], 'b0', 0, 2.5)
t1 = d.pas(balls[0], 2.6, (4, 32), 0.7)                                   # ut ur rutan
d.mv('p0', 2.7, 3.7, (6, 34)); stand(d, 'p0', 3.7, 4.0); d.mv('p0', 4.0, 5.2, (22, 30))   # piraten hämtar bollen
d.carry(balls[0], 'p0', 4.0, 5.2); wander(d, 'p0', 5.2, 17.9, BX[0], 760, 1.6); d.carry(balls[0], 'p0', 5.2, 17.9)
# b0 är nu pirat och jagar b3
stand(d, 'b0', 2.6, 3.6); d.mv('b0', 3.6, 5.6, (36, 58)); d.mv('b0', 5.6, 7.0, (28, 66))
# händelse 2: pirat p1 sparkar ut bollen för b2
d.mv('p1', 0.6, 3.0, (70, 32)); d.mv('b2', 3.4, 4.0, (76, 30)); d.carry(balls[2], 'b2', 0, 4.0)
d.mv('p1', 3.0, 3.9, (72, 32))
t2 = d.pas(balls[2], 4.1, (97, 30), 0.7)
d.mv('p1', 4.2, 5.2, (94, 32)); stand(d, 'p1', 5.2, 5.5); d.mv('p1', 5.5, 6.7, (78, 28))
d.carry(balls[2], 'p1', 5.5, 6.7); wander(d, 'p1', 6.7, 17.9, BX[2], 770, 1.6); d.carry(balls[2], 'p1', 6.7, 17.9)
stand(d, 'b2', 4.0, 4.8); d.mv('b2', 4.8, 7.0, (70, 56)); d.mv('b2', 7.0, 9.4, (56, 70))
# händelse 3: nya piraten b0 sparkar ut bollen för b3
d.mv('b3', 9.6, 10.2, (24, 74)); d.carry(balls[3], 'b3', 0, 10.2)
d.mv('b0', 7.0, 9.8, (28, 72)); stand(d, 'b0', 9.8, 10.3)
t3 = d.pas(balls[3], 10.3, (24, 97), 0.7)
d.mv('b0', 10.4, 11.4, (26, 94)); stand(d, 'b0', 11.4, 11.7); d.mv('b0', 11.7, 12.9, (24, 74))
d.carry(balls[3], 'b0', 11.7, 12.9); wander(d, 'b0', 12.9, 17.9, BX[3], 780, 1.6); d.carry(balls[3], 'b0', 12.9, 17.9)
stand(d, 'b3', 10.2, 11.0); d.mv('b3', 11.0, 13.4, (44, 50)); wander(d, 'b3', 13.4, 17.9, (38, 42, 62, 56), 790, 1.6)
wander(d, 'b2', 9.4, 17.9, (52, 60, 64, 70), 791, 1.8)
for k in (1, 4, 5): d.carry(balls[k], f'b{k}', 0, 17.9)
fp = [(0, 'Alla dribblar med varsin boll', 'Två pirater utan boll står inne i rutan.'),
      (2.4, 'Piraten sparkar ut bollen ur rutan', 'Skydda bollen med kroppen.'),
      (3.7, 'Ny pirat – piraten får bollen', 'Den som blev av med bollen blir pirat.'),
      (9.8, 'Den nya piraten jagar', 'Och sparkar ut nästa boll.'),
      (13, 'Vem har aldrig varit pirat?', 'Räkna efter två minuter.')]
finish(d, 'w02', 'pirater', ['Pirater', 'Lek med boll'], 'Ruta med koner · Alla har boll utom två pirater',
       fp, 'LEK MED BOLL', [('box', 10, 12, 90, 88)],
       [lab(t1 + 0.3, t1 + 2.3, (20, 46), 'NY PIRAT'), lab(t2 + 0.3, t2 + 2.3, (80, 46), 'NY PIRAT'), lab(t3 + 0.3, t3 + 2.3, (40, 88), 'NY PIRAT')])
f = factor(fp); ids = {k: i for i, k in enumerate(d.order)}
swap_color(ids['b0'], (t1 - 0.4) * f, B, R); swap_color(ids['p0'], (t1 - 0.4) * f, R, B)
swap_color(ids['b2'], (t2 - 0.4) * f, B, R); swap_color(ids['p1'], (t2 - 0.4) * f, R, B)
swap_color(ids['b3'], (t3 - 0.4) * f, B, R)
C[-1]['players'][ids['b0']]['color'] = (lambda tt, a=(t1 - 0.4) * f, c=(t3 - 0.4) * f: B if tt < a else (R if tt < c else B))
for i, k in enumerate(d.order): C[-1]['players'][i]['label'] = ''

# ============ w03 Tunnelsvansen ============
d = Drill(); d.p('r', 'F', R, (44, 50))
LOOP = [(50, 90), (50, 10), (24, 10), (24, 90)]
def loop_pos(s):
    L = [((LOOP[i][0] - LOOP[i - 1][0]) ** 2 + (LOOP[i][1] - LOOP[i - 1][1]) ** 2) ** .5 for i in range(1, 4)] + [((LOOP[0][0] - LOOP[3][0]) ** 2 + (LOOP[0][1] - LOOP[3][1]) ** 2) ** .5]
    s %= sum(L); i = 0
    while s > L[i]: s -= L[i]; i += 1
    a, c = LOOP[i], LOOP[(i + 1) % 4]; w = s / L[i]; return (a[0] + (c[0] - a[0]) * w, a[1] + (c[1] - a[1]) * w)
SP = 12; N = 6; OFF = [k * 220 / N for k in range(N)]
balls = []
for k in range(N):
    d.p(f'b{k}', str(k + 1), B, loop_pos(OFF[k])); balls.append(d.newball(rec(d, f'b{k}', 0)))
    tt = 0.0
    while tt < 17.9: tt = round(tt + 0.5, 2); d.mv(f'b{k}', tt - 0.5, tt, loop_pos(OFF[k] - SP * tt) if False else loop_pos(OFF[k] + SP * tt))
    d.carry(balls[k], f'b{k}', 0, 17.9)
# när passerar spelarna stöldzonen (y 42–58 på väg upp i kanalen)?
def cross(k):
    out = []
    for f_ in range(0, 179):
        tt = f_ / 10; x, y = loop_pos(OFF[k] + SP * tt)
        if x == 50 and 49.5 <= y <= 50.7: out.append(tt)
    return out
evts = sorted((tt, k) for k in range(N) for tt in cross(k))
STEAL = {evts[1][1], evts[3][1]}
tprev = 0; steals = []; frees = []
for tt, k in evts:
    if tt - tprev < 0.6: continue
    d.mv('r', max(tprev, tt - 1.0), tt, (45, 50 + (0 if k in STEAL else 4)))
    tprev = tt + 0.2
    if k in STEAL: steals.append((tt, k))
    else: frees.append((tt, k))
tails_off = {k: tt for tt, k in steals}
fp = [(0, 'Dribbla genom kanalen', 'Och tillbaka på utsidan. Alla har en väst som svans.'),
      (steals[0][0] - 0.6, 'Försvararen tar svansar, inte bollen', 'En stulen svans = ett liv mindre.'),
      (frees[1][0] - 0.3 if len(frees) > 1 else 9, 'Igenom kanalen: ett liv tillbaka', 'Alla börjar med fem liv.'),
      (14, 'Byt försvarare efter 60–90 sekunder', 'Håll farten genom stöldzonen.')]
fp.sort(key=lambda x: x[0]); fp[0] = (0,) + fp[0][1:]
ex = [lab(tt, tt + 1.6, (64, 50), '-1 LIV') for tt, k in steals] + [lab(tt + 0.7, tt + 2.0, (64, 34), '+1 LIV') for tt, k in frees if tt > 1]
finish(d, 'w03', 'tunnelsvansen', ['Tunnelsvansen', 'Lek med boll'], 'Smal kanal, dubbelt så lång som bred · Stöldzon i mitten',
       fp, 'LEK MED BOLL', [('box', 38, 20, 62, 80), ('zone', 38, 42, 62, 58, (230, 120, 110), 'STÖLDZON')], ex)
f = factor(fp)
for i, k in enumerate(d.order[1:], start=1):
    kk = int(k[1:]); C[-1]['players'][i]['tails'] = (lambda tt, s=tails_off.get(kk, 99) * f: 1 if tt < s else 0)

# ============ w04 Kungen av ringen ============
d = Drill()
ST = [(36, 30), (64, 30), (26, 50), (74, 50), (36, 70), (64, 70), (50, 44)]
team(d, 'b', B, ST); BX = boxes(ST, 6)
balls = [d.newball(rec(d, f'b{k}', 0)) for k in range(7)]
# händelse 1: b6 petar ut bollen för b1
wander(d, 'b1', 0, 2.4, BX[1], 801, 1.6); d.mv('b6', 0.3, 2.6, (58, 36)); d.carry(balls[6], 'b6', 0, 2.6)
d.carry(balls[1], 'b1', 0, 2.6)
t1 = d.pas(balls[1], 2.8, (78, 6), 0.8)
d.mv('b1', 2.9, 4.2, (80, 8)); stand(d, 'b1', 4.2, 7.2); d.mv('b1', 7.2, 8.6, (64, 30))      # uppgift utanför och tillbaka
d.carry(balls[1], 'b1', 4.2, 8.6); wander(d, 'b1', 8.6, 17.9, BX[1], 802, 1.6); d.carry(balls[1], 'b1', 8.6, 17.9)
wander(d, 'b6', 2.6, 7.0, (44, 38, 56, 52), 803, 1.6); d.carry(balls[6], 'b6', 2.6, 7.0)
# händelse 2: b4 petar ut bollen för b2
wander(d, 'b2', 0, 7.4, BX[2], 804, 1.6); d.carry(balls[2], 'b2', 0, 7.6)
wander(d, 'b4', 0, 5.6, BX[4], 805, 1.6); d.mv('b4', 5.6, 7.6, (30, 58)); d.carry(balls[4], 'b4', 0, 17.9 if False else 7.6)
t2 = d.pas(balls[2], 7.9, (3, 56), 0.8)
d.mv('b2', 8.0, 9.2, (5, 58)); stand(d, 'b2', 9.2, 12.2); d.mv('b2', 12.2, 13.6, (26, 50))
d.carry(balls[2], 'b2', 9.2, 13.6); wander(d, 'b2', 13.6, 17.9, BX[2], 806, 1.6); d.carry(balls[2], 'b2', 13.6, 17.9)
wander(d, 'b4', 7.6, 17.9, BX[4], 807, 1.6); d.carry(balls[4], 'b4', 7.6, 17.9)
wander(d, 'b6', 7.0, 17.9, (44, 38, 56, 52), 808, 1.6); d.carry(balls[6], 'b6', 7.0, 17.9)
for k in (0, 3, 5): wander(d, f'b{k}', 0, 17.9, BX[k], 810 + k, 1.6); d.carry(balls[k], f'b{k}', 0, 17.9)
fp = [(0, 'Alla dribblar inne i ringen', 'Med varsin boll. Skydda din egen boll.'),
      (2.2, 'Peta ut andras bollar ur ytan', 'Utan att tappa din egen.'),
      (4.2, 'Ute: gör en snabb uppgift', 'Till exempel fem jongleringar. Sedan tillbaka in.'),
      (7.6, 'Ny boll petas ut', 'Huvudet upp – se vem som kommer.'),
      (13.6, 'Vem åker ut minst gånger?', 'Räkna efter två minuter.')]
finish(d, 'w04', 'kungen-av-ringen', ['Kungen av ringen', 'Lek med boll'], 'Ruta eller cirkel · Alla har en boll',
       fp, 'LEK MED BOLL', [('circle', 50, 50, 34)],
       [lab(4.3, 7.2, (80, 16), 'UPPGIFT'), lab(9.3, 12.2, (8, 66), 'UPPGIFT')])

# ============ w05 Brokull med boll ============
d = Drill(); d.p('k', 'K', R, (50, 50))
ST = [(22, 26), (46, 22), (74, 26), (22, 52), (78, 52), (24, 78), (50, 80), (76, 78)]
team(d, 'b', B, ST)
bA = d.newball(rec(d, 'b0', 0)); bB = d.newball(rec(d, 'b7', 0))
# kullaren tar b3, b0 passar mellan benen till b5
for k in (1, 2, 4, 6): wander(d, f'b{k}', 0, 17.9, boxes([ST[k]], 7)[0], 820 + k, 1.8)
d.mv('b3', 0, 2.6, (26, 50)); d.mv('k', 0.2, 2.6, (31, 50)); tag1 = 2.6
stand(d, 'b3', tag1, 6.0)
d.mv('b0', 0, 3.2, (24, 36)); d.carry(bA, 'b0', 0, 3.2)
d.mv('b5', 0, 3.2, (24, 66))
t = d.pas(bA, 3.6, (26, 50), 0.4); t = d.pas(bA, t, rec(d, 'b5', t + 0.5), 0.5); fr1 = t - 0.5      # mellan benen
wander(d, 'b3', 6.0, 17.9, boxes([ST[3]], 7)[0], 831, 1.8)
wander(d, 'b0', 3.2, 17.9, boxes([ST[0]], 6)[0], 832, 1.8)
wander(d, 'b5', t, 17.9, boxes([ST[5]], 6)[0], 833, 1.8); d.carry(bA, 'b5', t, 17.9)
# kullaren tar b4, b7 befriar
d.mv('k', 3.0, 6.6, (70, 52)); d.mv('b4', 4.0, 6.6, (76, 52)); tag2 = 6.6
d.mv('b7', 0, 6.8, (76, 66)); d.carry(bB, 'b7', 0, 7.2)
d.mv('b2', 7.0, 7.6, (76, 38))
t = d.pas(bB, 7.4, (76, 52), 0.4); t = d.pas(bB, t, rec(d, 'b2', t + 0.5), 0.5); fr2 = t - 0.5
wander(d, 'b4', 9.0, 17.9, boxes([ST[4]], 7)[0], 834, 1.8)
wander(d, 'b7', 7.2, 17.9, boxes([ST[7]], 6)[0], 835, 1.8)
d.mv('b2', t, t + 1.4, (64, 28)); d.carry(bB, 'b2', t, t + 1.4); wander(d, 'b2', t + 1.4, 17.9, boxes([ST[2]], 6)[0], 836, 1.8); d.carry(bB, 'b2', t + 1.4, 17.9)
stand(d, 'b4', tag2, 9.0)
d.mv('k', 7.0, 10.0, (52, 50)); stand(d, 'k', 10, 11); d.mv('k', 11, 12.4, (50, 64)); tsw = 12.4    # byt kullare
d.mv('b6', 11, 12.4, (50, 72)); stand(d, 'k', 12.4, 13); d.mv('k', 13, 15.4, (40, 40)); d.mv('b6', 13, 17.9, (66, 60))
fp = [(0, 'Kullaren jagar', 'Några dribblar med boll. En boll per par.'),
      (tag1, 'Kullad: stå bredbent', 'Vänta på hjälp från en lagkamrat.'),
      (fr1 - 0.3, 'Bollen mellan benen = fri', 'Lagkamraten passar igenom till en medspelare.'),
      (tag2, 'Ny kullad – ny befrielse', 'Lyft blicken och se vem som behöver hjälp.'),
      (tsw - 0.4, 'Byt kullare varje minut', 'Den nya kullaren jagar direkt.')]
finish(d, 'w05', 'brokull-med-boll', ['Brokull med boll', 'Lek med boll'], 'Ruta · En kullare · En boll per par',
       fp, 'LEK MED BOLL', [('box', 10, 12, 90, 90)],
       [lab(tag1, fr1, (26, 42), 'BREDBENT'), lab(fr1, fr1 + 1.6, (26, 42), 'FRI'),
        lab(tag2, fr2, (76, 44), 'BREDBENT'), lab(fr2, fr2 + 1.6, (76, 44), 'FRI')])
f = factor(fp); ids = {k: i for i, k in enumerate(d.order)}
swap_color(ids['k'], tsw * f, R, B); swap_color(ids['b6'], tsw * f, B, R)
C[-1]['players'][ids['k']]['label'] = ''; C[-1]['players'][ids['b6']]['label'] = ''

# ============ passa-och-följ-motor (w07, w08, w09) ============
def rotation(d, b, spots, queue, order, reps, t, passes, after=None):
    """spots: hörn -> position. queue: hörn -> lista med spelare (först = aktiv).
    passes: lista med (från-hörn, till-hörn, typ). Varje spelare följer sin passning till nästa hörn i 'order'."""
    for r in range(reps):
        t = passes(d, b, spots, queue, t)
    return t

# ============ w07 Passningsfyrkant med väggspel ============
d = Drill()
SP7 = {'A': (24, 80), 'B': (24, 22), 'C': (76, 22), 'D': (76, 80)}
QOFF = {'A': (-4, 6), 'B': (-4, -6), 'C': (4, -6), 'D': (4, 6)}
def qpos(c, n): x, y = SP7[c]; ox, oy = QOFF[c]; return (x + ox * n, y + oy * n)
Q = {'A': ['a0', 'a1', 'a2'], 'B': ['bb'], 'C': ['cc'], 'D': ['dd']}
for c, ps in Q.items():
    for n, pid in enumerate(ps): d.p(pid, c, B, qpos(c, n))
b = d.newball(rec(d, 'a0', 0)); t = 0.4; reps = []
def joinq(pid, c, t0, t1):
    Q[c].append(pid); d.mv(pid, t0, t1, qpos(c, len(Q[c]) - 1))
for r in range(2):
    a = Q['A'].pop(0); bp = Q['B'].pop(0); cp = Q['C'].pop(0); dp = Q['D'].pop(0)
    d.mv(bp, t, t + 0.6, (24, 38))                                               # B kommer emot
    t1 = d.pas(b, t + 0.1, rec(d, bp, t + 0.7)); t2 = d.pas(b, t1 + 0.15, rec(d, a, t1 + 0.6))   # lägger tillbaka
    joinq(bp, 'C', t2 + 0.1, t2 + 2.4)
    t3 = d.pas(b, t2 + 0.25, rec(d, cp, t2 + 1.6)); reps.append(t3)              # djupt till C
    joinq(a, 'B', t3 - 0.6, t3 + 2.2)
    t4 = d.pas(b, t3 + 0.25, rec(d, dp, t3 + 1.3)); joinq(cp, 'D', t4 - 0.4, t4 + 2.2)
    for n, pid in enumerate(Q['A']): d.mv(pid, t3, t3 + 0.8, qpos('A', n))
    t5 = d.pas(b, t4 + 0.25, rec(d, Q['A'][0], t4 + 1.3)); joinq(dp, 'A', t5 - 0.4, t5 + 2.0)
    t = t5 + 0.3
fp = [(0, 'A spelar på B som kommer emot', 'B lägger tillbaka direkt.'),
      (reps[0] - 1.2, 'A slår djupt till C', 'C spelar vidare till D.'),
      (reps[0] + 1.3, 'D spelar tillbaka till A-kön', 'Alla följer sin passning till nästa hörn.'),
      (reps[1] - 2.4, 'Nytt varv från A', 'Samma mönster: väggspel, djupt, vidare.')]
finish(d, 'w07', 'passningsfyrkant-med-vaggspel', ['Passningsfyrkant', 'Med väggspel'], 'Kvadrat 15 × 15 m · En spelare vid varje hörn · Kö och bollar vid A',
       fp, 'PASSNINGSÖVNING', [('cone',) + v for v in SP7.values()])

# ============ w08 Passa och följ i triangel ============
d = Drill()
SP8 = {0: (50, 20), 1: (80, 74), 2: (20, 74)}
QO8 = {0: (0, -6), 1: (5, 4), 2: (-5, 4)}
def q8(c, n): x, y = SP8[c]; ox, oy = QO8[c]; return (x + ox * n, y + oy * n)
Q = {0: ['p0', 'p3'], 1: ['p1'], 2: ['p2']}
for c, ps in Q.items():
    for n, pid in enumerate(ps): d.p(pid, str(int(pid[1]) + 1), B, q8(c, n))
b = d.newball(rec(d, 'p0', 0)); t = 0.4; dirs = []; c = 0
for k in range(8):
    step = 1 if k < 4 else -1
    if k == 4: dirs.append(t)
    nc = (c + step) % 3
    pas_ = Q[c].pop(0); recv = Q[nc][0]
    t2 = d.pas(b, t + 0.3, rec(d, recv, t + 1.0))
    Q[nc].append(pas_); d.mv(pas_, t + 0.4, t + 2.4, q8(nc, len(Q[nc]) - 1))     # följ passningen
    for n, pid in enumerate(Q[c]): d.mv(pid, t + 0.6, t + 1.2, q8(c, n))
    t = t2; c = nc
fp = [(0, 'Passa och följ din passning', 'Spring efter bollen till nästa kon.'),
      (2.5, 'Extraspelaren väntar i kön', 'Kliv fram och ta emot med rätt fot.'),
      (dirs[0] - 0.3, 'Byt håll', 'Byt håll varannan minut.'),
      (dirs[0] + 2.5, 'Samma sak åt andra hållet', 'Passa i rätt tempo till mottagaren.')]
finish(d, 'w08', 'passa-och-folj-i-triangel', ['Passa och följ', 'I triangel'], 'Triangel med koner · 10–12 m mellan · En extra spelare vid start',
       fp, 'PASSNINGSÖVNING', [('cone',) + v for v in SP8.values()], [lab(dirs[0], dirs[0] + 1.8, (50, 50), 'BYT HÅLL')])

# ============ w09 Tredje man i romb ============
d = Drill()
SP9 = {'A': (50, 84), 'B': (22, 50), 'C': (78, 50), 'D': (50, 16)}
QO9 = {'A': (0, 6), 'B': (-6, 0), 'C': (6, 0), 'D': (0, -6)}
def q9(c, n): x, y = SP9[c]; ox, oy = QO9[c]; return (x + ox * n, y + oy * n)
Q = {'A': ['a0', 'a1'], 'B': ['bb'], 'C': ['cc'], 'D': ['dd']}
for c, ps in Q.items():
    for n, pid in enumerate(ps): d.p(pid, c, B, q9(c, n))
b = d.newball(rec(d, 'a0', 0)); t = 0.4; marks = []
for r in range(2):
    a = Q['A'].pop(0); bp = Q['B'].pop(0); cp = Q['C'].pop(0); dp = Q['D'].pop(0)
    d.mv(bp, t, t + 0.7, (32, 60))                                               # B kommer emot
    t1 = d.pas(b, t + 0.15, rec(d, bp, t + 0.7))
    t2 = d.pas(b, t1 + 0.1, rec(d, cp, t1 + 0.9)); marks.append(t2)              # direkt till tredje man
    t3 = d.pas(b, t2 + 0.2, rec(d, dp, t2 + 1.2))                                # djupt till D
    Q['B'].append(a); d.mv(a, t1, t1 + 2.0, q9('B', 0))
    Q['C'].append(bp); d.mv(bp, t1 + 0.3, t1 + 2.6, q9('C', 0) if not Q['C'][:-1] else q9('C', 1))
    Q['D'].append(cp); d.mv(cp, t3 - 0.3, t3 + 1.8, q9('D', 0) if False else (50, 22))
    for n, pid in enumerate(Q['A']): d.mv(pid, t1, t1 + 0.8, q9('A', n))
    d.mv(dp, t3, t3 + 0.5, (50, 20)); tdr = drive(d, b, dp, t3 + 0.5, (52, 76), 20)   # D vänder och driver tillbaka
    Q['A'].append(dp); d.mv(dp, tdr, tdr + 0.6, q9('A', len(Q['A']) - 1)); d.carry(b, dp, tdr, tdr + 0.6)
    d.mv(cp, tdr - 0.6, tdr + 0.2, q9('D', 0))
    nxt = Q['A'][0]; t = d.pas(b, tdr + 0.7, rec(d, nxt, tdr + 1.2), 0.4) if nxt != dp else tdr + 0.6
fp = [(0, 'A spelar till B som kommer emot', 'B lägger av direkt.'),
      (marks[0] - 0.6, 'Till C – tredje man', 'C slår djupt till D.'),
      (marks[0] + 1.4, 'D vänder och driver tillbaka', 'Alla roterar en kon.'),
      (marks[1] - 2.0, 'Nytt varv från A', 'Spela på rätt fot och med rätt tempo.')]
finish(d, 'w09', 'tredje-man-i-romb', ['Tredje man', 'I romb'], 'Romb med fyra koner, A, B, C och D · Kö vid A',
       fp, 'PASSNINGSÖVNING', [('cone',) + v for v in SP9.values()])

# ============ w10 Långa passningar över mittzonen ============
d = Drill()
team(d, 'u', B, [(40, 14), (60, 14)]); team(d, 'n', B, [(40, 86), (60, 86)]); d.p('s', 'S', R, (50, 50))
b = d.newball(rec(d, 'u0', 0)); t = 0.4; cnt = []; DIST = ['s']
def lob(pid_from, pid_to, t):
    d.mv(DIST[0], t - 0.2, t + 0.6, (at(d.pl[pid_to]['tr'], t)[0] * 0.6 + 50 * 0.4, 50))   # störaren försöker
    t2 = d.pas(b, t + 0.2, rec(d, pid_to, t + 1.6), 1.4); cnt.append(t2); return t2
t = lob('u0', 'n0', t); t = d.pas(b, t + 0.2, rec(d, 'n1', t + 0.8))                   # ett touch ner, sedan vidare
t = lob('n1', 'u1', t + 0.2); t = d.pas(b, t + 0.2, rec(d, 'u0', t + 0.8))
t = lob('u0', 'n1', t + 0.2); tsw = t + 0.3
d.mv('u0', tsw, tsw + 1.8, (44, 50)); d.mv('s', tsw, tsw + 1.8, (30, 14)); DIST[0] = 'u0'   # störaren byter rad
t = d.pas(b, tsw + 0.2, rec(d, 'n0', tsw + 0.8)); t = lob('n0', 'u1', t + 1.2); t = d.pas(b, t + 0.2, rec(d, 's', t + 0.8))
t = lob('s', 'n0', t + 0.2)
fp = [(0, 'Långa passningar i luften', 'Över mittzonen till paret i andra änden.'),
      (cnt[0] - 0.4, 'Ta ner bollen med ett touch', 'Sedan en kort passning till kompisen.'),
      (cnt[1] - 0.6, 'Störaren försöker bryta', 'Slå passningen högt över mittzonen.'),
      (tsw, 'Efter tre passningar: byt störare', 'Störaren byter rad med en spelare.'),
      (tsw + 2.6, 'Ny störare i mittzonen', 'Samma sak igen.')]
finish(d, 'w10', 'langa-passningar-over-mittzonen', ['Långa passningar', 'Över mittzonen'], 'Två par ca 30 m isär · Mittzon med en störande spelare',
       fp, 'PASSNINGSÖVNING', [('zone', 10, 38, 90, 62, (230, 120, 110), 'MITTZON'), ('cone', 30, 8), ('cone', 70, 8), ('cone', 30, 92), ('cone', 70, 92)],
       counter(cnt[:3], pos=(84, 30), last='BYTE'))
f = factor(fp); ids = {k: i for i, k in enumerate(d.order)}
swap_color(ids['u0'], (tsw + 0.9) * f, B, R); swap_color(ids['s'], (tsw + 0.9) * f, R, B)
C[-1]['players'][ids['u0']]['label'] = ''; C[-1]['players'][ids['s']]['label'] = ''

if __name__ == '__main__': render(C, sys.argv)
