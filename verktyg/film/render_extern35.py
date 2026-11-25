# Externa övningar, omgång 35 (fjorton st). Regel: först d.mv, sedan d.carry; först mottagarens rörelse, sedan passningen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e9', __file__.replace('render_extern35.py', 'render_extern9.py'))
e9 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e9); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e9.finish, e9.rec, e9.chain, e9.wander, e9.counter, e9.arrivals
lab, hide, show, team, boxes, drive, shoot = e9.lab, e9.hide, e9.show, e9.team, e9.boxes, e9.drive, e9.shoot
factor, swap_color, stand, countdown, countup, win = e9.factor, e9.swap_color, e9.stand, e9.countdown, e9.countup, e9.win
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'

# ============ wj05 Spelarna först – lekmatch utan coachning ============

# ============ ct07 Nummerkedjan i rörelse ============
d = Drill()
ST = [(30, 30), (66, 26), (74, 60), (44, 72), (24, 54), (54, 46)]
team(d, 'b', B, ST)
for k in range(6): wander(d, f'b{k}', 0, 17.9, (14, 16, 86, 84), 13500 + k, 1.6)
b = d.newball(rec(d, 'b0', 0)); t = 0.4; cnt = []
for k in [1, 2, 3, 4, 5, 0, 1, 2]:
    t = d.pas(b, t + 0.3, rec(d, f'b{k}', t + 1.1)); cnt.append(t)
fp = [(0, 'Alla har ett nummer', 'Spelarna rör sig fritt i ytan.'),
      (1.2, 'Bollen går alltid till nästa nummer', '1 till 2 till 3 …'),
      (4.0, 'Passa och flytta dig', 'Vet var nästa spelare är innan bollen kommer.'),
      (8.0, 'Passa framför löparen', 'Variant: boll nummer två eller vänd ordning.')]
finish(d, 'ct07', 'nummerkedjan-i-rorelse', ['Nummerkedjan', 'I rörelse'], 'Yta 25 × 25 m · Numrerade spelare',
       fp, 'PASSNING', [('box', 10, 12, 90, 88)], counter(cnt, pos=(88, 92), last=None))

# ============ ct08 Konskogen – passa utan att nudda ============
d = Drill()
PR = [(26, 22), (26, 78), (50, 22), (50, 78), (74, 22), (74, 78)]
for k, ps in enumerate(PR): d.p(f'p{k}', '', B if k % 2 == 0 else R, ps)
FOR = [(x, y) for x in (16, 22, 30, 36, 44, 52, 58, 66, 72, 80, 86) for y in (42, 50, 58) if (x * 7 + y) % 3 != 0]
cnt = []
for pr in range(3):
    a, c = f'p{2 * pr}', f'p{2 * pr + 1}'; bb = d.newball(rec(d, a, 0)); t = 0.4 + 0.3 * pr
    for rep in range(5):
        t = d.pas(bb, t + 0.5, rec(d, c if rep % 2 == 0 else a, t + 1.5)); cnt.append(t) if pr == 0 else None
        if rep == 2:   # flyttar längre isär
            d.mv(a, t, t + 0.8, (PR[2 * pr][0], 14)); d.mv(c, t, t + 0.8, (PR[2 * pr + 1][0], 86))
fp = [(0, 'Paren på var sin sida om skogen', ''),
      (1.0, 'Hitta luckan mellan konerna', 'Insidan och lagom kraft.'),
      (4.0, '+1 per lyckad passning', 'Minus ett om bollen träffar en kon.'),
      (7.0, 'Längre isär när det går bra', 'Mottagning åt rätt håll för nästa passning.')]
finish(d, 'ct08', 'konskogen-passa-utan-att-nudda', ['Konskogen', 'Passa utan att nudda'], 'Konskog i mitten · Par på var sin sida',
       fp, 'PASSNING', [('cone', x, y) for x, y in FOR], counter(cnt, pos=(12, 92), last=None))

# ============ ea01 Skill game: måltavlan ============
d = Drill(); d.p('s', '', B, (50, 64))
for k in range(3): d.p(f'q{k}', '', B, (40 + 10 * k, 84))
ZN = [(22, 4), (78, 4), (50, 4), (30, 4), (70, 4)]; PT = ['3', '3', '1', '2', '2']; ex = []; t = 0.4
for k, (zx, zy) in enumerate(ZN):
    bb = d.newball((200, 200) if k else rec(d, 's', 0))
    if k: show(d, bb, t, rec(d, 's', t))
    tg = d.pas(bb, t + 0.6, (zx, zy + 1), 0.6); hide(d, bb, tg + 0.3); ex.append(lab(tg, tg + 1.2, (zx, 14), '+' + PT[k])); t = tg + 0.6
fp = [(0, 'Fem skott per spelare', 'Placering före kraft.'),
      (1.2, 'Poäng efter zon', 'Hörnen ger mest.'),
      (4.6, 'Titta upp och välj zon', 'Insidan för placering.'),
      (8.0, 'Omgång två: svaga foten', 'Omgång tre: skott efter vändning.')]
finish(d, 'ea01', 'skill-game-maltavlan', ['Skill game', 'Måltavlan'], 'Mål delat i zoner · 11–16 m',
       fp, 'AVSLUT', [('zone', 14, 1, 38, 8, (240, 210, 90), '3'), ('zone', 62, 1, 86, 8, (240, 210, 90), '3'),
                      ('zone', 38, 1, 62, 8, (180, 220, 200), '1'), ('line', [(14, 8), (86, 8)])], ex)
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ ea02 Skill game: portjakten mot klockan ============
d = Drill(); d.p('s', '', B, (12, 88)); d.p('n', '', R, (6, 92))
PO = [(26, 74), (44, 84), (62, 70), (80, 56), (64, 38), (40, 46), (24, 26), (52, 16), (82, 22)]
b = d.newball(rec(d, 's', 0)); t = 0.5
for (x, y) in PO:
    t = drive(d, b, 's', t, (x, y), 20)
d.mv('n', t - 4, t, (12, 88))
fp = [(0, 'Dribbla genom portarna i ordning', 'Så snabbt som möjligt.'),
      (2.0, 'Korta touch nära portarna', 'Längre touch på raka sträckor.'),
      (6.0, 'Missad port = två sekunders straff', 'Huvudet upp – var är nästa port?'),
      (t - 1.0, 'Ny bana varje omgång', 'Variant: bara vänster fot, eller en jagare.')]
shapes = [('box', 4, 6, 96, 96)]
for k, (x, y) in enumerate(PO): shapes += [('cone', x - 4, y), ('cone', x + 4, y), ('text', x, y + 5, str(k + 1))]
tt = 0.5
finish(d, 'ea02', 'skill-game-portjakten-mot-klockan', ['Skill game', 'Portjakten mot klockan'], 'Nio numrerade portar · Tidtagning',
       fp, 'TEKNIK', shapes, countup(0.5, 9, (88, 92), (t - 0.5) / 9))

# ============ ea03 Skill game: passningsmålen ============
d = Drill(); d.p('s', '', B, (50, 90))
RZ = [(50, 64, '1'), (30, 42, '2'), (70, 30, '3'), (50, 16, '4')]; ex = []; t = 0.4
for k, (zx, zy, pt) in enumerate([RZ[0], RZ[1], RZ[3], RZ[2]]):
    bb = d.newball(rec(d, 's', 0) if k == 0 else (200, 200))
    if k: show(d, bb, t, rec(d, 's', t))
    tt = d.pas(bb, t + 0.5, (zx, zy), 0.7 + 0.25 * k); ex.append(lab(tt, tt + 1.4, (zx + 12, zy), '+' + pt)); t = tt + 1.0
    hide(d, bb, t)
d.p('m', 'M', R, (50, 40)); d.mv('m', t, t + 0.6, (30, 42))
bb = d.newball((200, 200)); show(d, bb, t + 0.3, rec(d, 's', t + 0.3)); tt = d.pas(bb, t + 0.8, rec(d, 'm', t + 1.8), 1.0)
fp = [(0, 'Slå mot valfri zon', 'Bollen måste stanna i zonen.'),
      (1.2, 'Poäng efter avstånd', 'Tio bollar per spelare.'),
      (4.5, 'Lång passning: vristen och följ igenom', 'Precision före kraft.'),
      (t, 'Variant: mottagare i zonen', 'Ska ta emot inne i rutan.')]
finish(d, 'ea03', 'skill-game-passningsmalen', ['Skill game', 'Passningsmålen'], 'Fyra zoner på olika avstånd',
       fp, 'PASSNING', [('zone', zx - 7, zy - 6, zx + 7, zy + 6, (240, 210, 90), pt) for zx, zy, pt in RZ], ex)

# ============ ea04 Skill game: håll porten stängd ============
d = Drill(); d.p('a', 'A', B, (50, 84)); d.p('f', 'F', R, (50, 40))
b = d.newball(rec(d, 'a', 0))
d.mv('f', 0.4, 1.6, (50, 62)); t = drive(d, b, 'a', 0.4, (50, 72), 10)
d.mv('f', t, t + 0.8, (44, 66)); t = drive(d, b, 'a', t, (62, 68), 10)       # styrs åt sidan
d.mv('f', t, t + 0.8, (60, 62)); t = drive(d, b, 'a', t, (70, 60), 10)
d.mv('a', t, t + 0.8, (66, 56)); tw = win(d, b, 'f', 'a', t + 0.9, 0.6)
d.mv('f', tw, tw + 1.2, (50, 50)); d.carry(b, 'f', tw, tw + 1.2)
fp = [(0, 'Ett mot ett mot porten', 'Anfallaren ska ta sig igenom.'),
      (1.6, 'Sidställd – styr åt ena hållet', 'Rätt avstånd: en armlängd.'),
      (4.0, 'Tålamod, inte hugga', 'Tio sekunder på klockan.'),
      (tw - 0.2, 'Bollvinst – försvararens poäng', 'Eller om tiden går ut.')]
finish(d, 'ea04', 'skill-game-hall-porten-stangd', ['Skill game', 'Håll porten stängd'], 'Port 4 m bred · 10 sekunder',
       fp, 'DUELL', [('box', 20, 20, 80, 92), ('cone', 44, 24), ('cone', 56, 24)], countdown(0.4, 8, (88, 30), (tw - 0.4) / 8) + [lab(tw, tw + 1.6, (60, 46), '+1 F')])

# ============ ag01 Åldersstegen 6–7 år: bollkalaset ============
d = Drill(); d.p('t', 'T', T_COL, (50, 50))
KP = [(24, 28), (74, 26), (30, 70), (70, 72), (50, 30), (48, 74)]
team(d, 'k', B, KP, [''] * 6)
balls = [d.newball(rec(d, f'k{k}', 0)) for k in range(6)]
for k in range(6):
    wander(d, f'k{k}', 0, 3.6, (12, 14, 88, 86), 13600 + k, 1.2); d.carry(balls[k], f'k{k}', 0, 3.6)
    stand(d, f'k{k}', 3.6, 4.4); d.carry(balls[k], f'k{k}', 3.6, 4.4)                       # stopp med sulan
d.p('j', 'J', R, (50, 8))
for k in range(6):
    wander(d, f'k{k}', 4.4, 8.6, (12, 14, 88, 86), 13700 + k, 1.2); d.carry(balls[k], f'k{k}', 4.4, 8.6 if k != 2 else 6.4)
d.mv('j', 4.4, 6.2, rec(d, 'k2', 6.2)); d.pas(balls[2], 6.4, (14, 92), 0.6); hide(d, balls[2], 7.2)   # jagaren petar bort
for k in range(6):
    if k == 2: continue
    d.mv(f'k{k}', 8.6, 10.2, (20 + 12 * k, 82)); d.carry(balls[k], f'k{k}', 8.6, 10.2)
    if k == 0: d.mv('t', 9.0, 10.0, (50, 30))
    tg = d.pas(balls[k], 10.4 + 0.3 * k, rec(d, 't', 11.0 + 0.3 * k), 0.6); hide(d, balls[k], tg + 0.2)
fp = [(0, 'Lek 1: dribbla – stopp med sulan', 'På signal. Max 30 sekunders förklaring.'),
      (4.4, 'Lek 2: jagaren petar bort bollar', ''),
      (8.6, 'Lek 3: skjut på tränaren', 'Tränaren är ett rörligt mål.'),
      (12.0, 'Sist: 3 mot 3 utan målvakt', 'Beröm försök, inte bara lyckanden.')]
finish(d, 'ag01', 'aldersstegen-6-7-ar-bollkalaset', ['Åldersstegen 6–7 år', 'Bollkalaset'], 'Yta 20 × 20 m · En boll per barn',
       fp, 'LEK', [('box', 8, 10, 92, 90)], [lab(3.6, 4.4, (50, 50), 'STOPP!')])

# ============ ag02 Åldersstegen 14 år: vänd och avsluta under press ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96))
BP = [(20, 66), (40, 72), (62, 72), (82, 64), (50, 50), (36, 40)]; RP = [(30, 28), (48, 22), (66, 26), (78, 38), (54, 40), (26, 44)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b3', 0))
d.mv('r3', 0.4, 1.6, (80, 54)); d.mv('r4', 0.4, 1.6, (72, 56))                                            # två pressar bollen
t = d.pas(b, 0.6, rec(d, 'b2', 1.4)); t = d.pas(b, t + 0.3, rec(d, 'b1', t + 1.0))                        # bakåt och via mitten
d.mv('b0', 0.6, t + 1.0, (14, 44)); t = d.pas(b, t + 0.3, rec(d, 'b0', t + 1.3), 1.0); tsw = t             # kanten bytt
d.mv('r5', tsw - 0.6, tsw + 0.6, (20, 36)); d.mv('r0', tsw - 0.6, tsw + 0.6, (26, 30))
d.mv('b5', tsw - 0.8, tsw + 0.6, (32, 26)); t = d.pas(b, tsw + 0.2, rec(d, 'b5', tsw + 0.8))
tg = shoot(d, b, t + 0.05, (44, 1)); hide(d, b, tg + 0.3)
fp = [(0, 'Sex mot sex', 'Försvaret pressar alltid med två på bollen.'),
      (1.4, 'Byt kant innan ni får skjuta', 'Via mitten eller bakåt.'),
      (tsw - 0.2, 'Kanten bytt – nu får ni avsluta', 'Avslut innan pressen hinner fram.'),
      (tg - 0.3, 'Avslut på max två touch: dubbelt', 'Försvaret: kliv tillsammans.')]
finish(d, 'ag02', 'aldersstegen-14-ar-vand-och-avsluta-under-press', ['Åldersstegen 14 år', 'Vänd och avsluta under press'], 'Plan 40 × 30 m · Två mål med målvakter',
       fp, 'SPELÖVNING', [('box', 6, 2, 94, 98)], [lab(tsw, tsw + 1.4, (14, 56), 'BYTT KANT'), lab(tg, tg + 1.8, (44, 14), 'x2')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ xn01 Stela häxan – befria med väggspel ============
d = Drill()
KP = [(24, 30), (70, 26), (30, 70), (74, 72), (50, 52), (46, 22)]
team(d, 'k', B, KP, [''] * 6); team(d, 'h', R, [(14, 50), (86, 50)], ['H', 'H'])
balls = [d.newball(rec(d, f'k{k}', 0)) for k in range(6)]
for k in (0, 1, 3, 5): wander(d, f'k{k}', 0, 17.9, (12, 14, 88, 86), 13800 + k, 1.4); d.carry(balls[k], f'k{k}', 0, 17.9)
d.mv('k2', 0, 2.2, (36, 64)); d.carry(balls[2], 'k2', 0, 2.2); d.mv('h0', 0, 2.2, (34, 62))                  # fångad – står stel
stand(d, 'k2', 2.2, 7.4); d.carry(balls[2], 'k2', 2.2, 7.4)
d.mv('h0', 2.4, 4.6, (20, 40)); wander(d, 'h0', 4.6, 17.9, (12, 14, 88, 86), 13810, 1.4)
wander(d, 'h1', 0, 17.9, (12, 14, 88, 86), 13811, 1.4)
d.mv('k4', 0, 3.2, (54, 58)); d.carry(balls[4], 'k4', 0, 3.2); stand(d, 'k4', 3.2, 3.4)
t = d.pas(balls[4], 3.6, rec(d, 'k2', 4.4)); t = d.pas(balls[4], t + 0.3, rec(d, 'k4', t + 1.0))             # väggspel befriar
d.mv('k4', t, t + 3, (60, 30)); d.carry(balls[4], 'k4', t, t + 3); tf = t
d.mv('k2', tf, tf + 3, (24, 80)); d.carry(balls[2], 'k2', tf, tf + 3)
wander(d, 'k4', tf + 3, 17.9, (12, 14, 88, 86), 13820, 1.4); d.carry(balls[4], 'k4', tf + 3, 17.9)
wander(d, 'k2', tf + 3, 17.9, (12, 14, 88, 86), 13821, 1.4); d.carry(balls[2], 'k2', tf + 3, 17.9)
fp = [(0, 'Häxorna jagar dem som dribblar', ''),
      (2.0, 'Fångad – stå stel och håll bollen', ''),
      (3.4, 'Befria med väggspel', 'Kompisen passar, den stela spelar tillbaka.'),
      (tf + 0.4, 'Fri igen!', 'Byt häxor varje minut.')]
finish(d, 'xn01', 'stela-haxan-befria-med-vaggspel', ['Stela häxan', 'Befria med väggspel'], 'Yta 20 × 20 m · Två häxor',
       fp, 'LEK', [('box', 8, 10, 92, 90)], [lab(2.2, 3.6, (36, 56), 'STEL'), lab(tf, tf + 1.4, (36, 56), 'FRI!')])

# ============ xn02 Snurra och skjut ============
d = Drill(); d.p('mv', 'MV', T_COL, (50, 4))
for tm, x, col in (('b', 34, B), ('r', 66, R)):
    for k in range(3): d.p(f'{tm}{k}', '', col, (x - 6 + 6 * k, 94))
ex = []
for tm, x, col in (('b', 34, B), ('r', 66, R)):
    pid = f'{tm}0'; cx, cy = x, 62; t = 0.4 + (0.2 if tm == 'r' else 0)
    d.mv(pid, t, t + 0.8, (cx, cy + 5)); t += 0.8
    for v in range(5):
        for a in range(0, 360, 90):
            import math
            d.mv(pid, t, t + 0.12, (cx + 5 * math.sin(math.radians(a + 90)), cy + 5 * math.cos(math.radians(a + 90)))); t += 0.12
    bb = d.newball((200, 200)); show(d, bb, t + 0.9, (x + 1.8, 40.8)); d.mv(pid, t, t + 1.2, (x, 42)); t += 1.2
    tg = shoot(d, bb, t + 0.1, (46 if tm == 'b' else 54, 1)); hide(d, bb, tg + 0.3)
    ex.append(lab(tg, tg + 1.6, (x, 14), '+1')); d.mv(pid, tg + 0.3, tg + 2.4, (x + 10 if tm == 'b' else x - 10, 96))
    d.mv(f'{tm}1', tg + 0.3, tg + 1.6, (cx, cy + 5))
fp = [(0, 'Två led tävlar', ''),
      (1.2, 'Fem varv runt konen', 'Hitta balansen först.'),
      (4.0, 'Ta bollen och skjut', 'Titta på bollen när du skjuter.'),
      (7.0, 'Poäng per mål', 'Mjukt underlag och gott om plats. Ha kul!')]
finish(d, 'xn02', 'snurra-och-skjut', ['Snurra', 'och skjut'], 'Två koner · Bollar framför målet',
       fp, 'LEK', [('cone', 34, 62), ('cone', 66, 62)], ex + countup(1.2, 5, (50, 62), 0.48 * 1.0))
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ xn03 Reaktorn 2 mot 2 ============
d = Drill(); d.p('t', 'T', T_COL, (50, 96)); d.p('mv', 'MV', T_COL, (50, 4))
team(d, 'b', B, [(40, 74), (60, 74)]); team(d, 'r', R, [(44, 66), (56, 66)])
b = d.newball((200, 200)); show(d, b, 1.4, rec(d, 't', 1.4))
t = d.pas(b, 1.6, (66, 50), 0.9)                                                                          # tränaren rullar in
d.mv('r1', t - 0.5, t, (64, 50)); d.mv('b1', t - 0.5, t + 0.2, (70, 54)); d.mv('r0', t - 0.4, t + 0.6, (50, 46)); d.mv('b0', t - 0.4, t + 0.6, (54, 56))
d.carry(b, 'r1', t, t + 0.3); t = d.pas(b, t + 0.4, rec(d, 'r0', t + 1.0)); t = drive(d, b, 'r0', t, (48, 26), 18)
d.mv('b0', t - 1.4, t, (52, 32)); d.mv('r1', t - 1.4, t, (64, 24)); d.mv('b1', t - 1.4, t, (60, 30))
t = d.pas(b, t + 0.1, rec(d, 'r1', t + 0.7)); tg = shoot(d, b, t + 0.05, (54, 1))
fp = [(0, 'Ryggen mot tränaren', 'Två par väntar på signalen.'),
      (1.4, 'Tränaren rullar in en boll', 'Reagera på ljud och syn.'),
      (3.4, 'Två mot två – vinn bollen', 'Laget som vinner anfaller målet.'),
      (tg - 0.4, 'Avsluta snabbt', 'Max 20 sekunder.')]
finish(d, 'xn03', 'reaktorn-2-mot-2', ['Reaktorn', '2 mot 2'], 'Yta 20 × 25 m · Mål med målvakt',
       fp, 'DUELL', [('box', 20, 4, 80, 92)], [lab(1.4, 2.4, (70, 86), 'NU!')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ dd01 Bollmästaren 20/20 ============
d = Drill()
SP = [(30, 30), (70, 30), (30, 70), (70, 70)]
for k, ps in enumerate(SP): d.p(f'p{k}', '', B, ps)
MV_ = ['SULTAPP', 'SULRULLA IN–UT', 'INSIDA–INSIDA', 'V-DRAG', 'RULLA OCH STOPP']
for k, (x, y) in enumerate(SP):
    bb = d.newball((x + 1.8, y - 3.5)); tr = d.balls[bb]; t = 0.2
    for m in range(5):
        for j in range(5):
            dx = [(0, 0), (3, 0), (2.5, 0), (2.5, -1.5), (4, 0)][m]
            tr += [(t, (x + dx[0] * (1 if j % 2 else -1) * 0.6, y - 3.5 + dx[1])), (t + 0.25, (x + dx[0] * (-1 if j % 2 else 1) * 0.6, y - 3.5))]; t += 0.5
        tr.append((t + 0.3, (x + 1.8, y - 3.5))); t += 0.4
fp = [(0, 'Fem bollmästarrörelser', '20 sekunder vardera, 10 sekunder vila.'),
      (2.8, 'Lätta fötter, på tå', 'Båda fötterna.'),
      (8.0, 'Räkna dina touch', 'Försök slå förra veckan.'),
      (11.5, 'Blicken upp ibland', '')]
finish(d, 'dd01', 'bollmastaren-20-20', ['Bollmästaren', '20/20'], 'På stället · En boll per spelare',
       fp, 'TEKNIK', [], [lab(0.2 + 2.9 * m, 0.2 + 2.9 * (m + 1), (50, 50), MV_[m]) for m in range(5)])
C[-1]['_stuck'] = True

# ============ dd02 Snabba fötter till avslut ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
for tm, x, col in (('b', 34, B), ('r', 66, R)):
    for k in range(3): d.p(f'{tm}{k}', '', col, (x - 6 + 6 * k, 94))
ex = []; LAD = [(x, y) for x in (34, 66) for y in (82, 77, 72, 67, 62, 57)]
for tm, x in (('b', 34), ('r', 66)):
    pid = f'{tm}1'; t = 0.4 + (0.25 if tm == 'r' else 0)
    d.mv(pid, t, t + 0.5, (x, 86)); t += 0.5
    for i, y in enumerate([82, 77, 72, 67, 62, 57]):
        d.mv(pid, t, t + 0.25, (x + (1.5 if i % 2 else -1.5), y)); t += 0.25
    bb = d.newball((200, 200)); show(d, bb, t + 0.6, (x + 1.8, 42.8)); d.mv(pid, t, t + 0.9, (x, 44)); t += 0.9
    d.carry(bb, pid, t, t + 0.3); tg = shoot(d, bb, t + 0.4, (44 if tm == 'b' else 56, 1)); hide(d, bb, tg + 0.3)
    if tm == 'b': ex.append(lab(tg, tg + 1.6, (44, 14), 'MÅL!'))
    d.mv(pid, tg + 0.3, tg + 2.6, (x + (-12 if tm == 'b' else 12), 96))
fp = [(0, 'Två lag tävlar', 'Flest mål vinner.'),
      (1.0, 'Snabba, korta steg i stegen', 'En fot per ruta, två fötter, sidled, in–ut.'),
      (3.4, 'Max två touch och skott', 'Avsluta innan du tappar fart.'),
      (6.0, 'Behåll balansen till bollen', '')]
finish(d, 'dd02', 'snabba-fotter-till-avslut', ['Snabba fötter', 'Till avslut'], 'Två koordinationsstegar · Mål med målvakt',
       fp, 'AVSLUT', [('line', [(x - 4, y), (x + 4, y)]) for x, y in LAD] + [('line', [(x - 4, 84), (x - 4, 55)]) for x in (34, 66)] + [('line', [(x + 4, 84), (x + 4, 55)]) for x in (34, 66)], ex)
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ dd03 Första touchen bort från pressen ============
d = Drill()
TR = [(28, 30), (72, 30), (50, 72)]
team(d, 'b', B, TR); d.p('f', '', R, (50, 44))
b = d.newball(rec(d, 'b0', 0)); t = 0.4; cnt = []; h = 0
for nk in [1, 2, 0, 1, 2, 0, 2, 1]:
    fx, fy = TR[nk]; d.mv('f', t, t + 0.7, ((fx + 50) / 2, (fy + 50) / 2 - 2))                               # försvararen pressar mottagaren
    t = d.pas(b, t + 0.1, rec(d, f'b{nk}', t + 0.8)); cnt.append(t)
    away = (fx + (fx - 50) * 0.16, fy + (fy - 50) * 0.16); d.mv(f'b{nk}', t, t + 0.35, away); d.carry(b, f'b{nk}', t, t + 0.35)
    d.mv(f'b{nk}', t + 0.6, t + 1.4, TR[nk]); t += 0.4
fp = [(0, 'Tre mot en', 'Max två touch.'),
      (1.2, 'Första touchen bort från försvararen', 'Mottagning med bakre foten.'),
      (5.0, 'Titta på försvararen innan bollen kommer', 'Vinkel: inte i linje med försvararen.'),
      (9.0, 'Tio passningar = poäng', 'Den som tappar går in i mitten.')]
finish(d, 'dd03', 'forsta-touchen-bort-fran-pressen', ['Första touchen', 'Bort från pressen'], 'Ruta 10 × 10 m · Tre mot en',
       fp, 'RONDO', [('box', 16, 16, 84, 84)], counter(cnt, pos=(88, 92), last=None))

if __name__ == '__main__': render(C, sys.argv)
