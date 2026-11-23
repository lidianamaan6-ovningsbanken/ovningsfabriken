# Externa övningar, omgång 14 (tolv st). Regel: först d.mv, sedan d.carry; först mottagarens rörelse, sedan passningen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e9', __file__.replace('render_extern14.py', 'render_extern9.py'))
e9 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e9); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e9.finish, e9.rec, e9.chain, e9.wander, e9.counter, e9.arrivals
lab, hide, show, team, boxes, drive, shoot = e9.lab, e9.hide, e9.show, e9.team, e9.boxes, e9.drive, e9.shoot
factor, swap_color, stand, countdown, countup, win = e9.factor, e9.swap_color, e9.stand, e9.countdown, e9.countup, e9.win
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'
def dribblers(d, pre, pts, col, seed, t1=17.9, step=1.6, r=7, labels=None):
    balls = []
    for k, ps in enumerate(pts):
        d.p(f'{pre}{k}', labels[k] if labels else '', col, ps); balls.append(d.newball(rec(d, f'{pre}{k}', 0)))
    return balls

# ============ sa8 Målvaktsträning – inlägg ============
d = Drill(); d.p('mv', 'MV', ORA, (50, 5)); d.p('t', 'T', T_COL, (60, 60)); d.p('mv2', 'MV', ORA, (50, 95))
d.p('k', 'Y', B, (88, 56)); team(d, 'a', B, [(42, 30), (56, 34)]); d.p('m', 'M', R, (30, 44))
b = d.newball(rec(d, 't', 0))
t = d.pas(b, 0.4, rec(d, 'k', 1.3)); t = drive(d, b, 'k', t, (88, 16), 20)                               # driver i korridoren
d.mv('a0', t - 1.4, t + 0.6, (46, 12)); d.mv('a1', t - 1.4, t + 0.6, (58, 14))
d.mv('mv', t + 0.2, t + 1.0, (54, 9)); t = d.pas(b, t + 0.1, rec(d, 'mv', t + 1.0), 0.9); tc = t       # målvakten fångar
d.carry(b, 'mv', tc, tc + 0.4); t = d.pas(b, tc + 0.5, rec(d, 'm', tc + 1.5), 1.0)                     # sätter igång spelet direkt
d.mv('k', tc, tc + 2.4, (88, 56)); d.mv('a0', tc, tc + 2.0, (42, 30)); d.mv('a1', tc, tc + 2.0, (56, 34)); d.mv('mv', tc + 0.6, tc + 1.4, (50, 5))
b2 = d.newball((200, 200)); show(d, b2, tc + 1.6, rec(d, 't', tc + 1.6))
t = d.pas(b2, tc + 1.8, rec(d, 'k', tc + 2.8)); t = drive(d, b2, 'k', t, (88, 16), 20)
d.mv('a0', t - 1.4, t + 0.6, (48, 10)); d.mv('a1', t - 1.4, t + 0.6, (56, 12))
d.mv('mv', t + 0.2, t + 1.0, (52, 10)); t = d.pas(b2, t + 0.1, rec(d, 'mv', t + 1.0), 0.9); tb = t      # boxar
tb2 = d.pas(b2, tb + 0.05, (28, 30), 0.7); hide(d, b2, tb2 + 0.3)
fp = [(0, 'Tränaren spelar till anfallaren', 'Som driver i korridoren och slår inlägg.'),
      (tc - 0.6, 'Målvakten fångar', 'Och sätter igång spelet direkt.'),
      (tc + 1.8, 'Nytt inlägg', ''),
      (tb - 0.4, 'Eller boxar undan', 'Byt roller efter fyra inlägg.')]
finish(d, 'sa8', 'malvaktstraning-inlagg', ['Målvaktsträning', 'Inlägg'], 'Yta ca 50 × 60 m med två mål',
       fp, 'MÅLVAKT', [('zone', 80, 4, 100, 96, (200, 220, 200), '')], [lab(tc, tc + 1.4, (64, 16), 'FÅNGAR'), lab(tb, tb + 1.4, (64, 16), 'BOXAR')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ ok01 Svansleken ============
d = Drill()
ST = [(22, 26), (50, 22), (78, 26), (22, 72), (50, 76), (78, 72), (36, 50), (64, 50)]
balls = dribblers(d, 'p', ST, B, 0)
BX = [(14, 18, 32, 36), (42, 16, 58, 30), (68, 18, 86, 36), (14, 62, 32, 82), (42, 68, 58, 84), (68, 62, 86, 82), (28, 42, 44, 58), (56, 42, 72, 58)]
# p6 tar p0:s svans, sedan tar p0 svansen från p3
for k in (1, 2, 4, 5, 7): wander(d, f'p{k}', 0, 17.9, BX[k], 2300 + k, 1.6); d.carry(balls[k], f'p{k}', 0, 17.9)
d.mv('p0', 0, 2.4, (28, 34)); d.mv('p6', 0, 2.4, (32, 40)); t1 = 2.6
stand(d, 'p0', 2.4, 3.0); stand(d, 'p6', 2.4, 3.0)
wander(d, 'p6', 3.0, 17.9, BX[6], 2306, 1.6); d.carry(balls[6], 'p6', 0, 17.9)
wander(d, 'p3', 0, 6.4, BX[3], 2303, 1.6); d.mv('p3', 6.4, 7.6, (26, 62)); d.mv('p0', 3.0, 7.6, (24, 56)); t2 = 7.8
stand(d, 'p0', 7.6, 8.2); stand(d, 'p3', 7.6, 8.2)
wander(d, 'p0', 8.2, 17.9, BX[0], 2310, 1.6); wander(d, 'p3', 8.2, 17.9, BX[3], 2313, 1.6)
d.carry(balls[0], 'p0', 0, 17.9); d.carry(balls[3], 'p3', 0, 17.9)
fp = [(0, 'Alla dribblar med en svans', 'Väst nedstoppad i byxlinningen.'),
      (t1 - 0.3, 'Ta så många svansar som möjligt', 'Utan att tappa din boll.'),
      (t2 - 0.3, 'Tappat svansen? Ta någon annans', ''),
      (11, 'Skydda bollen och svansen', 'Lyft blicken.')]
finish(d, 'ok01', 'svansleken', ['Svansleken', 'Lek med boll'], 'Yta 25 × 20 m · Alla har en boll och en svans',
       fp, 'LEK MED BOLL', [('box', 10, 12, 90, 88)], [lab(t1, t1 + 1.6, (36, 32), '+1 SVANS'), lab(t2, t2 + 1.6, (30, 48), '+1 SVANS')])
f = factor(fp)
for i, pid in enumerate(d.order):
    if pid == 'p6': C[-1]['players'][i]['tails'] = (lambda tt, a=t1 * f: 1 if tt < a else 2)
    elif pid == 'p0': C[-1]['players'][i]['tails'] = (lambda tt, a=t1 * f, b2=t2 * f: 1 if tt < a else (0 if tt < b2 else 1))
    elif pid == 'p3': C[-1]['players'][i]['tails'] = (lambda tt, b2=t2 * f: 1 if tt < b2 else 0)
    else: C[-1]['players'][i]['tails'] = (lambda tt: 1)

# ============ ok02 Rävar och bönder ============
d = Drill()
ST = [(22, 26), (50, 22), (78, 26), (22, 72), (50, 76), (78, 72)]
balls = dribblers(d, 'r', ST, ORA, 0); team(d, 'b', B, [(40, 50), (62, 50)], ['', ''])
BX = [(14, 18, 34, 40), (40, 16, 60, 34), (66, 18, 86, 40), (14, 58, 34, 82), (40, 66, 60, 82), (66, 58, 86, 82)]
for k in (1, 3, 4, 5): wander(d, f'r{k}', 0, 17.9, BX[k], 2400 + k, 1.6); d.carry(balls[k], f'r{k}', 0, 17.9)
d.mv('r0', 0, 2.2, (26, 32)); d.carry(balls[0], 'r0', 0, 2.4); d.mv('b0', 0.3, 2.4, (32, 36))
t1 = d.pas(balls[0], 2.6, (4, 30), 0.7); hide(d, balls[0], t1 + 0.3)                                  # bonden sparkar ut bollen
stand(d, 'r0', 2.2, 3.0); d.mv('r0', 3.0, 5.0, (40, 58)); wander(d, 'b0', 2.4, 17.9, (34, 34, 50, 50), 2410, 1.6)   # räven blir bonde
wander(d, 'r2', 0, 6.4, BX[2], 2402, 1.6); d.mv('r2', 6.4, 7.4, (76, 34)); d.carry(balls[2], 'r2', 0, 7.6)
d.mv('b1', 0.4, 7.4, (70, 38)); t2 = d.pas(balls[2], 7.8, (97, 40), 0.7); hide(d, balls[2], t2 + 0.3)
stand(d, 'r2', 7.4, 8.2); d.mv('r2', 8.2, 10.0, (64, 56)); wander(d, 'r2', 10.0, 17.9, (56, 48, 72, 60), 2420, 1.6)
wander(d, 'b1', 7.8, 17.9, (62, 34, 78, 48), 2411, 1.6); wander(d, 'r0', 5.0, 17.9, (34, 52, 48, 62), 2412, 1.6)
fp = [(0, 'Rävarna dribblar i hönsgården', 'Bönderna försöker sparka ut bollarna.'),
      (t1 - 0.4, 'Bollen ut – räven blir bonde', ''),
      (t2 - 0.4, 'Fler bönder – svårare för rävarna', ''),
      (12, 'Pågår tills en räv är kvar', 'Nästa omgång börjar de sista rävarna som bönder.')]
finish(d, 'ok02', 'ravar-och-bonder', ['Rävar och bönder', 'Lek med boll'], 'Yta 25 × 20 m · Rävarna har varsin boll',
       fp, 'LEK MED BOLL', [('box', 10, 12, 90, 88)], [lab(t1, t1 + 1.6, (22, 46), 'NY BONDE'), lab(t2, t2 + 1.6, (78, 50), 'NY BONDE')])
f = factor(fp); ids = {k: i for i, k in enumerate(d.order)}
swap_color(ids['r0'], (t1 - 0.2) * f, ORA, B); swap_color(ids['r2'], (t2 - 0.2) * f, ORA, B)

# ============ ok03 Samla bollar ============
d = Drill()
team(d, 'b', B, [(12, 30), (12, 50), (12, 70)], ['', '', '']); team(d, 'r', R, [(88, 30), (88, 50), (88, 70)], ['', '', '']); team(d, 'j', YEL, [(44, 40), (58, 62)], ['J', 'J'])
BALLS = [(34, 24), (66, 26), (40, 56), (60, 50), (32, 78), (68, 76)]
bl = [d.newball(p) for p in BALLS]
def fetch(pid, bi, t, home, spd=14):
    bx, by = BALLS[bi]; t2 = t + max(0.8, ((d.pos(pid)[0] - bx) ** 2 + (d.pos(pid)[1] - by) ** 2) ** .5 / spd)
    d.mv(pid, t, t2, (bx - 2, by + 1)); t3 = t2 + max(1.0, abs(home[0] - bx) / spd); d.mv(pid, t2 + 0.1, t3, home); d.carry(bl[bi], pid, t2 + 0.1, t3); return t3
t = fetch('b0', 0, 0.4, (10, 26)); fetch('r0', 1, 0.6, (90, 26)); fetch('r2', 5, 0.8, (90, 74))
# b1 blir kullad och lämnar bollen
bx, by = BALLS[2]; d.mv('b1', 0.5, 2.0, (bx - 2, by + 1)); d.mv('b1', 2.1, 3.6, (28, 56)); d.carry(bl[2], 'b1', 2.1, 3.6)
d.mv('j0', 1.0, 3.6, (30, 52)); tk = 3.6; d.mv('b1', tk + 0.2, tk + 1.6, (12, 50))                     # kullad – springer hem
wander(d, 'j0', tk + 0.4, 17.9, (34, 30, 56, 70), 2500, 1.6)
fetch('b2', 4, 1.0, (10, 74)); fetch('r1', 3, 1.0, (90, 50))
t = fetch('b1', 2, tk + 2.0, (10, 50))
wander(d, 'j1', 0, 17.9, (48, 30, 66, 70), 2501, 1.6)
fp = [(0, 'Driv bollar till ert bo', 'Två jägare försöker kulla.'),
      (tk - 0.3, 'Kullad – lämna bollen', 'Och spring hem.'),
      (tk + 2.0, 'Försök igen', ''),
      (12, 'Slut när alla bollar är samlade', 'Byt jägare.')]
finish(d, 'ok03', 'samla-bollar', ['Samla bollar', 'Lek med boll'], 'Två lag med varsitt bo · Bollar utspridda · Två jägare',
       fp, 'LEK MED BOLL', [('box', 4, 12, 96, 88), ('zone', 4, 12, 18, 88, (120, 170, 230), 'BO'), ('zone', 82, 12, 96, 88, (230, 120, 110), 'BO')],
       [lab(tk, tk + 1.6, (30, 44), 'KULLAD')])

# ============ ok04 Följa John ============
d = Drill(); d.p('L', 'L', YEL, (50, 26))
OFF = [(-16, 16), (0, 16), (16, 16), (-16, 32), (0, 32), (16, 32)]
for k, o in enumerate(OFF): d.p(f'p{k}', '', B, (50 + o[0], 26 + o[1]))
LP = [(0.4, (50, 26)), (2.6, (30, 30)), (3.6, (30, 30)), (5.6, (46, 40)), (7.4, (66, 30)), (8.4, (66, 30)), (10.4, (60, 46)), (12.0, (40, 46)), (13.0, (40, 46)), (15.0, (52, 34))]
lb = d.newball(rec(d, 'L', 0)); pb = [d.newball(rec(d, f'p{k}', 0)) for k in range(6)]
for (ta, pa), (tb_, pb_) in zip(LP, LP[1:]):
    d.mv('L', ta, tb_, pb_)
    for k, o in enumerate(OFF): d.mv(f'p{k}', ta + 0.3, tb_ + 0.3, (pb_[0] + o[0], pb_[1] + o[1]))       # alla härmar
d.carry(lb, 'L', 0, 15.4)
for k in range(6): d.carry(pb[k], f'p{k}', 0, 15.4)
fp = [(0, 'Ledaren driver – alla härmar', 'Alla har en boll.'),
      (2.6, 'Stanna bollen med sulan', 'Alla gör samma sak.'),
      (5.6, 'Byt riktning och tempo', ''),
      (12.0, 'Byt ledare ibland', 'Sedan samma sak i par.')]
finish(d, 'ok04', 'folja-john', ['Följa John', 'Lek med boll'], 'Fri yta · Alla har boll · En ledare',
       fp, 'LEK MED BOLL', [], [lab(2.6, 3.6, (30, 20), 'STOPP'), lab(7.4, 8.4, (66, 20), 'STOPP'), lab(12.0, 13.0, (40, 36), 'STOPP')])

# ============ ok05 Doppboll ============
d = Drill()
BP = [(30, 70), (60, 62), (44, 46), (70, 36)]; RP = [(40, 60), (68, 52), (34, 40), (56, 30)]
team(d, 'b', B, BP); team(d, 'r', R, RP); d.p('bg', '', B, (50, 10))
for k in range(4): wander(d, f'r{k}', 0, 6, boxes([RP[k]], 3)[0], 2600 + k, 1.8)
b = d.newball(rec(d, 'b0', 0)); marks = []
def dopp(frm, to, t):
    fx, fy = at(d.pl[frm]['tr'], t); tx, ty = rec(d, to, t + 1.0)
    t1 = d.pas(b, t, ((fx + tx) / 2, (fy + ty) / 2), 0.5); marks.append(t1); return d.pas(b, t1, (tx, ty), 0.5)   # studsar mitt emellan
t = dopp('b0', 'b2', 0.6); stand(d, 'b2', t - 1.0, t + 0.6)                                            # ingen får springa med bollen
t = dopp('b2', 'b3', t + 0.6); stand(d, 'b3', t - 1.0, t + 0.6)
d.mv('bg', t - 1.0, t + 0.4, (60, 10)); t = dopp('b3', 'bg', t + 0.6); tg = t                         # till medspelare i målytan
fp = [(0, 'Två lag spelar med händerna', 'Ingen får springa med bollen.'),
      (marks[0] - 0.2, 'Bollen studsar före varje kast', 'Annars får motståndarna den.'),
      (marks[1], 'Rör dig utan boll', 'Bli spelbar för kastaren.'),
      (tg - 0.4, 'Mål: kast till medspelare i målytan', '')]
finish(d, 'ok05', 'doppboll', ['Doppboll', 'Lek och reaktion'], 'Yta 25 × 20 m med en målyta i varje ände',
       fp, 'LEK', [('box', 10, 4, 90, 96), ('zone', 30, 4, 70, 16, (120, 170, 230), 'MÅLYTA'), ('zone', 30, 84, 70, 96, (230, 120, 110), 'MÅLYTA')],
       [lab(m, m + 0.6, (84, 60), 'STUDS') for m in marks] + [lab(tg, tg + 1.6, (50, 22), 'MÅL')])

# ============ ok06 Champions League (kaosboll) ============
d = Drill()
ST = [(30, 30), (54, 26), (74, 36), (26, 58), (50, 52), (72, 64), (40, 76)]
balls = dribblers(d, 'p', ST, B, 0); BX = boxes(ST, 6)
for k in (0, 2, 3, 5, 6): wander(d, f'p{k}', 0, 17.9, BX[k], 2700 + k, 1.6); d.carry(balls[k], f'p{k}', 0, 17.9)
d.mv('p4', 0, 2.4, (60, 34)); d.carry(balls[4], 'p4', 0, 2.4); d.mv('p1', 0, 2.4, (56, 30)); d.carry(balls[1], 'p1', 0, 2.6)
t1 = d.pas(balls[1], 2.6, (66, 6), 0.7)                                                                 # skjuts ut
d.mv('p1', 2.7, 3.8, (66, 8)); d.mv('p1', 4.0, 5.4, (92, 6)); d.mv('p1', 5.4, 6.2, (95, 12)); d.mv('p1', 6.2, 8.0, (60, 28))   # runt konen och in igen
d.carry(balls[1], 'p1', 3.8, 8.0); wander(d, 'p1', 8.0, 17.9, BX[1], 2711, 1.6); d.carry(balls[1], 'p1', 8.0, 17.9)
wander(d, 'p4', 2.4, 17.9, BX[4], 2704, 1.6); d.carry(balls[4], 'p4', 2.4, 17.9)
fp = [(0, 'Alla dribblar', 'Och försöker skjuta ut de andras bollar.'),
      (t1 - 0.5, 'Bollen ut', 'Spring runt en kon med bollen och kom tillbaka in.'),
      (6.2, 'Tillbaka in', ''),
      (11, 'Max en halv meter till din boll', 'Då är den svår att ta.')]
finish(d, 'ok06', 'champions-league-kaosboll', ['Champions League', 'Kaosboll'], 'Yta 25 × 20 m · Alla har en boll',
       fp, 'LEK MED BOLL', [('box', 12, 14, 88, 86), ('cone', 94, 6), ('cone', 6, 6), ('cone', 94, 94), ('cone', 6, 94)])

# ============ ok07 Driva med stopp ============
d = Drill(); d.p('t', 'T', T_COL, (50, 94))
ST = [(22, 26), (46, 24), (72, 28), (24, 54), (50, 50), (76, 56), (34, 76), (64, 76)]
balls = dribblers(d, 'p', ST, B, 0); BX = boxes(ST, 7)
STOPS = [(3.6, 5.6, 'STOPP – SULAN'), (8.6, 10.6, 'STOPP – KNÄET'), (13.6, 15.6, 'STOPP – PANNAN')]
for k in range(8):
    pid = f'p{k}'; t = 0
    for s0, s1, _ in STOPS:
        wander(d, pid, t, s0, BX[k], 2800 + k * 7 + int(s0), 1.2); stand(d, pid, s0, s1); t = s1
    wander(d, pid, t, 17.9, BX[k], 2899 + k, 1.2); d.carry(balls[k], pid, 0, 17.9)
fp = [(0, 'Driv nära fötterna', 'Alla har en boll.'),
      (3.6, 'STOPP: sulan på bollen', 'Stå helt still.'),
      (8.6, 'STOPP: knät på bollen', 'Sedan rumpa och panna.'),
      (13.6, 'Variant: grönt, gult och rött', 'Rött betyder stopp.')]
finish(d, 'ok07', 'driva-med-stopp', ['Driva med stopp', 'Teknik'], 'Yta 25 × 20 m · Alla har en boll',
       fp, 'TEKNIK', [('box', 10, 14, 90, 88)], [lab(s0, s1, (50, 8), txt) for s0, s1, txt in STOPS])

# ============ ok08 Vändningar ============
d = Drill()
CONES = [(20, 22), (80, 24), (24, 78), (78, 76), (50, 50), (50, 16), (50, 84), (16, 50), (84, 50)]
ST = [(36, 34), (64, 36), (36, 66), (64, 64), (30, 50), (70, 50)]
TG = [[(20, 22), (50, 50)], [(80, 24), (50, 16)], [(24, 78), (16, 50)], [(78, 76), (50, 84)], [(16, 50), (20, 22)], [(84, 50), (78, 76)]]
balls = dribblers(d, 'p', ST, B, 0)
for k in range(6):
    pid = f'p{k}'; t = 0.3 * k
    for lap in range(4):
        cx, cy = TG[k][lap % 2]; sx, sy = d.pos(pid)
        dx, dy = cx - sx, cy - sy; L = (dx * dx + dy * dy) ** .5 or 1
        stop = (cx - dx / L * 5, cy - dy / L * 5)                           # vänd en bit före konen
        dur = max(1.2, L / 14); d.mv(pid, t, t + dur, stop); d.mv(pid, t + dur, t + dur + 0.5, (stop[0] - dx / L * 3, stop[1] - dy / L * 3))
        t += dur + 0.6
    d.carry(balls[k], pid, 0, t)
fp = [(0, 'Driv mot en kon och vänd', 'Koner utspridda i ytan.'),
      (3, 'Ny kon – ny vändning', 'Insida, utsida eller sula.'),
      (8, 'Huvudet upp', 'Se var de andra är.'),
      (12, 'Uppgradering: utan koner', 'Vänd när en annan spelare kommer nära.')]
finish(d, 'ok08', 'vandningar', ['Vändningar', 'Teknik'], 'Yta 25 × 20 m med koner utspridda',
       fp, 'TEKNIK', [('box', 8, 10, 92, 90)] + [('cone',) + c for c in CONES])

# ============ ok09 Vändning på signal ============
d = Drill(); d.p('t', 'T', T_COL, (96, 94))
ST = [(30, 30), (54, 26), (74, 36), (26, 58), (50, 52), (72, 64), (40, 76), (62, 80)]
balls = dribblers(d, 'p', ST, B, 0); BX = boxes(ST, 6)
SIDE_B = [(26, 18), (38, 18), (50, 18), (62, 18), (74, 18), (32, 26), (56, 26), (68, 26)]
SIDE_D = [(18, 26), (18, 38), (18, 50), (18, 62), (18, 74), (26, 32), (26, 56), (26, 68)]
for k in range(8):
    pid = f'p{k}'
    wander(d, pid, 0, 3.4, BX[k], 2900 + k, 1.6); d.mv(pid, 3.6, 5.6, SIDE_B[k]); wander(d, pid, 6.0, 9.6, BX[k], 2910 + k, 1.6)
    d.mv(pid, 9.8, 11.8, SIDE_D[k]); wander(d, pid, 12.2, 17.9, BX[k], 2920 + k, 1.6); d.carry(balls[k], pid, 0, 17.9)
fp = [(0, 'Driv och vänd vid konerna', 'Rektangelns sidor har namn.'),
      (3.4, 'Tränaren ropar ”NORR!”', 'Alla driver till den sidan.'),
      (6.0, 'Fortsätt sedan', 'Lägg till en fint vid varje kon.'),
      (9.6, 'Ny signal: ”VÄST!”', '')]
finish(d, 'ok09', 'vandning-pa-signal', ['Vändning på signal', 'Lek och reaktion'], 'Yta 25 × 20 m · Rektangelns sidor har namn',
       fp, 'LEK', [('box', 12, 12, 88, 88), ('text', 50, 7, 'NORR'), ('text', 50, 93, 'SYD'), ('text', 6, 50, 'VÄST'), ('text', 94, 50, 'ÖST')],
       [lab(3.4, 5.4, (70, 44), '”NORR!”'), lab(9.6, 11.6, (70, 44), '”VÄST!”')])

# ============ ok10 Hinderbana med finter ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
CN = [(40, 80), (60, 70), (40, 60), (60, 50), (40, 40), (60, 30)]
for k in range(3): d.p(f'p{k}', '', B, (50, 92 + 3 * k))
balls = [d.newball(rec(d, f'p{k}', 0)) for k in range(3)]
for k in range(3):
    pid = f'p{k}'; t = 0.4 + 4.2 * k
    if k: d.mv(pid, t - 1.0, t, (50, 92))
    d.carry(balls[k], pid, 0, t)
    pts = [(c[0] - 6 if c[0] < 50 else c[0] + 6, c[1]) for c in CN] + [(52, 20)]          # utsidan av konerna
    t2 = d.path(pid, t, pts, 1.6); d.carry(balls[k], pid, t, t2)
    d.mv(pid, t2, t2 + 0.5, (50, 16)); d.carry(balls[k], pid, t2, t2 + 0.5)                    # sista sträckan i full fart
    tg = shoot(d, balls[k], t2 + 0.5, (44 + 6 * k, 1)); hide(d, balls[k], tg + 0.4)
    d.mv(pid, tg + 0.2, tg + 2.4, (70, 94 - 3 * k))
fp = [(0, 'Driv genom banan', 'Riktningsförändring på utsidan av konerna.'),
      (2.2, 'Fint vid varje kon', 'I banans slutdel.'),
      (3.6, 'Sista sträckan i full fart mot mål', 'Och avslut.'),
      (8.0, 'Variant: rullning före avslut', 'Nästa spelare startar.')]
finish(d, 'ok10', 'hinderbana-med-finter', ['Hinderbana', 'Med finter'], 'Konbana i sicksack som slutar mot ett mål',
       fp, 'TEKNIK', [('cone',) + c for c in CN])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ ok11 Kolonner med finter ============
d = Drill()
LANES = [24, 50, 76]
for li, x in enumerate(LANES):
    d.p(f'a{li}', '', B, (x, 82)); d.p(f'b{li}', '', B, (x, 88))
balls = [d.newball(rec(d, f'a{li}', 0)) for li in range(3)]
for li, x in enumerate(LANES):
    t = 0.4 + 0.3 * li; order = [f'a{li}', f'b{li}']
    for lap in range(4):
        pid = order[lap % 2]; other = order[(lap + 1) % 2]; side = 1 if lap % 2 == 0 else -1     # högervarv, sedan vänstervarv
        pts = [(x, 40), (x + 5 * side, 32), (x, 26), (x - 5 * side, 32), (x, 40), (x, 78)]
        t2 = d.path(pid, t, pts, 1.4); d.carry(balls[li], pid, t, t2)
        d.mv(other, t2 - 1.0, t2 - 0.2, (x, 82))
        d.mv(pid, t2 + 0.2, t2 + 1.0, (x + 5, 88)); t = t2 + 0.1                                 # lämna över bollen
fp = [(0, 'Driv till konen framför', 'En boll per par.'),
      (1.6, 'Fint och runt konen', 'Först högervarv.'),
      (4.0, 'Tillbaka och lämna över', 'Nästa gör vänstervarv.'),
      (9.0, 'Max två spelare per kon', '')]
finish(d, 'ok11', 'kolonner-med-finter', ['Kolonner', 'Med finter'], 'Koner 8–10 m isär · En boll per par',
       fp, 'TEKNIK', [('cone', x, 32) for x in LANES] + [('cone', x, 86) for x in LANES])

if __name__ == '__main__': render(C, sys.argv)
