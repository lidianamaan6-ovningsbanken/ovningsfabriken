# Externa övningar, omgång 22 (tolv st). Regel: först d.mv, sedan d.carry; först mottagarens rörelse, sedan passningen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e9', __file__.replace('render_extern22.py', 'render_extern9.py'))
e9 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e9); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e9.finish, e9.rec, e9.chain, e9.wander, e9.counter, e9.arrivals
lab, hide, show, team, boxes, drive, shoot = e9.lab, e9.hide, e9.show, e9.team, e9.boxes, e9.drive, e9.shoot
factor, swap_color, stand, countdown, countup, win = e9.factor, e9.swap_color, e9.stand, e9.countdown, e9.countup, e9.win
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'

# ============ mk01 Hajar och små fiskar ============
d = Drill(); d.p('h', 'H', R, (50, 50))
ST = [(24, 26), (50, 22), (76, 26), (24, 74), (50, 78), (76, 74)]
balls = []
for k, ps in enumerate(ST): d.p(f'p{k}', '', B, ps); balls.append(d.newball(rec(d, f'p{k}', 0)))
for k in (1, 2, 4, 5): wander(d, f'p{k}', 0, 17.9, boxes([ST[k]], 7)[0], 4400 + k, 1.6); d.carry(balls[k], f'p{k}', 0, 17.9)
d.mv('p3', 0, 2.6, (28, 62)); d.carry(balls[3], 'p3', 0, 2.6); d.mv('h', 0.3, 2.6, (33, 60))
tw = d.pas(balls[3], 2.8, rec(d, 'h', 3.0), 0.3); d.mv('h', tw, tw + 1.6, (50, 40)); d.carry(balls[3], 'h', tw, tw + 1.6)   # hajen tar bollen
hide(d, balls[3], tw + 1.7)
stand(d, 'p3', 2.6, 7.4)                                                                                     # fryser
d.mv('p0', 0, 4.2, (20, 56)); d.mv('p0', 4.2, 6.6, (24, 54)); d.carry(balls[0], 'p0', 0, 6.6)
t0 = 6.6; pts = [(34, 58), (34, 68), (22, 68), (22, 56)]; t1 = d.path('p0', t0, pts, 1.2); d.carry(balls[0], 'p0', t0, t1)   # dribblar runt – tinar upp
show(d, balls[3], t1 + 0.2, rec(d, 'p3', t1 + 0.2)); wander(d, 'p3', t1 + 0.2, 17.9, boxes([ST[3]], 7)[0], 4413, 1.6); d.carry(balls[3], 'p3', t1 + 0.2, 17.9)
wander(d, 'p0', t1, 17.9, boxes([ST[0]], 7)[0], 4410, 1.6); d.carry(balls[0], 'p0', t1, 17.9)
wander(d, 'h', tw + 1.6, 17.9, (40, 40, 60, 60), 4420, 1.6)
fp = [(0, 'Alla fiskar har en boll', 'Hajen jagar.'),
      (tw - 0.3, 'Av med bollen – frys', ''),
      (t0, 'Dribbla runt den frusna', 'Då tinar den upp.'),
      (t1 + 0.4, 'Fri igen', 'Föräldrar kan vara med som hajar.')]
finish(d, 'mk01', 'hajar-och-sma-fiskar', ['Hajar och', 'små fiskar'], 'Avgränsad yta · Alla fiskar har en boll',
       fp, 'LEK MED BOLL', [('box', 12, 12, 88, 88)], [lab(tw, t1, (28, 80), 'FRUSEN'), lab(t1, t1 + 1.6, (28, 80), 'UPPTINAD')])

# ============ mk02 Pacman – träffa tränaren ============
d = Drill(); d.p('t', 'T', T_COL, (50, 50))
ST = [(24, 26), (50, 18), (76, 26), (82, 56), (70, 80), (30, 80), (18, 54)]
balls = []
for k, ps in enumerate(ST): d.p(f'p{k}', '', B, ps); balls.append(d.newball(rec(d, f'p{k}', 0)))
for k in range(7): wander(d, f'p{k}', 0, 6.4, boxes([ST[k]], 6)[0], 4500 + k, 1.6); d.carry(balls[k], f'p{k}', 0, 6.4)
wander(d, 't', 0, 6.4, (42, 42, 58, 58), 4510, 1.6)
tsig = 6.6; d.mv('t', 6.4, 9.0, (60, 46))
for k in range(7):
    t1 = d.pas(balls[k], tsig + 0.2 + 0.25 * k, (61.8, 44.8), 0.8 + 0.05 * k)                                 # alla försöker träffa tränaren
    t2 = d.pas(balls[k], t1, (61.8 + (ST[k][0] - 60) * 0.3, 44.8 + (ST[k][1] - 46) * 0.3), 0.5); hide(d, balls[k], t2 + 0.3)
    d.mv(f'p{k}', t2, t2 + 2.0, (61.8 + (ST[k][0] - 60) * 0.32, 46 + (ST[k][1] - 46) * 0.36))
fp = [(0, 'Dribbla runt tränaren', 'Alla har en boll.'),
      (3.0, 'Tränaren rör sig', 'De yngsta: tränaren härmar ett djur.'),
      (tsig, '”NU!” – träffa tränaren med en passning', ''),
      (tsig + 2.4, 'Hämta bollen – nästa runda', '')]
finish(d, 'mk02', 'pacman-traffa-tranaren', ['Pacman', 'Träffa tränaren'], 'Avgränsad yta · Alla har en boll',
       fp, 'LEK MED BOLL', [('box', 10, 10, 90, 90)], [lab(tsig - 0.2, tsig + 1.4, (50, 34), '”NU!”')])

# ============ mk03 Barcelona – passningar blir poäng ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96))
BP = [(30, 66), (70, 62), (44, 46), (58, 30)]; RP = [(34, 36), (66, 34), (52, 54), (44, 22)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
for k in range(4): wander(d, f'r{k}', 0, 6, boxes([RP[k]], 4)[0], 4600 + k, 1.6)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b2', 'b1', 'b0', 'b2', 'b3'], 0.3); cnt = arrivals(d, b)[:5]
tg = shoot(d, b, t + 0.1, (46, 1))
fp = [(0, 'Tre mot tre eller fyra mot fyra', 'Mål i båda ändar.'),
      (cnt[1], 'Räkna passningarna', ''),
      (tg - 0.4, 'Mål efter fem passningar: 5 poäng', ''),
      (tg + 0.6, 'Inspark vid utboll', 'Flest poäng vinner.')]
finish(d, 'mk03', 'barcelona-passningar-blir-poang', ['Barcelona', 'Passningar blir poäng'], 'Rutnät med mål i båda ändar',
       fp, 'SMÅLAGSSPEL', [('box', 12, 2, 88, 98)], counter(cnt, pos=(84, 50), last=None) + [lab(tg, tg + 2.0, (46, 14), '+5')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ mk04 Triangelmål ============
d = Drill()
TRI = [(28, 28), (72, 26), (50, 52), (26, 74), (74, 76)]
def tri(c): x, y = c; return [('cone', x, y - 3), ('cone', x - 3, y + 2), ('cone', x + 3, y + 2)]
PAIRS = [((16, 28), (40, 28)), ((60, 76), (86, 76))]
ROUTE = {0: [0, 2, 3], 1: [4, 2, 1]}
for k, (a, c) in enumerate(PAIRS): d.p(f'a{k}', '', B, a); d.p(f'c{k}', '', B, c)
for k in range(2):
    bl = d.newball(rec(d, f'a{k}', 0)); t = 0.4 + 0.3 * k + (1.6 if k else 0); h, o = f'a{k}', f'c{k}'
    for gi in ROUTE[k] * 2:
        gx, gy = TRI[gi]
        d.mv(h, t, t + 2.0, (gx - 11, gy)); d.mv(o, t, t + 2.0, (gx + 11, gy)); d.carry(bl, h, t, t + 2.0)
        t = d.pas(bl, t + 2.1, rec(d, o, t + 2.7)) + 0.1; h, o = o, h                                         # genom triangeln
fp = [(0, 'Passa genom en triangel', 'Par med en boll.'),
      (2.6, 'Flytta till nästa triangel', ''),
      (7.0, 'Huvudet upp – välj en ledig', ''),
      (12.0, 'Omgångar på ungefär en minut', '')]
shapes = [s for c in TRI for s in tri(c)]
finish(d, 'mk04', 'triangelmal', ['Triangelmål', 'Passningsövning'], 'Rutnät med koner i trianglar · Par med en boll',
       fp, 'PASSNINGSÖVNING', [('box', 6, 10, 94, 90)] + shapes)

# ============ mk05 3 mot 2 mot mål ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
AP = [(30, 88), (50, 90), (70, 88)]; team(d, 'a', B, AP); team(d, 'f', R, [(42, 40), (58, 40)])
b = d.newball(rec(d, 'a1', 0))
for k, ps in enumerate([(30, 50), (50, 56), (70, 48)]): d.mv(f'a{k}', 0.4, 2.8, ps)
d.carry(b, 'a1', 0.4, 2.8); d.mv('f0', 1.2, 2.8, (46, 44)); d.mv('f1', 1.2, 2.8, (58, 38))
t = d.pas(b, 2.9, rec(d, 'a2', 3.6)); d.mv('a2', t, t + 1.0, (68, 28)); d.carry(b, 'a2', t, t + 1.0); t += 1.0
d.mv('a0', t - 1.6, t, (38, 22)); t = d.pas(b, t + 0.1, rec(d, 'a0', t + 0.9)); tg = shoot(d, b, t + 0.05, (44, 1)); hide(d, b, tg + 0.3)
for k in range(3): d.mv(f'a{k}', tg + 0.2, tg + 2.2, AP[k])
d.mv('f0', tg, tg + 1.6, (42, 40)); d.mv('f1', tg, tg + 1.6, (58, 40))
b2 = d.newball((200, 200)); show(d, b2, tg + 2.3, rec(d, 'a1', tg + 2.3))
t = d.pas(b2, tg + 2.5, rec(d, 'a0', tg + 3.2)); d.mv('a0', t, t + 1.0, (34, 54)); d.carry(b2, 'a0', t, t + 1.0); t += 1.0
tw = win(d, b2, 'f0', 'a0', t + 0.2, 0.6); t = drive(d, b2, 'f0', tw, (40, 96), 22)                           # dribbla över anfallarnas kortlinje
for k, ps in enumerate([(34, 70), (50, 74), (66, 72)]): d.mv(f'a{k}', tw, t, ps)
fp = [(0, 'Tre anfallare från kortlinjen', 'Mot två försvarare.'),
      (tg - 0.4, 'Mål – ny omgång', ''),
      (tw - 0.2, 'Försvararna vinner bollen', 'Mål genom att dribbla över anfallarnas kortlinje.'),
      (t - 0.4, 'Rotera in nya spelare', '')]
finish(d, 'mk05', '3-mot-2-mot-mal', ['3 mot 2', 'Mot mål'], 'Rutnät med ett mål i ena änden',
       fp, 'ÖVERLÄGE', [('line', [(10, 96), (90, 96)])])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ mk06 Femmålsspelet ============
d = Drill(); d.p('t', 'T', T_COL, (96, 50))
GL = [(30, 6), (70, 6), (30, 94), (70, 94), (50, 50)]
BP = [(30, 70), (70, 68), (46, 30), (60, 78)]; RP = [(34, 30), (66, 32), (38, 60), (62, 22)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 't', 0))
t = d.pas(b, 0.4, rec(d, 'b1', 1.4)); t = d.pas(b, t + 0.2, rec(d, 'b3', t + 0.9))
d.mv('b2', t - 1.0, t + 0.4, (44, 42)); t = d.pas(b, t + 0.2, rec(d, 'b2', t + 1.0)); tg = d.pas(b, t + 0.1, (50, 48), 0.4)   # mittmålet
d.mv('r2', tg - 0.6, tg + 0.4, (52, 56)); t = d.pas(b, tg + 0.5, rec(d, 'r2', tg + 0.9), 0.4)                  # bollförlust – rollerna byts
t = d.pas(b, t + 0.2, rec(d, 'r0', t + 1.0)); t = drive(d, b, 'r0', t, (30, 14), 18); tg2 = d.pas(b, t + 0.1, (30, 4), 0.4); hide(d, b, tg2 + 0.3)
fp = [(0, 'Tränaren spelar in', 'Fem mål: två i varje ände och ett i mitten.'),
      (tg - 0.4, 'Mål i vilket mål som helst', 'Även i mitten.'),
      (tg + 0.4, 'Bollförlust – rollerna byts', ''),
      (tg2 - 0.4, 'Nu gör rött mål', '')]
finish(d, 'mk06', 'femmalsspelet', ['Femmåls-', 'spelet'], 'Rutnät med fem mål',
       fp, 'SMÅLAGSSPEL', [('box', 8, 4, 92, 96)] + [('smallgoal',) + g for g in GL], [lab(tg, tg + 1.4, (50, 40), 'MÅL'), lab(tg2, tg2 + 1.6, (30, 14), 'MÅL')])

# ============ mk07 Hot box ============
d = Drill()
BP = [(30, 70), (70, 68), (30, 30), (70, 30)]; RP = [(36, 40), (64, 38), (40, 62), (60, 60)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
for k in range(4): wander(d, f'r{k}', 0, 8, boxes([RP[k]], 4)[0], 4700 + k, 1.6)
b = d.newball(rec(d, 'b0', 0))
t = d.pas(b, 0.4, rec(d, 'b3', 1.6), 1.2); tb = t                                                            # genom mittrutan – bara bollen
t = d.pas(b, t + 0.3, rec(d, 'b2', t + 1.3)); d.mv('b2', t - 1.0, t + 0.4, (30, 20))
t = drive(d, b, 'b2', t, (38, 10), 16); tg = shoot(d, b, t + 0.1, (46, 1)); hide(d, b, tg + 0.3)
fp = [(0, 'Ingen spelare i mittrutan', 'Bara bollen får gå igenom.'),
      (tb - 1.0, 'Spela genom rutan', ''),
      (tg - 0.6, 'Mål', 'Inga hörnor eller inkast – inspark.'),
      (tg + 0.4, 'Omgångar på fem minuter', '')]
finish(d, 'mk07', 'hot-box', ['Hot box', 'Smålagsspel'], 'Rutnät med mål i båda ändar · Liten ruta i mitten',
       fp, 'SMÅLAGSSPEL', [('box', 10, 2, 90, 98), ('zone', 40, 42, 60, 58, (230, 120, 110), 'HOT BOX')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ mk08 2 mot 2 mot 2 – håll bollen ============
d = Drill()
BP = [(22, 24), (78, 76)]; WP = [(78, 24), (22, 76)]; RP = [(44, 44), (56, 56)]
team(d, 'b', B, BP); team(d, 'w', WHITE, WP); team(d, 'r', R, RP)
for k in range(2): wander(d, f'b{k}', 0, 17.9, boxes([BP[k]], 6)[0], 4800 + k, 1.6); wander(d, f'w{k}', 0, 17.9, boxes([WP[k]], 6)[0], 4810 + k, 1.6)
wander(d, 'r0', 0, 4.4, boxes([RP[0]], 4)[0], 4820, 1.4); wander(d, 'r1', 0, 4.4, boxes([RP[1]], 4)[0], 4821, 1.4)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['w0', 'b1', 'w1', 'b0'], 0.3)
tw = win(d, b, 'r0', 'b0', t + 0.4, 0.8)                                                                      # blått rörde den senast – tar över
for k, ps in enumerate([(44, 44), (56, 56)]): d.mv(f'b{k}', tw + 0.2, tw + 1.6, ps)
wander(d, 'r1', tw, 17.9, (60, 60, 84, 84), 4822, 1.6); wander(d, 'r0', tw + 0.4, 17.9, (16, 18, 34, 34), 4823, 1.6)
t = chain(d, b, tw + 0.5, ['w0', 'r1', 'w1', 'r0'], 0.3)
fp = [(0, 'Två par håller bollen mot det tredje', 'Tre lag om två.'),
      (tw - 0.3, 'Försvararna vinner bollen', 'De tar över från paret som senast rörde den.'),
      (tw + 0.6, 'Spelet stannar inte', ''),
      (tw + 3.0, 'Variant: max två eller ett touch', '')]
finish(d, 'mk08', '2-mot-2-mot-2-hall-bollen', ['2 mot 2 mot 2', 'Håll bollen'], 'Kvadrat med koner · Tre lag om två',
       fp, 'RONDO', [('box', 12, 12, 88, 88)])

# ============ mk09 3 mot 3 + 1 – räkna passningar ============
d = Drill()
BP = [(26, 30), (74, 32), (40, 72)]; RP = [(44, 44), (60, 58), (30, 58)]
team(d, 'b', B, BP); team(d, 'r', R, RP); d.p('n', 'N', YEL, (60, 74))
for k in range(3): wander(d, f'b{k}', 0, 17.9, boxes([BP[k]], 7)[0], 4900 + k, 1.6); wander(d, f'r{k}', 0, 8, boxes([RP[k]], 5)[0], 4910 + k, 1.6)
wander(d, 'n', 0, 17.9, boxes([(60, 74)], 6)[0], 4920, 1.6)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b1', 'n', 'b2', 'b0', 'n', 'b1'], 0.35); cnt = arrivals(d, b)[:6]
tw = win(d, b, 'r0', 'b1', t + 0.3, 0.9)
for k in range(3): wander(d, f'r{k}', tw + 0.4, 17.9, boxes([RP[k]], 9)[0], 4930 + k, 1.6)
t = chain(d, b, tw + 0.5, ['r1', 'n', 'r2'], 0.35); cnt2 = arrivals(d, b)[-3:]
fp = [(0, 'Tre mot tre plus en neutral', 'Den neutrala hjälper laget med bollen.'),
      (cnt[1], 'Räkna passningarna', 'Tills laget tappar bollen.'),
      (tw - 0.2, 'Bollförlust – nu räknar rött', ''),
      (tw + 2.0, 'Byt roller efter en minut', '')]
finish(d, 'mk09', '3-mot-3-plus-1-rakna-passningar', ['3 mot 3 + 1', 'Räkna passningar'], 'Kvadrat per grupp om sju',
       fp, 'POSITIONSSPEL', [('box', 12, 14, 88, 86)], counter(cnt, pos=(26, 8), last=None) + counter(cnt2, pos=(74, 8), last=None))

# ============ mk10 Tagg med tio touch ============
d = Drill(); d.p('tg', 'T', R, (50, 50))
ST = [(22, 24), (48, 20), (74, 26), (24, 72), (50, 76), (72, 70)]
balls = []
for k, ps in enumerate(ST): d.p(f'p{k}', '', B, ps); balls.append(d.newball(rec(d, f'p{k}', 0)))
for k in (0, 1, 3, 4, 5): wander(d, f'p{k}', 0, 17.9, boxes([ST[k]], 6)[0], 5000 + k, 1.6); d.carry(balls[k], f'p{k}', 0, 17.9)
d.mv('p2', 0, 2.4, (72, 40)); d.mv('tg', 0.3, 2.4, (68, 42)); tt = 2.4                                         # tagen
d.mv('p2', tt + 0.2, tt + 1.8, (94, 40)); stand(d, 'p2', tt + 1.8, tt + 5.0); d.mv('p2', tt + 5.0, tt + 6.4, (72, 30))   # straffzonen – tio touch – tillbaka
wander(d, 'p2', tt + 6.4, 17.9, boxes([ST[2]], 6)[0], 5012, 1.6); d.carry(balls[2], 'p2', 0, 17.9)
wander(d, 'tg', tt + 0.4, 17.9, (36, 36, 64, 64), 5020, 1.6)
fp = [(0, 'Taggaren jagar dribblarna', 'Alla har en boll.'),
      (tt - 0.2, 'Tagen – gå till straffzonen', ''),
      (tt + 1.8, 'Tio bollkontakter', 'Till exempel toe taps.'),
      (tt + 5.0, 'Tillbaka in', '')]
finish(d, 'mk10', 'tagg-med-tio-touch', ['Tagg med', 'tio touch'], 'Avgränsad yta med en straffzon vid sidan · Alla har en boll',
       fp, 'LEK', [('box', 10, 10, 84, 90), ('zone', 86, 30, 100, 56, (230, 120, 110), 'STRAFF')],
       [lab(tt, tt + 1.4, (66, 48), 'TAGEN')] + countup(tt + 1.8, 10, (94, 26), 0.32))

# ============ mk11 1 mot 1 till koner ============
d = Drill()
d.p('a', 'A', B, (24, 50)); d.p('f', 'F', R, (52, 50))
b = d.newball(rec(d, 'a', 0)); ex = []; t = 0.4
for rep, (to, def_) in enumerate([((80, 44), (60, 52)), ((20, 56), (36, 50)), ((80, 58), (66, 48))]):
    sx = 1 if to[0] > 50 else -1
    d.mv('a', t, t + 1.0, (50 + sx * -4, 40 if rep != 1 else 60)); d.carry(b, 'a', t, t + 1.0)                    # finta
    d.mv('f', t, t + 1.0, def_)
    d.mv('a', t + 1.0, t + 2.4, to); d.carry(b, 'a', t + 1.0, t + 2.4); d.mv('f', t + 1.0, t + 2.4, (to[0] - sx * 8, to[1]))
    ex.append(lab(t + 2.4, t + 3.6, (to[0], to[1] - 10), '+1')); t += 3.0
d.mv('a', t, t + 1.0, (60, 46)); d.carry(b, 'a', t, t + 1.0); tw = win(d, b, 'f', 'a', t + 1.0, 0.5)
d.mv('f', tw, tw + 1.6, (22, 50)); d.carry(b, 'f', tw, tw + 1.6)                                               # byt roller
fp = [(0, 'Dribbla till konerna', 'Försvararen försöker stoppa.'),
      (2.8, 'Nådde konen: poäng', ''),
      (3.4, 'Fram och tillbaka', ''),
      (tw - 0.2, 'Försvararen vinner – byt roller', '')]
finish(d, 'mk11', '1-mot-1-till-koner', ['1 mot 1', 'Till koner'], 'Två konpar · 1 mot 1',
       fp, 'DUELL', [('cone', 84, 40), ('cone', 84, 62), ('cone', 16, 40), ('cone', 16, 62)], ex)

# ============ mk12 Bollbehärskning ============
d = Drill()
ST = [(30, 34), (70, 34), (30, 68), (70, 68)]
for k, ps in enumerate(ST): d.p(f'p{k}', '', B, ps)
for k, (x, y) in enumerate(ST):
    b = d.newball((x, y - 3.5)); tr = d.balls[b]; t = 0.4
    while t < 5.6: tr += [(t, (x - 0.8, y - 3.5)), (t + 0.25, (x + 0.8, y - 3.5))]; t += 0.5                  # tåtramp
    while t < 11.0: tr += [(t, (x - 2.5, y - 1)), (t + 0.3, (x + 2.5, y - 1))]; t += 0.6                     # mellan insidorna
    while t < 16.6: tr += [(t, (x, y - 3.5)), (t + 0.4, (x, y - 1)), (t + 0.8, (x + 2.5, y - 1)), (t + 1.2, (x, y - 3.5))]; t += 1.6   # triangeln
fp = [(0, 'Tåtramp ovanpå bollen', 'En boll per spelare.'),
      (5.6, 'Bollen mellan insidorna', 'Bell taps.'),
      (11.0, 'Triangeln', 'Dra tillbaka, insida till andra foten, tillbaka.'),
      (15.0, '30 sekunder till en minut per teknik', '3–4 set.')]
finish(d, 'mk12', 'bollbeharskning-toe-taps-bell-taps-trianglar', ['Bollbehärskning', 'Toe taps, bell taps, trianglar'], 'En boll per spelare',
       fp, 'TEKNIK', [], [lab(0.4, 5.6, (50, 10), 'TOE TAPS'), lab(5.6, 11.0, (50, 10), 'BELL TAPS'), lab(11.0, 17.0, (50, 10), 'TRIANGEL')])
C[-1]['_stuck'] = True

if __name__ == '__main__': render(C, sys.argv)
