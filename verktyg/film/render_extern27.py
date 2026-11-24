# Externa övningar, omgång 27 (tolv st). Regel: först d.mv, sedan d.carry; först mottagarens rörelse, sedan passningen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e9', __file__.replace('render_extern27.py', 'render_extern9.py'))
e9 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e9); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e9.finish, e9.rec, e9.chain, e9.wander, e9.counter, e9.arrivals
lab, hide, show, team, boxes, drive, shoot = e9.lab, e9.hide, e9.show, e9.team, e9.boxes, e9.drive, e9.shoot
factor, swap_color, stand, countdown, countup, win = e9.factor, e9.swap_color, e9.stand, e9.countdown, e9.countup, e9.win
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'

# ============ if18 Kanaler och inlägg ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96))
team(d, 'bk', B, [(8, 58), (92, 42)], ['K', 'K']); team(d, 'rk', R, [(8, 34), (92, 70)], ['K', 'K'])
BP = [(34, 66), (66, 64), (50, 50)]; RP = [(36, 34), (64, 36), (50, 60)]; team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b0', 0))
t = d.pas(b, 0.4, rec(d, 'b2', 1.1)); t = d.pas(b, t + 0.2, rec(d, 'bk1', t + 1.3)); tw = t                 # bred uppspelning
t = drive(d, b, 'bk1', t, (92, 14), 18)
for k, ps in enumerate([(44, 12), (58, 10), (50, 24)]): d.mv(f'b{k}', t - 2.2, t + 0.4, ps)
d.mv('r0', t - 1.8, t + 0.4, (46, 10)); d.mv('r1', t - 1.8, t + 0.4, (56, 14))
t = d.pas(b, t + 0.1, rec(d, 'b1', t + 1.0), 0.9); tg = shoot(d, b, t + 0.05, (54, 1))
fp = [(0, 'Två spelare per lag i kanalerna', 'Rotera varannan minut.'),
      (tw - 0.8, 'Bred uppspelning först', 'Sedan finns målchansen.'),
      (tg - 1.2, 'Inlägg', ''),
      (tg - 0.2, 'Mål efter inlägg: två poäng', 'Variant: försvarare får gå in i kanalen.')]
finish(d, 'if18', 'kanaler-och-inlagg', ['Kanaler och', 'inlägg'], 'Mittyta 27 × 46 m · Kanaler på 4,5 m',
       fp, 'SPELÖVNING', [('zone', 0, 4, 16, 96, (200, 220, 200), ''), ('zone', 84, 4, 100, 96, (200, 220, 200), '')], [lab(tg, tg + 1.8, (54, 14), '+2')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ gh01 Konditionsstafetter ============
d = Drill()
LX = [24, 50, 76]; COL = [B, R, YEL]
for li, x in enumerate(LX):
    for k in range(3): d.p(f'p{li}{k}', '', COL[li], (x, 86 + 5 * k))
KIND = ['LÖPNING', 'BAKLÄNGES', 'DRIBBLING']; ex = []
for li, x in enumerate(LX):
    t = 0.4 + 0.15 * li; bb = d.newball((200, 200))
    for k in range(3):
        pid = f'p{li}{k}'
        if k: d.mv(pid, t - 0.8, t, (x, 86))
        if k == 2: show(d, bb, t - 0.1, rec(d, pid, t))
        t2 = d.path(pid, t, [(x, 14)], 1.6 if k == 0 else 1.1); t3 = d.path(pid, t2, [(x + 4, 86)], 1.6 if k == 0 else 1.1)
        if k == 2: d.carry(bb, pid, t, t3)
        d.mv(pid, t3, t3 + 0.6, (x + 6, 96 - 5 * k)); t = t3 + 0.2
        if li == 0: ex.append(lab(t2 - 1.0, t2 + 0.6, (50, 6), KIND[k]))
fp = [(0, 'Lag om tre i varsin kanal', 'Stafett fram och tillbaka.'),
      (3.0, 'Vanlig löpning', ''),
      (7.0, 'Baklänges – sedan dribbling', 'Insidan, sidledsrullning, mountain climbers.'),
      (12.0, 'Räkna poäng', 'Eller låt varje lopp vara en egen vinst.')]
finish(d, 'gh01', 'konditionsstafetter', ['Konditions-', 'stafetter'], 'Rektangel 25–30 × 40–50 m · Lag om tre i varsin kanal',
       fp, 'STAFETT', [('cone', x, 14) for x in LX] + [('line', [(37, 10), (37, 92)]), ('line', [(63, 10), (63, 92)])], ex)

# ============ gh02 Finishing Wars ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96))
team(d, 'bd', B, [(30, 74), (50, 80), (70, 74)]); d.p('ba', 'A', B, (50, 28))
team(d, 'rd', R, [(30, 26), (50, 20), (70, 26)]); d.p('ra', 'A', R, (50, 72))
b = d.newball(rec(d, 'bd1', 0))
t = d.pas(b, 0.4, rec(d, 'bd0', 1.0)); d.mv('ba', t - 0.4, t + 0.6, (40, 34)); t = d.pas(b, t + 0.2, rec(d, 'ba', t + 1.4), 1.2)   # över mittlinjen – ingen spelare korsar
d.mv('rd0', t - 1.0, t, (36, 28)); t = d.pas(b, t + 0.1, rec(d, 'bd0', t + 1.4), 1.2)                       # läggning tillbaka
t = d.pas(b, t + 0.2, rec(d, 'ba', t + 1.4), 1.2); d.mv('ba', t - 1.4, t, (46, 22)); tg = shoot(d, b, t + 0.05, (54, 1))
fp = [(0, 'Tre försvarare och en anfallare', 'Två målvakter.'),
      (1.6, 'Ingen får korsa mittlinjen', ''),
      (tg - 2.2, 'Läggningar och kombinationer', 'Ger mest poäng.'),
      (tg - 0.3, 'Mål', 'Med ett tredje lag: spela till 5–6 mål och rotera.')]
finish(d, 'gh02', 'finishing-wars', ['Finishing', 'Wars'], 'Yta 25–30 × 30 m · Två mål · Mittlinje',
       fp, 'AVSLUT', [('line', [(4, 50), (96, 50)])])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ gh03 Passningscirkeln ============
d = Drill()
for side, sx in (('l', -1), ('r', 1)):
    d.p(f'{side}s', '', B, (50 + sx * 30, 84)); d.p(f'{side}m', '', B, (50 + sx * 10, 50)); d.p(f'{side}d', '', B, (50 + sx * 30, 16)); d.p(f'{side}q', '', B, (50 + sx * 38, 88))
for side, sx in (('l', -1), ('r', 1)):
    bb = d.newball(rec(d, f'{side}s', 0)); t = 0.4 + (0.4 if sx > 0 else 0)
    for rep in range(1):
        run, mid, dp = f'{side}s', f'{side}m', f'{side}d'
        d.mv(run, t, t + 1.2, (50 + sx * 18, 60)); t1 = d.pas(bb, t, rec(d, mid, t + 1.0))                        # löparen mot mittkonen
        t2 = d.pas(bb, t1 + 0.1, rec(d, run, t1 + 0.8))                                                          # vägg
        d.mv(run, t2, t2 + 1.6, (50 + sx * 30, 26)); t3 = d.pas(bb, t2 + 0.1, rec(d, dp, t2 + 1.0))
        d.mv(mid, t2, t2 + 1.4, (50 + sx * 22, 40))                                                             # överlappar
        t4 = d.pas(bb, t3 + 0.2, rec(d, mid, t3 + 0.9)); d.mv(f'{side}q', t4 - 0.4, t4 + 1.4, (50 + sx * 30, 84)); t5 = d.pas(bb, t4 + 0.2, rec(d, f'{side}q', t4 + 1.6), 1.4)
        d.mv(dp, t3 + 0.4, t5 + 1.0, (50 + sx * 38, 88))
        d.mv(mid, t4 + 0.3, t5 + 1.4, (50 + sx * 10, 50)); d.mv(run, t3, t5 + 1.0, (50 + sx * 30, 16))
        t = t5 + 0.6
fp = [(0, 'Två speglade halvor', 'Åtta koner, två bollar.'),
      (1.4, 'Löparen mot mittkonen – vägg', 'Ett touch där det går.'),
      (3.2, 'Diagonal passning och överlapp', 'Följ din passning.'),
      (8.0, 'Kör i tio minuter', 'Ursprungligen NC Courages uppvärmning.')]
finish(d, 'gh03', 'passningscirkeln-nc-courage', ['Passningscirkeln', 'Från NC Courage'], 'Ruta 22 × 15 m · Åtta koner · Två bollar',
       fp, 'PASSNINGSÖVNING', [('cone', 20, 84), ('cone', 80, 84), ('cone', 40, 50), ('cone', 60, 50), ('cone', 20, 16), ('cone', 80, 16), ('cone', 12, 88), ('cone', 88, 88)])

# ============ gh04 Passnings- och kommunikationsrutan ============
d = Drill()
OUT = [(10, 30), (10, 70), (30, 90), (70, 90), (90, 70), (90, 30), (70, 10), (30, 10)]
IN = [(38, 40), (62, 40), (40, 62), (60, 62)]
for k, ps in enumerate(OUT): d.p(f'o{k}', '', ORA, ps)
for k, ps in enumerate(IN): d.p(f'i{k}', '', B, ps)
for k in range(4):
    wander(d, f'i{k}', 0, 17.9, boxes([IN[k]], 9)[0], 7300 + k, 1.5)
    bb = d.newball(rec(d, f'i{k}', 0)); t = 0.4 + 0.3 * k; o = (2 * k) % 8
    for rep in range(6):
        t = d.pas(bb, t + 0.6, rec(d, f'o{o}', t + 1.4)); t = d.pas(bb, t + 0.2, rec(d, f'i{k}', t + 1.1)); o = (o + 3) % 8   # få tillbaka – vänd – nästa
fp = [(0, 'Hälften inne med var sin boll', 'Hälften runt rutan.'),
      (1.6, 'Passa till en ledig ytterspelare', 'Få tillbaka och vänd.'),
      (6.0, 'Hitta nästa', 'Prata – ropa på bollen.'),
      (12.0, 'Byt roller var tredje minut', 'Variant: dribbla genom en innerruta först.')]
finish(d, 'gh04', 'passnings-och-kommunikationsrutan', ['Passnings- och', 'kommunikationsrutan'], 'Ruta 10 × 10 m upp till 15–20 m',
       fp, 'PASSNINGSÖVNING', [('box', 18, 18, 82, 82)])

# ============ gh05 Passningstriangeln ============
d = Drill()
TRI = [(50, 16), (82, 76), (18, 76)]
DEF = [((TRI[i][0] + TRI[(i + 1) % 3][0]) / 2, (TRI[i][1] + TRI[(i + 1) % 3][1]) / 2) for i in range(3)]
d.p('a0', 'A', B, (50, 10)); d.p('a1', 'A', B, (44, 8)); d.p('b0', 'B', B, (88, 78)); d.p('c0', 'C', B, (12, 78))
occ = {0: ['a0', 'a1'], 1: ['b0'], 2: ['c0']}
QO = {0: (0, -5), 1: (5, 2), 2: (-5, 2)}
def qp(c, n): x, y = TRI[c]; return (x + QO[c][0] * (1 + n), y + QO[c][1] * (1 + n))
b = d.newball(rec(d, 'a0', 0)); t = 0.4; c = 0; flip = None
for rep in range(8):
    step = -1 if rep < 4 else 1
    if rep == 4: flip = t
    nc = (c + step) % 3; p = occ[c].pop(0); r = occ[nc][0]
    t1 = d.pas(b, t, rec(d, r, t + 1.3), 1.1)                                                               # på utsidan av konen
    d.mv(p, t + 0.3, t1 + 1.4, qp(nc, len(occ[nc]))); occ[nc].append(p)
    for n, w in enumerate(occ[c]): d.mv(w, t + 0.4, t + 1.0, qp(c, n))
    t = t1 + 0.3; c = nc
fp = [(0, 'Passa på utsidan av konerna', 'Konerna är försvarare.'),
      (1.6, 'Moturs i fem minuter', 'Följ passningen.'),
      (flip, 'Sedan medurs', ''),
      (flip + 3.0, 'Progression: väggspel på vägen', 'B spelar tillbaka direkt.')]
finish(d, 'gh05', 'passningstriangeln', ['Passnings-', 'triangeln'], 'Triangel med 15 m sidor · 4–5 spelare',
       fp, 'PASSNINGSÖVNING', [('cone',) + c for c in TRI] + [('redcone',) + dd for dd in DEF], [lab(flip, flip + 1.6, (50, 50), 'MEDURS')])

# ============ gh06 Power och finess ============
d = Drill(); d.p('mv', 'MV', R, (50, 4)); d.p('t', 'T', T_COL, (50, 70))
team(d, 'b', B, [(34, 46), (34, 52)], ['', '']); team(d, 'r', R, [(66, 46), (66, 52)], ['', ''])
t = 0.4; ex = []
for k, (pid, sx) in enumerate([('b0', -1), ('r0', 1), ('b1', -1)]):
    bl = d.newball((200, 200)); show(d, bl, t, rec(d, 't', t))
    d.mv(pid, t, t + 0.6, (50 + sx * 12, 40)); t1 = d.pas(bl, t + 0.1, rec(d, pid, t + 0.9))
    tg = shoot(d, bl, t1 + 0.05, (50 - sx * 4, 1)); hide(d, bl, tg + 0.3); ex.append(lab(tg, tg + 1.0, (76, 14), 'LÅNGSKOTT'))   # långskott på ett touch
    b2 = d.newball((200, 200)); show(d, b2, tg + 0.4, rec(d, 't', tg + 0.4))
    d.mv(pid, tg, tg + 1.0, (50 + sx * 6, 18)); t2 = d.pas(b2, tg + 0.5, rec(d, pid, tg + 1.3), 0.8)            # avslut i boxen på ett touch
    tg2 = shoot(d, b2, t2 + 0.05, (50 + sx * 5, 1)); hide(d, b2, tg2 + 0.3); ex.append(lab(tg2, tg2 + 1.0, (76, 14), 'FINESS'))
    d.mv(pid, tg2 + 0.2, tg2 + 2.2, (50 + sx * 16, 60 + 6 * k)); t = tg2 + 0.4
fp = [(0, 'Tränaren rullar bollen med fart', 'Två lag i led.'),
      (1.2, 'Långskott på ett touch', 'Power.'),
      (ex[1]['t0'] - 1.0, 'Sedan avslut i boxen på ett touch', 'Finess.'),
      (t - 1.0, 'Flest mål vinner', 'Rotera målvakter efter varje match.')]
finish(d, 'gh06', 'power-och-finess', ['Power och', 'finess'], 'Två koner 25–30 m från mål · Målvakt',
       fp, 'AVSLUT', [('cone', 30, 40), ('cone', 70, 40)], ex)
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ gh07 Rondolagen ============
d = Drill()
BP = [(14, 14), (40, 12), (60, 16), (86, 14), (30, 36), (70, 38)]; RP = [(14, 86), (40, 88), (60, 84), (86, 86), (30, 64), (70, 62)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
for k in range(6): wander(d, f'b{k}', 0, 17.9, boxes([BP[k]], 4)[0], 7400 + k, 1.6)
b = d.newball(rec(d, 'b0', 0))
d.mv('r4', 0.4, 2.0, (34, 26)); d.mv('r5', 0.4, 2.0, (64, 28))                                              # två pressare in
t = chain(d, b, 0.4, ['b1', 'b4', 'b2', 'b5'], 0.3)
tw = win(d, b, 'r5', 'b5', t + 0.3, 0.6); t = d.pas(b, tw + 0.2, rec(d, 'r2', tw + 1.6), 1.4); to = t          # snabbt till de egna
d.mv('r5', tw + 0.4, tw + 2.4, (70, 62)); d.mv('r4', tw + 0.4, tw + 2.4, (30, 64))
d.mv('b4', to - 0.4, to + 1.4, (34, 74)); d.mv('b5', to - 0.4, to + 1.4, (64, 72))                              # nu skickar blått in två
t = chain(d, b, to, ['r0', 'r3', 'r1'], 0.3)
fp = [(0, 'Laget utan boll skickar in två pressare', 'Två lag i var sin halva.'),
      (tw - 0.3, 'Pressarna vinner bollen', ''),
      (to - 1.0, 'Snabbt till de egna i andra halvan', ''),
      (to + 0.4, 'Nu skickar blått in två', 'Variant: neutral zon på 5 m i mitten.')]
finish(d, 'gh07', 'rondolagen', ['Rondo-', 'lagen'], 'Yta 20 × 30 m delad i två halvor',
       fp, 'RONDO', [('box', 6, 4, 94, 96), ('line', [(6, 50), (94, 50)])])

# ============ gh08 Stjärnskottet ============
d = Drill(); d.p('mv', 'MV', R, (50, 4)); d.p('s', 'S', B, (50, 34))
ST = [ring_pos(50, 40, 26, i, 5, a0=90) for i in range(5)]
for k, ps in enumerate(ST): d.p(f'k{k}', str(k + 1), ORA, ps)
t = 0.4
for k in range(5):
    bl = d.newball(rec(d, f'k{k}', 0)); d.carry(bl, f'k{k}', 0, t)
    t1 = d.pas(bl, t, rec(d, 's', t + 0.9)); d.mv('s', t1, t1 + 0.4, (50 + (2 if k % 2 else -2), 32)); d.carry(bl, 's', t1, t1 + 0.4)   # ta emot, vänd
    tg = shoot(d, bl, t1 + 0.45, (44 + 3 * k, 1)); hide(d, bl, tg + 0.3); t = tg + 0.3
fp = [(0, 'Skytten i rutan', 'Fem koner i en stjärna runt den.'),
      (1.2, 'Passning från kon 1', 'Ta emot, vänd och skjut.'),
      (5.0, 'Kon 2, 3, 4 och 5 i tur och ordning', 'Så snabbt som möjligt.'),
      (t - 1.0, 'Byt skytt efter ett varv', '')]
finish(d, 'gh08', 'stjarnskottet', ['Stjärn-', 'skottet'], 'Skottruta 5 × 5 m · Fem koner i en stjärna',
       fp, 'AVSLUT', [('box', 42, 28, 58, 42)])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ gh09 World Cuppies ============
d = Drill(); d.p('mv', 'MV', R, (50, 4)); d.p('t', 'T', T_COL, (50, 90))
COLS = [B, ORA, YEL]; PTS = [[(30, 50), (38, 56)], [(62, 48), (70, 56)], [(44, 70), (56, 72)]]
for g in range(3):
    for k in range(2): d.p(f'g{g}{k}', '', COLS[g], PTS[g][k])
bl = d.newball(rec(d, 't', 0))
t = d.pas(bl, 0.6, (50, 40), 1.0)
d.mv('g00', 0.8, t, (48, 42)); d.mv('g10', 0.8, t, (54, 40)); d.mv('g20', 0.8, t + 0.2, (50, 46))
d.carry(bl, 'g00', t, t + 0.2); t = d.pas(bl, t + 0.3, rec(d, 'g01', t + 1.0)); d.mv('g01', t - 1.0, t, (36, 34))
tg = shoot(d, bl, t + 0.1, (44, 1)); hide(d, bl, tg + 0.3)                                                 # mål – laget går vidare
for k in range(2): d.mv(f'g0{k}', tg + 0.2, tg + 2.2, (8, 30 + 6 * k))
bl2 = d.newball((200, 200)); show(d, bl2, tg + 1.0, rec(d, 't', tg + 1.0))
t = d.pas(bl2, tg + 1.2, (52, 42), 1.0); d.mv('g11', tg + 1.2, t, (56, 44)); d.mv('g21', tg + 1.2, t + 0.2, (50, 48))
d.carry(bl2, 'g11', t, t + 0.4); d.mv('g11', t, t + 1.0, (58, 30)); d.carry(bl2, 'g11', t + 0.4, t + 1.0); tg2 = shoot(d, bl2, t + 1.1, (56, 1))
d.mv('g20', tg2 + 0.2, tg2 + 2.4, (92, 70)); d.mv('g21', tg2 + 0.2, tg2 + 2.4, (92, 76))                       # laget utan mål åker ut
fp = [(0, 'Lag om två eller tre – varje lag ett land', ''),
      (0.8, 'Tränaren kastar in en boll', 'Alla mot alla.'),
      (tg - 0.4, 'Mål – laget går vidare', ''),
      (tg2 + 0.2, 'Laget utan mål åker ut', 'Med två bollar blir det snabbare.')]
finish(d, 'gh09', 'world-cuppies-alla-mot-alla', ['World Cuppies', 'Alla mot alla'], 'Halvplan · Ett mål och målvakt · Båge där man inte får skjuta',
       fp, 'LEK', [('circle', 50, 4, 3.6)], [lab(tg, tg + 1.6, (20, 22), 'VIDARE'), lab(tg2 + 0.4, tg2 + 2.0, (80, 64), 'UTSLAGET')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ ff01 Rånare och dribblare ============
d = Drill(); d.p('t', 'T', T_COL, (50, 95))
ST = [(22, 24), (50, 20), (78, 26), (24, 72), (50, 78), (76, 72)]
for k, ps in enumerate(ST): d.p(f'd{k}', '', B, ps)
team(d, 'r', R, [(40, 50), (62, 50)], ['', ''])
balls = [d.newball(rec(d, f'd{k}', 0)) for k in range(6)]
for k in (1, 3, 4, 5): wander(d, f'd{k}', 0, 17.9, boxes([ST[k]], 7)[0], 7500 + k, 1.6); d.carry(balls[k], f'd{k}', 0, 17.9)
tsig = 1.2
d.mv('d0', 0, 3.0, (28, 34)); d.carry(balls[0], 'd0', 0, 3.0); d.mv('r0', tsig, 3.0, (32, 38))
tw = d.pas(balls[0], 3.2, rec(d, 'r0', 3.4), 0.3)                                                          # rånaren vinner – blir dribblare
wander(d, 'r0', tw, 17.9, boxes([ST[0]], 7)[0], 7510, 1.6); d.carry(balls[0], 'r0', tw, 17.9)
d.mv('d0', tw, 5.8, (66, 40)); d.mv('d2', 0, 5.6, (72, 36)); d.carry(balls[2], 'd2', 0, 5.8)
tw2 = d.pas(balls[2], 6.0, rec(d, 'd0', 6.2), 0.3)                                                          # den nya rånaren vinner
wander(d, 'd0', tw2, 17.9, boxes([ST[2]], 7)[0], 7511, 1.6); d.carry(balls[2], 'd0', tw2, 17.9)
wander(d, 'd2', tw2 + 0.2, 17.9, (44, 40, 60, 60), 7512, 1.6); wander(d, 'r1', tsig, 17.9, (54, 42, 70, 60), 7513, 1.6)
fp = [(0, 'Dribblarna sprider ut sig', 'Rånarna börjar utan boll.'),
      (tsig, 'Signal – rånarna försöker vinna en boll', ''),
      (tw - 0.2, 'Vinner du bollen blir du dribblare', 'Den som tappade blir rånare.'),
      (12.0, '”Tid!” – den som har boll vinner', '')]
finish(d, 'ff01', 'ranare-och-dribblare', ['Rånare och', 'dribblare'], 'Avgränsad yta',
       fp, 'LEK MED BOLL', [('box', 10, 10, 90, 88)], [lab(tsig - 0.2, tsig + 1.2, (50, 50), 'SIGNAL'), lab(15.0, 17.4, (50, 50), '”TID!”')])
f = factor(fp); ids = {k: i for i, k in enumerate(d.order)}
swap_color(ids['d0'], (tw + 0.3) * f, B, R); swap_color(ids['r0'], (tw + 0.3) * f, R, B)
C[-1]['players'][ids['d0']]['color'] = (lambda tt, a=(tw + 0.3) * f, c=(tw2 + 0.3) * f: B if tt < a else (R if tt < c else B))
swap_color(ids['d2'], (tw2 + 0.3) * f, B, R)

# ============ ff02 Mål överallt ============
d = Drill()
GL = [(50, 10), (90, 50), (50, 90), (10, 50)]
ST = [(30, 30), (70, 30), (30, 70), (70, 70)]
for k, ps in enumerate(ST): d.p(f'p{k}', '', B, ps)
d.p('f', 'F', R, (50, 50))
balls = [d.newball(rec(d, f'p{k}', 0)) for k in range(4)]; ex = []
ROUTE = {0: [0, 3, 0], 1: [1, 0, 1], 2: [2, 1, 2], 3: [3, 2, 3]}
for k in range(4):
    t = 0.4 + 0.3 * k; pid = f'p{k}'
    for gi in ROUTE[k]:
        gx, gy = GL[gi]; ax, ay = 50 + (gx - 50) * 0.55 + (6 if k % 2 else -6), 50 + (gy - 50) * 0.55 + (6 if k > 1 else -6)
        t1 = d.path(pid, t, [(ax, ay)], 1.3); d.carry(balls[k], pid, t, t1)
        tg = d.pas(balls[k], t1 + 0.1, (gx, gy), 0.5); d.mv(pid, tg, tg + 1.0, (ax + (gx - ax) * 0.4, ay + (gy - ay) * 0.4))
        t2 = d.pas(balls[k], tg + 0.2, rec(d, pid, tg + 1.2), 0.9); t = t2 + 0.1   # hämta bollen
        if k == 0: ex.append(lab(tg, tg + 1.0, (gx, gy + (8 if gy < 50 else -8) if gx == 50 else gy), 'MÅL'))
wander(d, 'f', 6.0, 17.9, (40, 40, 60, 60), 7600, 1.4)
fp = [(0, 'Gör så många mål som möjligt', 'Fyra mål.'),
      (2.4, 'Inte i samma mål två gånger i rad', ''),
      (6.0, 'Lägg till en försvarare', 'Sedan en till.'),
      (12.0, 'Variant: varannan har boll', 'De andra försöker vinna en.')]
finish(d, 'ff02', 'mal-overallt', ['Mål', 'överallt'], 'Yta med fyra mål',
       fp, 'SMÅLAGSSPEL', [('box', 6, 6, 94, 94)] + [('smallgoal',) + g for g in GL], ex)

if __name__ == '__main__': render(C, sys.argv)
