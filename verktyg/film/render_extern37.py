# Externa övningar, omgång 37 (fjorton st). Regel: först d.mv, sedan d.carry; först mottagarens rörelse, sedan passningen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e9', __file__.replace('render_extern37.py', 'render_extern9.py'))
e9 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e9); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e9.finish, e9.rec, e9.chain, e9.wander, e9.counter, e9.arrivals
lab, hide, show, team, boxes, drive, shoot = e9.lab, e9.hide, e9.show, e9.team, e9.boxes, e9.drive, e9.shoot
factor, swap_color, stand, countdown, countup, win = e9.factor, e9.swap_color, e9.stand, e9.countdown, e9.countup, e9.win
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'

# ============ wj05 Spelarna först – lekmatch utan coachning ============

# ============ ps10 Konmålspassningar i par ============
d = Drill()
PR = [(30, 24, 30, 76), (70, 24, 70, 76)]
for k, (x1, y1, x2, y2) in enumerate(PR): d.p(f'a{k}', '', B, (x1, y1)); d.p(f'c{k}', '', R if k else B, (x2, y2))
cnt = []
for k, (x1, y1, x2, y2) in enumerate(PR):
    b = d.newball(rec(d, f'a{k}', 0)); t = 0.4 + 0.3 * k; side = 1
    for rep in range(6):
        rcv = f'c{k}' if rep % 2 == 0 else f'a{k}'; ry = y2 if rep % 2 == 0 else y1
        t = d.pas(b, t + 0.2, rec(d, rcv, t + 1.0)); cnt.append(t) if k == 0 else None
        nx = (x1 if rep % 2 == 0 else x1) + 5 * side; side = -side
        d.mv(rcv, t, t + 0.4, (nx, ry)); d.carry(b, rcv, t, t + 0.4); t += 0.4                                    # flytta bollen åt sidan
fp = [(0, 'Par med en boll', 'Passa genom konmålet.'),
      (1.2, 'Ta emot – flytta bollen åt sidan', 'Mottagning bort från konen.'),
      (4.0, 'Passa tillbaka genom målet', 'Insida, fot vid sidan av bollen.'),
      (8.0, 'Räkna träffar på 60 sekunder', 'Svårare: ett tillslag.')]
finish(d, 'ps10', 'konmalspassningar-i-par', ['Konmålspassningar', 'I par'], 'Konmål 1 m brett · 10–12 m mellan spelarna',
       fp, 'PASSNING', [('cone', x, 50) for x in (27, 33, 67, 73)], counter(cnt, pos=(14, 50), last=None))

# ============ ps11 Linjebollen – vänd spelet ============
d = Drill()
BP = [(24, 70), (76, 70), (50, 58)]; RP = [(34, 44), (62, 46), (50, 30)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b0', 0))
d.mv('r0', 0.3, 1.8, (28, 56)); d.mv('r1', 0.3, 1.8, (36, 50))                                             # röda flyttar mot bollsidan
t = d.pas(b, 0.6, rec(d, 'b2', 1.4)); t = d.pas(b, t + 0.3, rec(d, 'b1', t + 1.2)); tsw = t                 # sidbyte
d.mv('r1', tsw - 0.4, tsw + 1.2, (68, 40)); t = drive(d, b, 'b1', tsw, (80, 30), 16); t = drive(d, b, 'b1', t, (82, 10), 16)
stand(d, 'b1', t, t + 0.8); d.carry(b, 'b1', t, t + 0.8)
fp = [(0, 'Tre mot tre', 'Poäng: dribbla in och stoppa bollen på linjen.'),
      (1.6, 'Bredd drar isär försvaret', ''),
      (tsw - 0.3, 'Byt sida!', 'Sidbyte innan poängen dubblar den.'),
      (t - 0.6, 'Driv in i ytan – stoppa på linjen', '')]
finish(d, 'ps11', 'linjebollen-vand-spelet', ['Linjebollen', 'Vänd spelet'], 'Plan 20 × 25 m · Mållinjer',
       fp, 'SPELÖVNING', [('box', 10, 8, 90, 92), ('zone', 10, 6, 90, 10, (240, 210, 90), ''), ('zone', 10, 90, 90, 94, (240, 210, 90), '')],
       [lab(tsw, tsw + 1.4, (88, 66), 'SIDBYTE'), lab(t, t + 1.8, (60, 18), 'x2')])

# ============ ps13 Speluppbyggnad – tre passningar innan mitten ============
d = Drill(); d.p('mvb', 'MV', B, (50, 96)); d.p('mvr', 'MV', R, (50, 4))
BP = [(22, 80), (78, 80), (50, 70), (30, 56), (70, 58)]; RP = [(30, 46), (70, 46), (50, 40), (36, 26), (64, 24)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'mvb', 0))
t = d.pas(b, 0.4, rec(d, 'b0', 1.2)); cnt = [t]
d.mv('r0', 0.6, t + 0.4, (28, 52)); t = d.pas(b, t + 0.3, rec(d, 'b2', t + 1.0)); cnt.append(t)            # får bara pressa från mittlinjen
t = d.pas(b, t + 0.3, rec(d, 'b1', t + 1.0)); cnt.append(t)
d.mv('b4', t - 0.4, t + 0.8, (74, 40)); t = d.pas(b, t + 0.3, rec(d, 'b4', t + 1.2)); tmid = t                # förbi mitten
d.mv('b3', tmid - 0.6, tmid + 1.0, (40, 24)); t = d.pas(b, tmid + 0.3, rec(d, 'b3', tmid + 1.2)); tg = shoot(d, b, t + 0.05, (46, 1))
for k, ps in enumerate([(34, 30), (64, 32), (50, 22)]): d.mv(f'r{k}', tmid - 0.2, tg, ps)
fp = [(0, 'Fem mot fem – anfallet startar hos målvakten', ''),
      (1.0, 'Tre passningar på egen halva', 'Motståndarna pressar först från mittlinjen.'),
      (tmid - 0.4, 'Nu får ni passera mitten', 'Spela förbi första pressen.'),
      (tg - 0.3, 'Avslut', 'Bredd och djup från början.')]
finish(d, 'ps13', 'speluppbyggnad-tre-passningar-innan-mitten', ['Speluppbyggnad', 'Tre passningar innan mitten'], 'Plan 40 × 30 m · Två mål',
       fp, 'SMÅLAGSSPEL', [('box', 6, 2, 94, 98), ('line', [(6, 50), (94, 50)])], counter(cnt, pos=(90, 66), last=None) + [lab(tmid, tmid + 1.4, (88, 46), 'GÅ!')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ ps14 Väggspel och avslut i två led ============
d = Drill(); d.p('mv', 'MV', R, (50, 4)); d.p('v', 'V', YEL, (50, 34))
for tm, x in (('a', 22), ('c', 78)):
    for k in range(3): d.p(f'{tm}{k}', '', B, (x + (-4 if x < 50 else 4) * k, 76 + 5 * k))
ex = []; t = 0.4
for rep, (tm, x) in enumerate([('a', 22), ('c', 78), ('a', 22)]):
    pid = f'{tm}{0 if rep < 2 else 1}'
    if rep == 2: d.mv(pid, 0.6, t - 0.2, (22, 76))
    bb = d.newball(rec(d, pid, 0) if rep < 2 else (200, 200))
    if rep == 2: show(d, bb, t - 0.1, rec(d, pid, t - 0.1))
    tp = d.pas(bb, t, rec(d, 'v', t + 0.8)); d.mv(pid, t + 0.1, tp + 0.9, (40 if x < 50 else 60, 24))
    tr = d.pas(bb, tp + 0.15, rec(d, pid, tp + 0.9)); tg = shoot(d, bb, tr + 0.05, (44 if x < 50 else 56, 1)); hide(d, bb, tg + 0.3)
    d.mv(pid, tg + 0.3, tg + 2.4, (x + (-10 if x < 50 else 10), 92)); t = tr + 0.4
fp = [(0, 'Passa in till väggen', 'Två led, målvakt i mål.'),
      (1.2, 'Returen i löpningen – avslut', 'Avslut med få touch.'),
      (3.4, 'Nästa från andra ledet direkt', 'Passning i fart.'),
      (6.0, 'Följ upp returen', 'Variant: väggen vänder och skjuter själv.')]
finish(d, 'ps14', 'vaggspel-och-avslut-i-tva-led', ['Väggspel och avslut', 'I två led'], 'Två led · Vägg vid straffområdet',
       fp, 'AVSLUT', [])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ ps15 Kungen av planen 3 mot 3 ============
d = Drill(); d.p('t', 'T', T_COL, (97, 50))
BP = [(30, 64), (66, 62), (48, 48)]; RP = [(36, 36), (62, 34), (52, 56)]; YP = [(40, 96), (50, 97), (60, 96)]
team(d, 'b', B, BP); team(d, 'r', R, RP); team(d, 'y', YEL, YP)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b2', 'b1'], 0.3); t = drive(d, b, 'b1', t, (58, 18), 16); tg = d.pas(b, t + 0.1, (50, 4), 0.4); hide(d, b, tg + 0.3)
for k in range(3): d.mv(f'r{k}', tg + 0.2, tg + 2.2, (38 + 12 * k, 3)); d.mv(f'y{k}', tg + 0.2, tg + 1.8, RP[k])   # röda ut, gula in
b2 = d.newball((200, 200)); show(d, b2, tg + 1.9, rec(d, 't', tg + 1.9)); t = d.pas(b2, tg + 2.0, rec(d, 'y1', tg + 2.9), 0.9)
t = chain(d, b2, t, ['y2', 'y0'], 0.3)
fp = [(0, 'Tre lag om tre', 'Ett lag vilar bakom målen.'),
      (1.4, 'Avsluta tidigt', ''),
      (tg - 0.2, 'Mål – laget som släppte in går ut', ''),
      (tg + 1.9, 'Vilande laget in direkt', 'Laget som håller längst vinner.')]
finish(d, 'ps15', 'kungen-av-planen-3-mot-3', ['Kungen av planen', '3 mot 3'], 'Plan 20 × 25 m · Småmål',
       fp, 'SMÅLAGSSPEL', [('box', 12, 4, 88, 92), ('smallgoal', 50, 4), ('smallgoal', 50, 92)], [lab(tg, tg + 1.6, (68, 12), 'UT!')])

# ============ ps16 2 mot 1 – överlapp eller inspel ============
d = Drill(); d.p('mv', 'MV', R, (50, 4)); d.p('a', '', B, (40, 78)); d.p('c', '', B, (62, 82)); d.p('f', 'F', R, (48, 40))
b = d.newball(rec(d, 'a', 0))
t = drive(d, b, 'a', 0.4, (44, 52), 12); d.mv('f', 0.6, t, (46, 40))                                     # driver – låser försvararen
d.mv('c', 0.6, t + 0.8, (74, 40)); d.mv('f', t, t + 0.6, (44, 44))                                         # överlapp
t = d.pas(b, t + 0.3, rec(d, 'c', t + 1.0)); t = drive(d, b, 'c', t, (68, 20), 16); tg = shoot(d, b, t + 0.05, (54, 1))
d.mv('f', t - 0.6, t, (58, 30)); d.mv('a', t - 1.0, tg, (48, 22))
fp = [(0, 'Två anfallare mot en försvarare', ''),
      (0.6, 'Driv mot försvararen för att låsa', ''),
      (2.0, 'Kompisen väljer: överlapp eller inspel', 'Rätt tajmning.'),
      (tg - 0.4, 'Avslut tidigt', 'Byt roller efter varje anfall.')]
finish(d, 'ps16', '2-mot-1-overlapp-eller-inspel', ['2 mot 1', 'Överlapp eller inspel'], 'Yta 20 × 30 m · Mål med målvakt',
       fp, 'ÖVERLÄGSENHET', [('box', 20, 4, 86, 92)])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ pl01 Orienterad mottagning i rondo ============
d = Drill()
OU = [(50, 20), (80, 50), (50, 80), (20, 50)]; team(d, 'b', B, OU); team(d, 'f', R, [(42, 44), (58, 56)], ['', ''])
b = d.newball(rec(d, 'b0', 0)); t = 0.4; cnt = []
for nk, nxt, f in [(1, 2, 'f1'), (2, 3, 'f1'), (3, 0, 'f0'), (0, 1, 'f0'), (1, 2, 'f1'), (2, 3, 'f1')]:
    tx, ty = OU[nk]; d.mv(f, t, t + 0.6, ((tx + 50) / 2, (ty + 50) / 2))
    t = d.pas(b, t + 0.15, rec(d, f'b{nk}', t + 0.85)); cnt.append(t)
    nx, ny = OU[nxt]; d.mv(f'b{nk}', t, t + 0.35, (tx + (nx - tx) * 0.12, ty + (ny - ty) * 0.12)); d.carry(b, f'b{nk}', t, t + 0.35)   # touch mot nästa
    d.mv(f'b{nk}', t + 0.7, t + 1.4, OU[nk]); t += 0.35
fp = [(0, 'Fyra ute, två inne', ''),
      (1.2, 'Mottagning bort från försvararen', 'Och mot nästa passning.'),
      (4.4, 'Skanna före mottagningen', 'Öppen kropp.'),
      (8.0, 'Bakåt eller stilla = poäng till försvaret', 'Tio passningar = poäng.')]
finish(d, 'pl01', 'orienterad-mottagning-i-rondo', ['Orienterad mottagning', 'I rondo'], 'Ruta 12 × 12 m · Fyra mot två',
       fp, 'RONDO', [('box', 14, 14, 86, 86)], counter(cnt, pos=(90, 92), last=None))

# ============ pl02 Orienterad mottagning – spel mot linje ============
d = Drill()
BP = [(28, 72), (70, 70), (44, 56), (60, 40)]; RP = [(34, 44), (64, 52), (50, 64), (42, 28)]
team(d, 'b', B, BP); team(d, 'r', R, RP); team(d, 'j', YEL, [(6, 50), (94, 50)], ['J', 'J'])
for k in (0, 1): wander(d, f'r{k}', 0, 6, boxes([RP[k]], 4)[0], 14300 + k, 1.6)
b = d.newball(rec(d, 'b0', 0))
d.mv('r2', 0.4, 1.6, (46, 60)); t = d.pas(b, 0.4, rec(d, 'b2', 1.2))                                     # ryggen mot – måste spela vägg
tv = d.pas(b, t + 0.2, rec(d, 'j1', t + 1.2)); d.mv('b3', tv - 0.6, tv + 0.6, (66, 34))
t = d.pas(b, tv + 0.2, rec(d, 'b3', tv + 1.0)); d.mv('b3', t, t + 0.35, (64, 28)); d.carry(b, 'b3', t, t + 0.35)   # rättvänd
t = drive(d, b, 'b3', t + 0.35, (62, 8), 18); d.mv('r3', t - 1.4, t, (54, 14))
fp = [(0, 'Fyra mot fyra plus två jokrar', ''),
      (1.0, 'Ryggen mot spelriktningen – spela vägg', 'Läs pressen.'),
      (tv + 0.4, 'Ta emot rättvänd i fart framåt', ''),
      (t - 0.6, 'Dribbla över linjen: poäng', '')]
finish(d, 'pl02', 'orienterad-mottagning-spel-mot-linje', ['Orienterad mottagning', 'Spel mot linje'], 'Plan 25 × 30 m · Jokrar på kanterna',
       fp, 'SPELÖVNING', [('box', 10, 6, 90, 94), ('zone', 10, 4, 90, 8, (240, 210, 90), ''), ('zone', 10, 92, 90, 96, (240, 210, 90), '')],
       [lab(1.2, 2.4, (32, 52), 'VÄGG'), lab(t, t + 1.6, (74, 12), '+1')])

# ============ pl03 Spela den fria spelaren ============
d = Drill()
OU = [(50, 18), (80, 40), (70, 78), (30, 78), (20, 40)]; team(d, 'b', B, OU); team(d, 'f', R, [(44, 46), (58, 54)], ['', ''])
b = d.newball(rec(d, 'b0', 0)); t = 0.4
for nk, shadow in [(4, 1), (3, 2), (1, 4), (2, 0)]:
    sx, sy = OU[shadow]; d.mv('f0', t, t + 0.7, ((sx + 50) / 2, (sy + 50) / 2))                              # skuggar en passningslinje
    t = d.pas(b, t + 0.3, rec(d, f'b{nk}', t + 1.1))
d.mv('f0', t - 0.4, t + 0.4, (40, 56)); d.mv('f1', t - 0.4, t + 0.4, (62, 56)); tg = d.pas(b, t + 0.3, rec(d, 'b0', t + 1.3), 1.0)  # mellan båda
fp = [(0, 'Fem ute, två inne', 'Försvararna skuggar passningslinjer.'),
      (1.2, 'Spela alltid till den som inte är täckt', 'Skanna efter fri spelare.'),
      (4.0, 'Rörelse för att bli fri', 'Snabbt beslut.'),
      (tg - 1.0, 'Genom båda försvararna: 2 poäng', '')]
finish(d, 'pl03', 'spela-den-fria-spelaren', ['Spela den', 'fria spelaren'], 'Ruta 15 × 15 m · Fem mot två',
       fp, 'RONDO', [('box', 12, 12, 88, 88)], [lab(tg, tg + 1.8, (64, 28), '+2')])

# ============ pl04 Fri spelare mellan linjerna – smålagsspel ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96)); d.p('jk', 'J', YEL, (76, 60))
BP = [(24, 82), (50, 84), (76, 82), (40, 64), (52, 46)]; RP = [(30, 30), (50, 26), (70, 30), (38, 48), (62, 46)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b1', 0))
t = d.pas(b, 0.4, rec(d, 'b3', 1.2)); d.mv('b4', 0.6, t + 0.4, (50, 38))                                   # mellan mittfält och backlinje
t = d.pas(b, t + 0.2, rec(d, 'b4', t + 1.0)); tf = t; d.mv('b4', t, t + 0.35, (50, 34)); d.carry(b, 'b4', t, t + 0.35)
d.mv('b2', tf - 0.8, tf + 0.8, (70, 18)); t = d.pas(b, tf + 0.4, rec(d, 'b2', tf + 1.1)); tg = shoot(d, b, t + 0.05, (54, 1))
d.mv('r3', tf - 0.4, tf + 0.6, (44, 40)); d.mv('r4', tf - 0.4, tf + 0.6, (58, 38))
fp = [(0, 'Fem mot fem plus joker', ''),
      (0.8, 'Stå mellan linjerna', 'Mellan motståndarnas mittfält och backlinje.'),
      (tf - 0.2, 'Fri mellan linjerna – öppen kropp', 'Spela snabbt framåt.'),
      (tg - 0.3, 'Mål via spelaren mellan linjerna: dubbelt', '')]
finish(d, 'pl04', 'fri-spelare-mellan-linjerna-smalagsspel', ['Fri spelare mellan linjerna', 'Smålagsspel'], 'Plan 40 × 30 m · Två mål',
       fp, 'SMÅLAGSSPEL', [('box', 6, 2, 94, 98), ('zone', 6, 34, 94, 42, (240, 210, 90), '')], [lab(tg, tg + 1.8, (54, 14), 'x2')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ pl05 Nödstöd – alltid två vinklar ============
d = Drill()
team(d, 'b', B, [(32, 34), (68, 34), (50, 70)]); d.p('f', '', R, (50, 46))
b = d.newball(rec(d, 'b0', 0)); t = 0.4; cnt = []; holder = 'b0'
for nk, spots in [('b1', {'b0': (34, 66), 'b2': (66, 72)}), ('b2', {'b0': (28, 48), 'b1': (78, 54)}), ('b0', {'b1': (60, 26), 'b2': (24, 74)}), ('b1', {'b0': (36, 30), 'b2': (76, 76)})]:
    tx, ty = at(d.pl[nk]['tr'], t); d.mv('f', t, t + 0.7, ((tx + 50) / 2, (ty + 50) / 2))
    t = d.pas(b, t + 0.15, rec(d, nk, t + 0.9)); cnt.append(t)
    for pid, ps in spots.items(): d.mv(pid, t - 0.3, t + 0.6, ps)                                               # rör dig efter passningen
    t += 0.3
fp = [(0, 'Tre mot en', 'Bollhållaren har alltid två stöd i vinkel.'),
      (1.2, 'Rör dig efter varje passning', 'Vinkel, inte linje.'),
      (4.0, 'Stöd i linje bakom försvararen = bollförlust', ''),
      (7.0, 'Kort avstånd under press', 'Tio passningar ger poäng.')]
finish(d, 'pl05', 'nodstod-alltid-tva-vinklar', ['Nödstöd', 'Alltid två vinklar'], 'Ruta 10 × 10 m · Tre mot en',
       fp, 'RONDO', [('box', 14, 14, 86, 86)], counter(cnt, pos=(90, 92), last=None))

# ============ pl06 Tala genom bollen ============
d = Drill()
BP = [(36, 70), (64, 70), (50, 50)]; RP = [(40, 40), (60, 44), (50, 62)]
team(d, 'b', B, BP); team(d, 'r', R, RP); team(d, 's', YEL, [(6, 40), (94, 40)], ['S', 'S'])
b = d.newball(rec(d, 'b0', 0))
d.mv('r2', 0.3, 1.4, (52, 56)); t = d.pas(b, 0.4, rec(d, 'b2', 0.9), 0.5); th = t                          # hård passning på bortre foten
d.mv('b2', t, t + 0.4, (54, 44)); d.carry(b, 'b2', t, t + 0.4); t = drive(d, b, 'b2', t + 0.4, (56, 26), 16)   # vänd
d.mv('r0', t - 1.2, t, (50, 30)); ts = d.pas(b, t + 0.2, rec(d, 's1', t + 1.4), 1.2)
d.mv('b1', ts - 0.4, ts + 0.6, (70, 30)); t = d.pas(b, ts + 0.3, rec(d, 'b1', ts + 1.4), 1.1)                  # mjuk på närmre foten = tillbaka
t = drive(d, b, 'b1', t + 0.1, (72, 8), 16)
fp = [(0, 'Tre mot tre med två stöd på kanterna', ''),
      (th - 0.4, 'Hård passning på bortre foten = vänd', 'Passningen är ett budskap.'),
      (ts - 0.4, 'Mjuk passning på närmre foten = spela tillbaka', 'Mottagaren läser passningen.'),
      (t - 0.6, 'Dribbla över linjen: poäng', '')]
finish(d, 'pl06', 'tala-genom-bollen', ['Tala genom', 'bollen'], 'Plan 20 × 25 m · Stödspelare på kanterna',
       fp, 'SPELÖVNING', [('box', 10, 6, 90, 94), ('zone', 10, 4, 90, 8, (240, 210, 90), ''), ('zone', 10, 92, 90, 96, (240, 210, 90), '')],
       [lab(th, th + 1.2, (62, 54), 'VÄND'), lab(t, t + 1.6, (82, 12), '+1')])

# ============ pl07 Försvara väggspel ============
d = Drill(); d.p('mv', 'MV', R, (50, 4)); d.p('a', '', B, (40, 80)); d.p('c', '', B, (62, 54)); d.p('f', 'F', R, (46, 60))
b = d.newball(rec(d, 'a', 0))
t = drive(d, b, 'a', 0.4, (40, 66), 12); d.mv('f', 0.6, t, (42, 58))
t = d.pas(b, t + 0.1, rec(d, 'c', t + 0.7)); d.mv('a', t - 0.5, t + 1.0, (46, 40))                            # passar och springer
d.mv('f', t - 0.4, t + 0.9, (46, 44))                                                                          # följer löparen
tw = d.pas(b, t + 0.3, rec(d, 'f', t + 0.9), 0.6); d.mv('f', tw, tw + 1.2, (40, 64)); d.carry(b, 'f', tw, tw + 1.2)
fp = [(0, 'Två anfallare mot en försvarare', 'Anfallarna söker väggspel.'),
      (1.4, 'Följ den som passar och springer', 'Titta inte efter bollen.'),
      (2.6, 'Kroppen mellan löpare och mål', 'Läs passningen.'),
      (tw - 0.2, 'Bruten retur: poäng till försvararen', '')]
finish(d, 'pl07', 'forsvara-vaggspel', ['Försvara', 'väggspel'], 'Yta 20 × 25 m · Mål med målvakt',
       fp, 'DUELL', [('box', 20, 4, 80, 92)], [lab(tw, tw + 1.6, (60, 42), '+1 F')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ pl08 Press och täckning 2 mot 2 ============
d = Drill()
team(d, 'a', B, [(30, 76), (70, 78)]); team(d, 'f', R, [(36, 46), (60, 40)])
for k in range(2): d.p(f'q{k}', '', B, (6, 70 + 6 * k)); d.p(f'p{k}', '', R, (94, 30 + 6 * k))
b = d.newball(rec(d, 'a0', 0))
d.mv('f0', 0.3, 1.4, (32, 66)); d.mv('f1', 0.3, 1.4, (46, 56))                                               # press och täckning snett bakom
t = d.pas(b, 1.2, rec(d, 'a1', 2.2), 1.0)
d.mv('f1', 1.3, t, (66, 68)); d.mv('f0', 1.3, t, (52, 56))                                                    # byter roller i bollens rullning
tw = win(d, b, 'f1', 'a1', t + 0.6, 0.6); t = drive(d, b, 'f1', tw, (60, 48), 16)
fp = [(0, 'Två mot två', 'Nya par från kön.'),
      (0.6, 'Närmast pressar – den andra täcker', 'Rätt avstånd mellan press och täckning.'),
      (1.4, 'Byt roll i bollens rullning', 'Prata!'),
      (tw - 0.2, 'Vinn bollen och dribbla över mittlinjen', 'Poäng till försvararna.')]
finish(d, 'pl08', 'press-och-tackning-2-mot-2', ['Press och täckning', '2 mot 2'], 'Yta 20 × 20 m · Mittlinje',
       fp, 'DUELL', [('box', 12, 12, 88, 88), ('line', [(12, 50), (88, 50)])], [lab(t, t + 1.6, (60, 42), '+1')])

if __name__ == '__main__': render(C, sys.argv)
