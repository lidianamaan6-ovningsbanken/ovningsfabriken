# Externa övningar, omgång 36 (fjorton st). Regel: först d.mv, sedan d.carry; först mottagarens rörelse, sedan passningen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e9', __file__.replace('render_extern36.py', 'render_extern9.py'))
e9 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e9); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e9.finish, e9.rec, e9.chain, e9.wander, e9.counter, e9.arrivals
lab, hide, show, team, boxes, drive, shoot = e9.lab, e9.hide, e9.show, e9.team, e9.boxes, e9.drive, e9.shoot
factor, swap_color, stand, countdown, countup, win = e9.factor, e9.swap_color, e9.stand, e9.countdown, e9.countup, e9.win
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'

# ============ wj05 Spelarna först – lekmatch utan coachning ============
import math

# ============ cl01 Hem på signal – organiserad reträtt ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96)); d.p('t', 'T', T_COL, (97, 50))
BP = [(22, 66), (42, 72), (62, 70), (80, 60), (40, 46), (60, 40)]; RP = [(28, 52), (46, 56), (66, 52), (76, 40), (36, 30), (54, 24)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'r1', 0))
t = chain(d, b, 0.4, ['r2', 'r3'], 0.3); tw = win(d, b, 'b5', 'r3', t + 0.4, 0.7)                      # blått vinner
d.mv('b3', tw - 0.4, tw + 0.8, (84, 34)); t = d.pas(b, tw + 0.2, rec(d, 'b3', tw + 0.9)); th = t
HOME = [(30, 24), (44, 20), (58, 22), (72, 28), (42, 12), (56, 10)]                                        # röda faller bakom bollen
d.mv('r3', th - 0.2, th + 0.8, (80, 30))
for k in (0, 1, 2, 4, 5): d.mv(f'r{k}', th - 0.2, th + 2.4, HOME[k])
t = drive(d, b, 'b3', th, (80, 26), 12); d.mv('b5', th, th + 1.6, (58, 22)); t = d.pas(b, t + 0.6, rec(d, 'b5', t + 1.3))
fp = [(0, 'Sex mot sex', ''),
      (tw - 0.2, 'Bollvinst', ''),
      (th - 0.3, '”HEM!” – bakom bollen på fem sekunder', 'Spring mot eget mål, inte mot bollen.'),
      (th + 2.6, 'Närmsta pressar, övriga faller', 'Kompakt bakom bollen.')]
finish(d, 'cl01', 'hem-pa-signal-organiserad-retratt', ['Hem på signal', 'Organiserad reträtt'], 'Plan 40 × 30 m · Två mål',
       fp, 'SMÅLAGSSPEL', [('box', 6, 2, 94, 98)], [lab(th - 0.3, th + 1.2, (88, 58), 'HEM!')] + countdown(th, 5, (14, 50), 0.5))
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ cl02 Rondo med pivot i mitten ============
d = Drill()
OU = [(50, 22), (78, 50), (50, 78), (22, 50)]
team(d, 'b', B, OU); d.p('pv', 'P', B, (50, 50)); team(d, 'f', R, [(38, 40), (62, 60)], ['', ''])
b = d.newball(rec(d, 'b0', 0))
d.mv('f0', 0.3, 2.4, (40, 52)); d.mv('f1', 0.3, 2.4, (62, 42))
t = chain(d, b, 0.4, ['b1', 'b2', 'b3'], 0.3); cnt = arrivals(d, b)[:3]
d.mv('pv', t - 0.8, t + 0.2, (54, 56)); d.mv('f0', t - 0.6, t + 0.4, (36, 40))
t = d.pas(b, t + 0.3, rec(d, 'pv', t + 0.9)); tp = t; t = d.pas(b, t + 0.3, rec(d, 'b1', t + 0.9))   # genom pivoten
d.mv('f1', tp, t + 0.6, (66, 52)); t = chain(d, b, t, ['b0', 'b3'], 0.3)
tw = win(d, b, 'f0', 'b3', t + 0.4, 0.6); d.mv('f0', tw + 0.3, tw + 1.5, OU[3]); d.mv('b3', tw + 0.3, tw + 1.5, (40, 42))
fp = [(0, 'Fyra ute, pivot i mitten', 'Mot två försvarare.'),
      (1.2, 'Runt: 1 poäng per fem i rad', 'Snabbt runt när mitten är stängd.'),
      (tp - 0.6, 'Genom pivoten: 2 poäng', 'Pivoten skannar före mottagningen.'),
      (tw - 0.2, 'Den som tappar byter', '')]
finish(d, 'cl02', 'rondo-med-pivot-i-mitten', ['Rondo med pivot', 'I mitten'], 'Ruta 15 × 15 m · 4 + 1 mot 2',
       fp, 'RONDO', [('box', 16, 16, 84, 84)], [lab(t - 1.2, t, (50, 90), '+2')] if False else [lab(tp + 0.2, tp + 1.8, (74, 66), '+2')])

# ============ cl03 Kantpressen 3 mot 2 ============
d = Drill()
team(d, 'a', B, [(30, 80), (50, 84)]); team(d, 'p', R, [(26, 46), (50, 42), (70, 50)])
b = d.newball(rec(d, 'a0', 0))
d.mv('p0', 0.3, 1.6, (22, 66)); d.mv('p1', 0.3, 1.6, (36, 62)); d.mv('p2', 0.3, 1.6, (54, 64))             # pressar mot sidlinjen
t = drive(d, b, 'a0', 0.4, (18, 70), 10); d.mv('a1', 0.6, 2.0, (40, 76))
tw = win(d, b, 'p0', 'a0', t + 0.6, 0.6)
d.mv('p1', tw, tw + 1.2, (40, 84)); t = d.pas(b, tw + 0.2, rec(d, 'p1', tw + 1.0)); t = drive(d, b, 'p1', t, (44, 90), 12)
tg = d.pas(b, t + 0.1, (40, 96), 0.4); hide(d, b, tg + 0.3)
fp = [(0, 'Tre pressare mot två', 'Bollhållarna ska genom porten.'),
      (1.0, 'Använd sidlinjen som extra försvarare', 'Första pressaren stänger insidan.'),
      (tw - 0.2, 'Bollvinst', ''),
      (tw + 0.4, 'Kontra direkt – mål i minimålet', 'Byt roller efter fem anfall.')]
finish(d, 'cl03', 'kantpressen-3-mot-2', ['Kantpressen', '3 mot 2'], 'Kantkorridor 15 × 25 m · Port och minimål',
       fp, 'ÖVERLÄGSENHET', [('box', 10, 10, 90, 96), ('cone', 44, 12), ('cone', 56, 12), ('smallgoal', 40, 96), ('smallgoal', 74, 96)], [lab(tg, tg + 1.6, (52, 88), '+1')])

# ============ cl04 Z-passningen – kort, lång, kort ============
d = Drill()
Z = [(24, 80), (76, 80), (24, 24), (76, 24)]; BACK = [(18, 86), (82, 86), (18, 18), (82, 18)]
for k, ps in enumerate(Z): d.p(f'a{k}', '', B, ps)
d.p('a4', '', B, BACK[0])
at_cone = {0: ['a0', 'a4'], 1: ['a1'], 2: ['a2'], 3: ['a3']}
b = d.newball(rec(d, 'a0', 0)); t = 0.4; cnt = []; c = 0
for step in range(7):
    nc = (c + 1) % 4; src = at_cone[c].pop(0); rcv = at_cone[nc][0]
    t2 = d.pas(b, t + 0.3, rec(d, rcv, t + 0.3 + (1.4 if c == 1 else 0.9))); cnt.append(t2)
    d.mv(src, t + 0.4, t + 0.4 + (2.4 if c == 1 else 1.6), BACK[nc]); at_cone[nc].append(src)
    if at_cone[c]: d.mv(at_cone[c][0], t + 0.6, t + 1.4, Z[c])                                                # nästa i kön kliver fram
    t = t2; c = nc
fp = [(0, 'Spelare vid varje kon', ''),
      (0.8, 'Kort – lång diagonal – kort', 'Alla följer sin passning.'),
      (2.4, 'Öppen kropp för den långa', 'Vristen och följ igenom.'),
      (6.0, 'Mottagning i rörelse', 'Variant: två bollar samtidigt.')]
finish(d, 'cl04', 'z-passningen-kort-lang-kort', ['Z-passningen', 'Kort, lång, kort'], 'Fyra koner i Z · 15 × 25 m',
       fp, 'PASSNING', [('cone', x, y) for x, y in Z] + [('line', [Z[0], Z[1], Z[2], Z[3]])], [lab(cnt[1] - 1.0, cnt[1] + 0.4, (50, 50), 'LÅNG')])

# ============ cl05 Yo-yo med boll ============
d = Drill()
XS = [22, 38, 54, 70]
for k, x in enumerate(XS): d.p(f'p{k}', '', B if k % 2 == 0 else R, (x, 84))
balls = [d.newball(rec(d, f'p{k}', 0)) for k in range(4)]
for k, x in enumerate(XS):
    tt = drive(d, balls[k], f'p{k}', 0.4 + 0.05 * k, (x, 18), 32 - 2 * k)
    d.mv(f'p{k}', tt, tt + 0.4, (x + 2, 16)); d.carry(balls[k], f'p{k}', tt, tt + 0.4)                    # vändning med sulan
    tt2 = drive(d, balls[k], f'p{k}', tt + 0.4, (x, 84), 17)
    stand(d, f'p{k}', tt2, 9.0); d.carry(balls[k], f'p{k}', tt2, 9.0)
fp = [(0, 'Alla startar på linjen', 'Snabb dribbling 20 m.'),
      (2.6, 'Vändning – kontrollerad jogg tillbaka', 'Med sula eller insida.'),
      (7.0, '10 sekunders vila', 'Andas på vilan.'),
      (9.0, '6–10 repetitioner, två serier', 'Kontrollera bollen även när du är trött.')]
finish(d, 'cl05', 'yo-yo-med-boll', ['Yo-yo', 'med boll'], 'Två linjer 20 m isär · En boll per spelare',
       fp, 'LEK', [('line', [(12, 88), (80, 88)]), ('line', [(12, 14), (80, 14)])], [lab(7.2, 9.0, (88, 50), 'VILA')])

# ============ ps01 Riktningsrondo med målzon ============
d = Drill()
team(d, 'b', B, [(30, 36), (70, 36), (30, 64), (70, 64)]); team(d, 'f', R, [(44, 48), (56, 52)], ['', ''])
d.p('zt', 'M', B, (50, 8)); d.p('zb', 'M', B, (50, 92))
b = d.newball(rec(d, 'b2', 0))
d.mv('f0', 0.3, 2.0, (40, 42)); d.mv('f1', 0.3, 2.0, (60, 46))
t = chain(d, b, 0.4, ['b3', 'b1'], 0.3); d.mv('b0', t - 0.8, t + 0.2, (34, 30))
t = d.pas(b, t + 0.3, rec(d, 'b0', t + 1.0)); t = d.pas(b, t + 0.3, rec(d, 'zt', t + 1.0)); tz = t             # in i målzonen
d.mv('b0', tz, tz + 1.4, (40, 8)); d.mv('zt', tz + 0.2, tz + 1.4, (40, 30)); d.carry(b, 'zt', tz, tz + 1.4)     # passaren tar platsen
d.mv('f0', tz, tz + 1.6, (44, 52)); d.mv('f1', tz, tz + 1.6, (56, 56))
t = chain(d, b, tz + 1.4, ['b2', 'b3'], 0.3); t = d.pas(b, t + 0.3, rec(d, 'zb', t + 1.0))
fp = [(0, 'Fyra mot två', 'En spelare väntar i varje målzon.'),
      (1.2, 'Håll bollen – spela framåt när det går', 'Rättvänd mottagning.'),
      (tz - 0.4, 'In i målzonen: poäng', 'Passaren tar platsen i zonen.'),
      (tz + 1.4, 'Anfall åt andra hållet', 'Fyll platsen direkt.')]
finish(d, 'ps01', 'riktningsrondo-med-malzon', ['Riktningsrondo', 'Med målzon'], 'Ruta 15 × 20 m · Målzon i varje ände',
       fp, 'RONDO', [('box', 18, 16, 82, 84), ('zone', 30, 2, 70, 14, (240, 210, 90), ''), ('zone', 30, 86, 70, 98, (240, 210, 90), '')],
       [lab(tz, tz + 1.6, (64, 8), '+1'), lab(t, t + 1.6, (64, 92), '+1')])

# ============ ps02 Färgkon-reaktion till 1 mot 1 ============
d = Drill(); d.p('mv', 'MV', R, (50, 4)); d.p('t', 'T', T_COL, (90, 62))
d.p('a', '', B, (44, 86)); d.p('f', '', R, (56, 86))
CK = [(30, 72), (70, 72), (50, 76)]
d.mv('a', 1.2, 2.0, (32, 74)); d.mv('f', 1.4, 2.4, (34, 70))                                                 # rundar blå kon
d.mv('a', 2.0, 2.8, (40, 62)); d.mv('f', 2.4, 3.2, (46, 56))
b = d.newball((200, 200)); show(d, b, 2.4, rec(d, 't', 2.4)); t = d.pas(b, 2.6, rec(d, 'a', 3.4), 0.8)
d.mv('f', 3.2, t + 0.6, (44, 44)); t = drive(d, b, 'a', t, (38, 46), 14)
d.mv('f', t, t + 0.8, (36, 34)); t = drive(d, b, 'a', t, (56, 30), 14); d.mv('f', t - 0.4, t + 0.2, (52, 30))
tg = shoot(d, b, t + 0.05, (56, 1))
fp = [(0, 'Anfallare och försvarare startar samtidigt', ''),
      (1.0, 'Tränaren ropar en färg', 'Båda rundar den konen.'),
      (2.4, 'Bollen in – först dit blir anfallare', 'Första touch framåt.'),
      (tg - 0.6, 'Ett mot ett mot mål', 'Försvararen: bromsa och styr.')]
finish(d, 'ps02', 'fargkon-reaktion-till-1-mot-1', ['Färgkon-reaktion', 'Till 1 mot 1'], 'Tre färgkoner · Mål med målvakt',
       fp, 'DUELL', [('redcone', 70, 72), ('yellowcone', 50, 78), ('cone', 30, 72), ('box', 14, 4, 86, 92)], [lab(1.0, 2.4, (78, 52), '”ORANGE!”')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ ps03 Alla bär alla – bollstafett ============
d = Drill()
for tm, x, col in (('b', 34, B), ('r', 66, R)):
    for k in range(3): d.p(f'{tm}{k}', '', col, (x - 6 + 6 * k, 88))
ex = []
for tm, x in (('b', 34), ('r', 66)):
    bl = [d.newball((x - 4 + 4 * j, 18 + (j % 2) * 3)) for j in range(3)]; t = 0.4 + (0.3 if tm == 'r' else 0)
    for k in range(3):
        pid = f'{tm}{k}'; sx, sy = d.pos(pid)
        d.mv(pid, t, t + 0.4, (x, 84)); t += 0.4
        tt = d.path(pid, t, [(x - 4 + 4 * k, 22 + (k % 2) * 3)], 1.5)                                         # spring till bollarna
        tt2 = drive(d, bl[k], pid, tt + 0.1, (x - 4 + 4 * k, 78), 30)
        d.mv(pid, tt2, tt2 + 0.6, (x - 8 + 8 * k, 92)); d.carry(bl[k], pid, tt2, tt2 + 0.6); t = tt2 + 0.4
    ex.append(lab(t, t + 1.6, (x, 70), 'ALLA HEMMA!' if tm == 'b' else ''))
fp = [(0, 'Lagets bollar ligger i andra änden', 'En spelare åt gången.'),
      (1.0, 'Dribbla hem med en boll', 'Bollen nära foten.'),
      (5.0, 'Nästa springer när du är hemma', 'Heja och pusha laget.'),
      (9.0, 'Först med alla bollar hemma vinner', 'Variant: vänster fot eller passa sista biten.')]
finish(d, 'ps03', 'alla-bar-alla-bollstafett', ['Alla bär alla', 'Bollstafett'], 'Två banor 20 m · Rutor med bollar',
       fp, 'LEK', [('box', 24, 12, 44, 30), ('box', 56, 12, 76, 30), ('line', [(20, 84), (80, 84)])], [e for e in ex if e['text']])
C[-1]['_stuck'] = False

# ============ ps04 Doppboll med frisläpp ============
d = Drill()
KP = [(24, 30), (70, 26), (30, 70), (74, 72), (50, 52), (46, 22)]
team(d, 'k', B, KP, [''] * 6); team(d, 'j', R, [(14, 50), (86, 50)], ['J', 'J'])
balls = [d.newball(rec(d, f'k{k}', 0)) for k in range(6)]
for k in (0, 1, 3, 5): wander(d, f'k{k}', 0, 17.9, (12, 14, 88, 86), 14000 + k, 1.4); d.carry(balls[k], f'k{k}', 0, 17.9)
jb = d.newball(rec(d, 'j0', 0))
d.mv('k2', 0, 2.0, (36, 62)); d.carry(balls[2], 'k2', 0, 2.0); d.mv('j0', 0, 1.6, (24, 58)); d.carry(jb, 'j0', 0, 1.6)
th = d.pas(jb, 1.8, rec(d, 'k2', 2.3), 0.5); d.mv('j0', th, th + 1.2, (32, 56)); t = d.pas(jb, th + 0.2, rec(d, 'j0', th + 1.2), 0.9)  # träff under knät
stand(d, 'k2', 2.0, 4.8); d.carry(balls[2], 'k2', 2.0, 4.8)
d.carry(jb, 'j0', t, t + 0.6); wander(d, 'j0', t + 0.6, 17.9, (12, 14, 88, 86), 14010, 1.4); d.carry(jb, 'j0', t + 0.6, 17.9)
wander(d, 'j1', 0, 17.9, (12, 14, 88, 86), 14011, 1.4)
d.mv('k4', 0, 3.6, (44, 52)); d.carry(balls[4], 'k4', 0, 3.6)
tb = d.pas(balls[4], 3.8, (28, 74), 0.8); d.mv('k4', 3.8, tb + 0.4, (28, 76)); d.carry(balls[4], 'k4', tb + 0.4, tb + 0.6)   # mellan benen
d.mv('k4', tb + 0.6, tb + 3, (60, 30)); d.carry(balls[4], 'k4', tb + 0.6, tb + 3); tf = tb
d.mv('k2', tf + 0.2, tf + 3, (24, 82)); d.carry(balls[2], 'k2', tf + 0.2, tf + 3)
wander(d, 'k4', tb + 3, 17.9, (12, 14, 88, 86), 14020, 1.4); d.carry(balls[4], 'k4', tb + 3, 17.9)
wander(d, 'k2', tf + 3, 17.9, (12, 14, 88, 86), 14021, 1.4); d.carry(balls[2], 'k2', tf + 3, 17.9)
fp = [(0, 'Alla dribblar, två jagare', ''),
      (1.6, 'Träff under knät – frys med benen isär', ''),
      (3.6, 'Befria: passa mellan benen', 'Hjälp varandra.'),
      (tf + 0.4, 'Fri igen!', 'Byt jagare var 90:e sekund.')]
finish(d, 'ps04', 'doppboll-med-frislapp', ['Doppboll', 'Med frisläpp'], 'Yta 20 × 20 m · Två jagare',
       fp, 'LEK', [('box', 8, 10, 92, 90)], [lab(2.3, 3.8, (36, 54), 'FRYS'), lab(tf + 0.2, tf + 1.6, (36, 58), 'FRI!')])

# ============ ps05 Väggspelsmatchen ============
d = Drill()
BP = [(28, 70), (66, 68), (44, 52), (60, 36)]; RP = [(34, 40), (64, 46), (50, 62), (44, 26)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b0', 0))
t = d.pas(b, 0.4, rec(d, 'b2', 1.2)); d.mv('r2', 0.4, 1.6, (48, 58))
t = d.pas(b, t + 0.2, rec(d, 'b3', t + 0.8)); d.mv('b2', t - 0.6, t + 0.6, (52, 30)); tv = d.pas(b, t + 0.15, rec(d, 'b2', t + 0.75))   # väggspel
d.mv('r3', tv - 0.8, tv + 0.4, (46, 22)); t = drive(d, b, 'b2', tv, (50, 18), 18); tg = d.pas(b, t + 0.05, (50, 5), 0.4); hide(d, b, tg + 0.3)
fp = [(0, 'Fyra mot fyra med småmål', ''),
      (1.8, 'Spela och gå', 'Retur i rätt fart.'),
      (tv - 0.2, 'Lyckat väggspel: 1 poäng', ''),
      (tg - 0.3, 'Mål direkt efter väggspel: 3 poäng', 'Vanligt mål ger 1 poäng.')]
finish(d, 'ps05', 'vaggspelsmatchen', ['Väggspels-', 'matchen'], 'Yta 25 × 30 m · Småmål',
       fp, 'SMÅLAGSSPEL', [('box', 12, 4, 88, 96), ('smallgoal', 50, 4), ('smallgoal', 50, 96)], [lab(tv, tv + 1.4, (68, 30), '+1'), lab(tg, tg + 1.8, (50, 14), '+3')])

# ============ ps06 Nummermatchen ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96)); d.p('t', 'T', T_COL, (96, 50))
for k in range(4): d.p(f'b{k}', str(k + 1), B, (4, 30 + 13 * k)); d.p(f'r{k}', str(k + 1), R, (96 - 0, 20 + 8 * k) if False else (88 + 0 * k, 70 + 6 * k))
b = d.newball((200, 200)); show(d, b, 1.0, rec(d, 't', 1.0))
d.mv('b1', 1.0, 2.2, (34, 46)); d.mv('r1', 1.0, 2.2, (60, 56))
t = d.pas(b, 1.2, (50, 50), 1.0); d.mv('b1', 2.2, t + 0.2, (48, 50)); t = drive(d, b, 'b1', t + 0.2, (44, 66), 14)
d.mv('r1', 2.2, t, (48, 70)); te = t
d.mv('b3', te - 0.6, te + 0.8, (30, 76)); d.mv('r3', te - 0.4, te + 1.6, (60, 84))                          # extra nummer – 2 mot 1
t = d.pas(b, te + 0.1, rec(d, 'b3', te + 0.8)); t = drive(d, b, 'b3', t, (40, 86), 14); tg = shoot(d, b, t + 0.05, (46, 99))
fp = [(0, 'Två lag med numrerade spelare', ''),
      (1.0, 'Tränaren ropar ”2!” och spelar in', 'Snabb start – mot mål direkt.'),
      (te - 0.6, 'Extra nummer: ”4!” – två mot ett', 'Prata med kompisen.'),
      (tg - 0.3, 'Spela tills mål eller boll ut', '')]
finish(d, 'ps06', 'nummermatchen', ['Nummer-', 'matchen'], 'Plan 20 × 30 m · Två mål',
       fp, 'DUELL', [('box', 10, 2, 90, 98)], [lab(1.0, 2.4, (84, 40), '”2!”'), lab(te - 0.6, te + 0.8, (84, 40), '”4!”')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ ps07 Tre rondos med vandrande försvarare ============
d = Drill()
BX = [(6, 30, 34, 70), (36, 30, 64, 70), (66, 30, 94, 70)]
for i, (x1, y1, x2, y2) in enumerate(BX):
    cx = (x1 + x2) / 2
    for k, ps in enumerate([(cx, y1 + 3), (x2 - 3, 50), (cx, y2 - 3), (x1 + 3, 50)]): d.p(f'b{i}{k}', '', B, ps)
    d.p(f'f{i}', '', R, (cx, 50))
ex = []
for i, (x1, y1, x2, y2) in enumerate(BX):
    b = d.newball(rec(d, f'b{i}0', 0)); t = 0.3 + 0.2 * i; seq = [1, 2, 3, 0, 2, 1, 3, 0, 1, 2] if i == 0 else [1, 2, 3, 0, 1, 3, 2, 0]
    cx = (x1 + x2) / 2
    for nk in seq:
        tx, ty = at(d.pl[f'b{i}{nk}']['tr'], t); d.mv(f'f{i}', t, t + 0.6, ((tx + cx) / 2, (ty + 50) / 2))
        t = d.pas(b, t + 0.15, rec(d, f'b{i}{nk}', t + 0.75))
    if i == 0: tdone = t
d.mv('f0', tdone + 0.2, tdone + 2.4, (44, 50)); ex.append(lab(tdone, tdone + 1.8, (20, 22), '10! VIDARE'))
d.mv('f1', tdone + 0.4, tdone + 2.6, (76, 46))
fp = [(0, 'Tre rutor, en försvarare i varje', 'Fyra ute.'),
      (1.2, 'Tio passningar – försvararen springer vidare', 'Kroppen öppen mot nästa passning.'),
      (tdone - 0.2, 'Försvararen till nästa ruta', 'Vilka tar sig hela vägen runt?'),
      (tdone + 2.6, 'Vinner försvararen bollen – byt', 'Spela bort från försvararen.')]
finish(d, 'ps07', 'tre-rondos-med-vandrande-forsvarare', ['Tre rondos', 'Med vandrande försvarare'], 'Tre rutor 10 × 10 m i rad',
       fp, 'RONDO', [('box', *bx) for bx in BX], ex)

# ============ ps08 Fyra kvadrater – 1 mot 1 med jokrar ============
d = Drill()
SQ = [(8, 10, 48, 48), (52, 10, 92, 48), (8, 52, 48, 90), (52, 52, 92, 90)]
for i, (x1, y1, x2, y2) in enumerate(SQ):
    cx, cy = (x1 + x2) / 2, (y1 + y2) / 2; d.p(f'a{i}', '', B, (cx, cy + 8)); d.p(f'f{i}', '', R, (cx, cy - 8))
for k, ps in enumerate([(50, 6), (50, 94), (4, 50), (96, 50)]): d.p(f'j{k}', 'J', YEL, ps)
for i, (x1, y1, x2, y2) in enumerate(SQ):
    b = d.newball(rec(d, f'a{i}', 0)); t = 0.4 + 0.3 * i
    if i == 0:   # vägg på jokern, sedan över linjen
        d.mv('f0', 0.4, 1.4, (34, 30)); t = d.pas(b, 0.6, rec(d, 'j2', 1.2)); d.mv('a0', 0.6, 1.6, (18, 26)); t = d.pas(b, t + 0.2, rec(d, 'a0', t + 0.8))
        d.mv('f0', t - 0.4, t + 0.4, (22, 20)); t = drive(d, b, 'a0', t, (26, 10), 14); tg = t; d.carry(b, 'a0', t, t + 0.4)
    else:
        wander(d, f'a{i}', 0, 17.9, (x1 + 4, y1 + 4, x2 - 4, y2 - 4), 14100 + i, 1.2); d.carry(b, f'a{i}', 0, 17.9)
        d.mv(f'f{i}', 0, 0.3, d.pos(f'f{i}'))
for i in (1, 2, 3):
    tr = d.pl[f'a{i}']['tr']; d.pl[f'f{i}']['tr'] = [(t, (x - 4, y - 8)) for t, (x, y) in tr]
fp = [(0, 'Ett mot ett i varje kvadrat', 'Jokrar runt om.'),
      (0.6, 'Använd jokern för att få fart', 'Vägg – men poäng bara på dribbling.'),
      (tg - 0.4, 'Dribbla över motståndarens linje: poäng', 'Våga utmana.'),
      (tg + 1.0, '60 sekunder – sedan rotera', 'Försvara: låg och sidställd.')]
finish(d, 'ps08', 'fyra-kvadrater-1-mot-1-med-jokrar', ['Fyra kvadrater', '1 mot 1 med jokrar'], 'Fyra kvadrater 10 × 10 m · Jokrar runt om',
       fp, 'DUELL', [('box', *s_) for s_ in SQ], [lab(tg, tg + 1.6, (28, 16), '+1')])

# ============ ps09 Innelag och utelag ============
d = Drill()
BP = [(30, 34), (66, 38), (48, 60)]; RP = [(40, 46), (60, 56), (36, 66)]; WP = [(50, 12), (88, 50), (50, 88), (12, 50)]
team(d, 'b', B, BP); team(d, 'r', R, RP); team(d, 'w', YEL, WP, ['U'] * 4)
for k in range(3): wander(d, f'r{k}', 0, 17.9, boxes([RP[k]], 5)[0], 14200 + k, 1.6)
b = d.newball(rec(d, 'b0', 0)); seq = ['w0', 'b1', 'w1', 'b2', 'w2', 'b0', 'w3', 'b1', 'w0', 'b2']
t = chain(d, b, 0.4, seq, 0.25); cnt = arrivals(d, b)[:10]
fp = [(0, 'Två lag inne, ett lag runt om', 'Utelaget spelar med laget som har bollen.'),
      (1.2, 'Använd utespelarna', 'Spelbar hela tiden.'),
      (cnt[5], 'Tio passningar i följd = poäng', ''),
      (cnt[-1], 'Byte direkt vid bollförlust', 'Byt utelag var tredje minut.')]
finish(d, 'ps09', 'innelag-och-utelag', ['Innelag', 'och utelag'], 'Ruta 20 × 20 m · Utelag på sidorna',
       fp, 'POSITIONSSPEL', [('box', 16, 16, 84, 84)], counter(cnt, pos=(90, 92), last='+1'))

if __name__ == '__main__': render(C, sys.argv)
