# Externa övningar, omgång 13 (tolv st). Regel: först d.mv, sedan d.carry; först mottagarens rörelse, sedan passningen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e9', __file__.replace('render_extern13.py', 'render_extern9.py'))
e9 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e9); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e9.finish, e9.rec, e9.chain, e9.wander, e9.counter, e9.arrivals
lab, hide, show, team, boxes, drive, shoot = e9.lab, e9.hide, e9.show, e9.team, e9.boxes, e9.drive, e9.shoot
factor, swap_color, stand, countdown, countup, win = e9.factor, e9.swap_color, e9.stand, e9.countdown, e9.countup, e9.win
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'

# ============ sd32 Direkt återerövring 4 mot 2 ============
d = Drill()
XP = [(36, 36), (64, 36), (64, 64), (36, 64)]; team(d, 'x', B, XP); team(d, 'o', R, [(46, 46), (56, 54)])
team(d, 'w', R, [(10, 20), (90, 24), (12, 80), (88, 82)], ['O', 'O', 'O', 'O'])
b = d.newball(rec(d, 'x0', 0))
t = chain(d, b, 0.4, ['x1', 'x2', 'x3', 'x0', 'x1'], 0.25)
tw = win(d, b, 'o0', 'x1', t + 0.3); t = d.pas(b, tw + 0.2, rec(d, 'w1', tw + 1.2))                   # ut till medspelarna
d.mv('x1', tw, t + 0.6, (82, 28)); d.mv('x2', tw, t + 0.6, (76, 40))                                    # omställning direkt
d.mv('w1', t, t + 0.8, (88, 34)); d.carry(b, 'w1', t, t + 0.8); t += 0.8
tr = win(d, b, 'x1', 'w1', t + 0.2, 0.5)
d.mv('x1', tr, tr + 1.2, XP[1]); d.carry(b, 'x1', tr, tr + 1.2); d.mv('x2', tr, tr + 1.2, XP[2])
t = d.pas(b, tr + 1.3, rec(d, 'x0', tr + 2.0)); t = chain(d, b, t, ['x3'], 0.3)
fp = [(0, 'Lag X håller bollen mot två', 'I mittrutan 10 × 10 m.'),
      (tw - 0.2, 'O bryter och spelar ut', 'Till medspelarna i den stora ytan.'),
      (tw + 0.4, 'Ställ om direkt', 'Lag X jagar i den stora ytan.'),
      (tr - 0.2, 'Återerövring', 'Tillbaka in i rutan och fortsätt.')]
finish(d, 'sd32', 'direkt-atererovring-4-mot-2', ['Direkt återerövring', '4 mot 2'], 'Central ruta 10 × 10 m i en större yta',
       fp, 'ÅTERERÖVRING', [('box', 4, 10, 96, 92), ('box', 30, 30, 70, 70)], [lab(tr, tr + 1.6, (84, 44), 'ÅTERERÖVRAD')])

# ============ sd33 Avslut med återerövring ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96))
BT = [(30, 34), (46, 28), (60, 34), (70, 22)]; RT = [(42, 16), (58, 14)]                                # övertal uppe: blått
RB = [(30, 66), (46, 72), (60, 66), (70, 78)]; BB = [(42, 84), (58, 86)]                                # övertal nere: rött
team(d, 'bt', B, BT); team(d, 'rt', R, RT); team(d, 'rb', R, RB); team(d, 'bb', B, BB)
b = d.newball(rec(d, 'bt0', 0))
t = chain(d, b, 0.4, ['bt1', 'bt2', 'bt3'], 0.3); d.mv('rt1', t - 1.0, t, (64, 16)); tg = shoot(d, b, t + 0.1, (46, 1))   # övertal avslutar
hide(d, b, tg + 0.4)
b2 = d.newball((200, 200)); show(d, b2, tg + 0.8, rec(d, 'mvr', tg + 0.8))
t = d.pas(b2, tg + 1.0, rec(d, 'rt0', tg + 1.8)); d.mv('bt1', tg + 0.6, t + 0.6, (44, 22))                  # undertal bryter
t = d.pas(b2, t + 0.3, rec(d, 'rb1', t + 1.6), 1.3)                                                       # spelar till sina i andra halvan
t = chain(d, b2, t, ['rb2', 'rb3'], 0.3); d.mv('bb1', t - 1.0, t + 0.2, rec(d, 'rb3', t + 0.2))
tw = d.pas(b2, t + 0.3, rec(d, 'bb1', t + 0.5), 0.3)                                                     # blått bryter
t = d.pas(b2, tw + 0.3, rec(d, 'bt2', tw + 1.6), 1.3)
fp = [(0, 'Laget i övertal anfaller', 'Spelarna byter inte planhalva.'),
      (tg - 0.4, 'Avslut', 'Sedan vill laget återerövra.'),
      (tg + 1.0, 'Laget i undertal bryter', 'Och spelar till sitt övertal i andra halvan.'),
      (tw - 0.2, 'Ny brytning – spela tillbaka', 'Spelet går fram och tillbaka.')]
finish(d, 'sd33', 'avslut-med-atererovring', ['Avslut med', 'återerövring'], 'Dubbla straffområden · Båda lag i övertal på egen planhalva',
       fp, 'SPELÖVNING', [('line', [(4, 50), (96, 50)])])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ sd35 7 mot 7 – återerövring ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96))
BP = [(28, 78), (50, 82), (72, 78), (34, 58), (66, 56), (50, 40)]; RP = [(28, 22), (50, 18), (72, 22), (36, 38), (64, 42), (50, 60)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b1', 0))
t = chain(d, b, 0.4, ['b3', 'b5'], 0.3)
tl = win(d, b, 'r4', 'b5', t + 0.3)                                                                       # bollförlust
for k, ps in [(5, (58, 46)), (4, (64, 48)), (3, (50, 56))]: d.mv(f'b{k}', tl, tl + 1.2, ps)             # pressa snabbt
d.mv('r4', tl, tl + 0.8, (62, 52)); d.carry(b, 'r4', tl, tl + 0.8)
t = d.pas(b, tl + 0.9, rec(d, 'r5', tl + 1.6)); d.mv('r5', tl, t, (48, 66))
d.mv('b4', t - 0.6, t + 1.4, (52, 74)); d.mv('b1', t - 0.4, t + 0.8, (50, 76))                         # passerad – kom på försvarssidan
tw = win(d, b, 'b1', 'r5', t + 0.8, 0.5)
t = d.pas(b, tw + 0.3, rec(d, 'b2', tw + 1.0)); t = chain(d, b, t, ['b4'], 0.3)
fp = [(0, 'Sju mot sju med matchregler', ''),
      (tl - 0.2, 'Bollförlust – pressa direkt', 'Närmaste spelarna på bollen.'),
      (tl + 1.4, 'Passerad? Kom på försvarssidan', 'Spring hem mellan bollen och målet.'),
      (tw - 0.2, 'Återerövring', '')]
finish(d, 'sd35', '7-mot-7-atererovring', ['7 mot 7', 'Återerövring'], '7 mot 7-plan 50–55 × 30–35 m · Två mål',
       fp, 'MATCHLIKT', [])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ sd36 Bollstafett över – under ============
d = Drill(); ex = []
for tm, x, col in (('b', 34, B), ('r', 66, R)):
    ids = [f'{tm}{k}' for k in range(6)]
    for k, pid in enumerate(ids): d.p(pid, '', col, (x, 26 + 9 * k))
    ball = d.newball(rec(d, ids[0], 0)); t = 0.4 + (0.2 if tm == 'r' else 0)
    order = list(ids)
    for rnd in range(2):
        for k in range(5):
            t = d.pas(ball, t + 0.15, rec(d, order[k + 1], t + 0.55), 0.4)
            if tm == 'b': ex.append(lab(t - 0.4, t + 0.2, (16, 26 + 9 * k + 4), 'ÖVER' if k % 2 == 0 else 'UNDER'))
        last = order[-1]
        for k, pid in enumerate(order[:-1]): d.mv(pid, t + 0.2, t + 1.2, (x, 26 + 9 * (k + 1)))           # alla flyttar ett steg bak
        d.mv(last, t, t + 0.4, (x + 7, 26 + 9 * 5)); d.mv(last, t + 0.4, t + 2.0, (x + 7, 26)); d.carry(ball, last, t, t + 2.0)   # sista springer fram
        d.mv(last, t + 2.0, t + 2.4, (x, 26)); d.carry(ball, last, t + 2.0, t + 2.4); t += 2.4
        order = [last] + order[:-1]
fp = [(0, 'Bollen skickas bakåt i ledet', 'Varannan över huvudet, varannan mellan benen.'),
      (3.2, 'Den sista springer fram', 'Och startar nästa varv.'),
      (6.0, 'Nytt varv', ''),
      (11.0, 'Så snabbt som möjligt', 'Slå er egen tid – två lag kan tävla.')]
finish(d, 'sd36', 'bollstafett-over-under', ['Bollstafett', 'Över – under'], 'Spelare i led · Ca sex per lag',
       fp, 'STAFETT', [], ex)

# ============ sd37 Sicksackstafett ============
d = Drill()
CONES = {34: [(26, 66), (42, 54), (26, 42), (42, 30), (26, 18)], 66: [(58, 66), (74, 54), (58, 42), (74, 30), (58, 18)]}
for tm, x, col in (('b', 34, B), ('r', 66, R)):
    for k in range(5): d.p(f'{tm}{k}', '', col, (x, 82 + 4 * k))
    t = 0.4 + (0.3 if tm == 'r' else 0)
    for k in range(3):
        pid = f'{tm}{k}'
        for j, pid2 in enumerate([f'{tm}{q}' for q in range(k + 1, 5)]): d.mv(pid2, t, t + 0.6, (x, 82 + 4 * j))
        d.mv(pid, t, t + 0.3, (x, 76))
        t2 = d.path(pid, t + 0.3, [(c[0] + (3 if c[0] < x else -3), c[1]) for c in CONES[x]] + [(x, 12)], 2.2)
        t3 = d.path(pid, t2, [(x + 12, 40), (x + 12, 100 - 2)], 2.4)
        d.mv(pid, t3, t3 + 0.6, (x + 8, 98 - 6 * k)); t = t2 + 0.4
fp = [(0, 'Spring sicksack mellan konorna', 'Ca sex spelare per lag.'),
      (2.4, 'Och tillbaka', 'Nästa startar.'),
      (6.0, 'Låg tyngdpunkt i svängarna', 'Korta steg runt konan.'),
      (10.0, 'Slå er egen tid', '')]
d.newball((200, 200))                                                                     # ingen boll i stafetten
_g = finish.__globals__; _bl = _g['_ball_last']; _g['_ball_last'] = lambda balls: 99
finish(d, 'sd37', 'sicksackstafett', ['Sicksack-', 'stafett'], 'Konor i sicksack · Ca sex spelare per lag',
       fp, 'STAFETT', [('cone',) + c for x in CONES for c in CONES[x]] + [('cone', 34, 10), ('cone', 66, 10)])
_g['_ball_last'] = _bl

# ============ sa1 Dukning – ett touch i ring ============
d = Drill()
RING = [ring_pos(50, 50, 30, i, 7) for i in range(7)]
for k, ps in enumerate(RING): d.p(f'p{k}', '', B, ps)
d.p('m', '', B, (50, 50))
b = d.newball(rec(d, 'p0', 0))
order = ['p3', 'p6', 'm', 'p2', 'p5', 'p1', 'p4', 'p0', 'p3', 'p5', 'p1']
t = 0.4; marks = []
for pid in order:
    t = d.pas(b, t + 0.15, rec(d, pid, t + 0.8)); marks.append(t)                              # ett touch, aldrig tillbaka
ts2 = marks[3]; ts3 = marks[7]
d.mv('m', ts2, ts2 + 0.8, (50, 50))
d.mv('m', ts3 - 0.2, ts3 + 0.4, ((RING[3][0] + RING[0][0]) / 2, (RING[3][1] + RING[0][1]) / 2))   # aktiv motståndare
fp = [(0, 'Steg 1: alla i samma lag', 'Max ett touch.'),
      (ts2, 'Steg 2: passiv motståndare', 'Ingen återpassning till den som gav bollen.'),
      (ts3, 'Steg 3: aktiv motståndare', 'Nu får man spela tillbaka.'),
      (marks[-1] - 0.4, 'Lyft blicken innan bollen kommer', '')]
finish(d, 'sa1', 'dukning-ett-touch-i-ring', ['Dukning', 'Ett touch i ring'], 'Ring med 5–8 spelare och en i mitten',
       fp, 'RONDO', [])
f = factor(fp); ids = {k: i for i, k in enumerate(d.order)}
swap_color(ids['m'], ts2 * f, B, R)

# ============ sa2 Drivning med riktningsförändring och vändning ============
d = Drill(); ex = []
FEINT = ['INSIDA', 'UTSIDA', 'SULA']
YS = [22, 34, 46, 58, 70, 82]
balls = []
for k, y in enumerate(YS):
    d.p(f'p{k}', '', B, (14, y)); balls.append(d.newball(rec(d, f'p{k}', 0)))
for k, y in enumerate(YS):
    pid = f'p{k}'; t = 0.4 + 0.25 * k
    for lap in range(3):
        x0, x1 = (14, 84) if lap % 2 == 0 else (84, 14)
        d.mv(pid, t, t + 1.4, ((x0 + x1) / 2, y + (3 if k % 2 else -3))); d.carry(balls[k], pid, t, t + 1.4)      # fint mitt på
        d.mv(pid, t + 1.4, t + 3.0, (x1, y)); d.carry(balls[k], pid, t + 1.4, t + 3.0)
        stand(d, pid, t + 3.0, t + 3.4); d.carry(balls[k], pid, t + 3.0, t + 3.4); t += 3.4                     # vänd 180 grader
        if k == 0: ex.append(lab(t - 2.2, t - 1.0, (50, 12), FEINT[lap]))
fp = [(0, 'Driv från ena långsidan till den andra', 'Egen boll var.'),
      (1.4, 'En fint på varje passage', 'Insida, utsida, sula eller kombinationer.'),
      (3.4, 'Vänd 180 grader och tillbaka', ''),
      (7.0, 'Tio varianter', 'Byt fint varje gång.')]
finish(d, 'sa2', 'drivning-med-riktningsforandring-och-vandning', ['Drivning med', 'riktningsförändring och vändning'], 'Rektangel 13 × 26 m · Egen boll var',
       fp, 'TEKNIK', [('box', 10, 14, 88, 90)], ex)

# ============ sa3 Passningscirkel med mittkon ============
d = Drill()
ST = [(22, 14), (78, 14), (78, 86), (22, 86)]; MIDC = (50, 50)
for k, ps in enumerate(ST): d.p(f's{k}', '', B, ps)
d.p('e0', '', B, (16, 10)); d.p('e2', '', B, (84, 90))
occ = {0: ['s0', 'e0'], 1: ['s1'], 2: ['s2', 'e2'], 3: ['s3']}
def qp(c, n): x, y = ST[c]; return (x + (-6 if x < 50 else 6) * n, y + (-4 if y < 50 else 4) * n)
bA = d.newball(rec(d, 's0', 0)); bB = d.newball(rec(d, 's2', 0))
plan = [(bA, 0, 0.4), (bB, 2, 0.9), (bA, 1, 4.6), (bB, 3, 5.1), (bA, 2, 8.8), (bB, 0, 9.3)]
for ball, c, t in plan:
    nc = (c + 1) % 4; p = occ[c].pop(0); q = occ[nc][0]
    t1 = d.pas(ball, t, rec(d, q, t + 0.9))                                                  # passa
    d.mv(p, t + 0.2, t + 2.0, qp(nc, len(occ[nc]))); occ[nc].append(p)                      # ta mottagarens plats
    for n, w in enumerate(occ[c]): d.mv(w, t + 0.4, t + 1.0, qp(c, n))
    occ[nc].remove(q)
    d.mv(q, t1, t1 + 1.2, (MIDC[0] + (-4 if ST[nc][0] < 50 else 4), MIDC[1] + (-4 if ST[nc][1] < 50 else 4))); d.carry(ball, q, t1, t1 + 1.2)   # driv till mittkonen
    nn = (nc + 1) % 4; r = occ[nn][0]
    t2 = d.pas(ball, t1 + 1.3, rec(d, r, t1 + 2.0))                                          # passa vidare
    d.mv(q, t1 + 1.4, t1 + 3.0, qp(nc, len(occ[nc]))); occ[nc].append(q)
    for c2, lst in occ.items():                                    # ordna köerna så att ingen står på samma plats
        for n, w in enumerate(lst):
            tr = d.pl[w]['tr']; tend = max(tr[-1][0], t1 + 3.0); cur = at(tr, tend); goal = qp(c2, n)
            dd = ((cur[0] - goal[0]) ** 2 + (cur[1] - goal[1]) ** 2) ** .5
            if dd > 1: d.mv(w, tend, tend + max(0.6, dd / 15), goal)
fp = [(0, 'Två bollar – passa och ta mottagarens plats', ''),
      (1.4, 'Mottagaren driver till mittkonen', 'Och passar vidare.'),
      (5.0, 'Precision först', 'Högre tempo när det fungerar.'),
      (9.0, 'Lägg till väggspel och direktpassningar', '')]
finish(d, 'sa3', 'passningscirkel-med-mittkon', ['Passningscirkel', 'Med mittkon'], 'Yta 13 × 26 m · Koner i hörnen och mitt på långsidorna',
       fp, 'PASSNINGSÖVNING', [('cone',) + c for c in ST] + [('cone', 22, 50), ('cone', 78, 50), ('cone', 50, 50)])

# ============ sa4 Possession med tre lag, två touch ============
d = Drill(); d.p('t', 'T', T_COL, (97, 50))
AP = [(30, 20), (70, 80), (24, 60)]; BP = [(70, 22), (30, 80), (76, 44)]; CP = [(44, 40), (56, 56), (50, 30)]
team(d, 'a', B, AP); team(d, 'b', WHITE, BP); team(d, 'c', R, CP)
for k in range(3): wander(d, f'c{k}', 0, 5.0, boxes([CP[k]], 4)[0], 2200 + k, 1.6)
b = d.newball(rec(d, 'a1', 0))
t = chain(d, b, 0.4, ['b1', 'a2', 'b2', 'a0'], 0.3); tsw = t                                               # från kortsida till kortsida
t = d.pas(b, t + 0.3, rec(d, 'b0', t + 1.0))
tw = win(d, b, 'c2', 'b0', t + 0.3)
for k, ps in enumerate([(40, 34), (60, 40), (50, 56)]): d.mv(f'b{k}', tw + 0.2, tw + 1.8, ps)              # vitt byter roll och jagar
for k, ps in enumerate([(70, 22), (30, 80), (76, 44)]): d.mv(f'c{k}', tw + 0.2 if k != 2 else tw + 0.6, tw + 2.0, ps)
d.carry(b, 'c2', tw, tw + 0.6)
t = d.pas(b, tw + 0.7, rec(d, 'a2', tw + 1.4)); t = chain(d, b, t, ['c1', 'a1'], 0.3)
fp = [(0, 'Blått och vitt håller bollen mot rött', 'Två touch.'),
      (tsw - 0.4, 'Kortsida till kortsida: poäng', ''),
      (tw - 0.2, 'Vitt tappar bollen', 'Laget som tappar byter roll och jagar.'),
      (tw + 0.8, 'Nu håller blått och rött', 'Tränaren skjuter in ny boll när den går ut.')]
finish(d, 'sa4', 'possession-med-tre-lag-tva-touch', ['Possession med tre lag', 'Två touch'], 'Yta 13 × 26 m med konmål · Tre lag',
       fp, 'POSITIONSSPEL', [('box', 14, 8, 86, 92), ('cone', 40, 8), ('cone', 60, 8), ('cone', 40, 92), ('cone', 60, 92)],
       [lab(tsw, tsw + 1.6, (36, 12), '+1')])

# ============ sa5 Intensivt tvåmålsspel ============
d = Drill(); d.p('mvr', 'MV', R, (50, 6)); d.p('mvb', 'MV', B, (50, 94)); d.p('t', 'T', T_COL, (97, 50))
BP = [(30, 64), (70, 62), (50, 46)]; RP = [(34, 36), (66, 36), (52, 58)]; team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b2', 'b1'], 0.3); tout = shoot(d, b, t + 0.1, (70, -2)); hide(d, b, tout + 0.1)      # utanför
b2 = d.newball(rec(d, 't', 0)); t = d.pas(b2, tout + 0.3, rec(d, 'mvr', tout + 1.4), 1.0)                 # tränaren slår in ny boll
d.mv('mvr', tout, t, (50, 16)); d.carry(b2, 'mvr', t, t + 0.6)                                             # målvakten deltar som utespelare
d.mv('mvr', t, t + 0.6, (52, 22)); t = d.pas(b2, t + 0.7, rec(d, 'r0', t + 1.4)); t = chain(d, b2, t, ['r2'], 0.3)
d.mv('r2', t, t + 1.0, (54, 76)); d.carry(b2, 'r2', t, t + 1.0); tg = shoot(d, b2, t + 1.1, (46, 99))
d.mv('mvr', tg, tg + 1.4, (50, 6))
fp = [(0, '3–4 utespelare per lag', 'Liten yta med två mål.'),
      (tout - 0.3, 'Inga inkast eller hörnor', 'Tränaren slår in en ny boll direkt.'),
      (tout + 1.0, 'Målvakten deltar som utespelare', ''),
      (tg - 0.4, 'Korta matcher med vila', 'Byten efter ca 60 sekunder.')]
finish(d, 'sa5', 'intensivt-tvamalsspel', ['Intensivt', 'tvåmålsspel'], 'Liten yta med två mål och målvakter',
       fp, 'SMÅLAGSSPEL', [('box', 14, 4, 86, 96)])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ sa6 Pendelspel med löpningar mot straffområdet ============
d = Drill(); d.p('mv1', 'MV', G, (50, 4)); d.p('mv2', 'MV', B, (50, 96))
BP = [(30, 78), (70, 78), (40, 60), (60, 60), (50, 70)]; team(d, 'b', B, BP)
b = d.newball(rec(d, 'mv2', 0))
t = d.pas(b, 0.4, rec(d, 'b0', 1.2)); t = chain(d, b, t, ['b4', 'b3'], 0.3)
for k, ps in enumerate([(30, 30), (70, 26), (42, 20), (58, 22), (50, 40)]): d.mv(f'b{k}', t - 0.4, t + 2.2, ps)   # fyll på i guldzonen
d.carry(b, 'b3', t, t + 1.0); t = d.pas(b, t + 1.1, rec(d, 'b2', t + 2.0)); tz = t
t = d.pas(b, t + 0.3, rec(d, 'mv1', t + 1.0))                                                               # till målvakten
for k, ps in enumerate(BP): d.mv(f'b{k}', t + 0.2, t + 3.0, (ps[0], 100 - ps[1]))
d.carry(b, 'mv1', t, t + 0.8); t = d.pas(b, t + 1.0, rec(d, 'b3', t + 2.6)); t = chain(d, b, t, ['b4', 'b0'], 0.3)
for k, ps in enumerate([(30, 70), (70, 74), (42, 80), (58, 78), (50, 60)]): d.mv(f'b{k}', t - 0.4, t + 2.2, ps)
d.carry(b, 'b0', t, t + 1.0); t = d.pas(b, t + 1.1, rec(d, 'mv2', t + 2.0))
fp = [(0, 'Från målvakt till målvakt', 'Mittlinjen är offsidelinje.'),
      (tz - 1.4, 'Fyll på i guldzonen', 'Efter inträde på offensiv planhalva.'),
      (tz + 0.4, 'Till målvakten – åt andra hållet', ''),
      (t - 1.6, 'Variation: försvarare i guldzonerna', 'Då är målet att göra mål.')]
finish(d, 'sa6', 'pendelspel-med-lopningar-mot-straffomradet', ['Pendelspel', 'Med löpningar mot straffområdet'], 'Planhalva ca 52 × 40 m i straffområdets bredd',
       fp, 'SPELÖVNING', [('line', [(18, 50), (82, 50)]), ('zone', 28, 10, 72, 26, (240, 210, 90), 'GULDZON'), ('zone', 28, 74, 72, 90, (240, 210, 90), 'GULDZON')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ sa7 Inläggsspel med kantkorridorer ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96))
team(d, 'bk', B, [(9, 44), (91, 56)], ['K', 'K']); team(d, 'rk', R, [(9, 60), (91, 36)], ['K', 'K'])
BP = [(36, 66), (64, 64), (50, 52)]; RP = [(36, 30), (64, 32), (50, 62)]; team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b0', 0))
t = d.pas(b, 0.4, rec(d, 'b2', 1.1)); t = d.pas(b, t + 0.2, rec(d, 'bk1', t + 1.2))
d.mv('bk1', t, t + 1.8, (91, 16)); d.carry(b, 'bk1', t, t + 1.8); t += 1.8                                # ingen press i korridoren
for k, ps in enumerate([(40, 16), (60, 12), (50, 28)]): d.mv(f'b{k}', t - 2.4, t + 0.4, ps)                 # alla över mittlinjen
for k, ps in enumerate([(42, 12), (56, 10)]): d.mv(f'r{k}', t - 2.0, t + 0.4, ps)
t = d.pas(b, t + 0.1, rec(d, 'b1', t + 1.0), 0.9); tg = shoot(d, b, t + 0.05, (46, 1))
fp = [(0, 'Två lika stora lag', 'En spelare per lag i varje korridor.'),
      (1.6, 'Ingen press i korridoren', 'Kantspelaren driver och slår in.'),
      (tg - 0.8, 'Alla utespelare över mittlinjen vid mål', ''),
      (tg - 0.2, 'Mål räknas dubbelt', 'Om försvarande lag har spelare utanför egen planhalva.')]
finish(d, 'sa7', 'inlaggsspel-med-kantkorridorer', ['Inläggsspel', 'Med kantkorridorer'], 'Planhalva ca 52 × 65 m · Två mål och kantkorridorer',
       fp, 'SPELÖVNING', [('zone', 0, 4, 18, 96, (200, 220, 200), ''), ('zone', 82, 4, 100, 96, (200, 220, 200), ''), ('line', [(18, 50), (82, 50)])],
       [lab(tg, tg + 1.8, (46, 14), 'x2')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

if __name__ == '__main__': render(C, sys.argv)
