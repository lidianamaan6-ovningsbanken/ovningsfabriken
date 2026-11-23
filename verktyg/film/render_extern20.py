# Externa övningar, omgång 20 (tolv st). Regel: först d.mv, sedan d.carry; först mottagarens rörelse, sedan passningen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e9', __file__.replace('render_extern20.py', 'render_extern9.py'))
e9 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e9); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e9.finish, e9.rec, e9.chain, e9.wander, e9.counter, e9.arrivals
lab, hide, show, team, boxes, drive, shoot = e9.lab, e9.hide, e9.show, e9.team, e9.boxes, e9.drive, e9.shoot
factor, swap_color, stand, countdown, countup, win = e9.factor, e9.swap_color, e9.stand, e9.countdown, e9.countup, e9.win
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'

# ============ ve08 4 mot 4 med målzoner ============
d = Drill()
BP = [(30, 66), (70, 64), (42, 48), (60, 76)]; RP = [(34, 36), (66, 34), (52, 56), (44, 24)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b2', 'b1'], 0.3)
d.mv('b2', t - 1.2, t + 0.8, (46, 12)); d.mv('r3', t - 1.0, t + 0.8, (40, 22))
t = d.pas(b, t + 0.2, rec(d, 'b2', t + 1.1)); d.carry(b, 'b2', t, t + 0.5); tp = t                         # kontrollerad i målzonen
hide(d, b, tp + 0.8)
for k in range(4): d.mv(f'b{k}', tp + 0.4, tp + 2.4, BP[k]); d.mv(f'r{k}', tp + 0.4, tp + 2.4, RP[k])
b2 = d.newball((200, 200)); show(d, b2, tp + 2.5, rec(d, 'r1', tp + 2.5))
t = chain(d, b2, tp + 2.7, ['r2'], 0.3); t = drive(d, b2, 'r2', t, (54, 82), 18); d.mv('b3', t - 1.0, t, (62, 84))
tp2 = t + 0.3
fp = [(0, 'Fyra mot fyra utan målvakter', 'Målzon på 3 m i varje ände.'),
      (tp - 1.0, 'Kontrollerad boll i målzonen: 2 poäng', ''),
      (tp + 2.5, 'Rött anfaller', ''),
      (tp2 - 0.6, 'En touch in i zonen: 1 poäng', '')]
finish(d, 've08', '4-mot-4-med-malzoner', ['4 mot 4', 'Med målzoner'], 'Yta 25 × 20 m · 3 m målzoner i varje ände',
       fp, 'SMÅLAGSSPEL', [('box', 10, 4, 90, 96), ('zone', 10, 4, 90, 16, (120, 170, 230), 'MÅLZON'), ('zone', 10, 84, 90, 96, (230, 120, 110), 'MÅLZON')],
       [lab(tp, tp + 1.8, (50, 24), '+2'), lab(tp2, tp2 + 1.8, (50, 76), '+1')])

# ============ ve09 5 mot 5 med pressutlösare ============
d = Drill(); d.p('mvr', 'MV', R, (50, 6)); d.p('mvb', 'MV', B, (50, 94)); d.p('t', 'T', T_COL, (96, 50))
BP = [(30, 40), (70, 40), (50, 30), (38, 56), (62, 56)]; RP = [(30, 22), (70, 22), (40, 38), (60, 36), (50, 52)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'r4', 0))
t = d.pas(b, 0.4, rec(d, 'r2', 1.1)); t = d.pas(b, t + 0.2, rec(d, 'mvr', t + 1.0)); tu = t                  # bakåtpass – utlösare
for k, ps in enumerate([(36, 16), (62, 16), (52, 14), (42, 30), (60, 30)]): d.mv(f'b{k}', tu - 0.4, tu + 1.4, ps)
t = d.pas(b, tu + 0.4, rec(d, 'r1', tu + 1.3)); tw = win(d, b, 'b1', 'r1', t + 0.4, 0.5)                    # bollvinst inom fem sekunder
t = d.pas(b, tw + 0.2, rec(d, 'b2', tw + 0.8)); tg = shoot(d, b, t + 0.05, (46, 3))
fp = [(0, 'Vanligt 5 mot 5', 'Minimål.'),
      (tu - 0.4, 'Tränaren ropar ”bakåtpass!”', 'Det är utlösaren.'),
      (tu + 0.4, 'Pressa direkt – tillsammans', ''),
      (tw - 0.2, 'Bollvinst inom fem sekunder: bonuspoäng', '')]
finish(d, 've09', '5-mot-5-med-pressutlosare', ['5 mot 5', 'Med pressutlösare'], 'Två lag om fem · Minimål',
       fp, 'PRESS', [('box', 8, 4, 92, 96), ('smallgoal', 50, 4), ('smallgoal', 50, 96)],
       [lab(tu - 0.4, tu + 1.2, (78, 44), '”BAKÅTPASS!”')] + countup(tu, 5, (14, 40), (tw - tu) / 4)[:4] + [lab(tw, tw + 1.8, (70, 30), 'BONUS')])

# ============ db01 Minifotboll med fast anfallare ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96))
d.p('ba', 'A', B, (50, 14)); d.p('ra', 'A', R, (50, 86))                                                    # fast anfallare i motståndarnas målzon
BP = [(30, 66), (70, 62), (50, 46)]; RP = [(34, 34), (66, 36), (50, 56)]; team(d, 'b', B, BP); team(d, 'r', R, RP)
wander(d, 'ba', 0, 3.0, (40, 10, 60, 18), 3800, 1.4); wander(d, 'ra', 0, 17.9, (40, 82, 60, 90), 3801, 1.4)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b2'], 0.3); d.mv('ba', t - 0.6, t + 0.8, (44, 16)); t = d.pas(b, t + 0.2, rec(d, 'ba', t + 1.2))   # anfallaren rör bollen
d.mv('b1', t - 1.6, t + 0.4, (60, 26)); t = d.pas(b, t + 0.1, rec(d, 'b1', t + 0.7)); tg = shoot(d, b, t + 0.05, (54, 1))
fp = [(0, 'En fast anfallare i motståndarnas målzon', 'Hen kan inte göra mål själv.'),
      (1.4, 'Spela till anfallaren', ''),
      (tg - 0.6, 'Mål bara om anfallaren har rört bollen', 'Först till tio mål.'),
      (tg + 0.6, 'Variant: anfallaren får bara ett touch', '')]
finish(d, 'db01', 'minifotboll-med-fast-anfallare', ['Minifotboll', 'Med fast anfallare'], 'Yta 20–25 m · Fast anfallare i målzonen',
       fp, 'SMÅLAGSSPEL', [('zone', 30, 4, 70, 20, (120, 170, 230), 'ZON'), ('zone', 30, 80, 70, 96, (230, 120, 110), 'ZON')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ db02 Minifotboll med stödspelare ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96))
d.p('bs', 'S', B, (50, 84)); d.p('rs', 'S', R, (50, 16))                                                    # stödspelare i egen zon
BP = [(30, 62), (70, 60), (50, 48)]; RP = [(36, 36), (64, 34), (52, 52)]; team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b0', 0))
t = d.pas(b, 0.4, rec(d, 'bs', 1.2)); t = d.pas(b, t + 0.3, rec(d, 'b1', t + 1.1))                          # 4 mot 3 med stödspelaren
t = drive(d, b, 'b1', t, (62, 34), 18); d.mv('r1', t - 1.0, t, (60, 28))                                    # in i streckade zonen
d.mv('b2', t - 1.4, t, (46, 28)); t = d.pas(b, t + 0.1, rec(d, 'b2', t + 0.7)); tg = shoot(d, b, t + 0.05, (46, 1))
fp = [(0, 'Stödspelaren i egen målzon', 'Med bara när laget har bollen: 4 mot 3.'),
      (1.2, 'Använd stödspelaren', 'Hen får inte lämna sin zon.'),
      (tg - 1.6, 'Dribbla eller spela in i zonen', 'Innan mål får göras.'),
      (tg - 0.3, 'Mål', 'Först till tio mål.')]
finish(d, 'db02', 'minifotboll-med-stodspelare', ['Minifotboll', 'Med stödspelare'], 'Yta 20–25 m · Fast stödspelare i egen målzon',
       fp, 'SMÅLAGSSPEL', [('zone', 30, 80, 70, 96, (120, 170, 230), 'STÖD'), ('zone', 30, 4, 70, 20, (230, 120, 110), 'STÖD'), ('zone', 10, 20, 90, 36, (200, 220, 200), 'ZON')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ db03 Horst Wein med bandare ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96))
team(d, 'w', WHITE, [(6, 36), (6, 64), (94, 36)], ['', '', ''])                                             # bandarna
BP = [(32, 64), (68, 62), (50, 48)]; RP = [(36, 34), (64, 36), (50, 54)]; team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b0', 0))
t = d.pas(b, 0.4, rec(d, 'w1', 1.3)); t = d.pas(b, t + 0.2, rec(d, 'b2', t + 1.1)); t = d.pas(b, t + 0.2, rec(d, 'w2', t + 1.2))
d.mv('b1', t - 1.4, t + 0.6, (60, 24)); t = d.pas(b, t + 0.2, rec(d, 'b1', t + 1.1))
tg = shoot(d, b, t + 0.1, (54, 1)); hide(d, b, tg + 0.4)
for k, ps in enumerate([(6, 50), (94, 50), (94, 64)]): d.mv(f'r{k}', tg + 0.4, tg + 2.8, ps)                 # laget som släppte in blir bandare
for k, ps in enumerate([(36, 34), (64, 36), (50, 54)]): d.mv(f'w{k}', tg + 0.4, tg + 2.8, ps)
fp = [(0, '3 mot 3 med bandare', 'Bandarna spelar med laget som har bollen.'),
      (1.4, 'Använd bandarna', ''),
      (tg - 0.4, 'Mål', 'Efter dribbling eller spel in i zonen.'),
      (tg + 0.6, 'Laget som släppte in mål blir bandare', 'Först till fem mål.')]
finish(d, 'db03', 'horst-wein-med-bandare', ['Horst Wein', 'Med bandare'], 'Yta 20–25 m · Tre lag',
       fp, 'SMÅLAGSSPEL', [('box', 12, 2, 88, 98)])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True
f = factor(fp); ids = {k: i for i, k in enumerate(d.order)}
for k in range(3): swap_color(ids[f'r{k}'], (tg + 1.6) * f, R, WHITE); swap_color(ids[f'w{k}'], (tg + 1.6) * f, WHITE, R)

# ============ db04 Match där finter ger 3 mål ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96))
BP = [(30, 66), (70, 64), (44, 48), (58, 78)]; RP = [(34, 36), (66, 34), (52, 54), (46, 24)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b2'], 0.3); t = drive(d, b, 'b2', t, (46, 32), 16); d.mv('r3', t - 1.0, t, (46, 26))
d.mv('b2', t, t + 0.5, (40, 28)); d.carry(b, 'b2', t, t + 0.5); d.mv('r3', t, t + 0.5, (42, 24))
d.mv('b2', t + 0.5, t + 1.0, (54, 20)); d.carry(b, 'b2', t + 0.5, t + 1.0); tf = t + 0.5                     # fint
tg = shoot(d, b, t + 1.1, (54, 1))
fp = [(0, 'Vanlig match', 'Yta 25–30 m.'),
      (tf - 0.4, 'Fint eller bra dribbling', ''),
      (tg - 0.4, 'Mål efter fint: tre mål', ''),
      (tg + 0.6, 'Variant: max tre touch', '')]
finish(d, 'db04', 'match-dar-finter-ger-3-mal', ['Match där finter', 'ger 3 mål'], 'Yta 25–30 m · Klassisk match',
       fp, 'SMÅLAGSSPEL', [('box', 10, 2, 90, 98)], [lab(tf, tf + 1.2, (60, 34), 'FINT'), lab(tg, tg + 2.0, (54, 14), '+3')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ db05 Timglaset ============
d = Drill()
CN = [(36, 22), (64, 22), (44, 50), (56, 50), (36, 78), (64, 78)]
SP = [(28, 16), (72, 16), (72, 84), (28, 84)]
for k, ps in enumerate(SP): d.p(f'p{k}', '', B, ps)
d.p('q', '', B, (22, 12))
occ = {0: ['p0', 'q'], 1: ['p1'], 2: ['p2'], 3: ['p3']}
def qp(c, n): x, y = SP[c]; return (x + (-5 if x < 50 else 5) * n, y + (-4 if y < 50 else 4) * n)
b = d.newball(rec(d, 'p0', 0)); t = 0.4; laps = []
order = [0, 2, 1, 3]                                                                                        # diagonalt genom timglasets midja
for rep in range(8):
    c = order[rep % 4]; nc = order[(rep + 1) % 4]
    p = occ[c].pop(0); r = occ[nc][0]
    t1 = d.pas(b, t, rec(d, r, t + 1.2))
    d.mv(p, t + 0.2, t1 + 1.6, qp(nc, len(occ[nc]))); occ[nc].append(p)                                       # följ bollen
    for n, w in enumerate(occ[c]): d.mv(w, t + 0.4, t + 1.0, qp(c, n))
    if rep % 4 == 3: laps.append(t1)
    t = t1 + 0.4
fp = [(0, 'Passa runt konparen', 'Konparen bildar ett timglas.'),
      (1.6, 'Följ bollen', ''),
      (laps[0], 'Ett varv', 'Åt båda hållen.'),
      (laps[0] + 2.0, 'Flest varv på tre minuter vinner', 'Variant: fler bollar.')]
finish(d, 'db05', 'timglaset', ['Timglaset', 'Passningsövning'], 'Yta ca 15 m · Två konpar snett som ett timglas',
       fp, 'PASSNINGSÖVNING', [('cone',) + c for c in CN], counter(laps, pos=(50, 92), last=None))

# ============ db06 6 mot 6 + 3 – positionsspel ============
d = Drill()
AP = [(50, 8), (50, 92), (10, 34), (10, 66), (90, 34), (90, 66)]; PP = [(38, 36), (62, 36), (34, 62), (66, 62), (44, 50), (58, 52)]
team(d, 'b', B, AP); team(d, 'r', R, PP); team(d, 'j', YEL, [(50, 30), (40, 70), (60, 70)], ['J', 'J', 'J'])
for k in range(6): wander(d, f'r{k}', 0, 9.0, boxes([PP[k]], 4)[0], 3900 + k, 1.6)
for k in range(3): wander(d, f'j{k}', 0, 17.9, boxes([[(50, 30), (40, 70), (60, 70)][k]], 4)[0], 3910 + k, 1.6)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b2', 'j0', 'b4', 'j2', 'b1', 'j1', 'b3', 'b5'], 0.25); cnt = arrivals(d, b)[:8]
tw = win(d, b, 'r3', 'b5', t + 0.4)
for k in range(6): d.mv(f'r{k}', tw + 0.3, tw + 2.2, AP[k]); d.mv(f'b{k}', tw + 0.3, tw + 2.2, PP[k])        # rollerna byts
d.carry(b, 'r3', tw, tw + 2.2)
fp = [(0, 'Anfallarna på sidlinjerna', 'En i varje ände, två på varje sida.'),
      (2.0, 'Använd jokrarna i mitten', ''),
      (cnt[-1] - 0.3, 'Åtta passningar i rad: poäng', ''),
      (tw - 0.2, 'Bollvinst – rollerna byts', 'Det nya laget tar positionerna.')]
finish(d, 'db06', '6-mot-6-plus-3-positionsspel', ['6 mot 6 + 3', 'Positionsspel'], 'Yta 30 × 50 m · Tre jokrar i mitten',
       fp, 'POSITIONSSPEL', [('box', 10, 8, 90, 92)], counter(cnt, pos=(76, 20)))

# ============ db07 United-spelet ============
d = Drill()
BP = [(26, 76), (50, 80), (74, 76), (36, 58), (64, 58), (50, 44)]; RP = [(30, 28), (50, 22), (70, 28), (40, 42), (60, 40), (50, 60)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b1', 0))
t = d.pas(b, 0.4, rec(d, 'b0', 1.2)); d.mv('b1', t, t + 0.8, (50, 66)); ts1 = t                              # passning i sidled – sprinta framåt
t = d.pas(b, t + 0.3, rec(d, 'b3', t + 1.0)); t = d.pas(b, t + 0.2, rec(d, 'b1', t + 0.9))
d.mv('b3', t - 0.4, t + 0.6, (40, 46)); ts2 = t - 0.4
t = d.pas(b, t + 0.2, rec(d, 'b4', t + 0.9)); t = drive(d, b, 'b4', t, (64, 14), 18); d.mv('r2', t - 1.4, t, (70, 18))
d.mv('b4', t, t + 0.8, (62, 3)); d.carry(b, 'b4', t, t + 0.8); tg = t + 0.8                                 # dribbla över baklinjen
fp = [(0, 'Sju mot sju', 'Mål: dribbla över motståndarnas baklinje.'),
      (ts1, 'Passning i sidled – sprinta 5–8 m framåt', ''),
      (ts2, 'Glömmer någon sprinten?', 'Då får motståndarna poäng.'),
      (tg - 0.6, 'Över baklinjen: mål', 'Tio passningar i rad ger extra poäng.')]
finish(d, 'db07', 'united-spelet', ['United-', 'spelet'], 'Yta 30 × 50 m · Sju mot sju',
       fp, 'SPELÖVNING', [('box', 8, 4, 92, 96)], [lab(ts1, ts1 + 1.2, (64, 72), 'SPRINT'), lab(ts2, ts2 + 1.2, (28, 50), 'SPRINT'), lab(tg, tg + 1.8, (62, 10), 'MÅL')])

# ============ db08 Fotbollstennis ============
d = Drill()
team(d, 'b', B, [(34, 72), (66, 76)]); team(d, 'r', R, [(36, 26), (64, 22)])
b = d.newball(rec(d, 'b0', 0)); t = 0.4
seq = [('b0', 'r1'), ('r1', 'r0'), ('r0', 'b1'), ('b1', 'b0'), ('b0', 'r0'), ('r0', 'r1'), ('r1', 'b1')]
for frm, to in seq:
    if frm[0] != to[0]:
        t1 = d.pas(b, t + 0.2, (at(d.pl[to]['tr'], t)[0] + 1.8, 50), 0.5)                               # över nätet
        t = d.pas(b, t1, rec(d, to, t1 + 0.6), 0.6)
    else: t = d.pas(b, t + 0.2, rec(d, to, t + 0.9))                                                        # inom laget
    t += 0.2
tl = d.pas(b, t, (90, 60), 0.6); hide(d, b, tl + 0.3)                                                         # bollen ut – poäng
fp = [(0, 'Spela bollen över nätet', 'Som i tennis.'),
      (2.0, 'Alla touch med insidan', ''),
      (6.0, 'Låg intensitet', 'Bra efter match.'),
      (tl - 0.4, 'Får laget inte tillbaka bollen förlorar det poängen', '')]
finish(d, 'db08', 'fotbollstennis', ['Fotbollstennis', 'Teknik'], 'Bana delad med nät, band eller linje',
       fp, 'TEKNIK', [('box', 16, 8, 84, 92), ('line', [(16, 50), (84, 50)])], [lab(tl, tl + 1.6, (66, 40), 'POÄNG RÖTT')])

# ============ db09 Reaktionssnabbhet ============
d = Drill(); YS = [30, 70]
for k, y in enumerate(YS): d.p(f'k{k}', 'K', ORA, (30, y)); d.p(f's{k}', 'S', B, (40, y))
for k, y in enumerate(YS):
    b = d.newball(rec(d, f'k{k}', 0)); t = 0.4 + 0.4 * k
    for rep in range(2):
        t1 = d.pas(b, t, (78, y), 1.2)                                                                        # kastar över huvudet
        d.mv(f's{k}', t + 0.1, t1 + 0.3, (76, y + 1))                                                         # sprintar ut
        d.mv(f's{k}', t1 + 0.4, t1 + 2.4, (40, y)); d.carry(b, f's{k}', t1 + 0.4, t1 + 2.4)                   # vänder och sprintar tillbaka
        t2 = d.pas(b, t1 + 2.5, rec(d, f'k{k}', t1 + 3.0), 0.4); t = t2 + 0.6
fp = [(0, 'Kasta bollen över kompisens huvud', 'Par.'),
      (0.6, 'Sprinta ut', ''),
      (2.2, 'Vänd och sprinta tillbaka', 'Med bollen vid fötterna.'),
      (6.0, 'Byt roller', '')]
finish(d, 'db09', 'reaktionssnabbhet', ['Reaktions-', 'snabbhet'], 'Par',
       fp, 'LEK', [])

# ============ db10 Nickar mot mål ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
for k in range(3): d.p(f'k{k}', 'K', ORA, (30 + 20 * k, 42)); d.p(f'n{k}', 'N', B, (34 + 16 * k, 22))
t = 0.4; ex = []
for rep in range(6):
    k = rep % 3; b = d.newball((200, 200)); show(d, b, t, rec(d, f'k{k}', t))
    t1 = d.pas(b, t + 0.2, (35 + 16 * k, 21), 0.9); tg = d.pas(b, t1, (44 + 6 * k, 1), 0.4); hide(d, b, tg + 0.3)   # kast – nick
    ex.append(lab(t1, t1 + 0.8, (35 + 16 * k, 14), 'NICK')); t = t + 1.6
fp = [(0, 'Kasta in – nicka mot mål', 'Stora mål.'),
      (2.0, 'Många nickar på kort tid', ''),
      (5.0, 'Turas om att kasta och nicka', ''),
      (8.0, 'Byt målvakt efter en stund', '')]
finish(d, 'db10', 'nickar-mot-mal', ['Nickar', 'mot mål'], 'Stora mål · Bollar som kastas in',
       fp, 'AVSLUT', [], ex)
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

if __name__ == '__main__': render(C, sys.argv)
