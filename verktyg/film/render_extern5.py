# Externa övningar, omgång 5 (tolv st). Regel: först d.mv, sedan d.carry; hide före show.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e4', __file__.replace('render_extern5.py', 'render_extern4.py'))
e4 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e4); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e4.finish, e4.rec, e4.chain, e4.wander, e4.counter, e4.arrivals
lab, hide, show, team, boxes, drive, shoot = e4.lab, e4.hide, e4.show, e4.team, e4.boxes, e4.drive, e4.shoot
factor, swap_color, stand = e4.factor, e4.swap_color, e4.stand
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'
def dist(a, b): return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** .5
def run(d, pid, t, to, speed=20):
    dur = max(0.5, dist(d.pos(pid), to) / speed); d.mv(pid, t, t + dur, to); return t + dur

# ============ w11 Passning genom portar ============
d = Drill()
COLS = [22, 50, 78]; ROWS = [24, 50, 76]
GATES = [(x, y) for x in COLS for y in ROWS]
pairs = []
for k, x in enumerate(COLS):
    a, bb = f'a{k}', f'b{k}'; d.p(a, str(k + 1), B, (x - 7, 24)); d.p(bb, str(k + 1), B, (x + 7, 24)); pairs.append((a, bb))
cnt = []
for k, (a, bb) in enumerate(pairs):
    ball = d.newball(rec(d, a, 0)); x = COLS[k]; seq = [24, 50, 76, 50, 24, 50, 76][: 6]
    hold, part = a, bb; t = 0.3 + 0.5 * k
    for n, gy in enumerate(seq):
        if n > 0:
            side_h = x - 7 if d.pos(hold)[0] < x else x + 7
            tt = run(d, hold, t, (side_h, gy), 16); d.carry(ball, hold, t, tt)
            run(d, part, t, (2 * x - side_h, gy), 16); t = tt + 0.2
        t = d.pas(ball, t, rec(d, part, t + 0.5), 0.5)                         # genom porten
        if k == 0: cnt.append(t)
        hold, part = part, hold; t += 0.15
fp = [(0, 'Passa genom en port till partnern', 'Paren rör sig fritt med en boll.'),
      (cnt[0] + 0.3, 'Spring till en ny port', 'Den med boll driver, partnern ställer sig på andra sidan.'),
      (cnt[2] - 0.3, 'Genom nästa port', 'Huvudet upp – välj en ledig port.'),
      (cnt[4] - 0.3, 'Hur många portar på en minut?', 'Räkna portarna tillsammans.')]
finish(d, 'w11', 'passning-genom-portar', ['Passning', 'Genom portar'], 'Små konportar i en stor ruta · Spelarna i par',
       fp, 'PASSNINGSÖVNING', [('box', 6, 12, 94, 88)] + [('cone', gx, gy - 3) for gx, gy in GATES] + [('cone', gx, gy + 3) for gx, gy in GATES],
       counter(cnt, pos=(22, 8), last=None))

# ============ w12 Mittfältarens vändning ============
d = Drill()
d.p('a0', 'A', B, (50, 86)); d.p('a1', 'A', B, (50, 92)); d.p('bb', 'B', B, (50, 54)); d.p('f', 'F', R, (50, 45)); d.p('cc', 'C', B, (50, 14))
b = d.newball(rec(d, 'a0', 0)); Q = ['a0', 'a1']; B_ = 'bb'; C_ = 'cc'; marks = []
t = 0.4
for r in range(2):
    a = Q.pop(0); side = 1 if r == 0 else -1
    d.mv(B_, t - 0.2, t + 0.5, (50 - 4 * side, 56))                            # scannar och gör sig spelbar
    d.mv('f', t, t + 0.8, (50 - 2 * side, 47))
    t1 = d.pas(b, t + 0.3, rec(d, B_, t + 1.0))                                # tar emot på bakre foten
    d.mv(B_, t1, t1 + 0.7, (50 + 6 * side, 50)); d.carry(b, B_, t1, t1 + 0.7)  # vänder bort från försvararen
    t2 = d.pas(b, t1 + 0.8, rec(d, C_, t1 + 1.7)); marks.append((t1, t2))
    run(d, a, t1 - 0.6, (50, 54), 18)                                          # alla roterar: A till B
    run(d, B_, t2 - 0.4, (56, 16), 20)
    for n, pid in enumerate(Q): d.mv(pid, t1, t1 + 0.6, (50, 86 + 6 * n))
    t3 = d.pas(b, t2 + 0.3, rec(d, Q[0], t2 + 1.6))                            # C spelar tillbaka
    run(d, C_, t3 - 0.6, (50, 86 + 6 * len(Q)), 24); Q.append(C_)
    d.mv(B_, t3, t3 + 0.6, (50, 14))
    B_, C_ = a, B_; t = t3 + 0.2
fp = [(0, 'A spelar till B', 'B scannar innan bollen kommer.'),
      (marks[0][0] - 0.2, 'Ta emot på bakre foten', 'Vänd bort från försvararen.'),
      (marks[0][1] - 0.6, 'B spelar till C', 'C spelar tillbaka till A-kön.'),
      (marks[0][1] + 0.6, 'Alla roterar', 'A blir B, B blir C, C går till kön.'),
      (marks[1][0] - 0.2, 'Nästa vändning – åt andra hållet', 'Försvararen är passiv.')]
finish(d, 'w12', 'mittfaltarens-vandning', ['Mittfältarens', 'vändning'], 'A, B (vändspelare) och C på linje · Passiv försvarare bakom B',
       fp, 'PASSNINGSÖVNING', [('cone', 50, 80), ('cone', 50, 20)], [lab(0.3, marks[0][0], (62, 60), 'SCANNA')])

# ============ w13 6 mot 2 + 1 flytande ============
d = Drill(); RP = [(26, 28), (50, 20), (74, 28), (74, 72), (50, 80), (26, 72)]
team(d, 'b', B, RP); team(d, 'r', R, [(40, 42), (60, 58)]); d.p('n', 'F', YEL, (50, 50))
wander(d, 'n', 0, 3.6, (46, 46, 54, 54), 900, 1.2)
b = d.newball(rec(d, 'b0', 0))
d.mv('r0', 0.3, 3.0, (36, 36)); d.mv('r1', 0.3, 3.0, (44, 30))                   # pressar i par
t = chain(d, b, 0.4, ['b1', 'b2', 'b3'], 0.25)
t = d.pas(b, t + 0.25, rec(d, 'n', t + 0.9)); tp = t                              # genom mitten: poäng
d.mv('r0', tp - 0.6, tp + 0.4, (62, 56)); d.mv('r1', tp - 0.6, tp + 0.4, (66, 66))
t = d.pas(b, t + 0.3, rec(d, 'b5', t + 0.9)); t = chain(d, b, t, ['b0', 'b1'], 0.25)
d.mv('r0', t - 1.6, t - 0.6, (44, 28)); d.mv('r0', t - 0.6, t + 0.2, rec(d, 'b1', t + 0.2))
tw = d.pas(b, t + 0.25, rec(d, 'r0', t + 0.5), 0.3)
d.mv('r0', tw + 0.3, tw + 1.6, RP[1]); d.mv('b1', tw + 0.3, tw + 1.6, (46, 36))  # den som tappade går in
wander(d, 'n', 3.6, tw + 2, (46, 46, 54, 54), 901, 1.2)
d.mv('r1', tw, tw + 1.2, (56, 44))
t = chain(d, b, tw + 1.7, ['b2', 'n', 'b5', 'b0'], 0.25)
fp = [(0, 'Sex runt kanten, två försvarare inne', 'Den flytande spelar alltid med laget som har bollen.'),
      (tp - 0.7, 'Genom mitten till den flytande', 'Ger en poäng.'),
      (tp + 0.8, 'Försvararna pressar i par', 'En pressar, en täcker.'),
      (tw - 0.2, 'Den som tappar bollen går in', 'Spelet fortsätter direkt.')]
finish(d, 'w13', '6-mot-2-plus-1-flytande', ['6 mot 2 + 1', 'Flytande'], 'Ruta ca 15 × 15 m · Sex runt kanten · Två försvarare och en flytande inne',
       fp, 'RONDO', [('box', 20, 14, 80, 86)], [lab(tp, tp + 1.8, (50, 40), '+1')])

# ============ w14 5 mot 2 – träffa mittkonen ============
d = Drill(); RP = [(34, 34), (52, 28), (68, 40), (62, 68), (36, 64)]
team(d, 'b', B, RP); team(d, 'r', R, [(44, 46), (58, 54)])
b = d.newball(rec(d, 'b0', 0))
d.mv('r0', 0.3, 3, (42, 42)); d.mv('r1', 0.3, 3, (56, 50))
t = chain(d, b, 0.4, ['b1', 'b2', 'b3', 'b4', 'b0', 'b2'], 0.2); cnt = arrivals(d, b)[:6]
d.mv('r0', t - 1, t, (44, 56)); d.mv('r1', t - 1, t, (40, 46))
tc = d.pas(b, t + 0.3, (51, 49), 0.6); t = d.pas(b, tc, rec(d, 'b4', tc + 0.6), 0.6)   # träffar konen
d.mv('r0', tc, tc + 1.2, (46, 48)); d.mv('r1', tc, tc + 1.2, (54, 52))
t = chain(d, b, t, ['b0', 'b1', 'b3'], 0.25)
fp = [(0, 'Fem runt rutan, två skyddar konen', 'Sex passningar i rad ger en poäng.'),
      (cnt[-1] - 0.3, 'Sex passningar: 1 poäng', 'Leta efter vägen till konen.'),
      (tc - 0.6, 'Träffa konen: 2 poäng', 'Försvararna skyddar konen med kroppen.'),
      (tc + 1.0, 'Spelet fortsätter', 'Rör bollen snabbt så att luckan öppnas.')]
finish(d, 'w14', '5-mot-2-traffa-mittkonen', ['5 mot 2', 'Träffa mittkonen'], 'Ruta ca 10 × 10 m med en kon i mitten',
       fp, 'RONDO', [('box', 26, 20, 74, 76), ('cone', 50, 50)], counter(cnt, pos=(50, 14)) + [lab(tc, tc + 1.8, (50, 40), '+2')])

# ============ w15 Rondo i två zoner med vertikal poäng ============
d = Drill()
# zon A (smal) x 8–34, zon B (bred) x 42–92, båda y 14–86
d.p('nA1', 'N', G, (21, 12)); d.p('nA2', 'N', G, (21, 88)); d.p('nAm', 'N', G, (21, 50)); d.p('nAf', 'N', G, (21, 66))
d.p('nB1', 'N', G, (67, 12)); d.p('nB2', 'N', G, (67, 88)); d.p('nBm', 'N', G, (67, 50)); d.p('nBf', 'N', G, (67, 32))
team(d, 'ba', B, [(13, 72), (29, 30)]); team(d, 'ra', R, [(28, 74), (14, 34)])
team(d, 'bb', B, [(50, 72), (84, 66), (52, 28)]); team(d, 'rb', R, [(60, 64), (78, 40), (82, 26)])
wander(d, 'nAf', 0, 17.9, (14, 58, 28, 74), 910, 2); wander(d, 'nBf', 0, 9, (58, 26, 76, 38), 911, 2)
for pid, bx in [('ra0', (24, 66, 32, 80)), ('ra1', (10, 26, 18, 40))]: wander(d, pid, 0, 17.9, bx, sum(map(ord, pid)), 2)
for pid, bx in [('rb0', (56, 58, 64, 70)), ('rb1', (74, 36, 84, 46))]: wander(d, pid, 0, 9, bx, sum(map(ord, pid)) + 7, 2)
# zon B: från ena änden till den andra genom mittspelaren
bB = d.newball(rec(d, 'nB2', 0))
t = chain(d, bB, 0.4, ['bb0', 'bb1', 'nBm'], 0.3); tp = t
t = chain(d, bB, t, ['bb2', 'nB1'], 0.25); tend = t
d.mv('rb2', t - 0.2, t + 0.9, rec(d, 'nB1', t + 0.9))
t = d.pas(bB, t + 0.6, rec(d, 'bb2', t + 1.3))
d.mv('rb2', t - 0.9, t + 0.2, rec(d, 'bb2', t + 0.2)); tw = d.pas(bB, t + 0.3, rec(d, 'rb2', t + 0.5), 0.3)   # rött vinner bollen
d.mv('bb2', tw, tw + 1.0, (62, 44))
t = d.pas(bB, tw + 0.3, rec(d, 'rb1', tw + 1.0)); t = d.pas(bB, t + 0.3, rec(d, 'nB2', t + 1.3)); tov = t    # till neutrala i motsatt ände
d.mv('rb0', tw, tov, (58, 74)); d.mv('rb1', t - 0.2, t + 0.8, (78, 66)); d.mv('nBf', tw, tw + 1.5, (66, 70))
t = chain(d, bB, tov, ['rb0', 'rb1', 'nBm'], 0.3); tp2 = t
# zon A: samma mönster
bA = d.newball(rec(d, 'nA2', 0))
t = chain(d, bA, 0.9, ['ba0', 'nAm', 'ba1', 'nA1', 'ba1', 'nAm', 'ba0', 'nA2', 'ba0', 'nAm', 'ba1'], 0.4)
fp = [(0, 'För bollen till andra änden', 'De neutrala spelar med laget som har bollen.'),
      (tp - 0.6, 'Genom mittspelaren: poäng', 'Mittspelaren står mellan dockorna.'),
      (tend - 0.4, 'Fram till neutrala i andra änden', 'Nu går bollen åt andra hållet.'),
      (tw - 0.2, 'Rött vinner bollen', 'Först till neutrala i motsatt ände.'),
      (tov - 0.2, 'Nu har rött tagit över', 'Och anfaller genom mittspelaren.')]
finish(d, 'w15', 'rondo-i-tva-zoner-med-vertikal-poang', ['Rondo i två zoner', 'Med vertikal poäng'], 'Zon A 10 × 30 m (2 mot 2 + 4) · Zon B 15 × 30 m (3 mot 3 + 4)',
       fp, 'POSITIONSSPEL', [('box', 8, 8, 34, 92), ('box', 42, 8, 92, 92), ('pole', 15, 50), ('pole', 27, 50), ('pole', 59, 50), ('pole', 75, 50),
                             ('text', 21, 4, 'ZON A'), ('text', 67, 4, 'ZON B')],
       [lab(tp, tp + 1.6, (82, 50), '+1'), lab(tov, tov + 1.6, (82, 90), 'ÖVERTAGEN'), lab(tp2, tp2 + 1.6, (82, 50), '+1')])

# ============ w16 Trefärgsrondo 4 + 4 mot 4 ============
d = Drill()
BP = [(20, 22), (80, 30), (60, 80), (24, 64)]; WP = [(50, 18), (82, 66), (20, 84), (16, 44)]; RP = [(40, 40), (60, 42), (44, 60), (62, 60)]
team(d, 'b', B, BP); team(d, 'w', WHITE, WP); team(d, 'r', R, RP)
for k in range(4):
    wander(d, f'b{k}', 0, 17.9, boxes([BP[k]], 6)[0], 920 + k, 1.8); wander(d, f'w{k}', 0, 17.9, boxes([WP[k]], 6)[0], 930 + k, 1.8)
for k in range(4): wander(d, f'r{k}', 0, 5.0, boxes([RP[k]], 5)[0], 940 + k, 1.4)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['w0', 'b1', 'w1', 'b2', 'w2'], 0.25)
d.mv('r2', t - 1.0, t + 0.2, rec(d, 'w2', t + 0.2)); tw = d.pas(b, t + 0.3, rec(d, 'r2', t + 0.5), 0.3)   # jagarna vinner bollen
d.mv('r2', tw, tw + 1.0, (34, 70)); d.carry(b, 'r2', tw, tw + 1.0)
for k, ps in zip((0, 1, 3), [(30, 34), (70, 40), (68, 66)]): d.mv(f'r{k}', 5.0, tw + 1.6, ps)
t = d.pas(b, tw + 1.1, rec(d, 'w3', tw + 1.8)); t = chain(d, b, t, ['r0', 'w0', 'r1', 'w1', 'r3'], 0.3)
for k, ps in zip(range(4), [(32, 30), (64, 34), (52, 62), (40, 50)]): d.mv(f'b{k}', tw + 0.6, tw + 2.4, ps)   # blått jagar nu
for k in range(4): wander(d, f'b{k}', tw + 2.4, 17.9, boxes([[(32, 30), (64, 34), (52, 62), (40, 50)][k]], 5)[0], 950 + k, 1.4)
fp = [(0, 'Två lag håller bollen mot det tredje', 'Blått och vitt spelar ihop mot rött.'),
      (tw - 0.3, 'Rött vinner bollen och ropar en färg', 'Rött ropar ”vitt”.'),
      (tw + 1.0, 'Vitt spelar nu med rött', 'Laget som inte ropas jagar.'),
      (tw + 2.8, 'Blått motpressar', 'Motpressa tills en färg har ropats.')]
finish(d, 'w16', 'trefargsrondo-4-plus-4-mot-4', ['Trefärgsrondo', '4 + 4 mot 4'], 'Ruta ca 25 × 25 m · Tre lag om fyra',
       fp, 'RONDO', [('box', 8, 12, 92, 92)], [lab(tw + 0.1, tw + 2.0, (34, 80), '”VITT!”')])

# ============ w17 Slutzonsspel ============
d = Drill()
BP = [(34, 62), (66, 62), (50, 70), (30, 44), (70, 44)]; RP = [(40, 52), (60, 52), (50, 36), (34, 28), (66, 28)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b2', 0))
t = chain(d, b, 0.4, ['b0', 'b3'], 0.3)
d.mv('b4', t - 1.6, t + 0.6, (66, 14)); d.mv('r4', t - 1.4, t + 0.6, (64, 22))          # försvararen får inte gå in i slutzonen
t = d.pas(b, t + 0.3, rec(d, 'b4', t + 1.3)); tp = t                                     # kontrollerad mottagning i slutzonen
hide(d, b, tp + 0.6)
for k in range(5): d.mv(f'b{k}', tp + 0.4, tp + 2.6, BP[k]); d.mv(f'r{k}', tp + 0.4, tp + 2.6, RP[k] if k != 2 else (50, 50))
show(d, b, tp + 2.7, rec(d, 'r2', tp + 2.7))                                             # ny start från mitten
t = chain(d, b, tp + 2.9, ['r1', 'r4'], 0.3)
d.mv('r3', t - 1.6, t + 0.6, (66, 86)); d.mv('b0', t - 1.4, t + 0.6, (62, 78))
t = d.pas(b, t + 0.3, rec(d, 'r3', t + 1.3)); tp2 = t
fp = [(0, 'Två lag mot varandra', 'Försvarare får inte gå in i slutzonerna.'),
      (tp - 1.2, 'Passa till en lagkamrat i slutzonen', 'Mottagningen ska vara kontrollerad.'),
      (tp + 0.4, 'Poäng – ny start från mitten', 'Nu startar rött.'),
      (tp2 - 1.0, 'Rött spelar in i slutzonen', 'Tajma löpningen så att du är spelbar.')]
finish(d, 'w17', 'slutzonsspel', ['Slutzonsspel', 'Positionsspel'], 'Plan ca 30 × 20 m · 3 m bred slutzon i varje ände',
       fp, 'POSITIONSSPEL', [('box', 18, 8, 82, 92), ('zone', 18, 8, 82, 18, (120, 170, 230), 'SLUTZON'), ('zone', 18, 82, 82, 92, (230, 120, 110), 'SLUTZON')],
       [lab(tp, tp + 1.8, (50, 24), '+1'), lab(tp2, tp2 + 1.8, (50, 76), '+1')])

# ============ w18 6 mot 3 genom konportar ============
d = Drill()
GT = [(50, 22), (22, 50), (78, 50), (50, 78)]
BP = [(36, 30), (64, 30), (30, 62), (70, 62), (50, 46), (50, 86)]; RP = [(44, 38), (58, 56), (38, 66)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b4', 0))
t = chain(d, b, 0.4, ['b0'], 0.3)
d.mv('b1', t - 0.6, t + 0.6, (50, 12)); t = d.pas(b, t + 0.2, rec(d, 'b1', t + 1.0)); tp1 = t   # passning genom porten
d.mv('b1', tp1, tp1 + 1.0, (62, 28)); d.carry(b, 'b1', tp1, tp1 + 1.0); t = tp1 + 1.0
t = d.pas(b, t + 0.2, rec(d, 'b3', t + 1.0))
d.mv('b3', t, t + 1.0, (88, 50)); d.carry(b, 'b3', t, t + 1.0); tp2 = t + 0.6; t += 1.0      # dribbling genom porten
t = d.pas(b, t + 0.2, rec(d, 'b5', t + 1.2))
d.mv('r2', t - 1.4, t + 0.2, rec(d, 'b5', t + 0.2)); tw = d.pas(b, t + 0.3, rec(d, 'r2', t + 0.5), 0.3)   # försvararna vinner
d.mv('r2', tw, tw + 1.2, (40, 72)); d.carry(b, 'r2', tw, tw + 1.2)
t = d.pas(b, tw + 1.3, rec(d, 'r1', tw + 2.0)); d.mv('r1', t, t + 1.4, (14, 50)); d.carry(b, 'r1', t, t + 1.4); tp3 = t + 1.0
for k in range(6): d.mv(f'b{k}', tw + 0.4, tw + 2.2, [(40, 40), (56, 40), (36, 58), (60, 60), (30, 46), (48, 70)][k])
fp = [(0, 'Sex anfallare mot tre försvarare', 'Fyra konportar på 2 m.'),
      (tp1 - 0.6, 'Passa genom en port: poäng', 'Mottagaren står på andra sidan.'),
      (tp2 - 0.6, 'Dribbla genom en port: poäng', 'Välj porten som är öppen.'),
      (tw - 0.2, 'Försvararna vinner – lagen byter roller', 'Nu anfaller rött portarna.'),
      (tp3 - 0.4, 'Flest portar efter tre minuter vinner', '')]
finish(d, 'w18', '6-mot-3-genom-konportar', ['6 mot 3', 'Genom konportar'], 'Ruta ca 30 × 30 m · Fyra konportar på 2 m',
       fp, 'RONDO', [('box', 8, 8, 92, 92)] + [('cone', x - 3, y) if y in (22, 78) else ('cone', x, y - 3) for x, y in GT] + [('cone', x + 3, y) if y in (22, 78) else ('cone', x, y + 3) for x, y in GT],
       [lab(tp1, tp1 + 1.6, (62, 14), '+1'), lab(tp2, tp2 + 1.6, (84, 40), '+1'), lab(tp3, tp3 + 1.6, (18, 40), '+1')])

# ============ w19 Jaktrondo 6 mot 2 med byten ============
d = Drill(); d.p('t', 'T', T_COL, (64, 92))
RP = [(34, 22), (66, 22), (78, 46), (66, 70), (34, 70), (22, 46)]
team(d, 'b', B, RP); team(d, 'r', R, [(46, 88), (52, 88)], ['1', '1']); team(d, 'o', ORA, [(46, 94), (52, 94)], ['2', '2'])
b = d.newball(rec(d, 't', 0))
t = d.pas(b, 0.4, rec(d, 'b4', 1.2))
d.mv('r0', 0.4, 2.0, (44, 52)); d.mv('r1', 0.4, 2.0, (56, 40)); d.mv('o0', 0.8, 1.6, (46, 88)); d.mv('o1', 0.8, 1.6, (52, 88))
t = chain(d, b, t, ['b5', 'b0', 'b1'], 0.25)
d.mv('r1', t - 1.0, t + 0.2, rec(d, 'b1', t + 0.2)); d.mv('r0', t - 1.0, t + 0.2, (50, 34)); tw = d.pas(b, t + 0.3, rec(d, 'r1', t + 0.5), 0.3)   # paret vinner en boll
t = d.pas(b, tw + 0.4, rec(d, 't', tw + 1.5))
t = d.pas(b, t + 0.4, rec(d, 'b3', t + 1.2)); tsw = t - 1.0
d.mv('r0', tsw, tsw + 1.6, (40, 94)); d.mv('r1', tsw, tsw + 1.6, (58, 94))                     # tio sekunder: nästa par
d.mv('o0', tsw, tsw + 1.6, (42, 56)); d.mv('o1', tsw, tsw + 1.6, (60, 52))
t = chain(d, b, t, ['b2', 'b1', 'b0', 'b5'], 0.25)
fp = [(0, 'Tränaren spelar in', 'Sex håller bollen. Jagarna står parvis vid startkonen.'),
      (0.6, 'Ett par springer in och jagar', 'I tio sekunder.'),
      (tw - 0.2, 'Paret vinner en boll', 'Tränaren spelar in en ny.'),
      (tsw, 'Tio sekunder – nästa par', 'Paret som vinner flest bollar vinner.')]
finish(d, 'w19', 'jaktrondo-6-mot-2-med-byten', ['Jaktrondo 6 mot 2', 'Med byten'], 'Ruta ca 12 × 12 m · Startkon 10 m utanför',
       fp, 'RONDO', [('box', 16, 14, 84, 78), ('cone', 49, 84)], [lab(tw, tw + 1.6, (50, 8), '+1 PAR 1')])

# ============ w20 3 mot 1 i ruta ============
d = Drill()
def corners(x0): return [(x0, 36), (x0 + 28, 36), (x0 + 28, 64), (x0, 64)]
cnt0 = []
for k, x0 in enumerate((12, 60)):
    CR = corners(x0); occ = {0: f'a{k}', 1: f'c{k}', 3: f'e{k}'}
    for ci, pid in occ.items(): d.p(pid, '', B, CR[ci])
    d.p(f'm{k}', '', R, (x0 + 14, 50))
    b = d.newball(rec(d, occ[0], 0)); h = 0; t = 0.4 + 0.4 * k
    order = [1, 2, 3, 0, 1, 2, 3, 2, 1] if k == 0 else [3, 2, 1, 2, 3, 0, 1, 0, 3]
    for n, q in enumerate(order[:7]):
        # mottagaren q är granne till h; den som inte är med flyttar till det tomma hörnet
        others = [c for c in occ if c not in (h, q)]; free = [c for c in range(4) if c not in occ][0]
        mover = others[0]
        t2 = d.pas(b, t + 0.25, rec(d, occ[q], t + 0.85))
        d.mv(occ[mover], t + 0.3, t + 1.3, CR[free]); occ[free] = occ.pop(mover)
        d.mv(f'm{k}', t, t + 0.9, ((CR[q][0] + x0 + 14) / 2, (CR[q][1] + 50) / 2))
        h = q; t = t2
        if k == 0: cnt0.append(t2)
    if k == 0:
        nxt = [c for c in occ if c != h and abs(c - h) % 2 == 1][0]
        d.mv('m0', t - 0.2, t + 0.5, rec(d, occ[nxt], t + 0.6)); tw = d.pas(b, t + 0.3, rec(d, 'm0', t + 0.7), 0.4)
        loser = occ[h]; d.mv(loser, tw + 0.3, tw + 1.4, (x0 + 14, 50)); d.mv('m0', tw + 0.3, tw + 1.4, CR[h])   # den som tappar går in
        t = d.pas(b, tw + 1.5, rec(d, occ[nxt], tw + 2.1))
fp = [(0, 'Tre håller bollen mot en', 'Flera rutor bredvid varandra.'),
      (cnt0[0], 'Passa förbi mittspelaren', 'Spelaren utan boll flyttar till det lediga hörnet.'),
      (cnt0[3], 'Alltid spelbar', 'Två passningsvägar till den med boll.'),
      (cnt0[-1] + 0.3, 'Den som tappar bollen går in', 'Spelet fortsätter direkt.')]
finish(d, 'w20', '3-mot-1-i-ruta', ['3 mot 1', 'I ruta'], 'Ruta ca 7 × 7 m · Tre runt kanten och en inne · Flera rutor',
       fp, 'RONDO', [('box', 8, 32, 44, 68), ('box', 56, 32, 92, 68)])

# ============ w27 Kombinationsavslut i rotation ============
d = Drill(); d.p('mv1', 'MV', R, (50, 4)); d.p('mv2', 'MV', R, (50, 96))
d.p('s1', '1', B, (12, 88)); d.p('s2', '2', B, (46, 54)); d.p('s3', '3', B, (6, 50))
d.p('u1', '1', B, (88, 12)); d.p('u2', '2', B, (54, 46)); d.p('u3', '3', B, (94, 50))
b = d.newball(rec(d, 's1', 0)); b2 = d.newball(rec(d, 'u1', 0))
d.mv('s2', 0.3, 1.1, (38, 66)); t = d.pas(b, 0.5, rec(d, 's2', 1.1))                     # 2 kommer mot
t = d.pas(b, t + 0.15, rec(d, 's1', t + 0.7)); tl = t                                    # lägger tillbaka
t = d.pas(b, t + 0.25, rec(d, 's3', t + 1.0))                                            # 1 slår till 3
d.path('s2', tl, [(30, 60), (22, 56), (20, 46), (22, 36)], 1.4)                           # 2 rundar flaggan
t = d.pas(b, t + 0.6, rec(d, 's2', t + 1.2)); t = shoot(d, b, t + 0.05, (44, 1)); tg = t   # direktavslut
d.mv('s1', tl + 0.4, tg + 0.8, (44, 56)); d.mv('s3', tg - 0.4, tg + 1.0, (12, 88)); d.mv('s2', tg, tg + 1.6, (8, 52))
# samma mönster åt andra hållet
t0 = tg - 0.2
d.mv('u2', t0, t0 + 0.8, (62, 34)); t = d.pas(b2, t0 + 0.2, rec(d, 'u2', t0 + 0.8))
t = d.pas(b2, t + 0.15, rec(d, 'u1', t + 0.7)); tl2 = t
t = d.pas(b2, t + 0.25, rec(d, 'u3', t + 1.0))
d.path('u2', tl2, [(70, 40), (78, 44), (80, 54), (78, 64)], 1.4)
t = d.pas(b2, t + 0.6, rec(d, 'u2', t + 1.2)); t = shoot(d, b2, t + 0.05, (56, 99)); tg2 = t
d.mv('u1', tl2 + 0.4, tg2 + 0.8, (56, 44)); d.mv('u3', tg2 - 0.4, tg2 + 1.0, (88, 12))
fp = [(0, '1 spelar till 2, som lägger tillbaka', '2 kommer mot bollen från mittflaggan.'),
      (tl - 0.1, '1 slår till 3 vid konen', '2 rundar flaggan.'),
      (tg - 1.0, '3 lägger av – 2 avslutar direkt', 'Alla roterar ett steg.'),
      (t0 + 0.4, 'Samma mönster åt andra hållet', 'Mot det andra målet.')]
finish(d, 'w27', 'kombinationsavslut-i-rotation', ['Kombinationsavslut', 'I rotation'], 'Två mål med målvakter ca 30 m isär · Tre flaggor i mitten · Kon utanför ytterflaggorna',
       fp, 'AVSLUT', [('pole', 22, 50), ('pole', 50, 50), ('pole', 78, 50), ('cone', 4, 56), ('cone', 96, 44)])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ w28 Inlägg och avslut 4 mot 3 ============
d = Drill(); d.p('mv', 'MV', R, (50, 5)); d.p('t', 'T', T_COL, (50, 82))
PO = {1: (10, 22), 2: (90, 22), 3: (10, 44), 4: (90, 44)}
for n, ps in PO.items(): d.p(f'i{n}', 'I', WHITE, (ps[0] + (3 if n % 2 else -3), ps[1] + 4))
AP = [(30, 56), (44, 60), (58, 58), (72, 54)]; DP = [(38, 24), (50, 20), (62, 24)]
team(d, 'a', B, AP); team(d, 'd', R, DP)
b2 = d.newball(rec(d, 'i2', 0)); b1 = d.newball(rec(d, 'i3', 0))
tcall = 0.4
t = d.pas(b2, 1.4, (52, 14), 1.1); tc = 1.4                                              # inlägg från käpp 2
for k, ps in enumerate([(40, 22), (54, 16), (62, 30), (70, 38)]): d.mv(f'a{k}', 0.8, 2.4, ps)
for k, ps in enumerate([(42, 20), (50, 14), (60, 22)]): d.mv(f'd{k}', 1.2, 2.4, ps)
d.mv('a1', 2.4, 2.5, (54, 17)); t = d.pas(b2, t, rec(d, 'a1', 2.5), 0.1); t = shoot(d, b2, t, (44, 1)); tg = t
for k in range(4): d.mv(f'a{k}', tg + 0.2, tg + 2.2, AP[k])
for k in range(3): d.mv(f'd{k}', tg + 0.2, tg + 2.2, DP[k])
tcall2 = tg + 2.0
t = d.pas(b1, tcall2 + 1.0, (46, 20), 1.1)                                              # inlägg från käpp 3
for k, ps in enumerate([(34, 30), (46, 22), (56, 16), (66, 34)]): d.mv(f'a{k}', tcall2 + 0.4, tcall2 + 2.0, ps)
for k, ps in enumerate([(38, 26), (48, 18), (58, 20)]): d.mv(f'd{k}', tcall2 + 0.8, tcall2 + 2.0, ps)
d.mv('a1', tcall2 + 2.0, tcall2 + 2.2, (46, 21)); t = d.pas(b1, t, rec(d, 'a1', t + 0.1), 0.1); t = shoot(d, b1, t, (56, 1)); tg2 = t
fp = [(0, 'Tränaren ropar ett nummer', 'Inläggaren vid den käppen slår in.'),
      (tc, 'Anfallarna löper in i boxen', 'Fyra anfallare mot tre försvarare.'),
      (tg - 0.3, 'Avslut', 'Försök göra mål på inlägget.'),
      (tcall2 - 0.3, 'Nytt nummer', 'Byt försvarare efter tre omgångar.')]
finish(d, 'w28', 'inlagg-och-avslut-4-mot-3', ['Inlägg och avslut', '4 mot 3'], 'Zon framför mål med målvakt · Numrerade käppar med bollar runt straffområdet',
       fp, 'AVSLUT', [('pole', x, y) for x, y in PO.values()] + [('text', x, y + 6, str(n)) for n, (x, y) in PO.items()],
       [lab(tcall, tcall + 1.4, (50, 74), '”2!”'), lab(tcall2, tcall2 + 1.4, (50, 74), '”3!”')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

if __name__ == '__main__': render(C, sys.argv)
