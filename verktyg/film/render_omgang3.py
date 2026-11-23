# Omgång 3: tolv av Sams egna övningar, byggda steg för steg efter instruktionen.
import importlib.util, sys, math as _m, random
from film_hjalp import *
spec = importlib.util.spec_from_file_location('o2', __file__.replace('render_omgang3.py', 'render_omgang2.py'))
o2 = importlib.util.module_from_spec(spec); sys.argv_backup = sys.argv; sys.argv = ['x', 'NONE']; spec.loader.exec_module(o2); sys.argv = sys.argv_backup
finish = o2.finish
C.clear()
WHITE = '#f3f5ef'

def rec(d, pid, t):
    x, y = at(d.pl[pid]['tr'], t); return (x + 1.8, y - 1.2)
def chain(d, b, t, ids, gap=0.3):
    for pid in ids:
        t = d.pas(b, t + gap, rec(d, pid, t + gap + 0.6))
    return t
def wander(d, pid, t0, t1, box, seed, step=2.2):
    rnd = random.Random(seed); x1, y1, x2, y2 = box; t = t0
    while t < t1 - 0.3:
        nt = min(t1, t + step); cx, cy = d.pos(pid)
        nx = min(x2, max(x1, cx + rnd.uniform(-7, 7))); ny = min(y2, max(y1, cy + rnd.uniform(-6, 6)))
        d.mv(pid, t, nt, (nx, ny)); t = nt
def counter(times, pos=(50, 11), last='+1 POÄNG'):
    ex = []
    for i, t in enumerate(times):
        t1 = times[i + 1] if i + 1 < len(times) else t + 2.2
        ex.append(dict(kind='label', t0=t, t1=t1, pos=pos, text=(str(i + 1) if i < len(times) - 1 or not last else last)))
    return ex
def arrivals(d, b):
    """Tider då bollen når en mottagare (för räknaren)."""
    tr = d.balls[b]; return [tr[i][0] for i in range(1, len(tr)) if tr[i][0] != tr[i - 1][0] and tr[i][1] != tr[i - 1][1]]

BOX = (10, 16, 90, 84)

# ============ t47 Possession med 3 lag – hörnor ============
d = Drill()
inner = (16, 22, 84, 78)
for k, ps in enumerate([(30, 34), (60, 30), (70, 60), (36, 64)]): d.p(f'b{k}', str(k + 1), B, ps)
for k, ps in enumerate([(44, 44), (56, 48), (48, 58), (40, 52)]): d.p(f'r{k}', str(k + 1), R, ps)
for k, ps in enumerate([(11, 17), (89, 17), (89, 83), (11, 83)]): d.p(f'n{k}', 'N', G, ps)
for k in range(4): wander(d, f'b{k}', 0, 18, inner, k); wander(d, f'r{k}', 0, 18, inner, 10 + k, 1.6)
b = d.newball(rec(d, 'b0', 0)); t0 = 0.5
t = chain(d, b, t0, ['b1', 'b2', 'b3', 'b0', 'b1', 'b2'])           # sex passningar i rad
cnt = arrivals(d, b)[:6]
t = d.pas(b, t + 0.3, (88, 81)); tp = t                              # till neutral i hörnet
t = d.pas(b, t + 0.4, rec(d, 'b2', t + 1.0))                          # tillbaka = poäng
tpoint = t
t = chain(d, b, t, ['b3', 'b0'])
t2 = d.pas(b, t + 0.3, rec(d, 'r1', t + 0.9))                         # rött bryter
extras = counter(cnt + [tpoint]) + [dict(kind='label', t0=tpoint + 2.3, t1=tpoint + 4.5, pos=(50, 11), text='RÄKNINGEN BÖRJAR OM')]
finish(d, 't47', 'possession-med-3-lag-hornor', ['Possession med tre lag', 'Neutrala i hörnen'], 'Kvadrat · Två lag i mitten · En neutral spelare i varje hörn',
       [(0, 'Lagen försöker behålla bollen', 'Gör planen stor. Räkna högt tillsammans.'),
        (cnt[5] - 0.2, 'Sex passningar i rad', 'Nu kan laget spela till en neutral i ett hörn.'),
        (tp - 0.6, 'Till hörnet och tillbaka ger en poäng', 'Använd hörnspelarna för att lätta på pressen.'),
        (tpoint + 0.6, 'Spelet fortsätter – räkningen börjar om', 'Först till tre poäng vinner.')],
       'SPELUPPBYGGNAD', [('box', 12, 18, 88, 82)], extras)

# ============ t48 Possession med konportar längs kanterna ============
d = Drill()
GATES = [(50, 23), (50, 77), (19, 50), (81, 50)]
for k, ps in enumerate([(30, 34), (62, 32), (68, 62), (34, 66)]): d.p(f'b{k}', str(k + 1), B, ps)
for k, ps in enumerate([(44, 42), (56, 46), (50, 58), (42, 54)]): d.p(f'r{k}', str(k + 1), R, ps)
for k in range(4): wander(d, f'b{k}', 0, 9, (26, 30, 74, 70), k); wander(d, f'r{k}', 0, 18, (26, 30, 74, 70), 20 + k, 1.6)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b1', 'b2', 'b3', 'b0', 'b1', 'b2']); cnt = arrivals(d, b)[:6]
d.mv('b1', t - 1.2, t + 1.0, (85, 46))                                 # löper mot ledig port
t = d.pas(b, t + 0.3, (86.8, 44.8)); tpoint = t                        # genom porten i löpningen
d.mv('b0', 9, 12, (60, 40)); d.mv('b3', 9, 12, (64, 60)); d.mv('b2', t, t + 2, (70, 56))
t = chain(d, b, t + 0.3, ['b2', 'b0'])
finish(d, 't48', 'possession-med-konportar-langs-kanterna', ['Possession med konportar', 'Längs kanterna'], 'Kvadrat · Konportar en bit innanför kanterna · Två lag',
       [(0, 'Två lag spelar mot varandra', 'Räkna passningarna i rad.'),
        (cnt[5] - 0.2, 'Sex passningar i rad', 'Nu får laget spela genom en konport till en lagkamrat.'),
        (cnt[5] + 0.3, 'Rör dig mot en ledig port', 'Passningen genom porten i lagkamratens löpning.'),
        (tpoint + 0.4, 'En poäng – räkningen börjar om', 'Byt sida när en port är stängd. Först till tre poäng vinner.')],
       'SPELUPPBYGGNAD', [('box', 10, 16, 90, 84)] + [('cone', x + (0 if y in (23, 77) else 0), y + dd) if x in (19, 81) else ('cone', x + dd, y) for x, y in GATES for dd in (-5, 5)],
       counter(cnt + [tpoint]))

# ============ t49 Possession med avslut ============
d = Drill()
for k, ps in enumerate([(30, 42), (62, 40), (68, 58), (36, 60)]): d.p(f'b{k}', str(k + 1), B, ps)
for k, ps in enumerate([(44, 46), (56, 50), (50, 56), (42, 54)]): d.p(f'r{k}', str(k + 1), R, ps)
d.p('ba', 'A', B, (50, 20)); d.p('ra', 'A', R, (50, 80)); d.p('mv1', 'MV', G, (50, 5)); d.p('mv2', 'MV', G, (50, 95))
for k in range(4): wander(d, f'b{k}', 0, 8, (24, 38, 76, 62), k); wander(d, f'r{k}', 0, 8, (24, 38, 76, 62), 30 + k, 1.6)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b1', 'b2', 'b3', 'b0', 'b1', 'b2']); cnt = arrivals(d, b)[:6]
d.mv('ba', t - 1, t + 0.6, (44, 24)); t = d.pas(b, t + 0.3, (45.8, 22.8)); tout = t     # till anfallaren
d.mv('b2', tout - 0.6, tout + 2.0, (58, 22))                                            # extra spelare följer med
d.mv('r1', tout - 0.2, tout + 2.2, (54, 20))                                            # en försvarare får följa med
t = d.pas(b, t + 0.9, (58, 21.2)); t = d.pas(b, t + 0.2, (54, -1), 0.5); d.mv('mv1', t - 0.5, t, (53, 5))
finish(d, 't49', 'possession-med-avslut', ['Possession med avslut', 'Keep away i mitten'], 'Mittzon för bollinnehav · Ytterzoner med mål · En anfallare per lag',
       [(0, 'Bollen startar i mitten', 'Lagen spelar keep away. Varje lag har en anfallare i ytterzonen.'),
        (cnt[5] - 0.2, 'Sex passningar i rad', 'Nu får laget spela till sin anfallare i ytterzonen.'),
        (tout, 'En extra spelare följer med', 'Löp direkt efter passningen. Försvararna får följa med en spelare.'),
        (tout + 1.4, 'Avsluta snabbt', 'Innan försvaret hinner tillbaka.')],
       'SPELUPPBYGGNAD', [('zone', 4, 34, 96, 66, (200, 220, 200), 'MITTZON')], counter(cnt + [tout], pos=(80, 30), last='UT!'))
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ t50 Uppbyggnad 6 mot 5 till tre småmål ============
d = Drill()
blue6 = [(18, 84), (38, 88), (62, 88), (82, 84), (40, 66), (60, 66)]
for k, ps in enumerate(blue6): d.p(f'b{k}', str(k + 1), B, ps)
for k, ps in enumerate([(26, 72), (44, 76), (60, 76), (74, 72), (50, 58)]): d.p(f'w{k}', str(k + 1), WHITE, ps)
for k, ps in enumerate([(22, 36), (42, 30), (58, 30), (78, 36)]): d.p(f'a{k}', str(k + 7), B, ps)
for k, ps in enumerate([(26, 42), (44, 40), (56, 40), (74, 42)]): d.p(f'd{k}', str(k + 6), WHITE, ps)
d.p('mv', 'MV', G, (50, 96))
b = d.newball(rec(d, 'b1', 0))
d.mv('w1', 0.5, 2, (40, 82)); d.mv('w4', 1, 3, (44, 64))
t = chain(d, b, 0.4, ['b2', 'b3', 'b5'])                                  # hitta den fria spelaren
d.mv('a2', t - 1.2, t + 0.4, (60, 46)); d.mv('d2', t - 1, t + 0.8, (58, 42))
t = d.pas(b, t + 0.3, (61.8, 44.8)); tin = t                             # in i fötterna mellan linjerna
d.mv('a2', t + 0.1, t + 1.6, (64, 30)); d.carry(b, 'a2', t + 0.1, t + 1.6)    # vänder och anfaller
d.mv('a3', t, t + 1.8, (78, 22)); t = d.pas(b, t + 1.9, rec(d, 'a3', t + 2.6))
t = d.pas(b, t + 0.4, (80, 8), 0.5); tg = t
b2 = d.newball((200, 200)); d.balls[b2] = [(0, (200, 200)), (tg + 0.8, (200, 200)), (tg + 0.81, rec(d, 'b4', tg + 0.8))]
d.mv('w4', tg + 0.6, tg + 1.4, (42, 64)); t3 = d.pas(b2, tg + 1.2, rec(d, 'w4', tg + 1.6), 0.4)
d.carry(b2, 'w4', t3, t3 + 1.6); d.mv('w4', t3, t3 + 1.6, (46, 82)); d.pas(b2, t3 + 1.7, (48, 101), 0.5)
finish(d, 't50', 'uppbyggnad-6-mot-5-till-tre-smamal', ['Uppbyggnad 6 mot 5', 'Till tre småmål'], 'Uppbyggnadszon 6 mot 5 · Anfallszon 4 mot 4 med tre småmål',
       [(0, 'Blått bygger upp 6 mot 5', 'Backlinjen och två mittfältare mot fem vita.'),
        (1.6, 'Hitta den fria spelaren', 'Flytta bollen tills någon är fri.'),
        (tin - 0.6, 'Spela in i fötterna mellan linjerna', 'Till anfallarna i nästa zon.'),
        (tin + 0.3, 'Anfallarna vänder och anfaller direkt', 'Mål i något av de tre småmålen.'),
        (tg + 0.8, 'Vinner vitt bollen anfaller de stora målet', 'Byt roller efter 6 minuter.')],
       'SPELUPPBYGGNAD', [('line', [(0, 50), (100, 50)]), ('smallgoal', 20, 4), ('smallgoal', 50, 4), ('smallgoal', 80, 4)])
C[-1]['goals'] = [(50, 100)]; C[-1]['keep_goals'] = True

# ============ t51 Possession 8 mot 8 + 1 joker ============
d = Drill()
bl = [(16, 22), (40, 20), (66, 20), (86, 26), (14, 76), (40, 80), (64, 80), (86, 74)]
rd = [(30, 34), (52, 32), (72, 38), (28, 52), (72, 56), (30, 66), (50, 68), (68, 66)]
for k, ps in enumerate(bl): d.p(f'b{k}', str(k + 1), B, ps)
for k, ps in enumerate(rd): d.p(f'r{k}', str(k + 1), R, ps)
d.p('j', 'J', G, (50, 50))
for k in range(8): wander(d, f'b{k}', 0, 8, (12, 18, 88, 82), 40 + k, 2.6); wander(d, f'r{k}', 0, 8, (22, 28, 78, 72), 50 + k, 2.6)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b1', 'j', 'b3', 'b7', 'j', 'b5']); tl = t
d.mv('r5', t - 1, t, (38, 78)); t = d.pas(b, t + 0.3, rec(d, 'r5', t + 0.8), 0.4); tw = t          # rött vinner
for k in [4, 5, 6, 0]: d.mv(f'b{k}', tw, tw + 1.6, (36 + k, 72 - k))                               # aggressiv press fem sekunder
t = chain(d, b, t, ['r3', 'j', 'r1', 'r2'], 0.25)
for k in range(8): d.mv(f'b{k}', tw + 5, tw + 7, [(30, 30), (50, 28), (70, 30), (78, 50), (22, 50), (32, 68), (50, 70), (68, 68)][k])   # försvar i zon
finish(d, 't51', 'possession-8-mot-8-plus-1-joker', ['Possession 8 mot 8', 'Plus en joker'], 'Rektangel · Två lag om åtta · Jokern i mitten spelar med bollen',
       [(0, 'Håll bollen med max två touch', 'Jokern är pivot i mitten. Det blir 9 mot 8 i anfall.'),
        (2.5, 'Gör planen stor', 'Samlas inte i mitten.'),
        (tw - 0.3, 'Rött vinner bollen', 'De blir anfallande direkt, utan att spelet stannar.'),
        (tw + 0.4, 'Blått pressar aggressivt i fem sekunder', 'Försvara inifrån och ut, tvinga spelet till kanten.'),
        (tw + 5, 'Ingen bollvinst – försvara i zon', 'Laget flyttar ut och står kompakt.')],
       'SPELUPPBYGGNAD', [('box', 10, 16, 90, 84)], [dict(kind='label', t0=tw + 0.4 + i, t1=tw + 1.4 + i, pos=(50, 11), text=f'PRESS {5 - i}') for i in range(5)])

# ============ t52 Possession 4 mot 4 + 3 (två rutor och mittcirkel) ============
d = Drill()
for k, ps in enumerate([(30, 30), (30, 70), (52, 26), (60, 70)]): d.p(f'b{k}', str(k + 1), B, ps)
for k, ps in enumerate([(40, 40), (40, 60), (60, 42), (62, 58)]): d.p(f'r{k}', str(k + 1), R, ps)
d.p('em', 'E', G, (50, 50)); d.p('eo1', 'E', G, (50, 10)); d.p('eo2', 'E', G, (50, 90))
b = d.newball(rec(d, 'b0', 0))
d.mv('b0', 0.4, 2.2, (18, 46)); d.carry(b, 'b0', 0.4, 2.2); ta = 2.2                 # dribbla in i vänster ruta
d.mv('r0', 0.5, 2.4, (26, 44))
t = d.pas(b, ta + 0.3, (51.8, 11.2)); t = d.pas(b, t + 0.3, rec(d, 'em', t + 0.8))   # extra spelare utanför, in i cirkeln
tc = t
d.mv('b3', tc - 1.6, tc + 0.4, (78, 52)); t = d.pas(b, t + 0.4, (79.8, 50.8)); tr_ = t  # in i höger ruta = från ruta till motsatt
d.mv('r3', tr_ - 1.2, tr_ + 0.4, (78, 56)); t2 = d.pas(b, tr_ + 0.8, rec(d, 'r3', tr_ + 1.2), 0.4)  # bollförlust
for k, ps in enumerate([(70, 36), (66, 64), (40, 30), (40, 70)]): d.mv(f'b{k}', t2, t2 + 1.8, ps)
t = chain(d, b, t2, ['r2', 'eo1', 'r0'], 0.3)
finish(d, 't52', 'possession-4-mot-4-plus-3-tva-rutor-och-mittcirkel', ['Possession 4 mot 4 + 3', 'Två rutor och mittcirkel'], 'Ruta i varje kortände · Cirkel i mitten · En extra i mitten och två utanför',
       [(0, 'Blått anfaller, rött försvarar', 'Passa eller dribbla in i rutorna och mittcirkeln.'),
        (ta - 0.4, 'In i rutan ger poäng', 'Använd de extra spelarna för att skapa överlägen.'),
        (tc - 0.2, 'Via mittcirkeln', 'Effektivt bollinnehav.'),
        (tr_ - 0.3, 'Från en ruta till den motsatta', 'Det ger också poäng.'),
        (t2 - 0.2, 'Vid bollförlust byter lagen roll direkt', 'Snabba omställningar åt båda hållen.')],
       'SPELUPPBYGGNAD', [('box', 10, 16, 90, 84), ('box', 12, 36, 26, 64), ('box', 74, 36, 88, 64), ('circle', 50, 50, 9)],
       [dict(kind='label', t0=ta, t1=ta + 1.5, pos=(19, 30), text='+1'), dict(kind='label', t0=tr_, t1=tr_ + 1.5, pos=(81, 30), text='+1')])

# ============ t53 Possession 4 mot 4 + 2 med fyra rutor ============
d = Drill()
RU = [(20, 26), (80, 26), (80, 74), (20, 74)]
for k, ps in enumerate([(34, 34), (66, 34), (66, 66), (34, 66)]): d.p(f'b{k}', str(k + 1), B, ps)
for k, ps in enumerate([(44, 40), (56, 40), (56, 60), (44, 60)]): d.p(f'r{k}', str(k + 1), R, ps)
d.p('em', 'E', G, (50, 50)); d.p('eo', 'E', G, (50, 89))
b = d.newball(rec(d, 'b0', 0)); t = 0.3; marks = []
for k, ru in enumerate(RU):
    d.mv(f'b{k}', t, t + 1.2, ru)
    t = d.pas(b, t + 0.5, (ru[0] + 1.8, ru[1] - 1.2)); marks.append((t, ru))
    if k == 1: t = d.pas(b, t + 0.3, rec(d, 'em', t + 0.8)); tcirc = t; marks.append((t, (50, 50)))
    d.mv(f'b{k}', t + 0.2, t + 1.4, [(38, 36), (62, 36), (62, 64), (38, 64)][k])
for k in range(4): wander(d, f'r{k}', 0, t, (30, 30, 70, 70), 60 + k, 1.4)
tb = t
d.mv('r2', tb, tb + 0.8, rec(d, 'b3', tb + 0.8)); t2 = d.pas(b, tb + 0.9, rec(d, 'r2', tb + 1), 0.3)
for k in range(4): d.mv(f'b{k}', t2, t2 + 1.4, (d.pos('r2')[0] + [-6, 6, -4, 6][k], d.pos('r2')[1] + [-5, -5, 6, 6][k]))
extras = [dict(kind='label', t0=tt, t1=tt + 1.4, pos=(p_[0], p_[1] - 9), text='+1') for tt, p_ in marks] + [dict(kind='label', t0=tb, t1=tb + 2.2, pos=(50, 11), text='BONUS: ALLA RUTOR + CIRKELN')]
finish(d, 't53', 'possession-4-mot-4-plus-2-med-fyra-rutor', ['Possession 4 mot 4 + 2', 'Fyra rutor'], 'Ruta i varje hörn · Cirkel i mitten · En extra i mitten och en utanför',
       [(0, 'Passa eller dribbla in i rutorna', 'Poäng varje gång laget går in i en ruta.'),
        (tcirc - 0.5, 'Och in i mittcirkeln', 'Håll planen stor. Snabba beslut och rörelser.'),
        (tb, 'Alla fyra rutor och cirkeln ger bonus', 'Under samma omgång.'),
        (t2 - 0.3, 'Vid bollförlust: aggressiv återerövring', 'Alla jagar direkt.')],
       'SPELUPPBYGGNAD', [('box', 10, 16, 90, 84), ('circle', 50, 50, 8)] + [('box', x - 7, y - 7, x + 7, y + 7) for x, y in RU], extras)

# ============ t54 Possession 7 mot 7 + 2 – defensiv zon ============
d = Drill()
for k, ps in enumerate([(36, 84), (64, 84)]): d.p(f'aA{k}', str(k + 1), B, ps)
d.p('jA', 'J', G, (50, 90)); d.p('dA0', '1', R, (42, 76)); d.p('dA1', '2', R, (58, 76))
for k, x in enumerate([22, 40, 60, 78]): d.p(f'c{k}', str(k + 3), R, (x, 50))
for k, ps in enumerate([(32, 56), (68, 44)]): d.p(f'm{k}', str(k + 3), B, ps)
for k, ps in enumerate([(36, 16), (64, 16)]): d.p(f'aB{k}', str(k + 5), B, ps)
d.p('jB', 'J', G, (50, 10)); d.p('dB0', '7', R, (42, 24)); d.p('dB1', '8', R, (58, 24))
b = d.newball(rec(d, 'aA0', 0))
t = chain(d, b, 0.4, ['jA', 'aA1', 'aA0'])                                   # 3 mot 2 i zon A
d.mv('m0', t - 1, t + 0.5, (46, 54)); d.mv('c1', t - 0.8, t + 0.5, (44, 52))   # rörelse mellan försvararna
d.mv('aB0', t - 0.6, t + 1, (44, 26))
t = d.pas(b, t + 0.3, rec(d, 'aB0', t + 1.2), 1.2); tB = t                      # passning över linjen till zon B
d.mv('c2', tB - 0.4, tB + 1.6, (54, 28))                                     # mittback går in: 3 mot 2
d.mv('dA1', tB - 0.4, tB + 2.0, (60, 50)); d.mv('c1', tB, tB + 1.5, (40, 50))  # försvarare från A återställer fyrbackslinjen
d.mv('c3', tB, tB + 1.5, (80, 50))
t = chain(d, b, t, ['jB', 'aB1'])
d.mv('dB0', t - 0.8, t + 0.4, rec(d, 'aB1', t + 0.4)); t2 = d.pas(b, t + 0.6, rec(d, 'dB0', t + 1), 0.3)   # försvarare vinner bollen
t2 = chain(d, b, t2, ['c2', 'dB1'])                                          # två passningar i rad = poäng
finish(d, 't54', 'possession-7-mot-7-plus-2-defensiv-zon', ['Possession 7 mot 7 + 2', 'Defensiv zon'], 'Tre zoner: anfallszon A, centralzon och anfallszon B',
       [(0, 'Starta med 3 mot 2 i zon A', 'Två anfallare och en joker mot två försvarare.'),
        (tB - 1.6, 'Passning genom eller över linjen', 'Rörelser mellan försvararna skapar ytor.'),
        (tB, 'En mittback går in i zon B: 3 mot 2', 'En försvarare från zon A återställer fyrbackslinjen.'),
        (tB + 2.4, 'Kompakt och synkroniserat försvar', 'Anfallare i centralzonen får inte ta emot bakom linjen.'),
        (t2 - 1.4, 'Försvaret vinner bollen', 'Två passningar i rad ger poäng.')],
       'AVSLUT OCH MÅL', [('zone', 4, 66, 96, 96, (60, 150, 220), 'ZON A'), ('zone', 4, 4, 96, 34, (60, 150, 220), 'ZON B'), ('line', [(4, 50), (96, 50)])],
       [dict(kind='label', t0=t2, t1=t2 + 2, pos=(50, 40), text='+1')])

# ============ t55 Possession 4 mot 4 + 1 joker med fyra mål ============
d = Drill()
for k, ps in enumerate([(84, 50), (66, 30), (66, 70), (40, 46)]): d.p(f'b{k}', str(k + 1), B, ps)
for k, ps in enumerate([(30, 40), (30, 60), (54, 36), (54, 62)]): d.p(f'r{k}', str(k + 1), R, ps)
d.p('j', 'J', G, (52, 50))
b = d.newball(rec(d, 'b0', 0))
d.mv('b3', 1, 3, (30, 30)); d.mv('r0', 1, 3.4, (32, 36))
t = chain(d, b, 0.5, ['b1', 'j', 'b2'])                                       # från backen upp via jokern
d.mv('b2', t - 1, t + 1.4, (24, 68)); d.carry(b, 'b2', t, t + 1.2)
t = d.pas(b, t + 1.3, (6, 70), 0.5); tg = t                                   # mål i fritt småmål
b2 = d.newball((200, 200)); d.balls[b2] = [(0, (200, 200)), (tg + 0.6, (200, 200)), (tg + 0.61, rec(d, 'b3', tg + 0.6))]
d.mv('r1', tg + 0.4, tg + 1.2, (32, 34)); t3 = d.pas(b2, tg + 1.0, rec(d, 'r1', tg + 1.3), 0.3)
t3 = chain(d, b2, t3, ['j', 'r3']); d.carry(b2, 'r3', t3, t3 + 1.2); d.mv('r3', t3, t3 + 1.2, (80, 34)); d.pas(b2, t3 + 1.3, (94, 30), 0.5)
finish(d, 't55', 'possession-4-mot-4-plus-1-joker-med-fyra-mal', ['Possession 4 mot 4 + 1', 'Fyra småmål'], 'Rektangel delad på mitten · Två småmål i varje kortände',
       [(0, 'Spela från backen fram till anfallarna', 'Blå nr 1 är spelaren längst bort från målen.'),
        (1.2, 'Spela upp i banan via jokern', 'Jokern hjälper laget med boll.'),
        (tg - 1.6, 'Byt sida mot det fria målet', 'Mål i något av de två småmålen.'),
        (tg + 0.8, 'Rött vinner bollen och anfaller åt andra hållet', 'Omställning direkt vid bollvinst.')],
       'SPELUPPBYGGNAD', [('box', 10, 16, 90, 84), ('line', [(50, 16), (50, 84)]), ('smallgoal', 7, 30), ('smallgoal', 7, 70), ('smallgoal', 93, 30), ('smallgoal', 93, 70)])

# ============ t56 Lång och kort passning i fyra led ============
d = Drill(); cols = [20, 40, 60, 80]
for i, x in enumerate(cols):
    d.p(f'C{i}', 'C', B, (x, 90)); d.p(f'A{i}', 'A', B, (x, 70)); d.p(f'B{i}', 'B', B, (x, 30)); d.p(f'D{i}', 'D', B, (x, 10))
for i, x in enumerate(cols):
    off = i * 0.5; bb = d.newball((x + 1.8, 88.8)); t = 0.4 + off
    d.mv(f'A{i}', t, t + 0.6, (x, 74))                                          # kom mot bollen
    t = d.pas(bb, t + 0.2, (x + 1.8, 72.8)); t = d.pas(bb, t + 0.3, (x + 1.8, 88.8))   # kort och tillbaka
    t = d.pas(bb, t + 0.3, (x + 3, 72.8)); d.mv(f'A{i}', t, t + 0.5, (x + 2, 70)); t = d.pas(bb, t + 0.6, (x + 1.8, 31.2), 1.1)   # riktad mottagning, lång till B
    d.mv(f'B{i}', t - 0.6, t, (x, 27))
    t = d.pas(bb, t + 0.3, (x + 1.8, 11.2)); t = d.pas(bb, t + 0.3, (x + 1.8, 28.8))   # B kort med D
    t = d.pas(bb, t + 0.4, (x + 3.8, 68.8), 1.1)                                   # långt tillbaka till A
finish(d, 't56', 'lang-och-kort-passning-i-fyra-led', ['Lång och kort passning', 'Fyra led'], 'Rader om fyra: C, A, B, D · Alla rader kör samtidigt',
       [(0, 'C spelar kort till A och får tillbaka', 'Kom mot bollen innan du tar emot.'),
        (2.2, 'A tar emot riktat och slår långt till B', 'Första touchen öppnar upp för den långa passningen.'),
        (4, 'B spelar kort med D', 'Flera bollar i spel samtidigt.'),
        (5.6, 'B slår långt tillbaka till A', 'Lås fotleden och träffa mitt på bollen.'),
        (8, 'Byt plats efter två minuter', 'Ytter- och innerspelare byter.')],
       'SPELUPPBYGGNAD', [('text', 8, y, l) for y, l in [(90, 'C'), (70, 'A'), (30, 'B'), (10, 'D')]])

# ============ t58 Dubbelkvadrat + jokrar ============
d = Drill()
for k, ps in enumerate([(22, 34), (40, 30), (38, 66), (20, 62)]): d.p(f'b{k}', str(k + 1), B, ps)
for k, ps in enumerate([(30, 44), (34, 54), (26, 52), (42, 48)]): d.p(f'r{k}', str(k + 1), R, ps)
for k, ps in enumerate([(30, 12), (70, 12), (70, 88), (30, 88)]): d.p(f'j{k}', 'J', G, ps)
b = d.newball(rec(d, 'b0', 0))
for k in range(4): wander(d, f'b{k}', 0, 7, (14, 22, 46, 78), 70 + k, 1.8); wander(d, f'r{k}', 0, 7, (18, 28, 44, 72), 80 + k, 1.6)
t = chain(d, b, 0.4, ['b1', 'j0', 'b2', 'j3', 'b3'])                         # behåll bollen i planhalvan, jokrar max två touch
d.mv('r2', t - 1, t, rec(d, 'b3', t)); tw = d.pas(b, t + 0.2, rec(d, 'r2', t + 0.6), 0.3)   # rött vinner bollen
for k, ps in enumerate([(62, 34), (78, 30), (78, 66), (60, 64)]): d.mv(f'r{k}', tw, tw + 2, ps)   # flyttar spelet till andra halvan
d.mv('r2', tw, tw + 1.2, (56, 56)); d.carry(b, 'r2', tw, tw + 1.2)
for k, ps in enumerate([(30, 40), (40, 50), (34, 62), (46, 40)]): d.mv(f'b{k}', tw, tw + 0.8, ps)    # blått försöker vinna tillbaka direkt
for k, ps in enumerate([(58, 40), (62, 52), (66, 46), (54, 60)]): d.mv(f'b{k}', tw + 1.2, tw + 3, ps)
t = chain(d, b, tw + 1.3, ['r1', 'j1', 'r3', 'j2', 'r0'])
finish(d, 't58', 'dubbelkvadrat-plus-jokrar', ['Dubbelkvadrat', 'Med jokrar'], 'Yta 40 × 20 m i två halvor · Tredje laget är jokrar utanför',
       [(0, 'Blått håller bollen i sin planhalva', 'Jokrarna runt ytan spelar med laget som har bollen, max två touch.'),
        (2.6, 'Orientera dig', 'Första touchen åt det håll du vill passa.'),
        (tw - 0.3, 'Rött vinner bollen', 'Blått försöker vinna tillbaka den direkt.'),
        (tw + 1, 'Rött flyttar spelet till andra planhalvan', 'Där försöker de behålla bollen.'),
        (tw + 4, 'Passa när medspelaren är redo', 'Annars flytta bollen tills den är det.')],
       'SPELUPPBYGGNAD', [('box', 14, 20, 86, 80), ('line', [(50, 20), (50, 80)])])

# ============ t59 Ajax: mittzon och anfall i ändzonerna ============
d = Drill()
for k, ps in enumerate([(30, 56), (50, 62), (70, 56), (40, 44), (60, 44)]): d.p(f'b{k}', str(k + 1), B, ps)
for k, ps in enumerate([(30, 44), (50, 38), (70, 44), (40, 56), (60, 56)]): d.p(f'r{k}', str(k + 1), R, ps)
d.p('bf0', '9', B, (40, 16)); d.p('bf1', '10', B, (60, 16)); d.p('rd', '6', R, (50, 20))
d.p('rf0', '9', R, (40, 84)); d.p('rf1', '10', R, (60, 84)); d.p('bd', '6', B, (50, 80))
d.p('mv1', 'MV', G, (50, 5)); d.p('mv2', 'MV', G, (50, 95)); d.p('t1', 'T', G, (4, 50)); d.p('t2', 'T', G, (96, 50))
b = d.newball(rec(d, 'b1', 0))
t = chain(d, b, 0.4, ['b3', 'b4'])
d.mv('bf1', t - 0.6, t + 0.4, (58, 24)); t = d.pas(b, t + 0.3, rec(d, 'bf1', t + 1.1)); tin = t   # spela in till anfallarna
d.mv('b4', tin - 0.8, tin + 1.6, (64, 20))                                                     # passningsläggaren följer med: 3 mot 1
t = chain(d, b, t, ['bf0', 'b4']); t = d.pas(b, t + 0.2, (56, -1), 0.5); tg = t
b2 = d.newball((200, 200)); d.balls[b2] = [(0, (200, 200)), (tg + 0.5, (200, 200)), (tg + 0.51, (6, 52)), (tg + 1.3, rec(d, 'b0', tg + 1.3))]   # tränaren slår in ny boll
d.mv('r0', tg + 0.6, tg + 1.4, (32, 52)); t3 = d.pas(b2, tg + 1.6, rec(d, 'r0', tg + 1.9), 0.3)   # rött vinner bollen i mittzonen
d.carry(b2, 'r0', t3, t3 + 0.8); d.mv('r0', t3, t3 + 0.8, (18, 62)); d.pas(b2, t3 + 0.9, (7, 66), 0.4)   # direkt i småmål
finish(d, 't59', 'ajax-mittzon-och-anfall-i-andzonerna', ['Ajax: mittzon', 'Och anfall i ändzonerna'], 'Mittzon 5 mot 5 · Ändzoner 2 mot 1 med stort mål · Fyra småmål',
       [(0, 'Lagen spelar i mittzonen', 'Två anfallare väntar i ändzonen, en försvarare i den andra.'),
        (tin - 0.8, 'Spela in till anfallarna', 'Spela framåt när anfallarna är spelbara.'),
        (tin + 0.2, 'Passningsläggaren följer med: 3 mot 1', 'Följ din passning in i ändzonen.'),
        (tg + 0.4, 'Tränaren slår in en ny boll direkt', 'Så fort bollen är ute.'),
        (t3 - 0.2, 'Bollvinst i mittzonen', 'Mål direkt i ett av småmålen.')],
       'KONTRING', [('zone', 4, 30, 96, 70, (200, 220, 200), 'MITTZON'), ('smallgoal', 7, 34), ('smallgoal', 93, 34), ('smallgoal', 7, 66), ('smallgoal', 93, 66)])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

if __name__ == '__main__':
    render(C, sys.argv)
