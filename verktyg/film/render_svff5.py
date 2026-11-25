# SvFF-övningar efter skickade PDF:er, del 5. Regel: först d.mv, sedan d.carry; först mottagarens rörelse, sedan passningen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e9', __file__.replace('render_svff5.py', 'render_extern9.py'))
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

# ============ svb68199 Prickboll ============
d = Drill()
for k in range(3): d.p(f'a{k}', '', B, (32 + 18 * k, 88)); d.p(f'b{k}', '', R, (32 + 18 * k, 12))
mid = d.newball((50, 50)); t = 0.5; ex = []; mx, my = 50, 50
for r, (pid, ky) in enumerate([('a0', 88), ('b2', 12), ('a1', 88), ('a2', 88), ('b0', 12), ('a1', 88)]):
    bb = d.newball((200, 200)); show(d, bb, t - 0.1, rec(d, pid, t - 0.1)); th = d.pas(bb, t, (mx, my + (3 if ky > 50 else -3)), 0.8)
    push = -9 if ky > 50 else 9; nmy = my + push
    d.pas(mid, th, (mx, nmy), 0.6); d.pas(bb, th, (mx + (8 if r % 2 else -8), my + (8 if ky > 50 else -8)), 0.6); hide(d, bb, th + 1.2)
    my = nmy; t = th + 0.7
d.pas(mid, t, (mx, 6), 0.8); ex.append(lab(t + 0.6, t + 2.0, (50, 18), 'ÖVER LINJEN!'))
fp = [(0, 'Två lag på var sin sida – en boll i mitten', 'Skjut på mittbollen så att den rullar över motståndarnas linje.'),
      (1.2, 'Skott: stödjefoten bredvid bollen', 'Träffa med spänd fot.'),
      (4.0, 'Progression 1: rulla', 'Greppa bollen, kliv fram med motsatt ben, böj knät.'),
      (t - 0.6, 'Progression 2: kasta', 'För bollen i en båge över huvudet.')]
finish(d, 'svb68199', 'prickboll-svb68199', ['Prickboll', 'Speluppbyggnad'], 'Ca 6 spelare · Yta 10–12 × 7 m · Bollar',
       fp, 'LEK', [('line', [(14, 82), (86, 82)]), ('line', [(14, 18), (86, 18)])], ex)
C[-1]['_stuck'] = True

# ============ Gul och blå (två poster) ============
def gulbla(id_, slug, title, label, caps):
    d = Drill(); d.p('t', 'T', T_COL, (50, 96))
    ROWS = [30, 46, 62, 78]
    for k, y in enumerate(ROWS): d.p(f'g{k}', '', B, (44, y)); d.p(f'h{k}', '', R, (56, y))
    # GUL! – spelaren närmast den gula konan (vänster) springer, den andra jagar
    for k, y in enumerate(ROWS):
        d.mv(f'g{k}', 1.2 + 0.05 * k, 2.6, (12, y + (2 if k % 2 else -2))); d.mv(f'h{k}', 1.35 + 0.05 * k, 2.6, (18 + (6 if k == 1 else 0), y))
        d.mv(f'g{k}', 3.6, 5.2, (44, y)); d.mv(f'h{k}', 3.6, 5.2, (56, y))
    # progression med boll: BLÅ! – spelaren vid blå kona driver, den andra jagar utan boll
    balls = [d.newball((200, 200)) for _ in ROWS]
    for k, y in enumerate(ROWS):
        show(d, balls[k], 5.6, rec(d, f'h{k}', 5.6)); d.mv(f'h{k}', 5.6, 6.4, (56, y)); d.carry(balls[k], f'h{k}', 5.6, 6.6)
        t = drive(d, balls[k], f'h{k}', 6.8 + 0.06 * k, (88, y), 24); d.mv(f'g{k}', 6.95 + 0.06 * k, t, (80 if k != 2 else 86, y))
    fp = [(0, *caps[0]), (1.2, *caps[1]), (3.6, *caps[2]), (6.6, *caps[3])]
    finish(d, id_, slug, title, 'Spelare två och två · Yta ca 15 × 12 m · Gula och blå koner', fp, label,
           [('yellowcone', 8, y) for y in ROWS] + [('cone', 92, y) for y in ROWS], [lab(1.0, 2.2, (70, 92), '”GUL!”'), lab(6.4, 7.6, (70, 92), '”BLÅ!”')])

gulbla('svb22907', 'fs-gul-och-bla-svb22907', ['FS – Gul och Blå', 'Explosiv träning'], 'FYS',
       [('Två och två mittemot varandra', 'Gul kona bakom den ena, blå kona bakom den andra.'),
        ('”GUL!” – spring förbi den gula konan', 'Innan den andra hinner nudda din rygg.'),
        ('Stegring 1: ”GUL!” – den blåa springer', 'Var uppmärksam på signalen.'),
        ('Stegring 2: med boll', 'Driv förbi konan – korta steg först, sedan längre.')])
gulbla('svb69603', 'gul-och-bla-svb69603', ['Gul och blå', 'Lek'], 'LEK',
       [('Två och två mittemot varandra', 'Gul kona bakom den ena, blå kona bakom den andra.'),
        ('”GUL!” – spring förbi den gula konan', 'Innan den andra hinner nudda din rygg.'),
        ('Progression 1: byt håll', 'Vid ”GUL!” springer i stället den blåa.'),
        ('Progression 2: med boll', 'Driv med vristen eller utsidan – jagaren springer utan boll.')])

# ============ svb22909 FS – Tom och Jerry ============
d = Drill()
BL = [(44, 44), (52, 42), (58, 48), (46, 54), (54, 56), (50, 50)]
bl = [d.newball(q) for q in BL]
team(d, 'b', B, [(24, 90), (44, 90), (64, 90)], ['', '', '']); team(d, 'y', YEL, [(24, 10), (44, 10), (64, 10)], ['', '', '']); d.p('tom', 'TOM', R, (34, 50))
for k, (pid, home, gi) in enumerate([('b0', 90, 0), ('y1', 10, 1), ('b2', 90, 4), ('y0', 10, 2)]):
    t0 = 0.5 + 0.6 * k; sx = d.pos(pid)[0]
    t1 = d.path(pid, t0, [(sx + 6, 70 if home > 50 else 30), (BL[gi][0] - 1.8, BL[gi][1] + 1.2)], 1.4)
    t2 = d.path(pid, t1 + 0.2, [(sx + 2, 70 if home > 50 else 30), (sx, home)], 1.3); d.carry(bl[gi], pid, t1 + 0.2, t2)
d.mv('y2', 0.8, 2.6, (58, 30)); d.mv('tom', 0.6, 2.6, (60, 32)); tc = 2.6                                         # Tom tar svansen
d.mv('y2', tc + 0.2, tc + 2.0, (64, 10)); d.mv('tom', tc + 0.3, tc + 3.0, (34, 50))
wander(d, 'tom', tc + 3.0, 17.9, (28, 30, 72, 70), 800, 1.4)
fp = [(0, 'Bollarna i mitten – Tom vaktar', 'Jerry har en väst som svans. Två lag.'),
      (0.8, 'Hämta en boll och ta den bakom din linje', 'Spring åt olika håll – samarbeta i laget.'),
      (tc - 0.2, 'Tagen! Lämna tillbaka en boll till mitten', 'Säker bakom linjen och i bollytan.'),
      (6.0, 'Flest bollar när mitten är tom vinner', 'Stegring: driv bollarna tillbaka, inga händer.')]
finish(d, 'svb22909', 'fs-tom-och-jerry-svb22909', ['FS – Tom och Jerry', 'Lek'], 'Yta ca 15 × 12 m · Bollar i mitten · Västar som svansar',
       fp, 'LEK', [('box', 14, 6, 86, 94), ('line', [(14, 84), (86, 84)]), ('line', [(14, 16), (86, 16)]), ('box', 38, 38, 62, 62)], [lab(tc, tc + 1.4, (66, 24), 'TAGEN!')])
fc = factor(fp)
for i in range(6): tails(i, (lambda tt, i=i, a=tc * fc: 0 if (i == 5 and tt >= a) else 1))
C[-1]['_stuck'] = False

# ============ svb22958 FS – Fotbollskubb ============
d = Drill()
for k in range(3): d.p(f'a{k}', '', B, (30 + 20 * k, 92)); d.p(f'b{k}', '', R, (30 + 20 * k, 8))
KA = [(30, 74), (50, 74), (70, 74)]; KB = [(30, 26), (50, 26), (70, 26)]
ka = [d.newball(q) for q in KA]; kb = [d.newball(q) for q in KB]; king = d.newball((50, 50))
seq = [('a0', kb, 0), ('b1', ka, 2), ('a1', kb, 1), ('a2', kb, 2), ('b0', ka, 0), ('a1', None, None)]
t = 0.5; ex = []
for pid, target, ti in seq:
    bb = d.newball((200, 200)); show(d, bb, t - 0.1, rec(d, pid, t - 0.1))
    if target is None:
        th = d.pas(bb, t, (50, 50), 0.9); d.pas(king, th, (54, 40), 0.5); ex.append(lab(th, th + 1.6, (64, 46), 'KUNGEN!'))
    else:
        tx, ty = (KB if target is kb else KA)[ti]; th = d.pas(bb, t, (tx, ty), 0.9); d.pas(target[ti], th, (tx + 4, ty + (-8 if target is kb else 8)), 0.5)
        ex.append(lab(th, th + 1.0, (tx, ty + (-6 if target is kb else 6)), 'PRICK'))
    hide(d, bb, th + 0.4); t = th + 0.6
fp = [(0, 'Två lag bakom var sin linje', 'Bollar på koner framför – kungen i mitten.'),
      (0.8, 'Pricka motståndarnas bollar', 'Sikta med stödjefoten, spänd fot mitt på bollen.'),
      (3.6, 'Vanliga kubbregler', 'Alla motståndarbollar först – sedan kungen.'),
      (t - 1.2, 'Kungen ner – laget vinner!', 'Stegring: rulla, eller kasta som ett målvaktsutkast.')]
finish(d, 'svb22958', 'fs-fotbollskubb-svb22958', ['FS – Fotbollskubb', 'Lek'], '2–8 spelare · Yta ca 15 × 12 m · Bollar på koner',
       fp, 'LEK', [('line', [(14, 86), (86, 86)]), ('line', [(14, 14), (86, 14)])] + [('cone', x, y + 2) for x, y in KA + KB] + [('yellowcone', 50, 52)], ex)
C[-1]['_stuck'] = True

# ============ svb22961 FS – Bowling ============
d = Drill()
TRI = [(50, 22), (44, 30), (56, 30), (38, 38), (50, 38), (62, 38)]
pins = [d.newball(q) for q in TRI]
for k in range(3): d.p(f'p{k}', '', B, (42 + 8 * k, 86))
t = 0.6; rt = []
for pid, hits in [('p0', [0, 1, 2, 3, 4, 5])]:
    bb = d.newball(rec(d, pid, t - 0.1)); d.mv(pid, t - 0.4, t, (d.pos(pid)[0], 82))
    th = d.pas(bb, t, (50, 42), 1.1); rt.append(th)
    for hi in hits: hx, hy = TRI[hi]; d.pas(pins[hi], th + 0.04 * hi, (hx + (hx - 50) * 0.7, hy - 10), 0.5)
    d.pas(bb, th, (50, 10), 0.6); hide(d, bb, th + 0.8)
fp = [(0, 'Minst sex bollar på koner i en triangel', 'Rulla från linjen – två försök per omgång.'),
      (0.6, 'Bollen mellan handen och underarmen', 'Kliv fram med ett utfallssteg, motsatt ben.'),
      (rt[0] + 0.2, 'Alla ner på första = STRIKE', 'På andra försöket = spärr.'),
      (rt[0] + 1.6, 'Stegring: kasta – sedan skjut eller passa', 'Sikta med stödjefoten, spänd fot mitt på bollen.')]
finish(d, 'svb22961', 'fs-bowling-svb22961', ['FS – Bowling', 'Komma till avslut'], '2–3 spelare · Yta ca 10 × 2 m · Bollar på koner',
       fp, 'AVSLUT', [('cone', x, y + 2) for x, y in TRI] + [('line', [(30, 80), (70, 80)])], [lab(rt[0], rt[0] + 1.6, (72, 28), 'STRIKE!')])
C[-1]['_stuck'] = True

# ============ svb22965 FS – Inte nudda boll ============
d = Drill()
RUN = [(22, 90), (36, 90), (50, 90), (64, 90), (78, 90)]
team(d, 'k', B, RUN, [''] * 5); team(d, 'l', R, [(6, 34), (6, 62), (94, 46)], ['L', 'L', 'L'])
ex = []
for k, (x, y) in enumerate(RUN):
    zig = [(x + (6 if k % 2 else -6), 66), (x + (-4 if k % 2 else 4), 40), (x, 10)]
    d.path(f'k{k}', 1.0 + 0.1 * k, zig, 1.1)
for li, (lid, tgt, tt) in enumerate([('l0', 'k1', 2.0), ('l2', 'k3', 2.6), ('l1', 'k0', 3.2)]):
    bb = d.newball(rec(d, lid, 0)); tx, ty = at(d.pl[tgt]['tr'], tt + 0.6); th = d.pas(bb, tt, (tx + 6 if li == 0 else tx - 1, ty + 2), 0.6)
    hide(d, bb, th + 0.6)
    if li == 1: ex.append(lab(th, th + 1.4, (tx, ty - 8), 'TRÄFF!')); thit = th
    else: ex.append(lab(th, th + 1.0, (tx, ty - 8), 'MISS'))
d.mv('k3', thit + 1.5, thit + 3.6, (94, 70))                                                                     # träffad – blir ledare
fp = [(0, 'Alla på ena kortsidan', 'Ledarna med bollar längs långsidorna.'),
      (1.0, 'Spring över – undvik bollarna', 'Ändra tempo och riktning, eller hoppa.'),
      (thit - 0.2, 'Träffad under knät? Du blir ledare', 'Ledarna passar bara med bredsidan.'),
      (thit + 1.8, 'Fortsätt tills alla är träffade', 'Stegring: ledarna rullar bollarna.')]
finish(d, 'svb22965', 'fs-inte-nudda-boll-svb22965', ['FS – Inte nudda boll', 'Hoppa – landa – löp'], 'Yta ca 15 × 12 m · Ledare med bollar på långsidorna',
       fp, 'UPPVÄRMNING', [('box', 12, 6, 88, 94)], ex)
fc = factor(fp); C[-1]['players'][3]['color'] = (lambda tt, a=thit * fc: R if tt >= a else B)

# ============ Bollstafetter i led (kasta–fånga, över–under) ============
def ledstafett(id_, slug, title, caps, mode):
    d = Drill(); YS = [80, 68, 56, 44, 32, 20]
    team(d, 'p', B, [(50, y) for y in YS], [str(i + 1) for i in range(6)])
    b = d.newball(rec(d, 'p0', 0)); t = 0.5; ex = []
    if mode == 'kasta':
        d.mv('p0', 0.1, 0.4, (50, 86))
        for k in range(1, 6):
            t = d.pas(b, t, rec(d, f'p{k}', t + 0.6), 0.5); t = d.pas(b, t + 0.15, rec(d, 'p0', t + 0.7), 0.5)
            d.mv(f'p{k}', t, t + 0.3, (52, YS[k] + 1)); ex.append(lab(t, t + 0.8, (62, YS[k]), 'NER')); t += 0.2
        t = d.pas(b, t, rec(d, 'p5', t + 0.9), 0.8)
    else:
        for k in range(1, 6):
            t = d.pas(b, t + 0.05, rec(d, f'p{k}', t + 0.45), 0.4); ex.append(lab(t - 0.3, t + 0.3, (64, YS[k]), 'ÖVER' if k % 2 else 'UNDER'))
    tr = drive(d, b, 'p5', t + 0.2, (40, 50), 14) if mode != 'kasta' else t
    d.mv('p5', t + 0.2, t + 2.0, (50, 92)); d.carry(b, 'p5', t + 0.2, t + 2.0)
    fp = [(0, *caps[0]), (1.0, *caps[1]), (t - 0.6, *caps[2]), (t + 1.6, *caps[3])]
    finish(d, id_, slug, title, 'Ca 6 spelare · Bollar · Tävla mot klockan', fp, 'FYS', [], ex)
    C[-1]['_stuck'] = True
ledstafett('svb68190', 'bollstafett-kasta-fanga-svb68190', ['Bollstafett', 'Kasta – fånga'],
           [('Transportera bollen genom ledet', 'Den första står vänd mot de andra.'),
            ('Kasta – fånga tillbaka – sätt dig ner', 'Fånga med hela händerna.'),
            ('Sista spelaren springer fram och ställer sig först', 'Upprepa tills alla är tillbaka.'),
            ('Ta tid – slå er egen tid', 'Progression: längre avstånd, ett ben, två lag.')], 'kasta')
ledstafett('svb68187', 'bollstafett-over-under-svb68187', ['Bollstafett', 'Över – under'],
           [('Transportera bollen genom ledet', 'Så fort som möjligt.'),
            ('Varannan över huvudet, varannan mellan benen', 'Rör dig smidigt.'),
            ('Sista spelaren springer fram och ställer sig först', 'Upprepa tills alla är tillbaka.'),
            ('Ta tid – slå er egen tid', 'Progression: dribbla slalom tillbaka, två lag.')], 'over')

# ============ svb10577 FS – Färdighetsövning Ta bollen ============
d = Drill()
XS = [26, 42, 58, 74]
for k, x in enumerate(XS): d.p(f'b{k}', '', B, (x, 14)); d.p(f'r{k}', '', R, (x + 4, 62))
balls = [d.newball((x + 1.8, 22)) for x in XS]; tw = []
for k, x in enumerate(XS):
    t0 = 0.4 + 0.2 * k; d.mv(f'b{k}', t0, t0 + 0.6, (x, 24)); t = drive(d, balls[k], f'b{k}', t0 + 0.6, (x + (4 if k % 2 else -4), 50), 14)
    t = drive(d, balls[k], f'b{k}', t, (x, 58), 10); d.mv(f'r{k}', t - 1.0, t, (x + 3, 58))
    w = win(d, balls[k], f'r{k}', f'b{k}', t + 0.3 + 0.2 * k, 0.4); tw.append(w)
    t2 = drive(d, balls[k], f'r{k}', w, (x + (6 if k % 2 else -6), 84), 14); d.mv(f'b{k}', w + 0.2, w + 1.6, (x, 26))
fp = [(0, 'Blått hämtar en boll i zon A', 'Och driver in den i zon B. Inga passningar.'),
      (1.6, 'Rött erövrar bollarna i zon B', 'Kom så nära som möjligt.'),
      (tw[0] - 0.2, 'Driv in den erövrade bollen i zon C', 'Styr mot den fot där motspelaren har bollen.'),
      (tw[-1] + 1.0, 'Hur lång tid tar det att erövra alla?', 'Byt uppgifter.')]
finish(d, 'svb10577', 'fs-fardighetsovning-ta-bollen-svb10577', ['FS – Färdighetsövning', 'Ta bollen'], '8 barn · Yta 15 × 15 m · Zon A, B och C',
       fp, 'FÖRSVAR', [('box', 14, 8, 86, 92), ('line', [(14, 36), (86, 36)]), ('line', [(14, 72), (86, 72)]), ('text', 90, 22, 'A'), ('text', 90, 54, 'B'), ('text', 90, 82, 'C')], [])

# ============ svb223 Färdighetsövning – driva ============
d = Drill()
TOPX = [30, 50, 70]
for k, x in enumerate(TOPX): d.p(f't{k}', '', B, (x, 14)); d.p(f'u{k}', '', B, (x, 86))
balls = [d.newball(rec(d, f't{k}', 0)) for k in range(3)] + [d.newball(rec(d, f'u{k}', 0)) for k in range(3)]
for k, x in enumerate(TOPX):
    t = drive(d, balls[k], f't{k}', 0.5, (x + 3, 50), 14); t = drive(d, balls[k], f't{k}', t, (x - 3, 84), 14)
    t2 = drive(d, balls[3 + k], f'u{k}', 0.5, (x - 3, 50), 14); t2 = drive(d, balls[3 + k], f'u{k}', t2, (x + 3, 16), 14)
TS = 6.4; ids = [f't{k}' for k in range(3)] + [f'u{k}' for k in range(3)]
for i, pid in enumerate(ids):
    if pid == 'u1': continue
    wander(d, pid, TS, 17.9, (16, 16, 84, 84), 820 + i, 1.2); d.carry(balls[i], pid, TS, 17.9)
d.mv('u1', TS, TS + 2.2, rec(d, 't0', TS + 2.2)); d.carry(balls[4], 'u1', TS, TS + 2.2); tk = TS + 2.2               # jägaren kullar
wander(d, 'u1', tk + 0.2, 17.9, (16, 16, 84, 84), 830, 1.2); d.carry(balls[4], 'u1', tk + 0.2, 17.9)
fp = [(0, 'Alla driver var sin boll', 'Mellan kvadratens sidor.'),
      (1.0, 'Sträck på foten när du driver', ''),
      (TS, 'Stegring: alla driver runt i kvadraten', 'Ett barn är jägare.'),
      (tk - 0.2, 'Kullad? Då blir du ny jägare', 'Titta upp så ofta som möjligt.')]
finish(d, 'svb223', 'fardighetsovning-driva-svb223', ['Färdighetsövning', 'Driva'], '6 barn · Yta 15 × 15 m · Bollar och koner',
       fp, 'SPELUPPBYGGNAD', [('box', 12, 12, 88, 88)], [lab(tk, tk + 1.4, (40, 30), 'KULLAD!')])
fc = factor(fp)
C[-1]['players'][4]['color'] = (lambda tt, a=TS * fc, b2=tk * fc: R if a <= tt < b2 else B)
C[-1]['players'][0]['color'] = (lambda tt, b2=tk * fc: R if tt >= b2 else B)

# ============ svb45154 Skjuta, rulla och kasta i mål ============
d = Drill()
SP = [(30, 56), (38, 56), (46, 56), (54, 56), (62, 56), (70, 56)]
team(d, 's', B, SP, [''] * 6); t = 0.4; ex = []
for r, kind in enumerate(['SKJUTA', 'KASTA', 'RULLA']):
    for k in range(6):
        bb = d.newball((200, 200)); show(d, bb, t - 0.1, rec(d, f's{k}', t - 0.1))
        tg = d.pas(bb, t, (38 + 4.5 * k, 2), 0.7 if kind != 'RULLA' else 1.0); hide(d, bb, tg + 0.3); t += 0.3
    ex.append(lab(t - 1.8, t + 0.5, (50, 76), kind)); t += 0.9
fp = [(0, 'Varsin boll framför målet', 'I mål utan att bollen studsar före mållinjen.'),
      (0.6, 'Skjut med höger och vänster fot', 'Stödjefoten bredvid bollen, spänd fot.'),
      (2.9, 'Progression 1: kasta', 'För bollen i en båge över huvudet – båda händerna.'),
      (5.3, 'Progression 2: rulla', 'Bollen ska rulla över mållinjen längs marken.')]
finish(d, 'svb45154', 'skjuta-rulla-och-kasta-i-mal-svb45154', ['Skjuta, rulla och kasta i mål', 'Speluppbyggnad'], 'Ca 6 spelare · Ett mål · Varsin boll',
       fp, 'LEK', [('cone', x, 60) for x in (26, 74)], ex)
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ svb58231 Behålla bollen ============
d = Drill(); BX = (14, 22, 86, 78)
PR = [((30, 36), (38, 42)), ((70, 34), (62, 40)), ((50, 64), (58, 58))]
for k, (a, f) in enumerate(PR): d.p(f'a{k}', '', B, a); d.p(f'f{k}', '', R, f)
for k in range(3):                                                                                                # utan boll: kull
    tr = None; wander(d, f'a{k}', 0, 5.0, (max(14, PR[k][0][0] - 16), max(22, PR[k][0][1] - 12), min(86, PR[k][0][0] + 16), min(78, PR[k][0][1] + 12)), 840 + k, 1.0)
    tr = d.pl[f'a{k}']['tr']; d.pl[f'f{k}']['tr'] = [(0, PR[k][1])] + [(t + 0.7, (x + 4, y + 3)) for t, (x, y) in tr if t > 0]
balls = [d.newball((200, 200)) for _ in range(3)]
for k in range(3):
    show(d, balls[k], 5.4, rec(d, f'a{k}', 5.4))
    box = (max(14, PR[k][0][0] - 16), max(22, PR[k][0][1] - 12), min(86, PR[k][0][0] + 16), min(78, PR[k][0][1] + 12))
    if k == 0:
        wander(d, 'a0', 5.4, 8.0, box, 850, 1.0); d.carry(balls[0], 'a0', 5.4, 8.0); d.mv('f0', 5.6, 8.0, rec(d, 'a0', 8.0))
        tw = d.pas(balls[0], 8.2, rec(d, 'f0', 8.5), 0.3); wander(d, 'f0', 8.5, 17.9, box, 851, 1.0); d.carry(balls[0], 'f0', 8.5, 17.9)
        d.pl['a0']['tr'] += [(t + 0.6, (x - 4, y + 3)) for t, (x, y) in d.pl['f0']['tr'] if t > 8.5]
    else:
        d.mv(f'a{k}', 5.0, 5.4, d.pos(f'a{k}')); wander(d, f'a{k}', 5.4, 17.9, box, 860 + k, 1.0); d.carry(balls[k], f'a{k}', 5.4, 17.9)
        tr = d.pl[f'a{k}']['tr']; d.pl[f'f{k}']['tr'] += [(t + 0.7, (x + 4, y + 3)) for t, (x, y) in tr if t > 5.6]
fp = [(0, 'Två och två – den ena kullar den andra', 'Kullad? Byt roller.'),
      (5.4, 'Progression 1: med boll', 'Försök ta bollen från varandra.'),
      (tw - 0.2, 'Täck bollen med kroppen', 'Bryt, och driv bort efter bollvinst.'),
      (tw + 1.6, 'Progression 2: i lag', 'Kan ett lag ha alla bollar samtidigt?')]
finish(d, 'svb58231', 'behalla-bollen-svb58231', ['Behålla bollen', 'Speluppbyggnad'], 'Ca 6 spelare · Yta 10–12 × 7 m · Bollar och västar',
       fp, 'SPELUPPBYGGNAD', [('box', *BX)], [lab(tw, tw + 1.4, (40, 30), 'TAGEN!')])

# ============ svb247 Färdighetsövning – utmana, finta och dribbla 3 ============
d = Drill(); d.p('t', 'T', T_COL, (96, 50))
PR = [(26, 26), (72, 24), (50, 50), (28, 74), (74, 74)]
for k, (x, y) in enumerate(PR): d.p(f'tj{k}', 'A', B, (x, y)); d.p(f'po{k}', 'B', R, (x + 4, y + 4))
balls = [d.newball(rec(d, f'tj{k}', 0)) for k in range(5)] + [d.newball(rec(d, f'po{k}', 0)) for k in range(5)]
TS = 7.4
for k, (x, y) in enumerate(PR):
    box = (max(10, x - 16), max(10, y - 16), min(90, x + 16), min(90, y + 16))
    wander(d, f'tj{k}', 0, TS, box, 870 + k, 1.0); d.carry(balls[k], f'tj{k}', 0, TS)
    lag = 0.45 if k % 2 == 0 else 0.95
    tr = d.pl[f'tj{k}']['tr']; end = at(tr, TS - lag)
    d.pl[f'po{k}']['tr'] = [(0, (x + 4, y + 4))] + [(t + lag, (px + 3.5, py + 3)) for t, (px, py) in tr if 0 < t + lag < TS] + [(TS, (end[0] + 3, end[1] + (3 if k % 2 == 0 else 9)))]
    d.carry(balls[5 + k], f'po{k}', 0, TS + 2.0); stand(d, f'tj{k}', TS, TS + 2.0); d.carry(balls[k], f'tj{k}', TS, TS + 2.0); d.mv(f'po{k}', TS, TS + 2.0, d.pos(f'po{k}'))
fp = [(0, 'Par där alla har var sin boll', 'A (tjuven) driver fritt, B (polisen) skuggar.'),
      (1.6, 'Finta åt ett håll – gå åt det andra', 'Polisen tappar balansen och hinner inte med.'),
      (TS - 0.2, 'STOPP! Är polisen inom en armlängd?', 'Då vinner polisen, annars tjuven.'),
      (TS + 1.2, 'Byt uppgift', '')]
finish(d, 'svb247', 'fardighetsovning-utmana-finta-och-dribbla-3-svb247', ['Färdighetsövning', 'Utmana, finta och dribbla 3'], '10 barn · Yta 20 × 20 m · Var sin boll',
       fp, 'DUELL', [('box', 6, 6, 94, 94)], [lab(TS - 0.2, TS + 1.4, (88, 40), 'STOPP!')])

# ============ svb45165 Boule ============
d = Drill(); CN = (50, 30)
SP = [(26, 82), (38, 86), (50, 88), (62, 86), (74, 82)]
team(d, 's', B, SP, [''] * 5); t = 0.5; ex = []
STOP = [(46, 36), (55, 27), (52, 33), (43, 25), (51, 31)]
KIND = ['HÖGER FOT', 'VÄNSTER FOT', 'RULLA', 'KASTA', 'RULLA']
for k in range(5):
    bb = d.newball(rec(d, f's{k}', 0)); tg = d.pas(bb, t, STOP[k], 1.2 if k < 2 else 1.4); ex.append(lab(t, t + 1.4, (SP[k][0], SP[k][1] - 10), KIND[k])); t = tg + 0.4
ex.append(lab(t, t + 1.8, (66, 30), 'NÄRMAST!'))
fp = [(0, 'Varsin boll – en kona i ytan', 'Din boll ska stanna så nära konan som möjligt.'),
      (0.6, 'Skott med höger och vänster fot', 'Stödjefoten bredvid bollen, vristen mitt på bollen.'),
      (4.0, 'Rulla och kasta med höger och vänster hand', 'Kliv fram med motsatt ben, böj knät.'),
      (t, 'Vems boll är närmast?', 'Variera avståndet till konan.')]
finish(d, 'svb45165', 'boule-svb45165', ['Boule', 'Speluppbyggnad'], 'Ca 6 spelare · Yta 15 × 20 m · Varsin boll · En kona',
       fp, 'LEK', [('yellowcone', *CN)], ex)
C[-1]['_stuck'] = True

# ============ svb45167 Sicksack stafett ============
d = Drill()
CN = [(34, 70), (34, 56), (34, 42), (34, 28)]
for k in range(3): d.p(f'a{k}', str(k + 1), B, (34, 86 + 4 * k)); d.p(f'b{k}', str(k + 1), R, (66, 86 + 4 * k))
t = 0.4
for k in range(3):
    pid = f'a{k}'; d.mv(pid, t, t + 0.4, (34, 84)); zig = [(34 + (5 if i % 2 else -5), y) for i, (x, y) in enumerate(CN)] + [(34, 16)]
    t1 = d.path(pid, t + 0.4, zig, 1.6); t2 = d.path(pid, t1, [(42, 50), (44 + 5 * k, 86)], 1.8); d.mv(pid, t2, t2 + 0.6, (44 + 5 * k, 96))
    if k < 2: d.mv(f'a{k + 1}', t2 - 0.6, t2, (34, 84))
    t = t2 - 0.6
T2 = 0.4; balls = []
for k in range(3):                                                                                                  # progression: med boll
    pid = f'b{k}'; bb = d.newball(rec(d, pid, 0)) if k == 0 else d.newball((200, 200))
    if k: show(d, bb, T2, rec(d, pid, T2))
    d.mv(pid, T2, T2 + 0.4, (66, 84)); d.carry(bb, pid, T2, T2 + 0.4); t1 = T2 + 0.4
    for i, (x, y) in enumerate(CN): t1 = drive(d, bb, pid, t1, (66 + (5 if i % 2 else -5), y), 18)
    t1 = drive(d, bb, pid, t1, (66, 16), 18); t2 = drive(d, bb, pid, t1, (56 - 5 * k, 86), 22); d.mv(pid, t2, t2 + 0.6, (56 - 5 * k, 96)); d.carry(bb, pid, t2, t2 + 0.6); hide(d, bb, t2 + 0.7)
    T2 = t2 - 0.4
fp = [(0, 'Spring sicksack mellan konorna', 'Sedan rakt tillbaka – nästa startar.'),
      (1.6, 'Riktningsförändring och tempoväxling', 'Titta på bollen.'),
      (4.6, 'Progression 1: med boll', 'Röda laget driver bollen genom konorna.'),
      (8.0, 'Progression 2: två lag tävlar', 'Ta tid – slå er egen tid.')]
finish(d, 'svb45167', 'sicksack-stafett-svb45167', ['Sicksack stafett', 'Fotbollskoordination'], 'Ca 6 spelare · Bollar och konor',
       fp, 'FYS', [('cone', x, y) for x, y in CN] + [('cone', 66, y) for _, y in CN])

if __name__ == '__main__': render(C, sys.argv)
