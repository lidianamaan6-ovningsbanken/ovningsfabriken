# Omgång 1: tolv av Sams egna övningar.
from render_avslut_base import *
import math as _m

C.clear()
makebase_orig = makebase
Y_ = '#ffd65a'  # gul markering

def shapes_base(label, shapes):
    def mk(c):
        c = dict(c); c['goals'] = []
        im = makebase_orig(c); d = ImageDraw.Draw(im)
        d.rectangle((760, 20, 1050, 60), fill='#0a1e17')
        d.text((1040, 44), label, font=F(19, True), fill='#adc5b6', anchor='rm')
        for s in shapes:
            k = s[0]
            if k == 'zone':
                _, x1, y1, x2, y2, col, txt = s
                a = xy((x1, y1)); b = xy((x2, y2))
                ov = Image.new('RGBA', im.size, (0, 0, 0, 0)); od = ImageDraw.Draw(ov)
                od.rectangle((*a, *b), fill=col + (70,), outline=col + (200,), width=3); im.paste(ov, (0, 0), ov)
                d = ImageDraw.Draw(im)
                if txt: d.text((b[0] - 10, a[1] + 16), txt, font=F(15, True), fill='#e4ecd6', anchor='rm')
            elif k == 'box':
                _, x1, y1, x2, y2 = s; a = xy((x1, y1)); b = xy((x2, y2))
                d.rounded_rectangle((*a, *b), radius=9, outline='#e4ecd6', width=4)
            elif k == 'ring':  # ring av koner
                _, cx, cy, r, n = s
                for i in range(n):
                    v = 2 * _m.pi * i / n; xx, yy = xy((cx + r * _m.cos(v), cy + r * _m.sin(v) * 770 / 650 * 0.85))
                    d.polygon([(xx, yy - 7), (xx - 6, yy + 5), (xx + 6, yy + 5)], fill='#ff965b')
            elif k == 'circle':
                _, cx, cy, r = s; x, y = xy((cx, cy)); rx = 7.7 * r; ry = 6.5 * r * 770 / 650 * 0.85
                d.ellipse((x - rx, y - ry, x + rx, y + ry), outline='#b2cdb1', width=3)
            elif k == 'smallgoal':
                _, x, y = s; cx, cy = xy((x, y)); d.rectangle((cx - 17, cy - 10, cx + 17, cy + 10), outline='#eef4d9', width=3)
            elif k == 'cone':
                _, x, y = s; xx, yy = xy((x, y)); d.polygon([(xx, yy - 8), (xx - 7, yy + 6), (xx + 7, yy + 6)], fill='#ff965b')
            elif k == 'yellowcone':
                _, x, y = s; xx, yy = xy((x, y)); d.polygon([(xx, yy - 8), (xx - 7, yy + 6), (xx + 7, yy + 6)], fill=Y_)
            elif k == 'pole':
                _, x, y = s; xx, yy = xy((x, y)); d.line((xx, yy - 22, xx, yy + 6), fill='#ffd65a', width=5); d.ellipse((xx - 5, yy + 3, xx + 5, yy + 9), fill='#b98d1d')
            elif k == 'text':
                _, x, y, txt = s; d.text(xy((x, y)), txt, font=F(16, True), fill='#e4ecd6', anchor='mm')
        return im
    return mk

def follow(track, dx=2.2, dy=1.6):
    return [(t, (x + dx, y + dy)) for t, (x, y) in track]

def ring_pos(cx, cy, r, i, n, a0=-90):
    v = _m.radians(a0 + 360 * i / n); return (cx + r * _m.cos(v), cy + r * _m.sin(v) * 0.85 * 770 / 650)

def chain(*pts):
    """Boll som passas mellan punkter: (t, pos) där bollen ligger kvar en stund vid varje mottagare."""
    out = []
    for t, pos in pts:
        out.append((t, pos))
    return out

# ============ t01 Svansjage ============
paths = [
    [(0, (20, 25)), (4, (38, 32)), (8, (30, 55)), (12, (45, 70)), (18, (25, 78))],
    [(0, (50, 22)), (4, (64, 36)), (8, (78, 28)), (12, (70, 50)), (18, (58, 62))],
    [(0, (80, 24)), (4, (70, 46)), (6, (55, 52)), (7, (49, 55)), (10, (40, 40)), (14, (60, 32)), (18, (78, 40))],
    [(0, (22, 50)), (4, (18, 66)), (8, (32, 78)), (12, (20, 60)), (18, (34, 46))],
    [(0, (50, 50)), (4, (52, 56)), (6, (50, 57)), (7, (52, 60)), (10, (66, 70)), (14, (80, 76)), (18, (66, 80))],
    [(0, (78, 52)), (4, (84, 70)), (8, (66, 80)), (12, (54, 80)), (18, (42, 66))],
    [(0, (34, 78)), (4, (44, 66)), (8, (58, 72)), (12, (78, 64)), (18, (82, 26))],
    [(0, (64, 76)), (4, (80, 80)), (8, (84, 50)), (12, (62, 24)), (18, (40, 22))],
]
pl = [p(str(i + 1), (B if i % 2 == 0 else R), *paths[i]) for i in range(8)]
add('t01', 'svansjage', ['Svansjage', 'Lek med boll'], 'Ruta med koner · Alla har en boll · Västen nedstoppad som svans', pl, follow(paths[0]),
    [(0, 'Alla dribblar fritt i rutan', 'Varje spelare har en boll och en väst nedstoppad som svans.'),
     (3.5, 'Lyft blicken', 'Se var de andra är och håll bollen nära foten.'),
     (6, 'Ta en svans', 'Nr 3 tar svansen från nr 5 utan att tappa sin egen boll.'),
     (10, 'Skydda bollen och svansen', 'Ställ kroppen mellan motspelaren och din svans.'),
     (14, 'Flest svansar efter 60 sekunder vinner', 'Svansen du tar stoppar du i fickan.')])
C[-1]['balls'] = [follow(x) for x in paths]
C[-1]['shapes'] = shapes_base('LEK MED BOLL', [('box', 12, 14, 88, 86)])

# ============ t02 Snurra flaskan ============
cones2 = [(15, 15), (85, 15), (15, 85), (85, 85), (50, 15), (50, 85), (15, 50), (85, 50)]
pl = []
for i in range(8):
    st = ring_pos(50, 50, 13, i, 8)
    if i == 3:  # nr 4 tar bollen och dribblar runt hörnkon
        tr = [(0, st), (3, st), (3.6, (50, 52)), (6.5, (82, 82)), (7.3, (88, 88)), (8, (84, 80)), (11, st)]
    else:
        own = {0: (50, 15), 1: (85, 15), 2: (85, 50), 4: (50, 85), 5: (15, 85), 6: (15, 50), 7: (15, 15)}
        tgt = own[i]
        late = 1.6 if i == 6 else 0
        tr = [(0, st), (3.8 + late * .4, st), (6.5 + late, (tgt[0] * 1.08 - 4, tgt[1] * 1.08 - 4) if False else tgt), (7.2 + late, (tgt[0] + (2 if tgt[0] > 50 else -2), tgt[1] + (2 if tgt[1] > 50 else -2))), (10.5 + late * 1.2, st)]
    pl.append(p(str(i + 1), B, *tr))
pl.append(fixed('T', G, (50, 50)))
add('t02', 'snurra-flaskan', ['Snurra flaskan', 'Lek och reaktion'], 'Ring i mitten · Koner i hörnen och på sidorna', pl,
    [(0, (52, 50)), (3, (52, 50)), (3.6, (52, 54)), (6.5, (84, 84)), (7.3, (90, 90)), (8, (86, 82)), (11, ring_pos(50, 50, 13, 3, 8)), (18, ring_pos(50, 50, 13, 3, 8))],
    [(0, 'Alla står i ringen', 'Tränaren snurrar en flaska eller en boll i mitten.'),
     (3, 'Flaskan pekar på nr 4', 'Nr 4 tar bollen och dribblar runt valfri hörnkon.'),
     (4, 'Alla andra sprintar runt närmaste kon', 'Reagera snabbt och gör en kort sväng runt konen.'),
     (9, 'Tillbaka till ringen', 'Nr 4 tar första touchen framåt hela vägen hem.'),
     (12.5, 'Sist tillbaka snurrar nästa gång', 'Nr 7 kom sist och får snurra flaskan.')])
C[-1]['shapes'] = shapes_base('LEK OCH REAKTION', [('cone', x, y) for x, y in cones2])

# ============ t03 Bollstafett + tre i rad ============
def lineup(x, col, runner_t0):
    ys = [50, 57, 64, 71, 78]
    out = []
    for i, y in enumerate(ys):
        if i == 4:  # sista spelaren
            out.append(p(str(i + 1), col, (0, (x, y)), (runner_t0, (x, y)), (runner_t0 + 2.4, (x, 30)), (runner_t0 + 3, (x + 2, 27)), (runner_t0 + 5.4, (x, 50)), (18, (x, 50))))
        else:
            out.append(p(str(i + 1), col, (0, (x, y)), (runner_t0 + 3.6, (x, y)), (runner_t0 + 5, (x, y + 7)), (18, (x, y + 7))))
    return out
def relay_ball(x, t0):
    return [(0, (x, 48)), (0.6, (x, 48)), (1.4, (x, 55)), (2.2, (x, 62)), (3, (x, 69)), (t0 - 0.2, (x, 76)), (t0 + 6.2, (x, 76)), (t0 + 6.6, (x, 48)), (t0 + 7.4, (x, 55)), (t0 + 8.2, (x, 62)), (t0 + 9, (x, 69)), (18, (x, 76))]
pl = lineup(30, B, 4.6) + lineup(70, R, 5.2)
brick = [('cone', x0 + dx, dy) for x0 in (24, 64) for dx in (0, 6, 12) for dy in (12, 18, 24)]
add('t03', 'bollstafett-tre-i-rad', ['Bollstafett', 'Tre i rad'], 'Två lag på led · Varsin bricka med 3 × 3 koner', pl, relay_ball(30, 4.6),
    [(0, 'Två lag på led', 'Bollen skickas bakåt, över huvudet och mellan benen.'),
     (4.6, 'Sista spelaren sprintar till brickan', 'Lägg västen på en kon. Tänk innan du lägger den.'),
     (7.6, 'Spring tillbaka och ställ dig först', 'Leden flyttar ett steg bakåt.'),
     (11, 'Bollen skickas bakåt igen', 'Samarbete i leden ger fart.'),
     (14.5, 'Först med tre i rad vinner', 'Lagen turas om tills någon har tre västar i rad.')])
C[-1]['balls'] = [relay_ball(30, 4.6), relay_ball(70, 5.2)]
C[-1]['shapes'] = shapes_base('LEK OCH STAFETT', brick)

# ============ t04 Kull + sprint ============
pl = []
for i, y in enumerate([30, 40, 50, 60, 70]):
    caught = i in (1, 3)
    pl.append(p(str(i + 1), B, (0, (45, y)), (3.2, (45, y)), (6.4 + (0.6 if caught else 0), ((22 if caught else 13), y + (2 if caught else 0))), (10.5, ((22 if caught else 13), y)), (12, (45, y)), (13.6, (45, y)), (16.5, (56 + i * 3, y)), (18, (60 + i * 3, y))))
    tgt = (24, y + 1) if caught else (24, y)
    pl.append(p(str(i + 1), R, (0, (55, y)), (3.5, (55, y)), (6.8, tgt), (10.5, tgt), (12, (55, y)), (13.3, (55, y)), (16.8, (85, y)), (18, (86, y))))
pl.append(fixed('T', G, (50, 88)))
cones4 = [('cone', 10, y) for y in range(24, 80, 8)] + [('yellowcone', 90, y) for y in range(24, 80, 8)]
add('t04', 'kull-och-sprint', ['Kull + sprint', 'Lek och reaktion'], 'Två lag på led · Vänster konlinje för blått · Höger för rött', pl,
    [(0, (50, 84)), (18, (50, 84))],
    [(0, 'Två lag på led bredvid varandra', 'Blått hör till vänster konlinje och rött till höger.'),
     (3, 'Tränaren ger signal till blått', 'Blått sprintar hem till sin linje.'),
     (3.6, 'Rött jagar och försöker kulla', 'Explosiv första meter. Vänd snabbt åt rätt håll.'),
     (7, 'En poäng per kullad spelare', 'Rött hann kulla två blå spelare.'),
     (13.3, 'Ny signal: nu springer rött hem', 'Reagera på signalen. Blått jagar.')])
C[-1]['shapes'] = shapes_base('LEK OCH REAKTION', cones4)

# ============ t05 Tappa inte bollen ============
def group(cx, col, path, n=4, lab='12345'):
    out = []
    for i in range(n):
        dx, dy = 5 * _m.cos(2 * _m.pi * i / n), 4 * _m.sin(2 * _m.pi * i / n)
        out.append(p(lab[i], col, *[(t, (x + dx, y + dy)) for t, (x, y) in path]))
    return out
pA = [(0, (30, 76)), (1, (30, 76)), (8.5, (30, 26)), (10, (30, 24)), (17, (30, 74)), (18, (30, 76))]
pB = [(0, (70, 76)), (1, (70, 76)), (7, (70, 44)), (7.6, (70, 44)), (9.6, (70, 76)), (11, (70, 76)), (18, (70, 58))]
def juggle(path, n, t_end=18, drop=None):
    out = []; t = 0; i = 0
    while t <= t_end:
        x, y = at(path, t); a = 2 * _m.pi * (i % n) / n
        out.append((t, (x + 3.6 * _m.cos(a), y + 2.8 * _m.sin(a))))
        if drop and drop[0] <= t < drop[1]:
            out.append((drop[0] + 0.3, (x + 6, y + 4))); t = drop[1]; continue
        t = round(t + 0.6, 2); i += 1
    return out
add('t05', 'tappa-inte-bollen', ['Tappa inte bollen', 'Teknik och samarbete'], 'Två grupper i varsin tät ring · En kon längre bort',
    group(30, B, pA) + group(70, R, pB), juggle(pA, 4),
    [(0, 'Håll bollen i luften tillsammans', 'Fötter, lår och huvud. Bollen får inte nudda marken.'),
     (2, 'Ta små steg framåt tillsammans', 'Mjuka tillslag gör bollen lätt att ta emot.'),
     (7.2, 'Rött tappar bollen', 'Då börjar gruppen om från starten.'),
     (10, 'Blått vänder vid konen', 'Prata med varandra hela vägen.'),
     (15, 'Först tillbaka vinner', 'Byt grupper och kör igen.')])
C[-1]['balls'] = [juggle(pA, 4), juggle(pB, 4, drop=(7.2, 11))]
C[-1]['shapes'] = shapes_base('TEKNIK OCH SAMARBETE', [('cone', 30, 18), ('cone', 70, 18), ('text', 30, 90, 'START'), ('text', 70, 90, 'START')])

# ============ t08 Huvud, axlar, knä och tå ============
pl = []; balls = []
for j, y in enumerate([24, 41, 58, 75]):
    wA = j % 2 == 0
    pl.append(p('A', B, (0, (38, y)), (6.8, (38, y)), (7.5, (46 if wA else 44, y)), (9.5, (40, y)), (12.8, (38, y)), (13.5, (44 if not wA else 45, y)), (15, (39, y)), (18, (38, y))))
    pl.append(p('B', R, (0, (62, y)), (6.8, (62, y)), (7.5, (56 if wA else 54, y)), (9.5, (60, y)), (12.8, (62, y)), (13.5, (55 if not wA else 56, y)), (15, (61, y)), (18, (62, y))))
    side = 41 if wA else 59; side2 = 59 if wA else 41
    balls.append([(0, (50, y)), (7.4, (50, y)), (8, (side, y)), (10.5, (side, y)), (11.2, (50, y)), (13.4, (50, y)), (14, (side2, y)), (16, (side2, y)), (16.8, (50, y))])
pl.append(fixed('T', G, (50, 91)))
add('t08', 'huvud-axlar-kna-och-ta', ['Huvud, axlar, knä och tå', 'Lek och reaktion'], 'Spelarna i par mittemot varandra · En boll på en kon emellan', pl, balls[0],
    [(0, 'Paren står mittemot varandra', 'En boll ligger på en kon mellan er.'),
     (2, 'Tränaren ropar kroppsdelar', 'Huvud, axlar, knä och tå. Ta på rätt kroppsdel.'),
     (7, '”Boll!” Ta bollen först', 'Snabba fötter och låg tyngdpunkt när du startar.'),
     (9, 'Den som vinner får en poäng', 'Lägg tillbaka bollen på konen.'),
     (12.5, 'Ny runda', 'Lyssna noga. Tränaren kan försöka lura er.')])
C[-1]['balls'] = balls
C[-1]['shapes'] = shapes_base('LEK OCH REAKTION', [('yellowcone', 50, y + 2.2) for y in [24, 41, 58, 75]])

# ============ t09 Dribbla genom zonerna ============
r1 = [(0, (42, 90)), (1, (42, 88)), (3, (44, 74)), (3.8, (36, 68)), (4.6, (34, 60)), (6, (52, 50)), (6.8, (62, 44)), (8, (60, 30)), (9, (58, 22)), (18, (58, 22))]
r2 = [(0, (60, 92)), (8.5, (60, 92)), (9.5, (60, 84)), (11.5, (58, 70)), (12.5, (66, 64)), (14, (60, 50)), (15, (57, 47)), (18, (57, 50))]
d1 = [(0, (50, 70)), (3, (46, 72)), (4, (40, 68)), (5, (44, 66)), (11, (56, 70)), (12.3, (62, 66)), (18, (54, 70))]
d2 = [(0, (50, 45)), (6, (56, 46)), (7, (60, 42)), (13, (56, 48)), (14.6, (58, 48)), (18, (54, 46))]
add('t09', 'dribbla-genom-zonerna', ['Dribbla genom zonerna', 'Duell 1 mot 1'], 'Tre zoner i rad · Startruta med bollar · En försvarare per zon',
    [p('1', R, *r1), p('2', R, *r2), fixed('3', R, (34, 90)), fixed('4', R, (26, 90)), p('1', B, *d1), p('2', B, *d2)],
    follow(r1, 0, -3),
    [(0, 'Rött dribblar ut från startrutan', 'Blå försvarare väntar i den blå och den grå zonen.'),
     (2.5, 'Hög fart in i ytan', 'Försvararen får bara vara i sin egen zon.'),
     (4, 'Finta och byt riktning', 'Utnyttja ytan där försvararen inte är.'),
     (8.5, 'Hela vägen till grön zon ger en poäng', 'Nästa spelare startar från startrutan.'),
     (14.6, 'Försvararen vinner bollen', 'Byt roller efter två minuter.')])
C[-1]['balls'] = [follow(r1, 0, -3), [(t, (x, y - 3)) for t, (x, y) in r2[:-2]] + [(14.6, (58, 45)), (18, (54, 43))]]
C[-1]['shapes'] = shapes_base('KONTRING', [('zone', 4, 8, 96, 32, (80, 200, 120), 'GRÖN ZON'), ('zone', 4, 34, 96, 56, (150, 160, 155), 'GRÅ ZON'), ('zone', 4, 58, 96, 80, (60, 150, 220), 'BLÅ ZON'), ('box', 20, 83, 80, 97)])

# ============ t10 Spanska cirkeln ============
walls = [fixed('V', G, ring_pos(50, 50, 45, i, 8, -67.5)) for i in range(8)]
d1 = [(0, (30, 36)), (2, (24, 50)), (4, (28, 62)), (5.2, (32, 66)), (6.2, (40, 74)), (9, (60, 76)), (13, (74, 60)), (18, (70, 38))]
d2 = [(0, (70, 36)), (4, (74, 46)), (8, (72, 62)), (10.8, (64, 70)), (11.4, (62, 72)), (13, (56, 66)), (18, (50, 66))]
d3 = [(0, (50, 22)), (6, (66, 26)), (12, (34, 28)), (18, (26, 46))]
d4 = [(0, (48, 78)), (6, (30, 72)), (12, (26, 52)), (18, (34, 30))]
f1 = [(0, (47, 50)), (3, (47, 50)), (4.6, (34, 60)), (6, (34, 64)), (9, (46, 54)), (18, (48, 52))]
f2 = [(0, (53, 50)), (8, (53, 50)), (10.6, (63, 66)), (11.4, (62, 70)), (12.6, (54, 62)), (18, (52, 50))]
b1 = follow(d1[:3]) + [(4.6, (30, 63)), (5.1, ring_pos(50, 50, 45, 4, 8, -67.5)), (5.6, ring_pos(50, 50, 45, 4, 8, -67.5)), (6.3, (41, 75))] + follow(d1[5:])
add('t10', 'spanska-cirkeln', ['Spanska cirkeln', 'Positionsspel'], 'Ring av koner · Väggspelare runt om · Försvarare i mittcirkeln',
    [p('1', R, *d1), p('2', R, *d2), p('3', R, *d3), p('4', R, *d4), p('1', B, *f1), p('2', B, *f2)] + walls, b1,
    [(0, 'Rött dribblar i ringen', 'Blå försvarare väntar i mittcirkeln.'),
     (3, 'Blått kliver ut och pressar', 'Se pressen komma innan den är där.'),
     (4.6, 'Spela väggen tidigt', 'Väggspelaren gör sig spelbar med vinkel och spelar tillbaka direkt.'),
     (6.3, 'Förbi pressen', 'Ta med bollen vidare i ringen.'),
     (11.4, 'Blått vinner bollen', 'Då byter blå och röd spelare roll.')])
C[-1]['balls'] = [b1, follow(d2[:4]) + [(11.4, (62, 72)), (18, (52, 52))], follow(d3), follow(d4)]
C[-1]['shapes'] = shapes_base('POSITIONSSPEL', [('ring', 50, 50, 38, 20), ('circle', 50, 50, 11)])

# ============ t12 Rondo i stor cirkel ============
N = 12; pos = [ring_pos(50, 50, 38, i, N) for i in range(N)]
seq = [0, 4, 7, 2, 9, 5, 11, 6, 1, 8]
bt = []; t = 0
for k, i in enumerate(seq):
    bt += [(t, pos[i]), (t + 0.5, pos[i])]; t += 1.35
bt += [(t, ((pos[8][0] + pos[3][0]) / 2, (pos[8][1] + pos[3][1]) / 2)), (18, (50, 58))]
chasers = [p('1', R, (0, (42, 42)), (6, (40, 36)), (12, (54, 46)), (13.6, (50, 56)), (18, (50, 58))),
           p('2', R, (0, (58, 42)), (6, (62, 46)), (12, (46, 40)), (18, (46, 44))),
           p('3', R, (0, (42, 58)), (6, (48, 62)), (12, (40, 56)), (18, (40, 60))),
           p('4', R, (0, (58, 58)), (6, (54, 54)), (12, (60, 58)), (18, (60, 52)))]
add('t12', 'rondo-i-stor-cirkel', ['Rondo i stor cirkel', '12 mot 4'], '12 spelare runt cirkeln · 4 jagare i mitten · Max två touch',
    [fixed(str(i + 1), B, pos[i]) for i in range(N)] + chasers, bt,
    [(0, 'Blått håller bollen runt cirkeln', 'Max två touch. Fyra röda jagar i mitten.'),
     (2.7, 'Passa förbi jagarna', 'Sök passningen genom ringen när den är öppen.'),
     (6.8, 'Var redo innan bollen kommer', 'Öppen kropp och lätta fötter.'),
     (12.5, 'Jagarna jobbar ihop och stänger', 'Rött bryter passningen.'),
     (14, 'Den som bryter byter plats', 'Tio passningar i rad ger en poäng.')])
C[-1]['shapes'] = shapes_base('RONDO', [('circle', 50, 50, 38)])

# ============ t14 4 mot 2 till 6 mot 4 ============
inB = [[(0, (32, 32)), (3, (34, 36)), (7, (30, 34)), (8.5, (40, 42)), (18, (42, 46))],
       [(0, (68, 32)), (3, (66, 30)), (7, (70, 36)), (8.5, (58, 42)), (18, (56, 44))],
       [(0, (68, 68)), (3, (70, 66)), (7, (66, 68)), (8.5, (60, 56)), (18, (58, 58))],
       [(0, (32, 68)), (3, (30, 64)), (7, (34, 70)), (8.5, (42, 58)), (18, (44, 56))]]
inR = [[(0, (46, 46)), (3, (54, 40)), (6.5, (40, 58)), (7.5, (36, 64)), (9, (32, 60)), (18, (30, 50))],
       [(0, (54, 54)), (3, (48, 56)), (6.5, (60, 64)), (9, (66, 62)), (18, (70, 54))]]
outR = [(50, 18), (82, 50), (50, 82), (18, 50)]
outR_in = [(50, 30), (70, 50), (50, 70), (30, 50)]
pl = [p(str(i + 1), B, *inB[i]) for i in range(4)] + [p(str(i + 1), R, *inR[i]) for i in range(2)] + [p(str(i + 3), R, (0, outR[i]), (7.6, outR[i]), (9.2, outR_in[i]), (18, outR_in[i])) for i in range(4)]
ball = [(0, (32, 32)), (0.8, (32, 32)), (1.5, (68, 32)), (2.3, (66, 31)), (3, (69, 66)), (3.8, (70, 66)), (4.5, (32, 66)), (5.3, (30, 64)), (6, (34, 70)), (6.7, (34, 70)), (7.5, (37, 63)),
        (9.3, (32, 60)), (10.2, (50, 31)), (11, (50, 31)), (11.9, (70, 50)), (12.8, (69, 51)), (13.7, (50, 70)), (14.6, (50, 69)), (15.5, (30, 50)), (16.4, (30, 51)), (17.3, (50, 31)), (18, (50, 31))]
add('t14', '4-mot-2-till-6-mot-4-presspel', ['4 mot 2 till 6 mot 4', 'Presspel'], 'Kvadrat · Fyra blå och två röda inne · Fyra röda utanför', pl, ball,
    [(0, 'Fyra blå håller bollen mot två röda', 'Fyra röda väntar utanför kvadraten.'),
     (2.5, 'Blått: ta vinklar och spela snabbt', 'Hela tiden två passningsvägar.'),
     (7.5, 'Rött vinner bollen', 'Nu blir det sex röda mot fyra blå.'),
     (8.5, 'Röda utanför gör planen stor direkt', 'Blått pressar direkt efter bollförlusten.'),
     (13, 'Byt varje gång bollen byter lag', 'Pressa direkt när bollen vinns eller tappas.')])
C[-1]['shapes'] = shapes_base('ÅTERERÖVRING', [('box', 24, 24, 76, 76)])

# ============ t15 Kvadrat med 2 jagare och 1 joker ============
pl = [p('1', R, (0, (24, 50)), (4, (24, 44)), (8, (24, 54)), (18, (24, 50))),
      p('2', R, (0, (50, 24)), (4, (56, 24)), (9, (44, 24)), (18, (50, 24))),
      p('3', R, (0, (76, 50)), (5, (76, 56)), (10, (76, 46)), (18, (76, 50))),
      p('J', G, (0, (50, 50)), (2, (50, 54)), (6, (46, 48)), (11, (52, 46)), (18, (50, 50))),
      p('1', B, (0, (40, 40)), (2, (38, 46)), (4, (46, 34)), (7, (60, 44)), (10.5, (62, 36)), (11.5, (62, 32)), (13, (70, 36)), (18, (72, 46))),
      p('2', B, (0, (60, 60)), (3, (56, 56)), (6, (62, 50)), (9, (56, 40)), (11.5, (64, 40)), (13.2, (63, 30)), (18, (58, 30)))]
ball = [(0, (24, 50)), (0.8, (24, 50)), (1.6, (50, 52)), (2.2, (50, 54)), (3, (56, 24)), (3.6, (56, 24)), (4.5, (76, 55)), (5.2, (76, 56)), (6, (46, 48)), (6.6, (46, 48)), (7.5, (24, 53)), (8.2, (24, 54)),
        (9, (44, 24)), (9.6, (44, 24)), (10.5, (76, 47)), (11, (76, 47)), (11.6, (64, 37)), (12.2, (63, 35)), (13.2, (63, 31)), (18, (60, 32))]
add('t15', 'kvadrat-med-2-jagare-och-1-joker', ['Kvadrat med två jagare', 'Och en joker'], 'Kvadrat · Tre röda på sidorna · Joker och två jagare i mitten', pl, ball,
    [(0, 'Rött passar runt kvadraten', 'Jokern i mitten spelar med laget som har bollen.'),
     (1.6, 'Använd jokern för att spela igenom', 'Max två touch.'),
     (4.5, 'Rör dig längs linjen', 'Ny vinkel ger en ny passningsväg.'),
     (8.2, 'Fem passningar ger en poäng', 'Fortsätt räkna mot nästa poäng.'),
     (11.6, 'Jagaren bryter passningen', 'Den som tappade bollen byter med jagaren.')])
C[-1]['shapes'] = shapes_base('RONDO', [('box', 24, 24, 76, 76)])

# ============ t16 Passningsvariant med fem stationer ============
S5 = {1: (20, 86), 2: (50, 62), 3: (18, 36), 4: (82, 20), 5: (82, 80)}
def st(n, back=False):
    x, y = S5[n]; return (x, y + 6) if back else (x, y)
route = [1, 2, 3, 4, 2, 5, 1]
def cycle(t0):
    b = []; t = t0
    for k in range(len(route) - 1):
        a, c = route[k], route[k + 1]
        lng = (a, c) in [(3, 4), (5, 1)]
        b += [(t, st(a)), (t + 0.5, st(a))]; t += 0.5 + (1.6 if lng else 1.0)
    b.append((t, st(1)))
    return b, t
b1, tend = cycle(0); b2, _ = cycle(4.6)
pl = []
for n in S5:
    nxt = route[route.index(n) + 1] if n != 1 else 2
    pl.append(p(str(n), B, (0, st(n)), (1 + n, st(n)), (3 + n, st(nxt, True)), (18, st(nxt, True))))
    pl.append(p(str(n), B, (0, st(n, True)), (1.5 + n, st(n, True)), (2.5 + n, st(n)), (18, st(n))))
add('t16', 'passningsvariant-med-fem-stationer', ['Passningsvariant', 'Fem stationer'], 'Fem stationer med käppar · Två spelare vid varje · 1, 2, 3, 4, 2, 5, 1', pl, b1,
    [(0, 'A: 1 till 2, B: 2 till 3', 'Rör dig runt käppen innan mottagningen.'),
     (3, 'C: 3 spelar långt till 4', 'Ta emot med bortre foten.'),
     (4.6, 'Ny boll startar när förra är vid 3', 'Två bollar i spel samtidigt.'),
     (6.5, 'D: 4 till 2, E: 2 till 5', 'Spring efter din passning till nästa station.'),
     (9.5, 'F: 5 långt tillbaka till 1', 'Håll tempot. Byt riktning efter några minuter.')])
C[-1]['balls'] = [b1, b2]
C[-1]['shapes'] = shapes_base('SPELUPPBYGGNAD', [('pole', x + 4, y - 4) for x, y in S5.values()] + [('text', x, y + 11, str(n)) for n, (x, y) in S5.items()])

if __name__ == '__main__':
    for c in C:
        if len(sys.argv) > 1 and c['id'] not in sys.argv[1:]: continue
        c['base'] = c['shapes'](c)
        for t in [1, 4, 7.5, 11, 14.5]: frame(c, t).resize((360, 360)).save(ROOT / f"filmwork/{c['id']}-{t}.jpg")
        path = OUT / (c['slug'] + '.mp4')
        proc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', '1080x1080', '-r', '30', '-i', '-', '-an', '-c:v', 'libx264', '-threads', '4', '-preset', 'fast', '-crf', '17', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', str(path)], stdin=subprocess.PIPE)
        for f in range(c['seconds'] * 30): proc.stdin.write(frame(c, f / 30).tobytes())
        proc.stdin.close(); assert proc.wait() == 0
        print(c['id'], path.name, flush=True)
