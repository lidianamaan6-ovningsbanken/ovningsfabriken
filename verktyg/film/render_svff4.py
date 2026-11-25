# SvFF-övningar efter skickade PDF:er, del 4. Regel: först d.mv, sedan d.carry; först mottagarens rörelse, sedan passningen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e9', __file__.replace('render_svff4.py', 'render_extern9.py'))
e9 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e9); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e9.finish, e9.rec, e9.chain, e9.wander, e9.counter, e9.arrivals
lab, hide, show, team, boxes, drive, shoot = e9.lab, e9.hide, e9.show, e9.team, e9.boxes, e9.drive, e9.shoot
factor, swap_color, stand, countdown, countup, win = e9.factor, e9.swap_color, e9.stand, e9.countdown, e9.countup, e9.win
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'

# ============ wj05 Spelarna först – lekmatch utan coachning ============
SV = ('svb',)
import math

# ============ svb140370 Futsal – Boll-jage (U7–U10) ============
d = Drill(); BX = (16, 18, 84, 82)
KP = [(28, 30), (70, 28), (30, 68), (72, 70), (50, 50)]
team(d, 'k', B, KP, [''] * 5); d.p('j', 'J', R, (50, 12))
balls = [d.newball(rec(d, f'k{k}', 0)) for k in range(5)]
for k in (0, 1, 4): wander(d, f'k{k}', 0, 17.9, BX, 700 + k, 1.2); d.carry(balls[k], f'k{k}', 0, 17.9)
wander(d, 'k3', 0, 6.0, BX, 703, 1.2); d.carry(balls[3], 'k3', 0, 6.0)
# jagaren tar bollen från k2 – k2 tar tillbaka den innan den är ute
wander(d, 'k2', 0, 2.6, BX, 702, 1.2); d.carry(balls[2], 'k2', 0, 2.6); d.mv('j', 0.4, 2.6, rec(d, 'k2', 2.6))
tw = d.pas(balls[2], 2.8, rec(d, 'j', 3.1), 0.3); t = drive(d, balls[2], 'j', 3.1, (24, 80), 14)
d.mv('k2', 3.1, t - 0.2, (26, 76)); tb = win(d, balls[2], 'k2', 'j', t, 0.2)                                   # tillbaka innan linjen
wander(d, 'k2', tb + 0.2, 17.9, BX, 712, 1.2); d.carry(balls[2], 'k2', tb + 0.2, 17.9)
# jagaren tar k3:s boll och driver ut den – k3 hjälper sedan till att jaga
d.mv('j', tb, 6.2, rec(d, 'k3', 6.2)); stand(d, 'k3', 6.0, 6.3); d.carry(balls[3], 'k3', 6.0, 6.3)
tw2 = d.pas(balls[3], 6.4, rec(d, 'j', 6.7), 0.3); t = drive(d, balls[3], 'j', 6.7, (92, 66), 16); tout = t; hide(d, balls[3], t + 0.3)
d.mv('k3', 6.7, t, (84, 64)); d.mv('k3', t, t + 2.0, rec(d, 'k1', t + 2.0)); wander(d, 'k3', t + 2.0, 17.9, BX, 713, 1.2)
d.mv('j', t, t + 2.0, (50, 50)); wander(d, 'j', t + 2.0, 17.9, BX, 714, 1.2)
fp = [(0, 'Alla utom en eller två har varsin boll', 'Driv mot fria ytor, ändra riktning och tempo.'),
      (tw - 0.2, 'Jagaren tar bollen – och driver mot linjen', 'Bryt mellan bollhållarens tillslag.'),
      (tb - 0.3, 'Ta tillbaka den innan den är ute!', 'Snabb omställning från försvar till anfall.'),
      (tout - 0.2, 'Utdriven – du hjälper till att jaga', '')]
finish(d, 'svb140370', 'futsal-boll-jage-u7-u10-svb140370', ['Futsal – Boll-jage', 'U7–U10'], 'Ca 6 spelare · Yta 15 × 8 m · Bollar och västar',
       fp, 'SPELUPPBYGGNAD', [('box', *BX)], [lab(tb, tb + 1.2, (36, 72), 'TILLBAKA!'), lab(tout, tout + 1.4, (80, 58), 'UTE')])
fc = factor(fp); C[-1]['players'][3]['color'] = (lambda tt, a=tout * fc: R if tt >= a else B)

# ============ svb140457 Futsal – Driva och skjuta (U7+) ============
d = Drill(); d.p('mv1', 'MV', YEL, (50, 6)); d.p('mv2', 'MV', YEL, (50, 94))
for k in range(3): d.p(f'n{k}', '', B, (36 - 4 * k, 94 + 0)); d.p(f's{k}', '', B, (64 + 4 * k, 6))
t = 0.4; ex = []
for rep, (pid, top) in enumerate([('n0', True), ('s0', False), ('n1', True), ('s1', False)]):
    bb = d.newball(rec(d, pid, t))
    cx, cy = (50, 40) if top else (50, 60)
    t1 = drive(d, bb, pid, t, (cx - 6 if top else cx + 6, cy + (8 if top else -8)), 16)
    t1 = drive(d, bb, pid, t1, (cx + (6 if top else -6), cy), 16)                                              # utmana konan – liten riktningsförändring
    gx = 44 if rep % 2 == 0 else 56; goal = (gx, 1) if top else (gx, 99)
    keeper = 'mv1' if top else 'mv2'; save = rep == 1
    if save: d.mv(keeper, t1, t1 + 0.6, (gx - 1.8, 7.2 if top else 93.2)); tg = d.pas(bb, t1 + 0.1, (gx, 6 if top else 94), 0.5); d.carry(bb, keeper, tg, tg + 0.4); hide(d, bb, tg + 0.5); ex.append(lab(tg, tg + 1.2, (gx, 16 if top else 84), 'RÄDDNING'))
    else: tg = shoot(d, bb, t1, goal); hide(d, bb, tg + 0.3); ex.append(lab(tg, tg + 1.2, (gx, 14 if top else 86), 'MÅL'))
    d.mv(pid, tg, tg + 2.4, (64 + 4 * (3 + rep), 6) if top else (36 - 4 * (3 + rep), 94)); d.mv(keeper, tg + 0.5, tg + 1.0, (50, 6 if top else 94))   # sist i ledet bakom det mål man skjutit mot
    t = t1 + 0.6
fp = [(0, 'Två led – ett vid varje mål', 'En spelare åt gången driver fram till konan.'),
      (1.2, 'Utmana konan – liten riktningsförändring', 'Bollen nära foten. Öka farten.'),
      (2.6, 'Skott: stödjefoten bredvid bollen, spänd fot', 'Målvakten: fånga med båda händerna eller stöt bort.'),
      (5.0, 'Ställ dig sist bakom målet du sköt mot', 'Byt stolpe efter en stund – skjut med andra foten.')]
finish(d, 'svb140457', 'futsal-driva-och-skjuta-u7-svb140457', ['Futsal – Driva och skjuta', 'U7+'], '8–10 spelare · Yta 20 × 12 m · Två mål med målvakter',
       fp, 'AVSLUT', [('box', 16, 4, 84, 96), ('cone', 50, 40), ('cone', 50, 60)], ex)
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ Par – behåll bollen (två futsalvarianter) ============
def pairs(id_, slug, title, setup, fp_text, seed, prog_lab):
    d = Drill(); BX = (14, 22, 86, 78)
    PR = [((30, 36), (36, 42)), ((70, 34), (64, 40)), ((32, 66), (38, 60)), ((70, 66), (64, 60))]
    for k, (a, f) in enumerate(PR): d.p(f'a{k}', '', B, a); d.p(f'f{k}', '', R, f)
    balls = [d.newball(rec(d, f'a{k}', 0)) for k in range(4)]
    for k, ((ax, ay), _) in enumerate(PR):
        box = (max(BX[0], ax - 16), max(BX[1], ay - 12), min(BX[2], ax + 16), min(BX[3], ay + 12))
        if k == 0:
            wander(d, 'a0', 0, 3.4, box, seed, 1.1); d.carry(balls[0], 'a0', 0, 3.4); d.mv('f0', 0.3, 3.2, rec(d, 'a0', 3.4))
            tw = d.pas(balls[0], 3.6, rec(d, 'f0', 3.9), 0.3)
            t = drive(d, balls[0], 'f0', 3.9, (box[2] - 2, box[1] + 2), 14)                                              # snabbt ifrån till fri yta
            d.mv('a0', 3.9, t, (box[2] - 6, box[1] + 6)); wander(d, 'f0', t, 17.9, box, seed + 1, 1.1); d.carry(balls[0], 'f0', t, 17.9)
            d.pl['a0']['tr'] += [(tt + 0.5, (x - 4, y + 4)) for tt, (x, y) in d.pl['f0']['tr'] if tt > t]
        else:
            wander(d, f'a{k}', 0, 17.9, box, seed + 10 + k, 1.1); d.carry(balls[k], f'a{k}', 0, 17.9)
            tr = d.pl[f'a{k}']['tr']; d.pl[f'f{k}']['tr'] = [(0, PR[k][1])] + [(tt + 0.6, (x + 4, y + 4)) for tt, (x, y) in tr if tt > 0]
    fp = [(0, *fp_text[0]), (1.0, *fp_text[1]), (tw - 0.2, *fp_text[2]), (tw + 2.0, *fp_text[3])]
    finish(d, id_, slug, title, setup, fp, 'SPELUPPBYGGNAD', [('box', *BX)], [lab(tw, tw + 1.4, (44, 30), prog_lab)])

pairs('svb140371', 'futsal-en-mot-en-i-yta-u7-u8-svb140371', ['Futsal – En mot en i yta', 'U7–U8'], 'Två och två med en boll · Yta ca 15 × 8 m',
      [('Två och två med en boll', 'Bollhållaren täcker, driver och fintar.'),
       ('Kroppen mellan motspelaren och bollen', 'Gärna snedställd – använd sulan.'),
       ('Försvararen bryter – byt roller', 'Finta för att skapa tid, titta upp.'),
       ('Progression: två lag', 'Flest bollar under kontroll efter en viss tid vinner.')], 720, 'BYT ROLL')

pairs('svb140092', 'futsal-behalla-bollen-u7-u12-svb140092', ['Futsal – Behålla bollen', 'U7–U12'], 'Två och två med en boll · Yta 12–15 × 7–10 m',
      [('Två och två med en boll', 'Driv bort från motspelaren och skydda bollen.'),
       ('Riktningsförändring och tempoökning', 'Kroppen mellan motspelare och boll, sulan för kontroll.'),
       ('Bollen tagen – ta dig snabbt till fri yta', 'Den som tappade försöker ta tillbaka den.'),
       ('Byt motspelare efter en stund', 'Jagaren: bryt mellan tillslagen.')], 740, 'TAGEN!')

# ============ svb140093 Futsal – Fyra sidor (U7–U10) ============
d = Drill(); d.p('t', 'T', T_COL, (96, 94))
SIDE = {'TOPP': (50, 14), 'HÖGER': (86, 50), 'BOTTEN': (50, 86), 'VÄNSTER': (14, 50)}
KP = [(36, 40), (60, 38), (44, 58), (64, 60), (52, 48)]
team(d, 'k', B, KP, [''] * 5)
balls = [d.newball(rec(d, f'k{k}', 0)) for k in range(5)]
calls = [('”BRASILIEN!”', 'TOPP', 0.6), ('”SVERIGE!”', 'HÖGER', 4.0), ('”JAPAN!”', 'VÄNSTER', 6.4), ('”SPANIEN!”', 'BOTTEN', 9.6)]
ex = []
for ci, (txt, side, tc) in enumerate(calls):
    ex.append(lab(tc, tc + 1.4, (80, 94), txt)); sx, sy = SIDE[side]; tnext = calls[ci + 1][2] if ci + 1 < len(calls) else 13.6
    for k in range(5):
        tgt = (sx + (k - 2) * 7 if side in ('TOPP', 'BOTTEN') else sx, sy + (k - 2) * 7 if side in ('HÖGER', 'VÄNSTER') else sy)
        if ci == 2:   # nytt namn innan de hunnit fram – vänd med sulan
            mid = ((d.pos(f'k{k}')[0] + tgt[0]) / 2, (d.pos(f'k{k}')[1] + tgt[1]) / 2)
            t1 = drive(d, balls[k], f'k{k}', tc + 0.3, mid, 16); d.mv(f'k{k}', t1, t1 + 0.3, mid); d.carry(balls[k], f'k{k}', t1, t1 + 0.3)
        else: drive(d, balls[k], f'k{k}', tc + 0.3 + 0.05 * k, tgt, 16 + k % 2)
    if ci == 2: ex.append(lab(tc + 1.4, tc + 2.6, (50, 50), 'VÄND!'))
fp = [(0, 'Alla har varsin boll – fyra sidor med namn', 'Tränaren ropar ett namn.'),
      (1.0, 'Driv till den sidan', 'Bollen nära foten, sulan för att stoppa.'),
      (6.4, 'Progression: nytt namn innan ni kommit fram', 'Vänd med sulan, insidan eller utsidan.'),
      (9.8, 'Titta upp – var är de andra?', 'Träna olika sorters vändningar.')]
finish(d, 'svb140093', 'futsal-fyra-sidor-u7-u10-svb140093', ['Futsal – Fyra sidor', 'U7–U10'], 'Yta 10–12 × 8–10 m · Varsin boll',
       fp, 'SPELUPPBYGGNAD', [('box', 10, 10, 90, 90), ('text', 50, 6, 'BRASILIEN'), ('text', 96, 30, 'SVERIGE'), ('text', 50, 96, 'SPANIEN'), ('text', 4, 30, 'JAPAN')], ex)

# ============ svb140448 Futsal – Skjuta, rulla och kasta i mål ============
d = Drill(); d.p('mv', '', YEL, (200, 200)) if False else None
SP = [(32, 50), (46, 54), (58, 54), (70, 50)]
team(d, 's', B, SP, [''] * 4); ex = []
KIND = ['SKJUTA', 'KASTA', 'RULLA']
t = 0.4
for r, kind in enumerate(KIND):
    for k in range(4):
        bb = d.newball((200, 200)); dist = 0 if r == 0 else (8 if r == 1 else -6)
        y0 = SP[k][1] + dist; d.mv(f's{k}', t - 0.6, t - 0.1, (SP[k][0], y0)); show(d, bb, t - 0.1, rec(d, f's{k}', t - 0.1))
        gx = 40 + 6 * k; tg = d.pas(bb, t, (gx, 2), 0.7 if kind != 'RULLA' else 1.0); hide(d, bb, tg + 0.3); t += 0.45
    ex.append(lab(t - 1.8, t + 0.6, (50, 76), kind)); t += 0.9
fp = [(0, 'Alla har varsin boll framför målet', 'Bollen ska gå i mål utan att studsa före mållinjen.'),
      (0.6, 'Skjuta: stödjefoten bredvid bollen', 'Spänn foten.'),
      (2.9, 'Kasta: handbollskast med en hand', 'Variera avståndet till målet.'),
      (5.2, 'Rulla: greppa, kliv fram, böj knät', 'Släpp bollen längs golvet.')]
finish(d, 'svb140448', 'futsal-skjuta-rulla-och-kasta-i-mal-u7-u12-svb140448', ['Futsal – Skjuta, rulla och kasta', 'I mål · U7–U12'], 'Ca 4 spelare · Ett mål · Varsin boll',
       fp, 'LEK', [], ex)
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ svb140083 Futsal – Bowling (U7–U10) ============
d = Drill()
TRI = [(50, 26), (44, 34), (56, 34), (38, 42), (50, 42), (62, 42)]
pins = [d.newball(q) for q in TRI]
for k in range(3): d.p(f'p{k}', '', B, (40 + 10 * k, 84))
ex = []; t = 0.6
rolls = [('p0', [0, 1, 4], 'SPÄRR?'), ('p1', [2, 3, 5], 'SPÄRR!')]
roll_t = []
for pi, (pid, hits, txt) in enumerate(rolls):
    bb = d.newball(rec(d, pid, t - 0.1)); d.mv(pid, t - 0.4, t, (d.pos(pid)[0], 80))                                # utfallssteg
    th = d.pas(bb, t, (TRI[hits[0]][0], TRI[hits[0]][1] + 4), 1.1); roll_t.append(th)
    for hi in hits:
        hx, hy = TRI[hi]; d.pas(pins[hi], th + 0.05 * hi, (hx + (hx - 50) * 0.6 + 2, hy - 8), 0.5)
    d.pas(bb, th, (TRI[hits[0]][0], 10), 0.6); hide(d, bb, th + 0.8); t = th + 1.6
ex = [lab(roll_t[0], roll_t[0] + 1.4, (74, 30), '3 NERE'), lab(roll_t[1], roll_t[1] + 1.6, (74, 30), 'SPÄRR!')]
fp = [(0, 'Sex bollar på koner i en triangel', 'Rulla din boll från linjen.'),
      (0.6, 'Bollen mellan handen och underarmen', 'Kliv fram med motsatt ben i ett utfallssteg.'),
      (roll_t[0] + 0.4, 'Två försök per spelare och omgång', 'Alla ner på första = strike, på andra = spärr.'),
      (roll_t[1] + 0.6, 'Variera: kasta, passa eller skjut', 'Precision som vid igångsättning från målvakt.')]
finish(d, 'svb140083', 'futsal-bowling-u7-u10-svb140083', ['Futsal – Bowling', 'U7–U10'], 'Max 6 spelare · Yta ca 8 × 5 m · Bollar på koner',
       fp, 'LEK', [('cone', x, y + 2) for x, y in TRI] + [('line', [(28, 78), (72, 78)])], ex)
C[-1]['_stuck'] = True

# ============ svb140360 Futsal – Räkor och krabbor (U7–U12) ============
d = Drill()
RK = [(26, 88), (42, 88), (58, 88), (74, 88)]; KR = [(36, 50), (64, 52)]
team(d, 'r', B, RK, ['R'] * 4); team(d, 'c', R, KR, ['K', 'K'])
balls = [d.newball(rec(d, f'r{k}', 0)) for k in range(4)]
for k, (x, y) in enumerate(RK):
    if k == 2:
        t = drive(d, balls[k], 'r2', 0.6, (60, 60), 12); d.mv('c1', 0.6, t, (62, 54)); tw = d.pas(balls[k], t + 0.2, rec(d, 'c1', t + 0.5), 0.3)
        d.carry(balls[k], 'c1', t + 0.5, t + 1.6); d.mv('r2', t + 0.4, t + 1.6, (60, 66)); tl = t
        continue
    pts = [(x + (8 if k % 2 else -8), 60), (x, 40), (x, 12)]; t = 0.6 + 0.2 * k
    for q in pts: t = drive(d, balls[k], f'r{k}', t, q, 12)
d.mv('c0', 0.6, 3.0, (32, 54)); d.mv('c0', 3.0, 5.0, (40, 50))                                                     # krabbor rör sig långsamt
fp = [(0, 'Räkor driver från kortsida till kortsida', 'Krabborna försöker ta bollen.'),
      (1.2, 'Krabborna går i krabbställning', 'Bollen nära foten – titta upp efter lediga ytor.'),
      (tl - 0.2, 'Tappar en räka bollen …', '… blir den krabba i nästa omgång.'),
      (tl + 1.6, 'Variant: krabborna hoppar på ett ben', 'Byt ben varje omgång. Lättare: nudda räkorna.')]
finish(d, 'svb140360', 'futsal-rakor-och-krabbor-u7-u12-svb140360', ['Futsal – Räkor och krabbor', 'U7–U12'], 'Ca 6 spelare · Yta 10–12 × 7–8 m · Bollar',
       fp, 'SPELUPPBYGGNAD', [('box', 14, 8, 86, 92), ('line', [(14, 8), (86, 8)]), ('line', [(14, 92), (86, 92)])], [lab(tw, tw + 1.4, (72, 46), 'TAGEN!')])

if __name__ == '__main__': render(C, sys.argv)
