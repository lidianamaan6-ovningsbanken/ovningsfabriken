# Externa övningar, omgång 26 (tolv st). Regel: först d.mv, sedan d.carry; först mottagarens rörelse, sedan passningen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e9', __file__.replace('render_extern26.py', 'render_extern9.py'))
e9 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e9); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e9.finish, e9.rec, e9.chain, e9.wander, e9.counter, e9.arrivals
lab, hide, show, team, boxes, drive, shoot = e9.lab, e9.hide, e9.show, e9.team, e9.boxes, e9.drive, e9.shoot
factor, swap_color, stand, countdown, countup, win = e9.factor, e9.swap_color, e9.stand, e9.countdown, e9.countup, e9.win
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'

def no_ball_ok(fn):
    g = finish.__globals__; old = g['_ball_last']; g['_ball_last'] = lambda balls: 99
    try: fn()
    finally: g['_ball_last'] = old

# ============ if05 Korsa rutan ============
d = Drill()
EDGE = [(30, 10), (50, 10), (70, 10), (90, 50), (70, 90), (50, 90), (30, 90), (10, 50)]
for k, ps in enumerate(EDGE): d.p(f'p{k}', '', B, ps)
team(d, 'f', R, [(40, 46), (60, 54)], ['F', 'F'])
balls = [d.newball(rec(d, f'p{k}', 0)) for k in range(8)]; ex = []
plan = [(0, (38, 92), 0.6), (2, (62, 92), 1.0), (3, (10, 40), 1.6), (5, (58, 8), 2.4), (7, (90, 60), 3.0)]
for k, to, t0 in plan:
    pid = f'p{k}'; t1 = d.path(pid, t0, [((EDGE[k][0] + to[0]) / 2 + (4 if k % 2 else -4), (EDGE[k][1] + to[1]) / 2), to], 1.4)
    d.carry(balls[k], pid, 0, t1); ex.append(lab(t1, t1 + 1.4, (to[0], to[1] + (-8 if to[1] > 50 else 8)), '+2'))
d.mv('f0', 0.6, 3.6, (44, 40)); d.mv('f1', 0.6, 3.6, (58, 60))
d.mv('p1', 4.0, 6.0, (48, 32)); d.carry(balls[1], 'p1', 0, 6.0); d.mv('f0', 4.0, 6.0, (46, 36)); tt = 6.0        # taggad
d.mv('p1', 6.4, 8.4, (40, 46)); d.mv('f0', 6.4, 8.4, (50, 10)); hide(d, balls[1], 6.2); show(d, balls[1], 8.6, rec(d, 'f0', 8.6))   # byter roll
d.carry(balls[1], 'f0', 8.6, 17.9)
for k in (4, 6): d.carry(balls[k], f'p{k}', 0, 17.9)
fp = [(0, 'Dribblarna tar sig igenom ytan', 'Två försvarare inne.'),
      (2.6, 'Över hela ytan: två poäng', 'Till närmaste sida: en poäng.'),
      (tt - 0.6, 'Två taggar – byt roll', 'Med en försvarare.'),
      (9.0, 'Ny försvarare', '')]
finish(d, 'if05', 'korsa-rutan', ['Korsa', 'rutan'], 'Yta ca 14–18 m · Åtta dribblare runt kanten, två försvarare inne',
       fp, 'TEKNIK', [('box', 14, 14, 86, 86)], ex + [lab(tt, tt + 1.4, (48, 24), 'TAGG')])
f = factor(fp); ids = {k: i for i, k in enumerate(d.order)}
swap_color(ids['p1'], (tt + 0.4) * f, B, R); swap_color(ids['f0'], (tt + 0.4) * f, R, B)

# ============ if07 Vändningar: in- och utskär ============
d = Drill()
d.p('a', '', B, (30, 86)); d.p('c', '', ORA, (70, 14))
ba = d.newball(rec(d, 'a', 0)); bc = d.newball(rec(d, 'c', 0)); ex = []
for rep in range(2):
    t = 0.4 + 7.0 * rep
    t1 = d.path('a', t, [(30, 50), (34, 20)], 1.3); d.carry(ba, 'a', t, t1)                                   # till vändzonen
    t2 = d.path('a', t1, [(26, 16), (30, 50), (30, 86)], 1.3); d.carry(ba, 'a', t1, t2)                         # vänd – utskär
    t3 = d.path('c', t + 0.3, [(70, 50), (66, 80)], 1.3); d.carry(bc, 'c', t + 0.3, t3)
    t4 = d.path('c', t3, [(74, 84), (70, 50), (70, 14)], 1.3); d.carry(bc, 'c', t3, t4)
    ex.append(lab(t1, t1 + 1.2, (40, 10), 'INSKÄR' if rep == 0 else 'UTSKÄR'))
fp = [(0, 'Paren startar på motsatta sidor', 'Vändzon 5 × 5 m i varje ände.'),
      (2.4, 'Vänd i zonen och tillbaka', 'Inskär.'),
      (9.4, 'Utskär', 'Vänd med utsidan.'),
      (13.0, 'Variant: en försvarare möter i mitten', 'Och rollerna byts.')]
finish(d, 'if07', 'vandningar-in-och-utskar', ['Vändningar', 'In- och utskär'], 'Yta ca 18–27 m · Vändzon 5 × 5 m',
       fp, 'TEKNIK', [('zone', 20, 6, 80, 26, (200, 220, 200), 'VÄNDZON'), ('zone', 20, 74, 80, 94, (200, 220, 200), 'VÄNDZON')], ex)

# ============ if08 Passa och följ – fem koner ============
d = Drill()
CN = [(50, 86), (24, 64), (34, 30), (66, 30), (76, 64)]
d.p('s0', '', B, (50, 90)); d.p('s1', '', B, (50, 96))
for k in range(1, 5): d.p(f'c{k}', '', B, (CN[k][0] + (-4 if CN[k][0] < 50 else 4), CN[k][1]))
occ = {0: ['s0', 's1'], 1: ['c1'], 2: ['c2'], 3: ['c3'], 4: ['c4']}
def qp(c, n): x, y = CN[c]; return (x + (-4 if x < 50 else 4) * (1 + n) if c else x, y + (4 + 6 * n if c == 0 else 0))
b = d.newball(rec(d, 's0', 0)); t = 0.4
for rep in range(9):
    c = rep % 5; nc = (c + 1) % 5
    p = occ[c].pop(0); r = occ[nc][0]
    t1 = d.pas(b, t, rec(d, r, t + 0.9))                                                                       # passa på utsidan av konen
    d.mv(p, t + 0.2, t1 + 1.6, qp(nc, len(occ[nc]))); occ[nc].append(p)                                          # följ passningen
    for n, w in enumerate(occ[c]): d.mv(w, t + 0.3, t + 0.9, qp(c, n))
    d.carry(b, r, t1, t1 + 0.35); t = t1 + 0.4                                                                   # ta emot på bakre foten
fp = [(0, 'Passa och följ din passning', 'Fem koner, två vid startkonen.'),
      (1.4, 'Ta emot på bakre foten', ''),
      (4.0, 'Passa på utsidan av konen', ''),
      (9.0, 'Variant: väggspel före en lång passning', '')]
finish(d, 'if08', 'passa-och-folj-fem-koner', ['Passa och följ', 'Fem koner'], 'Yta ca 9–14 m · Fem koner',
       fp, 'PASSNINGSÖVNING', [('cone',) + c for c in CN])

# ============ if09 Passning genom portar 5 mot 5 ============
d = Drill()
GT = [(22, 22), (78, 22), (22, 78), (78, 78)]
BP = [(36, 36), (64, 30), (30, 62), (70, 66), (50, 50)]; RP = [(44, 26), (58, 42), (42, 56), (60, 60), (50, 76)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
for k in range(5): wander(d, f'r{k}', 0, 17.9, boxes([RP[k]], 4)[0], 6900 + k, 1.6)
b = d.newball(rec(d, 'b4', 0))
t = chain(d, b, 0.4, ['b0'], 0.3); d.mv('b1', t - 0.8, t + 0.6, (14, 14)); t = d.pas(b, t + 0.2, rec(d, 'b1', t + 1.0)); tp1 = t   # genom porten
t = chain(d, b, t, ['b0', 'b4', 'b3'], 0.3); d.mv('b2', t - 1.0, t + 0.6, (86, 86)); t = d.pas(b, t + 0.2, rec(d, 'b2', t + 1.0)); tp2 = t
fp = [(0, 'Fem mot fem utan målvakter', 'Fyra portar innanför hörnen.'),
      (tp1 - 0.6, 'Passa genom en port till en medspelare', 'Poäng.'),
      (tp1 + 0.4, 'Spela vidare – hitta nästa port', ''),
      (tp2, 'Variant: begränsa touch eller mindre portar', '')]
finish(d, 'if09', 'passning-genom-portar-5-mot-5', ['Passning genom portar', '5 mot 5'], 'Yta ca 27 × 27 m · Fyra portar innanför hörnen',
       fp, 'SMÅLAGSSPEL', [('box', 6, 6, 94, 94)] + [('cone', x + dx, y - dx) for x, y in GT for dx in (-3, 3)],
       [lab(tp1, tp1 + 1.4, (24, 10), '+1'), lab(tp2, tp2 + 1.4, (76, 92), '+1')])

# ============ if10 Drag back och Cruyff i triangel ============
d = Drill()
TRI = [(50, 26), (30, 64), (70, 64)]
d.p('p0', '', B, (50, 34)); d.p('p1', '', B, (36, 60))
for pi in range(2):
    pid = f'p{pi}'; bb = d.newball(rec(d, pid, 0)); t = 0.4 + 0.5 * pi; c = pi
    for lap in range(6):
        nc = (c + 1) % 3; (x0, y0), (x1, y1) = TRI[c], TRI[nc]
        mx, my = x0 + (x1 - x0) * 0.75, y0 + (y1 - y0) * 0.75
        t1 = d.path(pid, t, [(mx, my)], 1.2); d.carry(bb, pid, t, t1)
        L_ = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** .5; px, py = -(y1 - y0) / L_ * 3, (x1 - x0) / L_ * 3
        d.mv(pid, t1, t1 + 0.5, (mx + px, my + py)); d.carry(bb, pid, t1, t1 + 0.5)                                  # vändning vid konen
        t2 = d.path(pid, t1 + 0.5, [(x1 + (x0 - x1) * 0.15, y1 + (y0 - y1) * 0.15)], 1.2); d.carry(bb, pid, t1 + 0.5, t2)
        t = t2; c = nc
fp = [(0, 'Dribbla runt triangeln', 'Triangel på 5 m, max fyra per ruta.'),
      (1.6, 'Drag back vid konen', ''),
      (5.0, 'Sedan Cruyff-vändning', 'Och tvärtom.'),
      (10.0, 'Variant: sidoflick efter drag back', '')]
finish(d, 'if10', 'drag-back-och-cruyff-i-triangel', ['Drag back och Cruyff', 'I triangel'], 'Ruta 10 × 10 m · Triangel på 5 m',
       fp, 'TEKNIK', [('box', 14, 14, 86, 86)] + [('cone',) + c for c in TRI],
       [lab(0.4, 5.0, (50, 90), 'DRAG BACK'), lab(5.0, 10.0, (50, 90), 'CRUYFF'), lab(10.0, 17.6, (50, 90), 'SIDOFLICK')])

# ============ if11 Passning med tre lag ============
d = Drill()
COLS = [B, R, YEL]; PTS = [[(24, 24), (44, 30), (30, 46)], [(70, 22), (80, 42), (60, 40)], [(30, 74), (52, 66), (74, 74)]]
for g in range(3):
    for k in range(3): d.p(f'g{g}{k}', '', COLS[g], PTS[g][k])
for g in range(3):
    for k in range(3): wander(d, f'g{g}{k}', 0, 17.9, boxes([PTS[g][k]], 9)[0], 7000 + 10 * g + k, 1.6)
for g in range(3):
    bb = d.newball(rec(d, f'g{g}0', 0)); t = 0.4 + 0.3 * g; h = 0
    for rep in range(5): nk = (h + 1) % 3; t = d.pas(bb, t + 0.4, rec(d, f'g{g}{nk}', t + 1.3)); h = nk      # inom eget lag
    og = (g + 1) % 3
    for rep in range(3):
        t = d.pas(bb, t + 0.4, rec(d, f'g{og}{rep}', t + 1.5)); t = d.pas(bb, t + 0.4, rec(d, f'g{g}{(rep + 1) % 3}', t + 1.5))   # till en annan färg
fp = [(0, 'Tre lag, var sin boll', 'Alla rör sig i samma yta.'),
      (2.0, 'Passa inom eget lag', ''),
      (8.0, 'Sedan till en bestämd annan färg', 'Och tillbaka.'),
      (13.0, 'Variant: ett lag blir försvarare', '')]
finish(d, 'if11', 'passning-med-tre-lag', ['Passning', 'Med tre lag'], 'Yta ca 20–27 m · Tre lag',
       fp, 'PASSNINGSÖVNING', [('box', 10, 10, 90, 90)], [lab(0.4, 8.0, (50, 4), 'EGET LAG'), lab(8.0, 17.6, (50, 4), 'ANNAN FÄRG')])

# ============ if12 Fyra rutor – kort och långt ============
d = Drill()
BX = [(8, 8, 40, 40), (60, 8, 92, 40), (8, 60, 40, 92), (60, 60, 92, 92)]
def tri(bx): x1, y1, x2, y2 = bx; return [(x1 + 4, y1 + 4), (x2 - 4, y1 + 4), ((x1 + x2) / 2, y2 - 4)]
for q in (0, 3):
    for k, ps in enumerate(tri(BX[q])): d.p(f'a{q}{k}', '', B, ps)
for q in (1, 2):
    for k, ps in enumerate(tri(BX[q])): d.p(f'a{q}{k}', '', B, ps)
d.p('f', 'F', R, (24, 24)); team(d, 'm', R, [(46, 50), (54, 50)], ['F', 'F'])
b = d.newball(rec(d, 'a00', 0)); t = 0.4
wander(d, 'f', 0, 3.4, (18, 18, 30, 30), 7100, 1.2)
t = chain(d, b, t, ['a01', 'a02', 'a00', 'a01'], 0.2); tl = t
t = d.pas(b, t + 0.3, rec(d, 'a31', t + 1.8), 1.5); tl = t                                                     # lång boll till en annan ruta
d.mv('m0', tl - 1.0, tl + 0.8, (76, 76)); t = chain(d, b, t, ['a30', 'a32'], 0.25)
tw = win(d, b, 'm0', 'a32', t + 0.3, 0.5)
d.mv('m0', tw + 0.3, tw + 1.8, (76, 34)); d.carry(b, 'm0', tw + 0.3, tw + 1.8)                                  # vinner – går till en fri ruta
d.mv('a32', tw + 0.3, tw + 1.6, (50, 50))
fp = [(0, '3 mot 1 i en ruta', 'Fyra rutor, försvarare i mitten.'),
      (tl - 1.6, 'Efter några korta – en lång boll', 'Till en annan ruta.'),
      (tl + 0.2, 'Ny försvarare kliver in', ''),
      (tw - 0.2, 'Försvararen vinner – går till en fri ruta', 'Variant: 3 mot 2.')]
finish(d, 'if12', 'fyra-rutor-kort-och-langt', ['Fyra rutor', 'Kort och långt'], 'Yta ca 20–27 m · Fyra rutor och försvarare i mitten',
       fp, 'RONDO', [('box',) + bx for bx in BX])

# ============ if13 Kroppsdelsgrupper ============
d = Drill(); d.p('t', 'T', T_COL, (50, 95))
ST = [(22, 24), (48, 20), (74, 26), (24, 52), (52, 48), (78, 54), (30, 78), (68, 80)]
for k, ps in enumerate(ST): d.p(f'p{k}', '', B, ps)
for k in range(8): wander(d, f'p{k}', 0, 4.4, boxes([ST[k]], 8)[0], 7200 + k, 1.4)
GR = [[0, 1, 3], [2, 5, 4], [6, 7]]; CEN = [(32, 32), (66, 40), (48, 74)]
for g, mem in enumerate(GR):
    for j, k in enumerate(mem): d.mv(f'p{k}', 4.8, 6.6, (CEN[g][0] + 4 * (j - 1), CEN[g][1] + (3 if j % 2 else -3)))
for k in range(8): stand(d, f'p{k}', 6.6, 9.4); wander(d, f'p{k}', 9.6, 17.9, boxes([ST[k]], 8)[0], 7210 + k, 1.4)
fp = [(0, 'Spelarna rör sig fritt', ''),
      (4.4, 'Tränaren ropar', '”Tre – två fötter och en hand”.'),
      (6.6, 'Bilda grupper med rätt antal', 'Kroppsdelar i marken.'),
      (9.6, 'Rör er fritt igen', 'Nästa kommando.')]
d.newball((200, 200))
no_ball_ok(lambda: finish(d, 'if13', 'kroppsdelsgrupper', ['Kroppsdels-', 'grupper'], 'Yta ca 18–27 m',
       fp, 'LEK', [('box', 10, 10, 90, 88)], [lab(4.4, 6.6, (50, 6), '”TRE – TVÅ FÖTTER OCH EN HAND!”')]))

# ============ if14 Finter vid koner ============
d = Drill()
CN = [(50, 70), (50, 50), (50, 30)]; FT = ['FEJK OCH TA', 'SAX OCH TA', 'FLIP FLAP', 'STEP OVER']
for k in range(3): d.p(f'p{k}', '', B, (50, 92 + 0 * k) if k == 0 else (44 + 12 * (k - 1), 96))
balls = [d.newball(rec(d, f'p{k}', 0)) for k in range(3)]; ex = []; t = 0.4
for k in range(3):
    pid = f'p{k}'
    if k: d.mv(pid, t - 0.8, t, (50, 92))
    d.carry(balls[k], pid, 0, t)
    pts = []
    for i, (x, y) in enumerate(CN): pts += [(x + (4 if i % 2 == 0 else -4), y + 4), (x + (-5 if i % 2 == 0 else 5), y - 4)]   # fint vid varje kon
    t2 = d.path(pid, t, pts + [(50, 10)], 1.2); d.carry(balls[k], pid, t, t2)
    ex.append(lab(t + 0.8, t + 2.6, (72, 50), FT[k])); d.mv(pid, t2, t2 + 2.0, (80, 90 - 4 * k)); hide(d, balls[k], t2 + 0.2)
    t = t + 3.0
fp = [(0, 'Dribbla genom konerna', '1 m mellan konerna.'),
      (1.2, 'En fint vid varje kon', ''),
      (4.0, 'Sax, flip flap, step over', ''),
      (8.0, 'Variant: två möts och fintar varandra', '')]
finish(d, 'if14', 'finter-vid-koner', ['Finter', 'vid koner'], 'Koner i mitten och på sidorna',
       fp, 'TEKNIK', [('cone',) + c for c in CN] + [('cone', 20, 50), ('cone', 80, 50)], ex)

# ============ if15 Skott efter mottagning ============
d = Drill(); d.p('mv', 'MV', R, (50, 4)); d.p('c', 'C', B, (50, 40))
HP = [(14, 80), (86, 80), (14, 30), (86, 30)]
for k, ps in enumerate(HP): d.p(f'h{k}', '', ORA, ps)
t = 0.4; ex = []
for k, back in enumerate([False, False, True, True]):
    bb = d.newball(rec(d, f'h{k}', 0)); d.mv('c', t, t + 0.6, (50, 40))
    t1 = d.pas(bb, t + 0.2, rec(d, 'c', t + 1.4))
    if back: d.mv('c', t1, t1 + 0.5, (54, 36)); d.carry(bb, 'c', t1, t1 + 0.5); t1 += 0.5                         # med ryggen mot mål – vänd
    else: d.carry(bb, 'c', t1, t1 + 0.3); t1 += 0.3
    tg = shoot(d, bb, t1 + 0.05, (46 + 3 * k, 1)); hide(d, bb, tg + 0.3); t = tg + 0.3
    ex.append(lab(t1 - 0.6, t1 + 0.2, (70, 44), 'RYGGEN MOT MÅL' if back else 'FRAMÅTVÄND'))
fp = [(0, 'Hörnspelarna spelar in', 'Fem spelare och målvakt.'),
      (1.4, 'Två bollar framåtvänd', 'Ta emot och skjut.'),
      (ex[2]['t0'], 'Två med ryggen mot mål', 'Vänd och skjut.'),
      (t, 'Variant: lägg till en försvarare', '')]
finish(d, 'if15', 'skott-efter-mottagning', ['Skott efter', 'mottagning'], 'Yta ca 18 × 18 m · Fem spelare och målvakt',
       fp, 'AVSLUT', [], ex)
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ if16 Målspelaren lägger upp ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96))
d.p('bm', 'M', B, (40, 14)); d.p('rm', 'M', R, (60, 86))
BP = [(30, 60), (70, 58), (50, 44)]; RP = [(36, 34), (64, 36), (50, 62)]; team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b2'], 0.3); t = d.pas(b, t + 0.2, rec(d, 'bm', t + 1.2))                                 # till målspelaren
d.mv('b2', t - 1.2, t + 0.4, (48, 24)); t = d.pas(b, t + 0.2, rec(d, 'b2', t + 0.8)); tg = shoot(d, b, t + 0.05, (54, 1))   # lägger ut för skott
d.mv('b2', tg + 0.2, tg + 2.0, (40, 14)); d.mv('bm', tg + 0.2, tg + 2.2, (50, 44))                              # byter plats
fp = [(0, 'En målspelare vid motståndarnas mål', 'Varje lag har en.'),
      (1.6, 'Spela till målspelaren', ''),
      (tg - 0.6, 'Målspelaren lägger ut för skott', ''),
      (tg + 0.4, 'Skytten byter plats med målspelaren', 'Variant: begränsa touch eller tid.')]
finish(d, 'if16', 'malspelaren-lagger-upp', ['Målspelaren', 'lägger upp'], 'Yta ca 27–30 × 37–46 m · Två mål och målvakter',
       fp, 'SMÅLAGSSPEL', [], [lab(tg + 0.2, tg + 2.0, (60, 30), 'BYT PLATS')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ if17 Skott och inlägg i stationer ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
d.p('a', 'A', B, (50, 50)); d.p('b', 'B', B, (40, 60)); d.p('c', 'C', B, (60, 62)); d.p('k', 'K', B, (86, 40))
ba = d.newball(rec(d, 'a', 0)); bb = d.newball(rec(d, 'b', 0))
t = drive(d, ba, 'a', 0.4, (50, 30), 14); tg = shoot(d, ba, t + 0.1, (46, 1)); hide(d, ba, tg + 0.3)            # A dribblar och skjuter
t = d.pas(bb, tg + 0.2, rec(d, 'k', tg + 1.4)); t = drive(d, bb, 'k', t, (86, 14), 18)                          # B passar ut i kanalen
d.mv('c', tg, t + 0.8, (54, 12)); t = d.pas(bb, t + 0.1, rec(d, 'c', t + 1.0), 0.9); tg2 = shoot(d, bb, t + 0.05, (52, 1))   # C på inlägget
d.mv('a', tg + 0.2, tg + 2.4, (40, 60)); d.mv('b', tg + 0.6, tg + 2.6, (64, 70))
fp = [(0, 'A dribblar och skjuter', 'Tre stationer och två kanaler.'),
      (tg + 0.2, 'B passar ut i kanalen', ''),
      (tg2 - 1.2, 'C löper in mot inlägget', ''),
      (tg2, 'Rotera A till B till C', 'Variant: lägg till försvarare.')]
finish(d, 'if17', 'skott-och-inlagg-i-stationer', ['Skott och inlägg', 'i stationer'], 'Yta ca 37 × 27–30 m · Tre stationer och två kanaler',
       fp, 'AVSLUT', [('zone', 80, 4, 100, 70, (200, 220, 200), ''), ('zone', 0, 4, 20, 70, (200, 220, 200), '')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

if __name__ == '__main__': render(C, sys.argv)
