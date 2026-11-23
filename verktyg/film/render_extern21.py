# Externa övningar, omgång 21 (tolv st). Regel: först d.mv, sedan d.carry; först mottagarens rörelse, sedan passningen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e9', __file__.replace('render_extern21.py', 'render_extern9.py'))
e9 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e9); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e9.finish, e9.rec, e9.chain, e9.wander, e9.counter, e9.arrivals
lab, hide, show, team, boxes, drive, shoot = e9.lab, e9.hide, e9.show, e9.team, e9.boxes, e9.drive, e9.shoot
factor, swap_color, stand, countdown, countup, win = e9.factor, e9.swap_color, e9.stand, e9.countdown, e9.countup, e9.win
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'

# ============ db11 Dubbelt Y ============
d = Drill()
SP = {'S': (50, 88), 'M': (50, 56), 'L': (24, 22), 'R': (76, 22)}
d.p('s0', '', B, SP['S']); d.p('s1', '', B, (50, 94)); d.p('m0', '', B, SP['M']); d.p('l0', '', B, SP['L']); d.p('r0', '', B, SP['R'])
b = d.newball(rec(d, 's0', 0)); t = 0.4; marks = []
Q = {'S': ['s0', 's1'], 'M': ['m0'], 'L': ['l0'], 'R': ['r0']}
def qp(k, n): x, y = SP[k]; return (x, y + 6 * n) if k == 'S' else (x + (-5 if k == 'L' else 5 if k == 'R' else 0) * n, y - 5 * n if k != 'M' else y)
for rep, side in enumerate(['L', 'R', 'L']):
    s = Q['S'].pop(0); m = Q['M'].pop(0); w = Q[side].pop(0)
    d.mv(m, t, t + 0.6, (50, 62)); t1 = d.pas(b, t + 0.1, rec(d, m, t + 0.9))                                  # upp till mitten
    t2 = d.pas(b, t1 + 0.15, rec(d, w, t1 + 1.1)); marks.append(t2)                                             # ut till sidan
    d.mv(s, t1 - 0.4, t1 + 1.4, SP['M']); Q['M'].append(s)                                                     # följ passningen
    d.mv(m, t2 - 0.8, t2 + 1.4, qp(side, len(Q[side]))); Q[side].append(m)
    d.mv(w, t2 + 0.2, t2 + 1.6, (SP[side][0] + (10 if side == 'L' else -10), 30)); d.carry(b, w, t2 + 0.2, t2 + 1.6)
    t3 = d.pas(b, t2 + 1.7, rec(d, Q['S'][0], t2 + 3.0), 1.2)                                                  # tillbaka till startledet
    d.mv(w, t2 + 1.8, t2 + 4.0, qp('S', len(Q['S']))); Q['S'].append(w)
    t = t3 + 0.2
fp = [(0, 'Upp till mitten', 'Koner i form av ett Y.'),
      (marks[0] - 1.0, 'Ut till sidan', 'Följ din passning.'),
      (marks[0] + 1.6, 'Tillbaka till startledet', 'Flöde i spelet.'),
      (marks[1], 'Varianter: vägg, tredje man, djupled', '')]
finish(d, 'db11', 'dubbelt-y', ['Dubbelt Y', 'Passningsövning'], 'Koner i form av ett Y · Två led',
       fp, 'PASSNINGSÖVNING', [('cone', 50, 82), ('cone', 50, 50), ('cone', 30, 26), ('cone', 70, 26)])

# ============ db12 Ryggvänd vändning och avslut ============
d = Drill(); d.p('mv', 'MV', R, (50, 4)); d.p('p', 'P', WHITE, (50, 70)); d.p('a', 'A', B, (50, 34)); d.p('f', 'F', R, (50, 26))
balls = [d.newball((200, 200)) for _ in range(3)]; t = 0.4; ex = []
for k in range(3):
    show(d, balls[k], t, rec(d, 'p', t))
    t1 = d.pas(balls[k], t + 0.2, rec(d, 'a', t + 1.0)); side = 1 if k % 2 == 0 else -1
    if k == 2: d.mv('f', t, t1 + 0.4, (50 - 3 * side, 30))                                                    # aktiv försvarare
    d.mv('a', t1, t1 + 0.6, (50 + 6 * side, 28)); d.carry(balls[k], 'a', t1, t1 + 0.6)                         # vänder
    tg = shoot(d, balls[k], t1 + 0.7, (50 - 4 * side, 1)); hide(d, balls[k], tg + 0.3)
    d.mv('a', tg + 0.2, tg + 1.2, (50, 34)); d.mv('f', tg + 0.2, tg + 1.2, (50, 26)); t = tg + 1.0
fp = [(0, 'Anfallaren har ryggen mot mål', 'Passaren spelar in.'),
      (1.4, 'Vänd och avsluta', ''),
      (4.0, 'Vänd åt andra hållet', ''),
      (7.6, 'Variant: aktiv försvarare i ryggen', 'Först passiv.')]
finish(d, 'db12', 'ryggvand-vandning-och-avslut', ['Ryggvänd vändning', 'och avslut'], 'Mål · En passare och en anfallare med ryggen mot mål',
       fp, 'AVSLUT', [])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ db13 Första touchen ============
d = Drill(); YS = [24, 50, 76]; TECH = ['INSIDA', 'UTSIDA', 'LÅRET', 'TA MED ÅT SIDAN']
for k, y in enumerate(YS): d.p(f'k{k}', '', ORA, (30, y)); d.p(f'm{k}', '', B, (70, y))
balls = [d.newball(rec(d, f'k{k}', 0)) for k in range(3)]; ex = []
for k, y in enumerate(YS):
    t = 0.4 + 0.2 * k
    for rep in range(8):
        t1 = d.pas(balls[k], t, rec(d, f'm{k}', t + 0.8))
        if rep in (6, 7): d.mv(f'm{k}', t1, t1 + 0.4, (70, y + 5)); d.carry(balls[k], f'm{k}', t1, t1 + 0.4); d.mv(f'm{k}', t1 + 0.6, t1 + 1.0, (70, y))
        else: d.carry(balls[k], f'm{k}', t1, t1 + 0.4)
        t2 = d.pas(balls[k], t1 + 0.45, rec(d, f'k{k}', t1 + 1.1)); t = t2 + 0.15
        if k == 0 and rep % 2 == 0: ex.append(lab(t1 - 0.4, t1 + 1.4, (50, 8), TECH[rep // 2]))
fp = [(0, 'Många mottagningar på kort tid', 'Par eller små grupper.'),
      (2.0, 'Insida och utsida', ''),
      (6.0, 'Med låret', ''),
      (10.0, 'Ta med bollen åt sidan', '')]
finish(d, 'db13', 'forsta-touchen', ['Första', 'touchen'], 'Par eller små grupper',
       fp, 'PASSNINGSÖVNING', [], ex)

# ============ wb01 7 mot 7 med fria inläggszoner ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96))
BP = [(30, 72), (70, 72), (40, 56), (60, 56), (50, 40), (30, 34)]; RP = [(30, 28), (70, 28), (40, 44), (60, 44), (50, 60), (70, 64)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b1', 0))
t = chain(d, b, 0.4, ['b3'], 0.3)
d.mv('b1', t - 0.4, t + 1.2, (90, 40)); t = d.pas(b, t + 0.2, rec(d, 'b1', t + 1.4))                            # in i inläggszonen – får inte pressas
t = drive(d, b, 'b1', t, (90, 16), 18)
d.mv('b4', t - 1.6, t + 0.4, (48, 12)); d.mv('b5', t - 1.6, t + 0.4, (38, 18)); d.mv('r0', t - 1.4, t + 0.4, (42, 10))
t = d.pas(b, t + 0.1, rec(d, 'b4', t + 1.0), 0.9); d.carry(b, 'b4', t, t + 0.3); tg = shoot(d, b, t + 0.35, (46, 1))   # max tre touch
fp = [(0, 'Sju mot sju med målvakter', 'Inläggszoner på kanterna.'),
      (1.4, 'En spelare i inläggszonen', 'Får inte pressas där.'),
      (tg - 1.4, 'Inlägg', 'Avslut på max tre touch.'),
      (tg + 0.4, 'Inspark i stället för inkast', 'Sista 5–10 minuterna: fritt spel.')]
finish(d, 'wb01', '7-mot-7-med-fria-inlaggszoner', ['7 mot 7', 'Med fria inläggszoner'], 'Plan 50 × 40 m · Inläggszoner på kanterna',
       fp, 'SMÅLAGSSPEL', [('zone', 82, 4, 100, 96, (200, 220, 200), ''), ('zone', 0, 4, 18, 96, (200, 220, 200), '')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ wb02 4 mot 4 med ytspelare ============
d = Drill()
BP = [(30, 64), (70, 62), (44, 46), (58, 78)]; RP = [(34, 36), (66, 34), (52, 54), (40, 22)]
team(d, 'b', B, BP); team(d, 'r', R, RP); team(d, 'y', YEL, [(50, 6), (50, 94), (6, 50), (94, 50)], ['Y'] * 4)
team(d, 'w', WHITE, [(96, 84), (96, 88), (96, 92), (96, 96)], [''] * 4)
for k in range(4): wander(d, f'r{k}', 0, 6, boxes([RP[k]], 4)[0], 4000 + k, 1.6)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b2'], 0.3); t = d.pas(b, t + 0.2, rec(d, 'y3', t + 1.2)); ty = t                    # via ytspelaren
d.mv('b1', t - 1.0, t + 0.6, (66, 28)); t = d.pas(b, t + 0.1, rec(d, 'b1', t + 0.9))                        # två touch
d.carry(b, 'b1', t, t + 0.3); tg = d.pas(b, t + 0.4, (52, 4), 0.5); hide(d, b, tg + 0.3)
fp = [(0, 'Fyra mot fyra inne', 'Tredje laget vilar.'),
      (ty - 0.8, 'Spela via en ytspelare', 'Innan laget får avsluta.'),
      (tg - 0.6, 'Nu får laget avsluta', ''),
      (tg + 0.4, 'Ytspelarna kan begränsas till två touch', '')]
finish(d, 'wb02', '4-mot-4-med-ytspelare', ['4 mot 4', 'Med ytspelare'], 'Yta 40 × 40 m · Tre lag om fyra plus fyra ytspelare',
       fp, 'SMÅLAGSSPEL', [('box', 10, 10, 90, 90)], [lab(ty, ty + 1.4, (84, 40), 'VIA YTSPELARE')])

# ============ wb03 4 mot 4 med kantspelare ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96))
BP = [(34, 66), (66, 64), (44, 48), (56, 34)]; RP = [(36, 34), (64, 36), (50, 54), (46, 22)]
team(d, 'b', B, BP); team(d, 'r', R, RP); team(d, 'bk', B, [(8, 60), (92, 40)], ['K', 'K']); d.p('rf', 'F', R, (92, 30))
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b2'], 0.3); t = d.pas(b, t + 0.2, rec(d, 'bk1', t + 1.2))
t = drive(d, b, 'bk1', t, (92, 28), 14); d.mv('rf', t - 1.2, t, (90, 26))
d.mv('bk1', t, t + 0.6, (86, 20)); d.carry(b, 'bk1', t, t + 0.6); t += 0.6                                  # 1 mot 1 i korridoren
d.mv('b3', t - 1.4, t + 0.4, (52, 14)); t = d.pas(b, t + 0.1, rec(d, 'b3', t + 1.0), 0.9); tg = shoot(d, b, t + 0.05, (46, 1))
fp = [(0, 'Fyra mot fyra i mitten', 'Två kantspelare per lag utanför.'),
      (1.6, 'Kantspelaren tar 1 mot 1', 'Mot en försvarare i korridoren.'),
      (tg - 1.2, 'Och spelar in', ''),
      (tg + 0.4, 'Variant: dribbla in och skapa 5 mot 4', '')]
finish(d, 'wb03', '4-mot-4-med-kantspelare', ['4 mot 4', 'Med kantspelare'], 'Planens bredd · Kantkorridorer · Ett mål per lag',
       fp, 'SMÅLAGSSPEL', [('zone', 0, 4, 16, 96, (200, 220, 200), ''), ('zone', 84, 4, 100, 96, (200, 220, 200), '')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ wb04 Stoppa bollen på linjen ============
d = Drill()
BP = [(24, 70), (50, 74), (76, 70), (50, 56)]; RP = [(30, 34), (50, 28), (70, 34), (50, 44)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b1', 0))
t = chain(d, b, 0.4, ['b0', 'b3'], 0.3); d.mv('b2', t - 1.4, t + 0.6, (80, 30)); t = d.pas(b, t + 0.2, rec(d, 'b2', t + 1.2))
d.mv('r2', t - 1.0, t + 0.6, (74, 24)); t = drive(d, b, 'b2', t, (82, 12), 16); stand(d, 'b2', t, t + 1.0); d.carry(b, 'b2', t, t + 1.0); tp = t   # stoppar bollen på linjen
hide(d, b, tp + 1.2)
for k in range(4): d.mv(f'b{k}', tp + 1.0, tp + 3.0, BP[k]); d.mv(f'r{k}', tp + 1.0, tp + 3.0, RP[k])
b2 = d.newball((200, 200)); show(d, b2, tp + 3.1, rec(d, 'r1', tp + 3.1))
t = chain(d, b2, tp + 3.3, ['r0', 'r3'], 0.3); t = drive(d, b2, 'r3', t, (46, 86), 16); stand(d, 'r3', t, t + 1.0); d.carry(b2, 'r3', t, t + 1.0); tp2 = t
fp = [(0, 'Fyra mot fyra utan målvakter', 'En mållinje för varje lag.'),
      (tp - 1.0, 'Stoppa bollen på motståndarnas mållinje', 'Då är det mål.'),
      (tp + 3.1, 'Nu anfaller rött', ''),
      (tp2, 'Mål', 'Stopp med sulan på linjen.')]
finish(d, 'wb04', 'stoppa-bollen-pa-linjen', ['Stoppa bollen', 'På linjen'], 'Yta 40 m bred och 20 m djup · En mållinje för varje lag',
       fp, 'SPELÖVNING', [('line', [(6, 12), (94, 12)]), ('line', [(6, 88), (94, 88)])], [lab(tp, tp + 1.6, (82, 20), 'MÅL'), lab(tp2, tp2 + 1.6, (46, 80), 'MÅL')])

# ============ wb05 2 mot 2 med omställning ============
d = Drill()
d.p('a0', 'A', B, (40, 86)); d.p('a1', 'A', B, (60, 86)); d.p('f0', 'F', R, (40, 40)); d.p('f1', 'F', R, (60, 40))
d.p('q0', '', B, (44, 98)); d.p('q1', '', B, (56, 98)); d.p('q2', '', R, (44, 2)); d.p('q3', '', R, (56, 2))
b = d.newball(rec(d, 'a0', 0))
t = drive(d, b, 'a0', 0.4, (42, 60), 16); d.mv('a1', 0.4, t, (62, 60))
d.mv('f0', t - 0.8, t + 0.2, (44, 54)); tw = win(d, b, 'f0', 'a0', t + 0.2, 0.3)                              # försvararna vinner – anfaller direkt
t = d.pas(b, tw + 0.2, rec(d, 'f1', tw + 0.9)); d.mv('f1', tw, t, (60, 56))
t = drive(d, b, 'f1', t, (56, 86), 22); tg = shoot(d, b, t + 0.1, (50, 99)); hide(d, b, tg + 0.3)
d.mv('a0', tw, tg, (46, 80)); d.mv('a1', tw, tg, (58, 76))
d.mv('f0', tg, tg + 2.6, (40, 98)); d.mv('f1', tg, tg + 2.6, (60, 98))                                         # försvararna går sist i kön
d.mv('q2', tg, tg + 1.4, (40, 14)); d.mv('q3', tg, tg + 1.4, (60, 14))                                         # nästa par åt andra hållet
b2 = d.newball((200, 200)); show(d, b2, tg + 1.5, rec(d, 'q2', tg + 1.5))
t = drive(d, b2, 'q2', tg + 1.6, (40, 40), 16); d.mv('q3', tg + 1.6, t, (60, 40)); d.mv('a0', tg + 1.0, t, (44, 52)); d.mv('a1', tg + 1.0, t, (58, 52))
fp = [(0, 'Två anfallare mot två försvarare', 'Par i köer bakom målen.'),
      (tw - 0.2, 'Försvararna vinner – anfall direkt', ''),
      (tg + 0.2, 'Nästa par startar åt andra hållet', 'Försvararna går sist i kön.'),
      (tg + 2.0, 'Nya försvarare', '')]
finish(d, 'wb05', '2-mot-2-med-omstallning', ['2 mot 2', 'Med omställning'], 'Yta 30 × 40 m · Två mål · Par i köer bakom målen',
       fp, 'DUELL', [('box', 20, 4, 80, 96)])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ wb06 6 mot 6 + 1 – passningsspel ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96)); d.p('n', 'N', YEL, (50, 50))
BP = [(28, 78), (72, 78), (36, 60), (64, 60), (50, 70)]; RP = [(28, 22), (72, 22), (36, 40), (64, 40), (50, 30)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
for k in range(5): wander(d, f'r{k}', 0, 7, boxes([RP[k]], 4)[0], 4100 + k, 1.6)
b = d.newball(rec(d, 'mvb', 0))
t = d.pas(b, 0.4, rec(d, 'b0', 1.3)); tstart = 0.4                                                          # målvakten rullar ut
t = chain(d, b, t, ['b2', 'n', 'b3', 'b1', 'n', 'b4'], 0.3)
d.mv('b3', t - 1.6, t + 0.4, (60, 26)); t = d.pas(b, t + 0.2, rec(d, 'b3', t + 1.1)); tg = shoot(d, b, t + 0.1, (54, 1))
fp = [(0, 'Målvakten rullar ut', 'Spelet startar alltid så.'),
      (2.0, 'Den neutrala spelar med laget som har bollen', 'Sex mot sex plus en.'),
      (5.0, 'Passningsspel', 'Inspark i stället för inkast.'),
      (tg - 0.6, 'Avslut', 'Byt neutral var 5–10 minut.')]
finish(d, 'wb06', '6-mot-6-plus-1-passningsspel', ['6 mot 6 + 1', 'Passningsspel'], 'Plan 60 × 40 m · Ett mål i varje ände',
       fp, 'SMÅLAGSSPEL', [])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ wb07 Dribbla in i slutzonen ============
d = Drill()
BP = [(30, 62), (70, 60), (40, 44), (60, 46), (50, 70)]; RP = [(34, 32), (66, 34), (44, 54), (58, 40), (50, 28)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b2', 'b3'], 0.3); t = drive(d, b, 'b3', t, (58, 30), 14); d.mv('r4', t - 1.0, t, (56, 26))
d.mv('b3', t, t + 0.5, (66, 26)); d.carry(b, 'b3', t, t + 0.5); d.mv('r4', t, t + 0.5, (58, 24)); tf = t + 0.3   # dribbla förbi en motståndare
d.mv('b3', t + 0.5, t + 1.3, (68, 14)); d.carry(b, 'b3', t + 0.5, t + 1.3); t += 1.3
tg = d.pas(b, t + 0.1, (70, 3), 0.5); hide(d, b, tg + 0.3)
fp = [(0, 'Fem mot fem i mittzonen', 'Slutzoner 10 m in från kortsidorna.'),
      (tf - 0.6, 'Dribbla förbi en motståndare', 'Bara så får man gå in i slutzonen.'),
      (tg - 0.5, 'Avsluta i ett småmål', ''),
      (tg + 0.4, 'Sista 5–10 minuterna', 'En försvarare får gå tillbaka in i zonen.')]
finish(d, 'wb07', 'dribbla-in-i-slutzonen', ['Dribbla in', 'i slutzonen'], 'Yta 50 × 30 m · Slutzoner · Två småmål i varje ände',
       fp, 'SMÅLAGSSPEL', [('box', 8, 2, 92, 98), ('zone', 8, 2, 92, 20, (230, 120, 110), 'SLUTZON'), ('zone', 8, 80, 92, 98, (120, 170, 230), 'SLUTZON'),
                          ('smallgoal', 30, 3), ('smallgoal', 70, 3), ('smallgoal', 30, 97), ('smallgoal', 70, 97)])

# ============ wb09 Koordination med boll i rutor ============
d = Drill(); ex = []
TECH = ['ETT TOUCH', 'KASTA OCH VOLLEY', 'LÅR OCH VOLLEY', 'NICK']
for q, (x0, y0) in enumerate([(10, 10), (52, 10), (10, 52), (52, 52)]):
    pts = [(x0 + 8, y0 + 8), (x0 + 30, y0 + 10), (x0 + 30, y0 + 30), (x0 + 10, y0 + 30)]
    for k in range(4): d.p(f'p{q}{k}', str(k + 1), B, pts[k])
    for k in range(4): wander(d, f'p{q}{k}', 0, 17.9, boxes([pts[k]], 4)[0], 4200 + 10 * q + k, 1.6)
    b = d.newball(rec(d, f'p{q}0', 0)); t = 0.4 + 0.2 * q
    for rep in range(12): t = d.pas(b, t + 0.35, rec(d, f'p{q}{(rep + 1) % 4}', t + 1.0))                       # i ordning 1 till 4
for i, s in enumerate(TECH): ex.append(lab(0.4 + 4 * i, 4.4 + 4 * i, (50, 50), s))
fp = [(0, 'Bollen går 1 till 4', 'Alla rör sig i rutan.'),
      (4.4, 'Ledaren byter teknik', 'Kasta och volley.'),
      (8.4, 'Lår-, bröst- och insidesmottagning', ''),
      (12.4, 'Nick – och dribbling in till mitten', '')]
finish(d, 'wb09', 'koordination-med-boll-i-rutor', ['Koordination', 'Med boll i rutor'], 'Yta 20 × 20 m i fyra rutor · Grupper om fyra',
       fp, 'TEKNIK', [('box', 8, 8, 92, 92), ('line', [(50, 8), (50, 92)]), ('line', [(8, 50), (92, 50)])], ex)

# ============ wb10 Två touch – mottagning i spel ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96))
BP = [(30, 66), (70, 64), (44, 48), (58, 34)]; RP = [(34, 36), (66, 34), (52, 54), (44, 24)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'mvb', 0)); t = d.pas(b, 0.4, rec(d, 'b0', 1.4), 1.0)                                     # målvakten kastar ut
hold = 'b0'
for pid in ['b2', 'b1', 'b3']:
    d.carry(b, hold, t, t + 0.4)                                                                                # mottagning – minst två touch
    t = d.pas(b, t + 0.45, rec(d, pid, t + 1.1)); hold = pid
t1 = d.pas(b, t + 0.05, rec(d, 'b0', t + 0.8)); tf = t1                                                         # ett touch – frispark
hide(d, b, tf + 0.3)
b2 = d.newball((200, 200)); show(d, b2, tf + 1.2, rec(d, 'r2', tf + 1.2))
t = d.pas(b2, tf + 1.5, rec(d, 'r0', tf + 2.3)); d.carry(b2, 'r0', t, t + 0.4); t = d.pas(b2, t + 0.45, rec(d, 'r1', t + 1.1))
fp = [(0, 'Fem mot fem med målvakter', 'Målvakten kastar ut efter mål.'),
      (1.6, 'Minst två touch varje gång', 'Mottagning – sedan passning.'),
      (tf - 0.6, 'Ett touch: frispark till motståndarna', ''),
      (tf + 1.2, 'Sista 5–10 minuterna', 'Fritt antal touch på egen planhalva.')]
finish(d, 'wb10', 'tva-touch-mottagning-i-spel', ['Två touch', 'Mottagning i spel'], 'Yta 40 × 25 m · Ett mål i varje ände',
       fp, 'SMÅLAGSSPEL', [], [lab(tf, tf + 1.6, (60, 50), 'FRISPARK')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ wb11 Fönsteruppvärmning ============
d = Drill()
SV = [(50, 6), (94, 30), (94, 70), (50, 94), (6, 70), (6, 30)]
for k, ps in enumerate(SV): d.p(f's{k}', 'S', ORA, ps)
IN = [(36, 34), (64, 36), (36, 64), (64, 64), (50, 50)]
for k, ps in enumerate(IN): d.p(f'i{k}', '', B, ps)
for k in range(5): wander(d, f'i{k}', 0, 17.9, boxes([IN[k]], 8)[0], 4300 + k, 1.4)
for s in range(3):
    b = d.newball(rec(d, f's{s * 2}', 0)); t = 0.4 + 0.6 * s; srv = s * 2
    for rep in range(5):
        inn = f'i{(s + rep) % 5}'
        t1 = d.pas(b, t, rec(d, inn, t + 1.0)); d.carry(b, inn, t1, t1 + 0.4)                                  # mottagning
        nsrv = (srv + 1 + rep) % 6; t2 = d.pas(b, t1 + 0.45, rec(d, f's{nsrv}', t1 + 1.3)); srv = nsrv; t = t2 + 0.3   # vänd och passa till annan servare
fp = [(0, 'Servarna står på utsidan med boll', 'Hälften jobbar inne.'),
      (1.6, 'Ropa efter boll', 'Passning längs marken eller kast underifrån.'),
      (5.0, 'Mottagning – vänd och passa', 'Till en annan servare.'),
      (11.0, 'Byt roller varje minut', '')]
finish(d, 'wb11', 'fonsteruppvarmning', ['Fönster-', 'uppvärmning'], 'Yta 25 × 25 m · Servare runt om',
       fp, 'PASSNINGSÖVNING', [('box', 12, 12, 88, 88)])

if __name__ == '__main__': render(C, sys.argv)
