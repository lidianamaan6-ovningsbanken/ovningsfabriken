# Externa övningar, omgång 29 (tolv st). Regel: först d.mv, sedan d.carry; först mottagarens rörelse, sedan passningen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e9', __file__.replace('render_extern29.py', 'render_extern9.py'))
e9 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e9); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e9.finish, e9.rec, e9.chain, e9.wander, e9.counter, e9.arrivals
lab, hide, show, team, boxes, drive, shoot = e9.lab, e9.hide, e9.show, e9.team, e9.boxes, e9.drive, e9.shoot
factor, swap_color, stand, countdown, countup, win = e9.factor, e9.swap_color, e9.stand, e9.countdown, e9.countup, e9.win
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'

# ============ ff15 Flytta bollarna – passningsstafett ============
d = Drill()
for tm, x, col in (('b', 30, B), ('r', 70, R)):
    for k, y in enumerate((82, 62, 42, 22)): d.p(f'{tm}{k}', str(k + 1), col, (x + (-6 if k % 2 else 6), y))
for tm, x, col in (('b', 30, B), ('r', 70, R)):
    pile = [d.newball((x + dx, 94)) for dx in (-4, 0, 4)]; t = 0.4 + (0.3 if tm == 'r' else 0)
    for n, bl in enumerate(pile):
        d.mv(f'{tm}0', t, t + 0.6, (x + (-4, 0, 4)[n], 90)); d.carry(bl, f'{tm}0', t + 0.6, t + 0.8)
        tt = t + 0.9
        for k in (1, 2, 3): tt = d.pas(bl, tt, rec(d, f'{tm}{k}', tt + 0.8)) + 0.15
        tg = d.pas(bl, tt, (x, 5), 0.6); hide(d, bl, tg + 0.3)                                                    # i mål B
        d.mv(f'{tm}0', t + 0.8, t + 1.4, (x + 6, 82)); t = t + 2.6
fp = [(0, 'Spelare 1 tar en boll vid mål A', 'Ca fyra per lag på stationer.'),
      (1.6, 'Passa via 2 och 3 till 4', ''),
      (3.6, 'Spelare 4 skickar den i mål B', ''),
      (7.0, 'Först med alla bollar till B vinner', 'Svårare: följ passningen, byt håll.')]
finish(d, 'ff15', 'flytta-bollarna-passningsstafett', ['Flytta bollarna', 'Passningsstafett'], 'Delad yta med mål A och B · Ca fyra per lag',
       fp, 'STAFETT', [('smallgoal', 30, 4), ('smallgoal', 70, 4), ('text', 30, 98, 'A'), ('text', 70, 98, 'A'), ('line', [(50, 4), (50, 96)])])

# ============ ff16 Genom sidoporten till 1 mot 1 ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
BP = [(30, 56), (70, 54), (50, 70)]; RP = [(36, 44), (62, 46), (50, 60)]; team(d, 'b', B, BP); team(d, 'r', R, RP); team(d, 'n', YEL, [(14, 70), (86, 70)], ['N', 'N'])
for k in range(3): wander(d, f'r{k}', 0, 6, boxes([RP[k]], 4)[0], 8000 + k, 1.6)
b = d.newball(rec(d, 'b2', 0))
t = chain(d, b, 0.4, ['n0', 'b0', 'b1', 'n1'], 0.3); cnt = arrivals(d, b)[:4]
d.mv('b1', t - 1.0, t + 0.4, (78, 40)); t = d.pas(b, t + 0.2, rec(d, 'b1', t + 1.0))
t = drive(d, b, 'b1', t, (84, 30), 14); d.mv('b1', t, t + 1.2, (60, 18)); d.carry(b, 'b1', t, t + 1.2); t += 1.2     # genom sidoporten
tg = shoot(d, b, t + 0.1, (46, 1))                                                                             # 1 mot 1 mot målvakten
fp = [(0, 'Två lag, två neutrala och en målvakt', ''),
      (cnt[-1] - 0.4, 'Fyra passningar', 'Sedan får laget dribbla genom en sidoport.'),
      (tg - 1.4, '1 mot 1 mot målvakten', 'I frizonen.'),
      (tg - 0.2, 'Mål på första touchen ger fler poäng', 'Vinner försvaret bollen: avslut i öppna målet.')]
finish(d, 'ff16', 'genom-sidoporten-till-1-mot-1', ['Genom sidoporten', 'till 1 mot 1'], 'Spelzon · Frizon vid målvakten · Sidoportar · Öppet mål',
       fp, 'SPELÖVNING', [('zone', 20, 4, 80, 26, (240, 210, 90), 'FRIZON'), ('cone', 82, 26), ('cone', 90, 26), ('cone', 10, 26), ('cone', 18, 26), ('smallgoal', 50, 96)],
       counter(cnt, pos=(50, 90), last=None))
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ ff17 Överlapp och avslut ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
d.p('a', 'A', B, (30, 70)); d.p('c', 'C', B, (70, 46)); d.p('bb', 'B', B, (40, 76)); d.p('q', '', B, (26, 80))
ball = d.newball(rec(d, 'a', 0))
t = d.pas(ball, 0.4, rec(d, 'c', 1.4)); d.path('bb', 0.4, [(60, 60), (80, 44), (72, 26)], 1.4)               # B överlappar runt C
t = d.pas(ball, t + 0.6, rec(d, 'bb', t + 1.6)); d.carry(ball, 'bb', t, t + 0.4)                                # C lägger av
tg = shoot(d, ball, t + 0.45, (54, 1))
d.mv('a', tg - 1.0, tg + 1.0, (70, 46)); d.mv('c', tg - 0.6, tg + 1.4, (40, 76)); d.mv('bb', tg + 0.2, tg + 2.4, (26, 86)); d.mv('q', tg, tg + 1.0, (30, 70))   # rotera
fp = [(0, 'A passar till C', 'Medan B överlappar runt C.'),
      (2.0, 'C lägger av till B', ''),
      (tg - 0.6, 'Ett touch in i ytan – skott', 'Eller skjut direkt.'),
      (tg + 0.4, 'Rotera A till C till B', '')]
finish(d, 'ff17', 'overlapp-och-avslut', ['Överlapp och', 'avslut'], 'Två grupper · En målvakt',
       fp, 'AVSLUT', [])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ ff18 1 mot 1 i tredjedelar ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96))
ZX = [(6, 36), (36, 64), (64, 94)]
for z, (x1, x2) in enumerate(ZX): d.p(f'b{z}', '', B, ((x1 + x2) / 2 - 4, 60)); d.p(f'r{z}', '', R, ((x1 + x2) / 2 + 4, 40))
b = d.newball(rec(d, 'b1', 0))
for z, (x1, x2) in enumerate(ZX):
    if z != 1: wander(d, f'b{z}', 0, 17.9, (x1 + 4, 20, x2 - 4, 80), 8100 + z, 1.6); wander(d, f'r{z}', 0, 17.9, (x1 + 4, 20, x2 - 4, 80), 8110 + z, 1.6)
t = drive(d, b, 'b1', 0.4, (50, 46), 14); d.mv('r1', 0.4, t, (52, 40))
t = d.pas(b, t + 0.1, rec(d, 'b2', t + 0.9)); d.mv('r1', t, t + 1.4, (50, 30))
t = drive(d, b, 'b2', t, (80, 26), 16); t = d.pas(b, t + 0.1, rec(d, 'b1', t + 1.0)); d.mv('b1', t - 1.4, t, (46, 22))
tg = shoot(d, b, t + 0.05, (46, 1))
fp = [(0, 'Varje spelare har en tredjedel', 'Plan delad i tre zoner på längden.'),
      (1.4, '1 mot 1 i din zon', 'Rör dig upp och ner.'),
      (tg - 1.4, 'Spela till en kompis i en annan zon', ''),
      (tg, 'Variant: byt zon', 'Byt då plats med den som står där.')]
finish(d, 'ff18', '1-mot-1-i-tredjedelar', ['1 mot 1', 'I tredjedelar'], 'Stor plan delad i tre zoner på längden',
       fp, 'SMÅLAGSSPEL', [('line', [(36, 4), (36, 96)]), ('line', [(64, 4), (64, 96)])])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ ff19 Två anfallare följer upp ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96))
BD = [(24, 70), (44, 76), (60, 74), (76, 68)]; BA = [(40, 30), (62, 28)]; RD = [(26, 30), (44, 24), (60, 26), (76, 32)]; RA = [(40, 68), (60, 70)]
team(d, 'bd', B, BD); team(d, 'ba', B, BA, ['A', 'A']); team(d, 'rd', R, RD); team(d, 'ra', R, RA, ['A', 'A'])
b = d.newball(rec(d, 'bd1', 0))
t = chain(d, b, 0.4, ['bd2'], 0.3); d.mv('ba1', t - 0.8, t + 0.6, (60, 38)); t = d.pas(b, t + 0.2, rec(d, 'ba1', t + 1.4), 1.2)
d.mv('ba0', t - 1.0, t + 0.4, (44, 18)); t = d.pas(b, t + 0.1, rec(d, 'ba0', t + 0.8)); tg = shoot(d, b, t + 0.05, (46, 1))   # följer upp, första touch
fp = [(0, 'Fyra i försvarshalvan, två i anfallshalvan', 'Två lag om sex.'),
      (1.8, 'Ingen får lämna sin halva', ''),
      (tg - 1.0, 'Anfallarna följer upp', ''),
      (tg - 0.2, 'Mål på första touchen ger fler poäng', 'Övning: 2 mot 1 och målvakt.')]
finish(d, 'ff19', 'tva-anfallare-foljer-upp', ['Två anfallare', 'följer upp'], 'Två lag om sex',
       fp, 'SMÅLAGSSPEL', [('line', [(4, 50), (96, 50)])])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ sx01 Cirkelrondo 10 mot 3 ============
d = Drill()
RING = [ring_pos(50, 50, 38, i, 8) for i in range(8)]
for k, ps in enumerate(RING): d.p(f'o{k}', '', B, ps)
team(d, 'i', B, [(44, 44), (56, 56)], ['', '']); team(d, 'f', R, [(50, 36), (38, 56), (62, 44)], ['', '', ''])
team(d, 'w', R, [(94, 88), (88, 94), (96, 94)], ['', '', ''])
for k in range(2): wander(d, f'i{k}', 0, 17.9, boxes([[(44, 44), (56, 56)][k]], 5)[0], 8200 + k, 1.6)
b = d.newball(rec(d, 'o0', 0))
t = chain(d, b, 0.4, ['i0', 'o3', 'o5', 'i1', 'o7'], 0.3)
d.mv('f0', 0.6, t - 0.6, (48, 40)); d.mv('f1', 0.6, t - 0.6, (40, 52)); d.mv('f2', 0.6, t - 0.6, (60, 46))     # press, täckning, balans
tw = win(d, b, 'f2', 'o7', t + 0.4, 0.8)
for k, ps in enumerate([(90, 90), (84, 96), (96, 84)]): d.mv(f'f{k}', tw + 0.3, tw + 2.4, ps)                     # tre nya in
for k, ps in enumerate([(50, 36), (38, 56), (62, 44)]): d.mv(f'w{k}', tw + 0.3, tw + 2.6, ps)
b2 = d.newball((200, 200)); show(d, b2, tw + 2.2, rec(d, 'o2', tw + 2.2)); hide(d, b, tw + 0.6)
t = chain(d, b2, tw + 2.4, ['o4', 'i0'], 0.3)
fp = [(0, 'Tio anfallare mot tre försvarare', 'Åtta runt, två i mitten.'),
      (1.6, 'Press, täckning och balans', 'Tre försvarare i samarbete.'),
      (tw - 0.2, 'Försvararna vinner bollen', ''),
      (tw + 0.6, 'Tre nya försvarare går in', '')]
finish(d, 'sx01', 'cirkelrondo-10-mot-3', ['Cirkelrondo 10 mot 3', 'Press, täckning, balans'], 'Cirkel ca 18 × 18 m',
       fp, 'RONDO', [('circle', 50, 50, 43)], [lab(1.8, tw - 0.2, (50, 6), 'PRESS – TÄCKNING – BALANS')])

# ============ sx02 Omställningsrondo 6 mot 4 ============
d = Drill()
GL = [(10, 8), (90, 8), (10, 92), (90, 92)]
BP = [(26, 30), (74, 30), (20, 60), (80, 60), (40, 80), (60, 80)]; RP = [(42, 40), (58, 42), (42, 62), (58, 64)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
for k in range(6): wander(d, f'b{k}', 0, 17.9, boxes([BP[k]], 5)[0], 8300 + k, 1.6)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b1', 'b3', 'b5', 'b4'], 0.25); cnt = arrivals(d, b)[:4]
tw = win(d, b, 'r2', 'b4', t + 0.3, 0.8); t = drive(d, b, 'r2', tw, (16, 86), 20); tg = d.pas(b, t + 0.1, (10, 92), 0.4); hide(d, b, tg + 0.3)
for k in (0, 1, 3): wander(d, f'r{k}', 0, 17.9, boxes([RP[k]], 4)[0], 8310 + k, 1.6)
fp = [(0, 'Sex håller bollen mot fyra', 'Ett minimål i varje hörn.'),
      (cnt[1], 'Passningar i följd ger poäng', ''),
      (tw - 0.2, 'Försvararna vinner bollen', ''),
      (tg - 0.6, 'Mål i valfritt minimål', 'Snabb omställning.')]
finish(d, 'sx02', 'omstallningsrondo-6-mot-4-med-fyra-minimal', ['Omställningsrondo 6 mot 4', 'Med fyra minimål'], 'Yta ca 18 × 32 m · Ett minimål i varje hörn',
       fp, 'RONDO', [('box', 6, 4, 94, 96)] + [('smallgoal',) + g for g in GL], counter(cnt, pos=(50, 50), last=None) + [lab(tg, tg + 1.4, (18, 82), 'MÅL')])

# ============ sx03 Bakre fotens rondo ============
d = Drill()
SQ = [(50, 22), (78, 50), (50, 78), (22, 50)]
for k, ps in enumerate(SQ): d.p(f'p{k}', '', B, ps)
team(d, 'f', R, [(46, 48), (56, 54)], ['', ''])
b = d.newball(rec(d, 'p0', 0)); t = 0.4; h = 0; marks = []
for rep, side in enumerate([1, 1, -1, 1, -1, -1, 1, 1, -1, 1]):
    nk = (h + side) % 4                                                                                        # vänster eller höger – aldrig rakt över
    d.mv('f0', t, t + 0.7, ((SQ[h][0] + SQ[nk][0]) / 2 * 0.6 + 50 * 0.4, (SQ[h][1] + SQ[nk][1]) / 2 * 0.6 + 50 * 0.4))
    t = d.pas(b, t + 0.15, rec(d, f'p{nk}', t + 0.85)); marks.append(t); h = nk
wander(d, 'f1', 0, 17.9, (44, 44, 56, 56), 8400, 1.4)
fp = [(0, 'Fyra mot två', 'Ruta ca 7 × 11 m.'),
      (1.4, 'Till vänster eller höger', 'Ingen passning rakt över rutan.'),
      (marks[3], 'Ta emot på bakre foten', 'Öppen kropp mot nästa.'),
      (marks[6], 'Variant: 4 mot 1 eller 6 mot 2', '')]
finish(d, 'sx03', 'bakre-fotens-rondo', ['Bakre fotens rondo', 'Vänster eller höger'], 'Ruta ca 7 × 11 m · 4 mot 2',
       fp, 'RONDO', [('box', 18, 18, 82, 82), ('line', [(22, 50), (78, 50)])])

# ============ sx04 5 mot 4 – stort mål mot två minimål ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
AP = [(24, 50), (40, 56), (60, 56), (76, 50), (50, 40)]; DP = [(34, 28), (50, 22), (66, 28), (50, 36)]
team(d, 'a', B, AP); team(d, 'f', R, DP); d.p('n', 'N', YEL, (50, 74))
b = d.newball(rec(d, 'n', 0))
t = d.pas(b, 0.4, rec(d, 'a1', 1.2)); t = chain(d, b, t, ['a4', 'a3'], 0.3)
d.mv('a3', t, t + 0.8, (70, 26)); d.carry(b, 'a3', t, t + 0.8); t += 0.8; tg = shoot(d, b, t + 0.1, (54, 1)); hide(d, b, tg + 0.3)
b2 = d.newball((200, 200)); show(d, b2, tg + 0.6, rec(d, 'n', tg + 0.6))
t = d.pas(b2, tg + 0.8, rec(d, 'a0', tg + 1.8)); tw = win(d, b2, 'f0', 'a0', t + 0.4, 0.8)
t = drive(d, b2, 'f0', tw, (28, 86), 22); tg2 = d.pas(b2, t + 0.1, (30, 95), 0.4)                            # kontrar mot minimålet
fp = [(0, 'Fem plus en neutral mot fyra', ''),
      (tg - 1.0, 'Mål i det stora målet', ''),
      (tw - 0.2, 'Försvararna vinner bollen', ''),
      (tg2 - 1.0, 'Snabb kontring mot minimålen', 'Eller spela till den neutrala.')]
finish(d, 'sx04', '5-mot-4-stort-mal-mot-tva-minimal', ['5 mot 4', 'Stort mål mot två minimål'], 'Yta ca 40 × 37 m · Ett stort mål och två minimål',
       fp, 'SPELÖVNING', [('smallgoal', 30, 96), ('smallgoal', 70, 96)])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ sx05 Slottsspelet ============
d = Drill()
PB = [(20 + 15 * i, 6) for i in range(5)]; PR_ = [(20 + 15 * i, 94) for i in range(5)]
BP = [(30, 66), (70, 64), (44, 50), (58, 80)]; RP = [(34, 34), (66, 36), (52, 54), (42, 20)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
for k in range(4): wander(d, f'r{k}', 0, 17.9, boxes([RP[k]], 4)[0], 8500 + k, 1.6)
b1 = d.newball(rec(d, 'b0', 0)); b2 = d.newball(rec(d, 'r2', 0)); ex = []
t = d.pas(b1, 0.4, rec(d, 'b2', 1.2)); t = drive(d, b1, 'b2', t, (50, 22), 16); th = d.pas(b1, t + 0.1, (50, 7), 0.5)   # välter en käpp
ex.append(lab(th, th + 1.6, (50, 14), 'VÄLT'))
d.mv('b2', th, th + 0.6, (50, 8)); d.mv('b2', th + 0.6, th + 4.4, (52, 92)); d.carry(b1, 'b2', th + 0.6, th + 4.4)   # för käppen till slottet
t2 = d.pas(b2, 1.0, rec(d, 'r0', 1.8)); t2 = drive(d, b2, 'r0', t2, (64, 80), 16); d.mv('b3', t2 - 1.4, t2, (60, 84))
tw = win(d, b2, 'b3', 'r0', t2 + 0.2, 0.3)
fp = [(0, 'Två bollar i spel samtidigt', 'Fem käppar på varje lags bakre linje.'),
      (th - 0.6, 'Välta motståndarnas käpp', ''),
      (th + 0.8, 'För käppen till det egna slottet', 'Nu är den lagets egen.'),
      (th + 3.0, 'Ändra ytan och antalet bollar', '')]
finish(d, 'sx05', 'slottsspelet', ['Slotts-', 'spelet'], 'Yta ca 32 × 46 m · Fem käppar per lag',
       fp, 'SMÅLAGSSPEL', [('box', 6, 4, 94, 96)] + [('pole',) + p for p in PB] + [('pole',) + p for p in PR_], ex)

# ============ sx06 Skydda stenen 1 mot 1 ============
d = Drill()
PR = [(30, 32), (70, 32), (30, 70), (70, 70)]
for k, (x, y) in enumerate(PR): d.p(f's{k}', '', B, (x, y)); d.p(f'a{k}', '', ORA, (x + 8, y - 4))
for k, (x, y) in enumerate(PR):
    bb = d.newball((x + 1.8, y - 1.2)); t = 0.4 + 0.2 * k
    for rep in range(6):
        ang = [(8, -4), (0, -8), (-8, -4), (-8, 4), (0, 8), (8, 4)][(rep + k) % 6]
        d.mv(f'a{k}', t, t + 1.0, (x + ang[0], y + ang[1])); d.mv(f's{k}', t + 0.2, t + 1.0, (x - ang[0] * 0.2, y - ang[1] * 0.2))   # kroppen mellan
        d.carry(bb, f's{k}', t, t + 1.0, off=(-ang[0] * 0.15, -ang[1] * 0.15)); t += 1.1
    d.mv(f's{k}', t, t + 0.8, (x + 4, y + 2)); d.mv(f'a{k}', t, t + 0.8, (x - 2, y - 2)); d.carry(bb, f'a{k}', t + 0.8, t + 1.2)   # byt roller
fp = [(0, 'Står över bollen och skyddar den', 'Par.'),
      (2.0, 'Kroppen mellan bollen och motståndaren', 'Inga händer.'),
      (5.0, 'Vänd dig efter motståndaren', ''),
      (7.0, 'Byt roller efter 20–30 sekunder', '')]
finish(d, 'sx06', 'skydda-stenen-1-mot-1', ['Skydda stenen', '1 mot 1'], 'Ruta ca 14 × 18 m · Par',
       fp, 'DUELL', [('box', 14, 14, 86, 86)])
C[-1]['_stuck'] = True

# ============ sx07 2 mot 1 i två rutor ============
d = Drill()
team(d, 'a', B, [(16, 30), (40, 70)], ['', '']); d.p('f', '', R, (28, 50)); d.p('u', 'U', B, (76, 34)); d.p('l', 'L', R, (76, 66))
b = d.newball(rec(d, 'a0', 0))
t = d.pas(b, 0.4, rec(d, 'a1', 1.2)); d.mv('f', 0.6, t, (34, 60)); t = d.pas(b, t + 0.2, rec(d, 'a0', t + 1.0)); d.mv('f', t - 0.8, t, (24, 40))
t = d.pas(b, t + 0.2, rec(d, 'u', t + 1.4), 1.2); d.carry(b, 'u', t, t + 0.3); t = d.pas(b, t + 0.35, rec(d, 'a1', t + 1.4), 1.2)   # utpassning – max två touch
d.mv('f', t - 0.8, t + 0.2, rec(d, 'a1', t + 0.2)); tw = d.pas(b, t + 0.3, rec(d, 'f', t + 0.5), 0.3)
t = d.pas(b, tw + 0.3, rec(d, 'l', tw + 1.6), 1.3); tl = t                                                   # försvararen till sin lagkamrat
fp = [(0, 'Två anfallare mot en försvarare', 'Två rutor ca 7 × 11 m.'),
      (2.4, 'Använd spelaren i andra rutan', 'Max två touch.'),
      (tw - 0.2, 'Försvararen vinner bollen', ''),
      (tl - 0.8, 'Spelar till sin lagkamrat i andra rutan', '')]
finish(d, 'sx07', '2-mot-1-i-tva-rutor', ['2 mot 1', 'I två rutor'], 'Två rutor ca 7 × 11 m',
       fp, 'RONDO', [('box', 6, 20, 50, 80), ('box', 62, 20, 92, 80)])

if __name__ == '__main__': render(C, sys.argv)
