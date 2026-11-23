# Externa övningar, omgång 6 (tolv st). Regel: först d.mv, sedan d.carry; hide före show.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e4', __file__.replace('render_extern6.py', 'render_extern4.py'))
e4 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e4); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e4.finish, e4.rec, e4.chain, e4.wander, e4.counter, e4.arrivals
lab, hide, show, team, boxes, drive, shoot = e4.lab, e4.hide, e4.show, e4.team, e4.boxes, e4.drive, e4.shoot
factor, swap_color, stand = e4.factor, e4.swap_color, e4.stand
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'; GRN = '#3fbf5f'

# ============ w29 Väggspel och avslut ============
d = Drill(); d.p('mv', 'MV', R, (50, 5))
d.p('wl', 'V', WHITE, (20, 24)); d.p('wr', 'V', WHITE, (80, 24))
QL = ['l0', 'l1', 'l2']; QR = ['r0', 'r1', 'r2']
for n, pid in enumerate(QL): d.p(pid, '', B, (30, 64 + 6 * n))
for n, pid in enumerate(QR): d.p(pid, '', B, (70, 64 + 6 * n))
balls = {pid: d.newball(rec(d, pid, 0)) for pid in QL + QR}
t = 0.4; shots = []
for rep, (Q, W, sx) in enumerate([(QL, 'wl', 1), (QR, 'wr', -1), (QL, 'wl', 1)]):
    p = Q.pop(0); b = balls[p]; x0 = 30 if sx == 1 else 70
    for n, pid in enumerate(Q): d.mv(pid, t + 0.4, t + 1.2, (x0, 64 + 6 * n))
    t1 = drive(d, b, p, t, (x0 + 2 * sx, 42), 22)                                    # driver mot väggspelaren
    t2 = d.pas(b, t1 + 0.1, rec(d, W, t1 + 0.6))
    d.mv(p, t1 + 0.1, t2 + 0.7, (x0 + 10 * sx, 22))                                  # löper i djupled
    t3 = d.pas(b, t2 + 0.15, rec(d, p, t2 + 0.7)); t4 = shoot(d, b, t3 + 0.05, (50 - 4 * sx, 1)); shots.append(t4)
    d.mv(p, t4 + 0.2, t4 + 2.6, (x0 + 8 * sx, 82)); Q.append(p)                      # tillbaka till kön
    t = t3 - 0.2 if rep == 0 else t3 + 0.2
fp = [(0, 'Driv mot väggspelaren', 'Köerna turas om, en från vänster och en från höger.'),
      (shots[0] - 1.2, 'Väggspel och djupledsboll', 'Avsluta på första eller andra touchen.'),
      (shots[0] + 0.3, 'Nästa från höger', 'Samma sak på andra sidan.'),
      (shots[2] - 1.5, 'Väggspelaren byts varannan minut', 'Tajma löpningen efter passningen.')]
finish(d, 'w29', 'vaggspel-och-avslut', ['Väggspel', 'Och avslut'], 'Mål med målvakt · Två köer ca 25 m ut · En väggspelare på varje sida av straffområdet',
       fp, 'AVSLUT', [('cone', 30, 58), ('cone', 70, 58)])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ w30 Från 1 mot 0 till 1 mot 2 med kontring ============
d = Drill(); d.p('mv', 'MV', R, (50, 5))
team(d, 'a', B, [(50, 70), (50, 76), (50, 82)], ['A', 'A', 'A']); d.p('bb', 'B', R, (24, 46)); d.p('cc', 'C', R, (76, 46))
balls = [d.newball(rec(d, f'a{k}', 0)) for k in range(3)]
# steg 1: 1 mot 0
t = drive(d, balls[0], 'a0', 0.4, (50, 34), 20)
d.path('a0', t, [(44, 30), (54, 26)], 1.3); d.carry(balls[0], 'a0', t, d.pl['a0']['tr'][-1][0]); t = d.pl['a0']['tr'][-1][0]   # finten vid käppen
tg1 = shoot(d, balls[0], t, (42, 1)); d.mv('a0', tg1 + 0.3, tg1 + 2.6, (14, 80))
d.mv('a1', tg1 - 1.5, tg1 - 0.5, (50, 70)); d.mv('a2', tg1 - 1.5, tg1 - 0.5, (50, 76))
# steg 2: 1 mot 1 mot B
t0 = tg1 + 0.2; t = drive(d, balls[1], 'a1', t0, (50, 46), 20); d.mv('bb', t0 + 0.3, t, (46, 38))
d.mv('a1', t, t + 0.8, (60, 34)); d.carry(balls[1], 'a1', t, t + 0.8); d.mv('bb', t, t + 0.9, (54, 36)); t += 0.8   # dribblar förbi
tg2 = shoot(d, balls[1], t + 0.1, (56, 1)); d.mv('a1', tg2 + 0.3, tg2 + 2.6, (18, 84)); d.mv('bb', tg2, tg2 + 1.6, (24, 46))
d.mv('a2', tg2 - 1.0, tg2 - 0.2, (50, 70))
# steg 3: 1 mot 2 mot B och C, försvararna vinner och kontrar
t0 = tg2 + 0.6; t = drive(d, balls[2], 'a2', t0, (50, 48), 20)
d.mv('bb', t0 + 0.2, t, (44, 42)); d.mv('cc', t0, t, (56, 44))
d.mv('cc', t, t + 0.4, rec(d, 'a2', t + 0.4)); tw = d.pas(balls[2], t + 0.2, rec(d, 'cc', t + 0.5), 0.3)   # C vinner bollen
t = drive(d, balls[2], 'cc', tw, (52, 84), 22); tg3 = shoot(d, balls[2], t, (50, 97))                    # kontring mot småmålet
d.mv('bb', tw, tw + 1.6, (44, 70)); d.mv('a2', tw, tw + 1.4, (54, 66))
fp = [(0, 'Steg 1: A dribblar, fintar och avslutar', 'Finten görs vid käppen i straffområdet.'),
      (tg1 + 0.2, 'Steg 2: 1 mot 1 mot B', 'B kliver in som försvarare.'),
      (tg2 + 0.6, 'Steg 3: 1 mot 2 mot B och C', 'Två försvarare kliver in.'),
      (tw - 0.2, 'Försvararna vinner bollen', 'Och kontrar mot småmålet.')]
finish(d, 'w30', 'fran-1-mot-0-till-1-mot-2-med-kontring', ['Från 1 mot 0 till 1 mot 2', 'Med kontring'], 'Mål med målvakt · Positionerna A, B och C · Käpp i straffområdet · Småmål för kontringen',
       fp, 'AVSLUT', [('pole', 50, 28), ('smallgoal', 50, 98), ('text', 24, 52, 'B'), ('text', 76, 52, 'C')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ w31 3 mot 2 i dubbelt straffområde ============
d = Drill(); d.p('mv1', 'MV', G, (50, 4)); d.p('mv2', 'MV', G, (50, 96))
AP = [(30, 72), (50, 78), (70, 72)]; DP = [(40, 40), (60, 40)]
team(d, 'a', B, AP); team(d, 'f', R, DP)
b = d.newball(rec(d, 'a1', 0))
t = d.pas(b, 0.4, rec(d, 'a0', 1.0))
for k, ps in enumerate([(30, 40), (50, 46), (70, 36)]): d.mv(f'a{k}', 0.6, 2.4, ps)
d.mv('f0', 0.6, 2.0, (36, 32)); d.mv('f1', 0.6, 2.0, (58, 30))
d.carry(b, 'a0', t, 2.4); t = d.pas(b, 2.5, rec(d, 'a1', 3.1)); t = d.pas(b, t + 0.2, rec(d, 'a2', t + 0.8))
d.mv('f1', t - 0.8, t + 0.2, (66, 28)); tg = shoot(d, b, t + 0.1, (56, 1))                          # mål
hide(d, b, tg + 0.4)
for k in range(3): d.mv(f'a{k}', tg + 0.2, tg + 2.2, AP[k])
for k in range(2): d.mv(f'f{k}', tg + 0.2, tg + 2.2, DP[k])
show(d, b, tg + 2.3, rec(d, 'a1', tg + 2.3))
t = d.pas(b, tg + 2.5, rec(d, 'a2', tg + 3.1))
for k, ps in enumerate([(32, 46), (50, 52), (66, 50)]): d.mv(f'a{k}', tg + 2.6, tg + 4.0, ps)
d.mv('a2', t, t + 0.8, (66, 50)); d.carry(b, 'a2', t, t + 0.8); t += 0.8
d.mv('f1', t - 1.2, t + 0.2, rec(d, 'a2', t + 0.2)); tw = d.pas(b, t + 0.3, rec(d, 'f1', t + 0.5), 0.3)   # försvararna vinner
t = drive(d, b, 'f1', tw, (58, 80), 22); d.mv('f0', tw, t, (40, 72)); tc = shoot(d, b, t, (44, 99))     # kontring mot andra målet
for k in range(3): d.mv(f'a{k}', tw + 0.2, tw + 1.6, (AP[k][0], 60))
fp = [(0, 'Tre anfallare mot två försvarare', 'Anfallarna försöker göra mål.'),
      (tg - 0.8, 'Mål', 'Ny omgång från startpositionerna.'),
      (tw - 0.2, 'Försvararna vinner bollen', 'Och kontrar mot andra målet.'),
      (tc + 0.2, 'Byt roller efter varje omgång', 'Snabba beslut – avsluta när läget finns.')]
finish(d, 'w31', '3-mot-2-i-dubbelt-straffomrade', ['3 mot 2', 'I dubbelt straffområde'], 'Dubbelt straffområde · Mål och målvakt i båda ändar',
       fp, 'AVSLUT', [('box', 16, 2, 84, 98), ('line', [(16, 50), (84, 50)])])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ w32 Snabbavslut efter vändning ============
d = Drill(); d.p('mv', 'MV', R, (50, 5)); d.p('t', 'T', T_COL, (50, 66))
team(d, 'a', B, [(50, 28), (20, 34), (20, 40)]); team(d, 'f', R, [(58, 42), (80, 44), (80, 50)])
balls = [d.newball((51, 70)), d.newball((53, 70)), d.newball((49, 72))]
t = 0.3; shots = []
Aq = ['a0', 'a1', 'a2']; Fq = ['f0', 'f1', 'f2']
for rep in range(3):
    a = Aq[rep]; f = Fq[rep]; b = balls[rep]
    if rep > 0:
        d.mv(a, t - 1.8, t, (50, 28)); d.mv(f, t - 1.8, t, (58, 42))
    t1 = d.pas(b, t + 0.2, rec(d, a, t + 0.9))                                    # tränaren spelar in
    side = 1 if rep % 2 == 0 else -1
    d.mv(a, t1, t1 + 0.5, (50 - 6 * side, 22)); d.carry(b, a, t1, t1 + 0.5)         # vänder på första touchen
    d.mv(f, t1 - 0.1, t1 + 0.9, (50 - 3 * side, 26))                              # försvararen jagar bakifrån
    tg = shoot(d, b, t1 + 0.55, (50 + 5 * side, 1)); shots.append(tg)
    d.mv(a, tg + 0.3, tg + 2.6, (20, 46 + 4 * rep)); d.mv(f, tg + 0.3, tg + 2.6, (80, 56 + 4 * rep))
    t = tg + 1.2
fp = [(0, 'Tränaren spelar in till anfallaren', 'Försvararen startar en bit bakom.'),
      (shots[0] - 1.0, 'Vänd på första touchen', 'Och avsluta innan försvararen hinner fram.'),
      (shots[0] + 0.4, 'Nästa anfallare', 'Byt sida på vändningen.'),
      (shots[2] - 1.0, 'Snabbt avslut', 'Låg och hård i hörnet.')]
finish(d, 'w32', 'snabbavslut-efter-vandning', ['Snabbavslut', 'Efter vändning'], 'Mål med målvakt · Anfallare vid straffområdet · Tränare med bollar · Försvarare bakom',
       fp, 'AVSLUT', [])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ w33 Cutback-avslut ============
d = Drill(); d.p('mv', 'MV', R, (50, 5)); d.p('f', 'F', R, (50, 14))
d.p('y1', 'Y', B, (88, 42)); d.p('y2', 'Y', B, (12, 42))
team(d, 'l', B, [(40, 32), (58, 34)]); team(d, 'm', B, [(42, 44), (60, 46)])
b1 = d.newball(rec(d, 'y1', 0)); b2 = d.newball(rec(d, 'y2', 0))
t = drive(d, b1, 'y1', 0.4, (86, 7), 22)                                          # mot kortlinjen
d.mv('l0', 0.9, t + 0.4, (58, 7)); d.mv('l1', 0.9, t + 0.6, (50, 16))            # främre stolpen och straffpunkten
d.mv('f', t - 0.4, t + 0.4, (56, 10))
t = d.pas(b1, t + 0.1, rec(d, 'l1', t + 0.7)); tg = shoot(d, b1, t + 0.05, (44, 1))   # direktavslut
d.mv('l0', tg + 0.3, tg + 2.4, (60, 56)); d.mv('l1', tg + 0.3, tg + 2.4, (40, 58)); d.mv('f', tg + 0.3, tg + 1.6, (50, 14))
d.mv('y1', tg, tg + 2.2, (88, 60))
t0 = tg + 0.8; t = drive(d, b2, 'y2', t0, (14, 7), 22)
d.mv('m1', t0 + 0.4, t + 0.4, (42, 7)); d.mv('m0', t0 + 0.4, t + 0.6, (50, 17))
d.mv('f', t - 0.4, t + 0.4, (44, 11))
t = d.pas(b2, t + 0.1, rec(d, 'm0', t + 0.7)); tg2 = shoot(d, b2, t + 0.05, (56, 1))
fp = [(0, 'Yttern driver mot kortlinjen', 'En försvarare står i boxen.'),
      (tg - 1.6, 'Löparna: främre stolpen och straffpunkten', 'Yttern slår en cutback.'),
      (tg - 0.4, 'Avsluta direkt', 'Skjut på första touchen.'),
      (t0, 'Samma sak från andra kanten', 'Tajma löpningarna med inlägget.')]
finish(d, 'w33', 'cutback-avslut', ['Cutback-avslut', 'Avslutsövning'], 'Mål med målvakt · En ytter vid kanten · Två löpare utanför straffområdet',
       fp, 'AVSLUT', [])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ w34 Distansskott efter läggning ============
d = Drill(); d.p('mv', 'MV', R, (50, 5)); d.p('l', 'L', WHITE, (50, 24))
Q = ['q0', 'q1', 'q2', 'q3']
for n, pid in enumerate(Q): d.p(pid, '', B, (50, 64 + 6 * n))
balls = {pid: d.newball(rec(d, pid, 0)) for pid in Q[:3]}
t = 0.4; shots = []
for rep in range(3):
    p = Q[rep]; b = balls[p]; sx = 1 if rep % 2 == 0 else -1
    for n, pid in enumerate(Q[rep + 1:]): d.mv(pid, t + 0.3, t + 1.0, (50, 64 + 6 * n))
    t1 = d.pas(b, t, rec(d, 'l', t + 0.8))                                         # in till läggaren
    d.mv(p, t + 0.2, t1 + 0.7, (50 - 10 * sx, 38))
    t2 = d.pas(b, t1 + 0.1, rec(d, p, t1 + 0.7)); tg = shoot(d, b, t2 + 0.05, (50 + 4 * sx, 1)); shots.append(tg)   # snett tillbaka, skott direkt
    d.mv(p, tg + 0.3, tg + 2.8, (50 + 16 * sx, 84 + 4 * rep))
    t = tg + 0.3
d.mv('q3', shots[2] + 0.4, shots[2] + 2.0, (50, 26)); d.mv('l', shots[2] + 0.4, shots[2] + 2.4, (64, 80))   # byt läggare
fp = [(0, 'Spela in till läggaren', 'Läggaren står med ryggen mot mål.'),
      (shots[0] - 1.1, 'Läggning snett tillbaka', 'Skjut direkt från distans.'),
      (shots[1] - 1.1, 'Nästa spelare', 'Träffa målet – låg och hård.'),
      (shots[2] + 0.4, 'Byt läggare efter tre skott', 'Ny läggare från kön.')]
finish(d, 'w34', 'distansskott-efter-laggning', ['Distansskott', 'Efter läggning'], 'Mål med målvakt · En läggare vid straffområdet · Kö 25 m ut',
       fp, 'AVSLUT', [], counter(shots, pos=(80, 30), last=None))
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ w35 8 mot 6 – spelvändning mot svaga sidan ============
d = Drill(); d.p('t', 'T', T_COL, (96, 50))
BP = [(22, 82), (40, 86), (60, 86), (78, 82), (30, 64), (52, 66), (72, 62), (50, 48)]; RP = [(26, 30), (44, 26), (60, 26), (74, 30), (40, 44), (60, 44)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 't', 0))
t = d.pas(b, 0.4, rec(d, 'b4', 1.2))
for k, ps in enumerate([(26, 40), (40, 30), (58, 34), (34, 50), (48, 52), (62, 48)]): d.mv(f'r{k}', 0.6, 3.0, (ps[0] - 6, ps[1]))   # rött flyttar mot bollsidan
t = chain(d, b, t, ['b0', 'b5'], 0.25)
for k, ps in [(3, (84, 40)), (6, (74, 30))]: d.mv(f'b{k}', t - 1.4, t + 0.8, ps)
t = d.pas(b, t + 0.2, rec(d, 'b3', t + 1.3)); tsw = t                                   # spelvändning mot svaga sidan
t = drive(d, b, 'b3', t, (78, 22), 22); t = d.pas(b, t + 0.1, rec(d, 'b6', t + 0.7)); tg = shoot(d, b, t + 0.05, (70, 7)); hide(d, b, tg + 0.4)   # mål i småmålet
d.mv('r3', tsw, tsw + 1.6, (76, 26))
b2 = d.newball((200, 200)); show(d, b2, tg + 0.5, rec(d, 'r1', tg + 0.5))                # rött startar snabbt med ny boll
t = d.pas(b2, tg + 0.7, rec(d, 'r4', tg + 1.3)); t = d.pas(b2, t + 0.2, rec(d, 'r5', t + 0.8))
d.mv('b5', t - 1.2, t + 0.2, rec(d, 'r5', t + 0.2)); tw = d.pas(b2, t + 0.3, rec(d, 'b5', t + 0.5), 0.3)   # blått vinner och anfaller direkt
t = d.pas(b2, tw + 0.2, rec(d, 'b7', tw + 0.9)); t = drive(d, b2, 'b7', t, (34, 16), 22); tg2 = shoot(d, b2, t, (30, 7)); hide(d, b2, tg2 + 0.4)
d.mv('b7', tw - 1.0, tw + 0.6, (44, 34))
fp = [(0, 'Tränaren startar med en passning', 'Åtta mot sex, två småmål i varje ände.'),
      (tsw - 1.0, 'Spelvändning mot svaga sidan', 'Där försvaret är tunt.'),
      (tg - 0.6, 'Mål i valfritt småmål', 'Efter mål startar det andra laget snabbt med ny boll.'),
      (tw - 0.2, 'Bollvinst: anfall direkt', 'Laget som vinner bollen anfaller direkt.')]
finish(d, 'w35', '8-mot-6-spelvandning-mot-svaga-sidan', ['8 mot 6', 'Spelvändning mot svaga sidan'], 'Yta 35 × 35 m · Två småmål i varje ände · Bollar runt planen',
       fp, 'SPELVÄNDNING', [('box', 8, 8, 92, 92), ('smallgoal', 30, 8), ('smallgoal', 70, 8), ('smallgoal', 30, 92), ('smallgoal', 70, 92)],
       [lab(tsw - 0.6, tsw + 1.0, (50, 74), 'SPELVÄNDNING')])

# ============ w36 4 mot 4 + 3 mot fyra småmål ============
d = Drill()
d.p('nt', 'N', YEL, (50, 15)); d.p('nb', 'N', YEL, (50, 85)); d.p('ni', 'N', YEL, (50, 50))
team(d, 'b', B, [(42, 60), (58, 40), (11, 50), (89, 50)]); team(d, 'r', R, [(36, 40), (62, 30), (40, 70), (64, 62)])
b = d.newball(rec(d, 'b2', 0))
for k, bx in enumerate([(32, 32, 44, 46), (56, 24, 70, 36), (34, 62, 46, 76), (58, 56, 70, 70)]): wander(d, f'r{k}', 0, 7.2, bx, 960 + k, 1.6)
wander(d, 'ni', 0, 17.9, (46, 46, 56, 56), 970, 1.6)
t = chain(d, b, 0.4, ['b0', 'ni', 'b1'], 0.3)
t = d.pas(b, t + 0.2, rec(d, 'nt', t + 0.8)); t = d.pas(b, t + 0.05, rec(d, 'b1', t + 0.5), 0.45)   # läggning från neutral (ett touch)
d.mv('b1', t - 0.9, t, (56, 24)); tg = shoot(d, b, t + 0.05, (64, 8)); tp = tg; hide(d, b, tg + 0.4)                      # direkt i mål
b2 = d.newball((200, 200)); show(d, b2, tg + 0.5, rec(d, 'b3', tg + 0.5))
t = d.pas(b2, tg + 0.7, rec(d, 'b0', tg + 1.4)); t = d.pas(b2, t + 0.2, rec(d, 'nb', t + 0.8))
d.mv('r3', t - 0.4, t + 0.6, rec(d, 'nb', t + 0.7) if False else (58, 76))
t = d.pas(b2, t + 0.05, (56, 78), 0.4); tw = t; d.mv('r3', t - 0.6, t, (56, 76))                  # rött bryter läggningen
d.carry(b2, 'r3', tw, tw + 0.3)
for k, ps in [(2, (34, 44)), (3, (66, 44))]: d.mv(f'b{k}', tw + 0.2, tw + 1.8, ps)              # kantspelarna går in
for k, ps in [(0, (11, 50)), (1, (89, 50))]: d.mv(f'r{k}', tw + 0.2, tw + 2.0, ps)
t = d.pas(b2, tw + 0.4, rec(d, 'r2', tw + 1.0)); t = chain(d, b2, t, ['r0', 'ni', 'r1'], 0.3)
fp = [(0, 'Två inne och två på kanterna', 'De neutrala spelar alltid med laget som har bollen.'),
      (tp - 1.4, 'Läggning från neutral vid målet', 'De neutrala vid målen har ett touch.'),
      (tp - 0.4, 'Mål direkt efter läggningen', 'Bara då räknas målet.'),
      (tw - 0.2, 'Bollvinst: lagen byter roller', 'Kantspelarna går in.')]
finish(d, 'w36', '4-mot-4-plus-3-mot-fyra-smamal', ['4 mot 4 + 3', 'Mot fyra småmål'], 'Kvadrat med två småmål på två av sidorna · 4 mot 4 och tre neutrala',
       fp, 'SMÅLAGSSPEL', [('box', 8, 8, 92, 92), ('smallgoal', 36, 8), ('smallgoal', 64, 8), ('smallgoal', 36, 92), ('smallgoal', 64, 92)],
       [lab(tp, tp + 1.6, (64, 18), '+1')])

# ============ w37 Från 1 mot 0 till 3 mot 3 ============
d = Drill(); d.p('mvb', 'MV', B, (50, 95)); d.p('mvr', 'MV', R, (50, 5))
team(d, 'b', B, [(6, 60), (6, 68), (6, 76)]); team(d, 'r', R, [(94, 24), (94, 32), (94, 40)])
b = d.newball(rec(d, 'mvb', 0)); st = []
# 1 mot 0
d.mv('b0', 0.2, 1.4, (40, 80)); t = d.pas(b, 1.0, rec(d, 'b0', 1.6)); st.append(0)
t = drive(d, b, 'b0', t, (46, 26), 26); tg = shoot(d, b, t, (44, 1))
hide(d, b, tg + 0.3); show(d, b, tg + 1.0, rec(d, 'mvr', tg + 1.0))                              # ny start från målvakten
# 1 mot 1
st.append(tg + 0.6); d.mv('r0', tg - 0.6, tg + 1.2, (60, 30)); d.mv('b0', tg + 0.2, tg + 1.6, (50, 50))
t = d.pas(b, tg + 1.2, rec(d, 'r0', tg + 1.8)); t = drive(d, b, 'r0', t, (54, 50), 22)
d.mv('b0', t - 0.4, t + 0.3, rec(d, 'r0', t + 0.3)); tw = d.pas(b, t + 0.35, rec(d, 'b0', t + 0.6), 0.3)   # blått vinner och anfaller direkt
t = drive(d, b, 'b0', tw, (52, 22), 24); tg2 = shoot(d, b, t, (56, 1))
d.mv('r0', tw, tw + 1.2, (62, 30))
hide(d, b, tg2 + 0.3); show(d, b, tg2 + 1.0, rec(d, 'mvb', tg2 + 1.0))
# 2 mot 1 (sedan 2 mot 2 och 3 mot 3)
st.append(tg2 + 0.6); d.mv('b1', tg2 - 0.4, tg2 + 1.4, (32, 76)); d.mv('b0', tg2 + 0.2, tg2 + 1.6, (62, 70))
t = d.pas(b, tg2 + 1.2, rec(d, 'b1', tg2 + 1.9)); d.mv('r0', tg2 + 0.8, t + 0.8, (50, 44))
t = drive(d, b, 'b1', t, (40, 44), 24); d.mv('b0', t - 1.6, t + 0.4, (62, 34))
t = d.pas(b, t + 0.1, rec(d, 'b0', t + 0.7)); tg3 = shoot(d, b, t + 0.05, (54, 1))
d.mv('r1', tg3 - 0.6, tg3 + 1.2, (70, 26)); d.mv('b2', tg3 - 0.6, tg3 + 1.4, (30, 84))
fp = [(0, '1 mot 0', 'Anfallet startar från målvakten.'),
      (st[1], '1 mot 1', 'Laget som vinner bollen anfaller direkt.'),
      (st[2], '2 mot 1', 'Varje anfall lägger till en spelare.'),
      (tg3 + 0.3, 'Sedan 2 mot 2 och 3 mot 3', 'Ny start från målvakten efter mål eller boll ut.')]
finish(d, 'w37', 'fran-1-mot-0-till-3-mot-3', ['Från 1 mot 0', 'Till 3 mot 3'], 'Kvadrat ca 30 × 30 m · Mål och målvakt i båda ändar',
       fp, 'SMÅLAGSSPEL', [('box', 10, 2, 90, 98)])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ w38 Från 4 mot 1 till 5 mot 5 ============
d = Drill(); d.p('mvr', 'MV', R, (50, 5)); d.p('mvb', 'MV', B, (50, 95))
AP = [(26, 72), (42, 78), (58, 78), (74, 72)]; team(d, 'a', B, AP)
team(d, 'f', R, [(50, 34), (94, 40), (94, 48), (94, 56)])
b = d.newball(rec(d, 'a1', 0)); st = [0]
# 4 mot 1
for k, ps in enumerate([(28, 40), (44, 48), (60, 44), (74, 30)]): d.mv(f'a{k}', 0.4, 2.0, ps)
d.carry(b, 'a1', 0, 2.0); t = chain(d, b, 2.0, ['a2', 'a3'], 0.2); d.mv('f0', 1.4, t, (64, 36))
tg = shoot(d, b, t + 0.1, (58, 1)); hide(d, b, tg + 0.3)
for k in range(4): d.mv(f'a{k}', tg + 0.2, tg + 2.0, AP[k])
d.mv('f0', tg, tg + 1.6, (42, 36)); d.mv('f1', tg - 0.4, tg + 1.6, (60, 32))                     # ny försvarare kommer in
show(d, b, tg + 2.1, rec(d, 'a1', tg + 2.1)); st.append(tg + 0.4)
# 4 mot 2
for k, ps in enumerate([(28, 42), (44, 50), (60, 46), (74, 32)]): d.mv(f'a{k}', tg + 2.3, tg + 3.9, ps)
d.carry(b, 'a1', tg + 2.1, tg + 3.9); t = chain(d, b, tg + 3.9, ['a0', 'a1'], 0.2)
d.mv('f0', t - 0.8, t, (40, 38)); tg2 = shoot(d, b, t + 0.1, (46, 1)); hide(d, b, tg2 + 0.3)
for k in range(4): d.mv(f'a{k}', tg2 + 0.2, tg2 + 2.0, AP[k])
d.mv('f2', tg2 - 0.4, tg2 + 1.6, (50, 46)); st.append(tg2 + 0.4)
show(d, b, tg2 + 2.1, rec(d, 'a1', tg2 + 2.1))
# 4 mot 3: försvararna vinner och kontrar
t = d.pas(b, tg2 + 2.3, rec(d, 'a2', tg2 + 3.0)); d.mv('f2', t - 0.8, t + 0.2, rec(d, 'a2', t + 0.2))
tw = d.pas(b, t + 0.3, rec(d, 'f2', t + 0.5), 0.3); t = drive(d, b, 'f2', tw, (52, 84), 24); tc = shoot(d, b, t, (46, 99))
d.mv('a2', tw, tw + 1.6, (56, 74))
fp = [(0, 'Fyra anfallare mot en försvarare', 'Anfall mot mål.'),
      (st[1], 'Ny försvarare kommer in', 'Nu 4 mot 2.'),
      (st[2], '4 mot 3', 'Efter varje anfall kommer en ny försvarare in, tills det är 5 mot 5.'),
      (tw - 0.2, 'Försvararna vinner bollen', 'Och kontrar mot motsatt mål.')]
finish(d, 'w38', 'fran-4-mot-1-till-5-mot-5', ['Från 4 mot 1', 'Till 5 mot 5'], 'Kvadrat ca 30 × 30 m · Mål och målvakt i båda ändar',
       fp, 'SMÅLAGSSPEL', [('box', 10, 2, 90, 98)])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ w39 Spel mot fyra mål ============
d = Drill()
BP = [(20, 84), (50, 80), (80, 84), (34, 62), (66, 62)]; RP = [(20, 18), (50, 22), (80, 18), (34, 40), (66, 40)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b1', 0))
t = chain(d, b, 0.4, ['b0', 'b3'], 0.3)
for k, ps in enumerate([(14, 24), (32, 22), (60, 24), (24, 40), (42, 42)]): d.mv(f'r{k}', 0.6, t + 0.6, ps)   # rött flyttar mot bollsidan
d.mv('b4', t - 1.2, t + 0.6, (74, 36)); d.mv('b2', t - 1.2, t + 0.8, (84, 46))
t = d.pas(b, t + 0.2, rec(d, 'b2', t + 1.3)); tsw = t                                               # spelvändning
t = drive(d, b, 'b2', t, (78, 22), 24); tg = shoot(d, b, t, (76, 1))                                 # mål efter spelvändning: dubbelt
hide(d, b, tg + 0.4)
for k in range(5): d.mv(f'b{k}', tg + 0.2, tg + 2.4, BP[k]); d.mv(f'r{k}', tg + 0.2, tg + 2.4, RP[k])
show(d, b, tg + 2.5, rec(d, 'r1', tg + 2.5))
t = chain(d, b, tg + 2.7, ['r3', 'r0'], 0.3); t = drive(d, b, 'r0', t, (24, 76), 24); tg2 = shoot(d, b, t, (26, 99))
for k, ps in enumerate([(26, 86), (40, 80), (64, 80), (34, 70), (56, 66)]): d.mv(f'b{k}', tg + 2.8, tg2, ps)
d.mv('r3', tg + 3.4, tg2, (36, 62))
fp = [(0, 'Varje lag anfaller två mål', 'Och försvarar två.'),
      (tsw - 1.0, 'Spelvändning', 'Flytta spelet till sidan där det är tomt.'),
      (tg - 0.4, 'Mål efter spelvändning: dubbla poäng', 'Mål i valfritt av motståndarnas två mål.'),
      (tg + 2.5, 'Rött anfaller', 'Ett vanligt mål ger en poäng.')]
finish(d, 'w39', 'spel-mot-fyra-mal', ['Spel mot', 'fyra mål'], 'Plan med två mål i varje ände, långt isär · Två lag om 5–7',
       fp, 'SMÅLAGSSPEL', [], [lab(tg, tg + 1.8, (76, 12), 'x2'), lab(tg2, tg2 + 1.8, (26, 88), '+1')])
C[-1]['goals'] = [(24, 0), (76, 0), (24, 100), (76, 100)]; C[-1]['keep_goals'] = True

# ============ w40 Bollinnehav och femsekundersanfall ============
d = Drill(); d.p('mv', 'MV', R, (50, 5)); d.p('t', 'T', T_COL, (96, 56))
BP = [(24, 86), (50, 90), (76, 86), (30, 66), (70, 66), (50, 72)]; RP = [(36, 56), (64, 56), (50, 40), (50, 62)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
for k in range(4): wander(d, f'r{k}', 0, 6.4, boxes([RP[k]], 4)[0], 980 + k, 2.2)
b = d.newball(rec(d, 'b1', 0))
t = chain(d, b, 0.4, ['b0', 'b3', 'b5', 'b4', 'b2', 'b1'], 0.35)                                   # innehav i egen halva, passiva försvarare
tsig = t + 0.2
for k, ps in enumerate([(24, 30), (40, 20), (76, 34)]): d.mv(f'b{k + 3}', tsig, tsig + 2.2, ps)
t = d.pas(b, tsig + 0.3, rec(d, 'b4', tsig + 1.4)); t = drive(d, b, 'b4', t, (70, 30), 24)
t = d.pas(b, t + 0.1, rec(d, 'b3', t + 0.8)); tg = shoot(d, b, t + 0.05, (44, 1))
for k, ps in enumerate([(40, 44), (60, 44), (50, 30), (58, 24)]): d.mv(f'r{k}', tsig, tsig + 2.6, ps)
fp = [(0, 'Laget med boll håller den i egen halva', 'Mot passiva försvarare.'),
      (tsig, 'Tränarens signal: fem sekunder', 'In i motståndarhalvan och gör mål.'),
      (tg - 0.5, 'Mål inom fem sekunder', 'Snabbt framåt – få touch.'),
      (tg + 0.6, 'Yngre spelare får 8–10 sekunder', 'Sedan nytt bollinnehav.')]
finish(d, 'w40', 'bollinnehav-och-femsekundersanfall', ['Bollinnehav och', 'femsekundersanfall'], 'Halvplan eller hel plan · Mål med målvakt',
       fp, 'KONTRING', [('line', [(2, 50), (98, 50)])],
       [dict(kind='signal', t0=tsig, t1=tsig + 5, pos=(96, 56), color=GRN)] + [lab(tsig + i, tsig + i + 1, (84, 44), str(5 - i)) for i in range(5)])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

if __name__ == '__main__': render(C, sys.argv)
