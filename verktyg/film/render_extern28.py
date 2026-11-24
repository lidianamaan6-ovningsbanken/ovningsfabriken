# Externa övningar, omgång 28 (tolv st). Regel: först d.mv, sedan d.carry; först mottagarens rörelse, sedan passningen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e9', __file__.replace('render_extern28.py', 'render_extern9.py'))
e9 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e9); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e9.finish, e9.rec, e9.chain, e9.wander, e9.counter, e9.arrivals
lab, hide, show, team, boxes, drive, shoot = e9.lab, e9.hide, e9.show, e9.team, e9.boxes, e9.drive, e9.shoot
factor, swap_color, stand, countdown, countup, win = e9.factor, e9.swap_color, e9.stand, e9.countdown, e9.countup, e9.win
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'

# ============ ff03 Nummerspelet ============
d = Drill(); d.p('t', 'T', T_COL, (96, 50))
for k in range(4): d.p(f'b{k}', str(k + 1), B, (8, 26 + 16 * k)); d.p(f'r{k}', str(k + 1), R, (92, 26 + 16 * k))
b = d.newball(rec(d, 't', 0)); tc = 0.6
t = d.pas(b, tc + 0.4, (52, 50), 1.0)
d.mv('b1', tc + 0.4, t + 0.2, (48, 48)); d.mv('r1', tc + 0.4, t + 0.4, (60, 46))                              # ”2!”
d.carry(b, 'b1', t + 0.2, t + 0.5); t = d.pas(b, t + 0.6, rec(d, 'b0', t + 1.4))                              # spela tillbaka till linjen
t = d.pas(b, t + 0.3, rec(d, 'b1', t + 1.2)); d.mv('b1', t - 1.2, t, (40, 30)); d.mv('r1', t - 1.2, t + 0.4, (46, 26))
t = drive(d, b, 'b1', t, (46, 12), 14); tg = shoot(d, b, t + 0.1, (50, 3)); hide(d, b, tg + 0.3)
d.mv('b1', tg + 0.2, tg + 2.4, (8, 42)); d.mv('r1', tg + 0.2, tg + 2.4, (92, 42))
fp = [(0, 'Två lag med nummer på motsatta sidor', ''),
      (tc, 'Tränaren sparkar in och ropar ett nummer', ''),
      (tc + 2.4, 'De andra på linjen kan spela tillbaka', ''),
      (tg - 0.4, 'Mål', 'Inget mål på 20 sekunder? Tränaren ropar ”Byt!”.')]
finish(d, 'ff03', 'nummerspelet', ['Nummer-', 'spelet'], 'Två lag med nummer på motsatta sidor',
       fp, 'LEK', [('box', 4, 4, 96, 96), ('smallgoal', 50, 4), ('smallgoal', 50, 96)], [lab(tc - 0.2, tc + 1.4, (70, 60), '”2!”')])

# ============ ff04 2 mot 2 med rörlig målvakt ============
d = Drill()
team(d, 'b', B, [(40, 70), (50, 90)]); team(d, 'r', R, [(44, 34), (50, 10)])
b = d.newball(rec(d, 'b0', 0))
d.mv('b1', 0.4, 2.0, (62, 62)); d.mv('r1', 1.0, 2.4, (50, 12))                                               # målvakten blir utespelare med boll
t = d.pas(b, 0.6, rec(d, 'b1', 2.0), 1.2); t = drive(d, b, 'b1', t, (60, 36), 14); d.mv('r0', t - 1.2, t, (56, 30))
t = d.pas(b, t + 0.1, rec(d, 'b0', t + 0.9)); d.mv('b0', t - 1.6, t, (42, 26)); tg = shoot(d, b, t + 0.1, (46, 3)); hide(d, b, tg + 0.3)
d.mv('b1', tg, tg + 2.0, (50, 90)); d.mv('b0', tg, tg + 2.0, (40, 70))
b2 = d.newball((200, 200)); show(d, b2, tg + 1.2, rec(d, 'r1', tg + 1.2))                                     # motståndarna startar – 3 m avstånd
d.mv('r1', tg + 1.4, tg + 3.0, (60, 32)); d.carry(b2, 'r1', tg + 1.4, tg + 3.0)
fp = [(0, 'Två mot två, två mål', 'En av försvararna är målvakt.'),
      (0.8, 'Målvakten blir utespelare', 'När laget har bollen.'),
      (tg - 0.4, 'Mål', 'Extrapoäng för mål med olika kroppsdelar.'),
      (tg + 1.2, 'Start med dribbling eller passning', 'Motståndarna håller 3 m avstånd.')]
finish(d, 'ff04', '2-mot-2-med-rorlig-malvakt', ['2 mot 2', 'Med rörlig målvakt'], 'Två mål · 2 mot 2',
       fp, 'SMÅLAGSSPEL', [('box', 20, 4, 80, 96), ('smallgoal', 50, 4), ('smallgoal', 50, 96)])

# ============ ff05 Space Invaders ============
d = Drill()
XS = [24, 50, 76]
for k, x in enumerate(XS): d.p(f'u{k}', '', B, (x, 16)); d.p(f'n{k}', '', B, (x, 84))
team(d, 'm', R, [(36, 50), (64, 50)], ['', ''])
ex = []
for k, x in enumerate(XS):
    bb = d.newball(rec(d, f'u{k}', 0)); t = 0.4 + 0.5 * k
    for rep in range(5):
        a, c = (f'u{k}', f'n{k}') if rep % 2 == 0 else (f'n{k}', f'u{k}')
        if k == 1 and rep == 2:
            d.mv('m0', t - 0.6, t + 0.3, (49, 50)); t1 = d.pas(bb, t, (51, 49), 0.5); ex.append(lab(t1, t1 + 1.2, (50, 40), '+1 MONSTER'))
            t = d.pas(bb, t1 + 0.4, rec(d, c, t1 + 1.4), 0.9); d.mv('m0', t1 + 0.4, t1 + 1.4, (36, 50))
        else: t = d.pas(bb, t, rec(d, c, t + 1.2), 1.0)
        t += 0.4
wander(d, 'm1', 0, 17.9, (58, 44, 70, 56), 7700, 1.4)
fp = [(0, 'Paren på var sin sida om mittzonen', 'Rymdmonstren i zonen.'),
      (1.6, 'Lyckad passning: astronauterna får en poäng', ''),
      (ex[0]['t0'] - 0.4, 'Uppsnappning: monstren får en poäng', ''),
      (ex[0]['t1'], 'Rotera efter en tidsperiod', 'Variant: passa till vem som helst på andra sidan.')]
finish(d, 'ff05', 'space-invaders', ['Space', 'Invaders'], 'En mittzon och två linjer · Par med en boll',
       fp, 'PASSNINGSÖVNING', [('zone', 6, 38, 94, 62, (230, 120, 110), 'MITTZON'), ('line', [(6, 22), (94, 22)]), ('line', [(6, 78), (94, 78)])], ex)

# ============ ff06 Portmål i par ============
d = Drill()
GT = [(30, 30), (70, 30), (30, 70), (70, 70), (50, 50)]
PR = [((14, 20), (26, 14)), ((86, 82), (74, 88))]
for k, (a, c) in enumerate(PR): d.p(f'a{k}', '', B, a); d.p(f'c{k}', '', B, c)
team(d, 'f', R, [(50, 34), (50, 66)], ['F', 'F'])
wander(d, 'f0', 0, 17.9, (40, 26, 60, 40), 7800, 1.6); wander(d, 'f1', 0, 17.9, (40, 60, 60, 74), 7801, 1.6)
ROUTE = {0: [0, 2, 4], 1: [3, 1, 0]}; ex = []
for k in range(2):
    bb = d.newball(rec(d, f'a{k}', 0)); t = 0.4 + 1.0 * k; h, o = f'a{k}', f'c{k}'
    for gi in ROUTE[k]:
        gx, gy = GT[gi]
        d.mv(o, t, t + 1.4, (gx + 8, gy - 8)); t = d.pas(bb, t + 0.2, rec(d, o, t + 1.4)) + 0.2                     # passa
        t2 = d.path(o, t, [(gx - 6, gy + 6)], 1.2); d.carry(bb, o, t, t2); t = t2 + 0.2                               # driv genom en fri port
        if k == 0: ex.append(lab(t2 - 0.4, t2 + 0.8, (gx, gy - 10), '+1'))
        d.mv(h, t - 1.6, t, (gx - 12, gy + 4)); h, o = o, h
fp = [(0, 'Paren passar', 'Och driver genom en fri port.'),
      (2.4, 'En poäng per port', 'På 30 sekunder.'),
      (6.0, 'Försvararna nollställer räkningen', 'Bara genom att röra bollen.'),
      (10.0, 'Inte samma par två gånger i rad', '')]
finish(d, 'ff06', 'portmal-i-par', ['Portmål', 'I par'], 'Portar ca 1 m · Par med en boll · Två försvarare',
       fp, 'PASSNINGSÖVNING', [('box', 6, 6, 94, 94)] + [('cone', x + dx, y + dx) for x, y in GT for dx in (-3, 3)], ex)

# ============ ff07 Svansduellen 1 mot 1 ============
d = Drill()
PR = [(26, 30), (74, 30), (26, 70), (74, 70)]
for k, (x, y) in enumerate(PR): d.p(f'a{k}', '', B, (x - 4, y)); d.p(f'c{k}', '', ORA, (x + 6, y))
balls = [d.newball(rec(d, f'a{k}', 0)) for k in range(4)]; steal = {}
for k, (x, y) in enumerate(PR):
    wander(d, f'a{k}', 0, 7.0, (x - 12, y - 8, x + 4, y + 8), 7900 + k, 1.4); d.carry(balls[k], f'a{k}', 0, 7.0)
    tr = d.pl[f'a{k}']['tr']; d.pl[f'c{k}']['tr'] = [(0, (x + 6, y))] + [(t + 0.5, (px + 6, py + 2)) for t, (px, py) in tr if t > 0]
    if k in (1, 2): steal[k] = 6.4
for k, (x, y) in enumerate(PR):                                                                          # vinnaren vänster, förloraren höger
    win_ = f'c{k}' if k in steal else f'a{k}'; lose = f'a{k}' if k in steal else f'c{k}'
    l = PR[(k - 1) % 4]; r_ = PR[(k + 1) % 4]
    d.mv(win_, 7.4, 9.4, (l[0] + 8, l[1] - 6)); d.mv(lose, 7.4, 9.4, (r_[0] - 8, r_[1] + 6))
    hide(d, balls[k], 7.2)
fp = [(0, 'Skydda din svans', 'Partnern försöker ta den.'),
      (3.0, 'Kroppen mellan svansen och motståndaren', ''),
      (6.4, 'Svansen tagen', ''),
      (7.4, 'Vinnaren åt vänster, förloraren åt höger', 'Börja utan boll.')]
finish(d, 'ff07', 'svansduellen-1-mot-1', ['Svansduellen', '1 mot 1'], 'Par · Alla med en väst som svans',
       fp, 'DUELL', [], [lab(6.4, 7.6, (x, y - 12), 'TAGEN') for k, (x, y) in enumerate(PR) if k in (1, 2)])
f = factor(fp)
for i, pid in enumerate(d.order):
    k = int(pid[1]); lost = (pid[0] == 'a' and k in steal); won = (pid[0] == 'c' and k in steal)
    C[-1]['players'][i]['tails'] = (lambda tt, lo=lost, wo=won, s=6.4 * f: (0 if tt >= s else 1) if lo else ((2 if tt >= s else 1) if wo else 1))

# ============ ff08 Trollbron ============
d = Drill(); d.p('tr', 'T', R, (50, 50))
XS = [16, 30, 44, 58, 72, 86]
for k, x in enumerate(XS): d.p(f'p{k}', '', B, (x, 88))
balls = [d.newball(rec(d, f'p{k}', 0)) for k in range(6)]
for k, x in enumerate(XS):
    if k == 2: continue
    d.mv(f'p{k}', 0.8 + 0.1 * k, 4.6 + 0.1 * k, (x + (4 if k % 2 else -4), 12)); d.carry(balls[k], f'p{k}', 0, 4.8 + 0.1 * k)
d.mv('p2', 0.8, 2.6, (42, 54)); d.carry(balls[2], 'p2', 0, 2.6); d.mv('tr', 0.8, 2.6, (46, 50))
tl = d.pas(balls[2], 2.8, rec(d, 'tr', 3.0), 0.3)                                                            # tappar bollen
d.mv('p2', tl, tl + 1.2, (50, 50)); d.mv('tr', tl, 4.8, (44, 12)); d.carry(balls[2], 'tr', tl, 4.8)   # byter plats med trollet
for k, x in enumerate(XS):
    if k == 2: continue
    d.mv(f'p{k}', 6.6 + 0.1 * k, 10.4 + 0.1 * k, (x, 88)); d.carry(balls[k], f'p{k}', 4.8, 10.6 + 0.1 * k)
d.mv('tr', 6.6, 10.6, (42, 88)); d.carry(balls[2], 'tr', 4.8, 10.6); wander(d, 'p2', tl + 1.2, 17.9, (42, 44, 58, 56), 7810, 1.4)
fp = [(0, 'Signal – alla tar sig över med boll', 'Trollet i mitten.'),
      (tl - 0.4, 'Tappar du bollen byter du plats med trollet', ''),
      (6.6, 'Nästa signal – tillbaka', ''),
      (11.0, 'Svårare: fler troll eller mindre yta', '')]
finish(d, 'ff08', 'trollbron', ['Troll-', 'bron'], 'Yta mellan två linjer · Ett troll i mitten',
       fp, 'LEK', [('line', [(6, 92), (94, 92)]), ('line', [(6, 8), (94, 8)]), ('zone', 6, 40, 94, 60, (200, 220, 200), 'BRON')])
f = factor(fp); ids = {k: i for i, k in enumerate(d.order)}
swap_color(ids['p2'], (tl + 0.4) * f, B, R); swap_color(ids['tr'], (tl + 0.4) * f, R, B)

# ============ ff09 1 mot 1 från två håll ============
d = Drill()
team(d, 'b', B, [(40, 92), (46, 96), (34, 96)], ['', '', '']); team(d, 'r', R, [(60, 8), (54, 4), (66, 4)], ['', '', ''])
b = d.newball(rec(d, 'b0', 0))
d.mv('r0', 0.4, 2.4, (54, 40)); t = drive(d, b, 'b0', 0.4, (46, 56), 14)
d.mv('b0', t, t + 0.6, (56, 46)); d.carry(b, 'b0', t, t + 0.6); d.mv('r0', t, t + 0.6, (50, 44)); t += 0.6          # förbi
t = drive(d, b, 'b0', t, (56, 16), 18); tg = d.pas(b, t + 0.1, (50, 7), 0.5); hide(d, b, tg + 0.3)              # mål vid motståndarnas grupp
d.mv('b0', tg, tg + 2.6, (30, 98)); d.mv('r0', tg, tg + 2.4, (70, 4))
b2 = d.newball((200, 200)); show(d, b2, tg + 0.8, rec(d, 'r1', tg + 0.8))
d.mv('b1', tg + 1.0, tg + 2.6, (46, 60)); t = drive(d, b2, 'r1', tg + 1.0, (52, 46), 14)
tw = win(d, b2, 'b1', 'r1', t + 0.2, 0.4); t = drive(d, b2, 'b1', tw, (48, 84), 18); tg2 = d.pas(b2, t + 0.1, (50, 93), 0.5)   # försvararen vinner – mål åt andra hållet
fp = [(0, 'Grupperna startar på motsatta sidor', 'Grupper om 3–4 i två färger.'),
      (tg - 1.4, 'Förbi – mål i småmålet', 'Vid motståndarnas grupp.'),
      (tw - 0.2, 'Försvararen vinner', 'Och gör mål åt andra hållet.'),
      (tg2, 'Fler planer vid fler än tolv spelare', '')]
finish(d, 'ff09', '1-mot-1-fran-tva-hall', ['1 mot 1', 'Från två håll'], 'Små planer med småmål · Grupper om 3–4',
       fp, 'DUELL', [('box', 26, 6, 74, 94), ('smallgoal', 50, 6), ('smallgoal', 50, 94)])

# ============ ff10 Målzonsspelet ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96))
BP = [(30, 66), (70, 64), (44, 48), (58, 34)]; RP = [(34, 36), (66, 34), (52, 54), (44, 24)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b2'], 0.3); d.mv('b3', t - 1.0, t + 0.6, (52, 20)); t = d.pas(b, t + 0.2, rec(d, 'b3', t + 1.0))   # in i målzonen
tg = shoot(d, b, t + 0.05, (46, 1)); hide(d, b, tg + 0.3)                                                    # fritt skott på första touchen
b2 = d.newball((200, 200)); show(d, b2, tg + 1.0, rec(d, 'mvb', tg + 1.0))
t = d.pas(b2, tg + 1.2, rec(d, 'b1', tg + 2.2), 1.0); t = drive(d, b2, 'b1', t, (80, 30), 18); tg2 = d.pas(b2, t + 0.1, (84, 6), 0.6); hide(d, b2, tg2 + 0.3)   # nu de små målen
fp = [(0, 'Två jämna lag', 'Två stora mål och två små.'),
      (tg - 1.2, 'In i målzonen: fritt skott', 'Med första touchen därinne.'),
      (tg - 0.2, 'Mål i det stora målet', ''),
      (tg + 1.2, 'Nu skjuter laget i de små målen', '')]
finish(d, 'ff10', 'malzonsspelet', ['Målzons-', 'spelet'], 'Fyra mål: två fullstora och två små · Målzon',
       fp, 'SMÅLAGSSPEL', [('zone', 30, 4, 70, 24, (240, 210, 90), 'MÅLZON'), ('zone', 30, 76, 70, 96, (240, 210, 90), 'MÅLZON'), ('smallgoal', 84, 4), ('smallgoal', 16, 96)])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ ff11 Passa och spring till avslut ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
team(d, 'a', B, [(34, 60), (30, 66)], ['A', 'A']); team(d, 'b', B, [(66, 50), (70, 56)], ['B', 'B'])
balls = [d.newball(rec(d, 'a0', 0)), d.newball(rec(d, 'b1', 0))]
t = d.pas(balls[0], 0.4, rec(d, 'b0', 1.2)); d.mv('a0', 0.6, 2.4, (42, 26))                                   # A passar och springer
t = d.pas(balls[0], t + 0.2, rec(d, 'a0', t + 1.2), 1.0); tg = shoot(d, balls[0], t + 0.05, (44, 1)); hide(d, balls[0], tg + 0.3)   # B spelar in i ytan
d.mv('a0', tg + 0.2, tg + 2.4, (74, 62)); d.mv('b0', tg + 0.2, tg + 2.4, (26, 72))                             # byt roller
t0 = tg + 1.0; t = d.pas(balls[1], t0, rec(d, 'a1', t0 + 1.0))                                                  # variant 2: B passar till A
t = drive(d, balls[1], 'a1', t, (44, 20), 16); tg2 = shoot(d, balls[1], t + 0.1, (54, 1))
fp = [(0, 'A passar till B och springer mot mål', ''),
      (1.6, 'B spelar in i ytan', 'A avslutar.'),
      (t0, 'Variant 2: B passar – A driver och avslutar', 'Byt roller varje gång.'),
      (tg2, 'Svårare: bara svagare foten', '')]
finish(d, 'ff11', 'passa-och-spring-till-avslut', ['Passa och spring', 'till avslut'], 'Två grupper vid ett mål · Målvakt',
       fp, 'AVSLUT', [])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ ff12 Ta emot i fredad zon ============
d = Drill()
TZ = [(30, 30), (70, 30), (30, 70), (70, 70)]
BP = [(24, 50), (60, 20), (76, 52), (44, 80)]; RP = [(40, 40), (58, 48), (40, 62), (62, 66)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
for k in range(4): wander(d, f'r{k}', 0, 17.9, boxes([RP[k]], 4)[0], 7900 + k, 1.6)
b = d.newball(rec(d, 'b0', 0))
d.mv('b1', 0.4, 1.6, (70, 30)); t = d.pas(b, 0.6, rec(d, 'b1', 1.6), 1.0)                                      # ta emot i zonen
d.mv('b1', t, t + 0.6, (76, 22)); d.carry(b, 'b1', t, t + 0.6); tp = t + 0.6                                  # första touchen ut
t = drive(d, b, 'b1', tp, (78, 12), 14); tg = d.pas(b, t + 0.1, (70, 4), 0.5); hide(d, b, tg + 0.3)           # anfall målen: extra poäng
fp = [(0, 'Små triangelzoner – ingen tacklas där', ''),
      (1.4, 'Ta emot i en zon', ''),
      (tp - 0.3, 'Första touchen ut ur zonen: poäng', ''),
      (tg - 0.4, 'Anfall målen för en extrapoäng', '')]
finish(d, 'ff12', 'ta-emot-i-fredad-zon', ['Ta emot i', 'fredad zon'], 'Liten yta · Små triangelzoner och småmål',
       fp, 'SMÅLAGSSPEL', [('box', 8, 4, 92, 96), ('smallgoal', 30, 4), ('smallgoal', 70, 4), ('smallgoal', 30, 96), ('smallgoal', 70, 96)]
       + [('cone', x + dx, y + dy) for x, y in TZ for dx, dy in ((0, -5), (-5, 4), (5, 4))], [lab(tp, tp + 1.4, (84, 30), '+1'), lab(tg, tg + 1.4, (70, 14), '+1')])

# ============ ff13 Genom mittrutan ============
d = Drill()
OUT = [(50, 10), (90, 50), (50, 90), (10, 50)]
for k, ps in enumerate(OUT): d.p(f'o{k}', '', ORA, ps)
d.p('i0', '', B, (40, 34))
cnt = []; bb = d.newball(rec(d, 'i0', 0)); t = 0.4; inn = 'i0'
for o in [0, 1, 2, 3, 0, 1]:
    op = [p for p in d.order if p.startswith('o') or p.startswith('i')]
    target = None
    for pid in d.order:
        if pid == inn: continue
        px, py = at(d.pl[pid]['tr'], t)
        if ((px - OUT[o][0]) ** 2 + (py - OUT[o][1]) ** 2) ** .5 < 4: target = pid
    ox, oy = OUT[o]
    t1 = d.pas(bb, t, rec(d, target, t + 1.2)); d.mv(inn, t1 - 0.6, t1 + 1.2, (ox, oy))                       # byter plats
    d.mv(target, t1 - 0.4, t1, (ox + (50 - ox) * 0.1, oy + (50 - oy) * 0.1))
    ix, iy = 50 + (ox - 50) * 0.12, 50 + (oy - 50) * 0.12; ex_, ey_ = 50 - (oy - 50) * 0.3, 50 + (ox - 50) * 0.3
    t2 = d.path(target, t1, [(ix, iy), (50, 50), (ex_, ey_)], 1.2); d.carry(bb, target, t1, t2)                # genom mittkvadraten
    cnt.append(t2); inn = target; t = t2 + 0.1
fp = [(0, 'Innespelarna passar till en ytterspelare', 'Och byter plats.'),
      (1.6, 'Genom mittkvadraten', 'In på en sida, ut på en annan.'),
      (cnt[1], 'Hitta nästa', ''),
      (cnt[2], 'Flest passningar på en minut', 'Lägg till en försvarare för press.')]
finish(d, 'ff13', 'genom-mittrutan', ['Genom', 'mittrutan'], 'Yta med en liten kvadrat i mitten',
       fp, 'PASSNINGSÖVNING', [('box', 4, 4, 96, 96), ('box', 42, 42, 58, 58)], counter(cnt, pos=(84, 12), last=None))

# ============ ff14 Skjut ner bollarna ============
d = Drill()
KON = [(26, 8), (42, 8), (58, 8), (74, 8)]
team(d, 'b', B, [(36, 34), (64, 30)]); team(d, 'r', R, [(40, 20), (60, 18)])
target = [d.newball((x, y - 2)) for x, y in KON]
b = d.newball(rec(d, 'b0', 0)); ex = []
t = d.pas(b, 0.4, rec(d, 'b1', 1.2)); t1 = d.pas(b, t + 0.2, (KON[2][0], KON[2][1] + 1), 0.7)                  # träffar bollen på konen
d.pas(target[2], t1, (60, -4), 0.6); hide(d, target[2], t1 + 0.6); ex.append(lab(t1, t1 + 1.2, (58, 16), 'NERE'))
t2 = d.pas(b, t1, rec(d, 'b0', t1 + 1.2), 0.9); t3 = d.pas(b, t2 + 0.2, (KON[0][0], KON[0][1] + 1), 0.7)
d.pas(target[0], t3, (24, -4), 0.6); hide(d, target[0], t3 + 0.6); ex.append(lab(t3, t3 + 1.2, (26, 16), 'NERE'))
d.mv('b0', t3 - 0.6, t3 + 0.1, (25, 11)); d.carry(b, 'b0', t3 + 0.1, t3 + 1.2); d.mv('r0', t3 - 1.0, t3 + 0.6, (30, 18)); tw = win(d, b, 'r0', 'b0', t3 + 1.4, 0.5)
t = drive(d, b, 'r0', tw, (44, 84), 22); tg = d.pas(b, t + 0.1, (50, 94), 0.5); hide(d, b, tg + 0.3)          # andra laget mot det lilla målet
fp = [(0, 'Ena laget slår ner bollarna från konerna', '2 mot 2 eller 3 mot 3.'),
      (t1 - 0.6, 'Träff – bollen nere', ''),
      (tw - 0.2, 'Andra laget anfaller det lilla målet', ''),
      (tg + 0.2, 'Alla bollar nere – byt sida och uppgift', '')]
finish(d, 'ff14', 'skjut-ner-bollarna', ['Skjut ner', 'bollarna'], 'Bollar på koner i ena änden · Litet mål i den andra',
       fp, 'SMÅLAGSSPEL', [('cone', x, y + 2) for x, y in KON] + [('smallgoal', 50, 94), ('box', 14, 4, 86, 96)], ex)

if __name__ == '__main__': render(C, sys.argv)
