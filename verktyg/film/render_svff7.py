# SvFF-övningar efter skickade PDF:er, del 7. Regel: först d.mv, sedan d.carry; först mottagarens rörelse, sedan passningen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e9', __file__.replace('render_svff7.py', 'render_extern9.py'))
e9 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e9); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e9.finish, e9.rec, e9.chain, e9.wander, e9.counter, e9.arrivals
lab, hide, show, team, boxes, drive, shoot = e9.lab, e9.hide, e9.show, e9.team, e9.boxes, e9.drive, e9.shoot
factor, swap_color, stand, countdown, countup, win = e9.factor, e9.swap_color, e9.stand, e9.countdown, e9.countup, e9.win
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'

# ============ wj05 Spelarna först – lekmatch utan coachning ============
SV = ('svb',)
import math
_finish = finish
def finish(d, *a, **k):
    if not d.balls: d.balls.append([(0, (130, 0)), (14.0, (131, 0))])   # osynlig boll: utan boll ska övningen inte upprepas
    return _finish(d, *a, **k)
def tails(idx, fn): C[-1]['players'][idx]['tails'] = fn
def color_at(idx, fn): C[-1]['players'][idx]['color'] = fn
BOX = (10, 12, 90, 88)

# ============ svb89718 Ö1 – Förberedelseträning ============
d = Drill(); KP = [(24, 28), (70, 26), (30, 70), (74, 72), (50, 50), (46, 24)]
team(d, 'k', B, KP, [''] * 6); balls = []
T1 = 7.4
for k in range(6):
    wander(d, f'k{k}', 0, T1, BOX, 900 + k, 1.4); bb = d.newball(rec(d, f'k{k}', 0)); tr = d.balls[bb]; t = 0.2
    hts = [7, 4, 2, 1]
    while t + 0.3 < T1:
        x, y = at(d.pl[f'k{k}']['tr'], t); h = hts[int(t / 1.85) % 4]
        tr += [(t, (x + 1.8, y - 1.2)), (t + 0.3, (x + 1.8, y - 1.2 - h))]; t += 0.6
    balls.append(bb)
PAIRS = [(0, 1), (2, 3), (4, 5)]; PP = [((22, 30), (44, 30)), ((24, 66), (46, 66)), ((60, 48), (80, 48))]
for (a, c), (pa, pc) in zip(PAIRS, PP):
    d.mv(f'k{a}', T1, T1 + 1.2, pa); d.mv(f'k{c}', T1, T1 + 1.2, pc); d.balls[balls[c]] += [(T1, at(d.balls[balls[c]], T1)), (T1 + 0.01, (200, 200))]
    bb = balls[a]; d.balls[bb] += [(T1 + 1.2, rec(d, f'k{a}', T1 + 1.2))]; t = T1 + 1.4
    for rep in range(4): t = d.pas(bb, t + 0.3, rec(d, f'k{c}' if rep % 2 == 0 else f'k{a}', t + 1.0), 0.7)
fp = [(0, 'Alla har var sin boll', 'Spring runt, studsa, kasta och fånga.'),
      (0.4, 'Fånga i olika höjd', 'Över huvudet, i brösthöjd, i knähöjd, nära marken.'),
      (T1, 'I par med en boll', 'Kasta eller rulla till varandra – längs marken, i luften, med studs.'),
      (T1 + 3.0, 'Följsamma och rytmiska rörelser', '')]
finish(d, 'svb89718', 'o1-forberedelsetraning-forhindra-och-radda-avslut-svb89718', ['Ö1 – Förberedelseträning', 'Förhindra och rädda avslut'],
       'Alla har var sin boll · Yta 20 × 20 m', fp, 'MÅLVAKT', [('box', *BOX)],
       [lab(0.2 + i * 1.85, 0.2 + (i + 1) * 1.85, (50, 94), t_) for i, t_ in enumerate(['ÖVER HUVUDET', 'BRÖSTHÖJD', 'KNÄHÖJD', 'NÄRA MARKEN'])])
C[-1]['_stuck'] = True

# ============ 3 mot 3 med målvakter (två varianter) ============
def mv33(id_, slug, title, setup, caps, seed):
    d = Drill(); d.p('mvr', 'MV', R, (50, 6)); d.p('mvb', 'MV', B, (50, 94))
    BP = [(30, 68), (70, 66), (50, 54)]; RP = [(34, 34), (66, 32), (50, 46)]
    team(d, 'b', B, BP); team(d, 'r', R, RP); ex = []
    b = d.newball(rec(d, 'mvb', 0))
    t = d.pas(b, 0.4, rec(d, 'b0', 1.2), 0.8); t = chain(d, b, t, ['b2', 'b1'], 0.3); t = drive(d, b, 'b1', t, (64, 26), 16)
    d.mv('mvr', t - 0.3, t + 0.3, (56.2, 7.2)); tc = d.pas(b, t + 0.1, (58, 6), 0.5); d.carry(b, 'mvr', tc, tc + 0.6); ex.append(lab(tc, tc + 1.2, (72, 12), 'FÅNGAD'))
    t = d.pas(b, tc + 0.8, rec(d, 'r0', tc + 1.6), 0.8) if seed else d.pas(b, tc + 0.8, rec(d, 'r1', tc + 1.6), 0.8)
    who = 'r0' if seed else 'r1'; t = drive(d, b, who, t, (44 if seed else 58, 70), 16)
    d.mv('mvb', t - 0.4, t + 0.1, (40, 94)); tg = d.pas(b, t + 0.1, (58 if seed else 42, 99), 0.4); hide(d, b, tg + 0.3); ex.append(lab(tg, tg + 1.2, (66, 84), 'MÅL'))
    d.mv('mvr', tg + 0.4, tg + 2.0, (30, 34)); d.mv('r0', tg + 0.4, tg + 2.0, (50, 8))                               # byt målvakt
    fp = [(0, *caps[0]), (1.4, *caps[1]), (tc - 0.3, *caps[2]), (tg + 0.4, *caps[3])]
    finish(d, id_, slug, title, setup, fp, 'MÅLVAKT', [('box', 14, 4, 86, 96)], ex)
    C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True
mv33('svb201', 'malvakt-c-6-9-ar-skott-radda-avslut-so-2-svb201', ['Målvakt C – 6–9 år', 'Skott – rädda avslut (SÖ 2)'], '8 barn · Spelplan 25 × 20 m · Två mål',
     [('Spel 3 mot 3 med målvakter', 'Gör flera planer om ni är många.'), ('Hindra motståndarna att göra mål', ''),
      ('Målvakten fångar bollen', 'Fånga längs marken eller lås bollen mot kroppen.'), ('Byt målvakt efter några minuter', '')], 1)
mv33('svb312', 'spelovning-1-skott-radda-avslut-mv-svb312', ['Spelövning 1 – skott', 'Rädda avslut (MV)'], '8 barn · Spelplan 25 × 20 m · Två mål',
     [('Två lag – spel 3 mot 3 med målvakter', 'Fler planer ger hög aktivitet för alla.'), ('Hindra motståndarna att göra mål', ''),
      ('Stå upp och fånga – eller kasta dig', 'Lås bollen direkt mot kroppen.'), ('Byt målvakt efter några minuter', '')], 0)

# ============ svb198 Målvakt C – greppteknik, fånga avslut längs marken ============
d = Drill(); d.p('a', 'A', YEL, (50, 22)); d.p('b', 'B', B, (50, 78)); t = 0.6; ex = []
for k, (sh, kp) in enumerate([('a', 'b'), ('b', 'a'), ('a', 'b'), ('b', 'a')]):
    bb = d.newball(rec(d, sh, t - 0.2) if k == 0 else (200, 200))
    if k: show(d, bb, t - 0.1, rec(d, sh, t - 0.1))
    gy = 78 if kp == 'b' else 22; gx = 50 + (-4 if k % 2 else 4)
    d.mv(kp, t + 0.3, t + 0.9, (gx - 1.8, gy + 1.2)); tc = d.pas(bb, t + 0.1, (gx, gy), 0.9); d.carry(bb, kp, tc, tc + 1.0); hide(d, bb, tc + 1.1)
    ex.append(lab(tc, tc + 1.0, (gx + 14, gy), 'FÅNGA')); d.mv(kp, tc + 1.1, tc + 1.8, (50, gy)); t = tc + 1.9
fp = [(0, 'A skjuter längs marken till B som fångar', 'Sedan tvärtom.'), (1.4, 'Nå marken med händerna', 'Lås bollen mot överkroppen.'),
      (4.4, 'Bra balans', 'Försök undvika returer.'), (t - 1.2, 'Rädda avslut och undvik returer', '')]
finish(d, 'svb198', 'malvakt-c-6-9-ar-greppteknik-fanga-avslut-langs-marken-svb198', ['Målvakt C – 6–9 år', 'Greppteknik – fånga längs marken'],
       '2 barn · Två mål (eller konmål) 5–8 m isär · Bollar', fp, 'MÅLVAKT', [('ugoal', 50, 20, 'up'), ('ugoal', 50, 80, 'down'), ('cone', 34, 20), ('cone', 66, 20), ('cone', 34, 80), ('cone', 66, 80)], ex)

# ============ svb140364 Futsal – Par-jage ============
d = Drill(); BX = (14, 22, 86, 78)
KP = [(28, 34), (70, 30), (30, 68), (72, 70), (50, 60), (58, 40)]
team(d, 'k', B, KP, [''] * 6); d.p('j0', '', R, (46, 48)); d.p('j1', '', R, (50, 48))
for k in (0, 1, 3, 5): wander(d, f'k{k}', 0, 17.9, BX, 910 + k, 1.2)
d.mv('j0', 0.4, 3.0, (30, 62)); d.mv('j1', 0.4, 3.0, (34, 62)); d.mv('k2', 0, 3.0, (30, 66)); tc = 3.0                  # tagen – håller i handen
d.mv('k2', tc, tc + 0.4, (38, 62)); d.mv('k4', 0, 6.4, (66, 54))
for pid, dx in [('j0', 0), ('j1', 4), ('k2', 8)]: d.mv(pid, tc + 0.4, 6.4, (56 + dx, 54))
d.mv('k4', 6.4, 6.6, (68, 54)); tc2 = 6.6
for pid, q in [('j0', (34, 36)), ('j1', (38, 36)), ('k2', (60, 66)), ('k4', (64, 66))]: d.mv(pid, tc2 + 0.4, tc2 + 2.0, q)   # fyra – delar sig i två par
for i, (a, c) in enumerate([('j0', 'j1'), ('k2', 'k4')]):
    wander(d, a, tc2 + 2.0, 17.9, BX, 930 + i, 1.4); tr = d.pl[a]['tr']; d.pl[c]['tr'] += [(t, (x + 4, y)) for t, (x, y) in tr if t > tc2 + 2.0]
fp = [(0, 'Två jägare håller varandra i händerna', 'Tillsammans jagar de de andra.'),
      (tc - 0.2, 'Tagen? Håll i handen och jaga med', 'Samma om du springer utanför ytan.'),
      (tc2 - 0.2, 'Fyra jägare – dela er i två par', 'Kommunicera och samarbeta.'),
      (tc2 + 2.4, 'Den som är ensam kvar vinner', 'Rör dig mot fria ytor, öka farten, ändra riktning.')]
finish(d, 'svb140364', 'futsal-par-jage-u7-svb140364', ['Futsal – Par-jage', 'U7+'], 'Minst 6 spelare · Yta 10–12 × 7 m', fp, 'LEK', [('box', *BX)],
       [lab(tc, tc + 1.2, (24, 56), 'TAGEN!'), lab(tc2, tc2 + 1.2, (76, 46), 'TAGEN!'), lab(tc2 + 0.6, tc2 + 2.2, (50, 50), 'DELA!')])
fc = factor(fp); color_at(4, lambda tt, a=tc * fc: R if tt >= a else B); color_at(6, lambda tt, a=tc2 * fc: R if tt >= a else B)

# ============ svb140357 Futsal – Motorikstopp ============
d = Drill(); d.p('t', 'T', T_COL, (96, 50)); BX = (14, 20, 86, 80)
KP = [(26, 30), (70, 28), (30, 70), (72, 70), (50, 50), (48, 28)]; team(d, 'k', B, KP, [''] * 6)
CALLS = [(2.4, '”1!” – STÅ PÅ ETT BEN', 'stop'), (4.4, '”2!” – SPRING', 'run'), (6.6, '”3!” – HOPPA JÄMFOTA', 'hop'), (8.8, '”4!” – PÅ RYGG', 'stop'), (11.0, 'VARIANT: VISA FÄRG', 'run')]
for k in range(6):
    wander(d, f'k{k}', 0, 2.4, BX, 940 + k, 1.0); t = 2.4
    for i, (tc, _, kind) in enumerate(CALLS):
        nxt = CALLS[i + 1][0] if i + 1 < len(CALLS) else 14.0
        if kind == 'run': wander(d, f'k{k}', tc, nxt, BX, 950 + 10 * i + k, 1.0)
        elif kind == 'hop':
            x, y = d.pos(f'k{k}'); tt = tc
            while tt < nxt - 0.3: d.mv(f'k{k}', tt, tt + 0.2, (x, y - 1.5)); d.mv(f'k{k}', tt + 0.2, tt + 0.4, (x, y)); tt += 0.4
        else: stand(d, f'k{k}', tc, nxt)
fp = [(0, 'Alla springer i ytan', 'Tränaren ropar en siffra.'), (2.4, '1 – stå på ett ben · 2 – spring', ''),
      (6.6, '3 – hoppa jämfota · 4 – lägg dig på rygg', 'Låt barnen hitta på egna rörelser.'), (11.0, 'Variant: visa en färg i stället', 'Då måste barnen titta upp.')]
finish(d, 'svb140357', 'futsal-motorikstopp-u7-u12-svb140357', ['Futsal – Motorikstopp', 'U7–U12'], 'Ca 6 spelare · Yta ca 15 × 8 m', fp, 'LEK',
       [('box', *BX)], [lab(tc, tc + 1.6, (50, 90), txt) for tc, txt, _ in CALLS])

# ============ svb140374 Futsal – Svansleken (U7–U12) ============
d = Drill(); BX = (14, 22, 86, 78)
KP = [(26, 32), (70, 30), (30, 68), (72, 70), (52, 60)]; team(d, 'k', B, KP, [''] * 5); d.p('j', '', R, (50, 46))
for k in (0, 1, 3): wander(d, f'k{k}', 0, 17.9, BX, 960 + k, 1.2)
d.mv('j', 0.4, 2.8, (30, 62)); d.mv('k2', 0, 2.8, (26, 64)); tc = 2.8
wander(d, 'k2', tc + 0.2, 6.4, BX, 970, 1.2); d.mv('k2', 6.4, 7.4, (58, 64)); d.mv('k4', 0, 7.4, (62, 66)); tc2 = 7.4
wander(d, 'j', tc + 0.3, 17.9, BX, 971, 1.4); wander(d, 'k2', tc2 + 0.3, 17.9, BX, 972, 1.4); wander(d, 'k4', tc2 + 0.3, 17.9, BX, 973, 1.2)
fp = [(0, 'Alla har en väst som svans', 'En spelare jagar och drar loss svansar.'), (tc - 0.2, 'Svansen tagen – hjälp till att jaga', ''),
      (5.0, 'Fria ytor, byt riktning och öka farten', 'Jägarna samarbetar.'), (tc2 - 0.2, 'Fler jägare – färre svansar', '')]
finish(d, 'svb140374', 'futsal-svansleken-u7-u12-svb140374', ['Futsal – Svansleken', 'U7–U12'], 'Ca 6 spelare · Yta 10–12 × 7 m · Västar', fp, 'LEK',
       [('box', *BX)], [lab(tc, tc + 1.2, (22, 56), 'TAGEN!'), lab(tc2, tc2 + 1.2, (66, 58), 'TAGEN!')])
fc = factor(fp)
for i, tt0 in [(2, tc), (4, tc2)]:
    color_at(i, lambda tt, a=tt0 * fc: R if tt >= a else B); tails(i, lambda tt, a=tt0 * fc: 0 if tt >= a else 1)
for i in (0, 1, 3): tails(i, lambda tt: 1)

# ============ svb140359 Futsal – Kängurustafett ============
d = Drill(); ex = []
for tm, x, col in (('b', 34, B), ('r', 66, R)):
    for k in range(3): d.p(f'{tm}{k}', '', col, (x, 86 + 4 * k) if k else (x, 82))
for tm, x in (('b', 34), ('r', 66)):
    t = 0.5 + (0.3 if tm == 'r' else 0)
    for k in range(3):
        pid = f'{tm}{k}'
        if k: d.mv(pid, t - 0.8, t, (x, 82))
        y = 82
        for step in range(8): d.mv(pid, t, t + 0.25, (x + (1 if step % 2 else -1), y - 7)); y -= 7; t += 0.32       # hoppa jämfota
        d.mv(pid, t, t + 0.4, (x + 4, 24)); t += 0.4
        for step in range(8): d.mv(pid, t, t + 0.25, (x + 4 + (1 if step % 2 else -1), y + 7)); y += 7; t += 0.32
        d.mv(pid, t, t + 0.5, (x + 10, 90 + 3 * k)); t += 0.3
    if tm == 'b': ex.append(lab(t, t + 1.6, (x, 70), 'KLART!'))
fp = [(0, 'Lag om tre–fyra, två bollar per lag', 'En boll mellan knäna, en i händerna.'), (1.2, 'Hoppa jämfota som en känguru', 'Runda konen och hoppa tillbaka.'),
      (4.0, 'Tappar du en boll – ta upp den och fortsätt', ''), (7.5, 'Nästa i laget hoppar', 'Koordination och spänst.')]
finish(d, 'svb140359', 'futsal-kangurustafett-u7-u10-svb140359', ['Futsal – Kängurustafett', 'U7–U10'], 'Ca 6 spelare · Sträcka 5–8 m · Koner', fp, 'LEK',
       [('cone', 38, 22), ('cone', 70, 22), ('line', [(20, 84), (80, 84)])], ex)

# ============ svb142864 Futsal – Gladiatorerna ============
d = Drill()
RUN = [(24, 90), (38, 90), (52, 90), (66, 90), (80, 90)]
team(d, 'k', B, RUN, [''] * 5); team(d, 'l', R, [(6, 34), (6, 62), (94, 46)], ['L', 'L', 'L']); ex = []
for k, (x, y) in enumerate(RUN): d.path(f'k{k}', 1.0 + 0.1 * k, [(x + (6 if k % 2 else -6), 66), (x + (-4 if k % 2 else 4), 40), (x, 10)], 1.1)
for li, (lid, tgt, tt) in enumerate([('l0', 'k1', 2.0), ('l2', 'k3', 2.6), ('l1', 'k0', 3.2)]):
    bb = d.newball(rec(d, lid, 0)); tx, ty = at(d.pl[tgt]['tr'], tt + 0.6); th = d.pas(bb, tt, (tx + 6 if li == 0 else tx - 1, ty + 2), 0.6); hide(d, bb, th + 0.6)
    if li == 1: ex.append(lab(th, th + 1.4, (tx, ty - 8), 'TRÄFF!')); thit = th
    else: ex.append(lab(th, th + 1.0, (tx, ty - 8), 'MISS'))
d.mv('k3', thit + 1.5, thit + 3.6, (94, 70))
fp = [(0, 'Alla på ena kortsidan', 'Ledare med bollar längs långsidorna.'), (1.0, 'Spring över utan att bli träffad', 'Ändra riktning och fart, eller hoppa.'),
      (thit - 0.2, 'Träffad under knät? Du blir ledare', 'Ledarna passar med bredsidan och siktar lite framför.'), (thit + 1.8, 'Tills en spelare är kvar', 'Variant: rulla bollarna.')]
finish(d, 'svb142864', 'futsal-gladiatorerna-u7-u10-svb142864', ['Futsal – Gladiatorerna', 'U7–U10'], 'Spelare och bollar · Yta ca 15 × 8 m', fp, 'LEK', [('box', 12, 6, 88, 94)], ex)
fc = factor(fp); color_at(3, lambda tt, a=thit * fc: R if tt >= a else B)

# ============ svb122289 1 mot 1 med avslut ============
d = Drill(); d.p('mvr', 'MV', R, (50, 6)); d.p('mvb', 'MV', B, (50, 94))
d.p('bh', '', B, (16, 70)); d.p('a', 'A', B, (84, 58)); d.p('f', 'F', R, (88, 40)); d.p('q', '', B, (16, 78)); d.p('w', '', R, (90, 32))
b = d.newball(rec(d, 'bh', 0)); ex = []
t = d.pas(b, 0.5, rec(d, 'a', 1.6), 1.1); d.mv('f', 0.6, t + 0.4, (62, 40)); d.mv('bh', 1.2, 3.2, (24, 90))                                                 # försvararen in när passningen slås
d.mv('a', t, t + 0.4, (78, 52)); d.carry(b, 'a', t, t + 0.4); t = drive(d, b, 'a', t + 0.4, (66, 40), 14)
t = drive(d, b, 'a', t, (56, 26), 16); d.mv('f', t - 1.0, t, (60, 30)); d.mv('mvr', t - 0.4, t, (54, 8))
tg = shoot(d, b, t + 0.05, (44, 1)); hide(d, b, tg + 0.3); ex.append(lab(tg, tg + 1.2, (44, 12), 'MÅL'))
d.mv('a', tg + 0.3, tg + 2.2, (16, 86)); d.mv('f', tg + 0.3, tg + 2.2, (90, 24)); d.mv('q', tg + 0.4, tg + 1.4, (16, 70))
b2 = d.newball((200, 200)); show(d, b2, tg + 1.4, rec(d, 'q', tg + 1.4)); d.mv('w', tg + 1.4, tg + 2.2, (88, 40)); d.p('a2', 'A', B, (84, 62))
t = d.pas(b2, tg + 1.6, rec(d, 'a2', tg + 2.7), 1.1); d.mv('w', tg + 1.7, t + 0.4, (72, 50)); tw = win(d, b2, 'w', 'a2', t + 0.8, 0.6)
t = drive(d, b2, 'w', tw, (56, 78), 16); tg2 = shoot(d, b2, t, (56, 99)); hide(d, b2, tg2 + 0.3)
fp = [(0, 'Bollhållaren passar till andra sidan', 'Försvararen får gå in när passningen slås.'), (1.6, 'Ta in bollen – utmana en mot en', 'Riktningsförändring och tempoväxling.'),
      (tg - 0.4, 'Passera och gör mål', 'Målvakten styr försvararen och fångar eller stöter bort.'), (tw - 0.2, 'Försvaret erövrar – ställ om till anfall', 'Nya spelare in när bollen går ur spel.')]
finish(d, 'svb122289', '1-mot-1-med-avslut-svb122289', ['1 mot 1', 'med avslut'], '6–12 spelare · Dubbla straffområden · Två mål', fp, 'AVSLUT', [('box', 10, 4, 90, 96)],
       ex + [lab(tw, tw + 1.2, (78, 56), 'BOLLVINST')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ svb48731 SvFF D – Spelövning (spelform 5v5) ============
d = Drill(); d.p('mvr', 'MV', R, (50, 6)); d.p('mvb', 'MV', B, (50, 94))
team(d, 'b', B, [(34, 66), (66, 62)]); team(d, 'r', R, [(38, 34), (62, 30)])
b = d.newball(rec(d, 'mvr', 0)); ex = []
for k, q in enumerate([(36, 58), (62, 60)]): d.mv(f'b{k}', 0.2, 1.4, q)                                                     # retreat bakom mittlinjen
t = d.pas(b, 0.6, rec(d, 'r0', 1.6), 1.0); t = drive(d, b, 'r0', t, (36, 56), 14); d.mv('b0', t - 1.0, t, (38, 64))
tw = win(d, b, 'b0', 'r0', t + 0.4, 0.6); d.mv('b1', tw - 0.4, tw + 0.8, (66, 40)); t = d.pas(b, tw + 0.3, rec(d, 'b1', tw + 1.0))
t = drive(d, b, 'b1', t, (60, 20), 16); d.mv('mvr', t - 0.4, t, (56, 8)); tg = shoot(d, b, t + 0.05, (44, 1)); hide(d, b, tg + 0.3); ex.append(lab(tg, tg + 1.2, (44, 12), 'MÅL'))
fp = [(0, 'Spel 2 mot 2 med målvakter', '5 mot 5-regler med mittlinjen som retreatlinje.'), (0.6, 'Målvakten spelar ut – motståndarna backar', 'Rulla, kasta eller passa till fri medspelare.'),
      (tw - 0.2, 'Pressa, bryt – ta bollen framåt', 'Tempoväxla och riktningsförändra.'), (tg - 0.4, 'Avslut', 'Byten efter 1–2 minuter.')]
finish(d, 'svb48731', 'svff-d-spelovning-spelform-5v5-svb48731', ['SvFF D – Spelövning', 'Spelform 5 mot 5'], '6–11 spelare · Yta 20 × 15 m · Två mål', fp, 'SPELUPPBYGGNAD',
       [('box', 14, 4, 86, 96), ('line', [(14, 50), (86, 50)])], ex + [lab(0.4, 1.6, (76, 54), 'RETREAT')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ svb122274 Dubbelkvadrat ============
d = Drill()
BP = [(26, 30), (60, 24), (40, 44), (70, 42)]; RP = [(36, 32), (54, 36), (64, 30)]; JP = [(4, 26), (96, 34), (50, 2)]
team(d, 'b', B, BP); team(d, 'r', R, RP); team(d, 'j', YEL, JP, ['J', 'J', 'J'])
b = d.newball(rec(d, 'b0', 0)); cnt = []
t = chain(d, b, 0.4, ['j0', 'b2', 'b1', 'j1', 'b3'], 0.25); cnt = arrivals(d, b)[:5]
tw = win(d, b, 'r2', 'b3', t + 0.4, 0.7); t = d.pas(b, tw + 0.3, (54, 70), 1.0); d.mv('r1', tw, t, (52, 72)); d.carry(b, 'r1', t, t + 0.3); tsw = t
for k, q in enumerate([(30, 64), (66, 78), (70, 62)]): d.mv(f'r{k}', tw + 0.2, tsw + 1.2, q) if k != 1 else None
for k, q in enumerate([(30, 56), (56, 60), (46, 70), (66, 58)]): d.mv(f'b{k}', tw + 0.4, tsw + 1.6, q)
d.mv('j0', tw, tsw + 1.4, (4, 70)); d.mv('j1', tw, tsw + 1.4, (96, 66)); d.mv('j2', tw, tsw + 1.4, (50, 98))
t = chain(d, b, tsw + 0.6, ['r0', 'j0', 'r2'], 0.25)
fp = [(0, 'Tre lag – två spelar, ett är jokrar', 'Jokrarna är alltid med laget som har bollen, max två tillslag.'),
      (1.4, 'Behåll bollen på er planhalva', 'Orientera dig, använd första tillslaget.'),
      (tw - 0.2, 'Bollvinst – flytta spelet till andra planhalvan', 'Där försöker det nya laget behålla bollen.'),
      (tsw + 1.0, 'Återerövra efter bollförlust', 'Passa när medspelaren är redo.')]
finish(d, 'svb122274', 'dubbelkvadrat-svb122274', ['Dubbelkvadrat', 'Speluppbyggnad'], '9–12 spelare · Yta 40 × 20 m i två halvor', fp, 'SPELUPPBYGGNAD',
       [('box', 8, 6, 92, 94), ('line', [(8, 50), (92, 50)])], counter(cnt, pos=(88, 46), last=None) + [lab(tw, tw + 1.2, (66, 46), 'BOLLVINST')])

# ============ svb289 Spelövning 1 (smålagsspel) – passa ============
d = Drill(); OU = [(30, 34), (70, 34), (70, 66), (30, 66)]; team(d, 'b', B, OU); d.p('f', '', R, (50, 50))
b = d.newball(rec(d, 'b0', 0)); t = 0.4; cnt = []; cur = 0
for nk in [1, 2, 3, 0, 2, 1, 2, 3]:
    tx, ty = OU[nk]; d.mv('f', t, t + 0.8, ((tx + 50) / 2, (ty + 50) / 2))
    t = d.pas(b, t + 0.2, rec(d, f'b{nk}', t + 1.0)); cnt.append(t); cur = nk
tw = win(d, b, 'f', f'b{cur}', t + 0.5, 0.6); d.mv('f', tw + 0.3, tw + 1.4, OU[cur]); d.mv(f'b{cur}', tw + 0.3, tw + 1.4, (50, 50))
fp = [(0, 'Spel 4 mot 1', 'Behåll bollen inom laget.'), (1.2, 'Titta upp innan du får bollen', ''),
      (5.0, 'Passa när du har kontroll', 'Och ser att medspelaren är beredd.'), (tw - 0.2, 'Bruten – byt försvarsspelare', 'Hur många passningar blev det?')]
finish(d, 'svb289', 'spelovning-1-smalagsspel-passa-svb289', ['Spelövning 1 (smålagsspel)', 'Passa'], '5 barn · Spelplan 12 × 8 m', fp, 'SPELUPPBYGGNAD',
       [('box', 20, 24, 80, 76)], counter(cnt, pos=(88, 50), last=None) + [lab(tw, tw + 1.4, (50, 18), 'BRUTEN')])

# ============ svb288 Färdighetsövning 1 – passa ============
d = Drill(); d.p('a', 'A', B, (30, 50)); d.p('b', 'B', B, (70, 50))
for k, (x, y) in enumerate([(24, 22), (76, 22), (24, 80), (76, 80)]): d.p(f'p{k}', '', R if k < 2 else YEL, (x, y))
bb = d.newball(rec(d, 'a', 0)); t = 0.4; cnt = []
for rep in range(4): t = d.pas(bb, t + 0.3, rec(d, 'b' if rep % 2 == 0 else 'a', t + 1.1)); cnt.append(t)
T2 = t + 0.3                                                                                                                 # stegring: i rörelse, fler par
d.mv('a', T2, T2 + 3, (36, 40)); d.mv('b', T2, T2 + 3, (64, 60))
for rep in range(3): t = d.pas(bb, t + 0.4, rec(d, 'b' if rep % 2 == 0 else 'a', t + 1.2))
for pr, (x, y) in enumerate([(0, 1), (2, 3)]):
    b2 = d.newball((200, 200)); show(d, b2, T2, rec(d, f'p{x}', T2)); tt = T2 + 0.2
    for rep in range(4):
        d.mv(f'p{x}', tt, tt + 1.2, (d.pos(f'p{x}')[0], d.pos(f'p{x}')[1] + (4 if rep % 2 else -4))); d.mv(f'p{y}', tt, tt + 1.2, (d.pos(f'p{y}')[0], d.pos(f'p{y}')[1] + (-4 if rep % 2 else 4)))
        tt = d.pas(b2, tt + 0.3, rec(d, f'p{y}' if rep % 2 == 0 else f'p{x}', tt + 1.2))
fp = [(0, 'A passar till B som tar emot', 'Sedan tillbaka.'), (1.2, 'Titta på bollen när du slår till', 'Pendla bakåt med benet, sedan framåt med fart.'),
      (T2, 'Stegring 1: passa i rörelse', ''), (T2 + 2.0, 'Stegring 2: större yta, fler par', 'Alla springer runt och passar.')]
finish(d, 'svb288', 'fardighetsovning-1-passa-svb288', ['Färdighetsövning 1', 'Passa'], '2 barn · Yta 10 × 5 m · Bollar och koner', fp, 'PASSNING',
       [('box', 14, 14, 86, 86)], counter(cnt, pos=(50, 30), last=None))

# ============ svb69819 Futsal – Passa och ta emot bollen (U9+) ============
d = Drill(); grp = [((30, 30), (30, 70)), ((70, 30), (70, 70))]
for g, (top, bot) in enumerate(grp):
    d.p(f'a{g}', '', B, top); d.p(f'q{g}', '', B, (top[0], top[1] - 7)); d.p(f'c{g}', '', R if g else B, bot)
ex = []
for g, (top, bot) in enumerate(grp):
    bb = d.newball(rec(d, f'a{g}', 0)); t = 0.4 + 0.3 * g
    for rep in range(5): t = d.pas(bb, t + 0.35, rec(d, f'c{g}' if rep % 2 == 0 else f'a{g}', t + 1.0), 0.65)
    d.mv(f'a{g}', t + 0.3, t + 2.4, (bot[0], bot[1] + 7)); d.mv(f'q{g}', t + 0.3, t + 0.9, top)                         # joggar och ställer sig bakom den ensamma
    for rep in range(4): t = d.pas(bb, t + 0.35, rec(d, f'q{g}' if rep % 2 else f'c{g}', t + 1.0), 0.65) if rep else d.pas(bb, t + 1.0, rec(d, f'q{g}', t + 1.7), 0.65)
fp = [(0, 'Tre och tre med en boll', 'Två på ena sidan, en på andra, 6–8 m isär.'), (1.2, 'Mottagning med sulan', 'Sikta med stödjebenet, spänd fot mitt på bollen.'),
      (5.6, '4–5 passningar – sedan byte', 'Den som har någon bakom sig joggar över.'), (9.0, 'Båda fötterna', 'Ett tillslag, två tillslag, sula och andra foten.')]
finish(d, 'svb69819', 'futsal-passa-och-ta-emot-bollen-u9-svb69819', ['Futsal – Passa och ta emot', 'bollen · U9+'], 'Spelare och bollar · 6–8 m mellan leden', fp, 'PASSNING', [], [])

if __name__ == '__main__': render(C, sys.argv)
