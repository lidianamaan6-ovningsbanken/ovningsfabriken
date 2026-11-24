# Externa övningar, omgång 30 (tolv st). Regel: först d.mv, sedan d.carry; först mottagarens rörelse, sedan passningen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e9', __file__.replace('render_extern30.py', 'render_extern9.py'))
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

# ============ sx08 4 mot 2 – driv igenom ============
d = Drill()
TOP = [(30, 12), (70, 12), (30, 40), (70, 40)]; BOT = [(30, 60), (70, 60), (30, 88), (70, 88)]
team(d, 't', B, TOP); team(d, 'u', B, BOT); team(d, 'f', R, [(44, 24), (56, 30)], ['', '']); team(d, 'g', R, [(44, 72), (56, 78)], ['', ''])
b = d.newball(rec(d, 't0', 0))
for k in range(2): wander(d, f'g{k}', 0, 17.9, boxes([[(44, 72), (56, 78)][k]], 4)[0], 8600 + k, 1.4)
t = chain(d, b, 0.4, ['t1', 't3', 't2'], 0.3)
d.mv('f0', t - 1.0, t, (40, 22)); d.mv('f1', t - 1.0, t, (60, 22))                                         # lucka öppnas
t = drive(d, b, 't2', t + 0.1, (48, 56), 14); tg = t                                                       # driver igenom till nästa grupp
t = d.pas(b, t + 0.1, rec(d, 'u0', t + 0.7)); d.mv('t2', tg, tg + 2.4, (30, 40))
t = chain(d, b, t, ['u1', 'u3', 'u2'], 0.3)
fp = [(0, 'Fyra mot två i en ruta', 'Yta ca 11 × 33 m med två rutor.'),
      (2.0, 'Vänta på luckan', ''),
      (tg - 1.4, 'Driv igenom luckan', 'Över till nästa grupp.'),
      (tg + 0.6, 'Samma sak åt andra hållet', 'Variant: begränsa passningar eller touch.')]
finish(d, 'sx08', '4-mot-2-driv-igenom', ['4 mot 2', 'Driv igenom'], 'Yta ca 11 × 33 m med två rutor',
       fp, 'RONDO', [('box', 22, 4, 78, 48), ('box', 22, 52, 78, 96)])

# ============ sx09 Tresekundersomställningen ============
d = Drill()
GT = [(50, 8), (50, 92)]
BP = [(30, 66), (70, 64), (42, 46), (60, 80)]; RP = [(34, 36), (66, 34), (52, 56), (44, 22)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b2', 'b1'], 0.3)
tw = win(d, b, 'r2', 'b1', t + 0.3, 0.6)                                                                    # bollvinst – tre sekunder
for k, ps in [(1, (60, 58)), (2, (50, 52)), (0, (40, 60))]: d.mv(f'b{k}', tw, tw + 1.0, ps)                  # laget som tappar pressar och går ihop
t = d.pas(b, tw + 0.2, rec(d, 'r0', tw + 0.8)); t = d.pas(b, t + 0.1, rec(d, 'r1', t + 0.8)); t = d.pas(b, t + 0.1, rec(d, 'r3', t + 0.8))   # tre passningar
d.mv('r3', t, t + 1.0, (50, 12)); d.carry(b, 'r3', t, t + 1.0); tp = t + 0.8                                 # eller attackera en port
fp = [(0, 'Fyra mot fyra', 'Portar i varje ände.'),
      (tw - 0.2, 'Bollvinst – tre sekunder', 'Tre passningar eller attack mot en port.'),
      (tw + 0.4, 'Laget som tappar pressar direkt', 'Och går ihop.'),
      (tp - 0.4, 'Genom porten', '')]
finish(d, 'sx09', 'tresekundersomstallningen', ['Tresekunders-', 'omställningen'], 'Yta ca 18 × 23 m med portar',
       fp, 'OMSTÄLLNING', [('box', 12, 6, 88, 94)] + [('cone', x + dx, y) for x, y in GT for dx in (-5, 5)],
       countup(tw + 0.1, 3, (84, 50), (tp - tw) / 3) + [lab(tp, tp + 1.6, (50, 18), 'PORT')])

# ============ ys01 Sjukhuskull ============
d = Drill()
ST = [(22, 26), (48, 22), (76, 28), (24, 54), (52, 50), (78, 56), (34, 78), (66, 78)]
for k, ps in enumerate(ST): d.p(f'p{k}', '', B, ps)
d.p('k', '', R, (50, 36))
for k in (0, 1, 2, 3, 5, 6, 7): wander(d, f'p{k}', 0, 17.9, boxes([ST[k]], 7)[0], 8700 + k, 2.0)
d.mv('k', 0.3, 2.2, (50, 46)); tk1 = 2.2; wander(d, 'p4', 0, 2.0, boxes([ST[4]], 4)[0], 8710, 1.4)
d.mv('p4', 2.2, 5.0, (40, 60)); d.mv('k', 2.6, 5.0, (46, 64)); tk2 = 5.0                                      # handen på stället
d.mv('p4', 5.2, 7.6, (58, 70)); d.mv('k', 5.4, 7.6, (62, 72)); tk3 = 7.6                                     # tre kullningar
stand(d, 'p4', 7.6, 10.6); wander(d, 'p4', 10.6, 17.9, boxes([ST[4]], 7)[0], 8711, 1.4); wander(d, 'k', 8.0, 17.9, (30, 30, 70, 70), 8712, 1.6)
fp = [(0, 'Alla försöker kulla varandra', 'Ingen utrustning.'),
      (tk1, 'Kullad: håll handen där du träffades', ''),
      (tk3, 'Tre kullningar: fem stjärnhopp', ''),
      (10.6, 'Fri igen', '')]
d.newball((200, 200))
no_ball_finish(d, 'ys01', 'sjukhuskull', ['Sjukhus-', 'kull'], 'Ruta ca 18 × 18 m',
       fp, 'LEK', [('box', 12, 12, 88, 88)], [lab(tk1, tk1 + 1.2, (52, 38), '1'), lab(tk2, tk2 + 1.2, (42, 50), '2'), lab(tk3, tk3 + 1.2, (60, 60), '3'), lab(tk3 + 0.4, 10.6, (58, 82), '5 STJÄRNHOPP')])

# ============ ys02 Från 3 mot 2 till 2 mot 3 ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96))
team(d, 'b', B, [(30, 66), (50, 70), (70, 66)]); team(d, 'r', R, [(42, 34), (58, 34)]); d.p('rq', '', R, (94, 50))
b = d.newball(rec(d, 'b1', 0))
for k, ps in enumerate([(30, 40), (50, 46), (70, 38)]): d.mv(f'b{k}', 0.4, 2.2, ps)
d.carry(b, 'b1', 0.4, 2.2); t = d.pas(b, 2.3, rec(d, 'b2', 2.9)); d.mv('r1', 2.0, t, (64, 30))
t = d.pas(b, t + 0.2, rec(d, 'b0', t + 1.0)); d.mv('b0', t - 1.0, t, (36, 26)); tg = shoot(d, b, t + 0.05, (44, 1)); hide(d, b, tg + 0.3)   # mål
d.mv('b0', tg, tg + 2.0, (94, 56)); d.mv('rq', tg, tg + 1.6, (50, 50))                                         # byter roll: de tre blir två försvarare
for k, ps in [(1, (44, 62)), (2, (58, 62))]: d.mv(f'b{k}', tg, tg + 1.8, ps)
b2 = d.newball((200, 200)); show(d, b2, tg + 1.2, rec(d, 'mvr', tg + 1.2))
t = d.pas(b2, tg + 1.4, rec(d, 'r0', tg + 2.4)); t = drive(d, b2, 'r0', t, (40, 70), 16)
t = d.pas(b2, t + 0.1, rec(d, 'rq', t + 0.9)); d.mv('rq', t - 1.4, t, (58, 76)); tg2 = shoot(d, b2, t + 0.05, (54, 99))
fp = [(0, 'Tre anfallare mot två försvarare', ''),
      (tg - 0.4, 'Mål', 'Lagen byter roll.'),
      (tg + 1.0, 'Nu anfaller de två åt andra hållet', 'Två av de tre blir försvarare.'),
      (tg2 - 0.4, 'Även vid räddning eller bollvinst', '')]
finish(d, 'ys02', 'fran-3-mot-2-till-2-mot-3', ['Från 3 mot 2', 'till 2 mot 3'], 'Halv planhalva · Två mål med målvakter',
       fp, 'ÖVERLÄGE', [])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ ys03 Skottfilerna ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
LX = [26, 50, 74]
for k, x in enumerate(LX): d.p(f'm{k}', 'M', ORA, (x + 8, 30)); d.p(f'a{k}', '', B, (x, 50)); d.p(f'q{k}', '', B, (x, 56))
t = 0.4
for rep, k in enumerate([0, 1, 2, 0, 1, 2]):
    a = f'a{k}' if rep < 3 else f'q{k}'
    if rep >= 3: d.mv(a, t - 1.2, t, (LX[k], 50))
    bb = d.newball(rec(d, f'm{k}', t)); t1 = d.pas(bb, t, rec(d, a, t + 0.9))
    d.carry(bb, a, t1, t1 + 0.35); tg = shoot(d, bb, t1 + 0.4, (46 + 4 * k, 1)); hide(d, bb, tg + 0.3)       # ett touch och avslut
    d.mv(a, tg + 0.2, tg + 2.0, (LX[k] + 6, 66 + 8 * (rep // 3))); t = tg - 0.2
fp = [(0, 'Tre led ca 18 m från mål', 'En matare per led.'),
      (1.2, 'Mataren spelar in', 'Ett touch och avslut.'),
      (5.0, 'Nästa led', ''),
      (9.0, 'Byt matare var femte minut', '')]
finish(d, 'ys03', 'skottfilerna', ['Skott-', 'filerna'], 'Yta ca 23 × 37 m · Tre led · En matare per led',
       fp, 'AVSLUT', [])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ ys04 Målvaktens utspel på tre avstånd ============
d = Drill(); d.p('mv', 'MV', ORA, (50, 6))
TG = [(36, 34), (66, 58), (40, 84)]; KIND = ['RULLA', 'KASTA', 'SPARKA']; ex = []
t = 0.4
for k, (x, y) in enumerate(TG):
    bb = d.newball(rec(d, 'mv', t)); t1 = d.pas(bb, t + 0.2, (x, y), 0.8 + 0.4 * k); hide(d, bb, t1 + 0.5)
    ex.append(lab(t, t1 + 0.4, (78, 14), KIND[k])); t = t1 + 1.0
for k, (x, y) in enumerate(TG):
    bb = d.newball(rec(d, 'mv', t)); t1 = d.pas(bb, t + 0.2, (x + 1, y), 0.8 + 0.4 * k); hide(d, bb, t1 + 0.5); t = t1 + 0.8
fp = [(0, 'Rulla till det nära målet', 'Ca 18 m.'),
      (ex[1]['t0'], 'Kasta till det mellersta', 'Ca 32 m.'),
      (ex[2]['t0'], 'Sparka eller drop-kicka till det långa', 'Ca 46 m.'),
      (ex[2]['t1'] + 0.4, 'Tre omgångar av varje', '')]
finish(d, 'ys04', 'malvaktens-utspel-pa-tre-avstand', ['Målvaktens utspel', 'på tre avstånd'], 'Halvplan · Konmål på ca 18, 32 och 46 m',
       fp, 'MÅLVAKT', [('cone', x + dx, y) for x, y in TG for dx in (-4, 4)], ex)
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ sb01 Passa genom sektionerna ============
d = Drill()
EN = [(30, 6), (70, 6), (30, 94), (70, 94)]; IN = [(30, 32), (70, 32), (30, 68), (70, 68)]
team(d, 'e', B, EN); team(d, 'i', B, IN); team(d, 'f', R, [(50, 30), (50, 70)], ['', ''])
for k in range(4): wander(d, f'i{k}', 0, 17.9, boxes([IN[k]], 5)[0], 8800 + k, 1.4)
b = d.newball(rec(d, 'e0', 0))
t = chain(d, b, 0.4, ['i0', 'i1', 'i3', 'i2', 'e2'], 0.3); tp = t                                            # genom båda sektionerna
t = chain(d, b, t, ['i2', 'i3'], 0.3); tw = win(d, b, 'f1', 'i3', t + 0.4, 0.6)                              # försvararna vinner – anfallet börjar om
t = d.pas(b, tw + 0.3, rec(d, 'e1', tw + 1.6), 1.2)
wander(d, 'f0', 0, 17.9, (40, 22, 60, 40), 8810, 1.6)
fp = [(0, 'Åtta anfallare mot två försvarare', 'Ruta delad i två sektioner.'),
      (tp - 1.6, 'Bollen måste passera båda sektionerna', ''),
      (tp, 'Poäng', 'Först till fem.'),
      (tw - 0.2, 'Försvararna vinner – anfallet börjar om', 'Rotera efter 2–3 minuter.')]
finish(d, 'sb01', 'passa-genom-sektionerna', ['Passa genom', 'sektionerna'], 'Ruta ca 18 × 18 m i två sektioner · Anfallare i båda ändar',
       fp, 'POSITIONSSPEL', [('box', 12, 14, 88, 86), ('line', [(12, 50), (88, 50)])], [lab(tp, tp + 1.6, (50, 92), '+1')])

# ============ sb02 Kanalinnehav ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96))
BP = [(12, 60), (88, 58), (40, 64), (60, 48)]; RP = [(14, 36), (86, 38), (44, 40), (58, 58)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b2', 0))
t = d.pas(b, 0.4, rec(d, 'b0', 1.4)); t = d.pas(b, t + 0.2, rec(d, 'b3', t + 1.2)); t = d.pas(b, t + 0.2, rec(d, 'b1', t + 1.4))   # växling mellan kanalerna
d.mv('b1', t, t + 1.4, (88, 24)); d.carry(b, 'b1', t, t + 1.4); t += 1.4
d.mv('b3', t - 1.6, t + 0.4, (54, 18)); d.mv('b0', t - 1.6, t + 0.4, (14, 26)); t = d.pas(b, t + 0.1, rec(d, 'b3', t + 1.0), 0.9); tg = shoot(d, b, t + 0.05, (46, 1))
fp = [(0, 'Fem mot fem med två mål', 'Två kanaler och mitten.'),
      (1.6, 'Växla mellan kanalerna', 'Ger bonusmål.'),
      (tg - 1.4, 'En spelare i varje sektion', 'Först då får laget göra mål.'),
      (tg - 0.2, 'Mål', 'Först till tre mål.')]
finish(d, 'sb02', 'kanalinnehav', ['Kanal-', 'innehav'], 'Halva planens längd · Två kanaler och mitten',
       fp, 'SPELÖVNING', [('line', [(26, 4), (26, 96)]), ('line', [(74, 4), (74, 96)])])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ sb03 Över mittzonen – tre trios ============
d = Drill()
A = [(30, 12), (50, 22), (70, 12)]; Z = [(30, 88), (50, 78), (70, 88)]; M = [(34, 48), (50, 52), (66, 48)]
team(d, 'a', B, A); team(d, 'z', WHITE, Z); team(d, 'm', R, M)
for k in range(3): wander(d, f'm{k}', 0, 17.9, boxes([M[k]], 4)[0], 8900 + k, 1.4)
b = d.newball(rec(d, 'a0', 0)); sw = []
t = chain(d, b, 0.4, ['a1', 'a2'], 0.3); t = d.pas(b, t + 0.2, rec(d, 'z0', t + 1.4), 1.2); sw.append(t)          # max tre passningar – över
t = chain(d, b, t, ['z1', 'z2'], 0.3); t = d.pas(b, t + 0.2, rec(d, 'a2', t + 1.4), 1.2); sw.append(t)
t = chain(d, b, t, ['a1'], 0.3); t = d.pas(b, t + 0.2, rec(d, 'z1', t + 1.4), 1.2); sw.append(t)
fp = [(0, 'Tre trios', 'Två i ändarna, en försvarar i mitten.'),
      (sw[0] - 1.0, 'Max tre passningar – sedan över', ''),
      (sw[1] - 1.0, 'Och tillbaka', ''),
      (sw[2], 'Fem växlingar i rad vinner', 'Felpass ger byte med mittlaget.')]
finish(d, 'sb03', 'over-mittzonen-tre-trios', ['Över mittzonen', 'Tre trios'], 'Ruta ca 9 × 9 m i tre sektioner',
       fp, 'POSITIONSSPEL', [('box', 16, 4, 84, 96), ('line', [(16, 34), (84, 34)]), ('line', [(16, 66), (84, 66)])], counter(sw, pos=(90, 50), last=None))

# ============ sb04 Positionsspel i tre zoner ============
d = Drill()
BP = [(30, 78), (52, 50), (70, 22)]; RP = [(70, 78), (48, 50), (30, 22)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
for k in range(3): wander(d, f'b{k}', 0, 17.9, (BP[k][0] - 12, BP[k][1] - 10, BP[k][0] + 12, BP[k][1] + 10), 9000 + k, 1.6)
for k in range(3): wander(d, f'r{k}', 0, 17.9, (RP[k][0] - 12, RP[k][1] - 10, RP[k][0] + 12, RP[k][1] + 10), 9010 + k, 1.6)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b1', 'b2'], 0.4); tk = t                                                              # genom alla tre zoner
t = drive(d, b, 'b2', t, (64, 10), 16); tg = d.pas(b, t + 0.1, (50, 4), 0.5); hide(d, b, tg + 0.3)
fp = [(0, 'Tre mot tre, en spelare per zon', 'Två minimål.'),
      (1.4, 'Stanna i din zon', 'Lämnar du den får motståndarna mål.'),
      (tk - 0.6, 'Passningskedja genom alla tre zoner', 'Ger bonusmål.'),
      (tg - 0.4, 'Mål', 'Först till fem.')]
finish(d, 'sb04', 'positionsspel-i-tre-zoner', ['Positionsspel', 'I tre zoner'], 'Yta ca 18 × 14 m i tre zoner · Två minimål',
       fp, 'SMÅLAGSSPEL', [('box', 8, 4, 92, 96), ('line', [(8, 36), (92, 36)]), ('line', [(8, 64), (92, 64)]), ('smallgoal', 50, 4), ('smallgoal', 50, 96)],
       [lab(tk, tk + 1.6, (84, 50), 'BONUS')])

# ============ sb05 4 mot 4 med kantspel ============
d = Drill()
BP = [(34, 66), (60, 70), (44, 48), (58, 32)]; RP = [(38, 36), (62, 38), (50, 56), (44, 24)]
team(d, 'b', B, BP); team(d, 'r', R, RP); d.p('bk', 'K', B, (92, 54)); d.p('rk', 'K', R, (8, 46))
for k in range(4): wander(d, f'r{k}', 0, 7, boxes([RP[k]], 4)[0], 9100 + k, 1.6)
wander(d, 'rk', 0, 17.9, (4, 20, 12, 80), 9120, 1.6)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b2'], 0.3); t = d.pas(b, t + 0.2, rec(d, 'bk', t + 1.4))
d.mv('bk', t, t + 1.6, (92, 18)); d.carry(b, 'bk', t, t + 1.6); t += 1.6                                    # bara i kanalen
d.mv('b3', t - 1.6, t + 0.4, (56, 14)); t = d.pas(b, t + 0.1, rec(d, 'b3', t + 1.0), 0.9); tg = d.pas(b, t + 0.05, (50, 4), 0.4); hide(d, b, tg + 0.3)
fp = [(0, 'Fyra mot fyra med en kantspelare per lag', 'Kanalerna ca 2,7 m.'),
      (1.6, 'Ingen annan får gå in i kanalen', ''),
      (tg - 1.4, 'Kantspelaren ger sista passningen', ''),
      (tg - 0.2, 'Bonusmål', 'Först till tre.')]
finish(d, 'sb05', '4-mot-4-med-kantspel', ['4 mot 4', 'Med kantspel'], 'Yta ca 18 × 14 m · Sidokanaler',
       fp, 'SMÅLAGSSPEL', [('box', 0, 4, 100, 96), ('line', [(16, 4), (16, 96)]), ('line', [(84, 4), (84, 96)]), ('smallgoal', 50, 4), ('smallgoal', 50, 96)],
       [lab(tg, tg + 1.6, (50, 14), 'BONUS')])

# ============ sb06 Klyv försvaret – avslut ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
d.p('p1', 'P1', B, (30, 66)); d.p('p2', 'P2', B, (64, 40)); d.p('q', 'P1', B, (24, 74))
b = d.newball(rec(d, 'p1', 0))
t = d.path('p1', 0.4, [(36, 50), (42, 46), (46, 50)], 1.2); d.carry(b, 'p1', 0.4, t)                          # rundar markören
t = d.pas(b, t + 0.1, rec(d, 'p2', t + 0.8)); d.mv('p1', t - 0.6, t + 0.6, (52, 46)); t = d.pas(b, t + 0.1, rec(d, 'p1', t + 0.8))   # vägg
d.mv('p1', t, t + 1.2, (48, 58)); d.carry(b, 'p1', t, t + 0.4); t1 = d.pas(b, t + 0.4, rec(d, 'p2', t + 1.0))     # backar mot porten
d.mv('p1', t + 1.2, t1 + 1.2, (52, 22)); t = d.pas(b, t1 + 0.2, rec(d, 'p1', t1 + 1.2), 1.0)                    # passning genom porten
tg = shoot(d, b, t + 0.05, (44, 1))
d.mv('p1', tg + 0.4, tg + 2.6, (64, 40)); d.mv('p2', tg + 0.4, tg + 2.6, (24, 74)); d.mv('q', tg + 0.2, tg + 1.4, (30, 66))
fp = [(0, 'P1 rundar markören', 'Straffområdet.'),
      (2.2, 'Vägg med P2', ''),
      (4.0, 'Backa mot porten – passning för 1 mot 1', ''),
      (tg - 0.4, 'Avslut', 'Poäng för sekvensen, extra för mål och första touchen.')]
finish(d, 'sb06', 'klyv-forsvaret-avslut', ['Klyv försvaret', 'Avslut'], 'Straffområdet · En kon och en passningsport',
       fp, 'AVSLUT', [('cone', 42, 50), ('cone', 46, 30), ('cone', 56, 30)])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

if __name__ == '__main__': render(C, sys.argv)
