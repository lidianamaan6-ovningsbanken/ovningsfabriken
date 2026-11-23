# Externa övningar, omgång 7 (tolv st). Regel: först d.mv, sedan d.carry; hide före show.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e4', __file__.replace('render_extern7.py', 'render_extern4.py'))
e4 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e4); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e4.finish, e4.rec, e4.chain, e4.wander, e4.counter, e4.arrivals
lab, hide, show, team, boxes, drive, shoot = e4.lab, e4.hide, e4.show, e4.team, e4.boxes, e4.drive, e4.shoot
factor, swap_color, stand = e4.factor, e4.swap_color, e4.stand
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'

# ============ w41 5 mot 2 – vinn bollen inom sex passningar ============
d = Drill(); RP = [(32, 34), (50, 26), (68, 34), (64, 66), (36, 66)]
team(d, 'b', B, RP); team(d, 'r', R, [(44, 46), (56, 54)])
b = d.newball(rec(d, 'b0', 0))
d.mv('r0', 0.3, 3, (44, 40)); d.mv('r1', 0.3, 3, (58, 46))
t = chain(d, b, 0.4, ['b1', 'b2', 'b3', 'b4', 'b0', 'b1'], 0.2); cnt = arrivals(d, b)[:6]; tp = cnt[-1]
d.mv('r0', t - 1.2, t + 0.2, (54, 36)); d.mv('r1', t - 1.2, t + 0.2, (62, 42))
t0 = t + 0.4; cnt2 = []
t = d.pas(b, t0, rec(d, 'b2', t0 + 0.6)); cnt2.append(t); t = d.pas(b, t + 0.2, rec(d, 'b3', t + 0.8)); cnt2.append(t)
d.mv('r1', t - 0.9, t + 0.2, rec(d, 'b3', t + 0.2)); d.mv('r0', t - 0.9, t + 0.2, (56, 56)); tw = d.pas(b, t + 0.3, rec(d, 'r1', t + 0.5), 0.3)   # vinner inom sex
d.mv('r1', tw + 0.3, tw + 1.6, RP[3]); d.mv('b3', tw + 0.3, tw + 1.6, (52, 52)); d.mv('r0', tw + 0.3, tw + 1.6, RP[2]); d.mv('b2', tw + 0.3, tw + 1.6, (46, 44))   # byter in
t = chain(d, b, tw + 1.7, ['b4', 'b0', 'b1', 'r0'], 0.25)
fp = [(0, 'Fem håller bollen, två pressar', 'Försvararna ska vinna bollen inom sex passningar.'),
      (tp - 0.3, 'Sex passningar: poäng till laget', 'Spelet fortsätter direkt.'),
      (tw - 0.3, 'Försvararna vinner bollen i tid', 'De byter in sig – två går in i mitten.'),
      (tw + 1.7, 'Nya försvarare pressar', 'Pressa tillsammans och stäng passningsvägar.')]
finish(d, 'w41', '5-mot-2-vinn-bollen-inom-sex-passningar', ['5 mot 2', 'Vinn bollen inom sex passningar'], 'Rondo · Fem anfallare och två försvarare',
       fp, 'RONDO', [('box', 26, 20, 74, 80)], counter(cnt, pos=(50, 12)) + counter(cnt2, pos=(50, 12), last=None) + [lab(tw, tw + 1.6, (50, 88), 'BYTER IN')])

# ============ w42 6 mot 4 med kontring genom konportar ============
d = Drill()
BP = [(30, 30), (50, 26), (70, 30), (70, 66), (50, 72), (30, 66)]; RP = [(42, 40), (58, 42), (42, 58), (58, 58)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
for k in range(4): wander(d, f'r{k}', 0, 4.2, boxes([RP[k]], 4)[0], 1000 + k, 1.6)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b1', 'b2', 'b3', 'b4'], 0.25)
d.mv('r3', t - 1.0, t + 0.2, rec(d, 'b4', t + 0.2)); tw = d.pas(b, t + 0.3, rec(d, 'r3', t + 0.5), 0.3)   # de fyra vinner bollen
t = d.pas(b, tw + 0.2, rec(d, 'r1', tw + 0.9))
d.mv('r1', t, t + 1.8, (88, 50)); d.carry(b, 'r1', t, t + 1.8); tg = t + 1.4                              # kontra genom yttre konport
for k, ps in [(4, (56, 62)), (3, (66, 56)), (2, (74, 42))]: d.mv(f'b{k}', tw, tw + 1.4, ps)                # motpress direkt
d.mv('b3', tw + 1.4, t + 1.6, (80, 52)); d.mv('b2', tw + 1.4, t + 1.6, (82, 44))
d.mv('r3', tw + 0.3, tw + 1.4, (60, 60)); d.mv('r0', tw, tw + 1.6, (54, 44)); d.mv('r2', tw, tw + 1.6, (46, 60))
fp = [(0, 'Sex håller bollen mot fyra', 'Ruta 20 × 20 m.'),
      (tw - 0.3, 'De fyra vinner bollen', 'Nu ska de kontra genom en yttre konport.'),
      (tw + 0.4, 'Laget med sex motpressar direkt', 'Stäng vägen till portarna.'),
      (tg - 0.2, 'Genom porten: poäng', 'Portarna står 3 m utanför rutan.')]
finish(d, 'w42', '6-mot-4-med-kontring-genom-konportar', ['6 mot 4', 'Med kontring genom konportar'], 'Ruta ca 20 × 20 m · Fyra konportar 3 m utanför',
       fp, 'RONDO', [('box', 22, 18, 78, 82)] + [('cone', 50 + dx, 8) for dx in (-4, 4)] + [('cone', 50 + dx, 92) for dx in (-4, 4)] + [('cone', 10, 50 + dy) for dy in (-4, 4)] + [('cone', 90, 50 + dy) for dy in (-4, 4)],
       [lab(tg, tg + 1.8, (88, 38), '+1')])

# ============ w43 Från 3 mot 5 till 7 mot 5 ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
BP = [(34, 42), (50, 40), (66, 44), (62, 58), (38, 58)]; PP = [(44, 48), (56, 50), (50, 56)]; WP = [(6, 30), (6, 60), (94, 30), (94, 60)]
team(d, 'b', B, BP); team(d, 'r', R, PP); team(d, 'w', R, WP, ['4', '5', '6', '7'])
b = d.newball(rec(d, 'b0', 0))
for k in range(3): wander(d, f'r{k}', 0, 4.0, boxes([PP[k]], 4)[0], 1010 + k, 1.6)
t = chain(d, b, 0.4, ['b1', 'b2', 'b3', 'b4'], 0.25)
d.mv('r2', t - 1.0, t + 0.2, rec(d, 'b4', t + 0.2)); tw = d.pas(b, t + 0.3, rec(d, 'r2', t + 0.5), 0.3)   # pressarna vinner bollen
for k, ps in enumerate([(22, 22), (40, 14), (62, 14), (80, 24)]): d.mv(f'w{k}', tw, tw + 2.0, ps)            # lagkamraterna kommer in: 7 mot 5
d.mv('r0', tw, tw + 1.6, (36, 30)); d.mv('r1', tw, tw + 1.6, (60, 30))
for k, ps in enumerate([(30, 26), (48, 22), (64, 22), (58, 38), (42, 38)]): d.mv(f'b{k}', tw + 0.3, tw + 2.2, ps)
t = d.pas(b, tw + 0.4, rec(d, 'r0', tw + 1.2)); t = d.pas(b, t + 0.2, rec(d, 'w1', t + 0.9)); t = d.pas(b, t + 0.2, rec(d, 'w2', t + 0.8))
d.mv('b2', t - 0.9, t + 0.2, rec(d, 'w2', t + 0.2)); tb = d.pas(b, t + 0.3, rec(d, 'b2', t + 0.5), 0.3)  # femlaget vinner tillbaka
t = drive(d, b, 'b2', tb, (62, 74), 24); t = d.pas(b, t + 0.1, rec(d, 'b3', t + 0.8))
d.mv('b3', tb, t, (46, 80)); tg = shoot(d, b, t + 0.05, (30, 95))
d.mv('w2', tb, tb + 2.4, (60, 62)); d.mv('r1', tb, tb + 2.4, (48, 66))
fp = [(0, 'Fem håller bollen i mittzonen', 'Tre pressare. Fyra lagkamrater väntar utanför.'),
      (tw - 0.3, 'Pressarna vinner bollen', 'Nu blir det 7 mot 5 på hela planen.'),
      (tw + 1.0, 'Anfall mot det stora målet', 'Lagkamraterna kommer in direkt.'),
      (tb - 0.2, 'Femlaget vinner tillbaka bollen', 'Och anfaller småmålen.')]
finish(d, 'w43', 'fran-3-mot-5-till-7-mot-5', ['Från 3 mot 5', 'Till 7 mot 5'], 'Plan ca 40 × 30 m · Mittzon 20 × 15 m · Stort mål och småmål',
       fp, 'SPELÖVNING', [('zone', 26, 34, 74, 66, (200, 220, 200), 'MITTZON'), ('smallgoal', 30, 96), ('smallgoal', 70, 96)])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ w47 1 mot 1: styr anfallaren bort från mål ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
for z, x in (('l', 30), ('r', 70)):
    d.p(f'p{z}', 'P', WHITE, (x, 86)); d.p(f'a{z}', 'A', B, (x, 66)); d.p(f'd{z}', 'F', R, (x, 40))
bl = d.newball(rec(d, 'pl', 0)); br = d.newball(rec(d, 'pr', 0))
# vänster zon: försvararen styr ut anfallaren, avslut från dålig vinkel
t = d.pas(bl, 0.4, rec(d, 'al', 1.2)); d.mv('dl', 0.4, 1.4, (32, 52))
t = drive(d, bl, 'al', t, (36, 56), 14); d.mv('dl', t - 0.6, t + 1.4, (28, 46))
d.mv('al', t, t + 1.4, (20, 40)); d.carry(bl, 'al', t, t + 1.4); t += 1.4                       # styrs bort från mål
tg = shoot(d, bl, t + 0.1, (46, 2)); ts = tg
d.mv('al', tg + 0.3, tg + 2.4, (30, 40)); d.mv('dl', tg + 0.3, tg + 2.4, (36, 86)); d.mv('pl', tg + 0.3, tg + 2.4, (30, 66))   # rotera
# höger zon: försvararen vinner bollen och spelar i småmålet
t0 = 3.4; t = d.pas(br, t0, rec(d, 'ar', t0 + 0.8)); d.mv('dr', t0, t0 + 1.0, (70, 52))
t = drive(d, br, 'ar', t, (72, 56), 14); d.mv('dr', t - 0.4, t + 0.4, rec(d, 'ar', t + 0.4))
tw = d.pas(br, t + 0.45, rec(d, 'dr', t + 0.7), 0.3); tg2 = d.pas(br, tw + 0.3, (70, 31), 0.6)      # in i småmålet
d.mv('ar', tw, tw + 1.0, (66, 50)); hide(d, br, tg2 + 0.3)
d.mv('ar', tg2 + 0.4, tg2 + 2.4, (70, 40)); d.mv('dr', tg2 + 0.4, tg2 + 2.4, (64, 86)); d.mv('pr', tg2 + 0.4, tg2 + 2.4, (70, 66))
fp = [(0, 'Passaren spelar till anfallaren', 'Försvararen kliver ut samtidigt.'),
      (1.8, 'Styr anfallaren bort från mål', 'Ställ dig snett och visa ut mot kanten.'),
      (tw - 0.2, 'Försvararen vinner bollen', 'Och spelar in i småmålet.'),
      (tg2 + 0.4, 'Rotera efter varje försök', 'Passare, anfallare och försvarare byter plats.')]
finish(d, 'w47', '1-mot-1-styr-anfallaren-bort-fran-mal', ['1 mot 1', 'Styr anfallaren bort från mål'], 'Mål med målvakt · Zoner 10 × 10 m · Småmål bakom försvararen',
       fp, 'DUELL', [('box', 16, 32, 44, 60), ('box', 56, 32, 84, 60), ('smallgoal', 30, 31), ('smallgoal', 70, 31)],
       [lab(tg2, tg2 + 1.6, (82, 26), '+1')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ w48 1 mot 2: försvara i underläge ============
d = Drill()
d.p('p0', 'P', WHITE, (46, 90)); d.p('p1', 'P', WHITE, (54, 90)); team(d, 'a', B, [(32, 66), (68, 66)]); d.p('f', 'F', R, (50, 50))
b1 = d.newball(rec(d, 'p0', 0)); b2 = d.newball(rec(d, 'p1', 0))
t = d.pas(b1, 0.4, rec(d, 'a0', 1.3))                                                     # till vänster kant
d.mv('f', t - 0.4, t + 0.6, (44, 40))                                                    # väntar och fördröjer
d.mv('a1', 0.8, t + 1.2, (60, 46)); t = drive(d, b1, 'a0', t, (40, 46), 14)
t = d.pas(b1, t + 0.1, rec(d, 'a1', t + 0.7)); d.mv('f', t - 0.6, t + 0.4, (54, 34))
d.mv('a1', t, t + 0.6, (56, 30)); d.carry(b1, 'a1', t, t + 0.6); tg = shoot(d, b1, t + 0.6, (50, 13))
hide(d, b1, tg + 0.4)
d.mv('a0', tg, tg + 2.0, (32, 66)); d.mv('a1', tg, tg + 2.0, (68, 66)); d.mv('f', tg, tg + 1.6, (50, 50))
t0 = tg + 1.6; t = d.pas(b2, t0, rec(d, 'a1', t0 + 0.9))                                  # till höger kant
d.mv('f', t0 + 0.2, t + 0.3, rec(d, 'a1', t + 0.3))                                       # pressar direkt
tw = d.pas(b2, t + 0.35, rec(d, 'f', t + 0.6), 0.3); d.mv('f', tw, tw + 1.2, (56, 74)); d.carry(b2, 'f', tw, tw + 1.2)
d.mv('a0', t0 + 0.4, t + 0.4, (46, 54))
fp = [(0, 'Passaren spelar till en av kanterna', 'Två anfallare mot en försvarare.'),
      (1.3, 'Försvararen väntar', 'Fördröj och ta bort passningen.'),
      (tg - 0.6, 'Anfallarna gör mål i småmålet', 'Rotera efter varje försök.'),
      (t0 + 0.4, 'Försvararen pressar', 'Rätt läge att gå på bollen – och vinner den.')]
finish(d, 'w48', '1-mot-2-forsvara-i-underlage', ['1 mot 2', 'Försvara i underläge'], 'Yta 20 × 10 m · Småmål i ena änden · Startkon i andra',
       fp, 'DUELL', [('box', 30, 12, 70, 88), ('smallgoal', 50, 12), ('cone', 50, 84), ('cone', 28, 66), ('cone', 72, 66), ('line', [(30, 50), (70, 50)])],
       [lab(1.3, 3.0, (50, 58), 'VÄNTA'), lab(t0 + 0.4, t0 + 2.0, (50, 58), 'PRESSA')])

# ============ w49 Press och täckning 2 mot 2 ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
team(d, 'a', B, [(40, 64), (62, 62)]); team(d, 'f', R, [(42, 32), (58, 30)])
b = d.newball(rec(d, 'a0', 0))
t = drive(d, b, 'a0', 0.4, (42, 50), 14); d.mv('f0', 0.6, t, (42, 42)); d.mv('f1', 0.6, t, (50, 34))   # press och täckning snett bakom
d.mv('a1', 0.6, t, (62, 48))
t = d.pas(b, t + 0.2, rec(d, 'a1', t + 0.9)); tsh = t
d.mv('f1', tsh - 0.6, tsh + 0.4, (60, 40)); d.mv('f0', tsh - 0.4, tsh + 0.6, (52, 34))             # rollbyte: ny press, ny täckning
t = drive(d, b, 'a1', t, (60, 44), 12)
d.mv('f1', t - 0.2, t + 0.3, rec(d, 'a1', t + 0.3)); tw = d.pas(b, t + 0.35, rec(d, 'f1', t + 0.6), 0.3)   # vinner bollen
t = drive(d, b, 'f1', tw, (66, 82), 24); tg = shoot(d, b, t, (70, 93)); hide(d, b, tg + 0.3)            # kontring mot småmål
d.mv('f0', tw, tw + 2, (48, 72)); d.mv('a1', tw, tw + 1.8, (60, 66)); d.mv('a0', tw, tw + 1.8, (52, 60))
fp = [(0, 'Anfallarna startar 20 m ut', 'Två mot två mot mål med målvakt.'),
      (0.8, 'Närmaste försvarare pressar', 'Den andra täcker snett bakom.'),
      (tsh - 0.2, 'Bollen flyttas – byt roller', 'Ny press på bollen, ny täckning.'),
      (tw - 0.2, 'Försvararna vinner bollen', 'Och kontrar mot småmålen.')]
finish(d, 'w49', 'press-och-tackning-2-mot-2', ['Press och täckning', '2 mot 2'], 'Mål med målvakt · Två anfallare mot två försvarare · Två småmål för kontring',
       fp, 'DUELL', [('smallgoal', 30, 94), ('smallgoal', 70, 94)],
       [lab(0.8, tsh, (30, 42), 'PRESS'), lab(0.8, tsh, (50, 26), 'TÄCK'), lab(tsh, tw, (70, 40), 'PRESS'), lab(tsh, tw, (46, 28), 'TÄCK')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ w50 Försvara inlägg 4 mot 3 ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
team(d, 'y', B, [(88, 40), (12, 40)], ['Y', 'Y']); AP = [(40, 32), (52, 34), (62, 30)]; DP = [(36, 22), (46, 22), (56, 22), (64, 20)]
team(d, 'a', B, AP); team(d, 'f', R, DP)
b1 = d.newball(rec(d, 'y0', 0)); b2 = d.newball(rec(d, 'y1', 0))
t = drive(d, b1, 'y0', 0.4, (88, 12), 22)
for k, ps in enumerate([(44, 10), (54, 8), (60, 14)]): d.mv(f'a{k}', 0.6, t + 0.4, ps)
for k, ps in enumerate([(40, 10), (48, 8), (56, 9), (62, 12)]): d.mv(f'f{k}', 0.8, t + 0.4, ps)     # faller med löpningarna
t = d.pas(b1, t + 0.1, rec(d, 'f2', t + 1.0), 0.9); tc = d.pas(b1, t + 0.05, (64, 40), 0.7); hide(d, b1, tc + 0.3)   # rensning ut ur boxen
for k in range(3): d.mv(f'a{k}', tc, tc + 2.0, AP[k])
for k in range(4): d.mv(f'f{k}', tc, tc + 2.0, DP[k])
d.mv('y0', tc, tc + 2.0, (88, 40))
t = drive(d, b2, 'y1', tc + 0.6, (12, 12), 22)
for k, ps in enumerate([(56, 10), (46, 8), (38, 14)]): d.mv(f'a{k}', tc + 1.0, t + 0.4, ps)
for k, ps in enumerate([(38, 10), (46, 11), (54, 8), (62, 12)]): d.mv(f'f{k}', tc + 1.2, t + 0.4, ps)
t = d.pas(b2, t + 0.1, rec(d, 'a2', t + 1.0), 0.9); tg = shoot(d, b2, t + 0.05, (46, 1))                  # mål
fp = [(0, 'Yttern driver och slår in', 'Fyra försvarare mot tre anfallare i boxen.'),
      (1.4, 'Fall med löpningarna', 'Försvararna följer sina anfallare mot mål.'),
      (tc - 0.3, 'Rensning ut ur boxen: 1 poäng', 'Rensa högt och brett.'),
      (tg - 0.6, 'Mål ger anfallarna två poäng', 'Yttrarna turas om.')]
finish(d, 'w50', 'forsvara-inlagg-4-mot-3', ['Försvara inlägg', '4 mot 3'], 'Straffområde med målvakt · Fyra försvarare, tre anfallare · En ytter på varje kant',
       fp, 'FÖRSVAR', [], [lab(tc, tc + 1.6, (64, 48), '+1 FÖRSVAR'), lab(tg, tg + 1.8, (46, 16), '+2')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ w51 Backlinjen: kliv upp och fall ============
d = Drill(); d.p('mv', 'MV', R, (50, 4)); d.p('t', 'T', T_COL, (50, 66))
DP = [(26, 34), (42, 32), (58, 32), (74, 34)]; team(d, 'f', R, DP); team(d, 'a', B, [(36, 42), (64, 42)])
b = d.newball(rec(d, 't', 0))
for k in range(4): d.mv(f'f{k}', 0.6, 2.4, (DP[k][0], DP[k][1] - 10))                          # bollen fri: linjen faller
d.mv('a0', 0.6, 2.4, (36, 30)); d.mv('a1', 0.6, 2.4, (64, 30))
d.mv('a1', 2.6, 3.6, (66, 14)); t = d.pas(b, 2.8, (64, 12), 1.0); d.mv('f3', 2.8, 3.8, (66, 13))    # djupledsboll
tw = 3.8; d.mv('f3', tw, tw + 1.2, (60, 30)); d.carry(b, 'f3', tw, tw + 1.2); t = d.pas(b, tw + 1.3, rec(d, 't', tw + 2.4))
for k in range(4): d.mv(f'f{k}', tw + 1.4, tw + 3.2, (DP[k][0], DP[k][1] + 6))                 # pressad boll: linjen kliver upp
d.mv('a0', tw + 1.4, tw + 3.0, (38, 44)); d.mv('a1', tw + 1.4, tw + 3.0, (62, 44))
tp = tw + 2.4
for k in range(4): d.mv(f'f{k}', tp + 1.8, tp + 3.4, (DP[k][0], DP[k][1] - 10))                 # fri igen: fall
d.mv('a0', tp + 2.0, tp + 3.4, (40, 26)); d.mv('a0', tp + 3.4, tp + 4.0, (40, 14))
t = d.pas(b, tp + 3.4, (40, 12), 0.9); d.mv('f1', tp + 3.2, tp + 4.2, (41, 13)); tw2 = tp + 4.3
d.mv('f1', tw2, tw2 + 1.0, (44, 26)); d.carry(b, 'f1', tw2, tw2 + 1.0)
fp = [(0, 'Bollen är fri: linjen faller', 'Tillsammans – ingen släpper löparen bakom sig.'),
      (tw - 0.2, 'Djupledsbollen vinns: 1 poäng', 'Försvararna får en poäng för varje vunnen djupledsboll.'),
      (tw + 1.4, 'Bollen är pressad: linjen kliver upp', 'Prata och flytta som en linje.'),
      (tp + 1.8, 'Fri igen: fall tillsammans', 'Läs tränarens boll – pressad eller fri.')]
finish(d, 'w51', 'backlinjen-kliv-upp-och-fall', ['Backlinjen', 'Kliv upp och fall'], 'Halvplan med mål och målvakt · Fyra försvarare, två anfallare · Tränaren med bollar',
       fp, 'FÖRSVAR', [],
       [lab(0.4, 2.6, (50, 74), 'FRI'), lab(tw, tw + 1.6, (66, 24), '+1'), lab(tw + 1.4, tp + 1.8, (50, 74), 'PRESSAD'), lab(tp + 1.8, tp + 3.6, (50, 74), 'FRI'), lab(tw2, tw2 + 1.6, (40, 34), '+1')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ fs1 Hörna 1 – närstolpe och flick ============
d = Drill(); d.p('mv', 'MV', R, (50, 4)); d.p('h', 'H', B, (98, 2))
AP = [(48, 20), (52, 21), (49, 24), (53, 25)]; team(d, 'a', B, AP); DP = [(42, 9), (48, 8), (54, 8), (60, 9)]; team(d, 'f', R, DP)
b = d.newball(rec(d, 'h', 0))
tsig = 0.4
for k, ps in enumerate([(58, 8), (42, 7), (50, 18), (50, 32)]): d.mv(f'a{k}', 1.4, 2.8, ps)     # främre, bakre, straffpunkt, kanten
t = d.pas(b, 2.2, rec(d, 'a0', 3.0), 0.8); t = d.pas(b, t + 0.05, rec(d, 'a1', t + 0.6), 0.5)       # flick vidare
tg = shoot(d, b, t + 0.05, (46, 1))
for k, ps in enumerate([(56, 9), (44, 8), (50, 12), (60, 10)]): d.mv(f'f{k}', 2.0, 3.0, ps)
for k in range(4): d.mv(f'a{k}', tg + 0.4, tg + 2.6, AP[k])
for k in range(4): d.mv(f'f{k}', tg + 0.4, tg + 2.6, DP[k])
b2 = d.newball((200, 200)); show(d, b2, tg + 2.7, rec(d, 'h', tg + 2.7))
for k, ps in enumerate([(58, 8), (42, 7), (50, 18), (50, 32)]): d.mv(f'a{k}', tg + 3.6, tg + 5.0, ps)
t = d.pas(b2, tg + 4.4, rec(d, 'a0', tg + 5.2), 0.8); t = d.pas(b2, t + 0.05, rec(d, 'a1', t + 0.6), 0.5); tg2 = shoot(d, b2, t + 0.05, (46, 1))
fp = [(0, 'Signal från hörnläggaren', 'Handen upp. Fyra löpare samlade vid straffpunkten.'),
      (1.4, 'Första löparen till främre stolpen', 'De andra fyller bakre stolpen, straffpunkten och kanten.'),
      (tg - 0.8, 'Flick vidare – mål: 2 poäng', 'Mål på flick eller retur ger 2 poäng.'),
      (tg + 2.7, 'Ny hörna, samma mönster', 'Försvararna står i zon med målvakt.')]
finish(d, 'fs1', 'horna-1-narstolpe-och-flick', ['Hörna 1', 'Närstolpe och flick'], 'Hörna från höger · Fyra löpare vid straffpunkten · Fyra försvarare i zon',
       fp, 'FAST SITUATION', [], [lab(tsig, 2.0, (92, 10), 'HANDEN UPP'), lab(tg, tg + 1.8, (46, 16), '+2'), lab(tg2, tg2 + 1.8, (46, 16), '+2')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ fs2 Hörna 2 – kort hörna och inlägg ============
d = Drill(); d.p('mv', 'MV', R, (50, 4)); d.p('h', 'H', B, (98, 2)); d.p('k', 'K', B, (84, 18))
AP = [(42, 26), (52, 28), (60, 24)]; team(d, 'a', B, AP); DP = [(42, 9), (50, 8), (58, 9)]; team(d, 'f', R, DP)
b = d.newball(rec(d, 'h', 0))
d.mv('k', 0.3, 1.2, (92, 6)); t = d.pas(b, 1.0, rec(d, 'k', 1.5))                                   # kort pass
d.mv('h', t, t + 0.8, (90, 12)); t = d.pas(b, t + 0.1, rec(d, 'h', t + 0.8))                        # tillbaka till hörnläggaren
d.mv('h', t, t + 0.8, (82, 14)); d.carry(b, 'h', t, t + 0.8); t += 0.8                              # närmare mål
for k, ps in enumerate([(56, 8), (46, 10), (40, 16)]): d.mv(f'a{k}', t - 1.0, t + 0.6, ps)
t = d.pas(b, t + 0.1, rec(d, 'a1', t + 0.8), 0.7); tg = shoot(d, b, t + 0.05, (52, 1))
for k, ps in enumerate([(54, 10), (46, 9), (42, 12)]): d.mv(f'f{k}', t - 1.2, t, ps)
for k in range(3): d.mv(f'a{k}', tg + 0.4, tg + 2.4, AP[k]); d.mv(f'f{k}', tg + 0.4, tg + 2.4, DP[k])
d.mv('h', tg + 0.4, tg + 2.4, (98, 2)); d.mv('k', tg + 0.4, tg + 2.4, (84, 18))
b2 = d.newball((200, 200)); show(d, b2, tg + 2.5, rec(d, 'h', tg + 2.5))
d.mv('k', tg + 2.7, tg + 3.6, (92, 6)); t = d.pas(b2, tg + 3.4, rec(d, 'k', tg + 3.9))
for k, ps in enumerate([(70, 14), (68, 20), (72, 24)]): d.mv(f'f{k}', t - 0.4, t + 0.8, ps)      # försvaret kliver ut för tidigt
t = d.pas(b2, t + 0.3, rec(d, 'a1', t + 1.1)); d.mv('a1', t - 1.0, t, (54, 14)); tg2 = shoot(d, b2, t + 0.05, (48, 1))
fp = [(0, 'Kort hörna till spelaren som kommer emot', 'Tre löpare i straffområdet.'),
      (1.6, 'Tillbaka till hörnläggaren', 'Som slår inlägg från en ny vinkel, närmare mål.'),
      (tg - 0.6, 'Avslut på inlägget', 'Försvararna står i zon.'),
      (tg + 3.8, 'Försvaret kliver ut för tidigt', 'Spela inspel längs marken eller skjut.')]
finish(d, 'fs2', 'horna-2-kort-horna-och-inlagg', ['Hörna 2', 'Kort hörna och inlägg'], 'Kort hörna till en spelare som kommer emot · Inlägg från ny vinkel',
       fp, 'FAST SITUATION', [])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ fs3 Hörna 3 – bakre stolpen och nick tillbaka ============
d = Drill(); d.p('mv', 'MV', R, (50, 4)); d.p('h', 'H', B, (98, 2))
d.p('l', 'L', B, (22, 30)); team(d, 'n', B, [(60, 20), (64, 22)]); d.p('s', 'S', B, (50, 32))
DP = [(40, 10), (50, 9), (58, 14), (64, 16)]; team(d, 'f', R, DP)
b = d.newball(rec(d, 'h', 0))
d.mv('n0', 0.6, 1.8, (58, 8)); d.mv('n1', 0.6, 1.8, (62, 10)); d.mv('f2', 0.8, 2.0, (56, 10)); d.mv('f3', 0.8, 2.0, (60, 12))   # drar med sig försvarare
d.mv('l', 0.8, 2.6, (38, 9)); d.mv('f0', 1.6, 2.6, (42, 12))
t = d.pas(b, 1.4, rec(d, 'l', 2.6), 1.2)                                                            # hög hörna till bakre stolpen
d.mv('s', 1.8, t + 0.7, (52, 14)); d.mv('f1', t - 0.4, t + 0.6, (46, 9)); t = d.pas(b, t + 0.05, rec(d, 's', t + 0.6), 0.55)               # nick tillbaka, sen löpare
tg = shoot(d, b, t + 0.05, (52, 1)); tn = t
fp = [(0, 'Två löpare drar med sig försvarare', 'Mot främre stolpen.'),
      (1.4, 'Hörnan högt mot bakre stolpen', 'Den längsta spelaren startar utanför straffområdet.'),
      (tn - 0.6, 'Nick tillbaka in i målområdet', 'En löpare kommer sent i mitten.'),
      (tg + 0.2, 'Mål på andra bollen: 2 poäng', 'Tajma den sena löpningen.')]
finish(d, 'fs3', 'horna-3-bakre-stolpen-och-nick-tillbaka', ['Hörna 3', 'Bakre stolpen och nick tillbaka'], 'Hög hörna till bakre stolpen · Nick tillbaka in i målområdet',
       fp, 'FAST SITUATION', [], [lab(tg, tg + 1.8, (50, 18), '+2')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ fs4 Hörnförsvar – zon och två markerare ============
d = Drill(); d.p('mv', 'MV', R, (50, 4)); d.p('h', 'H', B, (98, 2))
ZP = [(40, 9), (47, 9), (54, 9), (61, 9)]; team(d, 'z', R, ZP); team(d, 'm', R, [(46, 20), (56, 22)]); d.p('np', 'F', R, (60, 4))
team(d, 'a', B, [(48, 24), (58, 26), (40, 28), (52, 34)])
b = d.newball(rec(d, 'h', 0))
for k, ps in enumerate([(46, 13), (56, 15), (42, 18), (52, 26)]): d.mv(f'a{k}', 0.8, 2.4, ps)
d.mv('m0', 0.8, 2.4, (46, 15)); d.mv('m1', 0.8, 2.4, (56, 17))                                    # markerar man mot man
t = d.pas(b, 1.6, rec(d, 'z1', 2.6), 1.0); tc = d.pas(b, t + 0.05, (62, 42), 0.8)                   # zonförsvarare rensar
d.mv('m1', t, tc + 0.4, (62, 40)); d.carry(b, 'm1', tc + 0.1, tc + 0.4)
t = drive(d, b, 'm1', tc + 0.4, (54, 70), 22); t = d.pas(b, t + 0.1, (50, 93), 0.9); tk = t; hide(d, b, tk + 0.3)        # kontring till konen
d.mv('m0', tc, tc + 2.6, (42, 64))
for k, ps in enumerate([(52, 40), (60, 50), (44, 34), (54, 56)]): d.mv(f'a{k}', tc, tc + 2.6, ps)
fp = [(0, 'Fyra i zon, två markerare', 'Och en vid främre stolpen.'),
      (1.6, 'Hörnan slås in', 'Zonen äger ytan, markerarna följer sina spelare.'),
      (tc - 0.4, 'Rensa förbi kanten av straffområdet', '1 poäng till försvarslaget.'),
      (tc + 0.6, 'Kontra till konen vid mittlinjen', '2 poäng.')]
finish(d, 'fs4', 'hornforsvar-zon-och-tva-markerare', ['Hörnförsvar', 'Zon och två markerare'], 'Fyra i zon i målområdet · Två markerar de farligaste nickspelarna',
       fp, 'FAST SITUATION', [('cone', 50, 94)], [lab(tc, tc + 1.6, (62, 48), '+1'), lab(tk, tk + 1.8, (50, 86), '+2')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

if __name__ == '__main__': render(C, sys.argv)
