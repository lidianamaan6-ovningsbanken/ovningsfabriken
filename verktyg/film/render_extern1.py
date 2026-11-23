# Externa övningar, omgång 1 (tolv st). Regel: först d.mv, sedan d.carry.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('o3', __file__.replace('render_extern1.py', 'render_omgang3.py'))
o3 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(o3); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = o3.finish, o3.rec, o3.chain, o3.wander, o3.counter, o3.arrivals
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'
def lab(t0, t1, pos, text): return dict(kind='label', t0=t0, t1=t1, pos=pos, text=text)
def hide(d, b, t): d.balls[b] += [(t, at(d.balls[b], t)), (t + 0.001, (200, 200))]
def show(d, b, t, pos): d.balls[b] += [(t - 0.001, (200, 200)), (t, pos)]
def team(d, pre, col, pts, labels=None):
    for k, ps in enumerate(pts): d.p(f'{pre}{k}', (labels[k] if labels else str(k + 1)), col, ps)
def boxes(pts, r=6):
    return [(x - r, y - r, x + r, y + r) for x, y in pts]
def drive(d, b, pid, t, to, speed=22):
    sx, sy = d.pos(pid); dur = max(0.6, ((to[0] - sx) ** 2 + (to[1] - sy) ** 2) ** .5 / speed)
    d.mv(pid, t, t + dur, to); d.carry(b, pid, t, t + dur); return t + dur
def shoot(d, b, t, goal): return d.pas(b, t + 0.1, goal)

# ============ b01 Rondo 5 mot 2 med poäng ============
d = Drill(); RP = [(34, 36), (50, 28), (66, 36), (64, 64), (36, 64)]
team(d, 'b', B, RP); team(d, 'r', R, [(46, 48), (56, 52)])
b = d.newball(rec(d, 'b0', 0))
d.mv('r0', 0.3, 3.5, (44, 40)); d.mv('r1', 0.3, 3.5, (60, 46))
t = chain(d, b, 0.4, ['b1', 'b3', 'b2', 'b4', 'b0']); cnt = arrivals(d, b)[:5]; tp = cnt[-1]
d.mv('r0', t - 1.2, t, (38, 54)); t2 = d.pas(b, t + 0.3, rec(d, 'b4', t + 0.9))
d.mv('r0', t2 - 0.6, t2 + 0.2, rec(d, 'b4', t2 + 0.2)); tw = d.pas(b, t2 + 0.3, rec(d, 'r0', t2 + 0.5), 0.3)   # bollvinst
d.mv('r0', tw + 0.3, tw + 1.6, RP[4]); d.mv('b4', tw + 0.3, tw + 1.6, (46, 52))                               # den som tappade går in
d.mv('r1', tw + 0.4, tw + 1.2, (54, 46)); t = chain(d, b, tw + 1.6, ['b3', 'b2', 'b1', 'r0', 'b0'])
finish(d, 'b01', 'rondo-5-mot-2-med-poang', ['Rondo 5 mot 2', 'Med poäng'], '5 mot 2 i en ruta på ca 8 × 8 m',
       [(0, 'Fem runt rutan, två försvarare inne', 'Laget med boll håller den med få touch.'),
        (tp - 0.3, 'Fem passningar i rad: 1 poäng', 'Till laget med boll.'),
        (tw - 0.3, 'Bollvinst: 1 poäng till försvararna', 'Och den som tappade går in.'),
        (tw + 1.6, 'Spelet fortsätter direkt', 'Fler spelare: parallella rutor med 5–7 i varje.')],
       'RONDO', [('box', 32, 30, 68, 70)], counter(cnt) + [lab(tw, tw + 1.6, (50, 22), '+1 FÖRSVAR')])

# ============ b02 Positionsspel 4 mot 4 + 3 jokrar ============
d = Drill()
BP = [(30, 34), (70, 34), (30, 66), (70, 66)]; RPp = [(42, 40), (58, 40), (42, 60), (58, 60)]
team(d, 'b', B, BP); team(d, 'r', R, RPp)
d.p('j1', 'J', G, (50, 16)); d.p('jm', 'J', G, (50, 50)); d.p('j2', 'J', G, (50, 84))
for k in range(4): wander(d, f'b{k}', 0, 18, boxes(BP, 7)[k], 400 + k, 2); wander(d, f'r{k}', 0, 18, boxes(RPp, 5)[k], 410 + k, 1.6)
b = d.newball(rec(d, 'j1', 0))
t = chain(d, b, 0.4, ['b0', 'jm', 'b3', 'j2']); tp = t                                       # från ena kortsidesjokern till den andra
t = chain(d, b, t, ['b2', 'b0', 'j1']); tp2 = t
finish(d, 'b02', 'positionsspel-4-mot-4-plus-3-jokrar', ['Positionsspel 4 mot 4', 'Plus tre jokrar'], 'Ca 30 × 25 m · En joker i varje ände och en i mitten',
       [(0, 'Jokrarna spelar med laget som har bollen', 'Det blir 7 mot 4 i bollinnehav. Jokrarna har två touch.'),
        (1.6, 'Spela via mittjokern', 'Ta bollen från ena kortsidan mot den andra.'),
        (tp - 0.5, 'Ena kortsidesjokern till den andra: poäng', 'Spelet fortsätter åt andra hållet.'),
        (tp2 - 0.5, 'Och tillbaka: ny poäng', 'Laget med boll håller den med få touch.')],
       'SPELUPPBYGGNAD', [('box', 18, 20, 82, 80)], [lab(tp, tp + 1.6, (50, 30), '+1'), lab(tp2, tp2 + 1.6, (50, 70), '+1')])

# ============ b03 Uppspel med säker zon för målvakten ============
d = Drill()
d.p('mv', 'MV', B, (50, 93)); d.p('mvr', 'MV', R, (50, 5))
team(d, 'b', B, [(30, 76), (70, 76), (40, 56), (60, 52), (50, 34)]); d.p('bk1', 'K', B, (4, 50)); d.p('bk2', 'K', B, (96, 50))
team(d, 'r', R, [(38, 70), (62, 68), (50, 58), (44, 40), (56, 30)]); d.p('rk1', 'K', R, (4, 30)); d.p('rk2', 'K', R, (96, 70))
b = d.newball(rec(d, 'mv', 0))
d.mv('r0', 0.5, 2, (36, 76)); d.mv('r1', 0.5, 2, (60, 76))                                   # ingen får pressa i den säkra zonen
t = d.pas(b, 1.2, rec(d, 'b1', 1.8)); t = chain(d, b, t, ['bk2', 'b3', 'b4']); tc = t
d.mv('b2', t - 1, t + 0.8, (38, 24)); t = d.pas(b, t + 0.3, rec(d, 'b2', t + 1.1)); t = shoot(d, b, t + 0.3, (46, 1)); d.mv('mvr', t - 0.5, t, (44, 5)); tg = t
hide(d, b, tg + 0.3); show(d, b, tg + 0.8, rec(d, 'mvr', tg + 0.8))
t = d.pas(b, tg + 1.0, rec(d, 'r4', tg + 1.6)); t = chain(d, b, t, ['r3'])
d.mv('b3', t - 0.6, t + 0.2, rec(d, 'r3', t + 0.2)); tw = d.pas(b, t + 0.3, rec(d, 'b3', t + 0.5), 0.3)       # blått vinner – försvararna här är rött
t = drive(d, b, 'b3', tw, (70, 22)); t = shoot(d, b, t, (80, 1))
finish(d, 'b03', 'uppspel-med-saker-zon-for-malvakten', ['Uppspel med säker zon', 'För målvakten'], 'Ca 50 × 40 m · Stort mål i varje ände och två småmål · Säker zon runt målvakten',
       [(0, 'Anfallande lag startar med målvakten', 'Ingen får pressa i den säkra zonen.'),
        (1.6, 'Kantspelarna utanför planen hjälper till', 'Varje lag har en spelare på varje kant.'),
        (tc - 0.4, 'Kombinera för mål i det stora målet', 'Blått avslutar.'),
        (tg + 1, 'Rött bygger upp från sin målvakt', 'Nu försvarar blått.'),
        (tw - 0.3, 'Försvararna vinner bollen', 'Mål i ett småmål, eller spela till egen målvakt.')],
       'SPELUPPBYGGNAD', [('zone', 32, 86, 68, 100, (120, 200, 160), 'SÄKER ZON'), ('zone', 32, 0, 68, 14, (120, 200, 160), 'SÄKER ZON'), ('smallgoal', 20, 4), ('smallgoal', 80, 4)])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ b04 Spelvändning för poäng ============
d = Drill()
d.p('mv', 'MV', R, (50, 5))
team(d, 'b', B, [(38, 86), (62, 86), (14, 72), (86, 72), (42, 64), (58, 64), (16, 40), (84, 40), (50, 34)])
team(d, 'r', R, [(44, 52), (56, 52), (20, 56), (36, 50), (64, 50), (80, 56), (36, 24), (50, 22), (64, 24)])
b = d.newball(rec(d, 'b0', 0))
for k in range(9): d.mv(f'r{k}', 0.6, 3, (d.pos(f'r{k}')[0] - 10, d.pos(f'r{k}')[1] + 4))            # försvaret stänger ena sidan
t = chain(d, b, 0.4, ['b2', 'b0', 'b1', 'b3']); tv = t                                             # spelvändning mellan korridorerna
for k in range(9): d.mv(f'r{k}', t - 1, t + 1.6, (d.pos(f'r{k}')[0] + 18, d.pos(f'r{k}')[1]))
d.mv('b7', t - 0.6, t + 0.8, (86, 26)); t = d.pas(b, t + 0.2, rec(d, 'b7', t + 1)); t = drive(d, b, 'b7', t, (82, 18))
d.mv('b8', t - 1.2, t, (44, 18)); t = d.pas(b, t + 0.1, rec(d, 'b8', t + 0.6)); t = shoot(d, b, t + 0.2, (50, 1)); tg = t
finish(d, 'b04', 'spelvandning-for-poang', ['Spelvändning', 'För poäng'], '9 mot 9 på halvplan + ca 10 m · Stort mål och två småmål',
       [(0, 'Blått bygger från mittbackarna', 'Rött pressar för att stänga ena sidan.'),
        (2.4, 'Försvarets två anfallare är låsta i mittzonen', 'Hitta vägen förbi pressen.'),
        (tv - 0.6, 'Spelvändning mellan korridorerna: 1 poäng', 'Bollen till den sida pressen lämnat.'),
        (tv + 1.6, 'Mål efter vändning på sista tredjedelen: 3 poäng', 'Försvararna: bollvinst 1 poäng, mål i småmål 3.')],
       'SPELUPPBYGGNAD', [('line', [(0, 33), (100, 33)]), ('line', [(0, 66), (100, 66)]), ('line', [(33, 0), (33, 100)]), ('line', [(67, 0), (67, 100)]), ('smallgoal', 30, 97), ('smallgoal', 70, 97)],
       [lab(tv, tv + 1.6, (86, 64), '+1'), lab(tg, tg + 2, (50, 12), '+3')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ b05 Driv förbi mittlinjen, 4 mot 2 i varje halva ============
d = Drill()
d.p('mvb', 'MV', B, (50, 95)); d.p('mvr', 'MV', R, (50, 5))
team(d, 'b', B, [(26, 76), (74, 76), (40, 62), (60, 62), (30, 30), (70, 30)])
team(d, 'r', R, [(44, 70), (56, 70), (26, 24), (74, 24), (40, 38), (60, 38)])
b = d.newball(rec(d, 'mvb', 0))
t = d.pas(b, 0.6, rec(d, 'b0', 1.3)); t = chain(d, b, t, ['b2', 'b3'])                            # 4 mot 2 i egen halva
t = drive(d, b, 'b3', t, (58, 44)); tc = t                                                           # driva över mittlinjen
d.mv('b2', tc - 1.2, tc + 0.4, (40, 44))                                                            # två får följa med
t = chain(d, b, t, ['b5', 'b4']); t = shoot(d, b, t + 0.2, (44, 1)); tg = t
hide(d, b, tg + 0.3); show(d, b, tg + 0.9, rec(d, 'mvr', tg + 0.9))
d.mv('b2', tg, tg + 2, (40, 62)); d.mv('b3', tg, tg + 2, (60, 62))
t = d.pas(b, tg + 1.0, rec(d, 'r2', tg + 1.6)); t = chain(d, b, t, ['r4', 'r5'])                  # målvakten spelar alltid ut
finish(d, 'b05', 'driv-forbi-mittlinjen-4-mot-2-i-varje-halva', ['Driv förbi mittlinjen', '4 mot 2 i varje halva'], '7 mot 7 eller 8 mot 8 · Planen delad på mitten',
       [(0, 'Målvakten spelar alltid ut', 'Laget med boll har överlägsenhet i egen halva.'),
        (2, 'Bara driva bollen över mittlinjen', 'Det är enda sättet att komma in i motståndarhalvan.'),
        (tc - 0.2, 'Två spelare får följa med: 4 mot 4', 'Försvarare får bara försvara i sin halva.'),
        (tg + 0.8, 'Rött startar från sin målvakt', 'Nu har rött 4 mot 2 i sin halva.')],
       'SPELUPPBYGGNAD', [('line', [(0, 50), (100, 50)])], [lab(tc, tc + 1.6, (60, 50), 'ÖVER LINJEN')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ b06 Anfall och kontring i fyra zoner ============
d = Drill()   # 60 m lång bana ritad vertikalt: zon 1 (10 m), zon 2 (20 m), säker zon (5 m), zon 4 (30 m)
d.p('mv1', 'MV', G, (50, 95)); d.p('mv2', 'MV', G, (50, 5))
team(d, 'b', B, [(40, 86), (60, 86), (50, 80)]); d.p('d1', '1', R, (50, 74))
team(d, 'k', R, [(42, 56), (58, 56)], ['2', '3']); team(d, 'w', R, [(30, 99), (70, 99)], ['4', '5'])
b = d.newball(rec(d, 'mv1', 0))
t = d.pas(b, 0.5, rec(d, 'b0', 1.2)); t = chain(d, b, t, ['b2', 'b1'])                            # 3 mot 1 i första zonen
for pid, ps in [('b0', (38, 54)), ('b1', (62, 52)), ('b2', (50, 60))]: d.mv(pid, t - 0.4, t + 1.6, ps)
t = drive(d, b, 'b1', t, (62, 50)); t = chain(d, b, t, ['b0'])                                     # mot två kontringsspelare
d.mv('k0', t - 0.8, t + 0.2, rec(d, 'b0', t + 0.2)); tw = d.pas(b, t + 0.3, rec(d, 'k0', t + 0.5), 0.3)
d.mv('w0', tw, tw + 1.4, (32, 70))                                                                 # väntande kontringsspelare kliver in
t = d.pas(b, tw + 0.4, rec(d, 'k1', tw + 1)); d.mv('k1', t, t + 1.4, (56, 24)); d.carry(b, 'k1', t, t + 1.4); t += 1.4
d.mv('k0', tw, t, (40, 26)); t = d.pas(b, t + 0.1, rec(d, 'k0', t + 0.6)); t = shoot(d, b, t + 0.2, (46, 1)); tg = t
finish(d, 'b06', 'anfall-och-kontring-i-fyra-zoner', ['Anfall och kontring', 'I fyra zoner'], 'Ca 60 × 18 m i fyra zoner · Mål i båda ändar',
       [(0, 'Anfallarna startar hos målvakten', '3 mot 1 i första zonen.'),
        (2.6, 'Vidare mot två kontringsspelare', 'Bara anfallarna får gå in i den smala säkra zonen.'),
        (tw - 0.3, 'Kontringslaget vinner bollen', 'En väntande kontringsspelare kliver in.'),
        (tw + 0.6, 'Kontringslaget anfaller direkt', 'Mot det andra målet.')],
       'KONTRING', [('line', [(0, 83), (100, 83)]), ('line', [(0, 50), (100, 50)]), ('zone', 0, 42, 100, 50, (120, 200, 160), 'SÄKER ZON')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ b07 Vinn i motståndarens halva och avsluta ============
d = Drill()
d.p('mvb', 'MV', B, (50, 94)); d.p('mvr', 'MV', R, (50, 6))
team(d, 'b', B, [(30, 70), (70, 70), (40, 44), (60, 40)]); team(d, 'r', R, [(36, 30), (64, 30), (44, 58), (58, 56)])
b = d.newball(rec(d, 'mvr', 0))
t = d.pas(b, 0.4, rec(d, 'r0', 1.0)); t = chain(d, b, t, ['r1'])
d.mv('b3', 0.8, t + 0.2, rec(d, 'r1', t + 0.2)); d.mv('b2', 0.8, t + 0.2, (48, 30))               # press högt
t2 = d.pas(b, t + 0.3, rec(d, 'r0', t + 1)); d.mv('b2', t + 0.2, t2 + 0.1, rec(d, 'r0', t2 + 0.1)); tw = d.pas(b, t2 + 0.2, rec(d, 'b2', t2 + 0.4), 0.3)   # vinner i motståndarens halva
t = drive(d, b, 'b2', tw, (44, 22)); t = shoot(d, b, t, (46, 1)); tg = t
hide(d, b, tg + 0.3); show(d, b, tg + 0.9, rec(d, 'mvr', tg + 0.9))
t = d.pas(b, tg + 1.0, rec(d, 'r1', tg + 1.5)); t = chain(d, b, t, ['r2', 'r3'])
finish(d, 'b07', 'vinn-i-motstandarens-halva-och-avsluta', ['Vinn i motståndarens halva', 'Och avsluta'], 'Smålagsspel med mittlinje',
       [(0, 'Vanligt smålagsspel', 'Rött spelar ut från målvakten.'),
        (1.4, 'Blått pressar högt', 'Försök vinna bollen i motståndarens halva.'),
        (tw - 0.3, 'Bollvinst i motståndarens halva', 'Gör mål innan bollen hamnar i egen halva.'),
        (tg, 'Mål räknas som tre', 'Gärna flera parallella planer.')],
       'KONTRING', [('line', [(0, 50), (100, 50)])], [lab(tg, tg + 2.2, (50, 14), '+3')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ b16 4 mot 4 – en passning innan mål ============
d = Drill()
team(d, 'b', B, [(30, 70), (70, 70), (40, 52), (60, 52)]); team(d, 'r', R, [(36, 34), (64, 34), (44, 46), (56, 46)]); d.p('T', 'T', G, (96, 50))
b = d.newball((94, 52)); t = d.pas(b, 0.6, rec(d, 'b3', 1.4))                                      # tränaren spelar in en boll
d.mv('r3', t - 0.4, t + 0.6, (60, 46))
t = drive(d, b, 'b3', t, (66, 40)); t = d.pas(b, t + 0.1, rec(d, 'b2', t + 0.7)); tp = t           # minst en passning
t = drive(d, b, 'b2', t, (44, 24)); t = shoot(d, b, t, (46, 5)); tg = t
b2 = d.newball((200, 200)); d.balls[b2] = [(0, (200, 200)), (tg + 0.6, (200, 200)), (tg + 0.601, (94, 52))]
t = d.pas(b2, tg + 0.8, rec(d, 'r2', tg + 1.4)); t = chain(d, b2, t, ['r0'])
d.mv('r1', t - 1, t + 0.4, (66, 60)); t = d.pas(b2, t + 0.1, rec(d, 'r1', t + 0.7)); t = drive(d, b2, 'r1', t, (60, 80)); shoot(d, b2, t, (54, 95))
finish(d, 'b16', '4-mot-4-en-passning-innan-mal', ['4 mot 4', 'En passning innan mål'], 'Ca 32 × 18 m utan målvakter · Matcher om två minuter',
       [(0, 'Tränaren spelar in en boll', 'Lagen försvarar var sin kortsida.'),
        (tp - 0.6, 'Minst en passning innan mål', 'Annars räknas inte målet.'),
        (tg - 0.6, 'Mål', 'Ny boll från tränaren direkt.'),
        (tg + 1.2, 'Rött anfaller åt andra hållet', 'Byt lag efter varje match.')],
       'ÅTERERÖVRING', [('box', 14, 6, 86, 94), ('ugoal', 50, 6, 'up'), ('ugoal', 50, 94, 'down')], [lab(tp, tp + 1.4, (50, 36), '1 PASSNING')])

# ============ b17 Snabbt mål efter bollvinst ============
d = Drill()
d.p('mvb', 'MV', B, (50, 94)); d.p('mvr', 'MV', R, (50, 6))
team(d, 'b', B, [(30, 70), (70, 70), (42, 50), (60, 46)]); team(d, 'r', R, [(34, 34), (66, 30), (46, 60), (58, 58)])
b = d.newball(rec(d, 'r2', 0))
t = chain(d, b, 0.4, ['r3', 'r1'])
d.mv('b3', t - 0.8, t + 0.2, rec(d, 'r1', t + 0.2)); tw = d.pas(b, t + 0.3, rec(d, 'b3', t + 0.5), 0.3)        # bollvinst
t = drive(d, b, 'b3', tw, (56, 22)); t = shoot(d, b, t, (46, 1)); tg = t
hide(d, b, tg + 0.3); show(d, b, tg + 0.9, rec(d, 'mvr', tg + 0.9))
t = d.pas(b, tg + 1.0, rec(d, 'r0', tg + 1.5)); t = chain(d, b, t, ['r2', 'r3'])
finish(d, 'b17', 'snabbt-mal-efter-bollvinst', ['Snabbt mål', 'Efter bollvinst'], 'Smålagsspel på flera parallella planer',
       [(0, 'Fritt spel', 'Rött har bollen.'),
        (tw - 0.3, 'Bollvinst – tre sekunder på sig', 'Mål inom tre sekunder räknas dubbelt.'),
        (tg, 'Mål inom tre sekunder: dubbelt', 'Spelet fortsätter från målvakten.')],
       'ÅTERERÖVRING', [], [lab(tw + i, tw + i + 1, (50, 40), f'{3 - i} SEK') for i in range(3)] + [lab(tg, tg + 2, (50, 14), 'x2')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ b18 Grindrace 1 mot 1 ============
d = Drill(); balls = []
for k, x in enumerate([22, 50, 78]):
    d.p(f'p{k}', 'P', B, (x - 6, 80)); d.p(f'q{k}', 'M', R, (x + 6, 80))
for k, x in enumerate([22, 50, 78]):
    bb = d.newball(rec(d, f'p{k}', 0)); t0 = 0.6 + k * 0.4
    t = d.pas(bb, t0, (x + 1, 60)); d.mv(f'q{k}', t0, t, (x + 1, 58))                              # passning genom grinden till partnern
    t = drive(d, bb, f'q{k}', t, (x + 2, 26)); d.mv(f'p{k}', t0 + 0.2, t + 0.2, (x - 3, 26))       # passaren försöker komma först
    d.mv(f'p{k}', t + 0.3, t + 2.6, (x + 6, 80)); d.mv(f'q{k}', t + 0.3, t + 2.6, (x - 6, 80)); d.carry(bb, f'q{k}', t + 0.3, t + 2.6)   # byt roller
finish(d, 'b18', 'grindrace-1-mot-1', ['Grindrace', '1 mot 1'], 'Par med en grind och en kon',
       [(0, 'Passa genom grinden till din partner', 'Partnern driver mot konen.'),
        (1.8, 'Passaren försöker komma först', 'Snabb reaktion efter passningen.'),
        (4.6, 'Tillbaka och byt roller', 'Byt roller efter fem försök.')],
       'ÅTERERÖVRING', [('cone', x + dx, 66) for x in (22, 50, 78) for dx in (-3, 5)] + [('cone', x + 2, 22) for x in (22, 50, 78)])

# ============ b20 8 mot 6 pressfas på halvplan ============
d = Drill()
d.p('mv', 'MV', B, (50, 94))
team(d, 'b', B, [(34, 84), (66, 84), (12, 72), (88, 72), (42, 64), (58, 64), (30, 46), (70, 46)])
team(d, 'r', R, [(42, 74), (58, 74), (24, 66), (76, 66), (50, 56), (50, 40)])
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b1', 'b5'])
d.mv('r4', t - 0.8, t + 0.4, (60, 60)); t = d.pas(b, t + 0.3, rec(d, 'b7', t + 1)); tpass = t      # en pressare passeras
for k in range(6): d.mv(f'r{k}', t, t + 1.6, (d.pos(f'r{k}')[0] + 5, d.pos(f'r{k}')[1] - 7))           # alla faller ner ett steg
t = drive(d, b, 'b7', t, (72, 30)); tl = t                                                          # förbi linjen
d.mv('b6', t - 1.4, t, (34, 22)); t = d.pas(b, t + 0.1, rec(d, 'b6', t + 0.7)); t = shoot(d, b, t + 0.2, (30, 3))
finish(d, 'b20', '8-mot-6-pressfas-pa-halvplan', ['8 mot 6', 'Pressfas på halvplan'], 'Halvplan ca 50 m bred · Småmål bakom en linje',
       [(0, 'Omstart från mittback', 'Även från ytterback, mittfältare eller målvakt.'),
        (tpass - 0.7, 'En pressande spelare blir passerad', 'Då faller alla ner ett steg.'),
        (tl - 0.6, 'Förbi linjen innan mål', 'Sedan mål i något av småmålen.'),
        (tl + 1.3, 'Faser om 6 minuter', 'Två gånger, sedan byter lagen.')],
       'FÖRHINDRA SPELUPPBYGGNAD', [('line', [(0, 30), (100, 30)]), ('smallgoal', 30, 4), ('smallgoal', 70, 4)], [lab(tpass, tpass + 1.6, (50, 50), 'NER ETT STEG')])
C[-1]['goals'] = [(50, 100)]; C[-1]['keep_goals'] = True

# ============ b22 7 mot 7: spela in i målvaktens händer ============
d = Drill()
d.p('mvb', 'MV', B, (50, 92)); d.p('mvr', 'MV', R, (50, 8))
team(d, 'b', B, [(30, 72), (70, 72), (50, 62), (24, 46), (76, 46), (40, 34), (60, 34)])
team(d, 'r', R, [(34, 26), (66, 26), (50, 38), (28, 54), (72, 54), (42, 64), (58, 64)])
b = d.newball(rec(d, 'b2', 0))
for k in range(7): d.mv(f'r{k}', 0.4, 2.4, (d.pos(f'r{k}')[0] * 0.8 + 10, d.pos(f'r{k}')[1] + 6))   # pressar som en enhet
t = chain(d, b, 0.4, ['b0', 'b3', 'b5'])
t = d.pas(b, t + 0.3, rec(d, 'mvr', t + 1.2), 1.1); tg = t                                          # spelar in i målvaktens händer
d.mv('mvr', tg - 0.6, tg, (48, 10))
t = d.pas(b, tg + 0.8, rec(d, 'r3', tg + 1.6)); t = chain(d, b, t, ['r5', 'r2'])
finish(d, 'b22', '7-mot-7-spela-in-i-malvaktens-hander', ['7 mot 7', 'Spela in i målvaktens händer'], 'Mellan straffområdena · Ca 55 m bred plan',
       [(0, 'Lagen pressar som en enhet', 'Målvakterna får bara röra sig i straffområdet.'),
        (2.2, 'Hitta vägen förbi pressen', 'Mål görs från var som helst på planen.'),
        (tg - 1.1, 'Spela så att målvakten kan fånga bollen', 'Det är ett mål.'),
        (tg + 0.8, 'Målvakten startar nytt anfall', 'Nu anfaller rött.')],
       'FÖRHINDRA SPELUPPBYGGNAD', [('box', 30, 0, 70, 16), ('box', 30, 84, 70, 100)], [lab(tg, tg + 2, (50, 22), 'MÅL')])

if __name__ == '__main__':
    render(C, sys.argv)
