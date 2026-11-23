# Externa övningar, omgång 10 (tolv st). Regel: först d.mv, sedan d.carry; först mottagarens rörelse, sedan passningen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e9', __file__.replace('render_extern10.py', 'render_extern9.py'))
e9 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e9); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e9.finish, e9.rec, e9.chain, e9.wander, e9.counter, e9.arrivals
lab, hide, show, team, boxes, drive, shoot = e9.lab, e9.hide, e9.show, e9.team, e9.boxes, e9.drive, e9.shoot
factor, swap_color, stand, countdown, countup, win = e9.factor, e9.swap_color, e9.stand, e9.countdown, e9.countup, e9.win
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'

# ============ fa2 Blockera skottet ============
d = Drill(); d.p('mv', 'MV', R, (50, 4)); d.p('f', 'F', R, (50, 40))
team(d, 'a', B, [(50, 84), (44, 90)])
b1 = d.newball(rec(d, 'a0', 0)); b2 = d.newball(rec(d, 'a1', 0))
t = drive(d, b1, 'a0', 0.4, (54, 44), 18); d.mv('f', 1.4, t + 0.3, (52, 36))
tb = d.pas(b1, t + 0.1, (52, 38), 0.2); t = d.pas(b1, tb, (84, 30), 0.7); hide(d, b1, t + 0.2)        # blockerat skott
d.mv('a0', tb + 0.3, tb + 2.6, (58, 92)); d.mv('f', tb + 0.3, tb + 1.6, (50, 40))
d.mv('a1', tb, tb + 1.2, (50, 84)); d.carry(b2, 'a1', tb, tb + 1.2)
t = drive(d, b2, 'a1', tb + 1.4, (46, 50), 18); d.mv('f', t - 0.6, t + 0.2, rec(d, 'a1', t + 0.2))
tw = d.pas(b2, t + 0.3, rec(d, 'f', t + 0.5), 0.3); d.mv('f', tw, tw + 1.2, (40, 60)); d.carry(b2, 'f', tw, tw + 1.2)   # bollvinst
fp = [(0, 'En anfallare med boll mot en försvarare', 'Anfallaren ska avsluta.'),
      (tb - 0.5, 'Blockera skottet: 1 poäng', 'Kroppen bakom bollen, händerna bakom ryggen.'),
      (tb + 1.4, 'Nästa anfallare', ''),
      (tw - 0.2, 'Bollvinst: 2 poäng', '')]
finish(d, 'fa2', 'blockera-skottet', ['Blockera', 'skottet'], 'Kanal 20 × 15 m mot mål med målvakt',
       fp, 'DUELL', [('box', 22, 2, 78, 96)], [lab(tb, tb + 1.6, (64, 40), '+1'), lab(tw, tw + 1.6, (40, 50), '+2')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ fa3 Försvara straffområdet 4 mot 4 ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
team(d, 'y', WHITE, [(90, 22), (10, 22)], ['I', 'I'])
AP = [(36, 30), (46, 32), (56, 30), (64, 34)]; DP = [(38, 18), (46, 16), (54, 16), (62, 18)]
team(d, 'a', B, AP); team(d, 'f', R, DP)
b1 = d.newball(rec(d, 'y0', 0)); b2 = d.newball(rec(d, 'y1', 0))
for k, ps in enumerate([(40, 12), (48, 9), (56, 11), (62, 16)]): d.mv(f'a{k}', 0.6, 2.2, ps)
for k, ps in enumerate([(42, 10), (50, 8), (58, 9), (60, 13)]): d.mv(f'f{k}', 0.8, 2.2, ps)
t = d.pas(b1, 1.4, rec(d, 'f2', 2.4), 1.0); tc = d.pas(b1, t + 0.05, (70, 44), 0.7); hide(d, b1, tc + 0.3)   # rensning
for k in range(4): d.mv(f'a{k}', tc, tc + 2.0, AP[k]); d.mv(f'f{k}', tc, tc + 2.0, DP[k])
for k, ps in enumerate([(60, 12), (50, 9), (42, 11), (36, 16)]): d.mv(f'a{k}', tc + 2.0, tc + 3.6, ps)
for k, ps in enumerate([(58, 10), (50, 7), (42, 9), (38, 13)]): d.mv(f'f{k}', tc + 2.2, tc + 3.6, ps)
t = d.pas(b2, tc + 2.8, rec(d, 'f2', tc + 3.8), 1.0); tc2 = d.pas(b2, t + 0.05, (28, 44), 0.7); hide(d, b2, tc2 + 0.3)
fp = [(0, 'Fyra mot fyra i straffområdet', 'En inläggsspelare på varje kant.'),
      (1.4, 'Inlägg från höger', 'Försvararna följer sina spelare och möter bollen.'),
      (tc - 0.4, 'Rensning ut ur straffområdet: 1 poäng', ''),
      (tc + 2.8, 'Inlägg från vänster', 'Inläggen slås i tur och ordning.')]
finish(d, 'fa3', 'forsvara-straffomradet-4-mot-4', ['Försvara straffområdet', '4 mot 4'], 'Straffområdet · Två inläggszoner på kanterna',
       fp, 'FÖRSVAR', [('zone', 80, 6, 100, 40, (200, 220, 200), ''), ('zone', 0, 6, 20, 40, (200, 220, 200), '')],
       [lab(tc, tc + 1.6, (70, 50), '+1'), lab(tc2, tc2 + 1.6, (28, 50), '+1')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ fa4 Kom tillbaka: inspel 2 mot 2 ============
d = Drill(); d.p('mv', 'MV', R, (50, 4)); d.p('w', 'K', WHITE, (90, 46))
team(d, 'a', B, [(48, 40), (60, 44)]); d.p('f0', 'F', R, (54, 30)); d.p('f1', 'F', R, (20, 24))
b = d.newball(rec(d, 'w', 0))
t = drive(d, b, 'w', 0.4, (88, 16), 20)
d.mv('a0', 0.8, t + 0.6, (52, 10)); d.mv('a1', 0.8, t + 0.6, (60, 18)); d.mv('f0', 1.0, t + 0.6, (58, 14))
d.mv('f1', 0.6, t + 0.6, (48, 10))                                                                 # kommer tillbaka från konen
d.mv('f1', t + 0.6, t + 1.0, (50, 10)); tw = d.pas(b, t + 0.1, rec(d, 'f1', t + 1.0), 0.9)           # stoppar inspelet
d.mv('f1', tw, tw + 1.2, (40, 26)); d.carry(b, 'f1', tw, tw + 1.2)
fp = [(0, 'Bollen spelas in från kanten', 'Två anfallare mot två försvarare.'),
      (0.6, 'Kom tillbaka!', 'Försvararen vid konen sprintar hem.'),
      (tw - 0.4, 'Stoppa inspelet', 'Möt bollen före anfallaren.'),
      (tw + 0.2, 'Bollvinst: 1 poäng', '')]
finish(d, 'fa4', 'kom-tillbaka-inspel-2-mot-2', ['Kom tillbaka', 'Inspel 2 mot 2'], 'Halv plan · Mål med målvakt · Kon vid sidan av straffområdet',
       fp, 'DUELL', [('cone', 20, 28)], [lab(tw, tw + 1.6, (40, 34), '+1')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ ae2 Vinn tillbaka på sex sekunder ============
d = Drill()
BP = [(20, 26), (78, 24), (22, 74), (78, 74), (50, 52)]; RP = [(40, 36), (60, 34), (36, 62), (62, 64), (50, 26)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
for k in range(5): wander(d, f'r{k}', 0, 5.0, boxes([RP[k]], 4)[0], 1400 + k, 1.6)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b1', 'b4', 'b3', 'b2', 'b0'], 0.25); cnt = arrivals(d, b)[:5]
t = d.pas(b, t + 0.3, rec(d, 'b1', t + 1.2)) if False else t
tl = win(d, b, 'r4', 'b0', t + 0.4); t = d.pas(b, tl + 0.3, rec(d, 'r1', tl + 1.0))                     # förlust
d.mv('b4', tl, t + 0.2, (52, 42)); d.mv('b1', tl, t + 0.2, (70, 28))
tw = win(d, b, 'b1', 'r1', t + 0.6, 0.6)
t = d.pas(b, tw + 0.3, rec(d, 'b3', tw + 1.1)); t = chain(d, b, t, ['b2'], 0.3)
fp = [(0, 'Fem mot fem', 'Fem passningar ger 1 poäng.'),
      (cnt[-1] - 0.3, 'Fem passningar: 1 poäng', ''),
      (tl - 0.2, 'Bollförlust', 'Vinn tillbaka inom sex sekunder.'),
      (tw - 0.2, 'Tillbaka inom sex sekunder: 2 poäng', '')]
finish(d, 'ae2', 'vinn-tillbaka-pa-sex-sekunder', ['Vinn tillbaka', 'på sex sekunder'], 'Ruta 25 × 25 m · Fem mot fem',
       fp, 'POSITIONSSPEL', [('box', 10, 14, 90, 86)], counter(cnt, pos=(50, 8)) + countup(tl + 0.1, 3, (88, 50), (tw - tl) / 3) + [lab(tw, tw + 1.8, (70, 18), '+2')])

# ============ ae3 Tjuvar och bönder ============
d = Drill()
team(d, 'b', B, [(20, 30), (20, 50), (20, 70)], ['B', 'B', 'B']); team(d, 't', R, [(66, 26), (64, 52), (68, 74)], ['T', 'T', 'T'])
balls = [d.newball(p) for p in [(10, 34), (12, 46), (10, 58), (12, 70)]]
# tjuv 0 tar en boll och dribblar hem
d.mv('t0', 0.4, 2.4, (12, 34)); t = 2.5; d.mv('t0', t, t + 3.2, (88, 30)); d.carry(balls[0], 't0', t, t + 3.2); th = t + 3.2   # hem
d.mv('b0', 1.6, th - 0.2, (80, 34))
# tjuv 1 tar en boll men bonden tar tillbaka den
d.mv('t1', 0.8, 2.8, (14, 48)); d.mv('t1', 2.9, 4.6, (40, 50)); d.carry(balls[1], 't1', 2.9, 4.6)
d.mv('b1', 2.6, 4.6, (42, 54)); tw = d.pas(balls[1], 4.8, rec(d, 'b1', 5.0), 0.3)                      # bonden tar tillbaka
d.mv('t1', 4.8, 6.2, (56, 46)); d.mv('b1', 5.0, 6.6, (16, 48)); d.carry(balls[1], 'b1', 5.0, 6.6)
# tjuv 2 tar en boll och kommer hem
d.mv('t2', 1.6, 3.8, (14, 70)); d.mv('t2', 3.9, 7.9, (88, 72)); d.carry(balls[3], 't2', 3.9, 7.9); th2 = 7.9
d.mv('b2', 3.4, 7.2, (80, 68))
for pid, ps in [('t0', (66, 26)), ('t1', (64, 52)), ('t2', (68, 74)), ('b0', (20, 30)), ('b2', (20, 70))]: d.mv(pid, 8.2, 10.2, ps)
d.mv('b1', 8.2, 10.2, (20, 50))
fp = [(0, 'Bönderna har bollar i sitt hem', 'Tjuvarna försöker ta dem.'),
      (2.5, 'Dribbla in bollen till tjuvarnas hem', ''),
      (tw - 0.2, 'Bonden tar tillbaka bollen', 'Innan tjuven är hemma.'),
      (8.2, 'Byt roller', 'Räkna bollarna i tjuvarnas hem.')]
finish(d, 'ae3', 'tjuvar-och-bonder', ['Tjuvar och', 'bönder'], 'Ruta 25 × 25 m · Ett hem för varje lag',
       fp, 'LEK MED BOLL', [('box', 4, 14, 96, 86), ('zone', 4, 14, 18, 86, (120, 170, 230), 'BÖNDER'), ('zone', 82, 14, 96, 86, (230, 120, 110), 'TJUVAR')],
       [lab(th, th + 1.6, (89, 22), '+1'), lab(th2, th2 + 1.6, (89, 64), '+1')])

# ============ sd01 Spelbredd och speldjup – passningskedja ============
d = Drill()
P = {'A': (50, 82), 'B': (20, 62), 'C': (80, 62), 'D': (38, 36), 'E': (64, 18)}
for k, ps in P.items(): d.p(k, k, B, ps)
b = d.newball(rec(d, 'A', 0))
seq = ['B', 'C', 'A', 'D', 'E', 'D', 'A', 'C', 'B', 'A']
t = 0.4; marks = []
for k in seq:
    x, y = P[k]; d.mv(k, t, t + 0.5, (x + (50 - x) * 0.08, y + (50 - y) * 0.08))                      # kliv mot bollen
    t = d.pas(b, t + 0.2, rec(d, k, t + 0.9)); marks.append(t); d.mv(k, t + 0.2, t + 0.8, P[k]); t += 0.15
fp = [(0, 'A – B – C – A', 'Bollen går i bredd först.'),
      (marks[2], 'A – D – E', 'Sedan i djupled.'),
      (marks[4], 'Vänd tillbaka från E', 'Bollen spelas både framåt och bakåt i kedjan.'),
      (marks[8], 'Byt plats efter några varv', 'Kliv mot bollen när den kommer.')]
finish(d, 'sd01', 'spelbredd-och-speldjup-passningskedja', ['Spelbredd och speldjup', 'Passningskedja'], 'Yta 30 × 20 m · Fem spelare A–E',
       fp, 'PASSNINGSÖVNING', [('box', 10, 8, 90, 92)])
for pl in C[-1]['players']: pass

# ============ sd02 Bredd och djup i två banor ============
d = Drill(); marks = []
for sx, names, pre in ((-1, ['X1', 'X2', 'X3', 'X7'], 'l'), (1, ['X4', 'X5', 'X6', 'X8'], 'r')):
    S = {'1': (50 + sx * 22, 88), '2': (50 + sx * 40, 62), '3': (50 + sx * 20, 46), '7': (50 + sx * 30, 16)}
    Q7 = (50 + sx * 30, 8)
    for k, nm in zip(('1', '2', '3', '7'), names): d.p(pre + k, nm, B, S[k])
    d.p(pre + 'q', names[3], B, Q7)
    role = {'1': pre + '1', '2': pre + '2', '3': pre + '3', '7': [pre + '7', pre + 'q']}
    b = d.newball(rec(d, role['1'], 0)); t = 0.4 + (0.3 if sx > 0 else 0)
    for rep in range(2):
        p1, p2, p3, (p7, p7b) = role['1'], role['2'], role['3'], role['7']
        d.mv(p2, t, t + 0.6, (S['2'][0] - sx * 4, S['2'][1] + 4)); t = d.pas(b, t + 0.1, rec(d, p2, t + 1.0))
        t = d.pas(b, t + 0.2, rec(d, p3, t + 0.9)); t3 = d.pas(b, t + 0.2, rec(d, p7, t + 1.4))
        if sx < 0: marks.append(t3)
        d.mv(p2, t, t + 1.8, S['1'])                                    # X2 till X1
        d.mv(p1, t - 0.4, t3 + 1.0, S['3'])                             # X1 till X3
        d.mv(p3, t + 0.2, t3 + 1.6, Q7)                                 # X3 bakom X7
        d.mv(p7b, t3 + 0.6, t3 + 1.4, S['7'])
        t = d.pas(b, t3 + 0.3, rec(d, p2, t3 + 1.8), 1.4)               # tillbaka till nya X1
        d.mv(p7, t3 + 0.5, t3 + 3.0, S['2'])                            # X7 fyller på
        role = {'1': p2, '2': p7, '3': p1, '7': [p7b, p3]}; t += 0.3
fp = [(0, 'Två banor körs parallellt', 'Samma mönster spegelvänt på andra sidan.'),
      (1.2, 'Bredd först, sedan djup', 'X1 till X2, X3 och vidare djupt.'),
      (marks[0] - 0.4, 'Rotation efter passningen', 'X2 till X1, X1 vidare och X3 bakom X7.'),
      (marks[1] - 1.2, 'Nytt varv', 'Passa på rätt fot – i spelriktningen.')]
finish(d, 'sd02', 'bredd-och-djup-i-tva-banor', ['Bredd och djup', 'I två banor'], 'Yta 45 × 30 m · Åtta stationer · Två banor parallellt',
       fp, 'PASSNINGSÖVNING', [('line', [(50, 4), (50, 96)])])

# ============ sd03 3 mot 1 – spelbarhet och spelavstånd ============
d = Drill()
CR = [(20, 34), (80, 34), (80, 66), (20, 66)]; occ = {0: 'a', 1: 'c', 3: 'e'}
for ci, pid in occ.items(): d.p(pid, '', B, CR[ci])
d.p('m', '', R, (50, 50))
b = d.newball(rec(d, 'a', 0)); h = 0; t = 0.4; marks = []
for q in [1, 2, 3, 0, 1, 2]:
    others = [c for c in occ if c not in (h, q)]; free = [c for c in range(4) if c not in occ][0]
    d.mv(occ[others[0]], t + 0.2, t + 1.4, CR[free]); occ[free] = occ.pop(others[0])
    d.mv('m', t, t + 1.0, ((CR[q][0] + 50) / 2, (CR[q][1] + 50) / 2))
    t = d.pas(b, t + 0.25, rec(d, occ[q], t + 1.05)); marks.append(t); h = q
nxt = [c for c in occ if c != h and abs(c - h) % 2 == 1][0]
d.mv('m', t - 0.2, t + 0.6, rec(d, occ[nxt], t + 0.7)); tw = d.pas(b, t + 0.3, rec(d, 'm', t + 0.8), 0.5)     # brytning
loser = occ[h]; d.mv(loser, tw + 0.3, tw + 1.6, (50, 50)); d.mv('m', tw + 0.3, tw + 1.6, CR[h]); occ[h] = 'm'   # byt försvarare
t = d.pas(b, tw + 1.7, rec(d, occ[nxt], tw + 2.5)); t = d.pas(b, t + 0.2, rec(d, 'm', t + 1.0))
fp = [(0, 'Tre håller bollen mot en', 'Yta 12 × 8 m.'),
      (marks[0], 'Spelbarhet', 'Den utan boll flyttar så att två passningsvägar finns.'),
      (marks[3], 'Rätt spelavstånd', 'Inte för nära – då hinner försvararen ta båda.'),
      (tw - 0.2, 'Brytning – byt försvarare', 'Eller efter en bestämd tid.')]
finish(d, 'sd03', '3-mot-1-spelbarhet-och-spelavstand', ['3 mot 1', 'Spelbarhet och spelavstånd'], 'Yta 12 × 8 m · Tre anfallare mot en försvarare',
       fp, 'RONDO', [('box', 14, 28, 86, 72)])
f = factor(fp); ids = {k: i for i, k in enumerate(d.order)}
swap_color(ids[loser], (tw + 0.9) * f, B, R); swap_color(ids['m'], (tw + 0.9) * f, R, B)

# ============ sd04 4 mot 2 i nio delytor ============
d = Drill()
X = [12, 37, 63, 88]; Y = [24, 41, 59, 76]
cell = lambda i, j: ((X[i] + X[i + 1]) / 2, (Y[j] + Y[j + 1]) / 2)
team(d, 'b', B, [cell(0, 0), cell(2, 0), cell(2, 2), cell(0, 2)]); team(d, 'r', R, [(44, 46), (58, 54)])
b = d.newball(rec(d, 'b0', 0))
moves = [('b1', cell(1, 0)), ('b2', cell(2, 1)), ('b3', cell(1, 2)), ('b0', cell(0, 1))]
t = 0.4; seq = ['b1', 'b2', 'b3', 'b0', 'b1', 'b2']
for n, pid in enumerate(seq):
    if n in (2, 4):
        mv_pid, ps = moves[n // 2 - 1]; d.mv(mv_pid, t, t + 1.0, ps)
    d.mv('r0', t, t + 0.9, ((at(d.pl[pid]['tr'], t + 0.9)[0] + 50) / 2, (at(d.pl[pid]['tr'], t + 0.9)[1] + 50) / 2))
    t = d.pas(b, t + 0.25, rec(d, pid, t + 0.95))
d.mv('r1', t - 0.8, t + 0.2, rec(d, 'b2', t + 0.2)); tw = d.pas(b, t + 0.3, rec(d, 'r1', t + 0.6), 0.4)   # brytning
d.mv('r1', tw + 0.3, tw + 1.6, cell(2, 0)); d.mv('b2', tw + 0.3, tw + 1.6, (54, 50))
t = d.pas(b, tw + 1.7, rec(d, 'b3', tw + 2.5)); t = chain(d, b, t, ['b0', 'r1'], 0.3)
fp = [(0, 'Fyra mot två i nio rutor', 'Anfallarna står i olika rutor.'),
      (2.2, 'Flytta till en ny ruta', 'Aldrig två anfallare i samma ruta.'),
      (tw - 0.2, 'Brytning – byt roller', 'Den som tappade går in.'),
      (tw + 1.7, 'Spelet fortsätter', 'Eller byt efter en bestämd tid.')]
finish(d, 'sd04', '4-mot-2-i-nio-delytor', ['4 mot 2', 'I nio delytor'], 'Yta 12 × 9 m i nio rutor på 4 × 3 m',
       fp, 'RONDO', [('box', 12, 24, 88, 76), ('line', [(37, 24), (37, 76)]), ('line', [(63, 24), (63, 76)]), ('line', [(12, 41), (88, 41)]), ('line', [(12, 59), (88, 59)])])
f = factor(fp); ids = {k: i for i, k in enumerate(d.order)}
swap_color(ids['b2'], (tw + 0.9) * f, B, R); swap_color(ids['r1'], (tw + 0.9) * f, R, B)

# ============ sd05 4 mot 4 + 3 väggar, byt yta ============
d = Drill()
BP = [(26, 60), (74, 62), (40, 80), (62, 78)]; RP = [(38, 66), (60, 68), (32, 76), (52, 86)]
team(d, 'b', B, BP); team(d, 'r', R, RP); d.p('vk', 'V', YEL, (50, 6)); team(d, 'vl', YEL, [(8, 70), (92, 70)], ['V', 'V'])
for k in range(4): wander(d, f'r{k}', 0, 4.6, boxes([RP[k]], 3)[0], 1500 + k, 1.6)
b = d.newball(rec(d, 'b2', 0))
t = chain(d, b, 0.4, ['b0', 'vl0', 'b3', 'b1'], 0.3); cnt = arrivals(d, b)[:4]
d.mv('vk', t - 0.6, t + 0.4, (50, 10)); t = d.pas(b, t + 0.2, rec(d, 'vk', t + 1.6), 1.4); tsw = t      # väggen på motsatt kortsida
NB = [(28, 22), (72, 24), (40, 40), (60, 38)]; NR = [(38, 28), (58, 30), (34, 42), (52, 46)]
for k in range(4): d.mv(f'b{k}', tsw - 1.0, tsw + 1.6, NB[k]); d.mv(f'r{k}', tsw - 0.8, tsw + 1.8, NR[k])
d.mv('vl0', tsw - 0.6, tsw + 1.6, (8, 30)); d.mv('vl1', tsw - 0.6, tsw + 1.6, (92, 30))                  # väggarna följer med
t = d.pas(b, tsw + 0.6, rec(d, 'b0', tsw + 1.6)); d.mv('vk', tsw + 0.8, tsw + 4.6, (50, 94))
t = chain(d, b, t, ['b2', 'vl1', 'b1'], 0.3)
fp = [(0, 'Fyra mot fyra i ena halvan', 'Tre väggar: en på kortsidan och två på långsidorna.'),
      (cnt[-1] - 0.3, 'Fyra passningar – hitta väggen', 'På motsatt kortsida.'),
      (tsw - 0.2, 'Spelet byter yta', 'Långsidesväggarna följer med i djupled.'),
      (tsw + 1.6, 'Samma sak i nya halvan', 'Nu åt andra hållet.')]
finish(d, 'sd05', '4-mot-4-plus-3-vaggar-byt-yta', ['4 mot 4 + 3 väggar', 'Byt yta'], 'Yta 40 × 30 m i två halvor · Tre väggspelare',
       fp, 'POSITIONSSPEL', [('box', 14, 12, 86, 88), ('line', [(14, 50), (86, 50)])], counter(cnt, pos=(88, 92), last=None))

# ============ sd06 Fyra konmål med joker ============
d = Drill()
BP = [(28, 70), (70, 72), (40, 52), (60, 60)]; RP = [(30, 36), (68, 30), (46, 40), (56, 26)]
team(d, 'b', B, BP); team(d, 'r', R, RP); d.p('j', 'J', YEL, (50, 48))
for k in range(4): wander(d, f'r{k}', 0, 4.4, boxes([RP[k]], 3)[0], 1600 + k, 1.6)
wander(d, 'j', 0, 2.2, (46, 44, 54, 52), 1610, 1.4)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b2', 'j', 'b1'], 0.3)
d.mv('b1', t + 0.1, t + 1.6, (72, 20)); d.carry(b, 'b1', t + 0.1, t + 1.6); t += 1.6
d.mv('b3', t - 1.6, t + 0.2, (74, 14)); tg = d.pas(b, t + 0.1, (72, 4), 0.5); hide(d, b, tg + 0.3)        # genom konmålet
b2 = d.newball((200, 200)); show(d, b2, tg + 1.2, rec(d, 'r2', tg + 1.2))
d.mv('j', tg, tg + 1.6, (44, 52)); t = d.pas(b2, tg + 1.4, rec(d, 'j', tg + 2.0)); t = d.pas(b2, t + 0.2, rec(d, 'r0', t + 0.9))
d.mv('r0', t, t + 1.6, (30, 82)); d.carry(b2, 'r0', t, t + 1.6); t += 1.6; tg2 = d.pas(b2, t + 0.1, (28, 96), 0.5); hide(d, b2, tg2 + 0.3)
d.mv('b0', t - 1.6, t, (36, 84))
fp = [(0, 'Fyra mot fyra plus joker', 'Jokern spelar alltid med laget som har bollen.'),
      (2.0, 'Anfall mot två konmål', 'Och försvara två.'),
      (tg - 0.4, 'Mål genom konmålet', 'Välj målet där det är tomt.'),
      (tg + 1.2, 'Nu anfaller rött', 'Jokern byter lag med bollen.')]
finish(d, 'sd06', 'fyra-konmal-med-joker', ['Fyra konmål', 'Med joker'], 'Yta 30 × 30 m · Fyra konmål, två per lag',
       fp, 'SMÅLAGSSPEL', [('box', 8, 6, 92, 94)] + [('cone', x + dx, y) for x in (28, 72) for dx in (-4, 4) for y in (6, 94)],
       [lab(tg, tg + 1.6, (72, 14), '+1'), lab(tg2, tg2 + 1.6, (28, 86), '+1')])

# ============ sd07 3 mot 3 + 2 med mål ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96))
BP = [(30, 62), (70, 60), (50, 44)]; RP = [(36, 34), (64, 32), (52, 58)]; team(d, 'b', B, BP); team(d, 'r', R, RP); team(d, 'j', YEL, [(10, 50), (90, 50)], ['J', 'J'])
for k in range(3): wander(d, f'r{k}', 0, 4.0, boxes([RP[k]], 3)[0], 1700 + k, 1.6)
b = d.newball(rec(d, 'mvb', 0))
t = d.pas(b, 0.4, rec(d, 'b0', 1.2)); t = chain(d, b, t, ['j0', 'b2', 'j1'], 0.3); cnt = arrivals(d, b)[1:4]
d.mv('b1', t - 1.4, t + 0.6, (64, 22)); t = d.pas(b, t + 0.2, rec(d, 'b1', t + 1.0)); tg = shoot(d, b, t + 0.05, (54, 1))
hide(d, b, tg + 0.4)
for k in range(3): d.mv(f'b{k}', tg + 0.2, tg + 2.0, BP[k]); d.mv(f'r{k}', tg + 0.2, tg + 2.0, RP[k])
b2 = d.newball((200, 200)); show(d, b2, tg + 2.0, rec(d, 'mvr', tg + 2.0))
t = d.pas(b2, tg + 2.2, rec(d, 'r0', tg + 3.0)); t = chain(d, b2, t, ['j0', 'r2'], 0.3)
fp = [(0, 'Tre mot tre plus två jokrar', 'Jokrarna spelar med laget som har bollen.'),
      (cnt[0] - 0.3, 'Minst tre passningar innan mål', ''),
      (tg - 0.5, 'Nu får laget göra mål', ''),
      (tg + 2.0, 'Rött startar från målvakten', 'Byt jokrar efter en stund.')]
finish(d, 'sd07', '3-mot-3-plus-2-med-mal', ['3 mot 3 + 2', 'Med mål'], 'Yta 30 × 20 m · Två mål med målvakter',
       fp, 'SMÅLAGSSPEL', [('box', 12, 2, 88, 98)], counter(cnt, pos=(86, 80), last='MÅL OK'))
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

if __name__ == '__main__': render(C, sys.argv)
