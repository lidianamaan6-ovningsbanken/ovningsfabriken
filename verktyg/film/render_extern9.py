# Externa övningar, omgång 9 (tolv st). Regel: först d.mv, sedan d.carry; hide före show.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e4', __file__.replace('render_extern9.py', 'render_extern4.py'))
e4 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e4); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e4.finish, e4.rec, e4.chain, e4.wander, e4.counter, e4.arrivals
lab, hide, show, team, boxes, drive, shoot = e4.lab, e4.hide, e4.show, e4.team, e4.boxes, e4.drive, e4.shoot
factor, swap_color, stand = e4.factor, e4.swap_color, e4.stand
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'
def countdown(t0, n, pos, step=1.0): return [lab(t0 + i * step, t0 + (i + 1) * step, pos, str(n - i)) for i in range(n)]
def countup(t0, n, pos, step=1.0): return [lab(t0 + i * step, t0 + (i + 1) * step, pos, str(i + 1)) for i in range(n)]
def win(d, b, thief, victim, t, lead=0.9):
    d.mv(thief, t - lead, t + 0.2, rec(d, victim, t + 0.2)); return d.pas(b, t + 0.3, rec(d, thief, t + 0.5), 0.3)

# ============ oa4 3 mot 3 med snabba starter ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96)); d.p('t', 'T', T_COL, (97, 50))
BP = [(30, 62), (66, 58), (50, 40)]; RP = [(36, 34), (64, 30), (52, 60)]; team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b1', 'b2'], 0.3); tout = d.pas(b, t + 0.2, (72, -3), 0.7); hide(d, b, tout + 0.1)   # skott utanför
b2 = d.newball(rec(d, 't', 0)); t = d.pas(b2, tout + 0.3, rec(d, 'b1', tout + 1.0))                         # ny boll direkt
tw = win(d, b2, 'r1', 'b1', t + 0.4); p = [tw]
d.mv('r2', tw - 0.6, tw + 0.9, (54, 74)); t = d.pas(b2, tw + 0.2, rec(d, 'r2', tw + 0.9)); p.append(t)
d.mv('r0', tw, t + 0.8, (40, 80)); t = d.pas(b2, t + 0.2, rec(d, 'r0', t + 0.8)); p.append(t); tg = shoot(d, b2, t + 0.05, (46, 99))
d.mv('b0', tw, tg, (44, 74)); d.mv('b2', tw, tg, (56, 66))
fp = [(0, 'Tre mot tre med målvakter', 'Tränaren har nya bollar vid sidan.'),
      (tout - 0.4, 'Bollen går ut', 'Tränaren spelar in en ny boll direkt.'),
      (tw - 0.2, 'Bollvinst', 'Mål på högst tre passningar ger 1 extra poäng.'),
      (tg - 0.3, 'Snabbt mål: extrapoäng', '')]
finish(d, 'oa4', '3-mot-3-med-snabba-starter', ['3 mot 3', 'Med snabba starter'], 'Plan 25 × 20 m · Mål och målvakter',
       fp, 'SMÅLAGSSPEL', [('box', 12, 2, 88, 98)], [lab(tout, tout + 1.2, (72, 8), 'UT'), lab(tg, tg + 1.8, (46, 88), '+1 EXTRA')] + counter(p[1:], pos=(84, 70), last=None))
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ oa5 Kontring från målvaktens utkast ============
d = Drill(); d.p('mvb', 'MV', B, (50, 4)); d.p('mvr', 'MV', R, (50, 96))
AP = [(30, 30), (50, 24), (70, 32), (44, 44)]; BP = [(30, 22), (50, 16), (68, 20), (60, 56)]
team(d, 'a', R, AP, ['A'] * 4); team(d, 'b', B, BP, ['B'] * 4)
b = d.newball(rec(d, 'a3', 0))
t = chain(d, b, 0.4, ['a0', 'a1'], 0.3); tsh = shoot(d, b, t + 0.1, (50, 6)); d.mv('mvb', tsh - 0.3, tsh, (50, 6))   # målvakten fångar
d.carry(b, 'mvb', tsh, tsh + 0.4)
for k, ps in enumerate([(14, 40), (40, 34), (84, 40)]): d.mv(f'b{k}', tsh - 0.2, tsh + 1.2, ps)
t = d.pas(b, tsh + 0.5, rec(d, 'b2', tsh + 1.5), 1.0); t0 = tsh + 0.5                                 # utkast
t = drive(d, b, 'b2', t, (78, 62), 26); d.mv('b3', t0, t + 0.8, (56, 78)); t = d.pas(b, t + 0.1, rec(d, 'b3', t + 0.8))
tg = shoot(d, b, t + 0.05, (46, 99))
for k, ps in enumerate([(30, 48), (50, 44), (70, 52), (50, 64)]): d.mv(f'a{k}', tsh + 0.3, tg, ps)
fp = [(0, 'Lag A anfaller mot målvakten', 'Halv plan med två mål.'),
      (tsh - 0.3, 'Målvakten fångar bollen', 'Lag B startar kontringen.'),
      (t0, 'Utkast – åtta sekunder', 'Mål inom 8 sekunder ger 2 poäng.'),
      (tg - 0.3, 'Mål på kontringen: 2 poäng', 'Byt efter tre minuter.')]
finish(d, 'oa5', 'kontring-fran-malvaktens-utkast', ['Kontring från', 'målvaktens utkast'], 'Halv plan · Två mål med målvakter',
       fp, 'KONTRING', [], countdown(t0, 8, (88, 60), (tg - t0) / 5) + [lab(tg, tg + 1.8, (46, 88), '+2')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ of1 Fem sekunders jakt ============
d = Drill(); d.p('t', 'T', T_COL, (97, 50))
BP = [(30, 62), (70, 62), (44, 44), (60, 30)]; RP = [(34, 34), (66, 40), (48, 60), (54, 76)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b2', 'b3'], 0.3)
tl = win(d, b, 'r1', 'b3', t); t = d.pas(b, tl + 0.3, rec(d, 'r2', tl + 1.0))                          # blått tappar
for k, ps in [(3, (62, 46)), (2, (50, 54)), (1, (60, 68))]: d.mv(f'b{k}', tl, tl + 1.4, ps)             # jagar direkt
tw = win(d, b, 'b2', 'r2', t + 0.4, 0.7)                                                                 # inom fem sekunder
t = d.pas(b, tw + 0.3, rec(d, 'b0', tw + 1.0)); t = drive(d, b, 'b0', t, (34, 14), 24); tg = shoot(d, b, t, (36, 7)); hide(d, b, tg + 0.3)
fp = [(0, 'Fyra mot fyra med småmål', 'Laget som tappar bollen har fem sekunder.'),
      (tl - 0.2, 'Bollförlust – jaga!', 'Tränaren räknar högt.'),
      (tw - 0.2, 'Tillbaka inom fem sekunder: 2 poäng', ''),
      (tw + 0.6, 'Anfall direkt', 'Mål i småmålet.')]
finish(d, 'of1', 'fem-sekunders-jakt', ['Fem sekunders', 'jakt'], 'Plan 30 × 25 m med småmål · Fyra mot fyra',
       fp, 'OMSTÄLLNING', [('box', 8, 8, 92, 92), ('smallgoal', 36, 8), ('smallgoal', 64, 8), ('smallgoal', 36, 92), ('smallgoal', 64, 92)],
       countup(tl + 0.1, 3, (84, 76), (tw - tl) / 3) + [lab(tw, tw + 1.8, (50, 86), '+2')])

# ============ of2 Tappa och återta i rutan ============
d = Drill()
BP = [(10, 34), (40, 32), (14, 66), (42, 66), (26, 50)]; RP = [(20, 40), (34, 42), (22, 58), (34, 58), (33, 50)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b2', 'b4'], 0.3)
d.mv('b1', t - 1.4, t + 0.4, (66, 36)); t = d.pas(b, t + 0.2, rec(d, 'b1', t + 1.3)); tsw = t            # spelvändning till andra rutan
MB = [(60, 34), (66, 36), (62, 66), (88, 66), (76, 50)]; MR = [(70, 40), (84, 40), (70, 58), (82, 58), (88, 30)]
for k in range(5):
    if k != 1: d.mv(f'b{k}', tsw - 0.6, tsw + 1.6, MB[k])
    d.mv(f'r{k}', tsw - 0.4, tsw + 1.6, MR[k])
t = chain(d, b, tsw + 1.6, ['b4', 'b3'], 0.3)
tl = win(d, b, 'r3', 'b3', t); t = d.pas(b, tl + 0.3, rec(d, 'r2', tl + 1.0))                           # förlust
d.mv('b2', tl, t + 0.2, (66, 62)); tw = win(d, b, 'b2', 'r2', t + 0.5, 0.6)                              # återtag inom sex
d.mv('b3', tl, tl + 1.0, (80, 62))
fp = [(0, 'Fem mot fem i ena rutan', 'Laget med bollen ska spela över till andra rutan.'),
      (tsw - 0.8, 'Spelvändning: 1 poäng', 'Spelet flyttar till andra rutan.'),
      (tl - 0.2, 'Bollförlust', 'Vinn tillbaka inom sex sekunder.'),
      (tw - 0.2, 'Återtag inom sex sekunder: 2 poäng', '')]
finish(d, 'of2', 'tappa-och-aterta-i-rutan', ['Tappa och återta', 'I rutan'], 'Två rutor 15 × 15 m bredvid varandra · Fem mot fem',
       fp, 'POSITIONSSPEL', [('box', 4, 24, 48, 76), ('box', 52, 24, 96, 76)],
       [lab(tsw, tsw + 1.6, (74, 18), '+1')] + countup(tl + 0.1, 3, (74, 84), (tw - tl) / 3) + [lab(tw, tw + 1.8, (60, 18), '+2')])

# ============ of3 Tappar du – jaga! ============
d = Drill()
ST = [(22, 26), (50, 22), (78, 26), (22, 72), (50, 76), (78, 72)]
team(d, 'b', B, ST); team(d, 'j', R, [(40, 50), (62, 50)])
BX = [(14, 18, 34, 40), (40, 16, 60, 34), (66, 18, 86, 40), (14, 58, 34, 82), (40, 66, 60, 82), (66, 58, 86, 82)]
balls = [d.newball(rec(d, f'b{k}', 0)) for k in range(6)]
for k in (1, 4, 5): wander(d, f'b{k}', 0, 17.9, BX[k], 1200 + k, 1.6); d.carry(balls[k], f'b{k}', 0, 17.9)
# jagare j0 tar bollen från b0
d.mv('b0', 0, 2.4, (26, 32)); d.carry(balls[0], 'b0', 0, 2.4); d.mv('j0', 0.3, 2.4, (30, 34))
t1 = d.pas(balls[0], 2.6, rec(d, 'j0', 2.9), 0.3); d.mv('j0', 2.9, 4.4, (20, 24)); d.carry(balls[0], 'j0', 2.9, 4.4)
wander(d, 'j0', 4.4, 17.9, BX[0], 1210, 1.6); d.carry(balls[0], 'j0', 4.4, 17.9)
stand(d, 'b0', 2.4, 3.0); d.mv('b0', 3.0, 5.6, (66, 56)); d.mv('b0', 5.6, 7.2, (42, 70))                # ny jagare direkt
# jagare j1 tar bollen från b2
wander(d, 'b2', 0, 3.0, BX[2], 1220, 1.6); d.mv('b2', 3.0, 4.0, (74, 32)); d.carry(balls[2], 'b2', 0, 4.0); d.mv('j1', 0.5, 4.0, (70, 36))
t2 = d.pas(balls[2], 4.2, rec(d, 'j1', 4.5), 0.3); d.mv('j1', 4.5, 6.0, (80, 26)); d.carry(balls[2], 'j1', 4.5, 6.0)
wander(d, 'j1', 6.0, 17.9, BX[2], 1230, 1.6); d.carry(balls[2], 'j1', 6.0, 17.9)
stand(d, 'b2', 4.0, 4.6); d.mv('b2', 4.6, 7.4, (40, 56)); d.mv('b2', 7.4, 9.2, (30, 66))
# nya jagaren b0 tar bollen från b3
wander(d, 'b3', 0, 7.2, BX[3], 1240, 1.6); d.mv('b3', 7.2, 8.0, (28, 74)); d.carry(balls[3], 'b3', 0, 8.0)
d.mv('b0', 7.2, 8.0, (34, 76)); t3 = d.pas(balls[3], 8.2, rec(d, 'b0', 8.5), 0.3)
d.mv('b0', 8.5, 10.0, (22, 70)); d.carry(balls[3], 'b0', 8.5, 10.0); wander(d, 'b0', 10, 17.9, BX[3], 1250, 1.6); d.carry(balls[3], 'b0', 10, 17.9)
stand(d, 'b3', 8.0, 8.6); d.mv('b3', 8.6, 11, (48, 50)); wander(d, 'b3', 11, 17.9, (40, 42, 60, 58), 1260, 1.6)
d.mv('b2', 9.2, 11.6, (64, 50)); wander(d, 'b2', 11.6, 17.9, (60, 44, 70, 56), 1270, 1.6)
fp = [(0, 'Alla dribblar – två jagare', 'Jagarna har ingen boll.'),
      (t1 - 0.4, 'Jagaren tar bollen', 'Den som blev av med bollen blir jagare direkt.'),
      (t2 + 0.6, 'Jaga en ny boll', 'Direkt – ingen vila.'),
      (t3 + 0.4, 'Vem har bollen kvar när tiden är slut?', '')]
finish(d, 'of3', 'tappar-du-jaga', ['Tappar du', 'jaga!'], 'Ruta 20 × 20 m · Alla har en boll utom två jagare',
       fp, 'LEK', [('box', 10, 12, 90, 88)], [lab(t1, t1 + 1.6, (26, 46), 'NY JAGARE'), lab(t2, t2 + 1.6, (76, 46), 'NY JAGARE'), lab(t3, t3 + 1.6, (26, 54), 'NY JAGARE')])
f = factor(fp); ids = {k: i for i, k in enumerate(d.order)}
C[-1]['players'][ids['b0']]['color'] = (lambda tt, a=(t1 - 0.2) * f, c=(t3 - 0.2) * f: B if tt < a else (R if tt < c else B))
swap_color(ids['j0'], (t1 - 0.2) * f, R, B); swap_color(ids['b2'], (t2 - 0.2) * f, B, R); swap_color(ids['j1'], (t2 - 0.2) * f, R, B); swap_color(ids['b3'], (t3 - 0.2) * f, B, R)
for i in range(len(d.order)): C[-1]['players'][i]['label'] = ''

# ============ of4 Från 3 mot 2 till 3 mot 3 ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
team(d, 'a', B, [(30, 70), (50, 74), (70, 70)]); team(d, 'f', R, [(40, 44), (60, 44)]); d.p('f3', '3', R, (50, 98))
b = d.newball(rec(d, 'a1', 0))
for k, ps in enumerate([(30, 44), (50, 50), (70, 42)]): d.mv(f'a{k}', 0.4, 3.0, ps)
d.carry(b, 'a1', 0.4, 3.0); d.mv('f0', 0.4, 3.2, (40, 30)); d.mv('f1', 0.4, 3.2, (60, 30))              # bromsar
d.mv('f3', 0.4, 4.6, (52, 34))                                                                          # den tredje springer tillbaka
t = d.pas(b, 3.1, rec(d, 'a2', 3.8)); d.mv('a2', t, t + 0.8, (70, 30)); d.carry(b, 'a2', t, t + 0.8); t += 0.8
d.mv('f1', t - 1.0, t + 0.2, rec(d, 'a2', t + 0.2)); tw = d.pas(b, t + 0.3, rec(d, 'f1', t + 0.5), 0.3)  # vinner bollen
t = drive(d, b, 'f1', tw, (62, 70), 22); tk = d.pas(b, t + 0.1, (50, 96), 1.0); hide(d, b, tk + 0.3)    # kontra mot konen
d.mv('a1', tw, tk, (52, 58)); d.mv('a2', tw, tk, (66, 52))
fp = [(0, 'Tre anfallare mot två försvarare', 'En tredje försvarare startar 15 m bakom.'),
      (0.6, 'Bromsa tills den tredje är tillbaka', 'Backa och stäng vägen mot mål.'),
      (4.4, 'Nu 3 mot 3', 'Försvararna kan gå på bollen.'),
      (tw - 0.2, 'Bollvinst – kontra mot konen', 'Konen står på mittlinjen.')]
finish(d, 'of4', 'fran-3-mot-2-till-3-mot-3', ['Från 3 mot 2', 'Till 3 mot 3'], 'Halv plan · Mål med målvakt',
       fp, 'ÖVERLÄGE', [('cone', 50, 97)])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ of5 Bromsa kontringen 2 mot 3 ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
team(d, 'a', B, [(30, 84), (50, 88), (70, 84)]); team(d, 'f', R, [(40, 50), (60, 50)])
b = d.newball(rec(d, 'a1', 0)); t0 = 0.4
for k, ps in enumerate([(28, 50), (50, 56), (72, 48)]): d.mv(f'a{k}', t0, t0 + 3.0, ps)
d.carry(b, 'a1', t0, t0 + 3.0); d.mv('f0', t0, t0 + 3.0, (42, 36)); d.mv('f1', t0, t0 + 3.0, (58, 36))
t = d.pas(b, t0 + 3.1, rec(d, 'a0', t0 + 3.8)); d.mv('f0', t - 0.6, t + 0.8, (34, 30)); d.mv('f1', t - 0.4, t + 0.8, (48, 28))
d.mv('a0', t, t + 1.0, (32, 36)); d.carry(b, 'a0', t, t + 1.0); t += 1.0
d.mv('a1', t - 0.6, t + 0.9, (50, 40)); t = d.pas(b, t + 0.1, rec(d, 'a1', t + 0.9)); d.mv('f1', t - 0.6, t + 0.4, (50, 33))
t6 = t0 + 6.0
tw = win(d, b, 'f1', 'a1', max(t + 0.6, t6 + 0.4), 0.6)                                                  # bollvinst
d.mv('f1', tw, tw + 1.2, (54, 52)); d.carry(b, 'f1', tw, tw + 1.2)
fp = [(0, 'Tre anfallare startar med boll', 'Två försvarare i en kanal mot mål.'),
      (1.0, 'Bromsa – håll ut i sex sekunder', 'Backa och tvinga dem att passa i sidled.'),
      (t6, 'Sex sekunder utan mål: 1 poäng', ''),
      (tw - 0.2, 'Bollvinst: 2 poäng', '')]
finish(d, 'of5', 'bromsa-kontringen-2-mot-3', ['Bromsa kontringen', '2 mot 3'], 'Kanal 40 × 25 m · Mål med målvakt',
       fp, 'DUELL', [('box', 18, 2, 82, 98)], countup(t0, 6, (88, 50)) + [lab(t6, t6 + 1.4, (88, 40), '+1'), lab(tw, tw + 1.8, (50, 62), '+2')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ of6 Kompakt efter bollförlust 6 mot 6 ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96))
BP = [(30, 72), (50, 76), (70, 72), (36, 48), (64, 46), (50, 34)]; RP = [(30, 24), (50, 20), (70, 24), (40, 40), (60, 36), (50, 60)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b1', 0))
t = chain(d, b, 0.4, ['b3', 'b5'], 0.3)
tl = win(d, b, 'r4', 'b5', t); d.mv('r4', tl, tl + 2.6, (58, 56)); d.carry(b, 'r4', tl, tl + 2.6)       # bollförlust
for k, ps in enumerate([(32, 78), (48, 80), (66, 76), (40, 66), (56, 68), (48, 62)]): d.mv(f'b{k}', tl + 0.1, tl + 2.4, ps)   # alla bakom bollen
tw = win(d, b, 'b4', 'r4', tl + 3.0, 0.6)
fp = [(0, 'Sex mot sex plus målvakter', 'Linje 15 m från varje mål.'),
      (tl - 0.2, 'Bollförlust – alla bakom bollen', 'Inom fem sekunder. Tränaren räknar.'),
      (tl + 2.4, 'Kompakt lag', 'Nu kan vi vinna tillbaka bollen.'),
      (tw - 0.2, 'Lyckat och bollvinst: 2 poäng', '')]
finish(d, 'of6', 'kompakt-efter-bollforlust-6-mot-6', ['Kompakt efter bollförlust', '6 mot 6'], 'Plan 50 × 40 m · Mål och målvakter · Linje 15 m från varje mål',
       fp, 'OMSTÄLLNING', [('line', [(4, 22), (96, 22)]), ('line', [(4, 78), (96, 78)])],
       countup(tl + 0.1, 5, (88, 54), 0.5) + [lab(tw, tw + 1.8, (58, 48), '+2')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ fu1 Styr åt sidan 1 mot 1 ============
d = Drill()
d.p('f', 'F', R, (50, 84)); d.p('a', 'A', B, (50, 50)); d.p('f2', 'F', R, (40, 96)); d.p('a2', 'A', B, (60, 96))
b = d.newball(rec(d, 'f', 0))
t = d.pas(b, 0.4, rec(d, 'a', 1.2)); d.mv('f', 0.5, 1.8, (50, 40))                                      # spelar till anfallaren och kliver på
d.mv('a', 1.2, 2.4, (54, 34)); d.carry(b, 'a', 1.2, 2.4); d.mv('f', 1.8, 2.6, (48, 28))                 # styrs åt sidan
d.mv('a', 2.4, 3.6, (74, 18)); d.carry(b, 'a', 2.4, 3.6); d.mv('f', 2.6, 3.6, (62, 22))
d.mv('a', 3.6, 4.2, (74, 10)); d.carry(b, 'a', 3.6, 4.2); tp = 4.0                                     # sidoport: 1 poäng
hide(d, b, 4.4); d.mv('a', 4.4, 6.4, (60, 96)); d.mv('f', 4.4, 6.4, (40, 96)); d.mv('f2', 4.4, 5.6, (50, 84)); d.mv('a2', 4.4, 5.8, (50, 50))
b2 = d.newball((200, 200)); show(d, b2, 5.7, rec(d, 'f2', 5.7))
t = d.pas(b2, 6.0, rec(d, 'a2', 6.8)); d.mv('f2', 6.1, 7.4, (50, 40))
d.mv('a2', 6.8, 7.6, (46, 40)); d.carry(b2, 'a2', 6.8, 7.6); tw = win(d, b2, 'f2', 'a2', 7.6, 0.4)       # bollvinst
d.mv('f2', tw, tw + 1.2, (40, 60)); d.carry(b2, 'f2', tw, tw + 1.2)
fp = [(0, 'Försvararen spelar till anfallaren', 'Och kliver på direkt.'),
      (1.6, 'Styr åt sidan', 'Bort från mittporten som ger 2 poäng.'),
      (tp - 0.4, 'Sidoport: 1 poäng', 'Bättre än mittporten för försvararen.'),
      (tw - 0.2, 'Bollvinst: 1 poäng till försvararen', 'Nästa par.')]
finish(d, 'fu1', 'styr-at-sidan-1-mot-1', ['Styr åt sidan', '1 mot 1'], 'Kanal 20 × 12 m · Port i mitten och portar på båda sidor',
       fp, 'DUELL', [('box', 22, 8, 78, 92)] + [('cone', x, 8) for x in (24, 32, 46, 54, 68, 76)], [lab(tp, tp + 1.6, (72, 20), '+1'), lab(tw, tw + 1.6, (46, 50), '+1')])

# ============ fu3 Stoppa fem passningar ============
d = Drill()
BP = [(30, 34), (66, 32), (36, 64), (64, 66)]; RP = [(44, 42), (56, 46), (42, 56), (58, 58)]; NP = [(50, 10), (50, 90), (8, 50), (92, 50)]
team(d, 'b', B, BP); team(d, 'r', R, RP); team(d, 'n', YEL, NP, ['A'] * 4)
for k in range(4): wander(d, f'r{k}', 0, 4.6, boxes([RP[k]], 3)[0], 1300 + k, 1.6)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['n2', 'b2', 'b3', 'n3', 'b1'], 0.25); cnt = arrivals(d, b)[:5]
t = d.pas(b, t + 0.2, rec(d, 'b0', t + 0.8)); c2 = [t]; t = d.pas(b, t + 0.2, rec(d, 'n0', t + 0.8)); c2.append(t)
tw = win(d, b, 'r0', 'n0', t + 0.2, 0.9) if False else None
d.mv('r1', t - 0.2, t + 0.9, (48, 22)); t = d.pas(b, t + 0.2, (48, 22), 0.6); tw = t                       # bryter innan fem
d.carry(b, 'r1', tw, tw + 0.2); t = d.pas(b, tw + 0.3, rec(d, 'r2', tw + 1.0)); t = chain(d, b, t, ['r3', 'n1'], 0.3)
fp = [(0, 'Fyra mot fyra plus fyra anspelare', 'Anspelarna spelar med laget som har bollen.'),
      (cnt[-1] - 0.3, 'Fem passningar: 1 poäng', ''),
      (tw - 0.3, 'Bryt innan fem: 2 poäng', 'Försvarslaget pressar tillsammans.'),
      (tw + 0.6, 'Nu håller rött bollen', 'Samma regler.')]
finish(d, 'fu3', 'stoppa-fem-passningar', ['Stoppa fem', 'passningar'], 'Ruta 30 × 25 m · Fyra mot fyra plus fyra anspelare',
       fp, 'POSITIONSSPEL', [('box', 12, 14, 88, 86)], counter(cnt, pos=(78, 22)) + counter(c2, pos=(78, 22), last=None) + [lab(tw, tw + 1.8, (48, 30), '+2')])

# ============ fu4 Pressa målvaktens utspel 3 mot 3 ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96))
RP = [(30, 20), (70, 20), (50, 34)]; BP = [(36, 56), (64, 56), (50, 70)]; team(d, 'r', R, RP); team(d, 'b', B, BP)
b = d.newball(rec(d, 'mvr', 0))
for k, ps in enumerate([(34, 26), (64, 28), (50, 40)]): d.mv(f'b{k}', 0.4, 2.0, ps)                     # press högt
t = d.pas(b, 1.0, rec(d, 'r0', 1.8)); d.mv('b0', 1.8, 2.6, rec(d, 'r0', 2.6)); tw = d.pas(b, 2.7, rec(d, 'b0', 2.9), 0.3)   # vinner på deras planhalva
t = d.pas(b, tw + 0.2, rec(d, 'b2', tw + 0.8)); tg = shoot(d, b, t + 0.05, (46, 1))
hide(d, b, tg + 0.4)
for k in range(3): d.mv(f'b{k}', tg + 0.2, tg + 2.2, BP[k]); d.mv(f'r{k}', tg + 0.2, tg + 2.2, RP[k])
b2 = d.newball((200, 200)); show(d, b2, tg + 2.2, rec(d, 'mvb', tg + 2.2))
for k, ps in enumerate([(36, 70), (66, 72), (52, 60)]): d.mv(f'r{k}', tg + 2.4, tg + 4.0, ps)
t = d.pas(b2, tg + 2.6, rec(d, 'b1', tg + 3.4)); t = d.pas(b2, t + 0.2, rec(d, 'b2', t + 0.9)); t = chain(d, b2, t, ['b0'], 0.3)
fp = [(0, 'Varje anfall startar med målvaktens utspel', 'Tre mot tre plus målvakter.'),
      (0.4, 'Pressa utspelet högt', 'Stäng de korta alternativen.'),
      (tw - 0.2, 'Bollvinst på deras planhalva', 'Mål nu räknas dubbelt.'),
      (tg + 2.2, 'Nytt utspel – andra hållet', 'Rött pressar nu.')]
finish(d, 'fu4', 'pressa-malvaktens-utspel-3-mot-3', ['Pressa målvaktens utspel', '3 mot 3'], 'Plan 30 × 20 m · Mål och målvakter',
       fp, 'PRESS', [('line', [(4, 50), (96, 50)])], [lab(tg, tg + 1.8, (46, 14), 'x2')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ fa1 Målvakt och två mot tre ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
AP = [(32, 30), (50, 34), (68, 30)]; DP = [(42, 18), (58, 18)]; team(d, 'a', B, AP); team(d, 'f', R, DP)
b = d.newball(rec(d, 'a1', 0)); t0 = 0.4
t = chain(d, b, t0, ['a0', 'a1', 'a2'], 0.3); d.mv('f1', t - 1.0, t, (62, 16)); tsv = shoot(d, b, t + 0.1, (54, 4))   # räddning
d.mv('mv', tsv - 0.4, tsv, (54, 5)); d.carry(b, 'mv', tsv, tsv + 0.6)
hide(d, b, tsv + 0.8)
for k in range(3): d.mv(f'a{k}', tsv + 0.4, tsv + 2.0, AP[k])
d.mv('mv', tsv + 0.6, tsv + 1.4, (50, 4))
b2 = d.newball((200, 200)); show(d, b2, tsv + 2.0, rec(d, 'a1', tsv + 2.0)); t1 = tsv + 2.0
t = d.pas(b2, t1 + 0.2, rec(d, 'a2', t1 + 0.8)); d.mv('a0', t1, t + 0.8, (40, 14)); t = d.pas(b2, t + 0.2, rec(d, 'a0', t + 1.0))
tg = shoot(d, b2, t + 0.05, (44, 1)); d.mv('f0', t1, t, (48, 16))
fp = [(0, 'Tre anfallare mot två försvarare och målvakt', 'Anfallarna har tio sekunder på sig.'),
      (tsv - 0.3, 'Räddning: 1 poäng till försvaret', ''),
      (t1, 'Nytt anfall', 'Tio sekunder igen.'),
      (tg - 0.3, 'Mål', 'Bollvinst eller räddning ger försvaret 1 poäng.')]
finish(d, 'fa1', 'malvakt-och-tva-mot-tre', ['Målvakt och', 'två mot tre'], 'Straffområdet · Mål med målvakt',
       fp, 'ÖVERLÄGE', [], countdown(t0, 10, (86, 40), (tsv - t0) / 6)[:6] + [lab(tsv, tsv + 1.6, (62, 14), '+1 FÖRSVAR')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

if __name__ == '__main__': render(C, sys.argv)
