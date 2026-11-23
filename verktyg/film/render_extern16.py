# Externa övningar, omgång 16 (tolv st). Regel: först d.mv, sedan d.carry; först mottagarens rörelse, sedan passningen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e9', __file__.replace('render_extern16.py', 'render_extern9.py'))
e9 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e9); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e9.finish, e9.rec, e9.chain, e9.wander, e9.counter, e9.arrivals
lab, hide, show, team, boxes, drive, shoot = e9.lab, e9.hide, e9.show, e9.team, e9.boxes, e9.drive, e9.shoot
factor, swap_color, stand, countdown, countup, win = e9.factor, e9.swap_color, e9.stand, e9.countdown, e9.countup, e9.win
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'

# ============ fi01 Passa genom mål ============
d = Drill(); YS = [24, 50, 76]; cnt = []
for k, y in enumerate(YS): d.p(f'l{k}', '', B, (26, y)); d.p(f'r{k}', '', B, (74, y))
balls = [d.newball(rec(d, f'l{k}', 0)) for k in range(3)]
for k, y in enumerate(YS):
    t = 0.4 + 0.3 * k; a, c = f'l{k}', f'r{k}'
    for rep in range(8):
        direct = rep >= 4
        t = d.pas(balls[k], t, rec(d, c, t + 0.9))
        if k == 0: cnt.append(t)
        if not direct: d.carry(balls[k], c, t, t + 0.4); t += 0.4                                  # ta emot och passa
        a, c = c, a; t += 0.1
fp = [(0, 'Passa genom målet', 'Ett litet konmål mellan paret.'),
      (cnt[1], 'Ta emot och passa', ''),
      (cnt[4] - 0.2, 'Eller passa direkt', ''),
      (cnt[6], 'Flest passningar på tid', 'Tävla mot de andra paren.')]
finish(d, 'fi01', 'passa-genom-mal', ['Passa', 'Genom mål'], 'Par med ett litet konmål mellan sig',
       fp, 'PASSNINGSÖVNING', [('cone', 50, y + dy) for y in YS for dy in (-4, 4)], counter(cnt, pos=(50, 10), last=None))

# ============ fi02 Slalomdribbling ============
d = Drill(); LX = [32, 68]
CN = {x: [(x, 76 - 9 * i) for i in range(7)] for x in LX}
for li, x in enumerate(LX):
    for k in range(3): d.p(f'p{li}{k}', '', B, (x - 4 + 4 * k, 90))
balls = {}
for li, x in enumerate(LX):
    for k in range(3): balls[(li, k)] = d.newball(rec(d, f'p{li}{k}', 0))
for li, x in enumerate(LX):
    t = 0.4 + 0.4 * li
    for k in range(2):
        pid = f'p{li}{k}'; b = balls[(li, k)]
        d.carry(b, pid, 0, t)
        fwd = [(x + (4 if i % 2 == 0 else -4), y) for i, (cx, y) in enumerate(CN[x])] + [(x, 14)]
        back = [(x + (-4 if i % 2 == 0 else 4), y) for i, (cx, y) in list(enumerate(CN[x]))[::-1]] + [(x + 11, 98 - 7 * k)]
        t2 = d.path(pid, t, [(x, 84)] + fwd, 1.5); t3 = d.path(pid, t2, back, 1.5); d.carry(b, pid, t, t3)
        t = t2 - 0.6
fp = [(0, 'Driv genom slalombanan', 'Koner ca 1 m isär.'),
      (1.4, 'Höger fot på vägen fram', ''),
      (5.0, 'Vänster fot tillbaka', ''),
      (9.0, 'Variant: bara utsidan – eller ta tid', '')]
finish(d, 'fi02', 'slalomdribbling', ['Slalom-', 'dribbling'], 'Slalombana med koner ca 1 m isär',
       fp, 'TEKNIK', [('cone',) + c for x in LX for c in CN[x]])

# ============ fi03 Driva och passa i fyrkant ============
d = Drill()
SQ = [(24, 76), (24, 24), (76, 24), (76, 76)]
d.p('p1', '1', B, (20, 82)); d.p('p2', '2', B, (80, 18)); d.p('p3', '3', B, (20, 82)) if False else d.p('p3', '3', B, (82, 82))
b = d.newball(rec(d, 'p1', 0))
holder, t = 'p1', 0.4
plan = [('p1', [(18, 50), (20, 20), (28, 18)], 'p2'), ('p2', [(82, 30), (82, 50), (82, 70)], 'p3'), ('p3', [(70, 82), (50, 82), (30, 82)], 'p1')]
d.mv('p1', 0.2, 0.4, (20, 82))
waits = {'p2': (76, 14), 'p3': (86, 80), 'p1': (16, 86)}
marks = []
for runner, pts, nxt in plan * 2:
    t2 = d.path(runner, t, pts, 1.3); d.carry(b, runner, t, t2)                                   # driv runt konen
    t3 = d.pas(b, t2 + 0.1, rec(d, nxt, t2 + 0.9)); marks.append(t3)
    d.mv(runner, t3, t3 + 3.2, waits[runner])
    t = t3 + 0.1
fp = [(0, 'Spelare 1 driver runt konerna', 'Fyrkant med koner.'),
      (marks[0] - 0.6, 'Passa till spelare 2', 'När du har rundat första konen.'),
      (marks[1] - 0.6, 'Spelare 2 driver vidare – pass till 3', ''),
      (marks[3], 'Variant: bara drivning runt fyrkanten', 'Framåt eller bakåt.')]
finish(d, 'fi03', 'driva-och-passa-i-fyrkant', ['Driva och passa', 'I fyrkant'], 'Fyrkant med koner',
       fp, 'TEKNIK', [('cone',) + c for c in SQ])

# ============ fi04 Teknikkvadrat ============
d = Drill()
SQ = [(20, 80), (20, 20), (80, 20), (80, 80)]
TASK = ['SLALOM', 'STOPP VID KON', 'BACKA', 'FINTER']
for k in range(4): d.p(f'p{k}', '', B, SQ[k])
balls = [d.newball(rec(d, f'p{k}', 0)) for k in range(4)]
def side_path(s, k):
    (x0, y0), (x1, y1) = SQ[s], SQ[(s + 1) % 4]
    if s == 0: return [(x0 + (3 if i % 2 else -3), y0 + (y1 - y0) * i / 5) for i in range(1, 6)]     # slalom
    if s == 1: return [((x0 + x1) / 2, y0), ((x0 + x1) / 2 + 0.1, y0), (x1, y1)]                      # stopp vid kon
    if s == 2: return [(x0, (y0 + y1) / 2), (x1, y1)]                                                 # backa
    px, py = (-(y1 - y0) / 60 * 4, (x1 - x0) / 60 * 4)                                              # finter: sidled
    return [(x0 + (x1 - x0) / 3 + px, y0 + (y1 - y0) / 3 + py), (x0 + 2 * (x1 - x0) / 3 - px, y0 + 2 * (y1 - y0) / 3 - py), (x1, y1)]
for k in range(4):
    t = 0.4; s = k
    for lap in range(4):
        t2 = d.path(f'p{k}', t, side_path(s, k), 1.0); d.carry(balls[k], f'p{k}', t, t2)
        if s == 1: stand(d, f'p{k}', t2, t2 + 0.6); d.carry(balls[k], f'p{k}', t2, t2 + 0.6); t2 += 0.6
        t = t2; s = (s + 1) % 4
fp = [(0, 'En teknikuppgift per sida', 'Kvadrat ca 8–10 m.'),
      (1.6, 'Slalom – stopp vid kon', ''),
      (5.0, 'Backa med bollen – finter', ''),
      (9.0, 'Gå runt och gör alla uppgifter', '')]
finish(d, 'fi04', 'teknikkvadrat', ['Teknik-', 'kvadrat'], 'Kvadrat ca 8–10 m · En uppgift per sida',
       fp, 'TEKNIK', [('cone',) + c for c in SQ] + [('cone', 20, 50), ('cone', 50, 20), ('text', 8, 50, 'SLALOM'), ('text', 50, 12, 'STOPP'), ('text', 92, 50, 'BACKA'), ('text', 50, 90, 'FINTER')])

# ============ fi05 Skott på liggande och rullande boll ============
d = Drill()
XS = [26, 38, 50, 62, 74]
for k, x in enumerate(XS): d.p(f'p{k}', '', B, (x, 54))
balls = [d.newball((x + 1.8, 48)) for x in XS]
t = 0.4; shots = []
for k in range(5):
    d.mv(f'p{k}', t, t + 0.5, (XS[k], 50)); tg = d.pas(balls[k], t + 0.5, (44 + 3 * k, 1), 0.8); shots.append(tg)   # liggande boll
    hide(d, balls[k], tg + 0.3); d.mv(f'p{k}', tg, tg + 0.6, (XS[k], 54)); t += 0.9
b2 = [d.newball((200, 200)) for _ in range(3)]
for j, k in enumerate((0, 2, 4)):
    show(d, b2[j], t, rec(d, f'p{k}', t)); t1 = d.pas(b2[j], t + 0.2, (XS[k] + 1, 40), 0.6)                     # spela fram bollen
    d.mv(f'p{k}', t + 0.2, t1 + 0.1, (XS[k] - 1, 41)); tg = d.pas(b2[j], t1 + 0.15, (46 + 2 * j, 1), 0.7)    # skjut när den rullar
    hide(d, b2[j], tg + 0.3); d.mv(f'p{k}', tg, tg + 1.0, (XS[k], 54)); t = tg - 0.2
fp = [(0, 'Alla lägger bollen på samma linje', 'Och skjuter efter varandra.'),
      (shots[2], 'Skott på liggande boll', ''),
      (shots[4] + 0.6, 'Spela fram bollen – skjut när den rullar', ''),
      (t - 0.6, 'Anpassa avståndet', 'Efter hur långt barnen kan skjuta.')]
finish(d, 'fi05', 'skott-pa-liggande-och-rullande-boll', ['Skott på liggande', 'och rullande boll'], 'Mål · En linje med bollar',
       fp, 'AVSLUT', [('line', [(18, 48), (82, 48)])])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ fi06 3 mot 3 – räkna passningar ============
d = Drill()
BP = [(26, 30), (72, 34), (40, 70)]; RP = [(44, 44), (60, 56), (30, 54)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
for k in range(3): wander(d, f'b{k}', 0, 17.9, boxes([BP[k]], 7)[0], 3100 + k, 1.6)
for k in range(3): wander(d, f'r{k}', 0, 7.4, boxes([RP[k]], 6)[0], 3110 + k, 1.6)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b1', 'b2', 'b0', 'b1', 'b2'], 0.4); cnt = arrivals(d, b)[:5]
tw = win(d, b, 'r0', 'b2', t + 0.4)
for k in range(3): wander(d, f'r{k}', tw + 0.4, 17.9, boxes([RP[k]], 8)[0], 3120 + k, 1.6)
t = chain(d, b, tw + 0.4, ['r1', 'r2', 'r0'], 0.4); cnt2 = arrivals(d, b)[-3:]
fp = [(0, 'Tre mot tre utan mål', 'Max fyra mot fyra.'),
      (cnt[1], 'Räkna passningarna', 'Totalt eller flest i rad.'),
      (tw - 0.2, 'Brytning – räkningen börjar om', ''),
      (tw + 0.6, 'Nu räknar rött', '')]
finish(d, 'fi06', '3-mot-3-rakna-passningar', ['3 mot 3', 'Räkna passningar'], 'Liten yta · Tre mot tre',
       fp, 'SMÅLAGSSPEL', [('box', 12, 14, 88, 86)], counter(cnt, pos=(26, 8), last=None) + counter(cnt2, pos=(74, 8), last=None))

# ============ fi07 Parboll ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96))
PB = [(34, 66), (62, 60)]; PR = [(38, 36), (64, 40)]
for k, ps in enumerate(PB): d.p(f'b{k}', '', B, ps); d.p(f'b{k}x', '', B, (ps[0] + 4, ps[1] + 1))
for k, ps in enumerate(PR): d.p(f'r{k}', '', R, ps); d.p(f'r{k}x', '', R, (ps[0] + 4, ps[1] + 1))
b = d.newball(rec(d, 'b0', 0))
def pairmv(pid, t0, t1, to): d.mv(pid, t0, t1, to); d.mv(pid + 'x', t0, t1, (to[0] + 4, to[1] + 1))   # håller varandra i handen
pairmv('b0', 0.4, 2.2, (36, 52)); d.carry(b, 'b0', 0.4, 2.2); pairmv('b1', 0.4, 2.2, (60, 40)); pairmv('r0', 0.6, 2.2, (40, 44)); pairmv('r1', 0.6, 2.4, (64, 30))
t = d.pas(b, 2.4, rec(d, 'b1', 3.2)); pairmv('b1', t, t + 1.4, (56, 22)); d.carry(b, 'b1', t, t + 1.4); t += 1.4
pairmv('r1', t - 1.2, t, (60, 18)); tg = shoot(d, b, t + 0.1, (46, 1)); hide(d, b, tg + 0.4)
for k, ps in enumerate(PB): pairmv(f'b{k}', tg + 0.2, tg + 2.4, ps)
for k, ps in enumerate(PR): pairmv(f'r{k}', tg + 0.2, tg + 2.4, ps)
b2 = d.newball((200, 200)); show(d, b2, tg + 2.5, rec(d, 'mvr', tg + 2.5))
t = d.pas(b2, tg + 2.7, rec(d, 'r0x', tg + 3.6)); pairmv('r0', t, t + 1.6, (40, 64)); d.carry(b2, 'r0x', t, t + 1.6)
fp = [(0, 'Spelarna håller varandra i händerna', 'Två och två hela spelet.'),
      (2.4, 'Samarbeta i paret', 'Spring åt samma håll.'),
      (tg - 0.4, 'Mål', 'Vanligt spel i övrigt.'),
      (tg + 2.5, 'Nytt anfall', '')]
finish(d, 'fi07', 'parboll', ['Parboll', 'Lek och reaktion'], 'Två lag och två mål · Spelarna i par',
       fp, 'LEK', [])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ fi08 Expressboll ============
d = Drill()
BP = [(22, 76), (42, 80), (62, 76), (80, 82)]; RP = [(20, 22), (40, 18), (60, 24), (80, 18)]
team(d, 'b', B, BP, [''] * 4); team(d, 'r', R, RP, [''] * 4)
bb = [d.newball(rec(d, f'b{k}', 0)) for k in range(4)]; rb = [d.newball(rec(d, f'r{k}', 0)) for k in range(4)]
ex = []
for k in range(4):
    t = 0.4 + 0.5 * k
    d.mv(f'b{k}', t, t + 0.6, (BP[k][0], 70)); t1 = d.pas(bb[k], t + 0.6, (BP[k][0] + 6 - 3 * k, 22 + 4 * k), 1.2)   # över till motståndarnas sida
    d.mv(f'r{k}', t + 0.2, t + 0.8, (RP[k][0], 30)); t2 = d.pas(rb[k], t + 0.8, (RP[k][0] - 4 + 2 * k, 74 + 3 * k), 1.2)
    # hämta och skicka tillbaka
    d.mv(f'r{k}', t1 - 0.6, t1 + 0.1, (BP[k][0] + 6 - 3 * k - 2, 22 + 4 * k + 1)); d.carry(bb[k], f'r{k}', t1 + 1.0, t1 + 1.8); d.mv(f'r{k}', t1 + 1.0, t1 + 1.8, (RP[k][0], 30))
    t3 = d.pas(bb[k], t1 + 2.0, (BP[k][0], 66 + 3 * k), 1.2)
    d.mv(f'b{k}', t2 - 0.6, t2 + 0.1, (RP[k][0] - 4 + 2 * k - 2, 74 + 3 * k + 1)); d.carry(rb[k], f'b{k}', t2 + 1.0, t2 + 1.8); d.mv(f'b{k}', t2 + 1.0, t2 + 1.8, (BP[k][0], 70))
    t4 = d.pas(rb[k], t2 + 2.0, (RP[k][0], 34 - 3 * k), 1.2)
    d.mv(f'b{k}', t2 + 2.1, t3, (BP[k][0] - 2, 67 + 3 * k)); d.carry(bb[k], f'b{k}', t3, t3 + 0.6)
    d.mv(f'r{k}', t1 + 2.1, t4, (RP[k][0] - 2, 35 - 3 * k)); d.carry(rb[k], f'r{k}', t4, t4 + 0.6)
fp = [(0, 'Alla har varsin boll', 'Två planhalvor.'),
      (1.0, 'Spela bollen över till motståndarna', 'Men bara bakom egen linje.'),
      (4.0, 'Hämta bollar i hela egna halvan', 'Och skicka iväg dem direkt.'),
      (9.0, 'Minst bollar kvar när tiden går ut vinner', '')]
finish(d, 'fi08', 'expressboll', ['Expressboll', 'Lek och reaktion'], 'Två planhalvor · Alla har varsin boll',
       fp, 'LEK', [('box', 10, 10, 90, 90), ('line', [(10, 50), (90, 50)]), ('line', [(10, 70), (90, 70)]), ('line', [(10, 30), (90, 30)])])

# ============ fi09 Prickboll ============
d = Drill()
BP = [(24, 82), (42, 84), (58, 84), (76, 82)]; RP = [(24, 18), (42, 16), (58, 16), (76, 18)]
team(d, 'b', B, BP, [''] * 4); team(d, 'r', R, RP, [''] * 4)
pb = d.newball((50, 50)); bb = [d.newball(rec(d, f'b{k}', 0)) for k in range(4)]; rb = [d.newball(rec(d, f'r{k}', 0)) for k in range(4)]
t = 0.6; hits = []
for k in (1, 2):
    d.mv(f'b{k}', t, t + 0.4, (BP[k][0], 72)); t1 = d.pas(bb[k], t + 0.4, (50, 52), 0.8); hits.append(t1)     # träffa prickbollen
    t2 = d.pas(pb, t1, (50 + 2 * k - 3, 44 - 6 * (k - 1)), 0.7); tb_ = d.pas(bb[k], t1, (40 + 20 * (k - 1), 60), 0.6); hide(d, bb[k], tb_ + 0.2); t = t1 + 0.3
d.mv('r1', t, t + 0.4, (RP[1][0], 28)); t1 = d.pas(rb[1], t + 0.4, (49, 40), 0.7); hits.append(t1)
d.pas(pb, t1, (48, 50), 0.6); tb_ = d.pas(rb[1], t1, (30, 46), 0.6); hide(d, rb[1], tb_ + 0.2); t = t1 + 0.4
d.mv('b3', t, t + 0.4, (BP[3][0], 72)); t1 = d.pas(bb[3], t + 0.4, (49, 52), 0.8); hits.append(t1)
tp = d.pas(pb, t1, (52, 26), 1.4); tb_ = d.pas(bb[3], t1, (64, 62), 0.6); hide(d, bb[3], tb_ + 0.2)                                           # över motståndarnas linje
hide(d, pb, tp + 0.2); show(d, pb, tp + 1.8, (50, 50))
fp = [(0, 'Alla har en boll – prickbollen i mitten', 'Skjut bara bakom egen linje.'),
      (hits[0] - 0.3, 'Träffa prickbollen', 'Få den att rulla mot motståndarnas linje.'),
      (tp - 0.6, 'Över linjen: poäng', ''),
      (tp + 1.8, 'Ny start från mitten', 'Hämta bollar i ert område.')]
finish(d, 'fi09', 'prickboll', ['Prickboll', 'Lek och reaktion'], 'Mittpunkt och två linjer · Alla har en boll',
       fp, 'LEK', [('line', [(8, 70), (92, 70)]), ('line', [(8, 30), (92, 30)]), ('text', 64, 50, 'PRICKBOLL')], [lab(tp, tp + 1.6, (52, 20), '+1')])

# ============ fi10 Konskog ============
d = Drill(); d.p('t', 'T', T_COL, (50, 95))
CN = [(20 + 15 * i + (7 if j % 2 else 0), 20 + 14 * j) for j in range(5) for i in range(5) if 20 + 15 * i + (7 if j % 2 else 0) < 86]
ST = [(28, 26), (50, 30), (72, 24), (30, 56), (58, 50), (74, 62), (40, 76), (66, 80)]
balls = []
for k, ps in enumerate(ST): d.p(f'p{k}', '', B, ps); balls.append(d.newball(rec(d, f'p{k}', 0)))
used = set()
for k in range(8):
    pid = f'p{k}'; wander(d, pid, 0, 8.4, boxes([ST[k]], 8)[0], 3200 + k, 1.4)
    cx = min((c for c in CN if c not in used), key=lambda c: (c[0] - at(d.pl[pid]['tr'], 8.4)[0]) ** 2 + (c[1] - at(d.pl[pid]['tr'], 8.4)[1]) ** 2); used.add(cx)
    d.mv(pid, 8.6, 9.8, (cx[0] + 3, cx[1] + 2)); stand(d, pid, 9.8, 12.0); wander(d, pid, 12.0, 17.9, boxes([ST[k]], 8)[0], 3220 + k, 1.4)
    d.carry(balls[k], pid, 0, 17.9)
fp = [(0, 'Dribbla runt så många koner som möjligt', 'Utan att röra dem.'),
      (4.0, 'Byt riktning runt konerna', 'Bollen nära foten.'),
      (8.6, 'Signal: stanna vid en kon', ''),
      (12.0, 'Vidare – eller ”Hela havet stormar”', '')]
finish(d, 'fi10', 'konskog', ['Konskog', 'Teknik'], 'Många koner utspridda · Alla har en boll',
       fp, 'TEKNIK', [('cone',) + c for c in CN], [lab(8.6, 11.6, (50, 8), 'STOPP VID EN KON')])

# ============ fi11 Täcka bollen ============
d = Drill()
ST = [(32, 30), (64, 28), (26, 56), (74, 54), (36, 74), (64, 74), (50, 46)]
balls = []
for k, ps in enumerate(ST): d.p(f'p{k}', '', B, ps); balls.append(d.newball(rec(d, f'p{k}', 0)))
for k in (0, 2, 3, 4, 5): wander(d, f'p{k}', 0, 17.9, boxes([ST[k]], 6)[0], 3300 + k, 1.6); d.carry(balls[k], f'p{k}', 0, 17.9)
d.mv('p6', 0.3, 2.6, (58, 34)); d.carry(balls[6], 'p6', 0, 2.6); wander(d, 'p1', 0, 2.4, boxes([ST[1]], 5)[0], 3311, 1.6); d.carry(balls[1], 'p1', 0, 2.6)
t1 = d.pas(balls[1], 2.8, (80, 6), 0.8)                                                                      # utsparkad
d.mv('p1', 2.9, 4.2, (80, 8)); stand(d, 'p1', 4.2, 4.6); d.mv('p1', 4.6, 6.2, (64, 28)); d.carry(balls[1], 'p1', 4.2, 6.2)   # hämta och hoppa in
wander(d, 'p1', 6.2, 17.9, boxes([ST[1]], 6)[0], 3312, 1.6); d.carry(balls[1], 'p1', 6.2, 17.9)
wander(d, 'p6', 2.6, 17.9, (44, 40, 56, 52), 3316, 1.6); d.carry(balls[6], 'p6', 2.6, 17.9)
fp = [(0, 'Driv och täck din boll', 'Begränsat område, alla har en boll.'),
      (2.2, 'Sparka ut kompisarnas bollar', ''),
      (4.2, 'Hämta bollen och hoppa in igen', ''),
      (9.0, 'Variant i par', 'En täcker med armar och kropp, en försöker ta bollen.')]
finish(d, 'fi11', 'tacka-bollen', ['Täcka bollen', 'Teknik'], 'Begränsat område · Alla har en boll',
       fp, 'TEKNIK', [('box', 16, 16, 84, 84)])

# ============ fi12 Tunneldatten ============
d = Drill(); d.p('k', 'D', R, (50, 50))
ST = [(24, 26), (50, 22), (76, 26), (24, 74), (50, 78), (76, 74)]
balls = []
for k, ps in enumerate(ST): d.p(f'p{k}', '', B, ps); balls.append(d.newball(rec(d, f'p{k}', 0)))
for k in (1, 2, 4, 5): wander(d, f'p{k}', 0, 17.9, boxes([ST[k]], 7)[0], 3400 + k, 1.6); d.carry(balls[k], f'p{k}', 0, 17.9)
d.mv('p3', 0, 2.6, (28, 56)); d.carry(balls[3], 'p3', 0, 2.6); d.mv('k', 0.2, 2.6, (33, 56)); td = 2.6        # dattad
hide(d, balls[3], td + 0.1); stand(d, 'p3', td, 6.4)
d.mv('p0', 0, 3.4, (20, 46)); d.carry(balls[0], 'p0', 0, 3.4)
t1 = d.pas(balls[0], 3.6, (28, 56), 0.5); t2 = d.pas(balls[0], t1, (34, 64), 0.5); d.mv('p0', 3.6, t2, (32, 64)); tr = t1   # genom tunneln
d.carry(balls[0], 'p0', t2, t2 + 1.4); d.mv('p0', t2, t2 + 1.4, (24, 40)); wander(d, 'p0', t2 + 1.4, 17.9, boxes([ST[0]], 7)[0], 3410, 1.6); d.carry(balls[0], 'p0', t2 + 1.4, 17.9)
show(d, balls[3], 6.4, rec(d, 'p3', 6.4)); wander(d, 'p3', 6.4, 17.9, boxes([ST[3]], 7)[0], 3413, 1.6); d.carry(balls[3], 'p3', 6.4, 17.9)
d.mv('k', 3.0, 6.0, (60, 40)); wander(d, 'k', 6.0, 17.9, (40, 38, 60, 62), 3420, 1.6)
fp = [(0, 'Vanlig datt – alla har en boll', ''),
      (td, 'Dattad: bollen över huvudet, stå bredbent', ''),
      (tr - 0.4, 'Rädda genom att dribbla genom tunneln', ''),
      (6.6, 'Fri igen', 'För de minsta går dattarna bara.')]
finish(d, 'fi12', 'tunneldatten', ['Tunneldatten', 'Lek och reaktion'], 'Begränsat område · Alla har en boll',
       fp, 'LEK', [('box', 12, 12, 88, 88)], [lab(td, tr, (28, 46), 'BOLLEN ÖVER HUVUDET'), lab(tr, tr + 1.6, (28, 46), 'FRI')])

if __name__ == '__main__': render(C, sys.argv)
