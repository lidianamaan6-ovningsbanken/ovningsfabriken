# Externa övningar, omgång 25 (tolv st). Regel: först d.mv, sedan d.carry; först mottagarens rörelse, sedan passningen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e9', __file__.replace('render_extern25.py', 'render_extern9.py'))
e9 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e9); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e9.finish, e9.rec, e9.chain, e9.wander, e9.counter, e9.arrivals
lab, hide, show, team, boxes, drive, shoot = e9.lab, e9.hide, e9.show, e9.team, e9.boxes, e9.drive, e9.shoot
factor, swap_color, stand, countdown, countup, win = e9.factor, e9.swap_color, e9.stand, e9.countdown, e9.countup, e9.win
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'; GRN = '#3fbf5f'

# ============ ds04 Fånga dem ============
d = Drill(); d.p('j', '', R, (50, 50))
ST = [(26, 26), (50, 22), (74, 26), (78, 52), (72, 76), (48, 80), (24, 72)]
for k, ps in enumerate(ST): d.p(f'p{k}', '', B, ps)
for k in (1, 2, 3, 4, 5): wander(d, f'p{k}', 0, 17.9, boxes([ST[k]], 7)[0], 6500 + k, 1.4)
jb = d.newball(rec(d, 'j', 0))
d.mv('p0', 0, 2.6, (30, 34)); d.mv('j', 0.2, 2.4, (36, 38)); d.carry(jb, 'j', 0, 2.4)
t1 = d.pas(jb, 2.5, (31, 36), 0.3); t1b = d.pas(jb, t1, rec(d, 'j', t1 + 0.6), 0.5)                       # träff under midjan inom 1 m
nb = d.newball((200, 200)); show(d, nb, t1 + 0.6, rec(d, 'p0', t1 + 0.6))                                   # den som träffas får en boll
wander(d, 'j', t1b, 17.9, (36, 36, 64, 64), 6510, 1.6); d.carry(jb, 'j', t1b, 17.9)
d.mv('p0', t1 + 0.6, t1 + 3.0, (30, 60)); d.carry(nb, 'p0', t1 + 0.6, t1 + 3.0)
d.mv('p6', 0, t1 + 3.0, (24, 70)); d.mv('p0', t1 + 3.0, t1 + 4.6, (26, 66)); d.carry(nb, 'p0', t1 + 3.0, t1 + 4.6)
t2 = d.pas(nb, t1 + 4.8, (24, 68), 0.3); t2b = d.pas(nb, t2, rec(d, 'p0', t2 + 0.6), 0.5)
nb2 = d.newball((200, 200)); show(d, nb2, t2 + 0.6, rec(d, 'p6', t2 + 0.6))
wander(d, 'p0', t2b, 17.9, (16, 40, 40, 70), 6511, 1.6); d.carry(nb, 'p0', t2b, 17.9)
wander(d, 'p6', t2 + 0.6, 17.9, (16, 64, 36, 84), 6512, 1.6); d.carry(nb2, 'p6', t2 + 0.6, 17.9)
fp = [(0, 'Jagaren dribblar', 'Och försöker träffa de andra med bollen.'),
      (t1 - 0.4, 'Träff under midjan – inom 1 m', 'Den som träffas får en boll och jagar med.'),
      (t2 - 0.4, 'Fler jagare', ''),
      (t2 + 1.4, 'Sista kvar startar nästa omgång', 'Börja med två jagare om det är svårt.')]
finish(d, 'ds04', 'fanga-dem', ['Fånga dem', 'Lek och reaktion'], 'Yta 8 × 8 m · Åtta spelare · En jagare med boll',
       fp, 'LEK', [('box', 14, 14, 86, 86)], [lab(t1, t1 + 1.4, (30, 26), 'TRÄFF'), lab(t2, t2 + 1.4, (24, 60), 'TRÄFF')])
f = factor(fp); ids = {k: i for i, k in enumerate(d.order)}
swap_color(ids['p0'], (t1 + 0.4) * f, B, R); swap_color(ids['p6'], (t2 + 0.4) * f, B, R)

# ============ ds05 Tacklingsrutan ============
d = Drill()
d.p('t', 'T', R, (50, 40)); team(d, 'a', B, [(50, 84), (40, 88), (60, 88)], ['A', 'A', 'A'])
balls = [d.newball(rec(d, f'a{k}', 0)) for k in range(3)]; ex = []; t = 0.4
for k in range(3):
    pid = f'a{k}'
    if k: d.mv(pid, t - 0.8, t, (50, 84))
    d.carry(balls[k], pid, 0, t)
    d.mv(pid, t, t + 1.4, (50, 60)); d.carry(balls[k], pid, t, t + 1.4); d.mv('t', t + 0.4, t + 1.4, (50, 56))   # tacklaren möter halvvägs
    tb = t + 1.4; ex.append(lab(tb, tb + 1.0, (64, 56), 'BLOCK')); stand(d, pid, tb, tb + 0.5); stand(d, 't', tb, tb + 0.5)
    hide(d, balls[k], tb + 0.5)
    d.mv(pid, tb + 0.5, tb + 2.4, (40 + 10 * k, 94)); d.mv('t', tb + 0.5, tb + 1.6, (50, 40)); t = tb + 1.6
fp = [(0, 'Anfallarna springer in en i taget', 'Ruta 4 × 4 m, grupper om fyra.'),
      (1.4, 'Möt halvvägs – blocktackling', ''),
      (4.6, 'Två tacklingar i rad, sedan byte', ''),
      (t - 1.0, 'När tekniken sitter', 'Får anfallaren försöka dribbla förbi.')]
finish(d, 'ds05', 'tacklingsrutan', ['Tacklings-', 'rutan'], 'Ruta 4 × 4 m · Grupper om fyra',
       fp, 'DUELL', [('box', 30, 30, 70, 78)], ex)

# ============ ds06 Tacklingslinjen ============
d = Drill()
d.p('a', 'A', B, (30, 70)); d.p('f', 'F', R, (30, 40)); d.p('a2', 'A', B, (24, 92)); d.p('f2', 'F', R, (16, 30))
b = d.newball(rec(d, 'a', 0))
d.mv('a', 0.4, 4.0, (70, 70)); d.carry(b, 'a', 0.4, 3.0); d.mv('f', 0.6, 2.8, (60, 64))                         # gående först
tw = d.pas(b, 3.0, (64, 78), 0.6); hide(d, b, tw + 0.4)                                                      # tacklad ut över sidlinjen
d.mv('a', 4.0, 6.0, (16, 92)); d.mv('f', 3.0, 5.6, (10, 30)); d.mv('a2', 3.6, 5.0, (30, 70)); d.mv('f2', 3.6, 5.6, (30, 40))
b2 = d.newball((200, 200)); show(d, b2, 5.2, rec(d, 'a2', 5.2))
d.mv('a2', 5.6, 8.0, (70, 70)); d.carry(b2, 'a2', 5.6, 7.4); d.mv('f2', 5.8, 7.4, (62, 64))                     # högre fart
tw2 = d.pas(b2, 7.4, (66, 78), 0.5); hide(d, b2, tw2 + 0.4)
fp = [(0, 'Anfallaren dribblar mellan konerna', 'Försvararen startar 5 m från första konen.'),
      (tw - 0.6, 'Tackla bollen ut över sidlinjen', ''),
      (5.2, 'Börja gående – öka sedan farten', ''),
      (tw2 - 0.4, 'Låt försvararen lyckas i början', '')]
finish(d, 'ds06', 'tacklingslinjen', ['Tacklings-', 'linjen'], 'Två koner 10 m isär · Tänkt sidlinje 1 m bort',
       fp, 'DUELL', [('cone', 30, 66), ('cone', 70, 66), ('line', [(20, 76), (80, 76)])], [lab(tw, tw + 1.4, (66, 84), 'UT'), lab(tw2, tw2 + 1.4, (66, 84), 'UT')])

# ============ ds07 Skottlagen ============
d = Drill(); d.p('mv', 'MV', R, (50, 4)); d.p('t', 'T', T_COL, (92, 40))
team(d, 'a', B, [(36, 30), (50, 34), (64, 30)]); team(d, 'f', R, [(42, 20), (58, 20)]); team(d, 'h', WHITE, [(8, 60), (92, 60)], ['H', 'H'])
t = 0.4; ex = []
for k, (to, out) in enumerate([('a1', 'MÅL'), ('a0', 'RÄDDNING'), ('a2', 'MÅL')]):
    bl = d.newball((200, 200)); show(d, bl, t, rec(d, 't', t)); t1 = d.pas(bl, t + 0.2, rec(d, to, t + 1.2), 1.0)   # bollen kastas in
    d.mv(f'f{k % 2}', t, t1, (at(d.pl[to]['tr'], t1)[0] - 4, at(d.pl[to]['tr'], t1)[1] - 6))
    tg = shoot(d, bl, t1 + 0.1, (46 + 4 * k, 1 if out == 'MÅL' else 5)); ex.append(lab(tg, tg + 1.2, (76, 14), out))
    if out == 'RÄDDNING': d.mv('mv', tg - 0.3, tg, (50, 5))
    hide(d, bl, tg + 0.3); t = tg + 0.6
d.mv('h0', t - 2.0, t, (30, 8)); d.mv('h1', t - 2.0, t, (70, 8))                                              # hämtarlaget samlar
fp = [(0, 'Bollar kastas, studsas eller rullas in', 'Under två minuter.'),
      (1.4, 'Anfall och försvar kämpar om bollen', 'Anfallarna skjuter.'),
      (ex[1]['t0'], 'Mål ger poäng', ''),
      (t - 1.2, 'Hämtarlaget samlar bollar', 'Sedan roterar lagen.')]
finish(d, 'ds07', 'skottlagen', ['Skott-', 'lagen'], 'Straffområdet · Tre lag',
       fp, 'AVSLUT', [], ex)
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ ds08 2 mot 2 + växlare, passningsmål ============
d = Drill()
team(d, 'b', B, [(36, 66), (64, 62)]); team(d, 'r', R, [(40, 36), (60, 34)]); d.p('v', 'V', YEL, (50, 50))
wander(d, 'r0', 0, 6, boxes([(40, 36)], 4)[0], 6600, 1.6); wander(d, 'r1', 0, 6, boxes([(60, 34)], 4)[0], 6601, 1.6)
b = d.newball(rec(d, 'b0', 0))
t = d.pas(b, 0.4, rec(d, 'v', 1.2)); t = d.pas(b, t + 0.3, rec(d, 'b1', t + 1.0))
d.mv('b1', t, t + 1.4, (58, 20)); d.carry(b, 'b1', t, t + 1.4); t += 1.4
tg = d.pas(b, t + 0.1, (50, 9), 0.6); hide(d, b, tg + 0.3)                                                    # passas in längs marken
b2 = d.newball((200, 200)); show(d, b2, tg + 1.0, rec(d, 'r0', tg + 1.0))
t = d.pas(b2, tg + 1.2, rec(d, 'v', tg + 2.0)); t = d.pas(b2, t + 0.3, rec(d, 'r1', t + 1.0))
d.mv('r1', t, t + 1.4, (56, 76)); d.carry(b2, 'r1', t, t + 1.4); t += 1.4; tg2 = d.pas(b2, t + 0.1, (50, 91), 0.6); hide(d, b2, tg2 + 0.3)
fp = [(0, 'Två mot två plus växlare', 'Växlaren spelar med laget som har bollen.'),
      (tg - 0.8, 'Passa in bollen längs marken', 'Bara då räknas målet.'),
      (tg + 1.0, 'Nu anfaller rött', ''),
      (tg2 - 0.4, 'Omgångar på tre minuter', 'Alla turas om att vara växlare.')]
finish(d, 'ds08', '2-mot-2-plus-vaxlare-passningsmal', ['2 mot 2 + växlare', 'Passningsmål'], 'Yta 8 × 8 m med småmål i varje ände',
       fp, 'SMÅLAGSSPEL', [('box', 22, 8, 78, 92), ('smallgoal', 50, 8), ('smallgoal', 50, 92)])

# ============ ds09 Tränarledd match på halvplan ============
d = Drill(); d.p('mv', 'MV', R, (50, 4)); d.p('t', 'T', T_COL, (50, 96))
AP = [(24, 50), (40, 56), (60, 56), (76, 50), (50, 40)]; DP = [(36, 26), (50, 22), (64, 26)]
team(d, 'a', B, AP); team(d, 'f', R, DP)
b = d.newball(rec(d, 't', 0))
t = d.pas(b, 0.4, rec(d, 'a1', 1.6)); t = chain(d, b, t, ['a4', 'a3'], 0.3)
d.mv('a3', t, t + 1.0, (70, 26)); d.carry(b, 'a3', t, t + 1.0); t += 1.0; tg = shoot(d, b, t + 0.1, (54, 1)); hide(d, b, tg + 0.3)
b2 = d.newball((200, 200)); show(d, b2, tg + 0.6, rec(d, 't', tg + 0.6))                                    # kontinuerligt spel
for k in range(5): d.mv(f'a{k}', tg, tg + 1.6, AP[k])
t = d.pas(b2, tg + 0.8, rec(d, 'a0', tg + 2.0)); tw = win(d, b2, 'f0', 'a0', t + 0.6, 0.8)
t = d.pas(b2, tw + 0.3, rec(d, 't', tw + 1.8), 1.4); tt = t                                                    # försvararna passar tillbaka till tränaren
fp = [(0, 'Tränaren servar bollen', 'Fem anfallare mot tre försvarare och målvakt.'),
      (tg - 0.6, 'Mål', 'Ny boll direkt – kontinuerligt spel.'),
      (tw - 0.2, 'Försvararna vinner bollen', 'Och passar tillbaka till tränaren.'),
      (tt, 'Variant: 3 mot 5 eller 8 mot 6', '')]
finish(d, 'ds09', 'tranarledd-match-pa-halvplan', ['Tränarledd match', 'på halvplan'], 'Halvplan · Två lag och tränaren som server',
       fp, 'SPELÖVNING', [])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ ds10 Stoppa skottet – målvaktstrio ============
d = Drill(); d.p('m1', 'MV1', ORA, (50, 5)); d.p('m2', 'MV2', ORA, (50, 40)); d.p('m3', 'MV3', ORA, (50, 70))
d.pl['m3']['tr'] = [(0, (28, 26))]
b = d.newball(rec(d, 'm2', 0)); t = 0.4; role = {'G': 'm1', 'S': 'm2', 'P': 'm3'}
for rep, tgt in enumerate([(44, 8), (56, 6), (46, 8)]):
    g, s_, p = role['G'], role['S'], role['P']
    d.mv(g, t + 0.3, t + 0.9, tgt); t1 = d.pas(b, t, (tgt[0] + 1.8, tgt[1] - 1.2), 0.9)                  # skott – räddning
    d.mv(s_, t1, t1 + 2.2, (50, 6))                                                                       # skytten springer in i mål
    d.mv(g, t1 + 0.2, t1 + 1.0, (40, 12)); t2 = d.pas(b, t1 + 1.0, rec(d, p, t1 + 1.8), 0.8)              # kastar ut till straffpunkten
    d.mv(g, t2, t2 + 1.4, (28, 26)); d.mv(p, t2, t2 + 1.2, (50, 40)); d.carry(b, p, t2, t2 + 1.2)
    role = {'G': s_, 'S': p, 'P': g}; t = t2 + 1.4
fp = [(0, 'MV2 skjuter mot MV1', 'Tre målvakter.'),
      (1.4, 'MV2 springer in i mål', 'MV1 kastar ut till MV3 vid straffpunkten.'),
      (4.6, 'Nästa skott – en lobb', 'Växla markskott och lobbar.'),
      (8.0, 'Anpassa kraften efter ålder', '')]
finish(d, 'ds10', 'stoppa-skottet-malvaktstrio', ['Stoppa skottet', 'Målvaktstrio'], 'Mål 3,64 m · Tre målvakter',
       fp, 'MÅLVAKT', [])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True
for pl in C[-1]['players']: pl['label'] = pl['label'].replace('MV', '')

# ============ ds11 Målvaktskriget ============
d = Drill(); d.p('m1', 'MV', ORA, (50, 22)); d.p('m2', 'MV', B, (50, 78))
b = d.newball(rec(d, 'm1', 0)); t = 0.4; ex = []
for rep, tx in enumerate([42, 58, 46, 54, 40]):
    a, c = ('m1', 'm2') if rep % 2 == 0 else ('m2', 'm1')
    ty = 80 if a == 'm1' else 20; save = rep != 3
    d.mv(c, t + 0.3, t + 0.8, (tx if save else 50 + (tx - 50) * 0.3, ty - 2 if c == 'm2' else ty + 2))
    t1 = d.pas(b, t, (tx + 1.8, ty - 1.2) if save else (tx, 82 if a == 'm1' else 18), 0.8)
    if not save: ex.append(lab(t1, t1 + 1.4, (70, 50), 'MÅL')); hide(d, b, t1 + 0.3); show(d, b, t1 + 1.0, rec(d, c, t1 + 1.0)); t1 += 0.8
    d.mv(c, t1 + 0.2, t1 + 0.8, (50, ty - 2 if c == 'm2' else ty + 2)); t = t1 + 0.6
fp = [(0, 'Två målvakter mot varandra', 'Två mål ca 15 m isär.'),
      (1.4, 'Försök göra mål på den andra', ''),
      (5.0, 'Snabbare och snabbare', 'Tränar reflexerna.'),
      (ex[0]['t0'] if ex else 8.0, 'Mål när bollen passerar linjen', '')]
finish(d, 'ds11', 'malvaktskriget', ['Målvakts-', 'kriget'], 'Två mål ca 15 m isär',
       fp, 'MÅLVAKT', [('ugoal', 50, 18, 'down'), ('ugoal', 50, 82, 'up')], ex)

# ============ if01 Bollbehärskning vid koner ============
d = Drill()
CN = [(20 + 15 * i, 20 + 15 * j) for i in range(5) for j in range(5)]
ST = [CN[0], CN[6], CN[12], CN[18], CN[24], CN[8], CN[16]]
for k, ps in enumerate(ST): d.p(f'p{k}', '', B, (ps[0] + 3, ps[1] + 3))
for k, ps in enumerate(ST):
    bb = d.newball((ps[0] + 4.8, ps[1] + 1.8)); tr = d.balls[bb]; t = 0.4
    x, y = ps[0] + 3, ps[1] + 3
    while t < 5.0: tr += [(t, (x + 0.8, y - 1.2)), (t + 0.25, (x + 2.6, y - 1.2))]; t += 0.5                        # toe taps
    nxt = CN[(CN.index(ps) + 1) % 25]; d.mv(f'p{k}', 5.2, 7.4, (nxt[0] + 3, nxt[1] + 3))                          # till närmaste fria kon
    tr += [(5.2, tr[-1][1]), (7.4, (nxt[0] + 4.8, nxt[1] + 1.8))]
    x, y = nxt[0] + 3, nxt[1] + 3; t = 7.6
    while t < 17.6: tr += [(t, (x + 0.6, y - 1.2)), (t + 0.3, (x + 3.0, y - 1.2))]; t += 0.6                       # slaps och in–ut
fp = [(0, 'En teknikuppgift vid varje kon', 'Fler koner än spelare.'),
      (2.4, 'Toe taps', ''),
      (5.2, 'Ingen kö – byt till närmaste fria kon', 'Med huvudet upp.'),
      (9.0, 'Slaps med utsidan och in–ut', 'Variant: olika uppgift per konfärg.')]
finish(d, 'if01', 'bollbeharskning-vid-koner', ['Bollbehärskning', 'vid koner'], 'Yta ca 18 × 18 m · Fler koner än spelare',
       fp, 'TEKNIK', [('cone',) + c for c in CN])
C[-1]['_stuck'] = True

# ============ if02 Dribbla och följ ============
d = Drill()
PR = [((26, 30), (26, 42)), ((70, 30), (70, 42)), ((26, 66), (26, 78)), ((70, 66), (70, 78))]
for k, (a, c) in enumerate(PR): d.p(f'd{k}', 'D', B, a); d.p(f'f{k}', 'F', ORA, c)
for k, (a, c) in enumerate(PR):
    bb = d.newball(rec(d, f'd{k}', 0))
    wander(d, f'd{k}', 0, 8.0, (a[0] - 10, a[1] - 6, a[0] + 10, a[1] + 6), 6700 + k, 2.0)
    tr = d.pl[f'd{k}']['tr']; d.pl[f'f{k}']['tr'] = [(0, c)] + [(t + 0.8, (x, y + 9)) for t, (x, y) in tr if t > 0]   # följer efter
    d.carry(bb, f'd{k}', 0, 8.2)
    t1 = d.pas(bb, 8.4, rec(d, f'f{k}', 8.9), 0.5)                                                             # signal – byt roller
    wander(d, f'f{k}', t1, 17.9, (c[0] - 10, c[1] - 6, c[0] + 10, c[1] + 4), 6710 + k, 2.0); d.carry(bb, f'f{k}', t1, 17.9)
    tr2 = d.pl[f'f{k}']['tr']; d.pl[f'd{k}']['tr'] = [(t, q) for t, q in d.pl[f'd{k}']['tr'] if t <= t1] + [(t + 0.8, (x, y - 9)) for t, (x, y) in tr2 if t > t1]
fp = [(0, 'Den ena dribblar, den andra följer', 'Par med en boll.'),
      (4.0, 'Följ efter – håll avståndet', ''),
      (8.4, 'Signal: byt roller', ''),
      (12.0, 'Variant: följaren får egen boll', 'Och försöker tagga dribblarens rygg.')]
finish(d, 'if02', 'dribbla-och-folj', ['Dribbla och', 'följ'], 'Yta ca 14–18 m · Par med en boll',
       fp, 'TEKNIK', [], [lab(8.2, 9.8, (50, 50), 'BYT!')])

# ============ if03 3 mot 3 med återvändare ============
d = Drill(); d.p('mv', 'MV', R, (50, 4)); d.p('t', 'T', T_COL, (50, 96))
team(d, 'a', B, [(30, 60), (50, 66), (70, 60)]); team(d, 'f', R, [(38, 34), (62, 34), (50, 24)]); team(d, 'x', R, [(6, 74), (6, 82)], ['Å', 'Å'])
b = d.newball(rec(d, 't', 0))
t = d.pas(b, 0.4, rec(d, 'a1', 1.4)); d.carry(b, 'a1', t, t + 0.3); t1 = t
d.mv('x0', t1, t1 + 2.6, (40, 30))                                                                         # första återvändaren efter första touchen
t = d.pas(b, t + 0.4, rec(d, 'a2', t + 1.1)); d.carry(b, 'a2', t, t + 0.3); d.mv('a2', t, t + 0.9, (66, 36)); d.carry(b, 'a2', t + 0.3, t + 0.9); t3 = t + 0.9
d.mv('x1', t3, t3 + 2.4, (58, 26))                                                                         # andra efter tredje touchen
d.mv('a0', 1.0, t3, (36, 30)); t = d.pas(b, t3 + 0.1, rec(d, 'a0', t3 + 0.8)); tg = shoot(d, b, t + 0.05, (44, 1))
fp = [(0, 'Tre anfallare mot tre försvarare', 'Tränaren matar in bollen.'),
      (t1, 'Första återvändaren släpps', 'Efter anfallarnas första touch.'),
      (t3, 'Andra återvändaren släpps', 'Efter tredje touchen.'),
      (tg - 0.4, 'Mål med skott', 'Lagen byter roller.')]
finish(d, 'if03', '3-mot-3-med-atervandare', ['3 mot 3', 'Med återvändare'], 'Yta ca 23 × 16 m · Mål och målvakt · Återvändarbox',
       fp, 'SPELÖVNING', [('box', 14, 4, 86, 92), ('zone', 0, 68, 12, 90, (230, 120, 110), '')], [lab(t1, t1 + 1.2, (16, 66), 'GÅ!'), lab(t3, t3 + 1.2, (16, 66), 'GÅ!')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ if04 Frys och tina ============
d = Drill()
ST = [(22, 24), (48, 20), (76, 26), (24, 74), (50, 78), (76, 72), (30, 50), (70, 50)]
for k, ps in enumerate(ST): d.p(f'p{k}', '', B, ps)
team(d, 'f', R, [(44, 44), (56, 58)], ['F', 'F'])
for k in (1, 2, 4, 5, 7): wander(d, f'p{k}', 0, 17.9, boxes([ST[k]], 7)[0], 6800 + k, 1.4)
d.mv('p0', 0, 2.4, (28, 32)); d.mv('f0', 0.2, 2.4, (32, 34)); tf = 2.4; stand(d, 'p0', tf, 6.4)               # frusen
d.mv('p6', 0, 5.6, (26, 44)); d.mv('p6', 5.6, 6.2, (29, 36)); tt = 6.2                                          # tinare rör vid
wander(d, 'p0', 6.6, 17.9, boxes([ST[0]], 7)[0], 6810, 1.4); wander(d, 'p6', 6.6, 17.9, boxes([ST[6]], 7)[0], 6816, 1.4)
d.mv('p3', 0, 8.6, (30, 66)); d.mv('f1', 2.0, 8.6, (36, 64)); stand(d, 'p3', 8.6, 12.0); d.mv('p3', 12.0, 17.9, (22, 76))
wander(d, 'f0', 2.6, 17.9, (36, 30, 64, 46), 6820, 1.6); wander(d, 'f1', 8.8, 17.9, (40, 54, 64, 70), 6821, 1.6)
fp = [(0, '2–3 frysare, resten tinare', ''),
      (tf - 0.3, 'Frusen – stå stilla', ''),
      (tt - 0.4, 'En tinare rör vid dig – fri igen', ''),
      (12.0, 'Frysarna byts varje minut', 'Variant: frys i olika balansställningar.')]
d.newball((200, 200))                                                                     # leken har ingen boll
_g = finish.__globals__; _bl = _g['_ball_last']; _g['_ball_last'] = lambda balls: 99
finish(d, 'if04', 'frys-och-tina', ['Frys och tina', 'Lek och reaktion'], 'Yta ca 18–27 m',
       fp, 'LEK', [('box', 12, 12, 88, 88)], [lab(tf, tt, (28, 22), 'FRUSEN'), lab(tt, tt + 1.4, (28, 22), 'TINAD'), lab(8.6, 12.0, (30, 88), 'FRUSEN')])
_g['_ball_last'] = _bl

if __name__ == '__main__': render(C, sys.argv)
