# Externa övningar, omgång 24 (tolv st). Regel: först d.mv, sedan d.carry; först mottagarens rörelse, sedan passningen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e9', __file__.replace('render_extern24.py', 'render_extern9.py'))
e9 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e9); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e9.finish, e9.rec, e9.chain, e9.wander, e9.counter, e9.arrivals
lab, hide, show, team, boxes, drive, shoot = e9.lab, e9.hide, e9.show, e9.team, e9.boxes, e9.drive, e9.shoot
factor, swap_color, stand, countdown, countup, win = e9.factor, e9.swap_color, e9.stand, e9.countdown, e9.countup, e9.win
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'; GRN = '#3fbf5f'

# ============ pj11 Passa mellan zonerna ============
d = Drill()
ZN = [(10, 10, 34, 34), (66, 10, 90, 34), (10, 66, 34, 90), (66, 66, 90, 90)]
BP = [(22, 22), (40, 46), (60, 40), (78, 78), (30, 60), (56, 64)]; RP = [(34, 36), (50, 30), (66, 46), (44, 58), (62, 70), (26, 46)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
for k in range(6): wander(d, f'r{k}', 0, 17.9, boxes([RP[k]], 4)[0], 6000 + k, 1.6)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b1', 'b2'], 0.3); d.mv('b3', t - 0.8, t + 0.4, (78, 78)); t = d.pas(b, t + 0.2, rec(d, 'b3', t + 1.2)); tz = t   # zon till zon
t = d.pas(b, t + 0.3, rec(d, 'b5', t + 1.0)); t = d.pas(b, t + 0.2, (50, 99), 0.7); tu = t; hide(d, b, tu + 0.2)      # spela ut ur planen
fp = [(0, 'Sex mot sex, fyra zoner', 'Två touch, sista passningen fritt.'),
      (tz - 1.4, 'Passa från en zon till en annan', 'Utan att motståndarna rör bollen.'),
      (tu - 1.2, 'Spela sedan ut bollen ur planen', ''),
      (tu, 'Poäng', '')]
finish(d, 'pj11', 'passa-mellan-zonerna', ['Passa mellan', 'zonerna'], 'Yta 35 × 35 m med fyra zoner',
       fp, 'POSITIONSSPEL', [('box', 6, 6, 94, 94)] + [('zone',) + z + ((200, 220, 200), '') for z in ZN], [lab(tu, tu + 1.6, (50, 88), '+1')])

# ============ pj12 Rondo 3 mot 1 – bryt passningslinjen ============
d = Drill()
d.p('a', '', B, (30, 70)); d.p('c', '', B, (70, 70)); d.p('z', '', B, (50, 26)); d.p('f', '', R, (50, 54))
b = d.newball(rec(d, 'a', 0)); t = 0.4; ex = []
seq = [('c', None), ('z', None), ('a', None), ('c', 'blk'), ('a', None), ('z', 'blk')]
for to, blk in seq:
    if blk:
        fr = at(d.balls[b], t); tx, ty = rec(d, to, t + 0.8); mx, my = (fr[0] + tx) / 2, (fr[1] + ty) / 2
        d.mv('f', t - 0.6, t + 0.3, (mx - 1.8, my + 1.2)); t1 = d.pas(b, t, (mx, my), 0.4); ex.append(lab(t1, t1 + 1.4, (50, 88), '+1 FÖRSVAR'))
        t = d.pas(b, t1 + 0.3, rec(d, 'a', t1 + 1.1)); d.mv('f', t1 + 0.3, t1 + 1.0, (50, 54))
    else:
        d.mv('f', t, t + 0.7, (50 + (at(d.pl[to]['tr'], t)[0] - 50) * 0.2, 54)); t = d.pas(b, t + 0.15, rec(d, to, t + 0.8))
fp = [(0, 'Tre mot en i en liten ruta', 'Ruta 5 × 5 m.'),
      (1.6, 'Passa till spelaren längst bak', ''),
      (ex[0]['t0'] - 0.4, 'Bryt passningslinjen: 1 poäng', 'Ställ dig i linjen mellan bollen och mottagaren.'),
      (ex[0]['t1'], 'Fem block à 2 minuter', 'Alla är i mitten under ett block.')]
finish(d, 'pj12', 'rondo-3-mot-1-bryt-passningslinjen', ['Rondo 3 mot 1', 'Bryt passningslinjen'], 'Ruta 5 × 5 m',
       fp, 'RONDO', [('box', 22, 18, 78, 80)], ex)

# ============ pj13 Tio passningar och vidare ============
d = Drill()
AP = [(24, 14), (40, 22), (60, 22), (76, 14), (34, 34), (66, 34)]; CP = [(24, 86), (40, 78), (60, 78), (76, 86), (34, 66), (66, 66)]
PP = [(30, 46), (44, 50), (58, 50), (70, 46), (40, 58), (60, 58)]
team(d, 'b', B, AP); team(d, 'w', WHITE, CP); team(d, 'r', R, PP)
for k in range(6): wander(d, f'b{k}', 0, 17.9, boxes([AP[k]], 4)[0], 6100 + k, 1.6); wander(d, f'w{k}', 0, 17.9, boxes([CP[k]], 4)[0], 6110 + k, 1.6)
for k in range(6): wander(d, f'r{k}', 0, 17.9, boxes([PP[k]], 4)[0], 6120 + k, 1.6)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b1', 'b4', 'b2', 'b5', 'b3', 'b2', 'b1', 'b4', 'b5', 'b2'], 0.2); cnt = arrivals(d, b)[:10]
t = d.pas(b, t + 0.2, rec(d, 'w2', t + 1.6), 1.4); to = t                                                     # över till andra sidan
t = chain(d, b, t, ['w0', 'w4', 'w5'], 0.25)
fp = [(0, 'Tre lag om sex', 'Laget med bollen spelar tio passningar.'),
      (cnt[4], 'Tio passningar', ''),
      (to - 1.4, 'Lämna över till andra sidan', ''),
      (to + 0.4, 'Pressarna: vinn och spela över = 1 poäng', '')]
finish(d, 'pj13', 'tio-passningar-och-vidare', ['Tio passningar', 'och vidare'], 'Yta 20 × 45 m · Tre lag om sex',
       fp, 'POSITIONSSPEL', [('box', 12, 4, 88, 96), ('line', [(12, 40), (88, 40)]), ('line', [(12, 60), (88, 60)])], counter(cnt, pos=(92, 20), last='ÖVER'))

# ============ pj14 5 mot 5 – frigör stödspelarna ============
d = Drill()
BP = [(30, 64), (70, 62), (44, 46), (58, 36), (50, 76)]; RP = [(34, 36), (66, 38), (50, 54), (42, 26), (60, 70)]
team(d, 'b', B, BP); team(d, 'r', R, RP); d.p('s1', 'S', YEL, (50, 4)); d.p('s2', 'S', YEL, (50, 96))
for k in range(5): wander(d, f'r{k}', 0, 7, boxes([RP[k]], 4)[0], 6200 + k, 1.6)
b = d.newball(rec(d, 'b4', 0))
t = d.pas(b, 0.4, rec(d, 's2', 1.4)); t1 = t; t = d.pas(b, t + 0.3, rec(d, 'b2', t + 1.3))
t = d.pas(b, t + 0.3, rec(d, 's1', t + 1.4)); t2 = t; t = d.pas(b, t + 0.3, rec(d, 'b3', t + 1.0))           # båda stöden passerade
t = drive(d, b, 'b3', t, (60, 70), 16); d.mv('b3', t, t + 0.8, (60, 99)); d.carry(b, 'b3', t, t + 0.8); tg = t + 0.6   # dribbla över linjen mitt emot
fp = [(0, 'Fem mot fem plus två stöd', 'Max två touch.'),
      (t1 - 0.6, 'Bollen ska passera båda stöden', ''),
      (t2 - 0.6, 'Andra stödet', ''),
      (tg - 1.4, 'Dribbla över linjen mitt emot senaste stödet', 'Det är mål.')]
finish(d, 'pj14', '5-mot-5-frigor-stodspelarna', ['5 mot 5', 'Frigör stödspelarna'], 'Yta 30 × 30 m · Stöd i varje bakre zon',
       fp, 'SPELÖVNING', [('box', 8, 2, 92, 98), ('zone', 30, 0, 70, 8, (240, 210, 90), ''), ('zone', 30, 92, 70, 100, (240, 210, 90), '')],
       [lab(t1, t1 + 1.2, (64, 92), '1'), lab(t2, t2 + 1.2, (64, 8), '2'), lab(tg, tg + 1.6, (60, 90), 'MÅL')])

# ============ us01 Väggträning ============
d = Drill()
XS = [26, 50, 74]
for k, x in enumerate(XS): d.p(f'p{k}', '', B, (x, 40))
SER = [('INSIDA HÖGER', 1), ('INSIDA VÄNSTER', -1), ('VÄXELVIS', 0), ('VOLLEY', 1), ('NICK', 0)]
ex = []
for k, x in enumerate(XS):
    b = d.newball(rec(d, f'p{k}', 0)); t = 0.4 + 0.1 * k
    for si, (name, foot) in enumerate(SER):
        if k == 0: ex.append(lab(t, t + 3.0, (50, 70), name))
        for rep in range(3):
            fx = foot if foot else (1 if rep % 2 == 0 else -1)
            t1 = d.pas(b, t, (x + fx, 13), 0.4); t = d.pas(b, t1, (x + 1.8 * fx, 38.8 if name not in ('NICK', 'VOLLEY') else 36), 0.4) + 0.12
        t += 0.4
fp = [(0, 'Vägg 2–3 m bort', 'Serier på 30 sekunder, en minuts vila.'),
      (3.4, 'Insida vänster – sedan växelvis', ''),
      (10.2, 'Volley', 'Bollen kastas upp med händerna.'),
      (13.6, 'Nick', 'Max tempo i varje serie.')]
finish(d, 'us01', 'vaggtraning-insida-volley-och-nick', ['Väggträning', 'Insida, volley och nick'], 'Vägg 2–3 m bort · En boll per spelare',
       fp, 'TEKNIK', [('zone', 8, 4, 92, 12, (190, 190, 190), 'VÄGG')], ex)

# ============ cu01 Tre i rad med boll ============
d = Drill()
RG = [(38 + 12 * i, 22 + 12 * j) for j in range(3) for i in range(3)]
for tm, x, col in (('b', 26, B), ('r', 74, R)):
    for k in range(3): d.p(f'{tm}{k}', '', col, (x, 82 + 5 * k))
put = {'b': [0, 4, 8], 'r': [2, 5, 1]}; ex = []
for tm, x, col in (('b', 26, B), ('r', 74, R)):
    bl = d.newball(rec(d, f'{tm}0', 0)); t = 0.4 + (0.3 if tm == 'r' else 0); hold = f'{tm}0'
    for k in range(3):
        pid = f'{tm}{k}'
        if k: d.mv(pid, t - 0.6, t, (x, 82)); t1 = d.pas(bl, t - 0.6, rec(d, pid, t), 0.5)
        gx, gy = RG[put[tm][k]]
        t2 = d.path(pid, t, [(gx + (2 if tm == 'r' else -2), gy + 4)], 1.6); d.carry(bl, pid, t, t2)              # dribbla fram och lägg tröjan
        ex.append(dict(kind='vest', t0=t2, pos=(gx, gy), color=col))
        t3 = d.path(pid, t2 + 0.2, [(x + (-6 if tm == 'b' else 6), 80 + 6 * k)], 1.6); d.carry(bl, pid, t2 + 0.2, t3)
        t = t3 + 0.3
tw = max(e['t0'] for e in ex if e['color'] == B)
fp = [(0, 'Dribbla fram och lägg en tröja i en ring', 'Två eller tre lag.'),
      (3.0, 'Nästa startar när den förra är tillbaka', ''),
      (tw - 0.6, 'Tre i rad vinner', ''),
      (tw + 0.6, 'Variant: svagare foten eller hinder', '')]
finish(d, 'cu01', 'tre-i-rad-med-boll', ['Tre i rad', 'Med boll'], 'Nio ringar i en kvadrat · Två lag',
       fp, 'STAFETT', [('circle', x, y, 1.4) for x, y in RG], ex + [lab(tw, tw + 2.0, (50, 8), 'TRE I RAD!')])

# ============ cu02 Nummerjakten ============
d = Drill(); d.p('t', 'T', T_COL, (96, 50))
for k in range(4): d.p(f'b{k}', str(k + 1), B, (8, 26 + 16 * k)); d.p(f'r{k}', str(k + 1), R, (92, 26 + 16 * k))
b = d.newball((51.8, 48.8)); tc = 0.6
d.mv('b2', tc + 0.3, tc + 2.0, (48, 50)); d.mv('r2', tc + 0.4, tc + 2.2, (60, 48))                             # ”3!” – båda springer
t = drive(d, b, 'b2', tc + 2.0, (70, 34), 16); d.mv('r2', tc + 2.2, t, (74, 40))                              # först anfaller, andra försvarar
tw = win(d, b, 'r2', 'b2', t + 0.3, 0.4); t = drive(d, b, 'r2', tw, (40, 60), 18)
fp = [(0, 'Tränaren ropar ett nummer', 'Två lag med numrerade spelare.'),
      (tc + 0.3, 'Spring mot bollen', ''),
      (tc + 2.0, 'Först till bollen anfaller', 'Den andra försvarar.'),
      (tw - 0.2, '4–5 omgångar med 45 sekunders vila', 'Variant: ropa två eller tre nummer.')]
finish(d, 'cu02', 'nummerjakten', ['Nummer-', 'jakten'], 'Två lag med numrerade spelare · En boll i mitten',
       fp, 'LEK', [('box', 4, 10, 96, 90)], [lab(tc - 0.3, tc + 1.2, (50, 30), '”3!”')])

# ============ cu03 Dribbla genom tre minimål ============
d = Drill()
GT = [(30, 28), (70, 34), (50, 70)]
BP = [(24, 48), (60, 20), (78, 60), (36, 80)]; RP = [(40, 36), (62, 48), (44, 58), (70, 76)]
team(d, 'b', B, BP); team(d, 'r', R, RP); team(d, 'n', YEL, [(14, 20), (86, 86)], ['N', 'N'])
for k in range(4): wander(d, f'r{k}', 0, 17.9, boxes([RP[k]], 4)[0], 6300 + k, 1.6)
b = d.newball(rec(d, 'b0', 0))
t = d.pas(b, 0.4, rec(d, 'b1', 1.4)); t = d.path('b1', t, [(30, 22), (30, 34)], 1.2); d.carry(b, 'b1', 1.4, t); tg1 = t - 0.4   # genom minimålet
t = d.pas(b, t + 0.2, rec(d, 'n0', t + 1.0)); t = d.pas(b, t + 0.2, rec(d, 'b2', t + 1.4))
t2 = d.path('b2', t, [(70, 42), (70, 28)], 1.2); d.carry(b, 'b2', t, t2); tg2 = t2 - 0.4                        # laget behåller bollen
t = d.pas(b, t2 + 0.2, rec(d, 'b3', t2 + 1.6), 1.4)
fp = [(0, 'Fyra mot fyra plus två neutrala', 'Tre minimål på 2 m.'),
      (tg1 - 0.6, 'Dribbla genom ett minimål: poäng', 'Laget behåller bollen.'),
      (tg2 - 0.6, 'Och genom nästa', ''),
      (tg2 + 0.6, 'Omgångar på två minuter', 'Variant: rutor på 1 × 1 m.')]
finish(d, 'cu03', 'dribbla-genom-tre-minimal', ['Dribbla genom', 'tre minimål'], 'Yta 35 × 35 m · Tre minimål på 2 m',
       fp, 'SMÅLAGSSPEL', [('box', 8, 8, 92, 92)] + [('cone', x + dx, y) for x, y in GT for dx in (-4, 4)],
       [lab(tg1, tg1 + 1.4, (30, 18), '+1'), lab(tg2, tg2 + 1.4, (70, 24), '+1')])

# ============ cu04 Överlägsenhet med fyra touch ============
d = Drill()
BP = [(30, 34), (66, 30)]; RP = [(44, 48), (56, 58)]; NP = [(30, 70), (70, 66)]
team(d, 'b', B, BP); team(d, 'r', R, RP); team(d, 'n', YEL, NP, ['N', 'N'])
for k in range(2): wander(d, f'r{k}', 0, 17.9, boxes([RP[k]], 5)[0], 6400 + k, 1.6)
b = d.newball(rec(d, 'b0', 0)); t = 0.4; hold = 'b0'; tc = []
for to in ['n0', 'b1', 'n1', 'b0', 'n0', 'b1', 'n1']:
    hx, hy = at(d.pl[hold]['tr'], t)
    for j, (dx, dy) in enumerate(((2, 0), (2, 2), (0, 2), (0, 0))): d.mv(hold, t, t + 0.35, (hx + dx, hy + dy)); d.carry(b, hold, t, t + 0.35); t += 0.35   # fyra touch i en liten fyrkant
    tc.append(t); t = d.pas(b, t + 0.05, rec(d, to, t + 0.9)); hold = to
fp = [(0, '2 mot 2 + 2 neutrala', 'Ruta 12 × 12 m.'),
      (1.4, 'Fyra touch innan passning', 'Neutrala spelar med laget som har bollen.'),
      (6.0, 'Täck bollen under touchen', ''),
      (10.0, 'Samma i 3 mot 3 + 3 och 4 mot 4 + 4', 'Större rutor.')]
finish(d, 'cu04', 'overlagsenhet-med-fyra-touch', ['Överlägsenhet', 'Med fyra touch'], 'Rutor 12 × 12, 15 × 15 och 20 × 20 m',
       fp, 'POSITIONSSPEL', [('box', 16, 16, 84, 84)], countup(0.4, 4, (50, 8), 0.35) + countup(tc[0] + 0.9, 4, (50, 8), 0.35))

# ============ ds01 Bollgymnastik och tick-tock ============
d = Drill()
ST = [(28, 32), (72, 32), (28, 70), (72, 70)]
for k, ps in enumerate(ST): d.p(f'p{k}', '', B, ps)
for k, (x, y) in enumerate(ST):
    bb = d.newball((x, y - 3.5)); tr = d.balls[bb]; t = 0.4
    for dx, dy in ((0, -3), (0, 2), (3, 0), (-3, 0)):                                                         # rulla framåt, bakåt, sidled
        tr += [(t, (x, y - 3.5)), (t + 0.7, (x + dx, y - 3.5 + dy)), (t + 1.4, (x, y - 3.5))]; t += 1.4
    while t < 11.0: tr += [(t, (x - 2, y - 2)), (t + 0.25, (x + 2, y - 2))]; t += 0.5                            # tick-tock på stället
    d.mv(f'p{k}', t, 17.0, (x, y - 10))
    while t < 17.0:
        f_ = (t - 11.0) / 6.0; tr += [(t, (x - 2, y - 2 - 10 * f_)), (t + 0.25, (x + 2, y - 2 - 10 * (f_ + 0.04)))]; t += 0.5   # tick-tock framåt
fp = [(0, 'Rulla bollen med sulan', 'Framåt, bakåt, i sidled.'),
      (5.6, 'Tick-tock på stället', 'Tippa bollen mellan fötterna.'),
      (11.0, 'Tick-tock framåt', ''),
      (14.0, 'Bygg upp tempot långsamt', 'Båda fötterna.')]
finish(d, 'ds01', 'bollgymnastik-och-tick-tock', ['Bollgymnastik', 'och tick-tock'], 'En boll per spelare',
       fp, 'TEKNIK', [], [lab(0.4, 5.6, (50, 10), 'SULAN'), lab(5.6, 11.0, (50, 10), 'TICK-TOCK'), lab(11.0, 17.4, (50, 10), 'TICK-TOCK FRAMÅT')])
C[-1]['_stuck'] = True

# ============ ds02 Väggspelaren ============
d = Drill(); d.p('v', 'V', YEL, (50, 26))
Q = ['q0', 'q1', 'q2']
for n, pid in enumerate(Q): d.p(pid, '', B, (50, 66 + 7 * n))
b = d.newball(rec(d, 'q0', 0)); t = 0.4
for rep in range(5):
    p = Q.pop(0)
    t1 = d.pas(b, t, rec(d, 'v', t + 0.9)); d.carry(b, 'v', t1, t1 + 0.4)                                      # stoppar
    t2 = d.pas(b, t1 + 0.45, rec(d, Q[0], t1 + 1.2))
    d.mv(p, t + 0.2, t + 1.6, (58, 66 + 7 * len(Q))); d.mv(p, t + 1.6, t + 2.2, (50, 66 + 7 * len(Q))); Q.append(p)   # sist i kön
    for n, w in enumerate(Q[:-1]): d.mv(w, t + 0.3, t + 1.0, (50, 66 + 7 * n))
    t = t2 + 0.2
d.mv('v', t, t + 1.4, (40, 26))
fp = [(0, 'Passa till väggen', 'Väggen står ca 5 m bort.'),
      (1.6, 'Väggen stoppar och spelar tillbaka', ''),
      (3.0, 'Den som passat går sist i kön', ''),
      (t - 1.0, 'Byt vägg efter ett varv', '')]
finish(d, 'ds02', 'vaggspelaren', ['Vägg-', 'spelaren'], 'Grupper om 3–4 · Väggen ca 5 m bort',
       fp, 'PASSNINGSÖVNING', [])

# ============ ds03 Passningsnamnleken ============
d = Drill()
NAMES = ['ALVA', 'OMAR', 'LIV', 'NOAH', 'SARA']
RING = [ring_pos(50, 50, 30, i, 5) for i in range(5)]
for k, ps in enumerate(RING): d.p(f'p{k}', NAMES[k][0], B, ps)
b = d.newball(rec(d, 'p0', 0)); t = 0.4; ex = []; hold = 0
for to in [2, 4, 1, 3, 0, 2, 4]:
    ex.append(lab(t - 0.1, t + 0.8, (RING[hold][0], RING[hold][1] - 10), '”' + NAMES[to] + '!”'))
    d.carry(b, f'p{hold}', t, t + 0.4); t = d.pas(b, t + 0.45, rec(d, f'p{to}', t + 1.3)); hold = to; t += 0.2   # två touch
fp = [(0, 'Bollen passas inom cirkeln', 'Grupper om fem.'),
      (1.0, 'Ropa namnet på nästa mottagare', 'Innan bollen kommer.'),
      (5.0, 'Två touch per spelare', ''),
      (9.0, 'Variant: den som passar ropar', 'Och cirkeln blir större.')]
finish(d, 'ds03', 'passningsnamnleken', ['Passnings-', 'namnleken'], 'Grupper om fem i en cirkel',
       fp, 'PASSNINGSÖVNING', [], ex)

if __name__ == '__main__': render(C, sys.argv)
