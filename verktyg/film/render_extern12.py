# Externa övningar, omgång 12 (tolv st). Regel: först d.mv, sedan d.carry; först mottagarens rörelse, sedan passningen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e9', __file__.replace('render_extern12.py', 'render_extern9.py'))
e9 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e9); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e9.finish, e9.rec, e9.chain, e9.wander, e9.counter, e9.arrivals
lab, hide, show, team, boxes, drive, shoot = e9.lab, e9.hide, e9.show, e9.team, e9.boxes, e9.drive, e9.shoot
factor, swap_color, stand, countdown, countup, win = e9.factor, e9.swap_color, e9.stand, e9.countdown, e9.countup, e9.win
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'

# ============ sd20 Överlappning ============
d = Drill()
d.p('x1', 'X1', B, (30, 86)); d.p('x1b', 'X1', B, (30, 92)); d.p('x2', 'X2', B, (34, 56)); d.p('o1', 'O', R, (40, 34))
d.p('x3', 'X3', B, (70, 86)); d.p('x3b', 'X3', B, (70, 92)); d.p('x4', 'X2', B, (66, 56)); d.p('o2', 'O', R, (60, 34))
b1 = d.newball(rec(d, 'x1', 0)); b2 = d.newball(rec(d, 'x3', 0))
t = d.pas(b1, 0.4, rec(d, 'x2', 1.2))
d.mv('x2', t, t + 1.2, (42, 42)); d.carry(b1, 'x2', t, t + 1.2); d.mv('o1', t, t + 1.2, (42, 34))      # utmanar försvararen
d.mv('x1', t - 0.6, t + 1.6, (16, 34)); t += 1.2                                                       # överlappar
t = d.pas(b1, t + 0.2, rec(d, 'x1', t + 0.9)); to = t
d.mv('x1', t, t + 1.4, (18, 12)); d.carry(b1, 'x1', t, t + 1.4); t += 1.4                              # driver
hide(d, b1, t + 0.4); d.mv('x1', t + 0.4, t + 3.4, (76, 98)); d.mv('x2', to, to + 2.4, (34, 56))        # X1 bakom X3
d.mv('x1b', to, to + 1.0, (30, 86))
t0 = t - 0.4; t = d.pas(b2, t0, rec(d, 'x4', t0 + 0.8))
d.mv('x4', t, t + 1.2, (58, 42)); d.carry(b2, 'x4', t, t + 1.2); d.mv('o2', t, t + 1.2, (58, 34))
d.mv('x3', t - 0.6, t + 1.6, (84, 34)); t += 1.2
t = d.pas(b2, t + 0.2, rec(d, 'x3', t + 0.9)); d.mv('x3', t, t + 2.0, (82, 8)); d.carry(b2, 'x3', t, t + 2.0)
fp = [(0, 'X1 passar X2', 'X2 utmanar försvararen.'),
      (1.4, 'X1 överlappar', 'Löp utanför i full fart.'),
      (to - 0.3, 'X1 får bollen och driver', 'Efter anfallet ställer sig X1 bakom X3.'),
      (t0, 'Byt sida', 'Samma sak från andra sidan.')]
finish(d, 'sd20', 'overlappning', ['Överlappning', 'Passningsövning'], 'Yta 45 × 30 m',
       fp, 'PASSNINGSÖVNING', [('box', 6, 4, 94, 96)])

# ============ sd21 1 mot 1 med avslut ============
d = Drill(); d.p('mv1', 'MV', G, (50, 4)); d.p('mv2', 'MV', G, (50, 96))
d.p('f', 'F', R, (50, 86)); d.p('a', 'A', B, (50, 26)); d.p('f2', 'F', R, (50, 14)); d.p('a2', 'A', B, (50, 74))
b = d.newball(rec(d, 'f', 0))
t = d.pas(b, 0.4, rec(d, 'a', 1.8), 1.4); d.mv('f', 0.5, 2.6, (50, 46))                                  # passar och går in
d.mv('a', t, t + 1.0, (46, 40)); d.carry(b, 'a', t, t + 1.0); t += 1.0
d.mv('a', t, t + 1.0, (62, 58)); d.carry(b, 'a', t, t + 1.0); d.mv('f', t, t + 1.0, (52, 52)); t += 1.0    # passerar
tg = shoot(d, b, t + 0.2, (54, 99)); hide(d, b, tg + 0.4)
d.mv('a', tg, tg + 2.0, (40, 90)); d.mv('f', tg, tg + 2.0, (60, 90))
b2 = d.newball((200, 200)); show(d, b2, tg + 0.6, rec(d, 'f2', tg + 0.6))
t = d.pas(b2, tg + 0.8, rec(d, 'a2', tg + 2.2), 1.4); d.mv('f2', tg + 0.9, tg + 3.0, (50, 54))
d.mv('a2', t, t + 1.0, (54, 60)); d.carry(b2, 'a2', t, t + 1.0); t += 1.0
d.mv('a2', t, t + 1.0, (40, 40)); d.carry(b2, 'a2', t, t + 1.0); d.mv('f2', t, t + 1.0, (46, 46)); t += 1.0
tg2 = shoot(d, b2, t + 0.2, (46, 1))
fp = [(0, 'Passa till motsatt sida', 'Försvararen går in när passningen slås.'),
      (1.8, 'Anfallaren passerar', 'Och avslutar.'),
      (tg + 0.6, 'Nästa par åt andra hållet', 'Anfallaren byter uppgift efter varje anfall.'),
      (tg2 - 0.6, 'Spela tills bollen är ur spel', '')]
finish(d, 'sd21', '1-mot-1-med-avslut', ['1 mot 1', 'Med avslut'], 'Dubbla straffområden plus målgårdens bredd',
       fp, 'DUELL', [('box', 30, 2, 70, 98)])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ sd22 2 mot 2 + 1 – mål efter väggspel ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96)); d.p('j', 'J', YEL, (50, 50))
BP = [(34, 64), (66, 60)]; RP = [(40, 38), (62, 36)]; team(d, 'b', B, BP); team(d, 'r', R, RP)
wander(d, 'j', 0, 1.2, (46, 46, 54, 54), 2100, 1.2)
b = d.newball(rec(d, 'b0', 0))
t = drive(d, b, 'b0', 0.4, (40, 46), 16); d.mv('r0', 0.6, t, (42, 38))
d.mv('j', t - 0.6, t + 0.4, (52, 42)); t = d.pas(b, t + 0.1, rec(d, 'j', t + 0.6))                       # väggspel
d.mv('b0', t - 0.4, t + 0.8, (44, 26)); t = d.pas(b, t + 0.05, rec(d, 'b0', t + 0.7)); tv = t
tg = shoot(d, b, t + 0.1, (46, 1)); hide(d, b, tg + 0.4)
for k in range(2): d.mv(f'b{k}', tg, tg + 2.0, BP[k]); d.mv(f'r{k}', tg, tg + 2.0, RP[k])
d.mv('j', tg, tg + 1.6, (50, 50))
b2 = d.newball((200, 200)); show(d, b2, tg + 1.4, rec(d, 'mvr', tg + 1.4))
t = d.pas(b2, tg + 1.6, rec(d, 'r1', tg + 2.4)); t = drive(d, b2, 'r1', t, (60, 66), 16); tg2 = shoot(d, b2, t + 0.1, (56, 99))   # utan väggspel
d.mv('b1', t - 1.2, t, (62, 72))
fp = [(0, 'Två mot två plus en joker', 'Jokern spelar med laget som har bollen.'),
      (tv - 1.2, 'Väggspel med jokern', ''),
      (tg - 0.4, 'Mål efter väggspel räknas', 'Byt uppgifter och målvakt.'),
      (tg2 - 0.6, 'Mål utan väggspel räknas inte', '')]
finish(d, 'sd22', '2-mot-2-plus-1-mal-efter-vaggspel', ['2 mot 2 + 1', 'Mål efter väggspel'], 'Yta 25 × 20 m med två mål',
       fp, 'SMÅLAGSSPEL', [('box', 14, 2, 86, 98)], [lab(tg, tg + 1.6, (46, 14), 'MÅL'), lab(tg2, tg2 + 1.8, (56, 86), 'RÄKNAS INTE')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ sd23 Djupledslöpning bakom backlinjen ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
team(d, 'f', R, [(28, 44), (42, 44), (58, 44), (72, 44)]); d.p('m', 'M', B, (50, 66))
d.p('pl', 'P', WHITE, (16, 84)); d.p('pr', 'P', WHITE, (84, 84)); d.p('rl', 'L', B, (32, 56)); d.p('rr', 'L', B, (68, 56))
b1 = d.newball(rec(d, 'pl', 0)); b2 = d.newball(rec(d, 'pr', 0))
t = d.pas(b1, 0.4, rec(d, 'm', 1.4)); d.mv('m', 0.6, 1.4, (46, 70))
d.mv('rl', t - 0.6, t + 1.4, (36, 30)); t = d.pas(b1, t + 0.3, (36, 30), 0.9); tp = t                    # genom backlinjen
d.carry(b1, 'rl', t, t + 0.3); tg = shoot(d, b1, t + 0.35, (44, 1)); hide(d, b1, tg + 0.4)
d.mv('rl', tg, tg + 2.2, (32, 56)); d.mv('m', tg, tg + 1.0, (50, 66))
t = d.pas(b2, tg + 0.6, rec(d, 'm', tg + 1.6)); d.mv('m', tg + 1.0, tg + 1.6, (54, 70))
d.mv('rr', t - 0.6, t + 1.4, (64, 30)); t = d.pas(b2, t + 0.3, (64, 30), 0.9)
d.carry(b2, 'rr', t, t + 0.3); tg2 = shoot(d, b2, t + 0.35, (56, 1))
fp = [(0, 'Passning till mittfältaren', 'Backlinjen ca 20 m från mål.'),
      (tp - 1.2, 'Spela bakom backlinjen', 'Löparen är redan på väg i full fart.'),
      (tg - 0.4, 'Avslut', ''),
      (tg + 0.6, 'Starta från andra sidan', '')]
finish(d, 'sd23', 'djupledslopning-bakom-backlinjen', ['Djupledslöpning', 'Bakom backlinjen'], 'Backlinje ca 20 m från mål · Löpare och passningsläggare på båda sidor',
       fp, 'AVSLUT', [])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ sd24 Skuggspel in i spelyta 3 ============
d = Drill(); d.p('mvb', 'MV', B, (50, 96)); d.p('mvr', 'MV', R, (50, 4)); d.p('t', 'T', T_COL, (97, 50))
BF = [(34, 80), (66, 80), (22, 62), (50, 64), (78, 62), (50, 46)]; RF = [(34, 22), (66, 22), (24, 36), (50, 34), (76, 36), (50, 50)]
team(d, 'b', B, BF); team(d, 'r', R, RF)
b = d.newball(rec(d, 'mvb', 0))
t = d.pas(b, 0.4, rec(d, 'b0', 1.2)); d.mv('b2', 0.8, 2.0, (18, 50)); t = d.pas(b, t + 0.2, rec(d, 'b2', t + 1.0))
d.mv('r2', t - 0.6, t + 0.6, (24, 42))
tf = t + 0.3                                                                                              # tränaren fryser spelet
t = d.pas(b, tf + 1.8, rec(d, 'b3', tf + 2.5)); d.mv('b5', tf + 1.6, t + 0.8, (60, 30))
t = d.pas(b, t + 0.2, rec(d, 'b5', t + 0.9)); tg = shoot(d, b, t + 0.1, (54, 1))
for k in range(6): d.mv(f'b{k}', tg + 0.4, tg + 2.8, BF[k])                                             # tillbaka till 2-3-1
d.mv('r2', tg, tg + 1.6, RF[2])
fp = [(0, 'Ett lag i försvarsformation', 'Det andra spelar sig förbi och avslutar.'),
      (tf, 'Tränaren fryser spelet', 'Och ställer frågor: Var är ytan? Vem är fri?'),
      (tf + 1.8, 'Spela vidare och avsluta', ''),
      (tg + 0.4, 'Tillbaka till 2-3-1', 'Lagen byter roller.')]
finish(d, 'sd24', 'skuggspel-in-i-spelyta-3', ['Skuggspel', 'In i spelyta 3'], 'Fullstor 7 mot 7-plan · Två lag',
       fp, 'MATCHLIKT', [('line', [(4, 50), (96, 50)])], [lab(tf, tf + 1.8, (80, 44), 'FRYS!')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ sd25 Skottmatch 3 mot 1 ============
d = Drill(); d.p('mv1', 'MV', R, (50, 4)); d.p('mv2', 'MV', B, (50, 96))
AP = [(30, 66), (50, 62), (70, 66)]; team(d, 'a', B, AP); d.p('fw', 'F', B, (54, 22)); d.p('o', 'O', R, (46, 56))
b = d.newball(rec(d, 'a0', 0))
t = d.pas(b, 0.4, rec(d, 'a1', 1.0)); d.mv('o', 0.6, t, (48, 58))
tsh = shoot(d, b, t + 0.1, (46, 4)); d.mv('mv1', tsh - 0.3, tsh, (46, 5))                                  # skott från distans
d.mv('fw', t, tsh + 0.4, (42, 10)); t = d.pas(b, tsh, rec(d, 'fw', tsh + 0.5), 0.5); tr = shoot(d, b, t + 0.05, (54, 1))   # forwarden på returen
hide(d, b, tr + 0.4); d.mv('fw', tr, tr + 1.6, (54, 22)); d.mv('mv1', tr, tr + 1.0, (50, 4))
b2 = d.newball((200, 200)); show(d, b2, tr + 0.6, rec(d, 'a2', tr + 0.6))
d.mv('o', tr, tr + 1.4, (62, 58)); t = d.pas(b2, tr + 1.0, rec(d, 'fw', tr + 2.2), 1.1)                 # kombinera med forwarden
d.mv('a1', tr + 0.8, t + 0.6, (50, 40)); t = d.pas(b2, t + 0.1, rec(d, 'a1', t + 0.7)); tg2 = shoot(d, b2, t + 0.05, (56, 1))
fp = [(0, 'Tre anfallare mot en försvarare', 'Skjut om ni har läge.'),
      (tsh - 0.3, 'Skott från distans', 'Forwarden går alltid på returen.'),
      (tr - 0.4, 'Mål på returen', ''),
      (tr + 1.0, 'Inget läge? Kombinera med forwarden', '')]
finish(d, 'sd25', 'skottmatch-3-mot-1', ['Skottmatch', '3 mot 1'], 'Yta 32 m djup · Dubbla straffområden',
       fp, 'AVSLUT', [('line', [(4, 50), (96, 50)])])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ sd26 Press och täckning 2 mot 2 ============
d = Drill()
d.p('x1', 'X1', B, (50, 92)); d.p('x2', 'X2', B, (50, 76)); team(d, 'y', B, [(32, 56), (68, 54)], ['X3', 'X4']); team(d, 'o', R, [(42, 30), (58, 28)], ['O1', 'O2'])
b = d.newball(rec(d, 'x1', 0))
t = d.pas(b, 0.4, rec(d, 'x2', 1.1))                                                     # X1 spelar till X2
t = d.pas(b, t + 0.2, rec(d, 'y0', t + 1.0)); d.mv('o0', t - 0.8, t + 0.6, (34, 46)); d.mv('o1', t - 0.8, t + 0.6, (46, 38))   # press och täckning
tp1 = t
t = drive(d, b, 'y0', t + 0.2, (36, 50), 8); t = d.pas(b, t + 0.1, rec(d, 'x2', t + 0.9))
t = d.pas(b, t + 0.2, rec(d, 'y1', t + 1.0)); tp2 = t
d.mv('o1', t - 0.8, t + 0.6, (64, 44)); d.mv('o0', t - 0.8, t + 0.6, (52, 36))            # nya roller
t = drive(d, b, 'y1', t + 0.2, (64, 48), 8)
tw = win(d, b, 'o1', 'y1', t + 0.2, 0.4); d.mv('o1', tw, tw + 1.0, (60, 36)); d.carry(b, 'o1', tw, tw + 1.0)   # avbryt när försvararna vinner
fp = [(0, 'X1 spelar till X2', 'X3 och X4 anfaller mot O1 och O2.'),
      (tp1 - 0.6, 'Närmaste pressar – den andra täcker', 'Täckningen snett bakom pressen.'),
      (tp2 - 0.6, 'Bollen flyttas – byt roller', 'Ny press, ny täckning.'),
      (tw - 0.2, 'Försvararna vinner bollen', 'Avbryt och starta om.')]
finish(d, 'sd26', 'press-och-tackning-2-mot-2-yta', ['Press och täckning', '2 mot 2'], 'Yta 30 × 20 m',
       fp, 'FÖRSVAR', [('box', 14, 14, 86, 86)], [lab(tp1, tp2, (26, 44), 'PRESS'), lab(tp1, tp2, (46, 30), 'TÄCK'), lab(tp2, tw, (72, 40), 'PRESS'), lab(tp2, tw, (52, 28), 'TÄCK')])

# ============ sd27 Press utan att vinna – täck bakom ============
d = Drill()
XP = [(24, 76), (50, 84), (76, 76)]; team(d, 'x', B, XP, ['X1', 'X2', 'X3']); d.p('x4', 'X4', B, (50, 10)); team(d, 'o', R, [(36, 52), (50, 44), (64, 52)])
b = d.newball(rec(d, 'x0', 0)); marks = []
seq = ['x1', 'x2', 'x1', 'x0']; t = 0.4
for k, pid in enumerate(seq):
    hold = ['x0', 'x1', 'x2', 'x1'][k]
    d.carry(b, hold, t, t + 0.9); t += 0.9                                                 # minst tre touch
    nearest = {'x0': 'o0', 'x1': 'o1', 'x2': 'o2'}[pid]
    t = d.pas(b, t + 0.1, rec(d, pid, t + 0.9)); marks.append(t)
    px, py = at(d.pl[pid]['tr'], t)
    for o, ps in (('o0', (36, 52)), ('o1', (50, 44)), ('o2', (64, 52))):
        if o == nearest: d.mv(o, t - 0.6, t + 0.6, (px + (50 - px) * 0.15, py - 9))     # pressar utan att vinna
        else: d.mv(o, t - 0.6, t + 0.6, (ps[0] + (px - ps[0]) * 0.2, 40))                 # täcker bakom
d.carry(b, 'x0', t, t + 0.9); t += 0.9
t = d.pas(b, t + 0.1, rec(d, 'x4', t + 1.6), 1.4); tx = t                                  # längs marken till X4
fp = [(0, 'X1–X3 passar med minst tre touch', 'De ska nå X4 längs marken.'),
      (marks[0] - 0.4, 'Närmaste försvarare pressar', 'Utan att vinna bollen.'),
      (marks[1] - 0.4, 'Övriga täcker bakom', 'Stäng vägen till X4.'),
      (tx - 1.0, 'Hittar de X4?', 'Försvararna flyttar ihop.')]
finish(d, 'sd27', 'press-utan-att-vinna-tack-bakom', ['Press utan att vinna', 'Täck bakom'], 'Yta 25 × 15 m',
       fp, 'FÖRSVAR', [('box', 14, 6, 86, 92)])

# ============ sd28 Markera 2 mot 2 + uppgivare ============
d = Drill(); d.p('mv', 'MV', R, (50, 4)); d.p('u', 'U', WHITE, (50, 90))
team(d, 'a', B, [(38, 56), (62, 52)]); team(d, 'f', R, [(40, 46), (60, 42)])
b = d.newball(rec(d, 'u', 0))
d.mv('a0', 0.4, 1.4, (34, 62)); d.mv('f0', 0.4, 1.4, (36, 54))                              # markera på rätt sida
t = d.pas(b, 0.6, rec(d, 'a0', 1.5)); t = drive(d, b, 'a0', t, (40, 40), 12); d.mv('f0', t - 1.0, t, (42, 32))
d.mv('a1', t - 1.0, t + 0.6, (58, 26)); d.mv('f1', t - 1.0, t + 0.6, (56, 22))
t = d.pas(b, t + 0.1, rec(d, 'a1', t + 0.8)); tw = win(d, b, 'f1', 'a1', t + 0.2, 0.4)      # bollvinst
t = d.pas(b, tw + 0.3, rec(d, 'u', tw + 1.5)); tu = t                                          # till uppgivaren
for k, ps in enumerate([(38, 56), (62, 52)]): d.mv(f'a{k}', tu, tu + 1.6, ps)
for k, ps in enumerate([(40, 46), (60, 42)]): d.mv(f'f{k}', tu, tu + 1.6, ps)
t = d.pas(b, tu + 1.8, rec(d, 'a1', tu + 2.6)); d.mv('f1', tu + 1.8, t, (62, 46))
t = drive(d, b, 'a1', t, (58, 30), 12); tg = shoot(d, b, t + 0.1, (52, 1))
fp = [(0, 'Två anfallare plus uppgivare', 'Mot två försvarare och målvakt.'),
      (0.4, 'Markera', 'Mellan anfallaren och målet.'),
      (tw - 0.2, 'Försvararna vinner bollen', 'Och spelar den till uppgivaren.'),
      (tu + 1.8, 'Nytt anfall', 'Byt uppgifter.')]
finish(d, 'sd28', 'markera-2-mot-2-plus-uppgivare', ['Markera 2 mot 2', '+ uppgivare'], 'Yta 25 × 20 m · Ett mål och målvakt',
       fp, 'DUELL', [('box', 16, 2, 84, 94)], [lab(tu, tu + 1.6, (50, 80), '+1')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ sd29 Press och täckning med mål ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96))
BP = [(36, 74), (64, 72)]; RP = [(40, 46), (60, 44)]; team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'mvb', 0))
t = d.pas(b, 0.4, rec(d, 'b0', 1.4), 1.0); d.mv('r0', 0.8, t + 0.6, (38, 62)); d.mv('r1', 0.8, t + 0.6, (48, 54))   # utkast – press och täckning
t = drive(d, b, 'b0', t + 0.1, (40, 66), 8); tw = win(d, b, 'r0', 'b0', t + 0.3, 0.4)
d.mv('r1', tw, tw + 1.0, (58, 74)); t = d.pas(b, tw + 0.2, rec(d, 'r1', tw + 1.0)); tg = shoot(d, b, t + 0.1, (54, 99))   # anfaller direkt
d.mv('b1', tw, tg, (56, 82)); d.mv('b0', tw, tg, (46, 74))
hide(d, b, tg + 0.4)
b2 = d.newball((200, 200)); show(d, b2, tg + 1.0, rec(d, 'mvb', tg + 1.0))
for k, ps in enumerate([(40, 70), (62, 66)]): d.mv(f'r{k}', tg + 0.4, tg + 2.0, ps)
t = d.pas(b2, tg + 1.2, rec(d, 'b1', tg + 2.2), 1.0); d.mv('r1', tg + 2.0, t + 0.6, (64, 60))
t = drive(d, b2, 'b1', t + 0.1, (70, 50), 10)
fp = [(0, 'Målvakten kastar ut till anfallarna', 'Två mot två med målvakter.'),
      (1.0, 'Press och täckning', 'Närmaste pressar, den andra täcker.'),
      (tw - 0.2, 'Bollvinst – anfall direkt', 'Rollerna byts.'),
      (tg + 1.0, 'Nytt utkast', '')]
finish(d, 'sd29', 'press-och-tackning-med-mal', ['Press och täckning', 'Med mål'], 'Yta 35 × 20 m med två mål',
       fp, 'FÖRSVAR', [('box', 18, 2, 82, 98)])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ sd30 Press 4 mot 4 ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96)); d.p('t', 'T', T_COL, (97, 50))
BP = [(28, 74), (72, 72), (40, 54), (62, 50)]; RP = [(32, 28), (68, 26), (44, 40), (58, 64)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b1', 'b3'], 0.3)
for k, ps in enumerate([(56, 52), (70, 46), (52, 44), (62, 58)]): d.mv(f'r{k}', t - 1.2, t + 0.6, ps)   # pressen flyttar mot bollen
tst = t + 0.6
tw = win(d, b, 'r3', 'b3', tst + 1.6, 0.6)
t = d.pas(b, tw + 0.3, rec(d, 'r2', tw + 1.0)); d.mv('r2', tw, t, (50, 66)); tg = shoot(d, b, t + 0.1, (46, 99))
fp = [(0, 'Fyra mot fyra med målvakter', 'Vanligt spel.'),
      (tst - 1.4, 'Pressa tillsammans', 'Flytta som en enhet mot bollen.'),
      (tst, 'Tränaren stoppar och coachar', 'Vem pressar? Vem täcker?'),
      (tw - 0.2, 'Bollvinst och avslut', '')]
finish(d, 'sd30', 'press-4-mot-4', ['Press', '4 mot 4'], 'Yta 35 × 40 m med två mål',
       fp, 'FÖRSVAR', [], [lab(tst, tst + 1.6, (80, 40), 'STOPP')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ sd31 Press 2 mot 2 med konmål ============
d = Drill()
d.p('x1', 'X1', B, (44, 94)); d.p('x2', 'X2', B, (46, 66)); d.p('o1', 'O1', R, (54, 34)); d.p('o2', 'O2', R, (56, 6))
b = d.newball(rec(d, 'x1', 0))
t = d.pas(b, 0.4, rec(d, 'x2', 1.2))
d.mv('x2', t, t + 1.6, (46, 40)); d.carry(b, 'x2', t, t + 1.6); d.mv('o1', t, t + 1.4, (48, 38)); t += 1.6   # O1 pressar
tw = win(d, b, 'o1', 'x2', t, 0.3)
d.mv('o2', tw - 0.6, tw + 0.4, (52, 14)); t = d.pas(b, tw + 0.3, rec(d, 'o2', tw + 1.2))                     # till O2
d.mv('x1', tw, t + 0.4, (50, 66))
d.mv('o2', t, t + 2.0, (52, 62)); d.carry(b, 'o2', t, t + 2.0); d.mv('x1', t + 0.4, t + 2.0, (50, 70)); t += 2.0   # O2 driver åt andra hållet, X1 pressar
d.mv('x2', tw, tw + 1.6, (40, 30))
fp = [(0, 'X1 spelar till X2', 'X2 driver mot konmålet.'),
      (1.4, 'O1 pressar', 'Bromsa och vinn bollen.'),
      (tw - 0.2, 'O1 vinner – spela till O2', 'O2 driver åt andra hållet.'),
      (tw + 1.6, 'Nu pressar X1', 'Rollerna roterar.')]
finish(d, 'sd31', 'press-2-mot-2-med-konmal', ['Press 2 mot 2', 'Med konmål'], 'Yta 20 × 10 m med konmål',
       fp, 'DUELL', [('box', 30, 8, 70, 92), ('cone', 44, 8), ('cone', 56, 8), ('cone', 44, 92), ('cone', 56, 92)])

if __name__ == '__main__': render(C, sys.argv)
