# Omgång 4: tolv av Sams egna övningar, steg för steg efter instruktionen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('o3', __file__.replace('render_omgang4.py', 'render_omgang3.py'))
o3 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(o3); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = o3.finish, o3.rec, o3.chain, o3.wander, o3.counter, o3.arrivals
C.clear()
WHITE = '#f3f5ef'; BLACK = '#1b211e'; YEL = '#f2cf45'

def newball_at(d, t, pos):
    b = d.newball((200, 200)); d.balls[b] = [(0, (200, 200)), (t - 0.01, (200, 200)), (t, pos)]; return b
def lab(t0, t1, pos, text): return dict(kind='label', t0=t0, t1=t1, pos=pos, text=text)

# ============ t60 Dortmund: fyra lag och fyra mål ============
# Två matcher korsvis på samma plan med två bollar, vanligt spel i båda hela tiden.
d = Drill()
BH = [(36, 70), (60, 64), (44, 52), (66, 80)]; RH = [(40, 30), (62, 36), (48, 46), (34, 20)]
WH = [(70, 38), (78, 60), (60, 50), (84, 48)]; YH = [(28, 40), (22, 60), (40, 50), (16, 50)]
for k in range(4):
    d.p(f'b{k}', str(k + 1), B, BH[k]); d.p(f'r{k}', str(k + 1), R, RH[k]); d.p(f'w{k}', str(k + 1), WHITE, WH[k]); d.p(f'y{k}', str(k + 1), YEL, YH[k])

def attack(ball, t, att, dfn, path, goal, scorer):
    """Laget anfaller: passningar längs path (spelar-id), sista spelaren avslutar i goal. Försvaret följer bollen."""
    home = {k: d.pos(f'{dfn}{k}') for k in range(4)}
    for pid in path:
        tgt = rec(d, pid, t + 0.7)
        for k in range(4):
            hx, hy = home[k]; bx, by = tgt
            d.mv(f'{dfn}{k}', t, t + 0.9, (hx + (bx - hx) * 0.3, hy + (by - hy) * 0.3))
        t = d.pas(ball, t + 0.25, tgt) + 0.15
    sx, sy = d.pos(scorer); ex, ey = ((goal[0] * 2 + sx * 3) / 5, (goal[1] * 2 + sy * 3) / 5)
    dur = max(1.0, ((ex - sx) ** 2 + (ey - sy) ** 2) ** .5 / 28)
    d.mv(scorer, t, t + dur, (ex, ey)); d.carry(ball, scorer, t, t + dur)
    return d.pas(ball, t + dur + 0.1, goal)

# Match 1: blått anfaller övre målet, rött nedre.
b1 = d.newball(rec(d, 'b0', 0))
d.mv('b3', 0.3, 2.2, (58, 40)); d.mv('b1', 0.6, 2.4, (64, 30))
t = attack(b1, 0.4, 'b', 'r', ['b2', 'b1', 'b3'], (50, 1), 'b3'); g1 = t
for k, ps in enumerate([(40, 56), (56, 60), (48, 66), (60, 72)]): d.mv(f'b{k}', g1, g1 + 3.0, ps)          # blått springer hem
for k, ps in enumerate([(46, 22), (58, 28), (40, 40), (64, 46)]): d.mv(f'r{k}', g1, g1 + 1.6, ps)
d.balls[b1] += [(g1 + 0.3, at(d.balls[b1], g1 + 0.3)), (g1 + 0.301, (200, 200)), (g1 + 0.999, (200, 200)), (g1 + 1.0, rec(d, 'r0', g1 + 1.0))]    # ny boll till rött
t = attack(b1, g1 + 1.2, 'r', 'b', ['r1', 'r2', 'r3'], (50, 99), 'r3'); g2 = t
for k, ps in enumerate(RH): d.mv(f'r{k}', g2, g2 + 3.0, ps)
d.balls[b1] += [(g2 + 0.3, at(d.balls[b1], g2 + 0.3)), (g2 + 0.301, (200, 200)), (g2 + 0.999, (200, 200)), (g2 + 1.0, rec(d, 'b1', g2 + 1.0))]
t = attack(b1, g2 + 1.2, 'b', 'r', ['b0', 'b2'], (50, 1), 'b2'); g3 = t

# Match 2: gult anfaller höger mål, vitt vänster.
b2 = d.newball(rec(d, 'y0', 0))
d.mv('y1', 0.4, 2.4, (48, 62)); d.mv('y2', 0.5, 2.6, (60, 44))
t = attack(b2, 0.9, 'y', 'w', ['y2', 'y1', 'y2'], (99, 50), 'y2'); h1 = t
for k, ps in enumerate(YH): d.mv(f'y{k}', h1, h1 + 3.0, ps)
d.balls[b2] += [(h1 + 0.3, at(d.balls[b2], h1 + 0.3)), (h1 + 0.301, (200, 200)), (h1 + 0.999, (200, 200)), (h1 + 1.0, rec(d, 'w3', h1 + 1.0))]
t = attack(b2, h1 + 1.2, 'w', 'y', ['w0', 'w2', 'w1'], (1, 50), 'w1'); h2 = t
for k, ps in enumerate(WH): d.mv(f'w{k}', h2, h2 + 3.0, ps)
d.balls[b2] += [(h2 + 0.3, at(d.balls[b2], h2 + 0.3)), (h2 + 0.301, (200, 200)), (h2 + 0.999, (200, 200)), (h2 + 1.0, rec(d, 'y3', h2 + 1.0))]
t = attack(b2, h2 + 1.2, 'y', 'w', ['y0', 'y2'], (99, 50), 'y2')

finish(d, 't60', 'dortmund-fyra-lag-och-fyra-mal', ['Dortmund', 'Fyra lag och fyra mål'], 'Fyra lag om 4–5 · Ett mål på varje sida · Två bollar',
       [(0, 'Två matcher korsvis på samma plan', 'Blått mot rött på kortsidorna, gult mot vitt på långsidorna.'),
        (2.5, 'Scanna hela tiden', 'Lyft blicken innan du tar emot, så undviker du krockar.'),
        (min(g1, h1) - 0.5, 'Vanligt spel i båda matcherna', 'Mål – nästa boll startar direkt hos motståndarna.'),
        (min(g2, h2) - 2, 'Använd luckorna', 'Den andra matchen skapar ytor du kan spela i.'),
        (max(g2, h2) + 0.8, 'Prata med dina medspelare', 'Byt motståndare efter fyra minuter.')],
       'SPELUPPBYGGNAD', [('box', 6, 8, 94, 92), ('ugoal', 50, 6, 'up'), ('ugoal', 50, 94, 'down'), ('smallgoal', 5, 50), ('smallgoal', 95, 50)], target=16.8)

# ============ t61 Uppbyggnad genom tre zoner mot mål ============
d = Drill()
d.p('gmv', 'MV', YEL, (50, 95)); d.p('smv', 'MV', BLACK, (50, 5))
for k, ps in enumerate([(20, 80), (40, 86), (60, 86), (80, 80)]): d.p(f'g{k}', str(k + 1), YEL, ps)       # fyra i första zonen
for k, ps in enumerate([(40, 52), (60, 48)]): d.p(f'gm{k}', str(k + 5), YEL, ps)                           # två i mittkorridoren
for k, ps in enumerate([(42, 24), (58, 20)]): d.p(f'ga{k}', str(k + 7), YEL, ps)                           # två i sista zonen
for k, ps in enumerate([(38, 74), (62, 74)]): d.p(f's{k}', str(k + 1), BLACK, ps)                         # 4 mot 2
for k, ps in enumerate([(44, 46), (56, 54)]): d.p(f'sm{k}', str(k + 3), BLACK, ps)                         # 2 mot 2
for k, ps in enumerate([(20, 22), (36, 18), (50, 16), (64, 18), (80, 22)]): d.p(f'sa{k}', str(k + 5), BLACK, ps)   # fem försvarare
b = d.newball(rec(d, 'gmv', 0))
t = chain(d, b, 0.4, ['g1', 'g0', 'g1', 'g2'])                                       # överläge 4 mot 2
d.mv('g2', t, t + 1.8, (62, 58)); d.carry(b, 'g2', t, t + 1.8); tdrive = t           # driver in i nästa zon: överläge
d.mv('sm1', t, t + 1.6, (60, 54)); t += 1.8
d.mv('gm0', t - 0.8, t + 0.2, (44, 56)); t = d.pas(b, t + 0.2, rec(d, 'gm0', t + 0.8))   # in till mittfältaren som kan vända
d.mv('gm0', t, t + 0.6, (44, 50)); d.carry(b, 'gm0', t, t + 0.6); t += 0.6
d.mv('ga0', t - 0.6, t + 0.6, (42, 32)); d.mv('ga1', t - 0.6, t + 1.4, (60, 12))      # en kommer mot, en går på djupet
t = d.pas(b, t + 0.2, rec(d, 'ga0', t + 0.8)); t = d.pas(b, t + 0.3, rec(d, 'ga1', t + 1.1)); tsh = t
t = d.pas(b, t + 0.3, (55, -1), 0.5); d.mv('smv', t - 0.5, t, (54, 5)); tg = t
finish(d, 't61', 'uppbyggnad-genom-tre-zoner-mot-mal', ['Uppbyggnad genom tre zoner', 'Mot mål'], 'Gult: fyra, två och två i zonerna · Svart försvarar · Mål i båda ändar',
       [(0, 'Gult bygger upp från egen målvakt', 'Fyra mot två i första zonen. Använd överläget.'),
        (tdrive, 'En gul spelare driver in i nästa zon', 'Det skapar överläge. Övriga är låsta i sina zoner.'),
        (tdrive + 1.8, 'Spela in när mittfältaren kan vända', 'Mittzonen spelar 2 mot 2.'),
        (tsh - 1.4, 'Anfallarna: en kommer mot, en går på djupet', 'Två anfallare mot fem försvarare och målvakt.'),
        (tg, 'Mål i stora målet ger tre poäng', 'Vinner svart bollen anfaller de målet i andra änden.')],
       'SPELUPPBYGGNAD', [('line', [(0, 34), (100, 34)]), ('line', [(0, 66), (100, 66)])], [lab(tg, tg + 2.5, (50, 40), '+3')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ t62 Spelövertag 8 mot 5 ============
d = Drill()
ring = [(18, 28), (40, 20), (62, 20), (82, 28), (84, 64), (62, 80), (38, 80), (16, 64)]
for k, ps in enumerate(ring): d.p(f'b{k}', str(k + 1), B, ps)
for k, ps in enumerate([(36, 40), (56, 36), (64, 56), (42, 60), (50, 48)]): d.p(f'r{k}', str(k + 1), R, ps)
for k in range(8): wander(d, f'b{k}', 0, 10, (14, 18, 86, 82), 140 + k, 2.4)
for k in range(5): wander(d, f'r{k}', 0, 10, (26, 28, 74, 72), 150 + k, 1.8)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.3, ['b1', 'b2', 'b4', 'b3', 'b5', 'b7', 'b6', 'b0', 'b2', 'b4'], 0.2); cnt = arrivals(d, b)[:10]
d.mv('r2', t, t + 1, rec(d, 'b4', t + 1)); tw = d.pas(b, t + 1.0, rec(d, 'r2', t + 1.2), 0.3)
d.mv('r2', tw, tw + 1.4, (80, 54)); d.carry(b, 'r2', tw, tw + 1.4); tg = d.pas(b, tw + 1.5, (93, 50), 0.4)
finish(d, 't62', 'spelovertag-8-mot-5', ['Spelövertag', '8 mot 5'], 'Ruta · Småmål på varje kortsida · Överlaget håller bollen',
       [(0, 'Överlaget håller bollen', 'Gör planen stor med bollen. Underlaget jagar.'),
        (3, 'Spela bort pressen med få touch', 'Tio passningar i rad ger en poäng.'),
        (cnt[-1], 'Tio passningar: en poäng', 'Räkningen börjar om.'),
        (tw - 0.4, 'Underlaget vinner bollen', 'Pressa tillsammans och styr mot sidan.'),
        (tg - 1.2, 'Mål i valfritt småmål', 'Byt underlag efter tre minuter.')],
       'SPELUPPBYGGNAD', [('box', 10, 14, 90, 86), ('smallgoal', 7, 50), ('smallgoal', 93, 50)], counter(cnt))

# ============ t63 Överflyttning i försvar ============
d = Drill(); X = [20, 40, 60, 80]
for k, x in enumerate(X): d.p(f'w1{k}', str(k + 1), WHITE, (x, 86)); d.p(f'w2{k}', str(k + 5), WHITE, (x, 50)); d.p(f'w3{k}', str(k + 9), WHITE, (x, 14))
for k, x in enumerate(X): d.p(f'ra{k}', str(k + 1), R, (x, 64)); d.p(f'rb{k}', str(k + 5), R, (x, 36))
b = d.newball(rec(d, 'w11', 0))
def shift(t, side):  # rött flyttar över som en enhet mot bollsidan
    for k, x in enumerate(X):
        d.mv(f'ra{k}', t, t + 1.0, (x + side * 10, 64)); d.mv(f'rb{k}', t, t + 1.0, (x + side * 10, 36))
t = d.pas(b, 0.5, rec(d, 'w10', 1)); shift(0.6, -1)
t = d.pas(b, t + 0.5, rec(d, 'w11', t + 1)); shift(t - 0.4, -0.3)
t = d.pas(b, t + 0.4, rec(d, 'w12', t + 1)); shift(t - 0.5, 0.4)
t = d.pas(b, t + 0.4, rec(d, 'w13', t + 1)); shift(t - 0.5, 1)
d.mv('w22', t, t + 0.8, (54, 50)); t = d.pas(b, t + 0.5, rec(d, 'w22', t + 1.2)); tthru = t     # igenom en röd linje
d.mv('rb2', tthru - 0.4, tthru + 0.6, (55, 46)); d.mv('ra2', tthru - 0.2, tthru + 0.6, (56, 56))  # närmaste kliver fram
tw = d.pas(b, tthru + 0.8, rec(d, 'rb2', tthru + 1.0), 0.3)                                         # bollvinst
finish(d, 't63', 'overflyttning-i-forsvar', ['Överflyttning i försvar', 'Två fyrbackslinjer'], 'Rött i två linjer om fyra · Vitt i tre linjer om fyra',
       [(0, 'Vitt passar i sidled', 'Rött försvarar i två fyrbackslinjer.'),
        (1, 'Rött flyttar över mot bollsidan som en enhet', 'Flytta över medan bollen rullar. Håll lika avstånd i linjen.'),
        (tthru - 0.8, 'Vitt spelar igenom en röd linje', 'Det ger vitt en poäng.'),
        (tthru + 0.2, 'Närmaste spelare kliver fram', 'När bollen kommer in i din zon.'),
        (tw, 'Rött vinner bollen: en poäng', 'Byt roller efter tre bollvinster.')],
       'FÖRHINDRA SPELUPPBYGGNAD', [('line', [(0, 68), (100, 68)]), ('line', [(0, 32), (100, 32)])] + [('cone', x, y) for x in (8, 92) for y in (32, 68)],
       [lab(tthru, tthru + 1.4, (50, 42), '+1 VITT'), lab(tw, tw + 2, (50, 42), '+1 RÖTT')])

# ============ t64 Stor engelsk kvadrat ============
d = Drill()
top = [(16, 12), (36, 22), (54, 12), (72, 22), (88, 14), (50, 26)]
bot = [(16, 88), (36, 78), (54, 88), (72, 78), (88, 86), (50, 74)]
mid = [(20, 50), (36, 46), (50, 54), (64, 46), (80, 50), (50, 42)]
for k, ps in enumerate(top): d.p(f'b{k}', str(k + 1), B, ps)
for k, ps in enumerate(bot): d.p(f'w{k}', str(k + 1), WHITE, ps)
for k, ps in enumerate(mid): d.p(f'r{k}', str(k + 1), R, ps)
d.mv('r1', 0.3, 1.6, (38, 20)); d.mv('r3', 0.3, 1.6, (62, 18))                                       # två pressare in där bollen är
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b1', 'b2', 'b4', 'b3', 'b5']); cnt = arrivals(d, b)[:5]
t = d.pas(b, t + 0.3, rec(d, 'w2', t + 1.6), 1.4); tl = t                                                 # över mittzonen
d.mv('r1', tl - 1.0, tl + 0.8, (36, 46)); d.mv('r3', tl - 1.0, tl + 0.8, (64, 46))
d.mv('r0', tl - 0.8, tl + 0.8, (30, 80)); d.mv('r4', tl - 0.8, tl + 0.8, (70, 80))                     # nya pressare
t = chain(d, b, t, ['w1', 'w5'])
d.mv('r4', t - 0.6, t, rec(d, 'w5', t)); tw = d.pas(b, t + 0.2, rec(d, 'r4', t + 0.4), 0.3)          # pressarna vinner bollen
for k, ps in enumerate(mid): d.mv(f'w{k}', tw + 0.4, tw + 2.6, ps)                                     # vitt byter plats med mittlaget
for k, ps in enumerate(bot): d.mv(f'r{k}', tw + 0.4, tw + 2.6, ps)
finish(d, 't64', 'stor-engelsk-kvadrat', ['Stor engelsk kvadrat', 'Tre zoner, tre lag'], 'Halvplan i tre zoner · Ett lag i varje zon',
       [(0, 'Ytterlagen håller bollen i sina zoner', 'Mittlaget skickar in två pressare där bollen är.'),
        (1.6, 'Flytta bollen bort från pressen', 'Se den långa passningen innan du får bollen.'),
        (cnt[-1], 'Fem passningar: spela över mittzonen', 'Bollen till andra ytterlaget ger en poäng.'),
        (tl + 0.2, 'Mittlaget skickar in två nya pressare', 'Pressa så att den långa passningen stängs.'),
        (tw, 'Pressarna vinner bollen', 'Laget som tappade bollen byter plats med mittlaget.')],
       'RONDO', [('line', [(0, 33), (100, 33)]), ('line', [(0, 67), (100, 67)])], counter(cnt + [tl], pos=(50, 40)))

# ============ t65 3 mot 3 + 3 ============
d = Drill()
DOCK = [(40, 40), (60, 40), (40, 60), (60, 60)]
for k, ps in enumerate([(30, 30), (70, 34), (50, 70)]): d.p(f'b{k}', str(k + 1), B, ps)
for k, ps in enumerate([(44, 34), (56, 50), (40, 52)]): d.p(f'r{k}', str(k + 1), R, ps)
for k, ps in enumerate([(12, 50), (88, 50), (50, 14)]): d.p(f'n{k}', 'N', G, ps)
b = d.newball(rec(d, 'b0', 0))
for k in range(3): wander(d, f'r{k}', 0, 9, (30, 30, 70, 70), 160 + k, 1.6)
d.mv('b2', 3, 4.2, (50, 54))                                                         # tar position i luckan mellan dockorna
t = chain(d, b, 0.3, ['n0', 'b1', 'n2', 'b0', 'n1', 'b1'])
t = d.pas(b, t + 0.3, rec(d, 'b2', t + 0.8)); tgap = t                                # genom luckan
t = chain(d, b, t, ['n0']); cnt = arrivals(d, b)[:8]
d.mv('r0', t - 0.6, t + 0.4, (16, 50)); tl = d.pas(b, t + 0.6, rec(d, 'r0', t + 0.8), 0.3)        # bollförlust
for k in range(3): d.mv(f'b{k}', tl, tl + 1.6, (20 + k * 3, 44 + k * 6))                           # de tre närmaste pressar direkt
tr = d.pas(b, tl + 2.0, rec(d, 'b1', tl + 2.2), 0.3)                                                # återvinst inom fem sekunder
finish(d, 't65', '3-mot-3-plus-3-positionsspel-mot-atererovring', ['3 mot 3 + 3', 'Positionsspel mot återerövring'], 'Dockor inne · 3 mot 3 · Tre neutrala på kanterna',
       [(0, 'Laget med boll spelar med de neutrala', 'Det blir 6 mot 3. Dockorna stänger vissa passningsvägar.'),
        (2.5, 'Ta position i luckorna mellan dockorna', 'Scanna före mottagning.'),
        (tgap - 0.4, 'Passning genom en lucka: extra poäng', 'Åtta passningar ger en poäng.'),
        (tl, 'Bollförlust: de tre närmaste pressar direkt', 'Vinn tillbaka inom fem sekunder.'),
        (tr, 'Tillbaka inom fem sekunder: en poäng', 'Till laget som tappade bollen.')],
       'SPELUPPBYGGNAD', [('box', 10, 12, 90, 88)] + [('pole', x, y) for x, y in DOCK],
       counter(cnt + [tgap + 3], pos=(50, 6), last=None)[:8] + [lab(tgap, tgap + 1.4, (50, 46), '+1 EXTRA'), lab(tl, tl + 2, (50, 6), '5 SEK'), lab(tr, tr + 2, (30, 34), '+1')])

# ============ t66 Speluppbyggnad mot anfall till småmål ============
d = Drill()
d.p('mv', 'MV', R, (50, 94))
for k, ps in enumerate([(38, 84), (62, 84)]): d.p(f'r1{k}', '1', R, ps)
for k, ps in enumerate([(14, 72), (86, 72)]): d.p(f'r2{k}', '2', R, ps)
d.p('r3', '3', R, (50, 64))
for k, ps in enumerate([(30, 14), (70, 14)]): d.p(f'r4{k}', '4', R, ps)
for k, ps in enumerate([(40, 76), (60, 76), (50, 56)]): d.p(f'p{k}', str(k + 1), B, ps)
b = d.newball(rec(d, 'mv', 0))
d.mv('p0', 0.4, 1.4, (42, 82)); t = d.pas(b, 0.5, rec(d, 'r11', 1.2))                      # första passningen: bredd och djup
d.mv('p1', t, t + 1, (66, 80)); t = d.pas(b, t + 0.3, rec(d, 'r21', t + 1))
d.mv('r3', t - 1, t + 0.4, (58, 60)); d.mv('p2', t, t + 1, (68, 64)); t = d.pas(b, t + 0.4, rec(d, 'r3', t + 1))   # 3:an mellan pressarna
d.mv('r41', t - 1, t + 0.2, (66, 22)); t = d.pas(b, t + 0.3, rec(d, 'r41', t + 1.2), 1.0); tr4 = t                # nå en 4:a med kontroll
d.mv('r41', t, t + 1.4, (70, 10)); d.carry(b, 'r41', t, t + 1.4); t = d.pas(b, t + 1.5, (72, 3), 0.4); tg = t        # vänder och anfaller småmålet
b2 = newball_at(d, tg + 0.6, rec(d, 'mv', tg + 0.6)); t3 = d.pas(b2, tg + 0.8, rec(d, 'r10', tg + 1.2))
d.mv('p0', tg + 0.6, tg + 1.8, rec(d, 'r10', tg + 1.8)); tw = d.pas(b2, tg + 1.9, rec(d, 'p0', tg + 2.1), 0.3)      # blått vinner bollen
t5 = d.pas(b2, tw + 0.8, (46, 101), 0.5)
finish(d, 't66', 'speluppbyggnad-mot-anfall-till-smamal', ['Speluppbyggnad', 'Mot anfall till småmål'], 'Rött 1–4 efter roll · Tre blå pressare · Två småmål vid mittlinjen',
       [(0, 'Rött bygger upp från målvakten', 'Mittback 1, ytterback 2, mittfältare 3, forwards 4.'),
        (0.6, 'Bredd och djup i första passningen', 'Tre blå pressar.'),
        (tr4 - 1.4, '3:an tar position mellan pressarna', 'Rött vill nå en 4:a med kontroll.'),
        (tr4, '4:an vänder upp direkt när det finns yta', 'Och anfaller småmålen.'),
        (tw - 0.3, 'Blått vinner bollen', 'Avslut mot det stora målet inom åtta sekunder.')],
       'SPELUPPBYGGNAD', [('smallgoal', 28, 4), ('smallgoal', 72, 4), ('pole', 30, 44), ('pole', 50, 40), ('pole', 70, 44)],
       [lab(tw + i, tw + i + 1, (50, 40), f'{8 - i} SEK') for i in range(3)])
C[-1]['goals'] = [(50, 100)]; C[-1]['keep_goals'] = True

# ============ t67 Kontring från central tredjedel ============
d = Drill()
d.p('mv', 'MV', R, (50, 95))
for k, x in enumerate([20, 40, 60, 80]): d.p(f'rb{k}', str(k + 2), R, (x, 76)); d.p(f'rm{k}', str(k + 6), R, (x, 54))
for k, x in enumerate([24, 42, 58, 76]): d.p(f'bm{k}', str(k + 6), B, (x, 42))
for k, x in enumerate([30, 50, 70]): d.p(f'bb{k}', str(k + 2), B, (x, 20))
for k, x in enumerate([40, 60]): d.p(f'bf{k}', str(k + 9), B, (x, 70))
b = d.newball(rec(d, 'mv', 0))
t = d.pas(b, 0.5, rec(d, 'rm1', 1.4), 1.0)                                                # målvakten spelar till mittfältet
for k in range(4): wander(d, f'rm{k}', 0, t + 3, (14, 38, 86, 62), 170 + k, 1.4)
t = chain(d, b, t, ['rm2', 'rm3', 'rm1'])
d.mv('bm1', t - 0.8, t, rec(d, 'rm1', t)); tw = d.pas(b, t + 0.2, rec(d, 'bm1', t + 0.4), 0.3)   # lag 1 vinner bollen
d.mv('bf0', tw, tw + 1.2, (36, 62)); d.mv('bf1', tw, tw + 1.6, (64, 84))                       # speldjup framåt och bakåt
t = d.pas(b, tw + 0.5, rec(d, 'bf0', tw + 1.3)); t = d.pas(b, t + 0.3, rec(d, 'bf1', t + 1.2), 0.9)
d.mv('rb2', t - 1, t + 0.4, (60, 82)); t = d.pas(b, t + 0.3, (54, 101), 0.5); tg = t
for k in range(4): d.mv(f'bm{k}', tw + 0.2, tw + 2.4, (24 + k * 17, 54))                       # flytta upp laget
finish(d, 't67', 'kontring-fran-central-tredjedel', ['Kontring', 'Från central tredjedel'], 'Yta ca 65 × 65 m i tredjedelar · Lag 1 i överläge',
       [(0, 'Målvakten spelar till lag 2:s mittfält', 'Mittfältet får bara vara i den centrala tredjedelen.'),
        (1.8, 'Lag 2 håller bollen centralt', 'Lag 1 (blått) pressar i överläge.'),
        (tw - 0.3, 'Lag 1 vinner bollen och kontrar', 'Bli spelbar direkt vid bollvinst.'),
        (tw + 1, 'Forwards möter lag 2:s backlinje', 'Erbjud speldjup framåt och bakåt i flera korridorer.'),
        (tg, 'Flytta upp laget', 'Vinner lag 2 bollen i egen tredjedel spelar de upp till mittfältet.')],
       'KONTRING', [('line', [(0, 33), (100, 33)]), ('line', [(0, 66), (100, 66)])])
C[-1]['goals'] = [(50, 100)]; C[-1]['keep_goals'] = True

# ============ t68 Speluppbyggnad i tre korridorer ============
d = Drill()
d.p('mv', 'MV', B, (50, 95))
blue = {'vb': (16, 78), 'mb1': (40, 84), 'mb2': (60, 84), 'hb': (84, 78), 'm1': (36, 60), 'm2': (64, 60), 'm3': (50, 46)}
for k, (pid, ps) in enumerate(blue.items()): d.p(pid, str(k + 2), B, ps)
for k, ps in enumerate([(30, 70), (50, 66), (70, 70), (40, 50), (60, 50), (50, 34)]): d.p(f's{k}', str(k + 1), BLACK, ps)
b = d.newball(rec(d, 'mv', 0))
t = chain(d, b, 0.4, ['mb1', 'vb'])                                                     # använd hela bredden
d.mv('s0', 1, t + 0.4, (20, 72)); d.mv('s1', 1.2, t + 0.6, (32, 66))                    # svart flyttar över
t = chain(d, b, t, ['mb1', 'mb2', 'hb'])                                                # byt korridor
d.mv('m2', t - 1, t + 0.2, (58, 56)); t = d.pas(b, t + 0.3, rec(d, 'm2', t + 0.8))      # mittfältaren mellan pressarna
d.mv('m2', t, t + 2, (74, 10)); d.carry(b, 'm2', t, t + 2); tl = t + 2                 # driver över sista linjen
finish(d, 't68', 'speluppbyggnad-i-tre-korridorer', ['Speluppbyggnad', 'I tre korridorer'], 'Halvplan i tre korridorer · Blått bygger upp · Svart pressar',
       [(0, 'Blått bygger upp från målvakten', 'Max tre blå spelare i samma korridor.'),
        (1.2, 'Använd hela bredden innan du spelar framåt', 'Svart pressar.'),
        (3, 'Byt korridor när motståndaren flyttat över', 'Mittfältarna tar position mellan pressarna.'),
        (tl - 1.6, 'Över sista linjen ger en poäng', 'Driv eller passa över linjen.'),
        (tl + 0.4, 'Vinner svart bollen kontrar de', 'Mot det stora målet.')],
       'SPELUPPBYGGNAD', [('line', [(33, 8), (33, 100)]), ('line', [(67, 8), (67, 100)]), ('line', [(0, 8), (100, 8)])], [lab(tl, tl + 2, (74, 16), '+1')])
C[-1]['goals'] = [(50, 100)]; C[-1]['keep_goals'] = True

# ============ t69 Engelska kvadraten med mål ============
d = Drill()
yel = [(16, 14), (36, 24), (60, 14), (84, 22), (50, 28)]
blu = [(16, 86), (36, 76), (60, 86), (84, 78), (50, 72)]
red = [(26, 50), (38, 44), (70, 44), (80, 54), (62, 56)]
for k, ps in enumerate(yel): d.p(f'y{k}', str(k + 1), YEL, ps)
for k, ps in enumerate(blu): d.p(f'b{k}', str(k + 1), B, ps)
for k, ps in enumerate(red): d.p(f'r{k}', str(k + 1), R, ps)
d.p('mv1', 'MV', G, (50, 40)); d.p('mv2', 'MV', G, (50, 60)); d.p('T', 'T', G, (96, 50))
d.mv('r1', 0.3, 1.6, (34, 20)); d.mv('r2', 0.3, 1.6, (66, 20))                                       # två röda pressar
b = d.newball(rec(d, 'y0', 0))
t = chain(d, b, 0.4, ['y1', 'y2', 'y3', 'y4', 'y1']); cnt = arrivals(d, b)[:5]
t = d.pas(b, t + 0.3, (47, 41), 0.6); d.mv('mv1', t - 0.5, t, (46, 40)); tg = t                         # avslut mot målet som vänder sig mot zonen
b2 = newball_at(d, tg + 0.6, (94, 52)); t2 = d.pas(b2, tg + 0.8, rec(d, 'b3', tg + 1.4))                # tränaren slår in boll till blått
d.mv('r1', tg, tg + 1.6, (40, 70)); d.mv('r2', tg, tg + 1.6, (70, 72)); d.mv('r3', tg + 1.4, tg + 2.4, rec(d, 'b3', tg + 2.4))
tw = d.pas(b2, tg + 2.5, rec(d, 'r3', tg + 2.7), 0.3); t3 = d.pas(b2, tw + 0.3, (52, 59), 0.5)       # rött vinner och avslutar direkt
for k, ps in enumerate(red): d.mv(f'b{k}', t3 + 0.4, t3 + 2.6, ps)                                    # blått byter med mittlaget
for k, ps in enumerate(blu): d.mv(f'r{k}', t3 + 0.4, t3 + 2.6, ps)
b3 = newball_at(d, t3 + 2.8, (94, 48)); t4 = d.pas(b3, t3 + 3.0, rec(d, 'y3', t3 + 3.6)); chain(d, b3, t4, ['y2', 'y4', 'y1', 'y0'])
for k, ps in zip([1, 2], [(34, 20), (66, 20)]): d.mv(f'b{k}', t3 + 2.8, t3 + 4.0, ps)
finish(d, 't69', 'engelska-kvadraten-med-mal', ['Engelska kvadraten', 'Med mål'], 'Tre zoner · Två mål rygg mot rygg i mitten · Gult, rött och blått',
       [(0, 'Gult och blått i ytterzonerna, rött i mitten', 'Två röda går in och pressar laget med boll.'),
        (1.6, 'Gör ytan stor', 'Fem passningar innan avslut.'),
        (cnt[-1], 'Avsluta mot målet som vänder sig mot er zon', 'Avsluta snabbt när du har fått rätt.'),
        (tg + 0.6, 'Tränaren slår in en ny boll', 'Pressarna: stäng skottvägen först.'),
        (tw, 'Rött vinner bollen och avslutar direkt', 'Laget som tappar bollen byter med mittlaget.')],
       'RONDO', [('line', [(0, 33), (100, 33)]), ('line', [(0, 67), (100, 67)]), ('box', 43, 42, 57, 58), ('line', [(43, 50), (57, 50)])], counter(cnt, pos=(50, 30)))

# ============ po01 Sex passningar – sen till målvakten ============
d = Drill()
d.p('bmv', 'MV', B, (50, 8)); d.p('rmv', 'MV', R, (50, 92))
for k, ps in enumerate([(30, 30), (64, 34), (70, 64), (36, 60)]): d.p(f'b{k}', str(k + 1), B, ps)
for k, ps in enumerate([(46, 40), (56, 52), (44, 58), (60, 40)]): d.p(f'r{k}', str(k + 1), R, ps)
for k in range(4): wander(d, f'b{k}', 0, 18, (16, 20, 84, 80), 180 + k, 2.0); wander(d, f'r{k}', 0, 18, (24, 26, 76, 74), 190 + k, 1.6)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b1', 'b2', 'b3', 'b0', 'b1', 'b0']); cnt = arrivals(d, b)[:6]
t = d.pas(b, t + 0.3, rec(d, 'bmv', t + 1)); tp = t                                                     # till egen målvakt: poäng
t = d.pas(b, t + 0.3, rec(d, 'b1', t + 1.2))                                                           # målvakten spelar direkt tillbaka
t = chain(d, b, t, ['b2', 'b3'])
finish(d, 'po01', 'sex-passningar-sen-till-malvakten', ['Sex passningar', 'Sen till målvakten'], 'Rektangel · En målvakt i varje kortände · Koner',
       [(0, 'Två lag spelar keep away', 'Snabba och exakta passningar. Rör dig för att öppna passningsvägar.'),
        (cnt[-1] - 0.2, 'Sex passningar i rad', 'Nu får laget spela till sin målvakt.'),
        (tp, 'En poäng', 'Målvakten spelar direkt tillbaka och laget fortsätter.'),
        (tp + 1.5, 'Räkningen börjar om', 'Först till tre poäng vinner. Försvar: pressa direkt eller stäng passningslinjer.')],
       'SPELUPPBYGGNAD', [('box', 10, 14, 90, 86)] + [('cone', x, y) for x, y in [(30, 40), (50, 36), (70, 40), (40, 50), (60, 50), (30, 60), (50, 64), (70, 60), (10, 14), (90, 14), (10, 86), (90, 86)]],
       counter(cnt + [tp]))

# ============ po02 Possession med tre lag – hörnspelare ============
d = Drill()
for k, ps in enumerate([(32, 34), (64, 32), (68, 64), (36, 66)]): d.p(f'b{k}', str(k + 1), B, ps)
for k, ps in enumerate([(46, 44), (56, 50), (46, 58), (58, 40)]): d.p(f'r{k}', str(k + 1), R, ps)
for k, ps in enumerate([(14, 18), (86, 18), (86, 82), (14, 82)]): d.p(f'n{k}', 'N', G, ps)
for k in range(4): wander(d, f'b{k}', 0, 18, (20, 24, 80, 76), 200 + k, 2.0); wander(d, f'r{k}', 0, 18, (28, 30, 72, 70), 210 + k, 1.6)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b1', 'n1', 'b2', 'b3', 'b0', 'b1']); cnt = arrivals(d, b)[:6]                  # hörnet får användas när som helst
tc = cnt[1]
t = d.pas(b, t + 0.3, (84, 20)); tp0 = t; t = d.pas(b, t + 0.4, rec(d, 'b1', t + 1.0)); tp = t          # vägg med hörnspelaren efter sex
t = chain(d, b, t, ['b2', 'b3'])
finish(d, 'po02', 'possession-med-tre-lag-hornspelare', ['Possession med tre lag', 'Hörnspelare'], 'Kvadrat ca 25 × 25 m · En neutral i varje hörn',
       [(0, 'Två lag i mitten, tredje laget i hörnen', 'Hörnspelarna spelar med den som har bollen.'),
        (tc - 0.4, 'Hörnet får användas när som helst', 'Men det ger ingen poäng före sex passningar.'),
        (cnt[-1] - 0.2, 'Sex passningar i rad', 'Rättvänd direkt efter returen.'),
        (tp0 - 0.6, 'Vägg med hörnspelaren ger en poäng', 'Dra med försvarare så hörnet öppnas.'),
        (tp + 0.4, 'Spelet stannar inte vid poäng', 'Först till tre. Byt lag i hörnen.')],
       'SPELUPPBYGGNAD', [('box', 14, 18, 86, 82)], counter(cnt + [tp]))

if __name__ == '__main__':
    render(C, sys.argv)
