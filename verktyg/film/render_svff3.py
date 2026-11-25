# SvFF-övningar efter skickade PDF:er, del 3. Regel: först d.mv, sedan d.carry; först mottagarens rörelse, sedan passningen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e9', __file__.replace('render_svff3.py', 'render_extern9.py'))
e9 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e9); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e9.finish, e9.rec, e9.chain, e9.wander, e9.counter, e9.arrivals
lab, hide, show, team, boxes, drive, shoot = e9.lab, e9.hide, e9.show, e9.team, e9.boxes, e9.drive, e9.shoot
factor, swap_color, stand, countdown, countup, win = e9.factor, e9.swap_color, e9.stand, e9.countdown, e9.countup, e9.win
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'

# ============ wj05 Spelarna först – lekmatch utan coachning ============
SV = ('svb',)
import math
def tails(idx, fn): C[-1]['players'][idx]['tails'] = fn

# ============ svb140080 Futsal – Rädd om fötterna ============
d = Drill()
KP = [(24, 30), (70, 26), (30, 70), (74, 72), (50, 52), (46, 22), (60, 78)]
team(d, 'k', B, KP, [''] * 7)
balls = [d.newball(rec(d, f'k{k}', 0)) for k in range(7)]
for k in (0, 1, 3, 5, 6): wander(d, f'k{k}', 0, 17.9, (12, 14, 88, 86), 500 + k, 1.3); d.carry(balls[k], f'k{k}', 0, 17.9)
d.mv('k4', 0, 2.6, (44, 56)); d.carry(balls[4], 'k4', 0, 2.6); d.mv('k2', 0, 2.6, (30, 66)); d.carry(balls[2], 'k2', 0, 2.6)
th = d.pas(balls[4], 2.8, (31.5, 67), 0.5)                                                              # passning mot fötterna, under knähöjd
d.mv('k4', th, th + 0.8, (40, 62)); d.carry(balls[4], 'k4', th + 0.8, th + 0.9) if False else None
tb = d.pas(balls[4], th + 0.1, rec(d, 'k4', th + 1.1), 1.0)                                              # bollen studsar tillbaka till passaren
stand(d, 'k2', 2.6, 8.4); d.carry(balls[2], 'k2', 2.6, 8.4)                                             # träffad: bredbent, bollen över huvudet
wander(d, 'k4', tb, 17.9, (12, 14, 88, 86), 520, 1.3); d.carry(balls[4], 'k4', tb, 17.9)
d.mv('k6', 0, 0.1, d.pos('k6')); d.pl['k6']['tr'] = [(0, (60, 78))]; d.mv('k6', 0.2, 5.0, (40, 76)); d.mv('k6', 5.0, 6.2, (30, 70)); d.mv('k6', 6.2, 7.6, (30, 62)); d.mv('k6', 7.6, 8.6, (36, 56))   # kryper mellan benen
d.balls[6] = [(0, rec(d, 'k6', 0))]; d.carry(balls[6], 'k6', 0, 5.0); tp = d.pas(balls[6], 5.0, (38, 74), 0.4); d.mv('k6', 8.6, 9.4, (39, 73)); d.carry(balls[6], 'k6', 9.4, 9.6)
wander(d, 'k6', 9.6, 17.9, (12, 14, 88, 86), 530, 1.3); d.carry(balls[6], 'k6', 9.6, 17.9)
wander(d, 'k2', 8.6, 17.9, (12, 14, 88, 86), 531, 1.3); d.carry(balls[2], 'k2', 8.6, 17.9)
fp = [(0, 'Alla driver med varsin boll', 'Bollen nära foten – titta upp.'),
      (2.6, 'Träffa en motspelares fötter', 'Passning under knähöjd, egen boll under kontroll.'),
      (3.4, 'Träffad – bredbent med bollen över huvudet', 'Samma om bollen går ut över linjen.'),
      (6.2, 'Rädda kompisen – kryp mellan benen', 'Den som kryper kan inte bli tagen.')]
finish(d, 'svb140080', 'futsal-radd-om-fotterna-u7-u12-svb140080', ['Futsal – Rädd om fötterna', 'U7–U12'], 'Yta ca 15 × 12 m · Varsin boll',
       fp, 'LEK', [('box', 8, 10, 92, 90)], [lab(th, th + 1.2, (24, 60), 'TRÄFF!'), lab(3.4, 7.4, (30, 58), 'BREDBENT'), lab(7.4, 8.8, (42, 60), 'RÄDDAD!')])
C[-1]['_stuck'] = False

# ============ svb48710 Ta bollen (framåt) – spelform 3v3 ============
d = Drill(); d.p('t', 'T', T_COL, (96, 50))
XS = [20, 32, 44, 56, 68, 80]
for k, x in enumerate(XS): d.p(f'p{k}', '', B, (x, 88))
balls = [d.newball(rec(d, f'p{k}', 0)) for k in range(6)]
for k, x in enumerate(XS):
    pts = [(x + (3 if i % 2 else -3), 88 - 16 * (i + 1)) for i in range(4)] + [(x, 10)]
    t = 0.8
    for q in pts: t = drive(d, balls[k], f'p{k}', t, q, 20 + k % 3)
    d.mv(f'p{k}', t, 7.0, d.pos(f'p{k}')); d.carry(balls[k], f'p{k}', t, 7.0)
# progression 3: försvarare bakom mittlinjen bryter och driver över anfallarnas kortlinje
d.p('f', 'F', R, (50, 54))
for k, x in enumerate(XS): d.mv(f'p{k}', 7.0, 8.6, (x, 88)); d.carry(balls[k], f'p{k}', 7.0, 8.6)
for k, x in enumerate(XS):
    if k == 2: continue
    pts = [(x + (3 if i % 2 else -3), 88 - 20 * (i + 1)) for i in range(3)] + [(x, 10)]; t = 8.8
    for q in pts: t = drive(d, balls[k], f'p{k}', t, q, 20)
t = drive(d, balls[2], 'p2', 8.8, (46, 62), 18); tw = win(d, balls[2], 'f', 'p2', t + 0.3, 0.6)
t = drive(d, balls[2], 'f', tw, (48, 88), 20); d.mv('p2', tw, t, (50, 80))
fp = [(0, 'Alla med varsin boll på kortlinjen', 'Driv till motsatt kortlinje på signal.'),
      (0.8, 'Driv mot fri yta', 'Ändra riktning och öka farten vid behov.'),
      (7.0, 'Progression: försvarare startar bakom mittlinjen', 'Bryt mellan motståndarens tillslag.'),
      (tw + 0.2, 'Bryt – och driv över anfallarnas kortlinje', 'Tappar du bollen: ta tillbaka den.')]
finish(d, 'svb48710', 'ta-bollen-framat-spelform-3v3-svb48710', ['Ta bollen (framåt)', 'Spelform 3 mot 3'], '6–11 spelare · Yta 15 × 10 m · En boll per spelare',
       fp, 'SPELUPPBYGGNAD', [('box', 12, 8, 88, 92), ('line', [(12, 50), (88, 50)])], [lab(0.4, 1.4, (96, 40), 'NU!'), lab(tw, tw + 1.2, (60, 60), 'BRYT')])

# ============ svb140471 Futsal – Hämta bollar ============
d = Drill()
BP = [(24, 88), (40, 88), (56, 88), (72, 88)]; RP = [(30, 50), (50, 44), (70, 50), (44, 60)]
team(d, 'b', B, BP, [''] * 4); team(d, 'r', R, RP, [''] * 4)
BL = [(30, 12), (42, 14), (54, 12), (66, 14), (36, 16), (60, 16)]
bl = [d.newball(q) for q in BL]
caught = 1
for k in range(4):
    t0 = 0.4 + 0.3 * k; x = BP[k][0]
    if k == caught:
        d.mv(f'b{k}', t0, t0 + 1.8, (x + 4, 52)); tc = t0 + 1.8; d.mv('r1', 0.6, tc, (x + 6, 50))                  # svansen tagen
        d.mv(f'b{k}', tc + 0.2, tc + 3.6, (x, 88)); continue                                                         # utfallsgång tillbaka
    t1 = d.path(f'b{k}', t0, [(x + (6 if k % 2 else -6), 50), BL[[0, 1, 2, 3][k]]], 1.4)
    t2 = d.path(f'b{k}', t1 + 0.2, [(x - 4, 50), (x, 86)], 1.2); d.carry(bl[k], f'b{k}', t1 + 0.2, t2)
for k in (0, 2, 3): wander(d, f'r{k}', 0, 17.9, boxes([RP[k]], 8)[0], 540 + k, 1.2)
fp = [(0, 'Två lag – ena laget har västar som svans', 'Spring över och hämta en boll.'),
      (1.4, 'Fria ytor, byt riktning och öka farten', 'De jagande försöker ta svansarna.'),
      (tc - 0.2, 'Svansen tagen – utfallsgång tillbaka', 'Sedan ett nytt försök.'),
      (6.0, 'Hämta så många bollar som möjligt', 'Till exempel på en och en halv minut.')]
finish(d, 'svb140471', 'futsal-hamta-bollar-u7-u12-svb140471', ['Futsal – Hämta bollar', 'U7–U12'], 'Ca 8 spelare · Yta ca 15 × 12 m · Bollar på andra sidan',
       fp, 'FYS', [('box', 12, 6, 88, 94), ('line', [(12, 22), (88, 22)]), ('line', [(12, 80), (88, 80)])], [lab(tc, tc + 1.4, (BP[caught][0] + 10, 46), 'TAGEN!')])
fc = factor(fp)
for k in range(4): tails(k + 0, (lambda tt, k=k, a=tc * fc: 0 if (k == caught and tt >= a) else 1))
C[-1]['_stuck'] = False

# ============ svb140087 Futsal – Pendelspel (grund) ============
d = Drill()
d.p('kb', '', B, (50, 8)); d.p('kb2', '', B, (50, 92)); d.p('kr', '', R, (8, 50)); d.p('kr2', '', R, (92, 50))
team(d, 'b', B, [(40, 36), (58, 64)]); team(d, 'r', R, [(36, 58), (62, 40)])
bb = d.newball(rec(d, 'kb', 0)); br = d.newball(rec(d, 'kr', 0)); cnt = []
t = 0.4
for seq in (['b0', 'b1', 'kb2'], ['b1', 'b0', 'kb']):
    for pid in seq:
        if pid.startswith('b'): d.mv(pid, t - 0.2, t + 0.6, (d.pos(pid)[0] + (4 if pid == 'b0' else -4), d.pos(pid)[1]))
        t = d.pas(bb, t + 0.3, rec(d, pid, t + 1.0)); cnt.append(t)
t = 0.8
for seq in (['r0', 'r1', 'kr2'], ['r1', 'r0', 'kr']):
    for pid in seq:
        if pid.startswith('r'): d.mv(pid, t - 0.2, t + 0.6, (d.pos(pid)[0], d.pos(pid)[1] + (4 if pid == 'r0' else -4)))
        t = d.pas(br, t + 0.3, rec(d, pid, t + 1.0))
fp = [(0, 'En spelare på varje kortsida, två i mitten', 'Två lag med varsin boll.'),
      (1.2, 'Från kortsida till kortsida via mitten', ''),
      (3.6, 'Orientera dig åt alla håll', 'Möt bollen halvt rättvänd.'),
      (6.4, 'Ta emot med foten längst från motspelaren', 'Använd sulan för snabb kontroll.')]
finish(d, 'svb140087', 'futsal-pendelspel-grund-u7-u12-svb140087', ['Futsal – Pendelspel', 'Grund · U7–U12'], 'Yta ca 15 × 12 m · En boll per lag',
       fp, 'SPELUPPBYGGNAD', [('box', 14, 6, 86, 94)], counter(cnt, pos=(88, 92), last=None))

# ============ svb140057 Futsal – Tjuv och polis ============
d = Drill(); d.p('t', 'T', T_COL, (96, 50))
PR = [(28, 30), (70, 28), (30, 70), (72, 70)]
for k, (x, y) in enumerate(PR): d.p(f'tj{k}', 'TJ', B, (x, y)); d.p(f'po{k}', 'P', R, (x + 4, y + 4))
balls = [d.newball(rec(d, f'tj{k}', 0)) for k in range(4)] + [d.newball(rec(d, f'po{k}', 0)) for k in range(4)]
TS = 7.4
for k, (x, y) in enumerate(PR):
    box = (max(12, x - 18), max(12, y - 16), min(88, x + 18), min(88, y + 16))
    wander(d, f'tj{k}', 0, TS, box, 560 + k, 1.0); d.carry(balls[k], f'tj{k}', 0, TS)
    lag = 0.45 if k % 2 == 0 else 0.9                                                                             # polis 1 och 3 hänger med, 2 och 4 tappar
    tr = d.pl[f'tj{k}']['tr']; d.pl[f'po{k}']['tr'] = [(0, (x + 4, y + 4))] + [(t + lag, (px + 3.5, py + 3)) for t, (px, py) in tr if t + lag < TS] + [(TS, at(tr, TS - lag)[:1] + (at(tr, TS - lag)[1] + (3 if k % 2 == 0 else 9),))]
    d.carry(balls[4 + k], f'po{k}', 0, TS + 2.0); stand(d, f'tj{k}', TS, TS + 2.0); d.carry(balls[k], f'tj{k}', TS, TS + 2.0); d.mv(f'po{k}', TS, TS + 2.0, d.pos(f'po{k}'))
fp = [(0, 'Par med varsin boll – tjuv och polis', 'Tjuven driver fritt, polisen skuggar.'),
      (1.6, 'Tjuven: finta, ändra riktning, öka farten', 'Polisen: hänga med så nära som möjligt.'),
      (TS - 0.2, 'STOPP! Inom armlängd? Då vinner polisen', 'Annars vinner tjuven. Byt uppgifter.'),
      (TS + 1.2, 'Variant: polisen utan boll', 'Mer matchlikt – svårare för tjuven.')]
finish(d, 'svb140057', 'futsal-tjuv-och-polis-u7-u15-svb140057', ['Futsal – Tjuv och polis', 'U7–U15'], 'Ca 8 barn · Yta ca 15 × 15 m · Varsin boll',
       fp, 'SPELUPPBYGGNAD', [('box', 8, 8, 92, 92)], [lab(TS - 0.2, TS + 1.4, (88, 40), 'STOPP!')])

# ============ Svansleken (två poster med samma övning) ============
def svans(id_, slug):
    d = Drill()
    KP = [(26, 30), (70, 28), (30, 70), (72, 72), (50, 50), (48, 24)]
    team(d, 'k', B, KP, [''] * 6); team(d, 'f', R, [(12, 50), (88, 50)], ['', ''])
    for k in (0, 1, 3, 5): wander(d, f'k{k}', 0, 8.0, (14, 14, 86, 86), 600 + k, 1.2)
    d.mv('f0', 0.4, 2.6, (28, 64)); d.mv('k2', 0.4, 2.2, (24, 64)); tc = 2.6                                     # svansen tas – blir försvarare
    d.mv('k2', tc + 0.2, 8.0, (60, 36)); d.mv('f1', 0.4, 4.4, (52, 44)); d.mv('k4', 0.4, 4.2, (52, 40)); tc2 = 4.4
    wander(d, 'k4', tc2 + 0.2, 8.0, (14, 14, 86, 86), 610, 1.2); wander(d, 'f0', tc + 0.2, 8.0, (14, 14, 86, 86), 611, 1.2); wander(d, 'f1', tc2 + 0.2, 8.0, (14, 14, 86, 86), 612, 1.2)
    # progression: med boll
    P2 = [(26, 30), (70, 28), (30, 70), (72, 72), (50, 50), (48, 24)]
    for k, q in enumerate(P2): d.mv(f'k{k}', 8.0, 9.4, q)
    d.mv('f0', 8.0, 9.4, (12, 50)); d.mv('f1', 8.0, 9.4, (88, 50))
    balls = [d.newball((200, 200)) for _ in range(6)]
    for k in range(6): show(d, balls[k], 9.4, rec(d, f'k{k}', 9.4))
    for k in range(6):
        if k == 3:
            d.mv('k3', 9.6, 11.0, (78, 60)); d.carry(balls[3], 'k3', 9.4, 11.0); d.mv('f1', 9.6, 11.0, (80, 56))
            tw = d.pas(balls[3], 11.2, rec(d, 'f1', 11.5), 0.3); t = drive(d, balls[3], 'f1', 11.5, (95, 62), 14); hide(d, balls[3], t + 0.2)   # drivs ut ur ytan
            d.mv('k3', 11.5, t, (86, 62))
        else:
            wander(d, f'k{k}', 9.6, 17.9, (14, 14, 86, 86), 620 + k, 1.2); d.carry(balls[k], f'k{k}', 9.4, 17.9)
    wander(d, 'f0', 9.6, 17.9, (14, 14, 86, 86), 630, 1.2)
    fp = [(0, 'Alla har en väst som svans', 'Två försvarare försöker ta västarna.'),
          (tc - 0.2, 'Tagen svans – du blir försvarare', 'Spring mot fria ytor, byt riktning och öka farten.'),
          (8.0, 'Progression: med boll', 'Behåll bollen i ytan.'),
          (tw - 0.2, 'Försvararen tar bollen och driver ut den', 'Tappar du bollen – ta tillbaka den innan den är ute.')]
    finish(d, id_, slug, ['Svansleken', 'Speluppbyggnad'], 'Ca 6 spelare · Yta 10–12 × 7 m · Västar och bollar',
           fp, 'LEK', [('box', 10, 10, 90, 90)], [lab(tc, tc + 1.2, (36, 70), 'TAGEN!'), lab(tc2, tc2 + 1.2, (60, 40), 'TAGEN!')], target=15.5)
    fc = factor(fp)
    for k in range(6): tails(k, (lambda tt, k=k, a=tc * fc, b2=tc2 * fc, e=8.0 * fc: 0 if tt >= e else 0 if (k == 2 and tt >= a) or (k == 4 and tt >= b2) else 1))
    C[-1]['players'][2]['color'] = (lambda tt, a=tc * fc, e=8.0 * fc: R if a <= tt < e else B)
    C[-1]['players'][4]['color'] = (lambda tt, a=tc2 * fc, e=8.0 * fc: R if a <= tt < e else B)
    C[-1]['_stuck'] = False
svans('svb124187', 'svansleken-svb124187')
svans('svb68193', 'svansleken-svb68193')

# ============ svb140479 Futsal – Hålla bollen inom laget ============
d = Drill()
BP = [(24, 28), (70, 26), (28, 70), (72, 72)]; RP = [(48, 30), (26, 50), (74, 50), (50, 74)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
bb = d.newball(rec(d, 'b0', 0)); br = d.newball(rec(d, 'r0', 0)); ex = []
t = 0.4
for a, c, hf in [('b0', 'b1', 'r0'), ('b1', 'b3', 'r2'), ('b3', 'b2', 'r3'), ('b2', 'b0', 'r1')]:
    t = d.pas(bb, t + 0.3, rec(d, c, t + 1.2))
    hx, hy = at(d.pl[hf]['tr'], t + 0.8); d.mv(a, t, t + 0.8, (hx - 3, hy)); ex.append(lab(t + 0.8, t + 1.4, (hx, hy - 6), 'HIGH FIVE'))
    d.mv(a, t + 1.0, t + 2.2, (BP[int(a[1])][0] + 4, BP[int(a[1])][1] + 2))
t = 0.8
for a, c in [('r0', 'r2'), ('r2', 'r3'), ('r3', 'r1'), ('r1', 'r0')]:
    t = d.pas(br, t + 0.3, rec(d, c, t + 1.2)); d.mv(a, t, t + 1.4, (d.pos(a)[0] + 6, d.pos(a)[1] - 4))
fp = [(0, 'Två lag om fyra med varsin boll', 'Passa inom laget.'),
      (1.4, 'Efter passning: high five med en motståndare', 'Rör dig till en ledig yta.'),
      (4.4, 'Sulan vid mottagning – spänd fot vid passning', 'Byt uppgift: knäböj, upphopp eller ner på golvet.'),
      (8.0, 'Progression: 6 mot 2', 'Anfallarna håller bollen, försvararna erövrar och behåller.')]
finish(d, 'svb140479', 'futsal-halla-bollen-inom-laget-u7-u10-svb140479', ['Futsal – Hålla bollen inom laget', 'U7–U10'], '8 spelare · Yta 15 × 12 m · En boll per lag',
       fp, 'SPELUPPBYGGNAD', [('box', 12, 12, 88, 88)], ex)

# ============ svb313 Färdighetsövning 1 – uppvärmning och koordination (MV) ============
d = Drill()
LN = [(20, 86), (40, 86), (60, 86), (80, 86)]
for k, ps in enumerate(LN): d.p(f'p{k}', '', B, ps)
MOVES = ['HANDBANDY', 'RULLA OCH PLOCKA UPP', 'STUDSA OCH FÅNGA', 'KASTA UPP OCH FÅNGA', 'HAND TILL HAND', 'SPARKA UPP OCH FÅNGA']
seg = 2.6
for k, (x, y) in enumerate(LN):
    bb = d.newball((x + 1.8, y - 3)); tr = d.balls[bb]; t = 0.3 + 0.1 * k; yy = y
    for m in range(6):
        t0 = t; d.mv(f'p{k}', t0, t0 + seg, (x, yy - 12) if m % 2 == 0 else (x, yy + 12)); yy = yy - 12 if m % 2 == 0 else yy + 12
        for j in range(5):
            tt = t0 + j * seg / 5; px, py = at(d.pl[f'p{k}']['tr'], tt)
            if m == 1 and j in (1, 2): tr.append((tt, (px, py - 8)))                                                 # rullar iväg
            elif m in (2, 3, 5): tr += [(tt, (px + 1.8, py - 3)), (tt + seg / 10, (px + 1.8, py - (7 if m != 2 else 0) - 3))]
            elif m == 4: tr.append((tt, (px + (2.5 if j % 2 else -2.5), py - 4)))
            else: tr.append((tt, (px + 1.8, py - 2)))
        t = t0 + seg
    tr.append((t, (at(d.pl[f'p{k}']['tr'], t)[0] + 1.8, at(d.pl[f'p{k}']['tr'], t)[1] - 3)))
fp = [(0, 'En boll per barn – rör dig framåt', 'Följsamma och rytmiska rörelser.'),
      (2.9, 'Rulla iväg bollen – plocka upp den', 'Innan den slutat rulla.'),
      (5.5, 'Studsa och fånga – kasta upp och fånga', 'Med båda händerna eller en hand.'),
      (10.7, 'Hand till hand – sparka upp och fånga', 'Studsa med en hand: jogga, galopp, hoppsasteg.')]
finish(d, 'svb313', 'fardighetsovning-1-uppvarmning-och-koordination-mv-svb313', ['Färdighetsövning 1', 'Uppvärmning och koordination (MV)'], 'Lika många bollar som barn',
       fp, 'MÅLVAKT', [], [lab(0.3 + m * seg, 0.3 + (m + 1) * seg, (50, 50), MOVES[m]) for m in range(6)], target=15.6)
C[-1]['_stuck'] = True

# ============ svb263 Färdighetsövning 3 – skjuta ============
d = Drill()
for k in range(4): d.p(f'a{k}', 'A', B, (12, 20 + 20 * k)); d.p(f'b{k}', 'B', R, (88, 20 + 20 * k))
CB = [d.newball((50, 20 + 20 * k)) for k in range(4)]                                                          # bollar på konerna
ex = []
for k in range(4):
    sb = d.newball(rec(d, f'a{k}', 0)); t = 0.5 + 0.5 * k; aim = (50, 20 + 20 * k)
    th = d.pas(sb, t, aim, 0.8)
    if k != 2:
        d.pas(CB[k], th, (64, 20 + 20 * k + (4 if k % 2 else -4)), 0.6); ex.append(lab(th, th + 1.0, (50, 13 + 20 * k), 'TRÄFF!'))
        d.pas(sb, th, (58, 20 + 20 * k + 3), 0.5)
    else: d.pas(sb, th, (80, 24 + 20 * k - 20), 0.7)
tB = 5.2
for k in range(4):
    sb = d.newball((200, 200)); show(d, sb, tB + 0.3 * k - 0.2, rec(d, f'b{k}', tB + 0.3 * k - 0.2)); t = tB + 0.3 * k
    th = d.pas(sb, t, (50 if k == 2 else 60, 20 + 20 * k), 0.8)
    if k == 2: d.pas(CB[2], th, (36, 62), 0.6); ex.append(lab(th, th + 1.0, (50, 53), 'TRÄFF!'))
fp = [(0, 'Två lag – lag A har varsin boll', 'Skjut ner bollarna som ligger på konerna.'),
      (0.6, 'Titta upp innan du skjuter', 'Titta på bollen när du skjuter.'),
      (tB - 0.2, 'Nu är det lag B:s tur', ''),
      (tB + 2.0, 'Spänn foten och träffa bollen hårt', 'För kraft i skottet.')]
finish(d, 'svb263', 'fardighetsovning-3-skjuta-svb263', ['Färdighetsövning 3', 'Skjuta'], '8 barn · Yta 20 × 20 m · Bollar på koner',
       fp, 'AVSLUT', [('box', 8, 8, 92, 92)] + [('cone', 50, 22 + 20 * k) for k in range(4)], ex)
C[-1]['_stuck'] = True

if __name__ == '__main__': render(C, sys.argv)
