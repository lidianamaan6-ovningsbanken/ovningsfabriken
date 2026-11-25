# Externa övningar, omgång 38 (fjorton st). Regel: först d.mv, sedan d.carry; först mottagarens rörelse, sedan passningen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e9', __file__.replace('render_extern38.py', 'render_extern9.py'))
e9 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e9); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e9.finish, e9.rec, e9.chain, e9.wander, e9.counter, e9.arrivals
lab, hide, show, team, boxes, drive, shoot = e9.lab, e9.hide, e9.show, e9.team, e9.boxes, e9.drive, e9.shoot
factor, swap_color, stand, countdown, countup, win = e9.factor, e9.swap_color, e9.stand, e9.countdown, e9.countup, e9.win
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'

# ============ wj05 Spelarna först – lekmatch utan coachning ============

# ============ pl09 Defensiva trianglar 3 mot 3 ============
d = Drill(); d.p('t', 'T', T_COL, (97, 50))
BP = [(26, 70), (70, 70), (48, 52)]; RP = [(34, 38), (62, 40), (50, 26)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b0', 0))
d.mv('r0', 0.4, 1.6, (30, 58)); d.mv('r2', 0.4, 1.8, (40, 44)); d.mv('r1', 0.4, 1.8, (56, 36))               # press, täckning, balans
t = d.pas(b, 0.6, rec(d, 'b2', 1.4)); d.mv('r2', 1.4, 2.4, (46, 46)); d.mv('r0', 1.4, 2.4, (38, 54)); d.mv('r1', 1.4, 2.4, (62, 40))
tf = t + 0.6; stand(d, 'b2', t, tf + 1.6); d.carry(b, 'b2', t, tf + 1.6)                                       # tränaren fryser
for k in range(3): stand(d, f'r{k}', 2.4, tf + 1.6)
tw = win(d, b, 'r2', 'b2', tf + 2.2, 0.6); d.mv('r1', tw - 0.6, tw + 0.6, (66, 60))
t = d.pas(b, tw + 0.2, rec(d, 'r1', tw + 0.9)); t = drive(d, b, 'r1', t, (60, 86), 18); tg = d.pas(b, t + 0.1, (50, 94), 0.4); hide(d, b, tg + 0.3)
fp = [(0, 'Tre mot tre', 'Försvaret har alltid en triangel.'),
      (1.2, 'En pressar, en täcker, en balanserar', 'Flytta som en grupp.'),
      (tf, 'STOPP – vem har vilken roll?', 'Tränaren fryser spelet.'),
      (tw - 0.2, 'Bollvinst på deras halva – mål dubbelt', 'Kompakt runt bollen.')]
finish(d, 'pl09', 'defensiva-trianglar-3-mot-3', ['Defensiva trianglar', '3 mot 3'], 'Plan 20 × 25 m · Småmål',
       fp, 'SMÅLAGSSPEL', [('box', 12, 6, 88, 94), ('line', [(12, 50), (88, 50)]), ('smallgoal', 50, 6), ('smallgoal', 50, 94)],
       [lab(tf, tf + 1.6, (30, 46), 'PRESS'), lab(tf, tf + 1.6, (52, 38), 'TÄCK'), lab(tf, tf + 1.6, (74, 32), 'BALANS'), lab(tg, tg + 1.8, (50, 84), 'x2')])

# ============ pl10 Markeringsavstånd ============
d = Drill(); d.p('t', 'T', T_COL, (97, 50))
BP = [(24, 70), (76, 68), (40, 46), (66, 40)]; RP = [(28, 60), (70, 58), (44, 38), (60, 28)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b0', 0))
d.mv('r0', 0.3, 1.2, (26, 64)); d.mv('r1', 0.3, 1.2, (62, 50)); d.mv('r3', 0.3, 1.2, (54, 30))               # nära bollen tätt, långt bort släpper
t = d.pas(b, 0.6, rec(d, 'b2', 1.4)); tf = t + 0.4
d.mv('r2', t - 0.6, t + 0.2, (42, 42)); d.mv('r0', t - 0.6, t + 0.6, (32, 58))
stand(d, 'b2', t, tf + 1.8); d.carry(b, 'b2', t, tf + 1.8)
t = d.pas(b, tf + 2.0, rec(d, 'b1', tf + 3.0), 1.0)                                                            # ny passning – ställ om
d.mv('r1', tf + 2.0, t, (74, 62)); d.mv('r2', tf + 2.0, t, (52, 44)); d.mv('r0', tf + 2.0, t, (40, 50))
fp = [(0, 'Fyra mot fyra', 'Avståndet styrs av bollen.'),
      (1.0, 'Nära bollen: markera tätt', 'Längre bort: släpp och täck yta.'),
      (tf, 'STOPP – kolla avstånden', 'Se både boll och spelare.'),
      (tf + 2.0, 'Ställ om vid varje passning', '')]
finish(d, 'pl10', 'markeringsavstand', ['Markerings-', 'avstånd'], 'Plan 25 × 30 m · Småmål',
       fp, 'SMÅLAGSSPEL', [('box', 10, 6, 90, 94), ('smallgoal', 50, 6), ('smallgoal', 50, 94)],
       [lab(tf, tf + 1.8, (42, 32), 'TÄTT'), lab(tf, tf + 1.8, (80, 52), 'SLÄPP')])

# ============ pl11 Djupledslöpningar – start i rätt tid ============
d = Drill(); d.p('mv', 'MV', R, (50, 4)); d.p('p', 'P', B, (50, 88)); d.p('m', 'M', B, (44, 62)); d.p('a', 'A', B, (66, 46))
b = d.newball(rec(d, 'p', 0))
d.mv('m', 0.4, 1.4, (46, 66)); t = d.pas(b, 0.6, rec(d, 'm', 1.6)); d.mv('m', t, t + 0.35, (46, 62)); d.carry(b, 'm', t, t + 0.35)   # rättvänd
ts = t; d.mv('a', ts, ts + 0.8, (58, 36)); d.mv('a', ts + 0.8, ts + 2.0, (54, 18))                              # diagonalt, sedan rakt
t = d.pas(b, ts + 0.6, (54, 20), 1.2); d.carry(b, 'a', t, t + 0.3); tg = shoot(d, b, t + 0.35, (48, 1))
fp = [(0, 'Passare, mittfältare, anfallare', ''),
      (ts - 0.4, 'Mittfältaren tar emot rättvänd', 'Då startar anfallaren.'),
      (ts + 0.4, 'Diagonalt – sedan rakt mot mål', 'Fel tajmning = offside.'),
      (tg - 0.4, 'Första touch mot mål', '')]
finish(d, 'pl11', 'djupledslopningar-start-i-ratt-tid', ['Djupledslöpningar', 'Start i rätt tid'], 'Halvplan · Konlinje som backlinje',
       fp, 'AVSLUT', [('cone', x, 34) for x in range(16, 90, 12)], [lab(ts, ts + 1.2, (76, 46), 'NU!')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ pl12 Djupledsspel 5 mot 4 ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
BP = [(20, 66), (40, 70), (60, 70), (80, 64), (50, 50)]; RP = [(24, 36), (42, 32), (58, 32), (76, 36)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b1', 0))
t = d.pas(b, 0.4, rec(d, 'b2', 1.2)); d.mv('b4', 0.6, t + 0.4, (54, 46)); d.mv('r2', 0.6, t + 0.6, (56, 40))   # skapar yta
t = d.pas(b, t + 0.3, rec(d, 'b4', t + 1.0))
d.mv('b3', t - 0.6, t + 1.4, (70, 16)); tp = d.pas(b, t + 0.3, (68, 18), 1.1)                                   # bakom backlinjen
d.carry(b, 'b3', tp, tp + 0.3); tg = shoot(d, b, tp + 0.35, (54, 1))
d.mv('r3', tp - 1.2, tp, (72, 26))
fp = [(0, 'Fem anfallare mot fyra försvarare', ''),
      (1.2, 'Skapa yta för löparen', ''),
      (tp - 1.0, 'Passning bakom backlinjen', 'Tajmning före fart.'),
      (tg - 0.3, 'Mål efter djupledspass: dubbelt', 'Försvaret kontrar mot två minimål.')]
finish(d, 'pl12', 'djupledsspel-5-mot-4', ['Djupledsspel', '5 mot 4'], 'Halvplan · Mål och två minimål',
       fp, 'ÖVERLÄGSENHET', [('smallgoal', 30, 96), ('smallgoal', 70, 96)], [lab(tg, tg + 1.8, (54, 12), 'x2')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ pl13 Tredje man – passningsmönster ============
d = Drill()
TRI = [((22, 82), (34, 52), (14, 30)), ((60, 82), (72, 52), (52, 30))]
for i, (A, B_, C_) in enumerate(TRI): d.p(f'a{i}', 'A', B, A); d.p(f'b{i}', 'B', B, B_); d.p(f'c{i}', 'C', B, C_)
d.p('f', '', R, (78, 46))
for i, (A, B_, C_) in enumerate(TRI):
    b = d.newball(rec(d, f'a{i}', 0)); t = 0.4 + 0.4 * i
    for rep in range(2):
        t = d.pas(b, t + 0.2, rec(d, f'b{i}', t + 1.0)); d.mv(f'c{i}', t - 0.3, t + 1.3, (C_[0] + 14, C_[1] - 6))   # C startar när B får bollen
        t = d.pas(b, t + 0.1, rec(d, f'a{i}', t + 0.7)); t = d.pas(b, t + 0.1, rec(d, f'c{i}', t + 1.0))
        tb = t; d.carry(b, f'c{i}', t, t + 0.4)
        if rep == 0:
            d.mv(f'c{i}', t + 0.4, t + 1.6, C_); d.carry(b, f'c{i}', t + 0.4, t + 1.6); t = d.pas(b, t + 1.7, rec(d, f'a{i}', t + 2.8), 1.1)
    if i == 1: d.mv('f', 0.6, 1.6, (74, 56))
fp = [(0, 'Tre spelare per triangel', ''),
      (1.0, 'A till B – B lägger tillbaka', 'Lägg tillbaka i rätt fart.'),
      (2.4, 'A spelar direkt till C', 'C startar när B får bollen.'),
      (6.0, 'Rotera positioner', 'Lägg till en passiv försvarare på B.')]
finish(d, 'pl13', 'tredje-man-passningsmonster', ['Tredje man', 'Passningsmönster'], 'Två trianglar · 10–15 m',
       fp, 'PASSNING', [])

# ============ pl14 Tredje man i rondo ============
d = Drill()
OU = [ring_pos(50, 50, 34, i, 6) for i in range(6)]; team(d, 'b', B, OU); team(d, 'f', R, [(44, 46), (58, 54)], ['', ''])
b = d.newball(rec(d, 'b0', 0))
d.mv('f0', 0.3, 1.6, (48, 38)); d.mv('f1', 0.3, 1.6, (56, 50))
t = d.pas(b, 0.5, rec(d, 'b1', 1.2)); t1 = t                                                                      # kort
t = d.pas(b, t + 0.1, rec(d, 'b0', t + 0.7)); t = d.pas(b, t + 0.1, rec(d, 'b3', t + 1.3), 1.2); t3 = t         # tillbaka – lång till tredje
d.mv('f0', t - 1.0, t + 0.4, (52, 60)); t = chain(d, b, t, ['b4', 'b2'], 0.3); tm = t
t = d.pas(b, t + 0.3, rec(d, 'b5', t + 1.3), 1.0)                                                                 # genom mitten
fp = [(0, 'Sex ute, två inne', ''),
      (t1 - 0.2, 'Kort – tillbaka …', 'Lägg tillbaka med ett touch.'),
      (t3 - 0.6, '… lång till tredje man: 2 poäng', 'Tredje man ska vara redo.'),
      (tm, 'Passning genom mitten: 1 poäng', 'Skanna innan.')]
finish(d, 'pl14', 'tredje-man-i-rondo', ['Tredje man', 'I rondo'], 'Ruta 20 × 20 m · Sex mot två',
       fp, 'RONDO', [('box', 10, 10, 90, 90)], [lab(t3, t3 + 1.6, (50, 92), '+2'), lab(t, t + 1.6, (50, 92), '+1')])

# ============ pl15 Vinn andra bollen ============
d = Drill(); d.p('mvb', 'MV', B, (50, 96)); d.p('mvr', 'MV', R, (50, 4))
BP = [(22, 74), (78, 74), (44, 50), (58, 46), (36, 34), (64, 30)]; RP = [(26, 60), (72, 58), (48, 40), (60, 54), (40, 24), (66, 20)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'mvb', 0))
for k, ps in [(2, (48, 40)), (3, (54, 34)), (4, (42, 34))]: d.mv(f'b{k}', 0.4, 1.8, ps)
for k, ps in [(2, (50, 38)), (3, (58, 44)), (0, (40, 44))]: d.mv(f'r{k}', 0.4, 1.8, ps)
t = d.pas(b, 0.6, (50, 38), 1.4)                                                                                 # långt utspel – duell
t2 = d.pas(b, t + 0.1, (56, 46), 0.5); d.mv('b3', t, t2, (54, 46)); tw = t2                                     # andra bollen
d.carry(b, 'b3', tw, tw + 0.3); d.mv('b5', tw - 0.6, tw + 0.8, (70, 22)); t = d.pas(b, tw + 0.35, rec(d, 'b5', tw + 1.1))
tg = shoot(d, b, t + 0.05, (56, 1))
fp = [(0, 'Sex mot sex', 'Varje omstart med långt utspel.'),
      (0.8, 'Stå runt duellen', 'Förutse var bollen landar.'),
      (tw - 0.2, 'Andra bollen vunnen: poäng', ''),
      (tg - 0.5, 'Anfall direkt efter vinst', 'Mål räknas som vanligt.')]
finish(d, 'pl15', 'vinn-andra-bollen', ['Vinn andra', 'bollen'], 'Plan 50 × 40 m · Två mål',
       fp, 'MATCHSPEL', [('box', 6, 2, 94, 98), ('circle', 52, 42, 9)], [lab(tw, tw + 1.6, (70, 52), '+1')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ pl16 Dra till dig och spela vidare ============
d = Drill()
OU = [(50, 18), (82, 50), (50, 82), (18, 50)]; team(d, 'b', B, OU); team(d, 'f', R, [(42, 44), (58, 56)], ['', ''])
b = d.newball(rec(d, 'b3', 0))
t = drive(d, b, 'b3', 0.4, (36, 50), 10); d.mv('f0', 0.6, t, (42, 50))                                             # dribblar in – lockar ut
d.mv('b0', t - 0.6, t + 0.4, (44, 24)); t = d.pas(b, t + 0.2, rec(d, 'b0', t + 0.8)); tp = t                       # in i ytan
t = drive(d, b, 'b0', t, (52, 30), 12); d.mv('b3', tp, tp + 1.0, OU[3])
t = chain(d, b, t, ['b1', 'b2'], 0.3)
fp = [(0, 'Fyra ute, två inne', 'Ytterspelarna får dribbla in.'),
      (0.6, 'Driv mot försvararen', 'Dra – frigör kompis.'),
      (tp - 0.4, 'Passa in i ytan han lämnade: 2 poäng', 'Passa i rätt ögonblick.'),
      (tp + 1.2, 'Spela vidare', '')]
finish(d, 'pl16', 'dra-till-dig-och-spela-vidare', ['Dra till dig', 'och spela vidare'], 'Ruta 15 × 15 m · Fyra mot två',
       fp, 'RONDO', [('box', 14, 14, 86, 86)], [lab(tp, tp + 1.6, (64, 22), '+2')])

# ============ pl17 Bjud in pressen via målvakten ============
d = Drill(); d.p('mv', 'MV', B, (50, 94))
BP = [(24, 78), (76, 78), (50, 62)]; RP = [(30, 50), (70, 50), (50, 40)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b0', 0))
t = d.pas(b, 0.4, rec(d, 'mv', 1.4), 1.0); tl = t                                                                  # lockar fram
for k, ps in [(0, (30, 76)), (2, (50, 76)), (1, (64, 72))]: d.mv(f'r{k}', 0.6, tl + 0.4, ps)
d.mv('b1', tl - 0.4, tl + 0.8, (86, 70)); t = d.pas(b, tl + 0.4, rec(d, 'b1', tl + 1.4), 1.0)                       # fria spelaren
t = drive(d, b, 'b1', t, (84, 30), 18); d.mv('b2', tl + 0.6, t, (60, 40))
fp = [(0, 'Målvakt plus tre mot tre', 'I egen tredjedel.'),
      (0.8, 'Spela till målvakten – locka fram pressen', ''),
      (tl + 0.2, 'Målvakten hittar den fria', 'Var fri i rätt tid.'),
      (t - 0.8, 'Driv över linjen: poäng', 'Motståndarna anfaller det stora målet.')]
finish(d, 'pl17', 'bjud-in-pressen-via-malvakten', ['Bjud in pressen', 'Via målvakten'], 'Egen tredjedel · Mål och linje',
       fp, 'SPELÖVNING', [('box', 10, 26, 90, 98), ('zone', 10, 24, 90, 28, (240, 210, 90), '')], [lab(tl - 0.2, tl + 1.0, (64, 86), 'LOCKA'), lab(t, t + 1.6, (72, 22), '+1')])
C[-1]['goals'] = [(50, 100)]; C[-1]['keep_goals'] = True

# ============ pl18 Offensiv markering – säkra bakom ============
d = Drill(); d.p('mvb', 'MV', B, (50, 96)); d.p('mvr', 'MV', R, (50, 4))
BP = [(36, 74), (62, 72), (30, 40), (52, 34), (74, 42)]; RP = [(48, 80), (28, 28), (50, 22), (72, 26), (60, 54)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
d.mv('b0', 0.3, 1.4, (44, 74)); d.mv('b1', 0.3, 1.4, (54, 76))                                                     # två säkrar mot röd nr 1
b = d.newball(rec(d, 'b2', 0))
t = chain(d, b, 0.6, ['b3', 'b4'], 0.3); tl = win(d, b, 'r3', 'b4', t + 0.4, 0.6)                                  # bollförlust
t = d.pas(b, tl + 0.3, (50, 74), 0.9); d.mv('b1', tl + 0.3, t, (48, 74)); d.mv('r0', tl + 0.3, t, (52, 82))
d.carry(b, 'b1', t, t + 0.4); tc = t
fp = [(0, 'Fem mot fem', 'Varje lag har en spelare som stannar högt.'),
      (0.6, 'Två bakom bollen markerar', 'Säkra innan du förlorar bollen.'),
      (tl - 0.2, 'Bollförlust – kontring', ''),
      (tc - 0.2, 'Kontringen stoppad', 'Mål på kontring räknas dubbelt.')]
finish(d, 'pl18', 'offensiv-markering-sakra-bakom', ['Offensiv markering', 'Säkra bakom'], 'Plan 40 × 30 m · Två mål',
       fp, 'SMÅLAGSSPEL', [('box', 6, 2, 94, 98)], [lab(0.6, 2.4, (64, 86), 'SÄKRA')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ pl19 Kontrapress eller retreat ============
d = Drill(); d.p('mvb', 'MV', B, (50, 96)); d.p('mvr', 'MV', R, (50, 4)); d.p('t', 'T', T_COL, (97, 50))
BP = [(30, 60), (70, 60), (40, 36), (60, 30), (50, 46)]; RP = [(34, 28), (66, 26), (44, 50), (58, 52), (50, 18)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b2', 0))
t = chain(d, b, 0.4, ['b4', 'b3'], 0.3); tl = win(d, b, 'r1', 'b3', t + 0.4, 0.6)
d.mv('b3', tl, tl + 0.8, (64, 28)); d.mv('b4', tl, tl + 1.0, (60, 36))                                             # kontrapress fem sekunder
t = d.pas(b, tl + 0.3, rec(d, 'r3', tl + 1.0)); t = d.pas(b, t + 0.3, rec(d, 'r2', t + 1.0)); tr = t                # bollen tar sig förbi
for k, ps in enumerate([(30, 72), (70, 72), (40, 64), (60, 62), (50, 70)]): d.mv(f'b{k}', tr, tr + 2.0, ps)        # retreat bakom bollen
t = drive(d, b, 'r2', tr, (44, 58), 12)
fp = [(0, 'Fem mot fem', ''),
      (tl - 0.2, 'Bollförlust – närmast pressar direkt', 'Fem sekunder.'),
      (tr - 0.2, 'Ingen vinst? Alla hem bakom bollen', 'Kompakt efter retreat.'),
      (tr + 2.0, 'Ibland ropar tränaren ”RETREAT!”', 'Hela laget gör samma sak.')]
finish(d, 'pl19', 'kontrapress-eller-retreat', ['Kontrapress', 'eller retreat'], 'Plan 40 × 30 m · Två mål',
       fp, 'SMÅLAGSSPEL', [('box', 6, 2, 94, 98)], countup(tl + 0.1, 3, (88, 30), (tr - tl) / 3) + [lab(tr, tr + 1.6, (84, 56), 'RETREAT!')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ pl20 Spindelspelet ============
d = Drill()
KP = [(24, 30), (70, 26), (30, 70), (74, 72), (50, 52), (46, 22)]
team(d, 'k', B, KP, [''] * 6); team(d, 's', R, [(14, 50), (86, 50)], ['S', 'S'])
balls = [d.newball(rec(d, f'k{k}', 0)) for k in range(6)]
for k in (0, 1, 3, 5): wander(d, f'k{k}', 0, 17.9, (12, 14, 88, 86), 14400 + k, 1.4); d.carry(balls[k], f'k{k}', 0, 17.9)
wander(d, 's1', 0, 17.9, (12, 14, 88, 86), 14410, 1.4)
d.mv('k2', 0, 2.4, (32, 66)); d.carry(balls[2], 'k2', 0, 2.4); d.mv('s0', 0, 2.4, (26, 62))
tk = d.pas(balls[2], 2.6, (4, 80), 0.7); hide(d, balls[2], tk + 0.2)                                                # sparkas ut ur nätet
d.mv('k2', tk, tk + 1.2, (40, 60)); wander(d, 'k2', tk + 1.2, 17.9, (12, 14, 88, 86), 14420, 1.4)
wander(d, 's0', tk, 17.9, (12, 14, 88, 86), 14421, 1.4)
fp = [(0, 'Alla med boll utom två spindlar', ''),
      (1.4, 'Spindlarna sparkar ut bollar ur nätet', 'Skydda bollen med kroppen.'),
      (tk + 0.2, 'Tappar du bollen blir du spindel', 'Titta upp och byt riktning.'),
      (8.0, 'Sista spelaren med boll vinner', '')]
finish(d, 'pl20', 'spindelspelet', ['Spindel-', 'spelet'], 'Yta 20 × 20 m · En boll per spelare',
       fp, 'LEK', [('box', 8, 10, 92, 90)], [lab(tk, tk + 1.6, (36, 52), 'SPINDEL!')])
swap_color(2, C[-1]['phases'][2][0], B, R)

# ============ pl21 Pacman ============
d = Drill()
LN = [('line', [(10, y), (90, y)]) for y in (20, 50, 80)] + [('line', [(x, 10), (x, 90)]) for x in (20, 50, 80)]
d.p('pm', 'P', YEL, (20, 20))
SP = [(50, 20), (80, 50), (20, 80), (50, 80), (80, 20)]
team(d, 'k', B, SP, [''] * 5)
b = d.newball(rec(d, 'pm', 0))
d.path('pm', 0.4, [(35, 20), (50, 20)], 0.8); d.carry(b, 'pm', 0.4, 2.0)
d.path('k0', 0.4, [(50, 35), (50, 50)], 0.9); d.path('k1', 0.4, [(80, 65), (80, 80), (65, 80)], 0.9)
d.path('k2', 0.4, [(20, 65), (20, 50)], 0.9); d.path('k3', 0.4, [(65, 80), (80, 80)], 0.9); d.path('k4', 0.4, [(80, 35)], 0.9)
th = d.pas(b, 2.2, rec(d, 'k0', 2.8), 0.6)                                                                           # träff!
d.carry(b, 'k0', th, th + 0.4); t2 = d.path('k0', th + 0.4, [(50, 65), (50, 80)], 0.8); d.carry(b, 'k0', th + 0.4, t2)   # ny Pacman
d.path('pm', th + 0.4, [(50, 35), (65, 50)] if False else [(35, 20)], 0.8)
d.path('k3', th, [(80, 80), (80, 65)], 0.9); d.path('k2', th, [(20, 35), (20, 20)], 0.9)
t3 = d.pas(b, t2 + 0.3, rec(d, 'k1', t2 + 1.0))
d.carry(b, 'k1', t3, t3 + 0.4); t4 = d.path('k1', t3 + 0.4, [(80, 80), (80, 60)], 0.8); d.carry(b, 'k1', t3 + 0.4, t4)   # tredje Pacman jagar
d.path('k4', t3, [(80, 20), (65, 20)], 0.8); t5 = d.pas(b, t4 + 0.2, rec(d, 'k4', t4 + 1.2), 1.0)
fp = [(0, 'Alla rör sig bara på linjerna', ''),
      (0.8, 'Pacman dribblar och passar på spelarna', 'Passa med precision.'),
      (th - 0.1, 'Träffad – du blir också Pacman', ''),
      (th + 1.2, 'Samarbeta som Pacman', 'Sista spelaren kvar vinner.')]
finish(d, 'pl21', 'pacman', ['Pac-', 'man'], 'Yta 20 × 20 m · Linjer på planen',
       fp, 'LEK', [('box', 10, 10, 90, 90)] + LN, [lab(th, th + 1.4, (62, 44), 'TRÄFF!'), lab(t3, t3 + 1.4, (72, 70), 'TRÄFF!'), lab(t5, t5 + 1.4, (66, 30), 'SISTA!')])
swap_color(1, C[-1]['phases'][2][0] + 0.1, B, YEL); swap_color(2, t3 * factor(fp) + 0.1, B, YEL); swap_color(5, t5 * factor(fp) + 0.1, B, YEL)

# ============ pl22 Från rondo till match – progressionsspel ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96))
BP = [(26, 52), (74, 50), (40, 40), (60, 60), (50, 70)]; RP = [(34, 46), (66, 44), (50, 54), (44, 62), (56, 36)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
for k in range(4): wander(d, f'r{k}', 0, 4.5, boxes([RP[k]], 4)[0], 14500 + k, 1.4)
b = d.newball(rec(d, 'b4', 0))
t = chain(d, b, 0.4, ['b0', 'b3', 'b1'], 0.3)
d.mv('b2', t - 1.0, t + 0.4, (46, 30)); t = d.pas(b, t + 0.2, rec(d, 'b2', t + 1.0)); tf = t                       # fri spelare tar bollen in
t = drive(d, b, 'b2', t, (46, 18), 16); d.mv('b0', tf, t + 0.4, (34, 16)); t = d.pas(b, t + 0.1, rec(d, 'b0', t + 0.7))
tg = shoot(d, b, t + 0.05, (44, 1)); d.mv('r4', tf, tg, (42, 12))
fp = [(0, 'Fem mot fem i mittzonen', 'Possession med syfte.'),
      (1.2, 'Hitta den fria spelaren', ''),
      (tf - 0.3, 'In i anfallszonen – nu får ni anfalla', 'Snabbt anfall när det öppnas.'),
      (tg - 0.3, 'Bollvinst? Ta er först ut ur mittzonen', '')]
finish(d, 'pl22', 'fran-rondo-till-match-progressionsspel', ['Från rondo till match', 'Progressionsspel'], 'Plan 50 × 30 m · Mittzon och anfallszoner',
       fp, 'SPELÖVNING', [('box', 6, 2, 94, 98), ('zone', 6, 30, 94, 70, (180, 220, 200), 'MITTZON')], [lab(tf, tf + 1.4, (62, 26), 'IN!')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

if __name__ == '__main__': render(C, sys.argv)
