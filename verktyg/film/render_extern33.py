# Externa övningar, omgång 33 (tolv st). Regel: först d.mv, sedan d.carry; först mottagarens rörelse, sedan passningen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e9', __file__.replace('render_extern33.py', 'render_extern9.py'))
e9 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e9); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e9.finish, e9.rec, e9.chain, e9.wander, e9.counter, e9.arrivals
lab, hide, show, team, boxes, drive, shoot = e9.lab, e9.hide, e9.show, e9.team, e9.boxes, e9.drive, e9.shoot
factor, swap_color, stand, countdown, countup, win = e9.factor, e9.swap_color, e9.stand, e9.countdown, e9.countup, e9.win
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'

# ============ wa10 Alla vill höra till – jokerspelet ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96))
BP = [(30, 66), (70, 64), (44, 48), (58, 80)]; RP = [(34, 36), (66, 34), (52, 56), (44, 22)]
team(d, 'b', B, BP); team(d, 'r', R, RP); d.p('j', 'J', YEL, (50, 40))
for k in range(4): wander(d, f'r{k}', 0, 6, boxes([RP[k]], 4)[0], 11000 + k, 1.6)
b = d.newball(rec(d, 'b0', 0))
t = d.pas(b, 0.4, rec(d, 'j', 1.3)); t = d.pas(b, t + 0.3, rec(d, 'b1', t + 1.1))
d.mv('b2', t - 1.0, t + 0.6, (46, 22)); t = d.pas(b, t + 0.2, rec(d, 'b2', t + 1.0)); tg = shoot(d, b, t + 0.05, (46, 1)); hide(d, b, tg + 0.3)
b2 = d.newball((200, 200)); show(d, b2, tg + 0.8, rec(d, 'mvr', tg + 0.8))
d.mv('j', tg, tg + 1.6, (52, 58)); t = d.pas(b2, tg + 1.0, rec(d, 'r2', tg + 2.0), 1.0); t = d.pas(b2, t + 0.3, rec(d, 'j', t + 1.0))
t = d.pas(b2, t + 0.3, rec(d, 'r1', t + 1.1))
fp = [(0, 'Jokern spelar med laget som har bollen', 'Två jämna lag och en joker.'),
      (1.4, 'Använd jokern', 'Jokern får inte göra mål.'),
      (tg + 0.8, 'Nu spelar jokern med rött', ''),
      (tg + 3.0, 'Byt joker var tredje minut', 'Så att alla får prova. Variant: två jokrar.')]
finish(d, 'wa10', 'alla-vill-hora-till-jokerspelet', ['Alla vill höra till', 'Jokerspelet'], 'Plan 35 × 50 m · Två mål',
       fp, 'ÖVERLÄGE', [])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ wa11 Ingen lämnas utanför – målspelaren ============
d = Drill()
BP = [(30, 66), (70, 64), (50, 48)]; RP = [(34, 36), (66, 34), (52, 56)]
team(d, 'b', B, BP); team(d, 'r', R, RP); d.p('bm', 'M', B, (50, 8)); d.p('rm', 'M', R, (50, 92))
d.p('fm', '', R, (56, 14))
wander(d, 'bm', 0, 4.0, (36, 4, 64, 14), 11100, 1.4); wander(d, 'rm', 0, 17.9, (36, 86, 64, 96), 11101, 1.4)
b = d.newball(rec(d, 'b0', 0))
t = d.pas(b, 0.4, rec(d, 'b2', 1.2)); d.mv('fm', 1.0, t, (54, 12))                                          # försvaret markerar målspelaren
d.mv('bm', 4.0, t + 1.2, (36, 8)); t = d.pas(b, t + 0.3, rec(d, 'bm', t + 1.4), 1.2); tg = t                  # passning till egna målspelaren = mål
d.mv('fm', tg - 1.0, tg, (42, 12))
d.mv('bm', tg + 0.4, tg + 2.4, (40, 62)); d.mv('b2', tg + 0.4, tg + 2.4, (50, 8))                            # byt målspelare
fp = [(0, 'En målspelare i motståndarnas slutzon', 'Plan 35 × 35 m.'),
      (1.4, 'Försvaret får markera målspelaren', ''),
      (tg - 0.6, 'Passning till målspelaren = mål', ''),
      (tg + 0.4, 'Byt målspelare efter varje mål', 'Ingen lämnas utanför.')]
finish(d, 'wa11', 'ingen-lamnas-utanfor-malspelaren', ['Ingen lämnas utanför', 'Målspelaren'], 'Plan 35 × 35 m med slutzoner',
       fp, 'SMÅLAGSSPEL', [('box', 8, 2, 92, 98), ('zone', 8, 2, 92, 16, (200, 220, 200), 'SLUTZON'), ('zone', 8, 84, 92, 98, (200, 220, 200), 'SLUTZON')],
       [lab(tg, tg + 1.6, (64, 20), 'MÅL')])

# ============ wa12 Spelarnas regler ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96))
BP = [(40, 54), (48, 58), (56, 54), (44, 62)]; RP = [(40, 44), (48, 40), (56, 44), (52, 36)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
for k in range(4): stand(d, f'b{k}', 0, 3.0); stand(d, f'r{k}', 0, 3.0)                                        # kommer överens om reglerna
NB = [(30, 66), (70, 64), (44, 48), (58, 80)]; NR = [(34, 36), (66, 34), (52, 56), (44, 22)]
for k in range(4): d.mv(f'b{k}', 3.0, 4.6, NB[k]); d.mv(f'r{k}', 3.0, 4.6, NR[k])
b = d.newball((200, 200)); show(d, b, 4.6, rec(d, 'b0', 4.6))
t = d.pas(b, 4.8, rec(d, 'b2', 5.6)); t = d.pas(b, t + 0.3, rec(d, 'b1', t + 1.1)); t = drive(d, b, 'b1', t, (62, 24), 16)
tg = shoot(d, b, t + 0.1, (54, 1))
fp = [(0, 'Kom överens om reglerna', 'Två minuter innan matchen.'),
      (3.0, 'Spela – ingen domare', 'Oenighet löser spelarna själva.'),
      (tg - 0.6, 'Mål', ''),
      (tg + 0.4, 'Efteråt: vilka regler fungerade?', 'Inspirerat av ”No Rules” från Kenya.')]
finish(d, 'wa12', 'spelarnas-regler', ['Spelarnas', 'regler'], 'Plan 30 × 40 m · Två mål',
       fp, 'SMÅLAGSSPEL', [], [lab(0.4, 3.0, (50, 26), 'VÅRA REGLER?')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ wa13 Eweite – kapplöpning till bollen ============
d = Drill()
for k in range(3): d.p(f'b{k}', '', B, (40 + 8 * k, 92)); d.p(f'r{k}', '', R, (44 + 8 * k, 8))
b = d.newball((51.8, 48.8))
d.mv('b0', 0.6, 2.6, (48, 52)); d.mv('r0', 0.6, 2.8, (54, 44))                                               # båda springer mot bollen
t = drive(d, b, 'b0', 2.6, (46, 30), 14); d.mv('r0', 2.8, t, (50, 24))                                         # först anfaller
d.mv('b0', t, t + 0.6, (38, 20)); d.carry(b, 'b0', t, t + 0.6); t += 0.6
d.mv('b0', t, t + 1.0, (36, 8)); d.carry(b, 'b0', t, t + 1.0); tw = t + 0.8; d.mv('r0', t, t + 1.0, (42, 14))
fp = [(0, 'Två led på varsin kortlinje', 'Leken kommer från Kenya.'),
      (0.6, 'Spring till bollen', 'Lika långt för båda.'),
      (2.8, 'Först till bollen anfaller', 'Den andra försvarar.'),
      (tw, 'Över motståndarnas linje', 'Variant: starta liggande eller sittande.')]
finish(d, 'wa13', 'eweite-kapplopning-till-bollen', ['Eweite', 'Kapplöpning till bollen'], 'Bana ca 30 m · En boll i mitten',
       fp, 'DUELL', [('line', [(20, 8), (80, 8)]), ('line', [(20, 92), (80, 92)])], [lab(tw, tw + 1.6, (36, 16), 'ÖVER')])

# ============ wa14 Fiskaren kommer ============
d = Drill(); d.p('f', 'F', R, (50, 50))
ST = [(24, 30), (50, 24), (76, 30), (24, 70), (50, 76), (76, 70), (36, 50), (64, 50)]
balls = []
for k, ps in enumerate(ST): d.p(f'p{k}', '', B, ps); balls.append(d.newball(rec(d, f'p{k}', 0)))
for k in range(8): wander(d, f'p{k}', 0, 3.0, boxes([ST[k]], 6)[0], 11200 + k, 2.4); wander(d, f'p{k}', 3.0, 6.0, boxes([ST[k]], 6)[0], 11210 + k, 1.0)
tc = 6.2
for k, (x, y) in enumerate(ST):
    if k == 6: continue
    d.mv(f'p{k}', tc, tc + 2.6, (4 if x < 50 else 96, y))                                                    # fly över sidlinjen
d.mv('p6', tc, tc + 1.6, (26, 50)); d.mv('f', tc, tc + 1.6, (30, 50)); tf = tc + 1.6; stand(d, 'p6', tf, tf + 1.6)
for k in range(8): d.carry(balls[k], f'p{k}', 0, 17.9)
wander(d, 'p6', tf + 1.6, 17.9, (30, 40, 70, 60), 11220, 1.6); wander(d, 'f', tf + 1.6, 17.9, (34, 34, 66, 66), 11221, 1.6)
for k, (x, y) in enumerate(ST):
    if k != 6: d.mv(f'p{k}', tf + 2.4, tf + 4.0, (x, y)); wander(d, f'p{k}', tf + 4.0, 17.9, boxes([ST[k]], 6)[0], 11230 + k, 1.6)
fp = [(0, '”Lugnt hav” – långsam dribbling', 'Tränaren är fiskare.'),
      (3.0, '”Stormigt hav” – snabbt', ''),
      (tc, '”Fiskaren kommer!”', 'Fly över sidlinjerna med bollen.'),
      (tf, 'Fångad – nu är du också fiskare', '')]
finish(d, 'wa14', 'fiskaren-kommer', ['Fiskaren', 'kommer'], 'Plan med koner · Alla med boll',
       fp, 'LEK MED BOLL', [('box', 8, 10, 92, 90)], [lab(0.2, 3.0, (50, 4), 'LUGNT HAV'), lab(3.0, 6.0, (50, 4), 'STORMIGT HAV'), lab(tc, tc + 1.8, (50, 4), '”FISKAREN KOMMER!”')])
f = factor(fp); ids = {k: i for i, k in enumerate(d.order)}
swap_color(ids['p6'], (tf + 0.4) * f, B, R)

# ============ wa15 Rädda din skatt ============
d = Drill()
ZB = (50, 88); ZR = (50, 12)
team(d, 'b', B, [(30, 74), (50, 70), (70, 74)], ['', '', '']); team(d, 'r', R, [(30, 26), (50, 30), (70, 26)], ['', '', ''])
rb = [d.newball((44 + 6 * k, 10)) for k in range(3)]; bb = [d.newball((44 + 6 * k, 90)) for k in range(3)]
for k in range(3):
    t0 = 0.4 + 0.5 * k
    d.mv(f'b{k}', t0, t0 + 2.4, (42 + 6 * k, 12)); d.mv(f'b{k}', t0 + 2.6, t0 + 5.8, (40 + 8 * k, 84)); d.carry(rb[k], f'b{k}', t0 + 2.6, t0 + 5.8)   # dribblar hem en skatt
    d.mv(f'r{k}', t0 + 0.2, t0 + 2.6, (42 + 6 * k, 88)); d.mv(f'r{k}', t0 + 2.8, t0 + 6.0, (40 + 8 * k, 16)); d.carry(bb[k], f'r{k}', t0 + 2.8, t0 + 6.0)
fp = [(0, 'Två lag, varsin zon med bollar', ''),
      (1.0, 'Hämta motståndarnas bollar', 'En i taget, bara med fötterna.'),
      (3.4, 'Dribbla hem till din zon', ''),
      (7.0, 'Variant: hinder på vägen', 'Eller använd målen som skattkammare.')]
finish(d, 'wa15', 'radda-din-skatt', ['Rädda din', 'skatt'], 'Två zoner med lika många bollar',
       fp, 'LEK MED BOLL', [('zone', 26, 2, 74, 18, (230, 120, 110), 'SKATT'), ('zone', 26, 82, 74, 98, (120, 170, 230), 'SKATT')])

# ============ wa16 Prickskytte ============
d = Drill()
TG = [(20, 20), (80, 22), (50, 50), (22, 78), (78, 80)]
ST = [(36, 30), (64, 36), (34, 64), (66, 66)]
balls = []
for k, ps in enumerate(ST): d.p(f'p{k}', '', B, ps); balls.append(d.newball(rec(d, f'p{k}', 0)))
ex = []
for k in range(4):
    t = 0.4 + 0.4 * k
    for j, gi in enumerate([(k) % 5, (k + 2) % 5]):
        gx, gy = TG[gi]; px, py = d.pos(f'p{k}')
        ax, ay = gx + (px - gx) * 0.5, gy + (py - gy) * 0.5
        t1 = d.path(f'p{k}', t, [(ax, ay)], 1.2); d.carry(balls[k], f'p{k}', t, t1)
        th = d.pas(balls[k], t1 + 0.1, (gx, gy + 2), 0.5); t2 = d.pas(balls[k], th, (gx + 4, gy + 6), 1.0)
        if k == 0: ex.append(lab(th, th + 1.0, (gx, gy - 8), 'TRÄFF'))
        d.mv(f'p{k}', t1 + 0.2, t2, (gx + 2.2, gy + 7.2)); d.carry(balls[k], f'p{k}', t2, t2 + 0.6); t = t2 + 0.6
fp = [(0, 'Dribbla och skjut på valfritt mål', 'En boll var.'),
      (2.0, 'Ett poäng per träff', ''),
      (5.0, 'Inte samma mål två gånger i rad', ''),
      (9.0, 'Variant: en försvarare per mål', 'Eller tränaren som stör.')]
finish(d, 'wa16', 'prickskytte', ['Prick-', 'skytte'], 'Lådor, hinkar eller koner som mål',
       fp, 'AVSLUT', [('box', 6, 6, 94, 94)] + [('yellowcone',) + g for g in TG], ex)

# ============ wa17 Galna regler-turneringen ============
d = Drill()
BP = [(30, 66), (66, 64), (48, 48)]; RP = [(34, 36), (62, 34), (52, 56)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
for k in range(3): wander(d, f'r{k}', 0, 17.9, boxes([RP[k]], 4)[0], 11300 + k, 1.6)
b = d.newball(rec(d, 'b0', 0)); ex = []
t = d.pas(b, 0.4, rec(d, 'b2', 1.2)); t = drive(d, b, 'b2', t, (50, 16), 16); tg = d.pas(b, t + 0.1, (50, 4), 0.4); hide(d, b, tg + 0.3)
ex.append(lab(0.2, tg + 0.4, (82, 94), 'VANLIG RUNDA'))
b2 = d.newball((200, 200)); show(d, b2, tg + 1.0, rec(d, 'b1', tg + 1.0)); t = tg + 1.2
for pid in ['b0', 'b2', 'b1']: t = d.pas(b2, t + 0.3, rec(d, pid, t + 1.0))   # alla måste ha rört bollen
t = drive(d, b2, 'b1', t, (52, 16), 16); tg2 = d.pas(b2, t + 0.1, (50, 4), 0.4)
ex.append(lab(tg + 0.8, tg2 + 1.6, (78, 94), 'NY REGEL: ALLA RÖR BOLLEN'))
fp = [(0, 'Spela en vanlig runda', 'Fyra eller fler lag.'),
      (tg + 0.8, 'Ny regel var 2–3 minut', 'Varje ny regel ersätter den förra.'),
      (tg + 2.0, 'Alla måste ha rört bollen innan mål', 'Eller bara svaga foten, max två touch …'),
      (tg2 - 0.2, 'Poängen följer med', 'Mest mål totalt vinner.')]
finish(d, 'wa17', 'galna-regler-turneringen', ['Galna regler-', 'turneringen'], 'Två eller fler små planer · Fyra eller fler lag',
       fp, 'SMÅLAGSSPEL', [('box', 10, 4, 90, 96), ('smallgoal', 50, 4), ('smallgoal', 50, 96)], ex)

# ============ wj01 Isoni – frysta kull med boll ============
d = Drill(); team(d, 'o', R, [(40, 46), (62, 54)], ['', ''])
ST = [(22, 24), (50, 20), (78, 26), (22, 76), (50, 80), (78, 74), (30, 52)]
balls = []
for k, ps in enumerate(ST): d.p(f'p{k}', '', B, ps); balls.append(d.newball(rec(d, f'p{k}', 0)))
for k in (1, 2, 3, 4, 5): wander(d, f'p{k}', 0, 17.9, boxes([ST[k]], 6)[0], 11400 + k, 1.6); d.carry(balls[k], f'p{k}', 0, 17.9)
d.mv('p6', 0, 2.6, (28, 58)); d.carry(balls[6], 'p6', 0, 2.6); d.mv('o0', 0.3, 2.6, (32, 56)); tk = 2.6
stand(d, 'p6', tk, 6.4); hide(d, balls[6], tk + 0.1)                                                       # fryser, bollen i händerna
d.mv('p0', 0, 4.2, (24, 46)); d.carry(balls[0], 'p0', 0, 4.4)
t1 = d.pas(balls[0], 4.6, (28, 58), 0.4); t2 = d.pas(balls[0], t1, (32, 68), 0.4); d.mv('p0', 4.6, t2 + 0.2, (30, 70)); tr = t1   # passa mellan benen
d.carry(balls[0], 'p0', t2 + 0.2, 17.9); wander(d, 'p0', t2 + 0.2, 17.9, boxes([ST[0]], 6)[0], 11410, 1.6)
show(d, balls[6], 6.4, rec(d, 'p6', 6.4)); wander(d, 'p6', 6.4, 17.9, boxes([ST[6]], 6)[0], 11416, 1.6); d.carry(balls[6], 'p6', 6.4, 17.9)
wander(d, 'o0', 2.8, 17.9, (36, 36, 64, 64), 11420, 1.6); wander(d, 'o1', 0, 17.9, (50, 44, 70, 64), 11421, 1.6)
fp = [(0, 'Två jagare (oni) utan boll', 'Japansk kull-lek som JFA använder.'),
      (tk, 'Kullad: frys med benen isär', 'Bollen i händerna.'),
      (tr - 0.4, 'Kompisen passar mellan benen', 'Då är du fri.'),
      (10.0, 'Byt oni efter en minut', '')]
finish(d, 'wj01', 'isoni-frysta-kull-med-boll', ['Isoni', 'Frysta kull med boll'], 'Avgränsad yta · Alla med boll',
       fp, 'LEK MED BOLL', [('box', 12, 12, 88, 88)], [lab(tk, tr, (28, 46), 'FRUSEN'), lab(tr, tr + 1.6, (28, 46), 'FRI')])

# ============ wj02 Ringoni – frizoner med boll ============
d = Drill(); team(d, 'o', R, [(40, 46), (62, 54)], ['', ''])
RG = [(26, 28), (74, 28), (26, 72), (74, 72), (50, 50)]
ST = [(40, 22), (60, 22), (40, 78), (60, 78), (16, 50), (84, 50)]
balls = []
for k, ps in enumerate(ST): d.p(f'p{k}', '', B, ps); balls.append(d.newball(rec(d, f'p{k}', 0)))
for k in (2, 3, 4, 5): wander(d, f'p{k}', 0, 17.9, boxes([ST[k]], 6)[0], 11500 + k, 1.6); d.carry(balls[k], f'p{k}', 0, 17.9)
d.mv('p0', 0, 2.0, (28, 30)); stand(d, 'p0', 2.0, 6.0); d.carry(balls[0], 'p0', 0, 6.0)                        # säker i ringen – fem sekunder
d.mv('p1', 0, 5.0, (36, 36)); d.mv('p1', 5.0, 6.0, (27, 30)); d.carry(balls[1], 'p1', 0, 6.0)                  # ny spelare kommer – den gamla lämnar
d.mv('p0', 6.0, 8.0, (44, 30)); wander(d, 'p0', 8.0, 17.9, boxes([ST[0]], 6)[0], 11510, 1.6); d.carry(balls[0], 'p0', 6.0, 17.9)
stand(d, 'p1', 6.0, 9.0); wander(d, 'p1', 9.0, 17.9, boxes([ST[1]], 6)[0], 11511, 1.6); d.carry(balls[1], 'p1', 6.0, 17.9)
wander(d, 'o0', 0, 17.9, (34, 36, 50, 64), 11520, 1.6); wander(d, 'o1', 0, 17.9, (52, 36, 68, 64), 11521, 1.6)
fp = [(0, 'Två jagare, alla andra dribblar', 'Ringar som frizoner.'),
      (2.0, 'Sulan på bollen i ringen = säker', 'Bara i fem sekunder och en åt gången.'),
      (5.6, 'Kommer en ny spelare måste du lämna', ''),
      (9.0, 'Inspirerat av JFA Kids', '”Hula hoop-oni”.')]
finish(d, 'wj02', 'ringoni-frizoner-med-boll', ['Ringoni', 'Frizoner med boll'], 'Avgränsad yta med 4–6 ringar',
       fp, 'LEK MED BOLL', [('box', 8, 10, 92, 90)] + [('circle', x, y, 6.0) for x, y in RG], countdown(2.0, 5, (26, 18), 0.8))

# ============ wj03 Konernas krig – välta och resa ============
d = Drill()
CN = [(24, 30), (50, 26), (76, 32), (34, 56), (66, 52), (26, 78), (52, 76), (76, 74)]
team(d, 'b', B, [(14, 14), (86, 14), (14, 90)], ['', '', '']); team(d, 'r', R, [(50, 44), (40, 66), (64, 66)], ['', '', ''])
bb = [d.newball(rec(d, f'b{k}', 0)) for k in range(3)]; ex = []
for k, (ci, t0) in enumerate([(0, 0.6), (2, 1.0), (5, 1.4)]):
    cx, cy = CN[ci]; px, py = d.pos(f'b{k}')
    d.mv(f'b{k}', t0, t0 + 1.0, (px + (cx - px) * 0.4, py + (cy - py) * 0.4)); d.carry(bb[k], f'b{k}', t0, t0 + 1.0)
    th = d.pas(bb[k], t0 + 1.1, (cx, cy), 0.6); ex.append(lab(th, th + 1.2, (cx, cy - 7), 'VÄLT'))
    d.mv(f'b{k}', th - 0.4, th + 0.8, (cx + 3, cy + 4)); d.carry(bb[k], f'b{k}', th + 0.8, 17.9)
    wander(d, f'b{k}', th + 0.8, 17.9, (cx - 8, cy - 6, cx + 8, cy + 8), 11600 + k, 1.6)
for k, ci in enumerate([1, 0, 5]):                                                                         # reser upp konerna
    cx, cy = CN[[2, 0, 5][k]]; d.mv(f'r{k}', 2.6 + k, 4.4 + k, (cx + 2, cy + 3)); stand(d, f'r{k}', 4.4 + k, 5.4 + k)
    ex.append(lab(4.4 + k, 5.4 + k, (cx, cy - 7), 'REST'))
    wander(d, f'r{k}', 5.4 + k, 17.9, (cx - 10, cy - 8, cx + 10, cy + 8), 11610 + k, 1.6)
fp = [(0, 'Ett lag välter koner med passningar', 'Det andra reser upp dem.'),
      (2.0, 'Träff – konen välts', ''),
      (4.4, 'Res upp den igen', ''),
      (9.0, 'Räkna konerna som ligger ner vid slutsignalen', 'Byt roller.')]
finish(d, 'wj03', 'konernas-krig-valta-och-resa', ['Konernas krig', 'Välta och resa'], 'Många koner utspridda · Hälften med boll',
       fp, 'LEK MED BOLL', [('box', 6, 6, 94, 94)] + [('cone',) + c for c in CN], ex)

# ============ wj04 Rull-dodgeball med fötterna ============
d = Drill()
RL = [(14, 30), (86, 30), (50, 88)]; ST = [(36, 36), (60, 34), (44, 54), (64, 58), (50, 70)]
team(d, 'r', ORA, RL, ['', '', '']); team(d, 'p', B, ST, [''] * 5)
for k in range(5): wander(d, f'p{k}', 0, 17.9, boxes([ST[k]], 6)[0], 11700 + k, 1.4)
ex = []
for k, (rk, tgt, t0) in enumerate([(0, 'p0', 0.6), (1, 'p3', 2.4), (2, 'p4', 4.2), (0, 'p2', 7.0)]):
    bb = d.newball(rec(d, f'r{rk}', t0)); tx, ty = at(d.pl[tgt]['tr'], t0 + 1.0)
    hit = k != 1
    th = d.pas(bb, t0, (tx, ty + 1) if hit else (tx + 8, ty - 6), 1.0)
    t2 = d.pas(bb, th, (tx + (12 if tx < 50 else -12), ty + 10), 0.6); hide(d, bb, t2 + 0.1)
    if hit: ex.append(lab(th, th + 1.2, (tx, ty - 8), 'TRÄFF'))
fp = [(0, 'Tre spelare med boll passar längs marken', 'Mot de andras fötter.'),
      (1.6, 'Träffad på fötterna – bli rullare', ''),
      (5.0, 'Bara passningar längs marken', ''),
      (9.0, 'Sista spelaren utan boll vinner', 'Inspirerat av japanska ”korogashi-dodge”.')]
finish(d, 'wj04', 'rull-dodgeball-med-fotterna', ['Rull-dodgeball', 'Med fötterna'], 'Ruta 15 × 15 m',
       fp, 'LEK', [('box', 20, 20, 80, 80)], ex)

if __name__ == '__main__': render(C, sys.argv)
