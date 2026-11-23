# Externa övningar, omgång 17 (tolv st). Regel: först d.mv, sedan d.carry; först mottagarens rörelse, sedan passningen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e9', __file__.replace('render_extern17.py', 'render_extern9.py'))
e9 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e9); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e9.finish, e9.rec, e9.chain, e9.wander, e9.counter, e9.arrivals
lab, hide, show, team, boxes, drive, shoot = e9.lab, e9.hide, e9.show, e9.team, e9.boxes, e9.drive, e9.shoot
factor, swap_color, stand, countdown, countup, win = e9.factor, e9.swap_color, e9.stand, e9.countdown, e9.countup, e9.win
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'; GRN = '#3fbf5f'

# ============ fi13 Gröne man ============
d = Drill(); d.p('g', 'G', GRN, (50, 50))
XS = [16, 30, 44, 58, 72, 86]
for k, x in enumerate(XS): d.p(f'p{k}', '', B, (x, 88))
balls = [d.newball(rec(d, f'p{k}', 0)) for k in range(6)]
# vända 1: alla dribblar till andra sidan, gröne man bryter p2
for k, x in enumerate(XS):
    if k == 2: continue
    d.mv(f'p{k}', 0.6 + 0.1 * k, 4.0 + 0.1 * k, (x + (4 if k % 2 else -4), 12)); d.carry(balls[k], f'p{k}', 0, 4.2 + 0.1 * k)
d.mv('p2', 0.6, 2.4, (42, 54)); d.carry(balls[2], 'p2', 0, 2.4); d.mv('g', 0.6, 2.4, (46, 50))
tw = d.pas(balls[2], 2.6, rec(d, 'g', 2.8), 0.3); t1 = d.pas(balls[2], tw + 0.2, (2, 44), 0.7); hide(d, balls[2], t1 + 0.2)   # bruten
d.mv('p2', 2.6, 4.4, (36, 50)); d.mv('g', tw + 0.2, 4.4, (60, 50))
# vända 2: tillbaka – nu är p2 också gröne man
for k, x in enumerate(XS):
    if k == 2: continue
    d.mv(f'p{k}', 5.6 + 0.1 * k, 9.6 + 0.1 * k, (x, 88)); d.carry(balls[k], f'p{k}', 4.2, 9.8 + 0.1 * k)
d.mv('g', 5.6, 7.4, (68, 46)); d.mv('p2', 5.6, 7.4, (24, 56))
d.mv('p4', 5.6 + 0.4, 7.2, (70, 50)); t2 = d.pas(balls[4], 7.4, rec(d, 'g', 7.6), 0.3)                       # bruten igen
d.mv('p4', 7.4, 9.0, (80, 54)); d.carry(balls[4], 'p4', 4.2, 7.2); t3 = d.pas(balls[4], t2 + 0.2, (98, 40), 0.7); hide(d, balls[4], t3 + 0.2)
fp = [(0, 'Dribbla till andra sidan', 'Gröne man har ingen boll.'),
      (tw - 0.3, 'Bruten – hjälp gröne man', 'I nästa vända.'),
      (5.6, 'Tillbaka – nu två som bryter', ''),
      (t2, 'Slut när en spelare har kvar bollen', '')]
finish(d, 'fi13', 'grone-man', ['Gröne man', 'Lek och reaktion'], 'Yta mellan två linjer · Alla har en boll utom gröne man',
       fp, 'LEK', [('line', [(6, 92), (94, 92)]), ('line', [(6, 8), (94, 8)])], [lab(tw, tw + 1.6, (40, 40), 'BRUTEN'), lab(t2, t2 + 1.6, (70, 40), 'BRUTEN')])
f = factor(fp); ids = {k: i for i, k in enumerate(d.order)}
swap_color(ids['p2'], (tw + 0.6) * f, B, GRN); swap_color(ids['p4'], (t2 + 0.6) * f, B, GRN)

# ============ fi14 Vän med bollen ============
d = Drill()
YS = [18, 32, 46, 60, 74, 88]
for k, y in enumerate(YS): d.p(f'p{k}', '', B, (8, y))
balls = [d.newball(rec(d, f'p{k}', 0)) for k in range(6)]
for k, y in enumerate(YS):
    pid = f'p{k}'; t = 0.4 + 0.2 * k
    for lap in range(3):
        x0, x1 = (8, 92) if lap % 2 == 0 else (92, 8)
        pts = [(x0 + (x1 - x0) * i / 4, y + (3 if i % 2 else -3) * (1 if lap != 1 else 0)) for i in range(1, 5)]
        t2 = d.path(pid, t, pts, 1.3); d.carry(balls[k], pid, t, t2); stand(d, pid, t2, t2 + 0.4); d.carry(balls[k], pid, t2, t2 + 0.4); t = t2 + 0.4
fp = [(0, 'Driv bollen över planen', 'Alla har en boll.'),
      (2.0, 'Olika drivningar och finter', ''),
      (5.6, 'Tillbaka – variera riktning och fot', ''),
      (10.0, 'Bollen är din vän', 'Nära foten hela tiden.')]
finish(d, 'fi14', 'van-med-bollen', ['Vän med bollen', 'Teknik'], 'Hela planen · Alla har en boll',
       fp, 'TEKNIK', [])

# ============ fi15 Driva och passa i par ============
d = Drill()
d.p('a0', '', B, (30, 90)); d.p('b0', '', B, (46, 90)); d.p('a1', '', R, (56, 90)); d.p('b1', '', R, (72, 90))
for pr, (a, c) in enumerate((('a0', 'b0'), ('a1', 'b1'))):
    b = d.newball(rec(d, a, 0)); t = 0.4 + 0.4 * pr; hold, oth = a, c; y = 90
    xs = {a: (30 if pr == 0 else 56), c: (46 if pr == 0 else 72)}
    for rep in range(6):
        y2 = y - 12
        d.mv(oth, t, t + 1.4, (xs[oth], y2)); d.mv(hold, t, t + 0.9, (xs[hold], y - 6)); d.carry(b, hold, t, t + 0.9)   # driv några meter
        t1 = d.pas(b, t + 0.9, rec(d, oth, t + 1.5)); d.mv(hold, t + 0.9, t1 + 0.2, (xs[hold], y2 + 2))
        hold, oth = oth, hold; t = t1 + 0.1; y = y2
fp = [(0, 'Paret joggar framåt', 'En boll per par.'),
      (1.2, 'Ta emot och driv några meter', ''),
      (2.2, 'Passa tillbaka', ''),
      (8.0, 'Hela vägen över planen', '')]
finish(d, 'fi15', 'driva-och-passa-i-par', ['Driva och passa', 'I par'], 'Par · En boll per par',
       fp, 'PASSNINGSÖVNING', [])

# ============ fi16 Pass, rörelse och avslut ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
SL = [(24, 72), (30, 64), (24, 56), (30, 48)]
for k in range(3): d.p(f'a{k}', '1', B, (22, 86 + 4 * k)); d.p(f'b{k}', '2', B, (62, 40 + 0 * k) if k == 0 else (68, 40 + 5 * k))
balls = [d.newball(rec(d, f'a{k}', 0)) for k in range(3)]
t = 0.4
for k in range(2):
    a, bp = f'a{k}', f'b{k}'
    d.carry(balls[k], a, 0, t)
    t1 = d.pas(balls[k], t, rec(d, bp, t + 1.2)); d.mv(bp, t1, t1 + 0.6, (56, 30)); d.carry(balls[k], bp, t1, t1 + 0.6)
    tg = shoot(d, balls[k], t1 + 0.7, (46, 1)); hide(d, balls[k], tg + 0.4)                                 # tar emot och avslutar
    t2 = d.path(a, t + 0.4, SL + [(40, 42), (52, 42)], 1.2); d.mv(a, t2, t2 + 1.0, (60, 46))                  # slalom, fram och baklänges
    d.mv(bp, tg + 0.3, tg + 2.8, (22, 94 + 4 * k))
    nb = f'b{k + 1}'; d.mv(nb, tg - 0.4, tg + 0.6, (62, 40))
    for j in range(k + 1, 3): d.mv(f'a{j}', t + 0.6, t + 1.2, (22, 86 + 4 * (j - k - 1)))
    t = tg + 0.6
fp = [(0, 'Spelare 1 passar till spelare 2', 'Mål, två led och en slalombana.'),
      (1.6, 'Spelare 2 tar emot och avslutar', ''),
      (2.2, 'Spelare 1 springer slalom', 'Fram- och baklänges till spelare 2:s plats.'),
      (t - 0.8, 'Nästa par', '')]
finish(d, 'fi16', 'pass-rorelse-och-avslut', ['Pass, rörelse', 'och avslut'], 'Mål · Två led och en slalombana',
       fp, 'AVSLUT', [('cone', x, y + 3) for x, y in SL])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ fi17 Finta och dribbla i led ============
d = Drill()
LA, LB, LC = (18, 84), (82, 84), (50, 12)
for k in range(2): d.p(f'a{k}', 'A', B, (LA[0] - 4 * k, LA[1] + 4 * k)); d.p(f'b{k}', 'B', B, (LB[0] + 4 * k, LB[1] + 4 * k)); d.p(f'c{k}', 'C', B, (LC[0] + 5 * k, LC[1] - 4 * k))
b = d.newball(rec(d, 'a0', 0)); t = 0.4; marks = []
seq = [('a0', 'b0', LB, 'c0'), ('b0', 'c0', LC, 'a1'), ('c0', 'a1', LA, 'b1')]
for passer, recv, rp, nxt in seq:
    t1 = d.pas(b, t, rec(d, recv, t + 1.2)); marks.append(t1)
    d.mv(passer, t + 0.2, t1 + 0.6, (50, 56))                                                                 # passiv försvarare i mitten
    d.mv(recv, t1, t1 + 1.0, (50 + (rp[0] - 50) * 0.4, 56 + (rp[1] - 56) * 0.4)); d.carry(b, recv, t1, t1 + 1.0)
    d.mv(recv, t1 + 1.0, t1 + 1.6, (50 + 8, 56 - 6 if rp != LC else 56 + 6)); d.carry(b, recv, t1 + 1.0, t1 + 1.6)   # fint och förbi
    nx = {'c0': LC, 'a1': LA, 'b1': LB}[nxt]
    endq = {LA: (LA[0] - 8, LA[1] + 8), LB: (LB[0] + 8, LB[1] + 8), LC: (LC[0] + 10, LC[1] - 6)}[rp]
    d.mv(passer, t1 + 1.6, t1 + 3.2, endq)                                                                       # byt led
    t = t1 + 1.7
fp = [(0, 'A passar B', 'Tre led.'),
      (marks[0], 'B driver mot en passiv A', 'A kliver in i mitten.'),
      (marks[0] + 1.0, 'Finta och dribbla förbi', 'Passa vidare till C.'),
      (marks[2], 'Byt led', 'Och så vidare.')]
finish(d, 'fi17', 'finta-och-dribbla-i-led', ['Finta och dribbla', 'I led'], 'Tre led · 6–8 spelare',
       fp, 'DUELL', [('cone',) + LA, ('cone',) + LB, ('cone',) + LC])

# ============ fi18 2 mot 1 – väggspel ============
d = Drill()
d.p('a', 'A', WHITE, (50, 90)); d.p('b', 'B', B, (38, 66)); d.p('c', 'C', B, (64, 44)); d.p('f', 'F', R, (46, 48))
b = d.newball(rec(d, 'a', 0))
t = d.pas(b, 0.4, rec(d, 'b', 1.4)); t = drive(d, b, 'b', t, (42, 56), 12); d.mv('f', t - 0.8, t, (44, 50))
t = d.pas(b, t + 0.1, rec(d, 'c', t + 0.7)); d.mv('b', t - 0.4, t + 0.8, (44, 36))
t = d.pas(b, t + 0.1, rec(d, 'b', t + 0.8)); tv = t                                                         # vägg förbi försvararen
d.mv('b', t, t + 1.4, (44, 16)); d.carry(b, 'b', t, t + 1.4); t += 1.4
t = d.pas(b, t + 0.2, rec(d, 'a', t + 2.0), 1.6)                                                            # tillbaka till A
d.mv('b', t - 1.6, t + 0.6, (64, 44)); d.mv('c', t - 1.6, t + 0.6, (38, 66)); d.mv('f', t - 1.6, t, (54, 48))   # B och C byter plats
t = d.pas(b, t + 0.3, rec(d, 'c', t + 1.3)); t = drive(d, b, 'c', t, (42, 56), 12)
t = d.pas(b, t + 0.1, rec(d, 'b', t + 0.7)); d.mv('c', t - 0.4, t + 0.8, (46, 34)); t = d.pas(b, t + 0.1, rec(d, 'c', t + 0.8))
d.mv('c', t, t + 1.2, (46, 16)); d.carry(b, 'c', t, t + 1.2)
fp = [(0, 'A passar B', 'Tre spelare och en försvarare.'),
      (tv - 1.2, 'Väggspel med C förbi försvararen', ''),
      (tv + 1.6, 'B och C byter plats', ''),
      (tv + 4.0, 'Samma igen', 'A byter uppgift efter en stund.')]
finish(d, 'fi18', '2-mot-1-vaggspel', ['2 mot 1', 'Väggspel'], 'Tre spelare varav en försvarare',
       fp, 'ÖVERLÄGE', [])

# ============ fi19 Insidespassning i tre steg ============
d = Drill(); YS = [26, 50, 74]
for k, y in enumerate(YS): d.p(f'a{k}', 'A', B, (28, y)); d.p(f'b{k}', 'B', B, (72, y))
balls = [d.newball(rec(d, f'a{k}', 0)) for k in range(3)]
steps = []
for k, y in enumerate(YS):
    t = 0.4 + 0.2 * k; a, c = f'a{k}', f'b{k}'
    for rep in range(9):
        step = rep // 3
        if k == 0 and rep % 3 == 0: steps.append(t)
        cx = 72 if c[0] == 'b' else 28
        t = d.pas(balls[k], t, rec(d, c, t + 0.9))
        if step == 1: d.mv(c, t, t + 0.4, (cx, y + 3)); d.carry(balls[k], c, t, t + 0.4); t += 0.4
        if step == 2: d.mv(c, t, t + 0.6, (cx, y + (6 if rep % 2 else -6))); d.carry(balls[k], c, t, t + 0.6); t += 0.6
        a, c = c, a; t += 0.1
fp = [(0, 'Steg 1: direktspel', 'Passa med insidan.'),
      (steps[1], 'Steg 2: flytta bollen i sidled', 'Passa med andra touchen.'),
      (steps[2], 'Steg 3: ta med bollen ca 2 m', 'Och passa åt båda håll.'),
      (steps[2] + 3.0, 'Anpassa avståndet', 'Efter skicklighet.')]
finish(d, 'fi19', 'insidespassning-i-tre-steg', ['Insidespassning', 'I tre steg'], 'Par · Avståndet anpassas efter skicklighet',
       fp, 'PASSNINGSÖVNING', [], [lab(s, s + 1.4, (50, 10), f'STEG {i + 1}') for i, s in enumerate(steps)])

# ============ fi20 Mottagning och vändning i tre ============
d = Drill()
d.p('e1', '', B, (50, 86)); d.p('m', 'M', B, (50, 52)); d.p('e2', '', B, (50, 14))
b = d.newball(rec(d, 'e1', 0)); t = 0.4; marks = []
for rep in range(4):
    src, dst = ('e1', 'e2') if rep % 2 == 0 else ('e2', 'e1')
    d.mv('m', t, t + 0.6, (50, 56 if src == 'e1' else 48))
    t1 = d.pas(b, t + 0.1, rec(d, 'm', t + 1.0))
    d.mv('m', t1, t1 + 0.6, (54, 52)); d.carry(b, 'm', t1, t1 + 0.6); marks.append(t1)                        # tar emot och vänder
    t2 = d.pas(b, t1 + 0.7, rec(d, dst, t1 + 1.6))
    t = t2 + 0.3
fp = [(0, 'Passa till mittspelaren', 'Tre spelare på rad.'),
      (marks[0], 'Ta emot och vänd', 'Passa till den tredje.'),
      (marks[1], 'Bollen tillbaka – vänd igen', ''),
      (marks[3], 'Byt uppgifter', 'Variant i par: vänd och skjut mot mål.')]
finish(d, 'fi20', 'mottagning-och-vandning-i-tre', ['Mottagning och vändning', 'I tre'], 'Tre spelare på rad',
       fp, 'PASSNINGSÖVNING', [])

# ============ fi21 Hitta varandra ============
d = Drill()
COLS = [B, R, YEL, ORA]; ST = [[(24, 26), (40, 40)], [(70, 24), (60, 42)], [(26, 70), (44, 58)], [(72, 72), (56, 62)]]
for p in range(4):
    for j in range(2): d.p(f'p{p}{j}', '', COLS[p], ST[p][j])
for p in range(4):
    for j in range(2): wander(d, f'p{p}{j}', 0, 17.9, boxes([ST[p][j]], 9)[0], 3500 + 10 * p + j, 1.5)
for p in range(4):
    b = d.newball(rec(d, f'p{p}0', 0)); t = 0.4 + 0.3 * p
    for rep in range(9): t = d.pas(b, t + 0.6, rec(d, f'p{p}{(rep + 1) % 2}', t + 1.5))
fp = [(0, 'Alla rör sig fritt', 'Två spelare per boll.'),
      (2.0, 'Passa inom paret', ''),
      (6.0, 'Bara när vägen är fri', 'Ingen spelare eller boll i vägen.'),
      (11.0, 'Lyft blicken', 'Hitta din kompis.')]
finish(d, 'fi21', 'hitta-varandra', ['Hitta varandra', 'Passningsövning'], 'Begränsat område · Två spelare per boll',
       fp, 'PASSNINGSÖVNING', [('box', 10, 12, 90, 88)])

# ============ fi22 Treminutersmatcher ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96))
BP = [(30, 66), (70, 64), (44, 48), (60, 80)]; RP = [(34, 34), (66, 36), (50, 56), (40, 20)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b2', 'b1'], 0.3); tout = d.pas(b, t + 0.1, (78, -3), 0.8); hide(d, b, tout + 0.1)     # utanför
b2 = d.newball((200, 200)); show(d, b2, tout + 0.4, rec(d, 'mvr', tout + 0.4))                            # motståndarnas målvakt startar med ny boll
t = d.pas(b2, tout + 0.7, rec(d, 'r0', tout + 1.5)); t = chain(d, b2, t, ['r2'], 0.3)
d.mv('r2', t, t + 1.2, (52, 78)); d.carry(b2, 'r2', t, t + 1.2); t += 1.2; tg = shoot(d, b2, t + 0.1, (46, 99))
d.mv('b3', tg - 1.4, tg, (58, 86))
fp = [(0, 'Matchspel i korta omgångar', '4–6 spelare per lag och målvakter.'),
      (tout - 0.3, 'Inga inkast eller hörnor', 'Motståndarnas målvakt startar med ny boll.'),
      (tout + 0.7, 'Spela direkt', ''),
      (tg - 0.4, 'Flest mål på tre minuter vinner', '')]
finish(d, 'fi22', 'treminutersmatcher', ['Treminuters-', 'matcher'], 'Yta ca 20 × 30 m · Två lag med målvakter',
       fp, 'SMÅLAGSSPEL', [('box', 14, 2, 86, 98)], [lab(tg, tg + 1.8, (46, 88), 'MÅL')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ xx01 Fotbollsputt ============
d = Drill()
for k in range(4): d.p(f'p{k}', '', B, (8, 42 + 6 * k))
balls = [d.newball(rec(d, f'p{k}', 0)) for k in range(4)]
ends = [(52, 56), (70, 42), (64, 55), (84, 46)]; t = 0.4; best = 0; ex = []
for k in range(4):
    pid = f'p{k}'
    d.mv(pid, t, t + 0.6, (8, 50)); d.carry(balls[k], pid, 0, t + 0.6)
    t1 = d.pas(balls[k], t + 0.7, ((ends[k][0] + 8) / 2 + 4, 50), 1.0); t2 = d.pas(balls[k], t1, ends[k], 0.7)   # rullar längs linjen – och av
    hide(d, balls[k], t2 + 0.3)                                                                              # bollen plockas upp
    d.mv(pid, t2 - 0.6, t2 + 2.0, (14 + 6 * k, 78))
    if ends[k][0] > best:
        if ex: ex[-1]['t1'] = t1 + 0.7
        best = ends[k][0]; ex.append(lab(t1 + 0.7, 18, (best, 34 if k % 2 else 64), 'REKORD'))
    t = t2 + 0.4
fp = [(0, 'Passa längs linjen', 'Så att bollen rullar så länge som möjligt.'),
      (2.2, 'En kon där bollen lämnar linjen', ''),
      (4.6, 'Nytt rekord – flytta konen', ''),
      (9.0, 'Vem slår rekordet?', '')]
finish(d, 'xx01', 'fotbollsputt', ['Fotbollsputt', 'Passningsövning'], 'Mittlinjen eller annan kritad linje',
       fp, 'PASSNINGSÖVNING', [('line', [(8, 50), (96, 50)])], ex)

# ============ xx02 Reaktor ============
d = Drill(); d.p('mv', 'MV', R, (50, 4)); d.p('t', 'T', T_COL, (50, 96))
for k in range(3): d.p(f'b{k}', '', B, (34, 54 + 8 * k)); d.p(f'r{k}', '', ORA, (66, 54 + 8 * k))
b1 = d.newball(rec(d, 't', 0)); b2 = d.newball((200, 200))
t = d.pas(b1, 0.4, (50, 36), 1.6)                                                                            # rullar mellan raderna
d.mv('b0', 0.8, t + 0.2, (48, 38)); d.mv('r0', 0.9, t + 0.4, (54, 40))                                       # första paret reagerar
d.carry(b1, 'b0', t + 0.2, t + 1.2); d.mv('b0', t + 0.2, t + 1.2, (46, 24)); d.mv('r0', t + 0.4, t + 1.2, (52, 28))   # duell
tg = shoot(d, b1, t + 1.3, (44, 1)); hide(d, b1, tg + 0.4)
d.mv('b0', tg + 0.2, tg + 2.6, (34, 78)); d.mv('r0', tg + 0.2, tg + 2.6, (66, 78))
for k in (1, 2): d.mv(f'b{k}', tg + 0.4, tg + 1.4, (34, 54 + 8 * (k - 1))); d.mv(f'r{k}', tg + 0.4, tg + 1.4, (66, 54 + 8 * (k - 1)))
show(d, b2, tg + 1.6, rec(d, 't', tg + 1.6)); t = d.pas(b2, tg + 1.8, (52, 30), 1.4)                       # snabbare boll
d.mv('r1', tg + 2.1, t + 0.1, (54, 32)); d.mv('b1', tg + 2.2, t + 0.3, (48, 34))
d.carry(b2, 'r1', t + 0.1, t + 0.9); d.mv('r1', t + 0.1, t + 0.9, (56, 20)); d.mv('b1', t + 0.3, t + 0.9, (50, 24))
tg2 = shoot(d, b2, t + 1.0, (54, 1))
fp = [(0, 'Instruktören rullar en boll mellan raderna', 'Två rader 20–25 m från mål.'),
      (1.0, 'Första paret reagerar', 'Spurta till bollen.'),
      (t - 1.8, 'Vinn duellen och skjut', ''),
      (tg + 1.6, 'Variera boll och startläge', 'Snabbt, långsamt, högt, lågt, liggande.')]
finish(d, 'xx02', 'reaktor', ['Reaktor', 'Lek och reaktion'], 'Två rader 20–25 m från mål · En målvakt',
       fp, 'LEK', [])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

if __name__ == '__main__': render(C, sys.argv)
