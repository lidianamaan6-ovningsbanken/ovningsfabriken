# Externa övningar, omgång 31 (tolv st). Regel: först d.mv, sedan d.carry; först mottagarens rörelse, sedan passningen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e9', __file__.replace('render_extern31.py', 'render_extern9.py'))
e9 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e9); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e9.finish, e9.rec, e9.chain, e9.wander, e9.counter, e9.arrivals
lab, hide, show, team, boxes, drive, shoot = e9.lab, e9.hide, e9.show, e9.team, e9.boxes, e9.drive, e9.shoot
factor, swap_color, stand, countdown, countup, win = e9.factor, e9.swap_color, e9.stand, e9.countdown, e9.countup, e9.win
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'

# ============ sb07 Rondo som blir anfall ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
RING = [(36, 52), (50, 46), (64, 52), (50, 62)]
team(d, 'a', B, RING); team(d, 'f', R, [(42, 24), (58, 24)])
b = d.newball(rec(d, 'a0', 0))
t = chain(d, b, 0.4, ['a1', 'a2', 'a3', 'a0', 'a1'], 0.25); cnt = arrivals(d, b)[:5]                         # fem passningar i rad
for k, ps in enumerate([(34, 30), (48, 26), (64, 28), (52, 40)]): d.mv(f'a{k}', t, t + 1.6, ps)              # sedan anfall
d.carry(b, 'a1', t, t + 1.6); t += 1.6
t = d.pas(b, t + 0.1, rec(d, 'a2', t + 0.7)); d.mv('f1', t - 1.0, t + 0.2, (60, 22))
t = d.pas(b, t + 0.1, rec(d, 'a0', t + 0.9)); d.mv('a0', t - 1.0, t, (38, 18)); tg = shoot(d, b, t + 0.05, (44, 1))
fp = [(0, 'Rondo i en cirkel framför boxen', 'Grupper om fyra.'),
      (cnt[-1] - 0.3, 'Fem passningar i rad: 1 poäng', ''),
      (cnt[-1] + 0.4, 'Sedan anfall mot två försvarare', ''),
      (tg - 0.3, 'Mål: en extra poäng', 'Försvararna: poäng för bollvinst eller förhindrat mål.')]
finish(d, 'sb07', 'rondo-som-blir-anfall', ['Rondo som', 'blir anfall'], 'Straffområdet och ytan framför · Grupper om fyra',
       fp, 'SPELÖVNING', [('circle', 50, 54, 3.0)], counter(cnt, pos=(76, 60)))
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ sb08 Överlasta och växla ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
BP = [(14, 50), (30, 46), (44, 56), (60, 60), (84, 52), (50, 30)]; RP = [(26, 30), (40, 26), (56, 26), (72, 30), (34, 42), (60, 44)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b2', 0))
t = chain(d, b, 0.4, ['b1', 'b0', 'b1'], 0.3)                                                               # överlasta vänsterkanten
for k, ps in enumerate([(20, 34), (30, 32), (40, 36), (56, 38)]): d.mv(f'r{k}', 0.8, t, ps)
d.mv('b4', t - 1.4, t + 1.0, (88, 30)); t = d.pas(b, t + 0.2, rec(d, 'b4', t + 1.8), 1.5); tsw = t           # lång diagonal
t = drive(d, b, 'b4', t, (88, 14), 18); d.mv('b5', t - 1.6, t + 0.6, (38, 8))
t = d.pas(b, t + 0.1, rec(d, 'b5', t + 1.1), 1.0); tg = shoot(d, b, t + 0.05, (42, 1))                       # inlägg mot bakre stolpen
fp = [(0, 'Överlasta ena kanten', '4-4-2 på planhalva.'),
      (tsw - 1.6, 'Lång diagonal till andra sidan', ''),
      (tg - 1.4, 'Inlägg mot bakre stolpen', '30 sekunder att göra mål.'),
      (tg - 0.2, 'Mål + bonus om upplägget följs', 'Försvaret: poäng för bollvinst och rensning.')]
finish(d, 'sb08', 'overlasta-och-vaxla', ['Överlasta', 'och växla'], 'Planhalva · 4-4-2',
       fp, 'SPELÖVNING', [], [lab(tsw - 1.4, tsw, (50, 46), 'DIAGONAL')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ sb09 1 mot 1-stafetten ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
d.p('a', '', B, (20, 50)); d.p('c', '', R, (80, 50)); d.p('a2', '', B, (16, 56)); d.p('c2', '', R, (84, 56))
POL = [(30, 46), (36, 42), (64, 42), (70, 46)]
b = d.newball((51.8, 30.8))
t1 = d.path('a', 0.4, [(28, 42), (34, 48), (40, 40), (48, 34)], 1.5)                                         # slalom mot bollen
t2 = d.path('c', 0.4, [(72, 42), (66, 48), (60, 40), (54, 36)], 1.3)
d.carry(b, 'a', t1, t1 + 0.3)
t = drive(d, b, 'a', t1 + 0.3, (44, 20), 12); d.mv('c', t2, t, (48, 18))                                      # först anfaller 1 mot 1
tg = shoot(d, b, t + 0.1, (46, 1)); hide(d, b, tg + 0.3)
fp = [(0, 'Två spelare tävlar genom slalomen', 'Mot bollen.'),
      (t1 - 0.6, 'Först till bollen anfaller', 'Den andra försvarar.'),
      (tg - 0.4, 'Mål: två poäng', 'Bollvinst eller blockering: en.'),
      (tg + 0.4, 'Frispark: minus en', 'Först till fem.')]
finish(d, 'sb09', '1-mot-1-stafetten', ['1 mot 1-', 'stafetten'], 'Straffområdet · Startkoner och slalom med fyra stolpar',
       fp, 'DUELL', [('pole',) + p for p in POL])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ st01 Aj! – träffa tränaren ============
d = Drill(); d.p('t', 'T', T_COL, (50, 50))
ST = [(22, 24), (50, 18), (78, 26), (82, 56), (72, 82), (40, 82), (18, 58)]
for k, ps in enumerate(ST): d.p(f'p{k}', '', B, ps)
balls = [d.newball(rec(d, f'p{k}', 0)) for k in range(7)]; ex = []
wander(d, 't', 0, 17.9, (36, 36, 64, 64), 9300, 1.6)
for k in range(7):
    wander(d, f'p{k}', 0, 17.9, boxes([ST[k]], 6)[0], 9310 + k, 1.6); d.carry(balls[k], f'p{k}', 0, 17.9)
for k, th in [(1, 3.0), (4, 6.4), (6, 9.8)]:
    tr = d.balls[balls[k]]; d.balls[balls[k]] = [(t, q) for t, q in tr if t < th]
    tx, ty = at(d.pl['t']['tr'], th + 0.6)
    d.pas(balls[k], th, (tx + 1.5, ty + 1), 0.6); d.pas(balls[k], th + 0.6, rec(d, f'p{k}', th + 1.6), 1.0)
    d.carry(balls[k], f'p{k}', th + 1.6, 17.9); ex.append(lab(th + 0.6, th + 1.6, (tx, ty - 8), '”AJ!”'))
fp = [(0, 'Alla med boll – tränaren är ett rörligt mål', ''),
      (3.4, 'Träff: tränaren ropar ”Aj!”', 'En poäng.'),
      (7.0, 'Fortsätt dribbla och sikta', ''),
      (11.0, 'Variant: bara insidan eller vänster fot', 'Eller en assistent som andra mål.')]
finish(d, 'st01', 'aj-traffa-tranaren', ['Aj!', 'Träffa tränaren'], 'Ruta ca 18 × 27 m · Alla med boll',
       fp, 'LEK MED BOLL', [('box', 10, 10, 90, 90)], ex)

# ============ st02 Flaggleken ============
d = Drill(); d.p('t', 'T', T_COL, (96, 50))
FL = [(30, 26), (70, 26), (30, 50), (70, 50), (30, 74), (70, 74)]
ST = [(44, 18), (56, 30), (44, 42), (56, 56), (44, 66), (56, 80), (50, 36), (50, 64)]
for k, ps in enumerate(ST): d.p(f'p{k}', '', B, ps)
balls = [d.newball(rec(d, f'p{k}', 0)) for k in range(8)]
for k in range(8): wander(d, f'p{k}', 0, 4.4, (40, ST[k][1] - 8, 60, ST[k][1] + 8), 9400 + k, 1.4)
order = [0, 1, 2, 3, 4, 5]
for j, k in enumerate([0, 1, 2, 3, 4, 5]):
    fx, fy = FL[j]; d.mv(f'p{k}', 4.6, 6.0, (fx + (3 if fx < 50 else -3), fy + 2))                            # tar en fri flagga
for k in (6, 7): d.mv(f'p{k}', 4.6, 6.0, (50, 40 if k == 6 else 60))                                         # två blir utan
for k in range(8): stand(d, f'p{k}', 6.0, 8.6); wander(d, f'p{k}', 8.6, 17.9, (40, ST[k][1] - 8, 60, ST[k][1] + 8), 9410 + k, 1.4); d.carry(balls[k], f'p{k}', 0, 17.9)
fp = [(0, 'Alla dribblar fritt', 'Två färre flaggor än spelare.'),
      (4.4, '”STOPP!” – ta en fri flagga', ''),
      (6.0, 'Två blir utan', ''),
      (8.6, 'Ny runda', 'Variant: ta bort flaggor varje runda.')]
finish(d, 'st02', 'flaggleken', ['Flagg-', 'leken'], 'Smal ruta ca 9 × 23 m · Flaggor',
       fp, 'LEK', [('box', 22, 8, 78, 92)] + [('pole',) + f for f in FL], [lab(4.4, 6.0, (50, 4), '”STOPP!”'), lab(6.0, 8.6, (64, 40), 'UTAN'), lab(6.0, 8.6, (64, 60), 'UTAN')])

# ============ st03 4 mot 4 med fem mål i straffområdet ============
d = Drill(); d.p('mv', 'MV', ORA, (50, 4))
SG = [(16, 20), (84, 20), (16, 70), (84, 70)]
BP = [(30, 56), (60, 60), (42, 36), (70, 40)]; RP = [(36, 46), (64, 50), (50, 28), (26, 30)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
for k in range(4): wander(d, f'r{k}', 0, 6, boxes([RP[k]], 4)[0], 9500 + k, 1.6)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b2'], 0.3); t = drive(d, b, 'b2', t, (24, 26), 16); tg1 = d.pas(b, t + 0.1, (16, 20), 0.4); hide(d, b, tg1 + 0.3)   # småmål 1
b2 = d.newball((200, 200)); show(d, b2, tg1 + 1.0, rec(d, 'b1', tg1 + 1.0))
t = d.pas(b2, tg1 + 1.2, rec(d, 'b3', tg1 + 2.2), 1.0); d.mv('b2', tg1 + 0.4, t + 0.6, (48, 14))
t = d.pas(b2, t + 0.2, (49, 13), 0.9); tn = t; tg2 = d.pas(b2, t + 0.05, (52, 1), 0.4)                          # nick i det stora målet
fp = [(0, 'Fyra mot fyra i straffområdet', 'Fyra småmål och det stora målet.'),
      (tg1 - 0.6, 'Mål i ett småmål: en poäng', ''),
      (tn - 0.8, 'Stora målet: bara nick eller volley', ''),
      (tg2, 'Två poäng', 'Räddar målvakten rullar hen till boxens kant.')]
finish(d, 'st03', '4-mot-4-med-fem-mal-i-straffomradet', ['4 mot 4', 'Med fem mål i straffområdet'], 'Straffområdet · Fyra småmål och stora målet',
       fp, 'SMÅLAGSSPEL', [('smallgoal',) + g for g in SG] + [('text', 16, 28, '1'), ('text', 84, 28, '2'), ('text', 16, 78, '3'), ('text', 84, 78, '4')],
       [lab(tg1, tg1 + 1.4, (22, 12), '+1'), lab(tn, tn + 1.0, (62, 14), 'NICK'), lab(tg2, tg2 + 1.6, (52, 12), '+2')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ st04 Nicka eller fånga ============
d = Drill(); d.p('t', 'T', T_COL, (50, 50))
RING = [ring_pos(50, 50, 26, i, 7) for i in range(7)]
for k, ps in enumerate(RING): d.p(f'p{k}', '', B, ps)
b = d.newball(rec(d, 't', 0)); t = 0.4; ex = []
for k, cmd in [(0, 'NICKA'), (2, 'FÅNGA'), (4, 'NICKA'), (6, 'FÅNGA'), (1, 'NICKA')]:
    ex.append(lab(t, t + 0.9, (50, 40), '”' + cmd + '!”'))
    t1 = d.pas(b, t + 0.1, rec(d, f'p{k}', t + 0.8), 0.7); t = d.pas(b, t1 + 0.1, rec(d, 't', t1 + 0.8), 0.6) + 0.3
k = 3; ex.append(lab(t, t + 0.9, (50, 40), '”FÅNGA!”'))
t1 = d.pas(b, t + 0.1, rec(d, f'p{k}', t + 0.8), 0.7); t2 = d.pas(b, t1 + 0.05, rec(d, 't', t1 + 0.7), 0.6)   # nickar fel – sätter sig
ex.append(lab(t1, t1 + 2.0, (RING[3][0], RING[3][1] + 8), 'FEL – SÄTT DIG'))
d.mv(f'p{k}', t1 + 0.4, t1 + 1.2, (RING[3][0] + (RING[3][0] - 50) * 0.25, RING[3][1] + (RING[3][1] - 50) * 0.25))
fp = [(0, 'Tränaren kastar mot en spelares huvud', 'Och ropar ”nicka” eller ”fånga”.'),
      (2.0, 'Gör det tränaren säger', ''),
      (t1 - 0.4, 'Fel – sätt dig', 'Sista stående vinner.'),
      (t1 + 1.6, 'Variant: vänd på reglerna', 'Eller lägg till lår och bröst.')]
finish(d, 'st04', 'nicka-eller-fanga', ['Nicka', 'eller fånga'], 'Liten cirkel · Tränaren i mitten',
       fp, 'LEK', [], ex)

# ============ st05 Träffa bollen ============
d = Drill()
PR = [((24, 30), (40, 40)), ((70, 66), (56, 56))]
for k, (a, c) in enumerate(PR): d.p(f'a{k}', '1', B, a); d.p(f'c{k}', '2', ORA, c)
ex = []
for k, (a, c) in enumerate(PR):
    ba = d.newball(rec(d, f'a{k}', 0)); bc = d.newball(rec(d, f'c{k}', 0)); t = 0.4 + 0.6 * k
    t1 = d.pas(ba, t, (a[0] + (30 if k == 0 else -30), a[1] + 14), 1.0)                                         # spelare 1 passar ut sin boll
    tx, ty = a[0] + (30 if k == 0 else -30), a[1] + 14
    t2 = d.pas(bc, t1 + 0.4, (tx - 1, ty - 1), 1.0); ex.append(lab(t2, t2 + 1.2, (tx, ty - 8), 'TRÄFF'))           # spelare 2 träffar den
    d.pas(ba, t2, (tx + 6, ty + 4), 0.5)
    d.mv(f'a{k}', t2, t2 + 1.6, (tx + 4, ty + 2)); d.mv(f'c{k}', t2, t2 + 1.4, (tx - 3, ty - 3))
    d.carry(ba, f'a{k}', t2 + 1.6, t2 + 2.0); d.carry(bc, f'c{k}', t2 + 1.4, t2 + 2.0)
    t3 = d.pas(bc, t2 + 2.2, (tx - 20 if k == 0 else tx + 20, ty + 10), 1.0)                                    # ny boll ut
    t4 = d.pas(ba, t3 + 0.4, (tx - 22 if k == 0 else tx + 22, ty + 9), 1.1)                                    # miss
    d.mv(f'c{k}', t3, t4 + 0.6, (tx - 18 if k == 0 else tx + 18, ty + 6)); d.mv(f'a{k}', t3 + 0.4, t4 + 1.0, (tx - 24 if k == 0 else tx + 24, ty + 6))
    d.carry(ba, f'a{k}', t4 + 1.0, t4 + 1.4); d.carry(bc, f'c{k}', t4 + 0.6, t4 + 1.0)
fp = [(0, 'Spelare 1 passar ut sin boll', 'Så att den stannar.'),
      (1.6, 'Spelare 2 försöker träffa den', ''),
      (ex[0]['t0'], 'Träff: en poäng', 'Missar hen siktar spelare 1 på spelare 2:s boll.'),
      (6.0, 'Först till fem poäng', 'Byt fotyta: insida, utsida, vrist.')]
finish(d, 'st05', 'traffa-bollen', ['Träffa', 'bollen'], 'Stor ruta ca 37 × 46 m · Par med var sin boll',
       fp, 'PASSNINGSÖVNING', [('box', 6, 10, 94, 90)], ex)

# ============ st06 Yttern utmanar backen ============
d = Drill(); d.p('mv', 'MV', R, (50, 4)); d.p('s', 'S', T_COL, (50, 96))
d.p('y0', 'Y', B, (88, 60)); d.p('k0', 'B', R, (88, 40)); d.p('y1', 'Y', B, (12, 60)); d.p('k1', 'B', R, (12, 40))
BP = [(34, 50), (50, 58), (66, 50), (50, 40)]; RP = [(36, 32), (50, 24), (64, 32), (50, 46)]; team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 's', 0))
t = d.pas(b, 0.4, rec(d, 'b1', 1.6), 1.2); t = d.pas(b, t + 0.2, rec(d, 'y0', t + 1.4))
d.mv('y0', t, t + 0.6, (86, 54)); d.carry(b, 'y0', t, t + 0.6); t += 0.6                                      # yttern vänder – backen väntar
d.mv('k0', t - 0.4, t + 0.6, (86, 46)); d.mv('y0', t, t + 0.8, (92, 40)); d.carry(b, 'y0', t, t + 0.8); t += 0.8   # kommer förbi
t = drive(d, b, 'y0', t, (88, 16), 18); d.mv('k0', t - 1.4, t, (84, 22))
d.mv('b3', t - 1.6, t + 0.4, (46, 12)); t = d.pas(b, t + 0.1, rec(d, 'b3', t + 1.0), 0.9); tg = shoot(d, b, t + 0.05, (54, 1))
fp = [(0, 'En ytter och en back i varje fil', '4 mot 4 i mitten. Server vid mittlinjen.'),
      (2.4, 'Backen låter yttern vända', 'Sedan press.'),
      (4.2, 'Yttern utmanar och kommer förbi', ''),
      (tg - 1.2, 'Inlägg eller passning', 'Variant: backen pressar direkt.')]
finish(d, 'st06', 'yttern-utmanar-backen', ['Yttern utmanar', 'backen'], 'Anfallstredjedelen · Kantfiler på ca 14 m',
       fp, 'SPELÖVNING', [('zone', 0, 4, 22, 96, (200, 220, 200), ''), ('zone', 78, 4, 100, 96, (200, 220, 200), '')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ st07 Mot kortlinjen – inläggsspelet ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96))
d.p('ya', 'Y', B, (90, 60)); d.p('yd', 'B', R, (90, 46)); d.p('za', 'Y', R, (10, 40)); d.p('zd', 'B', B, (10, 54))
BP = [(34, 60), (66, 58), (44, 40), (58, 30)]; RP = [(36, 34), (64, 36), (50, 52), (44, 22)]; team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b1', 0))
t = d.pas(b, 0.4, rec(d, 'ya', 1.4)); t = drive(d, b, 'ya', t, (90, 14), 16); d.mv('yd', 1.4, t - 0.6, (88, 20))   # kantförsvararen släpper inlägget i slutzonen
for k, ps in enumerate([(40, 14), (56, 10)]): d.mv(f'b{k + 2}', t - 2.0, t + 0.4, ps)
t = d.pas(b, t + 0.1, rec(d, 'b3', t + 1.1), 1.0); tg = shoot(d, b, t + 0.05, (54, 1))
fp = [(0, 'Fyra mot fyra i mitten', '1 mot 1 i varje kant.'),
      (1.6, 'Driv mot kortlinjen', ''),
      (tg - 1.4, 'Kantförsvararen släpper inlägget', 'När anfallaren nått slutzonen.'),
      (tg - 0.2, 'Mål räknas bara efter inlägg', '')]
finish(d, 'st07', 'mot-kortlinjen-inlaggsspelet', ['Mot kortlinjen', 'Inläggsspelet'], 'Halvplan · Kanaler på ca 9 m · Mål med målvakter',
       fp, 'SPELÖVNING', [('zone', 0, 4, 20, 96, (200, 220, 200), ''), ('zone', 80, 4, 100, 96, (200, 220, 200), ''), ('zone', 80, 4, 100, 20, (240, 210, 90), '')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ sm01 Första passningen 2 mot 2 ============
d = Drill()
d.p('h', '', B, (40, 88)); d.p('m', '', B, (60, 12)); d.p('r0', '', R, (40, 12)); d.p('r1', '', R, (60, 88))
b = d.newball(rec(d, 'h', 0))
t = d.pas(b, 0.4, rec(d, 'm', 1.8), 1.4)                                                                     # till motsatt kortlinje
d.mv('h', t, t + 1.4, (40, 50)); d.mv('r0', t, t + 1.2, (52, 26)); d.mv('r1', t, t + 1.4, (56, 60))           # alla går in – 2 mot 2
t = drive(d, b, 'm', t, (62, 34), 14); t = d.pas(b, t + 0.1, rec(d, 'h', t + 0.9))
d.mv('r1', t - 0.6, t + 0.4, (44, 58)); t = drive(d, b, 'h', t, (34, 72), 16); d.mv('h', t, t + 0.8, (32, 92)); d.carry(b, 'h', t, t + 0.8); tg = t + 0.6   # över kortlinjen
fp = [(0, 'Passa till motsatt kortlinje', 'Ruta ca 18 × 18 m.'),
      (1.8, 'Mottagen – alla in', '2 mot 2.'),
      (tg - 1.4, 'Dribbla över motståndarnas kortlinje', ''),
      (tg, 'Vinst', 'Variant: 1 mot 1, 3 mot 3 eller 4 mot 4.')]
finish(d, 'sm01', 'forsta-passningen-2-mot-2', ['Första passningen', '2 mot 2'], 'Ruta ca 18 × 18 m',
       fp, 'DUELL', [('box', 16, 8, 84, 92)], [lab(tg, tg + 1.6, (32, 84), 'VINST')])

# ============ sm02 Snabba omställningar med fyra lag ============
d = Drill()
team(d, 'b', B, [(36, 60), (64, 62)]); team(d, 'r', R, [(40, 40), (60, 40)]); team(d, 'w', WHITE, [(40, 8), (60, 8)], ['', '']); team(d, 'y', YEL, [(40, 92), (60, 92)], ['', ''])
b = d.newball(rec(d, 'b0', 0))
t = d.pas(b, 0.4, rec(d, 'b1', 1.2)); d.mv('b0', t - 0.6, t + 0.8, (44, 26)); t = drive(d, b, 'b1', t, (58, 24), 14)
t = d.pas(b, t + 0.1, rec(d, 'w1', t + 1.0)); tz = t                                                          # passar in i målzonen
for k, ps in enumerate([(40, 14), (60, 14)]): d.mv(f'b{k}', tz, tz + 1.0, ps)                                # anfaller zonen och behåller bollen
for k, ps in enumerate([(40, 40), (60, 42)]): d.mv(f'w{k}', tz, tz + 1.8, ps)                                # laget som tog emot försvarar
for k, ps in enumerate([(40, 90), (60, 90)]): d.mv(f'r{k}', tz, tz + 2.6, (ps[0], 70))
d.carry(b, 'w1', tz, tz + 0.4); t = d.pas(b, tz + 0.5, rec(d, 'b1', tz + 1.2))
t = chain(d, b, t, ['b0', 'b1'], 0.3)
fp = [(0, 'Fyra lag', 'Målzoner i båda ändar.'),
      (tz - 0.6, 'Passa in i en målzon', ''),
      (tz + 0.4, 'Anfall zonen och behåll bollen', 'Försvara mot laget som tog emot.'),
      (tz + 2.0, 'Laget som lämnar planen', 'Går till zonen det tidigare försvarade.')]
finish(d, 'sm02', 'snabba-omstallningar-med-fyra-lag', ['Snabba omställningar', 'med fyra lag'], 'Yta ca 23 × 37 m · Målzoner',
       fp, 'OMSTÄLLNING', [('box', 20, 2, 80, 98), ('zone', 20, 2, 80, 16, (200, 220, 200), 'ZON'), ('zone', 20, 84, 80, 98, (200, 220, 200), 'ZON')])

if __name__ == '__main__': render(C, sys.argv)
