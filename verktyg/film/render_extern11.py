# Externa övningar, omgång 11 (tolv st). Regel: först d.mv, sedan d.carry; först mottagarens rörelse, sedan passningen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e9', __file__.replace('render_extern11.py', 'render_extern9.py'))
e9 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e9); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e9.finish, e9.rec, e9.chain, e9.wander, e9.counter, e9.arrivals
lab, hide, show, team, boxes, drive, shoot = e9.lab, e9.hide, e9.show, e9.team, e9.boxes, e9.drive, e9.shoot
factor, swap_color, stand, countdown, countup, win = e9.factor, e9.swap_color, e9.stand, e9.countdown, e9.countup, e9.win
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'

# ============ sd08 3 mot 3 + 2 utan mål ============
d = Drill()
BP = [(24, 30), (76, 34), (50, 70)]; RP = [(40, 42), (60, 46), (48, 58)]; team(d, 'b', B, BP); team(d, 'r', R, RP); team(d, 'j', YEL, [(10, 52), (90, 52)], ['J', 'J'])
for k in range(3): wander(d, f'r{k}', 0, 6.0, boxes([RP[k]], 4)[0], 1800 + k, 1.6)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['j0', 'b2', 'j1', 'b1', 'b0'], 0.3)
tw = win(d, b, 'r0', 'b0', t + 0.4)
for k, ps in enumerate([(36, 40), (64, 42), (50, 54)]): d.mv(f'b{k}', tw + 0.2, tw + 1.8, ps)
for k, ps in enumerate([(26, 26), (74, 30), (52, 76)]):
    if k: d.mv(f'r{k}', tw + 0.2, tw + 1.8, ps)
d.mv('r0', tw, tw + 1.2, (26, 30)); d.carry(b, 'r0', tw, tw + 1.2)
t = d.pas(b, tw + 1.3, rec(d, 'j0', tw + 2.0)); t = chain(d, b, t, ['r2', 'j1', 'r1'], 0.3)
fp = [(0, 'Tre mot tre plus två jokrar', 'Jokrarna spelar med laget som har bollen.'),
      (1.2, 'Håll bollen', 'Använd jokrarna för att skapa överläge.'),
      (tw - 0.2, 'Bollvinst – rött håller nu', 'Jokrarna byter lag med bollen.'),
      (tw + 2.0, 'Fem mot tre igen', 'Byt jokrar efter två minuter.')]
finish(d, 'sd08', '3-mot-3-plus-2-utan-mal', ['3 mot 3 + 2', 'Utan mål'], 'Yta 25 × 20 m · Tre mot tre plus två jokrar',
       fp, 'POSITIONSSPEL', [('box', 10, 18, 90, 86)])

# ============ sd09 Spelvändning via kanten ============
d = Drill()
P = [(8, 64), (26, 78), (44, 62), (60, 78), (76, 62), (93, 38)]
for k, ps in enumerate(P): d.p(f'x{k + 1}', f'X{k + 1}', B, ps)
b = d.newball(rec(d, 'x1', 0))
t = chain(d, b, 0.4, ['x2', 'x3', 'x4', 'x5'], 0.3)
d.mv('x6', t - 0.8, t + 0.6, (93, 30)); t = d.pas(b, t + 0.2, rec(d, 'x6', t + 1.2)); te = t                # kantspelaren
d.mv('x5', te - 0.8, te + 0.6, (84, 48))                                                                    # stöttar
t = d.pas(b, te + 0.3, rec(d, 'x5', te + 1.0)); tb = t                                                       # tillbakaspel vänder spelet
d.mv('x5', tb, tb + 1.2, P[4]); d.mv('x6', tb, tb + 1.2, P[5])
t = chain(d, b, tb + 0.4, ['x4', 'x3', 'x2'], 0.3)
d.mv('x1', t - 1.0, t + 0.6, (7, 40)); t = d.pas(b, t + 0.2, rec(d, 'x1', t + 1.0)); d.mv('x2', t - 0.6, t + 0.6, (18, 56))
fp = [(0, 'X1 till X5 i kedja', 'Sex stationer från kant till kant.'),
      (te - 0.8, 'X5 hittar X6 på kanten', 'Den som passat stöttar kantspelaren.'),
      (tb - 0.4, 'Tillbakaspel vänder spelet', 'Nu går bollen åt andra hållet.'),
      (t - 1.0, 'Hela vägen till andra kanten', 'Upprepa åt båda hållen.')]
finish(d, 'sd09', 'spelvandning-via-kanten', ['Spelvändning', 'Via kanten'], 'Yta 50 × 40 m · Sex stationer från kant till kant',
       fp, 'PASSNINGSÖVNING', [('box', 4, 20, 96, 92)])

# ============ sd10 6 mot 6 – mål efter spelvändning ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96))
BK = [(10, 60), (90, 40)]; RK = [(10, 36), (90, 66)]; team(d, 'bk', B, BK, ['K', 'K']); team(d, 'rk', R, RK, ['K', 'K'])
BP = [(36, 70), (62, 72), (42, 50), (60, 44)]; RP = [(38, 30), (62, 28), (46, 42), (56, 58)]; team(d, 'b', B, BP); team(d, 'r', R, RP)
for k in range(4): wander(d, f'r{k}', 0, 5.6, boxes([RP[k]], 3)[0], 1900 + k, 1.6)
b = d.newball(rec(d, 'b0', 0))
t = d.pas(b, 0.4, rec(d, 'bk0', 1.3)); k1 = t                                                               # vänster kantspelare
d.mv('bk0', t, t + 1.2, (10, 48)); d.carry(b, 'bk0', t, t + 1.2); t += 1.2
t = d.pas(b, t + 0.1, rec(d, 'b2', t + 0.9)); t = d.pas(b, t + 0.2, rec(d, 'b3', t + 0.8))
t = d.pas(b, t + 0.2, rec(d, 'bk1', t + 1.0)); k2 = t                                                       # höger kantspelare
d.mv('bk1', t, t + 1.4, (90, 20)); d.carry(b, 'bk1', t, t + 1.4); t += 1.4
d.mv('b3', t - 1.6, t + 0.8, (54, 14)); t = d.pas(b, t + 0.1, rec(d, 'b3', t + 0.9)); tg = shoot(d, b, t + 0.05, (46, 1))
d.mv('r1', k2, tg, (58, 18))
fp = [(0, 'Sex mot sex med två kantspelare per lag', 'Kantspelarna i korridorerna får inte pressas.'),
      (k1 - 0.3, 'Ena kantspelaren har bollen', ''),
      (k2 - 0.3, 'Spelvändning till andra kanten', 'Båda kantspelarna har haft bollen.'),
      (tg - 0.5, 'Nu räknas målet', 'Mål räknas bara efter en spelvändning.')]
finish(d, 'sd10', '6-mot-6-mal-efter-spelvandning', ['6 mot 6', 'Mål efter spelvändning'], 'Yta 50 × 60 m · Två mål · Korridorer på kanterna',
       fp, 'SMÅLAGSSPEL', [('zone', 0, 4, 18, 96, (200, 220, 200), ''), ('zone', 82, 4, 100, 96, (200, 220, 200), '')],
       [lab(k1, tg + 1.8, (10, 86), 'VÄNSTER'), lab(k2, tg + 1.8, (90, 86), 'HÖGER'), lab(tg, tg + 1.8, (46, 14), 'MÅL')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ sd11 Spelvändning med mittspelare ============
d = Drill()
d.p('x5', 'X5', B, (18, 88)); d.p('x6', 'X6', B, (82, 88)); d.p('x3', 'X3', B, (50, 56))
d.p('x4', 'X4', B, (24, 44)); d.p('x1', 'X1', B, (18, 12)); d.p('x2', 'X2', B, (82, 12))
b = d.newball(rec(d, 'x5', 0)); marks = []
t = d.pas(b, 0.4, rec(d, 'x3', 1.4)); d.mv('x3', 0.6, 1.4, (46, 60))
d.mv('x4', t - 0.4, t + 1.6, (74, 38)); t = d.pas(b, t + 0.2, (72, 38), 1.2); marks.append(t)             # framför löpningen
d.carry(b, 'x4', t, t + 0.4); t = d.pas(b, t + 0.5, rec(d, 'x2', t + 1.4)); marks.append(t)
d.mv('x3', t - 1.0, t + 0.6, (50, 56))
d.mv('x2', t, t + 2.4, (82, 88)); d.carry(b, 'x2', t, t + 2.4); t += 2.4                                 # driver tillbaka och startar åt andra hållet
d.mv('x6', t - 2.2, t - 0.6, (82, 76))
t = d.pas(b, t + 0.2, rec(d, 'x3', t + 1.2)); d.mv('x3', t - 0.8, t, (54, 60))
d.mv('x4', t - 0.4, t + 1.6, (26, 38)); t = d.pas(b, t + 0.2, (28, 38), 1.2); marks.append(t)
d.carry(b, 'x4', t, t + 0.4); t = d.pas(b, t + 0.5, rec(d, 'x1', t + 1.4))
fp = [(0, 'X5 startar anfallet', 'Till mittspelaren X3.'),
      (marks[0] - 1.4, 'Passningen slås framför löpningen', 'X4 byter sida i full fart.'),
      (marks[1] - 0.4, 'Vidare till kanten', 'Sedan åt andra hållet.'),
      (marks[2] - 1.4, 'Samma mönster spegelvänt', 'Byt mittspelare efter några varv.')]
finish(d, 'sd11', 'spelvandning-med-mittspelare', ['Spelvändning', 'Med mittspelare'], 'Yta 35 × 20 m · Mittspelare · X1–X6 i mönster',
       fp, 'PASSNINGSÖVNING', [('box', 8, 4, 92, 96)])

# ============ sd12 Passningstjärnan ============
d = Drill()
SIDE = {'n': (50, 12), 's': (50, 88), 'w': (12, 50), 'e': (88, 50)}; MID = [(42, 44), (58, 56), (50, 50)]
for k, ps in SIDE.items(): d.p('s' + k, '', B, ps)
team(d, 'm', B, MID[:2] + [(52, 40)], ['', '', ''])
occ = {('s', k): 's' + k for k in SIDE}; mids = ['m0', 'm1', 'm2']; spots = {'m0': MID[0], 'm1': MID[1], 'm2': (52, 40)}
bA = d.newball(rec(d, 'm0', 0)); bB = d.newball(rec(d, 'm1', 0))
holder = {bA: 'm0', bB: 'm1'}; free_mid = ['m2']
plan = [(bA, 'n', 0.4), (bB, 's', 1.2), (bA, 'e', 3.6), (bB, 'w', 4.4), (bA, 's', 6.8), (bB, 'n', 7.6), (bA, 'w', 10.0), (bB, 'e', 10.8)]
for ball, side, t in plan:
    h = holder[ball]; sp = occ[('s', side)]; hp = at(d.pl[h]['tr'], t)
    t1 = d.pas(ball, t, rec(d, sp, t + 0.9))                                     # ut till sidan
    d.mv(h, t + 0.1, t + 1.6, SIDE[side])                                        # följ passningen
    recv = free_mid.pop(0)
    t2 = d.pas(ball, t1 + 0.3, rec(d, recv, t1 + 1.0))                          # in till fri mittspelare
    d.mv(sp, t1 + 0.4, t1 + 2.0, hp)                                             # sidospelaren går in
    occ[('s', side)] = h; holder[ball] = recv; free_mid.append(sp)
fp = [(0, 'Tre i mitten, två har boll', 'En spelare utanför varje sida.'),
      (1.4, 'Ut till sidan – in igen', 'Spela in till den fria mittspelaren.'),
      (3.2, 'Följ din passning och byt plats', ''),
      (8.0, 'Alltid minst en fri i mitten', 'Lyft blicken innan bollen kommer.')]
finish(d, 'sd12', 'passningstjarnan', ['Passnings-', 'tjärnan'], 'Yta 15 × 15 m · Tre i mitten, två bollar · En spelare utanför varje sida',
       fp, 'PASSNINGSÖVNING', [('box', 18, 18, 82, 82)])

# ============ sd13 Kontring – passa i djupled ============
d = Drill()
d.p('x1', 'X1', B, (50, 76)); d.p('x2', 'X2', B, (50, 56)); d.p('x3', 'X3', B, (40, 88)); d.p('x4', 'X4', B, (38, 12)); d.p('x5', 'X5', B, (62, 12))
d.p('y1', 'X1', B, (50, 24)); d.p('y2', 'X2', B, (50, 44)); d.p('y3', 'X3', B, (60, 12)) if False else None
d.p('q1', 'X1', B, (56, 92)); d.p('q2', 'X3', B, (44, 94))
b = d.newball(rec(d, 'x1', 0))
d.mv('x2', 0.4, 1.0, (50, 60)); t = d.pas(b, 0.5, rec(d, 'x2', 1.2))                                     # X1 till X2
t = d.pas(b, t + 0.15, rec(d, 'x3', t + 0.8))                                                             # tillbaka till X3
d.mv('x1', t - 0.8, t + 1.2, (56, 34)); t = d.pas(b, t + 0.2, rec(d, 'x1', t + 1.3)); td = t              # djupt till X1
t = d.pas(b, t + 0.2, rec(d, 'x5', t + 0.9)); t4 = t                                                      # vidare till X5
d.mv('x1', t4, t4 + 1.6, (68, 8)); d.mv('x2', t4 - 0.6, t4 + 2.2, (60, 26)); d.mv('x3', t4 - 0.8, t4 + 2.6, (50, 76))   # följ bollen
d.mv('q1', t4 - 0.4, t4 + 1.0, (40, 88))
# övningen vänder
d.mv('y2', t4 + 0.6, t4 + 1.2, (50, 40)); t = d.pas(b, t4 + 0.8, rec(d, 'y2', t4 + 1.5))
t = d.pas(b, t + 0.15, rec(d, 'x5', t + 0.8))
d.mv('y1', t - 0.8, t + 1.2, (44, 66)); t = d.pas(b, t + 0.2, rec(d, 'y1', t + 1.3))
t = d.pas(b, t + 0.2, rec(d, 'q1', t + 0.9)); tr = t
fp = [(0, 'X1 till X2, tillbaka till X3', 'Nio spelare i ett mönster som vänder.'),
      (td - 1.4, 'Djupt till X1', 'Som spelar vidare till X4 eller X5.'),
      (t4 + 0.2, 'Följ bollen till motsatt sida', ''),
      (t4 + 0.8, 'Övningen vänder', 'Samma mönster åt andra hållet.')]
finish(d, 'sd13', 'kontring-passa-i-djupled', ['Kontring', 'Passa i djupled'], 'Yta 35 × 15 m · Nio spelare i ett mönster som vänder',
       fp, 'PASSNINGSÖVNING', [('box', 30, 4, 70, 96)])

# ============ sd14 Lagdelar framför – snabb uppflyttning ============
d = Drill(); ex = []
for li, x in enumerate((22, 50, 78)):
    for row, y in enumerate((82, 54, 26)):
        d.p(f'p{li}{row}a', str(row + 1), B, (x - 5, y)); d.p(f'p{li}{row}b', str(row + 1), B, (x + 5, y))
    b = d.newball(rec(d, f'p{li}0a', 0)); t = 0.4 + 0.4 * li
    t = d.pas(b, t, rec(d, f'p{li}0b', t + 0.5), 0.4)
    t = d.pas(b, t + 0.2, rec(d, f'p{li}1a', t + 1.0))                                   # till paret framför
    d.mv(f'p{li}0a', t - 0.6, t + 1.6, (x - 5, 66)); d.mv(f'p{li}0b', t - 0.6, t + 1.6, (x + 5, 66))     # flyttar upp
    t = d.pas(b, t + 0.2, rec(d, f'p{li}1b', t + 0.7), 0.4)
    t = d.pas(b, t + 0.2, rec(d, f'p{li}2a', t + 1.0))
    d.mv(f'p{li}1a', t - 0.6, t + 1.6, (x - 5, 38)); d.mv(f'p{li}1b', t - 0.6, t + 1.6, (x + 5, 38))
    t = d.pas(b, t + 0.2, rec(d, f'p{li}2b', t + 0.7), 0.4)
    d.mv(f'p{li}2a', t, t + 1.6, (x - 5, 10)); d.mv(f'p{li}2b', t, t + 1.6, (x + 5, 10)); d.carry(b, f'p{li}2b', t, t + 1.6); t += 1.6
    # tillbaka ner: hela gruppen flyttar ner ett steg
    for row, (y0, y1) in enumerate(((66, 82), (38, 54), (10, 26))):
        d.mv(f'p{li}{row}a', t + 0.4, t + 2.2, (x - 5, y1)); d.mv(f'p{li}{row}b', t + 0.4, t + 2.2, (x + 5, y1))
    d.carry(b, f'p{li}2b', t + 0.4, t + 2.2)
    t = d.pas(b, t + 2.4, rec(d, f'p{li}1a', t + 3.2)); t = d.pas(b, t + 0.2, rec(d, f'p{li}0a', t + 1.0))
fp = [(0, 'Tre grupper bredvid varandra', 'Par bakom och par framför.'),
      (1.2, 'Spela till paret framför', 'Och flytta upp direkt.'),
      (5.0, 'Snabb uppflyttning', 'Hela lagdelen följer med bollen.'),
      (8.6, 'Tillbaka och igen', 'Byt i mitten efter ett par minuter.')]
finish(d, 'sd14', 'lagdelar-framfor-snabb-uppflyttning', ['Lagdelar framför', 'Snabb uppflyttning'], 'Yta 10 × 30 m · Tre grupper bredvid varandra',
       fp, 'PASSNINGSÖVNING', [('box', 12, 4, 32, 92), ('box', 40, 4, 60, 92), ('box', 68, 4, 88, 92)])

# ============ sd15 Ledig yta efter passning ============
d = Drill()
S = {'L': (14, 50), 'T': (50, 14), 'R': (86, 50)}
for k, ps in S.items(): d.p(k, k if k != 'T' else 'T', B, ps)
d.p('M', 'M', B, (50, 56))
b1 = d.newball(rec(d, 'L', 0)); b2 = d.newball(rec(d, 'T', 0))
hold = {'L': b1, 'T': b2}; free = 'R'; last = None; t = 0.4; turns = []
for step in range(6):
    h = [k for k in ('L', 'T', 'R') if k in hold and k != last][0]
    ball = hold.pop(h)
    hx, hy = S[h]; mx, my = 50 + (hx - 50) * 0.25, 52 + (hy - 52) * 0.25
    d.mv('M', t, t + 0.6, (mx, my)); t1 = d.pas(ball, t + 0.1, rec(d, 'M', t + 0.8))           # in till mitten
    fx, fy = S[free]; d.mv('M', t1, t1 + 0.5, (50 + (fx - 50) * 0.15, 52 + (fy - 52) * 0.15)); d.carry(ball, 'M', t1, t1 + 0.5)   # vänd
    turns.append(t1)
    t2 = d.pas(ball, t1 + 0.6, rec(d, free, t1 + 1.3)); hold[free] = ball; last = free; free = h; t = t2 + 0.1
d.mv('M', t, t + 1.4, (50, 26)); d.mv('T', t, t + 1.4, (50, 56))
fp = [(0, 'Mittspelaren spelar centralt', 'Fyra spelare och två bollar.'),
      (turns[0] - 0.2, 'Vänd till motsatt sida', 'Ta emot med rätt fot – öppen kropp.'),
      (turns[2], 'Spela till den lediga ytan', 'Den sida som just blev fri.'),
      (t, 'Byt mittspelare efter en minut', '')]
finish(d, 'sd15', 'ledig-yta-efter-passning', ['Ledig yta', 'Efter passning'], 'Kvadrat med fyra spelare och två bollar',
       fp, 'PASSNINGSÖVNING', [('box', 8, 8, 92, 92)])

# ============ sd16 Kontring 1 mot 1 ============
d = Drill()
d.p('s', 'S', WHITE, (50, 90)); d.p('a', 'A', B, (50, 72)); d.p('f', 'F', R, (50, 22)); d.p('a2', 'A', B, (40, 96)); d.p('f2', 'F', R, (62, 8))
b = d.newball(rec(d, 's', 0)); b2 = d.newball((200, 200))
t = d.pas(b, 0.4, rec(d, 'a', 1.2)); d.mv('f', 0.5, 2.2, (50, 42))                                       # försvararen startar när bollen lämnar foten
d.mv('a', t, t + 1.0, (56, 50)); d.carry(b, 'a', t, t + 1.0); t += 1.0
d.mv('a', t, t + 1.4, (66, 16)); d.carry(b, 'a', t, t + 1.4); d.mv('f', t, t + 1.4, (58, 24)); tp = t + 1.2   # driver över linjen
hide(d, b, t + 1.6)
d.mv('a', t + 1.6, t + 3.6, (62, 8)); d.mv('f', t + 1.6, t + 3.6, (40, 96))
d.mv('a2', t + 1.4, t + 2.8, (50, 72)); d.mv('f2', t + 1.4, t + 3.0, (50, 22))
show(d, b2, t + 3.1, rec(d, 's', t + 3.1)); t0 = t + 3.3
t = d.pas(b2, t0, rec(d, 'a2', t0 + 0.8)); d.mv('f2', t0 + 0.1, t + 0.6, (48, 56))
tw = win(d, b2, 'f2', 'a2', t + 0.8, 0.4)
d.mv('f2', tw, tw + 1.6, (44, 82)); d.carry(b2, 'f2', tw, tw + 1.6); tc = tw + 1.4                      # kontra över motsatt kortsida
d.mv('a2', tw, tw + 1.6, (50, 70))
fp = [(0, 'Bollhållaren spelar in', 'Försvararen startar när bollen lämnar foten.'),
      (1.6, 'Driv över försvararens linje', 'Ta yta med första touchen.'),
      (t0, 'Nästa par', ''),
      (tw - 0.2, 'Brytning – kontra direkt', 'Över motsatt kortsida. Spela tills bollen är ur spel.')]
finish(d, 'sd16', 'kontring-1-mot-1', ['Kontring', '1 mot 1'], 'Yta ca 15 × 12 m',
       fp, 'DUELL', [('box', 30, 20, 70, 80)], [lab(tp, tp + 1.6, (70, 26), '+1'), lab(tc, tc + 1.6, (36, 86), '+1')])

# ============ sd17 Spel i central tredjedel med kontring ============
d = Drill(); d.p('mvb', 'MV', B, (50, 96)); d.p('mvr', 'MV', R, (50, 4))
BP = [(26, 80), (50, 84), (74, 80), (36, 62), (64, 60), (50, 42)]; RP = [(34, 54), (66, 52), (50, 46), (40, 38), (60, 36), (50, 24)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
for k in (0, 1, 3, 4): wander(d, f'r{k}', 0, 3.0, boxes([RP[k]], 3)[0], 2000 + k, 1.6)
b = d.newball(rec(d, 'mvb', 0))
t = d.pas(b, 0.4, rec(d, 'b0', 1.1)); d.mv('r0', 1.0, 2.4, (30, 72))                                      # pressare lämnar mittzonen
t = d.pas(b, t + 0.3, rec(d, 'mvb', t + 1.0)); tb = t                                                   # spelbar bakåt
t = d.pas(b, t + 0.3, rec(d, 'b2', t + 1.1)); t = d.pas(b, t + 0.2, rec(d, 'b4', t + 0.9))
tl = win(d, b, 'r1', 'b4', t + 0.3)                                                                      # bollförlust
t = d.pas(b, tl + 0.2, rec(d, 'r2', tl + 0.9)); d.mv('r2', tl, t, (50, 60))
for k, ps in [(3, (46, 66)), (4, (58, 58)), (5, (52, 52))]: d.mv(f'b{k}', tl, t + 0.4, ps)               # återerövra
tw = win(d, b, 'b3', 'r2', t + 0.5, 0.6)
t = d.pas(b, tw + 0.3, rec(d, 'b5', tw + 1.0)); t = chain(d, b, t, ['b4'], 0.3)
fp = [(0, 'Laget med bollen startar från målvakten', 'Spelbart bakåt i första tredjedelen.'),
      (1.0, 'Kontringslaget får lämna mittzonen', 'För att pressa.'),
      (tl - 0.2, 'Bollförlust', 'Kontringslaget anfaller direkt.'),
      (tw - 0.2, 'Återerövra', 'Behåll bollen och vinn tillbaka den vid förlust.')]
finish(d, 'sd17', 'spel-i-central-tredjedel-med-kontring', ['Spel i central tredjedel', 'Med kontring'], '7 mot 7-plan i tre zoner',
       fp, 'SPELÖVNING', [('zone', 4, 34, 96, 66, (200, 220, 200), 'MITTZON')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ sd18 Väggspel – 5 mot 3 ============
d = Drill()
AP = [(20, 80), (80, 80), (20, 30), (80, 30), (50, 56)]; DP = [(32, 64), (68, 62), (50, 36)]
team(d, 'a', B, AP); team(d, 'f', R, DP)
b1 = d.newball(rec(d, 'a0', 0)); b2 = d.newball(rec(d, 'a1', 0))
t = drive(d, b1, 'a0', 0.4, (28, 70), 16); d.mv('f0', 0.4, t, (32, 62))
d.mv('a4', 0.6, t, (42, 66)); t = d.pas(b1, t + 0.1, rec(d, 'a4', t + 0.6))                              # vägg
d.mv('a0', t - 0.4, t + 0.8, (34, 52)); t = d.pas(b1, t + 0.1, rec(d, 'a0', t + 0.8)); tv1 = t
d.mv('a0', t, t + 1.4, (24, 34)); d.carry(b1, 'a0', t, t + 1.4); t += 1.4; t = d.pas(b1, t + 0.1, rec(d, 'a2', t + 0.8))
t0 = 2.0; t = drive(d, b2, 'a1', t0, (72, 70), 16); d.mv('f1', t0, t, (68, 60))
d.mv('a4', t - 0.6, t + 0.4, (58, 64)); t = d.pas(b2, t + 0.1, rec(d, 'a4', t + 0.6))
d.mv('a1', t - 0.4, t + 0.8, (66, 50)); t = d.pas(b2, t + 0.1, rec(d, 'a1', t + 0.8)); tv2 = t
d.mv('a1', t, t + 1.4, (76, 34)); d.carry(b2, 'a1', t, t + 1.4); t += 1.4; d.mv('f2', t - 1.4, t, (62, 36)); t = d.pas(b2, t + 0.1, rec(d, 'a3', t + 0.8))
t = drive(d, b2, 'a3', t, (60, 26), 14); t = d.pas(b2, t + 0.1, rec(d, 'a4', t + 1.0)); d.mv('a4', t - 1.6, t, (50, 50))
fp = [(0, 'Fem anfallare, tre försvarare, två bollar', 'Utmana försvararen.'),
      (tv1 - 0.8, 'Väggspel förbi försvararen', 'Spela när försvararen kliver på.'),
      (tv2 - 0.6, 'Samtidigt på andra sidan', ''),
      (tv2 + 1.4, 'Byt försvarare efter en stund', '')]
finish(d, 'sd18', 'vaggspel-5-mot-3', ['Väggspel', '5 mot 3'], 'Yta 30 × 20 m · Fem anfallare, tre försvarare och två bollar',
       fp, 'ÖVERLÄGE', [('box', 10, 20, 90, 90)])

# ============ sd19 Väggspel mot två mål ============
d = Drill()
AP = [(40, 84), (46, 90)]; BP = [(54, 16), (60, 10)]
team(d, 'a', B, AP, ['A', 'A']); d.p('va', 'V', B, (22, 50)); team(d, 'b', R, BP, ['B', 'B']); d.p('vb', 'V', R, (78, 50))
b = d.newball(rec(d, 'a0', 0))
t = drive(d, b, 'a0', 0.4, (36, 56), 18); d.mv('b0', 0.6, t, (40, 42))                                   # utmanar
d.mv('va', t - 0.6, t + 0.4, (26, 46)); t = d.pas(b, t + 0.1, rec(d, 'va', t + 0.6))
d.mv('a0', t - 0.4, t + 0.8, (42, 30)); t = d.pas(b, t + 0.1, rec(d, 'a0', t + 0.8)); tg = shoot(d, b, t + 0.1, (46, 1))   # efter väggspel
hide(d, b, tg + 0.4); d.mv('va', tg, tg + 2.0, (40, 92)); d.mv('a0', tg + 0.2, tg + 2.6, (30, 70))     # väggen ställer sig sist
b2 = d.newball((200, 200)); show(d, b2, tg + 0.8, rec(d, 'b1', tg + 0.8))
d.mv('a1', tg + 0.4, tg + 1.6, (44, 66))
t = drive(d, b2, 'b1', tg + 1.0, (58, 46), 18); d.mv('a1', tg + 1.6, t, (56, 56))
d.mv('b1', t, t + 1.2, (70, 62)); d.carry(b2, 'b1', t, t + 1.2); t += 1.2; tg2 = shoot(d, b2, t + 0.1, (54, 99))   # egen passering
fp = [(0, 'Lag A utmanar lag B', 'Avsluta efter väggspel eller egen passering.'),
      (tg - 1.2, 'Väggspel och avslut', ''),
      (tg + 0.8, 'Nu startar andra laget', 'Åt andra hållet. Väggen ställer sig sist.'),
      (tg2 - 0.8, 'Egen passering och avslut', 'Flest mål på bestämd tid vinner.')]
finish(d, 'sd19', 'vaggspel-mot-tva-mal', ['Väggspel', 'Mot två mål'], '30 m mellan två mål · Lag A mot lag B',
       fp, 'AVSLUT', [], [lab(tg, tg + 1.6, (46, 12), 'MÅL A'), lab(tg2, tg2 + 1.6, (54, 88), 'MÅL B')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

if __name__ == '__main__': render(C, sys.argv)
