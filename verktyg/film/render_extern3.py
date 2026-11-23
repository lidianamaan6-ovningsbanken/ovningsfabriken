# Externa övningar, omgång 3 (tolv st). Regel: först d.mv, sedan d.carry; hide före show.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e1', __file__.replace('render_extern3.py', 'render_extern1.py'))
e1 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e1); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e1.finish, e1.rec, e1.chain, e1.wander, e1.counter, e1.arrivals
lab, hide, show, team, boxes, drive, shoot = e1.lab, e1.hide, e1.show, e1.team, e1.boxes, e1.drive, e1.shoot
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'

# ============ g01 4 mot 2 med målspelare ============
d = Drill()
L = [(14, 30), (40, 28), (40, 70), (14, 72)]; Rr = [(60, 30), (86, 28), (86, 70), (60, 72)]
team(d, 'b', B, L); team(d, 'r', R, [(24, 46), (32, 56)]); team(d, 'w', WHITE, Rr); team(d, 'y', YEL, [(70, 46), (78, 56)])
team(d, 'n', G, [(50, 40), (50, 60)], ['M', 'M'])
for k in range(4): wander(d, f'b{k}', 0, 18, boxes(L, 4)[k], 500 + k, 2); wander(d, f'w{k}', 0, 18, boxes(Rr, 4)[k], 510 + k, 2)
for k in range(2): wander(d, f'r{k}', 0, 18, (18, 34, 36, 64), 520 + k, 1.6); wander(d, f'y{k}', 0, 18, (64, 34, 82, 64), 530 + k, 1.6)
b = d.newball(rec(d, 'b0', 0)); b2 = d.newball(rec(d, 'w0', 0))
t = chain(d, b, 0.4, ['b1', 'b2', 'b3', 'b0', 'b1', 'b2', 'b3', 'b0']); cnt = arrivals(d, b)[:8]
t = d.pas(b, t + 0.3, rec(d, 'n0', t + 0.9)); tp = t; t = d.pas(b, t + 0.3, rec(d, 'b1', t + 0.9))   # till målspelaren: poäng
chain(d, b2, 0.8, ['w1', 'w3', 'w2', 'w0', 'w1', 'w3', 'w2', 'w1'])
finish(d, 'g01', '4-mot-2-med-malspelare', ['4 mot 2', 'Med målspelare'], 'Två rutor och en mittzon · 4 mot 2 i varje ruta · Två målspelare i mitten',
       [(0, 'Fyra håller bollen mot två', 'Alla spelar inne i rutan, inte på linjerna.'),
        (cnt[-1] - 0.3, 'Åtta passningar i rad', 'Nu får laget passa till en målspelare.'),
        (tp - 0.6, 'Till målspelaren: 1 poäng', 'Målspelaren spelar tillbaka.'),
        (tp + 0.8, 'Byt försvarare och målspelare varannan minut', 'Max tre touch som variant.')],
       'RONDO', [('box', 8, 22, 46, 78), ('box', 54, 22, 92, 78), ('zone', 46, 22, 54, 78, (200, 220, 200), '')], counter(cnt + [tp], pos=(27, 16)))

# ============ g02 Gegenpressing 7 mot 6 till tomt mål ============
d = Drill(); d.p('mv', 'MV', R, (50, 6))
team(d, 'b', B, [(20, 80), (40, 84), (60, 84), (80, 80), (34, 62), (66, 62), (50, 50)])
team(d, 'r', R, [(28, 26), (44, 22), (56, 22), (72, 26), (40, 40), (60, 40)])
b = d.newball(rec(d, 'b1', 0))
t = chain(d, b, 0.4, ['b4', 'b6', 'b5'])
d.mv('r5', t - 0.6, t + 0.2, rec(d, 'b5', t + 0.2)); tl = d.pas(b, t + 0.3, rec(d, 'r5', t + 0.5), 0.3)   # bollförlust
for pid, ps in [('b5', (60, 46)), ('b6', (54, 48)), ('b4', (46, 50))]: d.mv(pid, tl, tl + 1.0, ps)       # sätt efter direkt
d.mv('r5', tl, tl + 0.8, (60, 48)); t = d.pas(b, tl + 0.9, rec(d, 'r4', tl + 1.5)); d.mv('b4', t - 0.6, t + 0.2, rec(d, 'r4', t + 0.2))
tw = d.pas(b, t + 0.3, rec(d, 'b4', t + 0.5), 0.3)                                              # återerövring
t = drive(d, b, 'b4', tw, (44, 28)); t = shoot(d, b, t, (46, 1))
finish(d, 'g02', 'gegenpressing-7-mot-6-till-tomt-mal', ['Gegenpressing 7 mot 6', 'Till tomt mål'], 'Stort mål med målvakt · Tomt mål utanför planen i andra änden',
       [(0, 'Anfallet startar från egen kortlinje', 'Sju anfallare mot sex försvarare.'),
        (tl - 0.3, 'Bollförlust', 'Försvararna vill passa i det tomma målet.'),
        (tl + 0.3, 'Sätt efter direkt', 'Närmaste spelarna pressar och stänger passningen.'),
        (tw - 0.2, 'Återerövring – anfall igen', 'Spelperioder på 3 minuter.')],
       'OMSTÄLLNING', [('smallgoal', 50, 98), ('line', [(0, 92), (100, 92)])])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ g03 Gegenpressing 6 mot 6 + 1 till vält mål ============
d = Drill(); d.p('mv', 'MV', R, (50, 6)); d.p('n', 'N', G, (50, 50))
team(d, 'b', B, [(24, 78), (50, 82), (76, 78), (36, 60), (64, 60), (50, 40)])
team(d, 'r', R, [(32, 26), (50, 22), (68, 26), (40, 44), (60, 44), (50, 62)])
b = d.newball(rec(d, 'b1', 0))
t = chain(d, b, 0.4, ['b3', 'n', 'b4'])
d.mv('r4', t - 0.6, t + 0.2, rec(d, 'b4', t + 0.2)); tw = d.pas(b, t + 0.3, rec(d, 'r4', t + 0.5), 0.3)
for pid, ps in [('b4', (60, 50)), ('b5', (56, 46)), ('b3', (48, 54))]: d.mv(pid, tw, tw + 1, ps)        # gegenpress
t = d.pas(b, tw + 0.8, rec(d, 'r5', tw + 1.6)); t = d.pas(b, t + 0.2, (50, 96), 0.9); tg = t         # passar i det välta målet
finish(d, 'g03', 'gegenpressing-6-mot-6-plus-1-till-valt-mal', ['Gegenpressing 6 mot 6 + 1', 'Till vält mål'], 'Mål med målvakt i ena änden · Vält mål i andra',
       [(0, 'Anfallet startar från egen kortlinje', 'Båda lagen får använda den neutrala spelaren.'),
        (tw - 0.3, 'Rött vinner bollen', 'Blått sätter press direkt.'),
        (tw + 1, 'Pass i det välta målet = mål', 'Inga hörnor, inspark eller inkast.'),
        (tg + 0.4, 'Spelperioder på 3 minuter', 'Nytt anfall från kortlinjen.')],
       'ÅTERERÖVRING', [('ugoal', 50, 96, 'down')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ g04 4 mot 4 + 2 anspelare, direktspel ============
d = Drill(); d.p('mvb', 'MV', B, (50, 94)); d.p('mvr', 'MV', R, (50, 6))
team(d, 'b', B, [(32, 72), (68, 72), (40, 50), (60, 48)]); team(d, 'r', R, [(34, 30), (66, 30), (44, 58), (56, 40)])
team(d, 'ba', B, [(26, 4), (74, 4)], ['A', 'A']); team(d, 'ra', R, [(26, 96), (74, 96)], ['A', 'A'])
b = d.newball(rec(d, 'mvb', 0))
t = d.pas(b, 0.5, rec(d, 'b0', 1.2)); t = chain(d, b, t, ['b2', 'b3'], 0.15)                         # bara direktspel
d.mv('b3', t, t + 0.8, (60, 28)); t = d.pas(b, t + 0.15, rec(d, 'ba1', t + 1.1), 1.0)
t = d.pas(b, t + 0.1, rec(d, 'b3', t + 0.7)); t = shoot(d, b, t + 0.1, (54, 1)); tg = t               # direkt efter anspelare: dubbelt
finish(d, 'g04', '4-mot-4-plus-2-anspelare-direktspel', ['4 mot 4 + 2 anspelare', 'Direktspel'], 'Målvakt och två anspelare per lag bredvid motståndarens mål',
       [(0, 'Anfallet startar från målvakten', 'Anfallarna spelar bara direkt.'),
        (2, 'Använd anspelarna', 'De står bredvid motståndarens mål och får användas när som helst.'),
        (tg - 0.8, 'Mål direkt efter anspelarens passning', 'Räknas dubbelt.'),
        (tg + 0.4, 'Perioder på 3 minuter', 'Nytt anfall från målvakten.')],
       'KONTRING', [], [lab(tg, tg + 2, (50, 14), 'x2')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ g06 4 mot 3 med kontring över konlinje ============
d = Drill(); d.p('mv', 'MV', R, (50, 6))
team(d, 'b', B, [(24, 76), (42, 80), (58, 80), (76, 76)]); team(d, 'r', R, [(34, 30), (50, 26), (66, 30)])
b = d.newball(rec(d, 'b1', 0))
t = chain(d, b, 0.4, ['b0', 'b2', 'b3'], 0.2)
d.mv('b3', t, t + 1.4, (74, 30)); d.carry(b, 'b3', t, t + 1.4); t += 1.4
d.mv('b1', t - 1.4, t, (46, 22)); t = d.pas(b, t + 0.1, rec(d, 'b1', t + 0.7)); t = shoot(d, b, t + 0.05, (44, 1)); tg = t   # direktmål
d.balls[b] += [(tg + 0.3, at(d.balls[b], tg + 0.3)), (tg + 0.301, (200, 200)), (tg + 2.499, (200, 200)), (tg + 2.5, rec(d, 'b0', tg + 2.5))]
for pid, ps in [('b0', (24, 76)), ('b1', (42, 80)), ('b2', (58, 80)), ('b3', (76, 76))]: d.mv(pid, tg, tg + 2.4, ps)
t = d.pas(b, tg + 2.7, rec(d, 'b2', tg + 3.3))
d.mv('r1', t - 2.0, t - 0.4, (56, 62)); d.mv('r1', t - 0.4, t + 0.2, rec(d, 'b2', t + 0.2)); tw = d.pas(b, t + 0.3, rec(d, 'r1', t + 0.5), 0.3)   # försvaret kliver upp och vinner
t = drive(d, b, 'r1', tw, (52, 92)); tc = t                                                       # kontring över konlinjen
finish(d, 'g06', '4-mot-3-med-kontring-over-konlinje', ['4 mot 3', 'Med kontring över konlinje'], 'Fyra anfallare mot tre försvarare · En konlinje per plan',
       [(0, 'Anfallet startar på kortlinjen', 'Gör så många mål som möjligt.'),
        (tg - 0.8, 'Direktmål räknas dubbelt', 'Nytt anfall direkt.'),
        (tw - 0.2, 'Försvararna vinner bollen', 'Och kontrar över konlinjen.'),
        (tc - 0.4, 'Kontringsmål räknas dubbelt', 'Perioder på 3 minuter, sedan byts försvararna.')],
       'FÖRHINDRA AVSLUT', [('cone', x, 92) for x in range(10, 95, 10)], [lab(tg, tg + 1.6, (50, 14), 'x2'), lab(tc, tc + 1.6, (52, 86), 'x2')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ i01 Lejonburen ============
d = Drill(); IN = [(36, 36), (62, 34), (66, 62), (38, 64), (50, 50)]; OUT = [(50, 14), (14, 50), (86, 50)]
team(d, 'b', B, IN); team(d, 'r', R, [(44, 44), (58, 56)]); team(d, 'u', B, OUT, ['U', 'U', 'U'])
balls = []
for k in range(5):
    wander(d, f'b{k}', 0, 18, boxes(IN, 9)[k], 540 + k, 1.8); balls.append(d.newball(rec(d, f'b{k}', 0)))
    if k not in (1, 3): d.carry(balls[k], f'b{k}', 0, 18)
wander(d, 'r0', 0, 3, (30, 30, 70, 70), 560, 1.4); wander(d, 'r1', 0, 6, (30, 30, 70, 70), 561, 1.4)
d.carry(balls[1], 'b1', 0, 3.4); t = d.pas(balls[1], 3.5, rec(d, 'u0', 4.1)); tp = t                 # passning till spelare utanför
d.mv('u0', t + 0.2, t + 1.6, (60, 30)); d.carry(balls[1], 'u0', t + 0.2, 18); d.mv('b1', t + 0.2, t + 1.6, (50, 14))   # byter plats
d.carry(balls[3], 'b3', 0, 6.4); d.mv('r1', 6, 6.6, rec(d, 'b3', 6.6)); tw = d.pas(balls[3], 6.7, rec(d, 'r1', 6.9), 0.3)   # vinner bollen
d.mv('r1', tw, tw + 1, (40, 60)); d.carry(balls[3], 'r1', tw, 18); d.mv('b3', tw, tw + 1.4, (52, 56))   # byter roll
wander(d, 'b3', tw + 1.4, 18, (36, 40, 64, 66), 562, 1.4); wander(d, 'r1', tw + 1, 18, (28, 50, 50, 70), 563, 1.8)
wander(d, 'r0', 3, 18, (30, 30, 70, 70), 564, 1.4); wander(d, 'u0', tw, 18, (40, 22, 70, 46), 565, 1.8); d.carry(balls[1], 'u0', tw, 18)
finish(d, 'i01', 'lejonburen', ['Lejonburen', 'Rondo med fem bollar'], '12 × 12 m · Fem med boll inne · Två försvarare inne · Tre utanför',
       [(0, 'Fem spelare driver med boll i rutan', 'Två med västar försöker vinna bollar.'),
        (tp - 0.6, 'Passning till en spelare utanför', 'Då byter de två plats.'),
        (tw - 0.2, 'Försvararen vinner en boll', 'Den som vann byter roll med den som tappade.'),
        (tw + 2, 'Lyft blicken och skydda bollen', 'Använd spelarna utanför.')],
       'RONDO', [('box', 26, 26, 74, 74)])

# ============ i03 Underlättad uppbyggnad i sidozoner ============
d = Drill()
team(d, 'b', B, [(18, 70), (34, 84), (34, 56)]); team(d, 'r', R, [(26, 56), (28, 36)])
team(d, 'w', WHITE, [(66, 70), (82, 84), (82, 56)]); team(d, 'y', YEL, [(74, 56), (72, 36)])
team(d, 'h', G, [(50, 40), (50, 70)], ['H', 'H'])
b = d.newball(rec(d, 'b1', 0))
t = chain(d, b, 0.4, ['b0', 'b2'])
t = d.pas(b, t + 0.3, rec(d, 'h1', t + 1)); tp = t                                                  # passning till hjälpare: poäng
t = d.pas(b, t + 0.3, rec(d, 'b2', t + 1)); d.mv('b2', t, t + 1.4, (30, 24)); d.carry(b, 'b2', t, t + 1.4); t += 1.4
t = shoot(d, b, t + 0.1, (24, 4)); tg = t                                                         # mål – rollerna byts
for k, ps in enumerate([(18, 70), (34, 84), (34, 56)]): d.mv(f'r{k}' if k < 2 else 'b2', tg, tg + 1.6, ps if k == 2 else [(26, 66), (20, 80)][k])
finish(d, 'i03', 'underlattad-uppbyggnad-i-sidozoner', ['Underlättad uppbyggnad', 'I sidozoner'], '16 × 32 m · Två sidozoner 3 mot 2 med mål · Två hjälpare i mitten',
       [(0, 'Bygg upp i sidozonen i överläge', '3 mot 2.'),
        (tp - 0.7, 'Passning till en hjälpare: 1 poäng', 'Hjälparna kan också användas för att byta sida.'),
        (tp + 0.4, 'Fortsätt mot mål', 'Rätt läge efter hjälparen.'),
        (tg, 'Mål – rollerna byts', 'Kan anpassas för 9 eller 15 spelare.')],
       'SPELUPPBYGGNAD', [('box', 10, 10, 42, 92), ('box', 58, 10, 90, 92), ('smallgoal', 26, 6), ('smallgoal', 74, 6)], [lab(tp, tp + 1.6, (50, 80), '+1')])

# ============ i04 10 mot 8: kort och smalt i pressen ============
d = Drill(); d.p('mv', 'MV', B, (50, 94)); d.p('T', 'T', G, (96, 60))
team(d, 'b', B, [(30, 82), (70, 82), (12, 66), (88, 66), (40, 64), (60, 64), (26, 46), (74, 46)])
team(d, 'r', R, [(36, 76), (64, 76), (22, 60), (78, 60), (44, 56), (56, 56), (34, 42), (66, 42), (50, 36), (50, 24)])
b = d.newball((94, 62)); t = d.pas(b, 0.6, rec(d, 'b1', 1.4))                                     # tränarens passning startar pressen
for k in range(10): d.mv(f'r{k}', t - 0.4, t + 1.2, (min(90, d.pos(f'r{k}')[0] * 0.7 + 22), d.pos(f'r{k}')[1] + 4))   # kort och smalt
t = chain(d, b, t, ['b5', 'b4', 'b0', 'mv', 'b1', 'b3', 'b7', 'b5', 'b0']); cnt = arrivals(d, b)[1:11]
finish(d, 'i04', '10-mot-8-kort-och-smalt-i-pressen', ['10 mot 8', 'Kort och smalt i pressen'], '10 försvarare mot 8 plus målvakt i motståndarens planhalva',
       [(0, 'Tränarens passning startar pressen', 'De tio jobbar med inövade signaler.'),
        (1.6, 'Kort och smalt', 'Laget står ihop och stänger mitten.'),
        (5, 'De åtta håller bollen med målvakten', 'Tio passningar i rad ger 1 poäng.'),
        (cnt[-1] - 0.5 if len(cnt) > 9 else 10, 'Varianter', 'Ta bollen över mittlinjen eller mål i småmål vid mittlinjen.')],
       'FÖRHINDRA SPELUPPBYGGNAD', [('line', [(0, 30), (100, 30)])], counter(cnt[:10], pos=(50, 14)))
C[-1]['goals'] = [(50, 100)]; C[-1]['keep_goals'] = True

# ============ i05 Positionsspel 5 mot 5 + 5 jokrar ============
d = Drill()
BP = [(36, 36), (64, 36), (50, 50), (36, 64), (64, 64)]; RP_ = [(44, 42), (56, 42), (44, 58), (56, 58), (50, 30)]
team(d, 'b', B, BP); team(d, 'r', R, RP_); team(d, 'j', G, [(50, 14), (14, 34), (86, 34), (14, 66), (86, 66)], ['J'] * 5)
for k in range(5): wander(d, f'b{k}', 0, 18, boxes(BP, 6)[k], 570 + k, 2); wander(d, f'r{k}', 0, 18, boxes(RP_, 4)[k], 580 + k, 1.6)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['j1', 'b2', 'j2', 'b1', 'j0', 'b0', 'b3', 'j3', 'b4', 'j4']); cnt = arrivals(d, b)[:10]
finish(d, 'i05', 'positionsspel-5-mot-5-plus-5-jokrar', ['Positionsspel 5 mot 5', 'Plus fem jokrar'], '30 × 20 eller 35 × 25 m · Fem jokrar runt ytan',
       [(0, 'Jokrarna spelar med laget som har bollen', 'Rollerna har olika antal touch.'),
        (2.5, 'Jokrar ett touch', 'Mittbackar tre touch, innermittfältare två touch.'),
        (cnt[-1] - 0.5, 'Tio passningar i rad: 1 poäng', 'Räkningen börjar om.')],
       'SPELUPPBYGGNAD', [('box', 18, 22, 82, 78)], counter(cnt, pos=(50, 6)))

# ============ i06 6 mot 8 i egen halva, sedan kontring 4 mot 2 ============
d = Drill(); d.p('mvb', 'MV', B, (50, 95)); d.p('mvr', 'MV', R, (50, 5))
team(d, 'b', B, [(28, 82), (44, 84), (56, 84), (72, 82), (40, 70), (60, 70)])
team(d, 'r', R, [(22, 64), (78, 64), (36, 60), (64, 60), (50, 66), (30, 76), (70, 76), (50, 56)])
team(d, 'f', B, [(30, 36), (44, 30), (56, 30), (70, 36)], ['7', '8', '9', '10']); team(d, 'd', R, [(42, 20), (58, 20)], ['9', '10'])
b = d.newball(rec(d, 'r4', 0))
t = chain(d, b, 0.4, ['r2', 'r0', 'r5'])
d.mv('b0', t - 0.6, t + 0.2, rec(d, 'r5', t + 0.2)); tw = d.pas(b, t + 0.3, rec(d, 'b0', t + 0.5), 0.3)
t = d.pas(b, tw + 0.3, rec(d, 'f1', tw + 1.4), 1.2); tp = t                                          # till de fyra
for pid, ps in [('f0', (26, 18)), ('f2', (62, 16)), ('f3', (76, 22))]: d.mv(pid, tp - 0.6, tp + 1.6, ps)
t = chain(d, b, t, ['f3', 'f2']); t = shoot(d, b, t + 0.1, (56, 1))
finish(d, 'i06', '6-mot-8-i-egen-halva-sedan-kontring-4-mot-2', ['6 mot 8 i egen halva', 'Sedan kontring 4 mot 2'], 'Sex plus målvakt mot åtta · Fyra lagkamrater i andra halvan',
       [(0, 'De sex försvarar mot åtta', 'I sin egen halva.'),
        (tw - 0.3, 'Bollvinst', 'Passa direkt till de fyra bortom mittlinjen.'),
        (tp - 0.4, 'Kontring 4 mot 2', 'Plus målvakt i andra halvan.'),
        (tp + 2.2, 'Avsluta', 'Sedan nytt anfall för de åtta.')],
       'OMSTÄLLNING', [('line', [(0, 50), (100, 50)])])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ s01 Utnyttja överläget via kantneutral ============
d = Drill(); d.p('mvb', 'MV', B, (50, 95)); d.p('mvr', 'MV', R, (50, 5))
team(d, 'b', B, [(34, 80), (66, 80), (40, 30), (60, 26), (50, 18)]); team(d, 'r', R, [(40, 70), (60, 70), (36, 20), (64, 20), (50, 34)])
d.p('nm', 'N', G, (50, 50)); d.p('nv', 'N', G, (4, 50)); d.p('nh', 'N', G, (96, 50))
b = d.newball(rec(d, 'mvb', 0))
t = d.pas(b, 0.5, rec(d, 'b0', 1.2)); t = chain(d, b, t, ['b1'])                                  # 3 mot 2 i egen halva
t = d.pas(b, t + 0.3, rec(d, 'nv', t + 1.2), 1.0); tin = t                                        # till kantneutralen i motsatt korridor
t = d.pas(b, t + 0.1, rec(d, 'b2', t + 0.8)); d.mv('nm', tin - 1, tin + 0.6, (50, 38))         # spelar direkt vidare: 3 mot 2
t = chain(d, b, t, ['b4']); d.mv('b3', t - 1, t, (60, 14)); t = d.pas(b, t + 0.1, rec(d, 'b3', t + 0.6)); t = shoot(d, b, t + 0.1, (54, 1)); tg = t
finish(d, 's01', 'utnyttja-overlaget-via-kantneutral', ['Utnyttja överläget', 'Via kantneutral'], 'Två lag om fem plus tre neutrala · 3 mot 2 i varje halva',
       [(0, 'Spelet startar alltid från målvakten', '3 mot 2 i egen halva.'),
        (tin - 1.2, 'Passa till kantneutralen i motsatt korridor', 'Eller driv över mittlinjen.'),
        (tin, 'Neutralen spelar direkt vidare', 'Det skapar 3 mot 2 i anfallshalvan.'),
        (tg - 0.8, 'Mål inom 7 sekunder: 3 poäng', 'Räknat från att laget kom in i anfallshalvan.')],
       'AVSLUT OCH MÅL', [('line', [(0, 50), (100, 50)]), ('line', [(50, 0), (50, 100)])],
       [lab(tin + i, tin + i + 1, (84, 8), f'{7 - i} SEK') for i in range(int(tg - tin) + 1)] + [lab(tg, tg + 1.8, (50, 14), '+3')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ s02 Uppbyggnad genom tre zoner med extra mittfältare ============
d = Drill(); d.p('mvb', 'MV', B, (50, 95)); d.p('mvr', 'MV', R, (50, 5)); d.p('T', 'T', G, (96, 92)); d.p('n', 'N', G, (56, 50))
team(d, 'b', B, [(36, 84), (64, 84), (38, 58), (62, 58), (50, 46), (40, 18), (60, 18)])
team(d, 'r', R, [(42, 80), (58, 80), (40, 44), (60, 44), (50, 60), (36, 12), (64, 12)])
b = d.newball((94, 92)); t = d.pas(b, 0.5, rec(d, 'mvb', 1.3))                                     # tränaren till målvakten
t = d.pas(b, t + 0.3, rec(d, 'b0', t + 1)); d.mv('b4', t - 1.2, t + 0.4, (50, 78))                  # mittfältaren faller ner: 3 mot 2
t = d.pas(b, t + 0.3, rec(d, 'b4', t + 0.9)); t = d.pas(b, t + 0.3, rec(d, 'b1', t + 0.9)); t3 = t
d.mv('b4', t, t + 1.4, (50, 46)); t = d.pas(b, t + 0.3, rec(d, 'b3', t + 1.1)); t = d.pas(b, t + 0.3, rec(d, 'n', t + 0.9)); t4 = t   # 4 mot 3 i mitten
d.mv('b2', t - 0.6, t + 1.6, (46, 24)); t = d.pas(b, t + 0.3, rec(d, 'b6', t + 1.1))                    # mittfältare följer med: 3 mot 2
t = d.pas(b, t + 0.3, rec(d, 'b2', t + 0.9)); t = shoot(d, b, t + 0.1, (46, 1))
finish(d, 's02', 'uppbyggnad-genom-tre-zoner-med-extra-mittfaltare', ['Uppbyggnad genom tre zoner', 'Med extra mittfältare'], 'Ca 73 × 18 m · Zoner 18, 37 och 18 m · Mål i båda ändar',
       [(0, 'Tränaren spelar till målvakten', 'Målvakten spelar ut till backarna.'),
        (t3 - 1.6, 'En mittfältare faller ner: 3 mot 2', 'Sedan tillbaka till mitten.'),
        (t4 - 0.8, 'Med den neutrala: 4 mot 3 i mitten', 'Hitta vägen framåt.'),
        (t4 + 0.6, 'Sista zonen', 'Tränaren väljer 1 mot 1, 2 mot 2 eller 3 mot 2.')],
       'SPELUPPBYGGNAD', [('line', [(0, 25), (100, 25)]), ('line', [(0, 75), (100, 75)])])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

if __name__ == '__main__':
    render(C, sys.argv)
