# Externa övningar, omgång 15 (tolv st). Regel: först d.mv, sedan d.carry; först mottagarens rörelse, sedan passningen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e9', __file__.replace('render_extern15.py', 'render_extern9.py'))
e9 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e9); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e9.finish, e9.rec, e9.chain, e9.wander, e9.counter, e9.arrivals
lab, hide, show, team, boxes, drive, shoot = e9.lab, e9.hide, e9.show, e9.team, e9.boxes, e9.drive, e9.shoot
factor, swap_color, stand, countdown, countup, win = e9.factor, e9.swap_color, e9.stand, e9.countdown, e9.countup, e9.win
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'

# ============ ok12 Stjärna i kvadrat ============
d = Drill()
CR = [(16, 16), (84, 16), (84, 84), (16, 84)]
OUT = [(-5, -4), (5, -4), (5, 4), (-5, 4)]
for c in range(4):
    for n in range(2): d.p(f'c{c}{n}', '', B, (CR[c][0] + OUT[c][0] * n, CR[c][1] + OUT[c][1] * n))
Q = {c: [f'c{c}0', f'c{c}1'] for c in range(4)}
def qpos(c, n): return (CR[c][0] + OUT[c][0] * n, CR[c][1] + OUT[c][1] * n)
bA = d.newball(rec(d, 'c00', 0)); bB = d.newball(rec(d, 'c10', 0))
for ball, c0, toff in ((bA, 0, 0.4), (bB, 1, 1.6)):
    c = c0; t = toff
    for lap in range(4):
        oc = (c + 2) % 4; p = Q[c].pop(0)
        for n, w in enumerate(Q[c]): d.mv(w, t + 0.4, t + 1.0, qpos(c, n))
        side = 4 if ball == bA else -4
        mid = (50 + side, 50 - side)
        t2 = d.path(p, t, [mid, (CR[oc][0] - OUT[oc][0] * 0.8, CR[oc][1] - OUT[oc][1] * 0.8)], 1.2); d.carry(ball, p, t, t2)   # rakt över
        nxt = Q[oc][0]
        t3 = d.pas(ball, t2 + 0.1, rec(d, nxt, t2 + 0.5), 0.4)                                        # lämna över
        d.mv(p, t2 + 0.3, t2 + 1.2, qpos(oc, len(Q[oc]))); Q[oc].append(p)
        c = oc; t = t3 + 0.1
fp = [(0, 'Spelare i hörnen', 'Driv rakt över till paret mitt emot.'),
      (1.6, 'En boll per rad', 'Två rader korsar varandra i mitten.'),
      (5.0, 'Lämna över och ställ dig sist', ''),
      (10.0, 'Uppgradering: fler bollar och finter', 'Finta varandra när ni möts.')]
finish(d, 'ok12', 'stjarna-i-kvadrat', ['Stjärna', 'I kvadrat'], 'Kvadrat ca 25 × 25 m · Spelare i hörnen',
       fp, 'TEKNIK', [('cone',) + c for c in CR])

# ============ ok13 1 mot 1 med fint ============
d = Drill()
LX = [24, 50, 76]
for li, x in enumerate(LX):
    d.p(f'a{li}', 'A', B, (x, 84)); d.p(f'f{li}', 'F', R, (x, 30))
balls = [d.newball(rec(d, f'a{li}', 0)) for li in range(3)]
for li, x in enumerate(LX):
    a, f = f'a{li}', f'f{li}'; b = balls[li]; t = 0.4 + 0.3 * li
    for rep in range(2):
        y0, y1, ydef = (84, 12, 46) if rep == 0 else (12, 84, 50)
        d.mv(f, t, t + 1.2, (x, ydef)); t1 = t + 1.4
        d.mv(a, t, t1, (x, (y0 + ydef) / 2 + (6 if rep == 0 else -6))); d.carry(b, a, t, t1)
        d.mv(a, t1, t1 + 0.5, (x + 5, ydef)); d.carry(b, a, t1, t1 + 0.5); d.mv(f, t1, t1 + 0.5, (x - 2, ydef))   # fint
        d.mv(a, t1 + 0.5, t1 + 1.8, (x, y1)); d.carry(b, a, t1 + 0.5, t1 + 1.8); tt = t1 + 1.8                  # till andra sidan
        d.mv(f, t1 + 0.6, tt, (x, y1 + (10 if rep == 0 else -10)))
        a, f = f, a; t = tt + 0.3                                                                             # lämna över – nytt anfall åt andra hållet
fp = [(0, 'Anfallaren driver mot försvararen', 'Kanal ca 5 × 20 m.'),
      (1.6, 'Fint och förbi', 'Ta dig till andra sidan.'),
      (4.0, 'Lämna över – nytt anfall åt andra hållet', 'Nu är det den andra som anfaller.'),
      (8.0, 'Vinner försvararen bollen?', 'Lämna tillbaka den.')]
finish(d, 'ok13', '1-mot-1-med-fint', ['1 mot 1', 'Med fint'], 'Kanal ca 5 × 20 m · Två spelare per boll',
       fp, 'DUELL', [('box', x - 9, 8, x + 9, 88) for x in LX])

# ============ ok14 Nöta – mottagning förbi konen ============
d = Drill()
YS = [26, 50, 74]
for k, y in enumerate(YS): d.p(f'l{k}', '', B, (24, y)); d.p(f'r{k}', '', B, (76, y))
balls = [d.newball(rec(d, f'l{k}', 0)) for k in range(3)]
for k, y in enumerate(YS):
    t = 0.4 + 0.3 * k; hold, recv = f'l{k}', f'r{k}'; side = 1
    for rep in range(5):
        rx = 76 if recv[0] == 'r' else 24
        d.mv(recv, t, t + 0.6, (rx, y - 4 * side))
        t1 = d.pas(balls[k], t + 0.1, rec(d, recv, t + 0.8))
        d.mv(recv, t1, t1 + 0.5, (rx, y + 4 * side)); d.carry(balls[k], recv, t1, t1 + 0.5)                  # första touchen förbi konen
        hold, recv = recv, hold; side = -side; t = t1 + 0.6
fp = [(0, 'Paret passar fram och tillbaka', 'Två koner 5–10 m isär.'),
      (1.2, 'Första touchen förbi konen', 'Från ena sidan av konen till den andra.'),
      (5.0, 'Spela på tå', 'Redo för nästa boll.'),
      (10.0, 'Båda fötterna', 'Växla sida varje gång.')]
finish(d, 'ok14', 'nota-mottagning-forbi-konen', ['Nöta', 'Mottagning förbi konen'], 'Två koner 5–10 m isär · Två spelare per boll',
       fp, 'PASSNINGSÖVNING', [('cone', 24, y) for y in YS] + [('cone', 76, y) for y in YS])

# ============ ok15 Sicksackpassningar ============
d = Drill()
CN = [(40, 86), (60, 72), (40, 58), (60, 44), (40, 30), (60, 16)]
for k in range(5): d.p(f'p{k}', '', B, (CN[k][0] + (-5 if CN[k][0] < 50 else 5), CN[k][1]))
d.p('q', '', B, (34, 94))
occ = [f'p{k}' for k in range(5)] + [None]
b = d.newball(rec(d, 'p0', 0)); t = 0.4; spots = lambda k: (CN[k][0] + (-5 if CN[k][0] < 50 else 5), CN[k][1])
for k in range(5):
    p, r = occ[k], occ[k + 1]
    if r is None:
        break
    t1 = d.pas(b, t, rec(d, r, t + 0.9))
    d.mv(r, t1, t1 + 0.6, (CN[k + 1][0], CN[k + 1][1] - 5)); d.carry(b, r, t1, t1 + 0.6)                     # runt konen
    d.mv(p, t + 0.3, t1 + 1.6, spots(k + 1) if False else (spots(k)[0] + 0, spots(k)[1]))
    t = t1 + 0.7
# sista mottagaren driver till lediga platsen högst upp; alla flyttar ett steg
last = occ[4]; d.mv(last, t, t + 1.2, spots(5)); d.carry(b, last, t, t + 1.2); t += 1.2
for k in range(4): d.mv(occ[k], t - 0.6, t + 1.2, spots(k + 1))
d.mv('q', t - 0.4, t + 1.0, spots(0))
occ = ['q'] + occ[:4] + [last]
t = d.pas(b, t + 0.2, rec(d, occ[4], t + 1.2)) if False else t
t2 = d.pas(b, t + 0.3, rec(d, 'q', t + 2.4), 1.8)                                                             # tillbaka till starten
fp = [(0, 'Passa snett framåt', 'Koner i sicksack, 5 m mellan.'),
      (1.4, 'Flytta bollen runt konen', 'Och passa vidare.'),
      (t - 1.0, 'Den som passat tar den lediga platsen', 'Alla flyttar ett steg.'),
      (t2 - 1.0, 'Ny runda', '')]
finish(d, 'ok15', 'sicksackpassningar', ['Sicksack-', 'passningar'], 'Koner i sicksack · 5 m mellan åt alla håll',
       fp, 'PASSNINGSÖVNING', [('cone',) + c for c in CN])

# ============ ok16 Nummerboll ============
d = Drill()
G1 = [(24, 30), (40, 22), (34, 44)]; G2 = [(66, 60), (80, 70), (62, 78)]
team(d, 'a', B, G1); team(d, 'b', R, G2)
for k in range(3): wander(d, f'a{k}', 0, 17.9, boxes([G1[k]], 9)[0], 3000 + k, 1.6); wander(d, f'b{k}', 0, 17.9, boxes([G2[k]], 9)[0], 3010 + k, 1.6)
bA = d.newball(rec(d, 'a0', 0)); bB = d.newball(rec(d, 'b0', 0))
t = chain(d, bA, 0.4, ['a1', 'a2', 'a0', 'a1', 'a2', 'a0'], 0.5); tsw = t
t = chain(d, bA, t, ['a2', 'a1', 'a0', 'a2', 'a1'], 0.5)                                                 # byt håll
t = chain(d, bB, 0.8, ['b1', 'b2', 'b0', 'b1', 'b2', 'b0'], 0.5); t = chain(d, bB, t, ['b2', 'b1', 'b0', 'b2'], 0.5)
fp = [(0, '1 passar 2, 2 passar 3', 'Tre spelare per boll.'),
      (2.4, 'Rör dig hela tiden', 'Sök nya ytor.'),
      (tsw - 0.2, 'Byt håll', '3 till 2 och 2 till 1.'),
      (tsw + 3.0, 'Se dig om innan du får bollen', '')]
finish(d, 'ok16', 'nummerboll', ['Nummerboll', 'Passningsövning'], 'Yta 25 × 20 m · Tre spelare per boll',
       fp, 'PASSNINGSÖVNING', [('box', 8, 8, 92, 92)], [lab(tsw, tsw + 1.6, (50, 50), 'BYT HÅLL')])

# ============ ok17 Teknikbana med avslut ============
d = Drill(); d.p('mv1', 'MV', R, (50, 4)); d.p('mv2', 'MV', R, (50, 96))
for k in range(3): d.p(f'u{k}', '', B, (20 - 8 * k, 94)); d.p(f'o{k}', '', B, (80 + 8 * k, 6))
COURSE_U = [(30, 80), (40, 72), (30, 64), (44, 56)]; COURSE_O = [(70, 20), (60, 28), (70, 36), (56, 44)]
bu = [d.newball(rec(d, f'u{k}', 0)) for k in range(2)]; bo = [d.newball(rec(d, f'o{k}', 0)) for k in range(2)]
t = 0.4
for rnd in range(2):
    for side, pre, course, goal, bl in (('u', 'u', COURSE_U, (46, 1), bu), ('o', 'o', COURSE_O, (54, 99), bo)):
        pid = f'{pre}{rnd}'
        d.carry(bl[rnd], pid, 0, t)
        t2 = d.path(pid, t, course + [(50, 50)], 1.4); d.carry(bl[rnd], pid, t, t2)                         # genom banan till konen
        tg = shoot(d, bl[rnd], t2 + 0.1, goal); hide(d, bl[rnd], tg + 0.4)
        home = (90, 18 + 7 * rnd) if pre == 'u' else (10, 82 - 7 * rnd)
        d.mv(pid, tg + 0.2, tg + 3.0, home)                                                                  # ställ dig sist på andra sidan
        t = t2 - 0.6
fp = [(0, 'Genom teknikbanan till konen', 'En och en.'),
      (2.6, 'Skott från konen', ''),
      (4.0, 'Hämta bollen – ställ dig sist på andra sidan', ''),
      (8.0, 'Samma sak från andra hållet', 'Två mål ca 20 m isär.')]
finish(d, 'ok17', 'teknikbana-med-avslut', ['Teknikbana', 'Med avslut'], 'Två mål ca 20 m isär · Teknikbana till en kon i mitten',
       fp, 'AVSLUT', [('cone',) + c for c in COURSE_U + COURSE_O] + [('cone', 50, 50)])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ ok18 Trollenäsaren ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
for k in range(3): d.p(f'a{k}', '', B, (34, 70 + 5 * k)); d.p(f'b{k}', '', ORA, (66, 70 + 5 * k))
ball = {f'a{k}': d.newball(rec(d, f'a{k}', 0)) for k in range(3)}; ball.update({f'b{k}': d.newball(rec(d, f'b{k}', 0)) for k in range(3)})
seq = [('a0', 'b0', 'L'), ('b0', 'a1', 'R'), ('a1', 'b1', 'L'), ('b1', 'a2', 'R')]
t = 0.4; marks = []; endq = {'L': 0, 'R': 0}
for runner, passer, side in seq:
    cx = 40 if side == 'L' else 60; sx = -1 if side == 'L' else 1
    t1 = d.path(runner, t, [(cx + 6 * sx, 44), (cx, 34), (cx - 6 * sx, 30)], 1.6)                         # runt konen
    d.carry(ball[runner], runner, 0, t)
    t2 = d.pas(ball[passer], t1 - 0.9, rec(d, runner, t1 + 0.1), 0.9); marks.append(t2)
    tg = shoot(d, ball[passer], t2 + 0.05, (50 - 4 * sx, 1)); hide(d, ball[passer], tg + 0.4)               # skjut direkt
    endq[side] += 1; d.mv(runner, tg + 0.2, tg + 2.6, (72 if side == 'L' else 28, 82 + 5 * endq[side]))   # ställ dig sist i andra kön
    t = t1 - 0.4
fp = [(0, 'Spelare 1 springer runt konen', 'Och får passning från spelare 2.'),
      (marks[0] - 0.2, 'Skjut direkt', ''),
      (marks[0] + 0.4, 'Spelare 2 rundar konen på andra sidan', ''),
      (marks[2], 'Extra mål bredvid om ni är många', '')]
finish(d, 'ok18', 'trollenasaren', ['Trollenäsaren', 'Avslutsövning'], 'Mål med koner ca 10 m ut',
       fp, 'AVSLUT', [('cone', 40, 36), ('cone', 60, 36)])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ ok19 Ibrakadabra – vägg och avslut ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
P1, P2, P3 = (40, 64), (58, 60), (50, 36)
d.p('s1', '1', B, P1); d.p('s2', '2', B, P2); d.p('s3', '3', B, P3); d.p('q', '1', B, (36, 76))
b = d.newball(rec(d, 's1', 0)); t = 0.4; marks = []
roles = ['s1', 's2', 's3']
for rep in range(2):
    p1, p2, p3 = roles
    t = d.pas(b, t, rec(d, p2, t + 0.6)); t = d.pas(b, t + 0.1, rec(d, p1, t + 0.6))                         # vägg
    t = d.pas(b, t + 0.2, rec(d, p3, t + 0.9))                                                               # till den bortre
    d.mv(p2, t - 0.8, t + 0.6, (60, 30)); t = d.pas(b, t + 0.15, rec(d, p2, t + 0.7)); marks.append(t)       # tillbaka till spelare 2
    tg = shoot(d, b, t + 0.05, (46, 1)); hide(d, b, tg + 0.4)
    d.mv(p1, tg, tg + 1.6, P2); d.mv(p2, tg + 0.2, tg + 1.8, P3); d.mv(p3, tg, tg + 2.2, (36 + 10 * rep, 84))             # rotera
    if rep == 0:
        d.mv('q', tg, tg + 1.4, P1); roles = ['q', p1, p2]
        b = d.newball((200, 200)); show(d, b, tg + 1.5, rec(d, 'q', tg + 1.5)); t = tg + 2.0
fp = [(0, 'Spelare 1 och 2 spelar vägg', 'Koner 5 m isär, 10 m till målet.'),
      (1.6, 'Spelare 1 slår till den bortre', 'Som spelar tillbaka till spelare 2.'),
      (marks[0] - 0.2, 'Spelare 2 avslutar direkt', 'Rotera.'),
      (marks[0] + 2.0, 'Nästa runda', '')]
finish(d, 'ok19', 'ibrakadabra-vagg-och-avslut', ['Ibrakadabra', 'Vägg och avslut'], 'Koner 5 m isär i mitten · 10 m till målet',
       fp, 'AVSLUT', [('cone', 44, 52), ('cone', 56, 52)])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ ok20 Pass och avslut ============
d = Drill(); d.p('mv', 'MV', R, (50, 4)); d.p('l', 'L', YEL, (50, 36))
for k in range(4): d.p(f'p{k}', '', B, (50, 74 + 5 * k))
balls = [d.newball(rec(d, f'p{k}', 0)) for k in range(4)]
t = 0.4; shots = []
for k in range(3):
    pid = f'p{k}'; side = -1 if k % 2 == 0 else 1
    for j in range(k + 1, 4): d.mv(f'p{j}', t, t + 0.6, (50, 74 + 5 * (j - k - 1)))
    d.carry(balls[k], pid, 0, t)
    t1 = d.pas(balls[k], t, rec(d, 'l', t + 0.8))
    d.mv(pid, t + 0.1, t1 + 0.6, (50 + 10 * side, 42))
    t2 = d.pas(balls[k], t1 + 0.1, rec(d, pid, t1 + 0.6), 0.5)                                               # lägger tillbaka i sidled
    tg = shoot(d, balls[k], t2 + 0.05, (50 - 4 * side, 1)); shots.append(tg); hide(d, balls[k], tg + 0.5)
    d.mv(pid, tg + 0.2, tg + 3.0, (60, 94))                                                                  # hämta bollen och ställ dig sist
    t = t2 + 0.4
fp = [(0, 'Passa till ledaren', 'Ledaren står vid konen ca 10 m ut.'),
      (shots[0] - 0.8, 'Ledaren lägger tillbaka i sidled', 'Skjut direkt.'),
      (shots[0] + 0.3, 'Hämta bollen och ställ dig sist', ''),
      (shots[2] - 0.6, 'Variant: ledaren kastar bollar i luften', '')]
finish(d, 'ok20', 'pass-och-avslut', ['Pass och', 'avslut'], 'Mål med en kon ca 10 m ut där ledaren står',
       fp, 'AVSLUT', [('cone', 50, 40)])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ ok21 Hattrick-varianten ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
POS = [(30, 52), (50, 56), (70, 52)]
team(d, 'p', B, POS, ['', '', ''])
b1 = d.newball(rec(d, 'p0', 0)); b2 = d.newball(rec(d, 'p1', 0))
t = drive(d, b1, 'p0', 0.4, (32, 42), 14)
d.mv('p0', t, t + 0.6, (38, 36)); d.carry(b1, 'p0', t, t + 0.6); t += 0.6                                   # fint vid konen
tg = shoot(d, b1, t + 0.1, (44, 1)); hide(d, b1, tg + 0.4)
d.mv('p0', tg, tg + 0.8, (40, 44))                                                                         # vänder
t = d.pas(b2, tg + 0.6, rec(d, 'p0', tg + 1.2)); t = d.pas(b2, t + 0.1, rec(d, 'p1', t + 0.6))               # väggspel med mittspelaren
d.mv('p1', t - 0.6, t, (50, 46)); tg2 = shoot(d, b2, t + 0.05, (54, 1)); hide(d, b2, tg2 + 0.4)
for k, ps in ((0, POS[1]), (1, POS[2]), (2, (30, 60))): d.mv(f'p{k}', tg2 + 0.3, tg2 + 2.4, ps)
d.mv('p2', tg2 + 2.4, tg2 + 3.2, POS[0])                                                                  # alla flyttar ett steg åt höger
fp = [(0, 'Längst till vänster: finta konen och skjut', 'Tre spelare bredvid varandra.'),
      (tg + 0.2, 'Vänd och spela vägg med mittspelaren', ''),
      (tg2 - 0.4, 'Mittspelaren skjuter direkt', ''),
      (tg2 + 0.4, 'Alla flyttar ett steg åt höger', 'Ny runda.')]
finish(d, 'ok21', 'hattrick-varianten', ['Hattrick-', 'varianten'], 'Koner ca 10 m från mål · Tre spelare bredvid varandra',
       fp, 'AVSLUT', [('cone', 34, 38)])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ ok22 Tiki-taka i par ============
d = Drill()
YS = [26, 50, 74]
for k, y in enumerate(YS): d.p(f'l{k}', '', B, (28, y)); d.p(f'r{k}', '', B, (72, y))
balls = [d.newball(rec(d, f'l{k}', 0)) for k in range(3)]
for k, y in enumerate(YS):
    t = 0.4 + 0.3 * k; a, c = f'l{k}', f'r{k}'
    for rep in range(6):
        outside = rep % 3 == 1
        ty = y + (9 if outside else 0)
        rx = 72 if c[0] == 'r' else 28; ax = 28 if c[0] == 'r' else 72
        if outside:
            d.mv(a, t, t + 0.6, (ax, ty)); d.carry(balls[k], a, t, t + 0.6); t += 0.6                     # flytta bollen utanför konerna
        d.mv(c, t, t + 0.5, (rx, ty))
        t = d.pas(balls[k], t + 0.1, rec(d, c, t + 0.8)) + 0.1
        if outside: d.mv(a, t - 0.6, t, (ax, y))
        a, c = c, a
fp = [(0, 'Först genom mitten', 'Koner 3 m isär, två per boll.'),
      (2.0, 'Flytta bollen utanför konerna', 'Och passa tillbaka.'),
      (4.0, 'Mitten, utsidan, mitten', 'Växla hela tiden.'),
      (9.0, 'Snabba fötter', 'Få touch.')]
finish(d, 'ok22', 'tiki-taka-i-par', ['Tiki-taka', 'I par'], 'Koner 3 m isär · Två per boll',
       fp, 'PASSNINGSÖVNING', [('cone', 50, y + dy) for y in YS for dy in (-4, 4)])

# ============ ok23 Ajax-mönstret ============
d = Drill()
CN = {'A': (34, 72), 'B': (66, 72), 'C': (66, 40), 'D': (34, 40)}
def qp(c, n): x, y = CN[c]; return (x - 5 * n if c in 'AD' else x + 5 * n, y + 5 * n if c in 'AB' else y - 5 * n)
Q = {'A': ['a0', 'a1', 'a2'], 'B': ['b0'], 'C': ['c0'], 'D': ['d0']}
for c, lst in Q.items():
    for n, pid in enumerate(lst): d.p(pid, '', B, qp(c, n))
b = d.newball(rec(d, 'a0', 0)); t = 0.4; marks = []
for rep in range(2):
    order = ['A', 'B', 'C', 'D']
    for c, nc in zip(order, order[1:]):
        p = Q[c].pop(0); r = Q[nc][0]
        t1 = d.pas(b, t, rec(d, r, t + 0.8))
        d.mv(r, t1, t1 + 0.5, (CN[nc][0] + (3 if nc in 'BC' else -3), CN[nc][1] + (-3 if nc in 'AB' else 3))); d.carry(b, r, t1, t1 + 0.5)   # tar med
        d.mv(p, t + 0.3, t1 + 1.6, qp(nc, len(Q[nc]))); Q[nc].append(p)
        for n, w in enumerate(Q[c]): d.mv(w, t + 0.5, t + 1.1, qp(c, n))
        t = t1 + 0.6
    last = Q['D'].pop(0); marks.append(t)
    d.mv(last, t, t + 1.4, (50, 56)); d.carry(b, last, t, t + 1.4); d.mv(last, t + 1.4, t + 2.4, qp('A', len(Q['A']))); d.carry(b, last, t + 1.4, t + 2.4)   # driver mellan konerna
    Q['A'].append(last); t += 2.4
    nxt = Q['A'][0]; t = d.pas(b, t + 0.2, rec(d, nxt, t + 0.9)) if nxt != last else t
fp = [(0, 'En spelare vid varje kon', 'Max tre vid startkonen.'),
      (1.2, 'Ta med och spela vidare', 'Bollen går enligt mönstret.'),
      (marks[0] - 0.2, 'Sista spelaren driver mellan konerna', 'Och ställer sig sist.'),
      (marks[0] + 2.6, 'Variant: väggspel vid varje kon', '')]
finish(d, 'ok23', 'ajax-monstret', ['Ajax-', 'mönstret'], 'Fyra koner 5 m isär · Max tre vid startkonen',
       fp, 'PASSNINGSÖVNING', [('cone',) + v for v in CN.values()])

if __name__ == '__main__': render(C, sys.argv)
