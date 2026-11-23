# Externa övningar, omgång 23 (tolv st). Regel: först d.mv, sedan d.carry; först mottagarens rörelse, sedan passningen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e9', __file__.replace('render_extern23.py', 'render_extern9.py'))
e9 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e9); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e9.finish, e9.rec, e9.chain, e9.wander, e9.counter, e9.arrivals
lab, hide, show, team, boxes, drive, shoot = e9.lab, e9.hide, e9.show, e9.team, e9.boxes, e9.drive, e9.shoot
factor, swap_color, stand, countdown, countup, win = e9.factor, e9.swap_color, e9.stand, e9.countdown, e9.countup, e9.win
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'; GRN = '#3fbf5f'

# ============ mk13 Vändningsstegen ============
d = Drill()
LX = [30, 70]; YC = [86, 74, 62, 50, 38, 26, 14]
for li, x in enumerate(LX):
    d.p(f'p{li}', '', B, (x + 4, 90))
for li, x in enumerate(LX):
    pid = f'p{li}'; b = d.newball(rec(d, pid, 0)); t = 0.4 + 0.3 * li
    for k in range(1, 5):
        t2 = d.path(pid, t, [(x + 4, YC[k] + 3)], 1.4 + 0.15 * k); d.carry(b, pid, t, t2)                         # dribbla till konen
        t3 = d.path(pid, t2, [(x - 4, YC[k] + 3), (x - 4, 90)], 1.4 + 0.15 * k); d.carry(b, pid, t2, t3)          # vänd och tillbaka
        t = t3
fp = [(0, 'Dribbla till andra konen och tillbaka', '6–8 koner på rad.'),
      (2.0, 'Sedan till tredje och tillbaka', 'Och så vidare.'),
      (6.0, 'Vänd med insida och utsida', 'Åt båda hållen.'),
      (11.0, 'Börja långsamt och öka', '')]
finish(d, 'mk13', 'vandningsstegen', ['Vändnings-', 'stegen'], '6–8 koner på rad',
       fp, 'TEKNIK', [('cone', x, y) for x in LX for y in YC])

# ============ mk14 Musikbollar och Simon säger ============
d = Drill(); d.p('t', 'T', T_COL, (50, 94))
ST = [(22, 26), (46, 22), (72, 28), (24, 54), (50, 50), (76, 56), (34, 76), (64, 76)]
balls = []
for k, ps in enumerate(ST): d.p(f'p{k}', '', B, ps); balls.append(d.newball(rec(d, f'p{k}', 0)))
for k in range(8):
    pid = f'p{k}'; bx = boxes([ST[k]], 7)[0]
    wander(d, pid, 0, 4.4, bx, 5100 + k, 1.4); stand(d, pid, 4.4, 7.0)                                         # musiken stannar
    wander(d, pid, 7.0, 11.4, bx, 5110 + k, 1.4); stand(d, pid, 11.4, 14.0)                                    # Simon säger
    wander(d, pid, 14.0, 17.9, bx, 5120 + k, 1.4); d.carry(balls[k], pid, 0, 17.9)
fp = [(0, 'Dribbla så länge musiken spelar', 'Alla har en boll.'),
      (4.4, 'Musiken stannar – stanna bollen', ''),
      (7.0, 'Musiken igen', ''),
      (11.4, 'Variant: Simon säger', 'Bara när Simon säger det.')]
finish(d, 'mk14', 'musikbollar-och-simon-sager', ['Musikbollar och', 'Simon säger'], 'Yta med koner · Alla har en boll',
       fp, 'LEK', [('box', 10, 12, 90, 88)],
       [lab(0.2, 4.4, (50, 6), 'MUSIK'), lab(4.4, 7.0, (50, 6), 'STOPP'), lab(7.0, 11.4, (50, 6), 'MUSIK'), lab(11.4, 14.0, (50, 6), '”SIMON SÄGER STOPP!”'), lab(14.0, 18, (50, 6), 'MUSIK')])

# ============ pj01 4 mot 4 + 2 ============
d = Drill()
BP = [(28, 30), (72, 32), (30, 70), (70, 68)]; RP = [(42, 42), (58, 44), (42, 58), (58, 56)]
team(d, 'b', B, BP); team(d, 'r', R, RP); team(d, 's', YEL, [(4, 50), (96, 50)], ['S', 'S'])
for k in range(4): wander(d, f'b{k}', 0, 17.9, boxes([BP[k]], 6)[0], 5200 + k, 1.6); wander(d, f'r{k}', 0, 17.9, boxes([RP[k]], 4)[0], 5210 + k, 1.6)
b = d.newball(rec(d, 's0', 0))
t = chain(d, b, 0.4, ['b0', 'b1', 'b3', 'b2', 'b0', 'b1', 'b3', 'b2'], 0.3); cnt = arrivals(d, b)[:8]       # åtta passningar
t = d.pas(b, t + 0.2, rec(d, 'b0', t + 0.9)); tq = d.pas(b, t + 0.05, rec(d, 's1', t + 1.4), 1.2)           # direkt till stödet på motsatt sida
fp = [(0, 'Fyra mot fyra plus två stöd', 'Stöden på motsatta sidor. Max två touch.'),
      (cnt[-1] - 0.3, 'Åtta passningar: 1 poäng', ''),
      (tq - 1.2, 'Direkt till stödet på motsatt sida', 'Också 1 poäng – räkningen nollställs.'),
      (tq + 0.3, 'Två block à 5 minuter', '')]
finish(d, 'pj01', '4-mot-4-plus-2-ytbesittning-med-stod', ['4 mot 4 + 2', 'Ytbesittning med stöd'], 'Yta 28 × 28 m · Två stöd utanför',
       fp, 'POSITIONSSPEL', [('box', 10, 10, 90, 90)], counter(cnt, pos=(50, 6)) + [lab(tq, tq + 1.6, (86, 40), '+1')])

# ============ pj02 Nå alla fyra stöden ============
d = Drill()
BP = [(30, 30), (70, 32), (32, 68), (68, 70)]; RP = [(44, 42), (58, 44), (44, 58), (58, 58)]; SP = [(50, 6), (94, 50), (50, 94), (6, 50)]
team(d, 'b', B, BP); team(d, 'r', R, RP); team(d, 's', B, SP, ['S'] * 4); team(d, 'w', WHITE, [(96, 88), (96, 94), (90, 96), (84, 96)], [''] * 4)
for k in range(4): wander(d, f'r{k}', 0, 17.9, boxes([RP[k]], 4)[0], 5300 + k, 1.6)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['s0', 'b1', 's1', 'b3', 's2', 'b2', 's3'], 0.3); ss = [x for i, x in enumerate(arrivals(d, b)[:7]) if i % 2 == 0]
fp = [(0, 'Fyra mot fyra inne, fyra stöd utanför', 'Tredje laget vilar.'),
      (ss[0] - 0.3, 'Nå alla fyra stöden', 'Utan att motståndarna rör bollen.'),
      (ss[3] - 0.3, 'Alla fyra: 1 poäng', ''),
      (ss[3] + 0.6, 'Lagen roterar', 'Inne, stöd och vila – fyra block à 3 min.')]
finish(d, 'pj02', 'na-alla-fyra-stoden', ['Nå alla fyra', 'stöden'], 'Yta 30 × 30 m · Fyra stöd · Tre lag roterar',
       fp, 'POSITIONSSPEL', [('box', 12, 12, 88, 88)], counter(ss, pos=(50, 50), last='+1 POÄNG'))

# ============ pj03 3 mot 3 – kungen av planen ============
d = Drill()
BP = [(32, 68), (68, 66), (50, 50)]; RP = [(36, 34), (64, 36), (50, 60)]
team(d, 'b', B, BP); team(d, 'r', R, RP); team(d, 'w', WHITE, [(96, 30), (96, 36), (96, 42)], [''] * 3)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b2', 'b1'], 0.3); t = drive(d, b, 'b1', t, (60, 22), 16); tg = shoot(d, b, t + 0.1, (52, 3)); hide(d, b, tg + 0.3)
for k, ps in enumerate([(96, 58), (96, 64), (96, 70)]): d.mv(f'r{k}', tg + 0.2, tg + 2.6, ps)               # laget som släppte in går ut
for k, ps in enumerate([(36, 34), (64, 36), (50, 60)]): d.mv(f'w{k}', tg + 0.4, tg + 2.6, ps)                # nästa lag in
b2 = d.newball((200, 200)); show(d, b2, tg + 2.7, rec(d, 'w2', tg + 2.7))
t = chain(d, b2, tg + 2.9, ['w0', 'w1'], 0.3); d.mv('b1', t - 1.2, t + 0.2, (62, 40))
fp = [(0, 'Tre mot tre med mål', 'Max två touch, max en minut per anfall.'),
      (tg - 0.4, 'Mål', 'Laget som släppte in går ut.'),
      (tg + 0.4, 'Nästa lag kommer in', ''),
      (tg + 3.0, 'Inget mål på en minut?', 'Då går anfallslaget ut.')]
finish(d, 'pj03', '3-mot-3-kungen-av-planen', ['3 mot 3', 'Kungen av planen'], 'Yta 20 × 30 m · Flera lag om tre',
       fp, 'SMÅLAGSSPEL', [('box', 14, 4, 86, 96), ('smallgoal', 50, 4), ('smallgoal', 50, 96)])

# ============ pj04 1 mot 1 – kungen av kanalen ============
d = Drill()
d.p('a', '1', B, (50, 76)); d.p('f', '2', R, (50, 30)); team(d, 'q', ORA, [(92, 44), (92, 50), (92, 56)], ['3', '4', '5'])
b = d.newball(rec(d, 'a', 0))
t = drive(d, b, 'a', 0.4, (48, 52), 14); d.mv('f', 0.4, t, (50, 44))
d.mv('a', t, t + 0.6, (58, 42)); d.carry(b, 'a', t, t + 0.6); d.mv('f', t, t + 0.6, (54, 40)); t += 0.6
d.mv('a', t, t + 1.0, (56, 18)); d.carry(b, 'a', t, t + 1.0); t += 1.0; tg = shoot(d, b, t + 0.1, (50, 9)); hide(d, b, tg + 0.3)
d.mv('f', tg, tg + 2.2, (92, 62)); d.mv('q0', tg + 0.2, tg + 1.8, (50, 30))                                  # den som släppte in går ut
for k in (1, 2): d.mv(f'q{k}', tg + 0.4, tg + 1.2, (92, 44 + 6 * (k - 1)))
b2 = d.newball((200, 200)); show(d, b2, tg + 2.0, rec(d, 'q0', tg + 2.0))
t = drive(d, b2, 'q0', tg + 2.2, (50, 50), 14); d.mv('a', tg + 0.4, t, (50, 64))
tw = win(d, b2, 'a', 'q0', t + 0.2, 0.4); d.mv('a', tw, tw + 1.4, (48, 80)); d.carry(b2, 'a', tw, tw + 1.4)
fp = [(0, '1 mot 1 i kanalen', 'De övriga väntar i kö.'),
      (tg - 0.4, 'Mål', 'Den som släppte in går ut.'),
      (tg + 2.0, 'Nästa spelare in', 'Omgångar på 30 sekunder.'),
      (tw - 0.2, 'Kungen av kanalen försvarar', '')]
finish(d, 'pj04', '1-mot-1-kungen-av-kanalen', ['1 mot 1', 'Kungen av kanalen'], 'Kanal 15 × 30 m med två mål',
       fp, 'DUELL', [('box', 30, 8, 70, 92), ('smallgoal', 50, 8), ('smallgoal', 50, 92)])

# ============ pj05 Passning mellan linjerna – tre lag ============
d = Drill()
TP = [(24, 14), (42, 14), (58, 14), (76, 14)]; MP = [(30, 48), (44, 52), (58, 48), (72, 52)]; NP = [(24, 86), (42, 86), (58, 86), (76, 86)]
team(d, 'b', B, TP); team(d, 'r', R, MP); team(d, 'w', WHITE, NP)
for k in range(4): wander(d, f'b{k}', 0, 17.9, (TP[k][0] - 5, 8, TP[k][0] + 5, 20), 5400 + k, 1.6); wander(d, f'w{k}', 0, 9.0, (NP[k][0] - 5, 80, NP[k][0] + 5, 92), 5410 + k, 1.6)
for k in range(4): wander(d, f'r{k}', 0, 6.0, boxes([MP[k]], 4)[0], 5420 + k, 1.6)
b = d.newball(rec(d, 'b1', 0))
t = d.pas(b, 0.4, rec(d, 'b2', 1.0)); t = d.pas(b, t + 0.2, rec(d, 'w3', t + 1.4), 1.2); p1 = t             # över mitten
t = d.pas(b, t + 0.3, rec(d, 'w1', t + 1.0)); t = d.pas(b, t + 0.2, rec(d, 'b0', t + 1.4), 1.2); p2 = t
t = d.pas(b, t + 0.3, rec(d, 'b3', t + 1.4)); d.mv('r3', t - 0.4, t + 0.8, (68, 46))
t2 = d.pas(b, t + 0.3, (68, 46), 0.7); tw = t2                                                              # mittlaget bryter
d.carry(b, 'r3', tw, tw + 0.4)
for k in range(4): d.mv(f'r{k}', tw + 0.4, tw + 2.4, (TP[k][0] + 2, 14)); d.mv(f'b{k}', tw + 0.4, tw + 2.4, MP[k])   # byter plats
fp = [(0, 'Tre lag om fyra', 'Mittlaget försöker bryta passningarna.'),
      (p1 - 1.0, 'Passning över mitten: 1 poäng', 'Mottagen och kontrollerad.'),
      (p2 - 1.0, 'Och tillbaka', ''),
      (tw - 0.3, 'Brytning – lagen byter plats', 'Laget som tappade går in i mitten.')]
finish(d, 'pj05', 'passning-mellan-linjerna-tre-lag', ['Passning mellan linjerna', 'Tre lag'], 'Yta 15 × 20 m · Fyra mot fyra mot fyra',
       fp, 'POSITIONSSPEL', [('box', 14, 6, 86, 94), ('line', [(14, 34), (86, 34)]), ('line', [(14, 66), (86, 66)])],
       [lab(p1, p1 + 1.4, (86, 92), '+1'), lab(p2, p2 + 1.4, (86, 8), '+1')])

# ============ pj06 Stödspelare och avslut på första touchen ============
d = Drill(); d.p('mvr', 'MV', R, (50, 6)); d.p('mvb', 'MV', B, (50, 94))
d.p('sb', 'S', B, (62, 1)); d.p('sr', 'S', R, (38, 99))
BP = [(30, 62), (70, 60), (44, 44), (58, 30), (50, 76)]; RP = [(34, 36), (66, 38), (50, 56), (42, 24), (58, 70)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
for k in range(5): wander(d, f'r{k}', 0, 6, boxes([RP[k]], 4)[0], 5500 + k, 1.6)
b = d.newball(rec(d, 'b4', 0))
t = chain(d, b, 0.4, ['b0', 'b2', 'b3'], 0.3); t = d.pas(b, t + 0.2, rec(d, 'sb', t + 1.2), 1.0); ts = t   # bollen når stödet
d.mv('b2', t - 1.0, t + 0.4, (46, 18)); t = d.pas(b, t + 0.2, rec(d, 'b2', t + 0.9)); tg = shoot(d, b, t + 0.05, (46, 7))   # avslut på första touchen
fp = [(0, 'Fem mot fem i mitten', 'Ett stöd bakom varje mål.'),
      (ts - 0.8, 'Bollen ska nå stödet', ''),
      (tg - 0.6, 'Avslut på första touchen', 'Annars går bollen tillbaka till stödet.'),
      (tg + 0.4, 'Två block à 5 minuter', '')]
finish(d, 'pj06', 'stodspelare-och-avslut-pa-forsta-touchen', ['Stödspelare och avslut', 'på första touchen'], 'Yta 20 × 40 m · Ett stöd bakom varje mål',
       fp, 'SMÅLAGSSPEL', [('box', 12, 4, 88, 96)])
C[-1]['goals'] = [(50, 2), (50, 98)]; C[-1]['keep_goals'] = True

# ============ pj07 Åtta passningar – sedan fyra mål ============
d = Drill()
GL = [(30, 6), (70, 6), (30, 94), (70, 94)]
BP = [(28, 30), (72, 32), (30, 70), (70, 68), (50, 50)]; RP = [(40, 40), (60, 42), (40, 60), (60, 58), (50, 30)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
for k in range(5): wander(d, f'r{k}', 0, 9, boxes([RP[k]], 4)[0], 5600 + k, 1.6)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b1', 'b4', 'b2', 'b3', 'b1', 'b0', 'b4', 'b3'], 0.25); cnt = arrivals(d, b)[:8]
t = drive(d, b, 'b3', t, (70, 82), 16); tg = d.pas(b, t + 0.1, (70, 94), 0.4); hide(d, b, tg + 0.3)
fp = [(0, 'Fem mot fem, fyra mål', ''),
      (cnt[2], 'Åtta passningar först', ''),
      (cnt[-1] - 0.2, 'Nu får laget göra mål', 'I vilket som helst av de fyra målen.'),
      (tg - 0.4, 'Mål', '')]
finish(d, 'pj07', 'atta-passningar-sedan-fyra-mal', ['Åtta passningar', 'sedan fyra mål'], 'Yta 30 × 30 m med fyra mål',
       fp, 'SMÅLAGSSPEL', [('box', 8, 6, 92, 94)] + [('smallgoal',) + g for g in GL], counter(cnt, pos=(50, 50), last='MÅL OK'))

# ============ pj08 Skapa 1 mot 1 ============
d = Drill(); d.p('sr', 'S', R, (50, 22)); d.p('sb', 'S', B, (50, 78))
BP = [(30, 62), (70, 60), (44, 44), (58, 52), (50, 70)]; RP = [(34, 38), (66, 40), (50, 56), (42, 46), (58, 30)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
for k in range(5): wander(d, f'r{k}', 0, 6, boxes([RP[k]], 4)[0], 5700 + k, 1.6)
b = d.newball(rec(d, 'b4', 0))
t = chain(d, b, 0.4, ['b0', 'b2'], 0.3); d.mv('b3', t - 0.8, t + 0.6, (56, 34)); t = d.pas(b, t + 0.2, rec(d, 'b3', t + 1.0)); t1 = t   # passa fram
d.mv('sr', t1 - 0.4, t1 + 0.6, (52, 26)); d.mv('b3', t1, t1 + 0.6, (60, 26)); d.carry(b, 'b3', t1, t1 + 0.6)  # 1 mot 1 mot stödet
d.mv('b3', t1 + 0.6, t1 + 1.6, (52, 6)); d.carry(b, 'b3', t1 + 0.6, t1 + 1.6); d.mv('sr', t1 + 0.6, t1 + 1.4, (54, 16)); tg = t1 + 1.6   # driver genom målet
fp = [(0, 'Fem mot fem med ett stöd bakom', ''),
      (t1 - 0.6, 'Passa fram till en spelare', ''),
      (t1 + 0.2, 'Ta 1 mot 1 mot stödet', ''),
      (tg - 0.4, 'Driv genom målet', 'Två block à 5 minuter.')]
finish(d, 'pj08', 'skapa-1-mot-1', ['Skapa', '1 mot 1'], 'Yta 20 × 40 m · Fem mot fem med ett stöd bakom',
       fp, 'SMÅLAGSSPEL', [('box', 12, 2, 88, 98), ('cone', 44, 6), ('cone', 56, 6), ('cone', 44, 94), ('cone', 56, 94)], [lab(tg, tg + 1.6, (50, 14), 'MÅL')])

# ============ pj09 Rondo 4 mot 1 med rutbyte ============
d = Drill()
BX = [(12, 12, 46, 46), (54, 12, 88, 46), (54, 54, 88, 88), (12, 54, 46, 88)]
def corners(bx): x1, y1, x2, y2 = bx; return [(x1 + 3, y1 + 3), (x2 - 3, y1 + 3), (x2 - 3, y2 - 3), (x1 + 3, y2 - 3)]
for q, bx in enumerate(BX):
    for k, ps in enumerate(corners(bx)): d.p(f'a{q}{k}', '', B, ps)
    d.p(f'f{q}', '', R, ((bx[0] + bx[2]) / 2, (bx[1] + bx[3]) / 2))
for q, bx in enumerate(BX):
    cs = corners(bx); b = d.newball(rec(d, f'a{q}0', 0)); t = 0.4 + 0.2 * q
    for rep in range(14):
        nk = [1, 2, 3, 0, 2, 0, 3, 1][rep % 8]; t = d.pas(b, t + 0.15, rec(d, f'a{q}{nk}', t + 0.7))
    cx, cy = (bx[0] + bx[2]) / 2, (bx[1] + bx[3]) / 2
    wander(d, f'f{q}', 0, 6.6, (cx - 6, cy - 6, cx + 6, cy + 6), 5800 + q, 1.2)
    nq = (q + 1) % 4; nb = BX[nq]
    d.mv(f'f{q}', 6.8, 9.0, ((nb[0] + nb[2]) / 2 + (2 if q % 2 else -2), (nb[1] + nb[3]) / 2))                   # byter ruta medurs
    wander(d, f'f{q}', 9.0, 17.9, ((nb[0] + nb[2]) / 2 - 6, (nb[1] + nb[3]) / 2 - 6, (nb[0] + nb[2]) / 2 + 6, (nb[1] + nb[3]) / 2 + 6), 5810 + q, 1.2)
fp = [(0, 'Fyra mot ett i varje ruta', 'Rutor 8 × 8 m.'),
      (3.0, 'Tio passningar', ''),
      (6.8, 'Försvararen byter ruta medurs', 'Efter tio passningar eller på signal.'),
      (11.0, 'Alla ska vara försvarare två gånger', 'Tio block à 1 minut.')]
finish(d, 'pj09', 'rondo-4-mot-1-med-rutbyte', ['Rondo 4 mot 1', 'Med rutbyte'], 'Flera rutor 8 × 8 m',
       fp, 'RONDO', [('box',) + bx for bx in BX], [lab(6.6, 8.8, (50, 50), 'BYT RUTA')])

# ============ pj10 6 mot 6 + 2 – vinn och spela ut ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
GATES = [(14, 30), (86, 30), (14, 70), (86, 70)]
BP = [(30, 46), (70, 46), (40, 30), (60, 30), (34, 62), (66, 62)]; RP = [(36, 22), (64, 22), (46, 40), (56, 40), (30, 54), (70, 54)]
team(d, 'b', B, BP); team(d, 'r', R, RP); team(d, 'j', YEL, [(50, 52), (50, 70)], ['J', 'J'])
b = d.newball(rec(d, 'b4', 0))
t = chain(d, b, 0.4, ['j0', 'b1'], 0.3)
tw = win(d, b, 'r5', 'b1', t + 0.3, 0.7)                                                                     # försvararna vinner bollen
t = d.pas(b, tw + 0.2, rec(d, 'r4', tw + 1.2)); t = d.pas(b, t + 0.2, rec(d, 'j1', t + 0.9))
d.mv('r4', t - 0.8, t + 1.2, (16, 76)); t = d.pas(b, t + 0.2, rec(d, 'r4', t + 1.2))                           # genom en diagonal port
d.mv('r4', t, t + 0.8, (12, 66)); d.carry(b, 'r4', t, t + 0.8); tp = t + 0.6
fp = [(0, 'Sex mot sex plus två jokrar', 'Två touch, sista passningen fritt.'),
      (tw - 0.2, 'Försvararna vinner bollen', ''),
      (tp - 1.4, 'För bollen genom en diagonal port', 'Först då får de anfalla.'),
      (tp + 0.4, 'Nu anfaller rött', '')]
finish(d, 'pj10', '6-mot-6-plus-2-vinn-och-spela-ut', ['6 mot 6 + 2', 'Vinn och spela ut'], 'Yta 30 × 50 m · Två mål och fyra diagonala portar',
       fp, 'SPELÖVNING', [('cone', x + dx, y + dy) for x, y in GATES for dx, dy in ((-3, -3), (3, 3))], [lab(tp, tp + 1.6, (20, 62), 'UT')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

if __name__ == '__main__': render(C, sys.argv)
