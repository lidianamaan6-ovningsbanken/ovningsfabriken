# Externa övningar, omgång 2 (tolv st). Regel: först d.mv, sedan d.carry; hide före show.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e1', __file__.replace('render_extern2.py', 'render_extern1.py'))
e1 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e1); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e1.finish, e1.rec, e1.chain, e1.wander, e1.counter, e1.arrivals
lab, hide, show, team, boxes, drive, shoot = e1.lab, e1.hide, e1.show, e1.team, e1.boxes, e1.drive, e1.shoot
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'

# ============ b23 Glida och skärma i 8 mot 8 ============
d = Drill(); d.p('mvr', 'MV', R, (50, 6))
team(d, 'b', B, [(30, 84), (70, 84), (12, 64), (88, 64), (40, 56), (60, 56), (30, 36), (70, 36)])
team(d, 'r', R, [(36, 20), (64, 20), (22, 34), (78, 34), (40, 42), (60, 42), (44, 62), (56, 62)])
b = d.newball(rec(d, 'b0', 0))
def slide(t, dx):                                         # försvaret glider som en enhet mot bollsidan
    for k in range(8): d.mv(f'r{k}', t, t + 1.2, (min(92, max(8, d.pos(f'r{k}')[0] + dx)), d.pos(f'r{k}')[1]))
t = d.pas(b, 0.4, rec(d, 'b1', 1.2)); slide(0.6, 8)
t = d.pas(b, t + 0.3, rec(d, 'b3', t + 1)); slide(t - 0.6, 6)                         # bollen ut i yttre korridor
d.mv('b7', t - 0.6, t + 0.4, (84, 34)); t = d.pas(b, t + 0.3, rec(d, 'b7', t + 1))
d.mv('r3', t - 0.8, t + 0.2, rec(d, 'b7', t + 0.2)); d.mv('r5', t - 0.8, t + 0.4, (76, 38))   # press + täckning vid kanten
tw = d.pas(b, t + 0.3, rec(d, 'r3', t + 0.5), 0.3)
t = d.pas(b, tw + 0.3, rec(d, 'r5', tw + 1)); t = chain(d, b, t, ['r4', 'r1'])
finish(d, 'b23', 'glida-och-skarma-i-8-mot-8', ['Glida och skärma', '8 mot 8'], 'Försvarande lag flyttar efter bollens position',
       [(0, 'Rött glider med bollen', 'Hela laget flyttar som en enhet mot bollsidan.'),
        (2.2, 'Styr spelet ut till yttre korridoren', 'Stäng vägen inåt.'),
        (tw - 0.8, 'Press och täckning vid kanten', 'Närmaste pressar, nästa täcker.'),
        (tw, 'Bollvinst i yttre korridoren ger poäng', 'Tränaren kan frysa spelet och visa positioner.')],
       'FÖRHINDRA SPELUPPBYGGNAD', [('line', [(25, 0), (25, 100)]), ('line', [(75, 0), (75, 100)])], [lab(tw, tw + 1.8, (80, 26), '+1')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ b24 Backlinjens djup under press ============
d = Drill()
team(d, 'b', B, [(30, 72), (70, 72), (50, 60), (36, 44), (64, 44), (50, 30)])
team(d, 'r', R, [(28, 24), (44, 22), (56, 22), (72, 24), (40, 52), (60, 52)])
b = d.newball(rec(d, 'b2', 0))
t = chain(d, b, 0.4, ['b0', 'b3'])
for k, x in enumerate([28, 44, 56, 72]): d.mv(f'r{k}', t - 1, t + 0.4, (x, 18))             # backlinjen faller i takt
d.mv('b5', t - 0.4, t + 1.2, (46, 12)); t = d.pas(b, t + 0.4, rec(d, 'b5', t + 1.3), 1.0); tl = t   # djupledsboll mot målytan
d.mv('r1', tl - 1, tl + 0.2, (45, 11)); tw = d.pas(b, tl + 0.2, rec(d, 'r1', tl + 0.4), 0.3)   # försvaret hinner före
d.mv('b5', tw + 0.2, tw + 1.6, (56, 30)); t = d.pas(b, tw + 0.3, rec(d, 'r4', tw + 1)); t = chain(d, b, t, ['r5'])
finish(d, 'b24', 'backlinjens-djup-under-press', ['Backlinjens djup', 'Under press'], '8 mot 8 · En målyta i varje ände',
       [(0, 'Blått anfaller', 'Mål görs genom att ta emot kontrollerat i målytan.'),
        (2, 'Backlinjen faller i takt', 'Spelaren, bollen, ytan och målet.'),
        (tl - 1, 'Djupledspassning mot målytan', 'Rätt djup gör att försvaret hinner först.'),
        (tw, 'Försvaret vinner bollen', 'Och spelar framåt mot andra målytan.')],
       'FÖRHINDRA AVSLUT', [('zone', 30, 2, 70, 14, (230, 200, 90), 'MÅLYTA'), ('zone', 30, 86, 70, 98, (230, 200, 90), 'MÅLYTA')])

# ============ b25 Försvara inlägg: återhämtning och rensning ============
d = Drill(); d.p('cb', 'MB', R, (44, 60)); d.p('T', 'T', G, (44, 46)); d.p('k', 'K', B, (88, 30)); d.p('cb2', 'MB', R, (34, 66))
PIN = [(38, 56), (44, 52), (50, 48)]
b = d.newball((200, 200))
t = d.path('cb', 0.4, [(40, 56), (46, 52), (42, 48), (48, 46)], 1.3)                         # genom pinnarna
d.balls[b] = [(0, (200, 200)), (t - 0.9, (200, 200)), (t - 0.899, rec(d, 'T', t))]
t = d.pas(b, t - 0.8, (48, 45)); t = d.pas(b, t + 0.05, rec(d, 'T', t + 0.6))               # kastad boll tillbaka med nick
d.mv('cb', t, t + 1.4, (54, 16)); b2 = d.newball((200, 200)); d.balls[b2] = [(0, (200, 200)), (t + 0.3, (200, 200)), (t + 0.301, rec(d, 'k', t + 0.3))]   # återhämtar in i boxen
t2 = d.pas(b2, t + 0.6, (56, 14), 1.1); t3 = d.pas(b2, t2 + 0.05, (96, 40), 0.9); tc = t2       # inlägg och rensning
d.mv('cb', t2 + 0.2, t2 + 2, (44, 60))
finish(d, 'b25', 'forsvara-inlagg-aterhamtning-och-rensning', ['Försvara inlägg', 'Återhämtning och rensning'], 'En mittback i taget · Tre par pinnar i kanten av straffområdet',
       [(0, 'Mittbacken springer genom pinnarna', 'Snabba fötter, låg tyngdpunkt.'),
        (2.4, 'Nicka eller volleya tillbaka', 'Tränaren kastar bollen.'),
        (3.6, 'Återhämta in i boxen', 'Ett inlägg slås från kanten.'),
        (tc - 0.2, 'Rensa ut ur boxen', 'Två block om 3 minuter med 2 minuters vila.')],
       'FÖRHINDRA AVSLUT', [('pole', x, y) for x, y in PIN])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ b26 Försvara inlägg mot löpande anfallare ============
d = Drill(); d.p('mv', 'MV', G, (50, 5))
team(d, 'a', B, [(42, 46), (58, 50)]); team(d, 'm', R, [(44, 30), (56, 30)]); d.p('k', 'K', B, (86, 44))
b = d.newball(rec(d, 'a0', 0))
t = d.pas(b, 0.5, rec(d, 'k', 1.3))                                                           # ut till kanten
d.mv('a0', t - 0.4, t + 1.6, (44, 16)); d.mv('a1', t - 0.2, t + 1.8, (60, 12))                # löper in i boxen
d.mv('m0', t - 0.2, t + 1.6, (45, 14)); d.mv('m1', t, t + 1.8, (58, 10))                     # mittbackarna faller in och följer
t = drive(d, b, 'k', t, (88, 22)); t = d.pas(b, t + 0.1, (46, 13.4), 1.0)
t = d.pas(b, t + 0.05, (3, 38), 0.9); tc = t                                                 # rensning
hide(d, b, tc + 0.5)
finish(d, 'b26', 'forsvara-inlagg-mot-lopande-anfallare', ['Försvara inlägg', 'Mot löpande anfallare'], 'Mittbackar mot två anfallare · Kantspelare slår inlägg',
       [(0, 'Anfallarna spelar ut till kanten', 'Och löper in i boxen.'),
        (1.6, 'Mittbackarna faller in och följer löpningarna', 'Se både boll och anfallare.'),
        (tc - 1.4, 'Inlägget kommer', 'Första kontakten på bollen.'),
        (tc - 0.4, 'Rensning ut ur boxen: poäng', 'Anfallarna får poäng för mål.')],
       'FÖRHINDRA AVSLUT', [], [lab(tc, tc + 1.6, (16, 34), '+1')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ b27 1 mot 1 i tre kanaler ============
d = Drill(); LANES = [(10, 26, 'smal'), (36, 64, 'kort'), (72, 92, 'lång')]
for k, (x1, x2, _) in enumerate(LANES):
    cx = (x1 + x2) / 2; top = 14 if k != 1 else 40
    d.p(f'd{k}', 'F', R, (cx, top + 6)); d.p(f'a{k}', 'A', B, (cx, 88)); d.p(f'q{k}', 'A', B, (cx + 4, 94))
for k, (x1, x2, _) in enumerate(LANES):
    cx = (x1 + x2) / 2; top = 14 if k != 1 else 40; bb = d.newball(rec(d, f'd{k}', 0)); t0 = 0.5 + 0.4 * k
    t = d.pas(bb, t0, rec(d, f'a{k}', t0 + 1.4), 1.2); d.mv(f'd{k}', t0 + 0.2, t + 0.6, (cx, (top + 88) / 2))
    if k == 1:   # försvararen vinner och passar till nästa anfallare
        t = drive(d, bb, f'a{k}', t, (cx + 4, 72)); d.mv(f'd{k}', t - 0.6, t, (cx + 3, 72)); tw = d.pas(bb, t + 0.1, rec(d, f'd{k}', t + 0.3), 0.3)
        t = d.pas(bb, tw + 0.4, rec(d, f'q{k}', tw + 1.2)); d.mv(f'd{k}', tw + 0.5, tw + 2.4, (cx + 6, 96)); d.mv(f'a{k}', tw, tw + 2, (cx, top + 6))
    else:
        t = drive(d, bb, f'a{k}', t, (x1 + 3 if k == 0 else x2 - 4, (top + 60) / 2)); t = drive(d, bb, f'a{k}', t, (cx, top))
finish(d, 'b27', '1-mot-1-i-tre-kanaler', ['1 mot 1', 'I tre kanaler'], 'Tre ytor: en smal, en kort och bred, en lång och bred',
       [(0, 'Försvararen passar till anfallaren', 'Anfallaren ska ta sig förbi till kortlinjen.'),
        (2.4, 'Ta dig förbi', 'Olika ytor ger olika lösningar.'),
        (5, 'Försvararen vinner bollen', 'Passar till nästa anfallare och ställer sig i den kön.'),
        (8, 'Alla roterar mellan ytorna', 'Köer bakom båda.')],
       'FÖRHINDRA AVSLUT', [('box', 10, 14, 26, 92), ('box', 36, 40, 64, 92), ('box', 72, 14, 92, 92)])

# ============ b29 Kontrapress och omställning till småmål ============
d = Drill(); RP = [(34, 38), (50, 30), (66, 38), (62, 62), (38, 62)]
team(d, 'b', B, RP); team(d, 'r', R, [(46, 48), (56, 52)])
b = d.newball(rec(d, 'b0', 0))
d.mv('r0', 0.3, 3, (44, 42)); d.mv('r1', 0.3, 3, (58, 56))
t = chain(d, b, 0.4, ['b1', 'b2', 'b3'])
d.mv('r1', t - 0.6, t + 0.2, rec(d, 'b3', t + 0.2)); tw = d.pas(b, t + 0.3, rec(d, 'r1', t + 0.5), 0.3)   # rött vinner
t = drive(d, b, 'r1', tw, (76, 74)); d.mv('r0', tw, tw + 1.6, (70, 66))                    # kontring mot småmål
for k, ps in zip([2, 3, 4], [(72, 60), (70, 76), (62, 72)]): d.mv(f'b{k}', tw, tw + 1.6, ps)   # blått ställer om direkt
d.mv('b3', t - 0.4, t + 0.2, rec(d, 'r1', t + 0.2)); tr_ = d.pas(b, t + 0.3, rec(d, 'b3', t + 0.5), 0.3)   # återerövring inom 6 s
for k, ps in enumerate(RP): d.mv(f'b{k}', tr_ + 0.6, tr_ + 2.6, ps)
d.mv('r0', tr_ + 0.6, tr_ + 2.6, (46, 48)); d.mv('r1', tr_ + 0.6, tr_ + 2.6, (56, 52)); d.carry(b, 'b3', tr_ + 0.6, tr_ + 2.6)
finish(d, 'b29', 'kontrapress-och-omstallning-till-smamal', ['Kontrapress och omställning', 'Till småmål'], 'Rondo 5 mot 2 · Småmål i hörnen av en större ruta',
       [(0, 'Rondo 5 mot 2', 'Laget med boll håller den.'),
        (tw - 0.3, 'Rött vinner bollen och kontrar', 'Mot småmålen. Kontringen ska avslutas inom sex sekunder.'),
        (tw + 0.4, 'Blått ställer om direkt', 'Stoppa kontringen.'),
        (tr_ - 0.2, 'Återerövring inom sex sekunder: poäng', 'Tillbaka till rondon.')],
       'OMSTÄLLNING', [('box', 30, 24, 70, 70), ('box', 14, 10, 86, 90), ('smallgoal', 17, 13), ('smallgoal', 83, 13), ('smallgoal', 17, 87), ('smallgoal', 83, 87)],
       [lab(tw + i, tw + i + 1, (50, 6), f'{6 - i} SEK') for i in range(int(tr_ - tw) + 1)] + [lab(tr_, tr_ + 1.8, (70, 64), '+1')])

# ============ b30 Närmaste spelarens beslut vid bollförlust ============
d = Drill(); d.p('mvb', 'MV', B, (50, 94)); d.p('mvr', 'MV', R, (50, 6))
team(d, 'b', B, [(30, 74), (70, 74), (40, 56), (60, 56), (24, 38), (76, 38), (50, 30)])
team(d, 'r', R, [(32, 24), (68, 24), (44, 40), (56, 40), (30, 56), (70, 56), (50, 66)])
b = d.newball(rec(d, 'b2', 0))
t = chain(d, b, 0.4, ['b3', 'b5'])
d.mv('r3', t - 0.6, t + 0.2, rec(d, 'b5', t + 0.2)); tl = d.pas(b, t + 0.3, rec(d, 'r3', t + 0.5), 0.3)    # bollförlust
d.mv('b5', tl, tl + 0.8, rec(d, 'r3', tl + 0.8)); d.mv('b6', tl, tl + 1, (58, 34))              # närmaste pressar direkt
d.mv('r3', tl, tl + 0.6, (60, 42)); t = d.pas(b, tl + 0.8, rec(d, 'r0', tl + 1.6), 0.8); tb = t   # motståndaren tvingas spela bakåt
t = chain(d, b, t, ['r1', 'r3'])
finish(d, 'b30', 'narmaste-spelarens-beslut-vid-bollforlust', ['Närmaste spelarens beslut', 'Vid bollförlust'], '8 mot 8 där ett lag startar med bollen',
       [(0, 'Blått anfaller', 'Fokus på omställning från anfall till försvar.'),
        (tl - 0.3, 'Bollförlust', 'Tränaren kan frysa spelet här.'),
        (tl + 0.3, 'Närmaste spelare pressar direkt', 'Nästa stänger passningen framåt.'),
        (tb - 0.4, 'Motståndaren tvingas spela bakåt', 'Inom fem sekunder: poäng.')],
       'OMSTÄLLNING', [], [lab(tl + i, tl + i + 1, (50, 48), f'{5 - i} SEK') for i in range(int(tb - tl) + 1)] + [lab(tb, tb + 1.8, (34, 30), '+1')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ b31 Kontring i överlägsenhet mot återhämtande ============
d = Drill(); d.p('mvr', 'MV', R, (50, 6))
team(d, 'b', B, [(36, 62), (50, 66), (64, 62)]); team(d, 'r', R, [(50, 44)]); d.p('rr', '2', R, (40, 78))
b = d.newball((60, 56)); d.balls[b] = [(0, (60, 56)), (0.5, (60, 56)), (0.9, rec(d, 'b1', 0.9))]   # bollvinst
d.mv('rr', 0.6, 4.6, (46, 22))                                                                     # återhämtande försvarare springer tillbaka
d.mv('b0', 0.6, 3, (30, 34)); d.mv('b2', 0.6, 3, (70, 34))
t = drive(d, b, 'b1', 1.0, (50, 46)); d.mv('r0', 1.0, 2.2, (50, 36))
t = d.pas(b, t + 0.1, rec(d, 'b2', t + 0.8)); t = drive(d, b, 'b2', t, (66, 20))
t = d.pas(b, t + 0.1, rec(d, 'b0', t + 0.8)); t = shoot(d, b, t + 0.2, (44, 1)); tg = t
finish(d, 'b31', 'kontring-i-overlagsenhet-mot-aterhamtande', ['Kontring i överlägsenhet', 'Mot återhämtande'], 'Två mål · En återhämtande försvarare startar bakom',
       [(0, 'Laget vinner bollen', 'Och kontrar direkt med överlägsenhet.'),
        (1, 'En försvarare springer tillbaka', 'Hen startar bakom anfallarna.'),
        (3, 'Utnyttja överläget innan hen hinner hem', 'Bredd och fart.'),
        (tg - 0.6, 'Avsluta inom tio sekunder', 'Kontringen måste vara klar.')],
       'OMSTÄLLNING', [], [lab(1 + i, 2 + i, (84, 8), f'{10 - i} SEK') for i in range(int(tg))])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ e01 Rondo med positioner (4 mot 1 → 5 mot 2) ============
d = Drill(); POS = {'b0': ('MB', (50, 74)), 'b1': ('YB', (26, 50)), 'b2': ('YB', (74, 50)), 'b3': ('MF', (50, 26))}
for pid, (l, ps) in POS.items(): d.p(pid, l, B, ps)
d.p('r0', '1', R, (50, 50)); d.p('b4', 'AN', B, (50, 8)); d.p('r1', '2', R, (64, 22))
b = d.newball(rec(d, 'b0', 0))
d.mv('r0', 0.4, 4.4, (44, 46))
t = chain(d, b, 0.4, ['b1', 'b3', 'b2', 'b0'])                                                 # 4 mot 1
d.mv('b4', t - 1, t + 0.6, (50, 16)); d.mv('b3', t - 1, t + 0.6, (64, 30)); d.mv('r1', t - 1, t + 0.6, (56, 40))   # 5 mot 2
t5 = t
t = chain(d, b, t, ['b1', 'b3'])
d.mv('r1', t - 0.6, t + 0.1, rec(d, 'b3', t + 0.1)); tw = d.pas(b, t + 0.3, rec(d, 'r1', t + 0.5), 0.3)
d.mv('r1', tw + 0.3, tw + 1.8, (64, 30)); d.mv('b3', tw + 0.3, tw + 1.8, (54, 44))            # byter roll med den som vann
t = d.pas(b, tw + 1.9, rec(d, 'b4', tw + 2.6)); t = chain(d, b, t, ['r1', 'b2'])
finish(d, 'e01', 'rondo-med-positioner-4-mot-1-till-5-mot-2', ['Rondo med positioner', '4 mot 1 till 5 mot 2'], 'Fasta platser runt ytan som motsvarar positionerna',
       [(0, 'Spelarna står på sina positioner', 'Mittback, ytterbackar och mittfältare – inte slumpvis.'),
        (1.6, '4 mot 1', 'Försvararen i mitten försöker vinna bollen.'),
        (t5 - 0.4, 'Progression: 5 mot 2', 'En anfallare och en försvarare till.'),
        (tw - 0.3, 'Den som tappar byter roll', 'Med försvararen som vann bollen.')],
       'RONDO', [('box', 22, 12, 78, 78)])

# ============ e02 Progression genom tre zoner, 4 mot 2 ============
d = Drill()   # 30 m lång: zon 1 15 m (y 90–45), zon 2 10 m (45–15), zon 3 5 m (15–0)
team(d, 'b', B, [(32, 84), (68, 84), (40, 60), (60, 60)]); team(d, 'r', R, [(44, 72), (56, 68)])
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b2', 'b1'])
for pid, ps in [('b2', (34, 36)), ('b3', (64, 32))]: d.mv(pid, t - 0.8, t + 0.6, ps)
d.mv('r0', t - 0.4, t + 1, (44, 40)); d.mv('r1', t - 0.2, t + 1.2, (56, 36))
t = d.pas(b, t + 0.3, rec(d, 'b3', t + 1.1)); t = d.pas(b, t + 0.3, rec(d, 'b0', t + 1.1), 0.9); tb = t    # bakåt för en bättre väg
d.mv('b0', tb - 1, tb, (40, 50)); t = d.pas(b, t + 0.3, rec(d, 'b2', t + 1))
d.mv('b2', t, t + 1, (36, 22)); d.mv('b3', t, t + 1.2, (60, 8)); d.mv('r0', t, t + 1.2, (44, 14))   # sista zonen 3 mot 1
t = d.pas(b, t + 0.6, rec(d, 'b3', t + 1.4)); tp = t
finish(d, 'e02', 'progression-genom-tre-zoner-4-mot-2', ['Progression genom tre zoner', '4 mot 2'], '30 × 15 m · Zoner på 15, 10 och 5 m',
       [(0, 'Ta dig zon för zon framåt', 'Zonerna blir mindre ju längre fram.'),
        (1.6, 'Spela bakåt för att hitta en bättre väg', 'Det är tillåtet.'),
        (tb + 0.4, 'In i nästa zon', 'Försvararna följer.'),
        (tp - 1, 'Sista zonen: 3 mot 1', 'Poäng när bollen kontrolleras i sista zonen.')],
       'SPELUPPBYGGNAD', [('box', 24, 0, 76, 92), ('line', [(24, 45), (76, 45)]), ('line', [(24, 15), (76, 15)])], [lab(tp, tp + 1.8, (50, 6), '+1')])

# ============ e03 4 mot 2 genom mittkorridoren ============
d = Drill()
team(d, 'b', B, [(18, 76), (40, 76), (18, 94), (40, 94)]); team(d, 'w', WHITE, [(60, 76), (82, 76), (60, 94), (82, 94)])
team(d, 'bc', B, [(46, 82), (54, 88)]); team(d, 'wd', WHITE, [(26, 84), (34, 86)])
for i in range(4): d.mv(f'b{i}', 0, 0.1, [(16, 74), (42, 74), (16, 96), (42, 96)][i])
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b1', 'b3', 'b2', 'b0', 'b1'])
t = d.pas(b, t + 0.3, rec(d, 'w0', t + 1), 0.9); tx = t                                        # över mittkorridoren till lagkamraterna
# lagen byter roller: blåa två går in i högra rutan och pressar, vita två går till korridoren
d.mv('bc0', tx - 0.4, tx + 1.2, (68, 84)); d.mv('bc1', tx - 0.4, tx + 1.2, (74, 88))
d.mv('wd0', tx - 0.4, tx + 1.4, (48, 82)); d.mv('wd1', tx - 0.4, tx + 1.4, (52, 90))
t = chain(d, b, t, ['w1', 'w3', 'w2', 'w0'])
finish(d, 'e03', '4-mot-2-genom-mittkorridoren', ['4 mot 2', 'Genom mittkorridoren'], '25 × 10 m · Två rutor 10 × 10 m och en mittkorridor på 5 m',
       [(0, 'Blått håller bollen i ena rutan', 'Två vita pressar. Två blå står i korridoren och stänger.'),
        (2.6, 'Hitta passningen genom korridoren', 'Till lagkamraterna i andra rutan.'),
        (tx - 0.3, 'Bollen byter ruta – lagen byter roller', 'Nu håller vitt bollen och blått pressar.')],
       'SPELUPPBYGGNAD', [('box', 10, 70, 44, 100), ('box', 56, 70, 90, 100), ('zone', 44, 70, 56, 100, (200, 220, 200), '')])

# ============ e05 Situationsspel 8 mot 6 på verkliga mått ============
d = Drill(); d.p('mv', 'MV', B, (50, 95))
team(d, 'b', B, [(36, 86), (64, 86), (12, 74), (88, 74), (42, 70), (58, 66), (24, 54), (76, 54)])
team(d, 'r', R, [(40, 78), (60, 78), (50, 64), (30, 66), (70, 66), (50, 50)])
b = d.newball(rec(d, 'mv', 0))
t = d.pas(b, 0.4, rec(d, 'b0', 1.2)); t = chain(d, b, t, ['b2', 'b4'])
d.mv('r3', t - 1, t, (36, 70)); t = d.pas(b, t + 0.3, rec(d, 'b6', t + 1))
t = drive(d, b, 'b6', t, (28, 46)); tc = t                                                      # kontrollerat över mittlinjen
d.mv('r5', tc - 1, tc + 0.4, rec(d, 'b6', tc + 0.4)); tw = d.pas(b, tc + 0.5, rec(d, 'r5', tc + 0.7), 0.3)
t = drive(d, b, 'r5', tw, (40, 26)); shoot(d, b, t, (30, 3))                                    # kontring mot småmål
finish(d, 'e05', 'situationsspel-8-mot-6-pa-verkliga-matt', ['Situationsspel 8 mot 6', 'På verkliga mått'], 'Anfallarna i sina riktiga positioner · Riktig planyta',
       [(0, 'Blått bygger upp från egen målvakt', 'Alla står i sina riktiga positioner.'),
        (2, 'Hitta vägen förbi pressen', 'Försvararna står i sina positioner i motståndarlaget.'),
        (tc - 0.6, 'Kontrollerat över mittlinjen: poäng', 'Eller mål.'),
        (tw, 'Försvararna vinner bollen', 'Och kontrar mot småmål.')],
       'SPELUPPBYGGNAD', [('line', [(0, 50), (100, 50)]), ('smallgoal', 30, 4), ('smallgoal', 70, 4)], [lab(tc, tc + 1.6, (28, 40), '+1')])
C[-1]['goals'] = [(50, 100)]; C[-1]['keep_goals'] = True

if __name__ == '__main__':
    render(C, sys.argv)
