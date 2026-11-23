# Externa övningar, omgång 18 (tolv st). Regel: först d.mv, sedan d.carry; först mottagarens rörelse, sedan passningen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e9', __file__.replace('render_extern18.py', 'render_extern9.py'))
e9 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e9); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e9.finish, e9.rec, e9.chain, e9.wander, e9.counter, e9.arrivals
lab, hide, show, team, boxes, drive, shoot = e9.lab, e9.hide, e9.show, e9.team, e9.boxes, e9.drive, e9.shoot
factor, swap_color, stand, countdown, countup, win = e9.factor, e9.swap_color, e9.stand, e9.countdown, e9.countup, e9.win
import math as _mm
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'

# ============ xx03 Vinkelspetsen ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
CN = [(30, 32), (24, 24), (19, 16), (15, 9)]
d.p('a', '', B, (32, 38)); d.p('q', '', B, (40, 44))
b = d.newball(rec(d, 'a', 0)); t = 0.4; ex = []
for k in range(3):
    x, y = CN[k]
    d.mv('a', t, t + 0.6, (x + 2, y + 2)); d.carry(b, 'a', 0 if k == 0 else t, t + 0.6)
    tg = d.pas(b, t + 0.8, (47, 1), 0.6); ex.append(lab(tg, tg + 1.4, (60, 14), 'MÅL' if k < 2 else 'MISS'))
    if k < 2:
        hide(d, b, tg + 0.3); show(d, b, tg + 1.0, (CN[k + 1][0] + 3.8, CN[k + 1][1] + 0.8))       # nästa kon – spetsigare vinkel
        d.mv('a', tg, tg + 1.0, (CN[k + 1][0] + 2, CN[k + 1][1] + 3))
    else:
        hide(d, b, tg + 0.3)
    t = tg + 1.0
d.mv('a', t, t + 1.6, (40, 46)); d.mv('q', t - 0.6, t + 1.0, (32, 38))
fp = [(0, 'Skjut från konen längst bort', 'Start 10–12 m från stolpen.'),
      (1.6, 'Mål – gå vidare till nästa kon', 'Vinkeln blir spetsigare.'),
      (t - 1.0, 'Spetsig vinkel – svårare', ''),
      (t + 0.4, 'Byt sida', 'Använd andra foten eller utsidan.')]
finish(d, 'xx03', 'vinkelspetsen', ['Vinkel-', 'spetsen'], 'Rad med koner från kortlinjen · Start 10–12 m från stolpen',
       fp, 'AVSLUT', [('cone',) + c for c in CN], ex)
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ xx04 Hinderbana med avslut ============
d = Drill(); d.p('mv', 'MV', R, (50, 4)); d.p('t', 'T', T_COL, (70, 30))
SL = [(24, 70), (30, 62), (24, 54), (30, 46)]; LIFT = [(44, 42), (52, 42)]; SPIN = (66, 52)
for k in range(2): d.p(f'p{k}', '', B, (14, 92 - 0 * k) if k == 0 else (8, 94))
balls = [d.newball(rec(d, f'p{k}', 0)) for k in range(2)]
t = 0.4; marks = []
for k in range(2):
    pid = f'p{k}'; b = balls[k]
    if k: d.mv(pid, t - 1.0, t, (14, 92))
    d.carry(b, pid, 0, t)
    t1 = d.path(pid, t, [(18, 80)] + [(x + (-4 if i % 2 else 4), y) for i, (x, y) in enumerate(SL)], 1.2); d.carry(b, pid, t, t1)   # fritt parti och slalom
    t2 = d.pas(b, t1 + 0.1, (50, 40), 0.6); d.mv(pid, t1, t2 + 0.3, (48, 42))                              # lyft över koner
    t3 = d.path(pid, t2 + 0.3, [(60, 48), (66, 46), (72, 52), (66, 58), (60, 54)], 1.1); d.carry(b, pid, t2 + 0.3, t3)   # 360 grader runt konen
    t4 = d.pas(b, t3 + 0.1, rec(d, 't', t3 + 0.8)); d.mv(pid, t3, t4 + 0.6, (56, 30)); t5 = d.pas(b, t4 + 0.1, rec(d, pid, t4 + 0.7))   # vägg med tränaren
    tg = shoot(d, b, t5 + 0.1, (46 + 6 * k, 1)); hide(d, b, tg + 0.4); marks.append((t1, t3, tg))
    d.mv(pid, tg + 0.2, tg + 3.0, (84, 90 - 6 * k))
    t = t2 + 0.4
fp = [(0, 'Fritt parti och slalom', 'Ett barn i taget.'),
      (marks[0][0], 'Lyft över konerna', ''),
      (marks[0][1] - 1.6, 'Runt konen 360 grader', 'Sedan vägg med tränaren.'),
      (marks[0][2] - 0.4, 'Avslut', 'Ge varje barn utrymme innan nästa startar.')]
finish(d, 'xx04', 'hinderbana-med-avslut', ['Hinderbana', 'Med avslut'], 'Bana på planen · Mål med målvakt',
       fp, 'TEKNIK', [('cone',) + c for c in SL] + [('cone',) + c for c in LIFT] + [('cone',) + SPIN])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ xx05 Snurra runt konen ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
for tm, x, col in (('b', 34, B), ('r', 66, R)):
    for k in range(3): d.p(f'{tm}{k}', '', col, (x, 82 + 5 * k))
CX = {34: (34, 56), 66: (66, 56)}
for tm, x, col in (('b', 34, B), ('r', 66, R)):
    pid = f'{tm}0'; b = d.newball(rec(d, pid, 0)); t = 0.4 + (0.3 if tm == 'r' else 0)
    cx, cy = CX[x]; d.mv(pid, t, t + 1.0, (cx, cy + 4)); d.carry(b, pid, 0, t + 1.0); t += 1.0
    hide(d, b, t)                                                                                # bollen läggs undan medan barnet snurrar
    pts = [(cx + 4 * _mm.sin(a / 12 * 2 * _mm.pi), cy + 4 * _mm.cos(a / 12 * 2 * _mm.pi)) for a in range(1, 12 * 4 + 1)]
    t2 = d.path(pid, t, pts, 0.9)                                                                   # handen på konen – åtta varv (fyra visas)
    show(d, b, t2 + 0.1, (cx + 1.8, cy - 1.2)); d.mv(pid, t2, t2 + 1.0, (cx, cy - 12)); d.carry(b, pid, t2 + 0.2, t2 + 1.0)
    tg = shoot(d, b, t2 + 1.1, (46 if x < 50 else 54, 1)); hide(d, b, tg + 0.4)
    d.mv(pid, tg + 0.2, tg + 2.6, (x + 8, 94))
    for k in (1, 2): d.mv(f'{tm}{k}', tg + 0.4, tg + 1.2, (x, 82 + 5 * (k - 1)))
fp = [(0, 'Handen på konen', 'En kon per lag.'),
      (1.6, 'Spring runt åtta gånger', ''),
      (7.0, 'Sedan skott mot mål', 'Eller spring tillbaka.'),
      (10.0, 'Kan köras som stafett', 'Nästa startar.')]
finish(d, 'xx05', 'snurra-runt-konen', ['Snurra runt', 'konen'], 'En kon per lag',
       fp, 'STAFETT', [('cone', 34, 56), ('cone', 66, 56)], [lab(1.6, 6.8, (50, 66), '8 VARV')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ xx06 Poängskott ============
d = Drill(); d.p('mv', 'MV', R, (50, 4)); d.p('t', 'T', T_COL, (50, 32))
for k in range(4): d.p(f'p{k}', '', B, (36 + 8 * k, 60))
balls = [d.newball(rec(d, f'p{k}', 0)) for k in range(4)]
t = 0.4; ex = []; PTS = ['3 POÄNG', '5 POÄNG', '1 POÄNG']
for k in range(3):
    pid = f'p{k}'
    t1 = d.pas(balls[k], t, rec(d, 't', t + 0.9)); d.mv(pid, t + 0.2, t1 + 0.4, (40 + 6 * k, 46))
    t2 = d.pas(balls[k], t1 + 0.1, rec(d, pid, t1 + 0.7)); tg = shoot(d, balls[k], t2 + 0.05, (44 + 5 * k, 1))   # direktskott
    hide(d, balls[k], tg + 0.4); ex.append(lab(tg, tg + 1.6, (70, 20), PTS[k]))
    d.mv(pid, tg + 0.2, tg + 2.4, (36 + 8 * k, 68)); t = tg + 0.6
fp = [(0, 'Passa till tränaren', 'Mål med målvakt och en rad framför.'),
      (1.6, 'Tränaren spelar tillbaka – direktskott', ''),
      (ex[0]['t0'], 'Tränaren ger 1–5 poäng', 'Barnen kan räkna själva.'),
      (t - 1.0, 'Nästa i raden', '')]
finish(d, 'xx06', 'poangskott', ['Poängskott', 'Avslutsövning'], 'Mål med målvakt och en rad framför',
       fp, 'AVSLUT', [], ex)
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ xx07 Fotbollsboccia ============
d = Drill()
XS = [18, 32, 46, 60, 74, 88]
for k, x in enumerate(XS): d.p(f'p{k}', '', B, (x, 84))
balls = [d.newball(rec(d, f'p{k}', 0)) for k in range(6)]
STOP = [46, 36, 41, 52, 38, 44]; t0 = 1.0
for k in range(6):
    d.mv(f'p{k}', 0.4, 1.0, (XS[k], 82)); d.carry(balls[k], f'p{k}', 0, 1.0)
    d.pas(balls[k], t0, (XS[k] + 1.8, STOP[k]), 1.8 + 0.1 * k)                                            # alla sparkar samtidigt
    hide(d, balls[k], 6.4); show(d, balls[k], 8.0, (XS[k] + 1.8, 60.8))
    d.mv(f'p{k}', 4.0, 6.4, (XS[k], STOP[k] + 3)); d.mv(f'p{k}', 6.4, 8.0, (XS[k], 62))                   # hämta – nytt avstånd
    d.pas(balls[k], 8.6, (XS[k] + 1.8, [42, 39, 44, 40, 37, 41][k]), 1.4 + 0.1 * k)
    hide(d, balls[k], 12.6)
fp = [(0, 'Barnen står på en rad', 'Parallellt med den kritade linjen.'),
      (t0, 'Alla sparkar samtidigt', 'Stanna så nära linjen som möjligt.'),
      (4.0, 'Vem kom närmast?', ''),
      (8.0, 'Nytt avstånd', 'Ändra mellan omgångarna.')]
finish(d, 'xx07', 'fotbollsboccia', ['Fotbolls-', 'boccia'], 'Kritad linje · Barnen på en rad',
       fp, 'PASSNINGSÖVNING', [('line', [(8, 40), (96, 40)])], [lab(3.4, 6.0, (62, 30), 'NÄRMAST'), lab(10.8, 12.6, (76, 30), 'NÄRMAST')])

# ============ lb01 Tå-touch och sulrullning ============
d = Drill()
ST = [(30, 34), (70, 34), (30, 68), (70, 68)]
for k, ps in enumerate(ST): d.p(f'p{k}', '', B, ps)
balls = []
for k, (x, y) in enumerate(ST):
    b = d.newball((x, y - 3.5)); balls.append(b); tr = d.balls[b]
    t = 0.4
    while t < 7.6: tr += [(t, (x - 0.8, y - 3.5)), (t + 0.25, (x + 0.8, y - 3.5))]; t += 0.5               # tå-touch: höger, vänster
    tr.append((8.0, (x, y - 3.5)))
    for j, dx in enumerate([6, -6, 6, -6]):                                                               # sulrullning i sidled
        t0 = 8.4 + 2.2 * j; d.mv(f'p{k}', t0, t0 + 1.8, (x + dx if j % 2 == 0 else x, y)); tr += [(t0, tr[-1][1]), (t0 + 1.8, (x + dx if j % 2 == 0 else x, y - 3.5))]
fp = [(0, 'Trippa med sulan ovanpå bollen', 'Höger, vänster – utan att sparka iväg den.'),
      (3.0, 'Räkna touch på 20 sekunder', ''),
      (8.4, 'Rulla bollen i sidled med sulan', ''),
      (13.0, 'Variant: gå runt bollen', 'Eller rulla bakåt och vänd.')]
finish(d, 'lb01', 'ta-touch-och-sulrullning', ['Tå-touch och', 'sulrullning'], 'En boll per barn · Går också att göra hemma',
       fp, 'TEKNIK', [], countup(0.5, 14, (50, 12), 0.5))
C[-1]['_stuck'] = True

# ============ lb02 Väggpassningar på tid ============
d = Drill()
XS = [26, 50, 74]
for k, x in enumerate(XS): d.p(f'p{k}', '', B, (x, 50))
balls = [d.newball(rec(d, f'p{k}', 0)) for k in range(3)]
cnt = []
for k, x in enumerate(XS):
    t = 0.4 + 0.15 * k
    for rep in range(10):
        foot = -1 if rep % 2 else 1                                                                       # växla fot
        t1 = d.pas(balls[k], t, (x + foot, 13), 0.5); t2 = d.pas(balls[k], t1, (x + 1.8 * foot, 48.8), 0.5)
        if k == 1: cnt.append(t1)
        if rep >= 5: t = t2 + 0.05                                                                        # bara ett touch
        else: d.carry(balls[k], f'p{k}', t2, t2 + 0.4); t = t2 + 0.45
fp = [(0, 'Passa med insidan mot väggen', 'Vägg, rebounder eller kompis.'),
      (2.0, 'Ta emot och passa igen', 'Växla fot varannan gång.'),
      (cnt[5] - 0.6, 'Variant: bara ett touch', ''),
      (cnt[8], 'Så många som möjligt på 30 sekunder', '')]
finish(d, 'lb02', 'vaggpassningar-pa-tid', ['Väggpassningar', 'På tid'], 'Vägg, rebounder eller en kompis',
       fp, 'PASSNINGSÖVNING', [('zone', 8, 4, 92, 12, (190, 190, 190), 'VÄGG')], counter(cnt, pos=(50, 70), last=None))

# ============ lb03 Målvaktslek ============
d = Drill(); d.p('mv', 'MV', ORA, (50, 6)); d.p('k', 'K', B, (50, 40)); d.p('q', '', ORA, (30, 14))
b = d.newball(rec(d, 'k', 0)); t = 0.4; ex = []
for rep, tx in enumerate([50, 42, 58, 46]):
    d.mv('mv', t + 0.3, t + 1.0, (tx, 7)); t1 = d.pas(b, t, (tx + 1.8, 8.8), 1.0)                            # lite vid sidan
    ex.append(lab(t1, t1 + 0.8, (66, 14), 'FÅNGA'))
    d.carry(b, 'mv', t1, t1 + 0.4); t2 = d.pas(b, t1 + 0.5, rec(d, 'k', t1 + 1.4), 0.9); t = t2 + 0.4        # rullar ut
d.mv('mv', t, t + 1.4, (30, 14)); d.mv('q', t, t + 1.4, (50, 7))                                           # alla får prova
fp = [(0, 'Bollen rullas eller kastas', 'I lagom tempo.'),
      (1.4, 'Fånga framför kroppen', 'Rulla eller kasta ut.'),
      (3.4, 'Kasta lite vid sidan', 'Barnet måste flytta fötterna.'),
      (t, 'Alla får prova att stå i mål', '')]
finish(d, 'lb03', 'malvaktslek', ['Målvaktslek', 'Lek och reaktion'], 'Mål och en kastare',
       fp, 'MÅLVAKT', [], ex)
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ lb04 Första touch åt sidan ============
d = Drill(); YS = [30, 70]
for k, y in enumerate(YS): d.p(f'a{k}', '', B, (24, y)); d.p(f'c{k}', '', B, (76, y))
balls = [d.newball(rec(d, f'a{k}', 0)) for k in range(2)]
ex = []
for k, y in enumerate(YS):
    t = 0.4 + 0.3 * k; hold, recv = f'a{k}', f'c{k}'
    for rep in range(6):
        side = 1 if rep % 3 != 1 else -1
        rx = 76 if recv[0] == 'c' else 24
        t1 = d.pas(balls[k], t, rec(d, recv, t + 1.0))
        if k == 0 and rep == 3: ex.append(lab(t1 - 0.8, t1 + 0.2, (50, y - 12), '”VÄNSTER!”'))
        d.mv(recv, t1, t1 + 0.5, (rx, y + 7 * side)); d.carry(balls[k], recv, t1, t1 + 0.5)                     # snett förbi konen
        d.mv(recv, t1 + 1.2, t1 + 2.0, (rx, y))
        hold, recv = recv, hold; t = t1 + 0.6
fp = [(0, 'Ta emot snett förbi konen', 'Två koner, vägg eller kompis.'),
      (2.0, 'Passa sedan igen', ''),
      (5.0, 'Variant: kompisen ropar sidan', 'Precis innan bollen kommer.'),
      (9.0, 'Båda fötterna', '')]
finish(d, 'lb04', 'forsta-touch-at-sidan', ['Första touch', 'åt sidan'], 'Två koner, vägg eller kompis',
       fp, 'PASSNINGSÖVNING', [('cone', 76, y) for y in YS] + [('cone', 24, y) for y in YS], ex)

# ============ lb05 Jonglering – nytt rekord ============
d = Drill()
ST = [(28, 32), (72, 32), (28, 70), (72, 70)]
for k, ps in enumerate(ST): d.p(f'p{k}', '', B, ps)
for k, (x, y) in enumerate(ST):
    b = d.newball((x + 1.8, y - 4)); tr = d.balls[b]; t = 0.4 + 0.2 * k
    for series, n in enumerate([1, 2, 3, 5]):
        for j in range(n): tr += [(t, (x + 1.8, y - 4)), (t + 0.25, (x + 1.8, y - 9)), (t + 0.5, (x + 1.8, y - 4))]; t += 0.5   # sparka upp – fånga
        t += 0.9
fp = [(0, 'Släpp bollen, sparka upp med vristen', 'Och fånga.'),
      (2.0, 'Två touch', ''),
      (4.4, 'Tre touch – och fler', 'Växla fot, använd låret.'),
      (8.0, 'Nytt rekord varje vecka', '')]
finish(d, 'lb05', 'jonglering-nytt-rekord', ['Jonglering', 'Nytt rekord'], 'En boll per spelare',
       fp, 'TEKNIK', [], [lab(0.4, 2.0, (50, 50), '1 TOUCH'), lab(2.0, 4.4, (50, 50), '2 TOUCH'), lab(4.4, 7.4, (50, 50), '3 TOUCH'), lab(7.4, 12, (50, 50), 'NYTT REKORD!')])
C[-1]['_stuck'] = True

# ============ lb06 Avslut efter inspel ============
d = Drill(); d.p('mv', 'MV', R, (50, 4)); d.p('pa', 'P', WHITE, (84, 30))
for k in range(3): d.p(f's{k}', '', B, (40, 52 + 6 * k))
pb = [d.newball((200, 200)) for _ in range(3)]
t = 0.4; marks = []
for k in range(3):
    show(d, pb[k], t, rec(d, 'pa', t))
    d.mv(f's{k}', t, t + 1.0, (46, 30)); t1 = d.pas(pb[k], t + 0.2, rec(d, f's{k}', t + 1.2), 1.0)              # längs marken från sidan
    if k < 2: d.carry(pb[k], f's{k}', t1, t1 + 0.4); t1 += 0.4                                                # ett touch
    tg = shoot(d, pb[k], t1 + 0.05, (46 + 4 * k, 1)); hide(d, pb[k], tg + 0.4); marks.append(tg)
    d.mv(f's{k}', tg + 0.2, tg + 2.6, (60, 64 + 6 * k))
    for j in range(k + 1, 3): d.mv(f's{j}', tg, tg + 0.8, (40, 52 + 6 * (j - k - 1)))
    t = tg + 0.4
fp = [(0, 'Passaren spelar längs marken', 'Från sidan.'),
      (1.4, 'Ta emot med ett touch och skjut', ''),
      (marks[1] + 0.4, 'Variant: direktskott', 'Eller svagare foten.'),
      (marks[2] - 0.4, 'Nästa spelare', '')]
finish(d, 'lb06', 'avslut-efter-inspel', ['Avslut efter', 'inspel'], 'Mål och en passare vid sidan',
       fp, 'AVSLUT', [])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ sr01 Fotbollsrundboll ============
d = Drill()
BASE = [(50, 88), (84, 58), (50, 28), (16, 58)]
team(d, 'k', B, [(50, 92), (40, 96), (60, 96)]); team(d, 'f', R, [(50, 58), (70, 36), (30, 36), (76, 76)]); d.p('pt', 'K', ORA, (50, 70))
b = d.newball(rec(d, 'pt', 0))
t = d.pas(b, 0.4, rec(d, 'k0', 1.3))                                                                       # rulla in
t = d.pas(b, t + 0.2, (34, 22), 1.3); tk = t                                                               # sparken
t2 = d.path('k0', tk - 1.0, [BASE[1], BASE[2]], 1.6)                                                       # spring runt baserna
d.mv('f2', tk - 1.0, tk, (36, 24)); d.carry(b, 'f2', tk, tk + 0.3)
t3 = d.pas(b, tk + 0.4, rec(d, 'f0', tk + 1.2)); d.mv('f0', tk, t3, (50, 62))
d.mv('f0', t3, t3 + 0.8, (50, 70)); d.carry(b, 'f0', t3, t3 + 0.8); tb = t3 + 0.8                          # till boet
d.mv('pt', t3 - 0.8, t3, (58, 74))
fp = [(0, 'Som rundboll – men med fötterna', 'Två lag.'),
      (tk - 0.8, 'Sparka och spring runt baserna', ''),
      (tk + 0.4, 'Fältlaget hämtar bollen', 'Och för den till boet.'),
      (tb, 'Står löparen på en bas?', 'Annars är löparen ute.')]
finish(d, 'sr01', 'fotbollsrundboll', ['Fotbolls-', 'rundboll'], 'Plan med baser · Två lag',
       fp, 'LEK', [('cone',) + c for c in BASE] + [('zone', 44, 64, 56, 76, (240, 210, 90), 'BO')], [lab(tb, tb + 1.8, (50, 80), 'BOLLEN I BOET')])

if __name__ == '__main__': render(C, sys.argv)
