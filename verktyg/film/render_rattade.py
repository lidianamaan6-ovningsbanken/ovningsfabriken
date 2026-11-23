# Rättade filmer: följer instruktionerna rad för rad (färger, svansar, flaska,
# västar, tränarsignal, platsbyten och spring efter passningen).
from film_hjalp import *
import math as _m

C.clear()

# ============ t01 Svansjage ============
# "Alla spelare har en boll och en väst instoppad som svans. Tar du en svans stoppar du den i fickan."
paths = [
    [(0, (20, 25)), (4, (38, 32)), (8, (30, 55)), (12, (45, 70)), (18, (25, 78))],
    [(0, (50, 22)), (4, (64, 36)), (8, (78, 28)), (12, (70, 50)), (18, (58, 62))],
    [(0, (80, 24)), (4, (70, 46)), (6, (55, 52)), (7, (50, 56)), (10, (40, 40)), (14, (60, 32)), (18, (78, 40))],
    [(0, (22, 50)), (4, (18, 66)), (8, (32, 78)), (12, (20, 60)), (18, (34, 46))],
    [(0, (50, 50)), (4, (52, 56)), (6, (50, 58)), (7, (53, 61)), (10, (66, 70)), (14, (80, 76)), (18, (66, 80))],
    [(0, (78, 52)), (4, (84, 70)), (8, (66, 80)), (12, (54, 80)), (18, (42, 66))],
    [(0, (34, 78)), (4, (44, 66)), (8, (58, 72)), (12, (78, 64)), (18, (82, 26))],
    [(0, (64, 76)), (4, (80, 80)), (8, (84, 50)), (12, (62, 24)), (18, (40, 22))],
]
pl = [p(str(i + 1), B, *paths[i]) for i in range(8)]
for i, q in enumerate(pl):
    q['tails'] = (lambda t: 0 if t >= 6.6 else 1) if i == 4 else (lambda t: 1)
add('t01', 'svansjage', ['Svansjage', 'Lek med boll'], 'Ruta med koner · Alla har en boll och en väst som svans', pl, follow(paths[0]),
    [(0, 'Alla dribblar fritt i rutan', 'Alla har en boll och en väst nedstoppad i byxlinningen som svans.'),
     (3.5, 'Försök ta andras svansar', 'Utan att tappa din egen boll.'),
     (6.6, 'Nr 3 tar svansen från nr 5', 'Tar du en svans stoppar du den i fickan.'),
     (10, 'Skydda bollen och svansen med kroppen', 'Bollen nära foten. Lyft blicken och se var de andra är.'),
     (14, 'Flest svansar efter 60 sekunder vinner', 'Räkna svansarna i fickan när tiden är slut.')])
C[-1]['balls'] = [follow(x) for x in paths]
C[-1]['extras'] = [dict(kind='label', t0=6.6, t1=9.5, pos=(51, 49), text='+1')]
C[-1]['shapes'] = shapes_base('LEK MED BOLL', [('box', 12, 14, 88, 86)])
C[-1]['extras'][0]['pos'] = (50, 47)

# ============ t02 Snurra flaskan ============
# "Tränaren snurrar en flaska i mitten av ringen. Den som flaskan pekar på tar bollen och dribblar runt
#  valfri hörnkon och tillbaka. Alla andra sprintar runt närmaste kon. Den som är sist tillbaka får snurra nästa gång."
cones2 = [(15, 15), (85, 15), (15, 85), (85, 85), (50, 15), (50, 85), (15, 50), (85, 50)]
pl = []; used = {}
for i in range(8):
    st = ring_pos(50, 50, 15, i, 8)
    if i == 3:
        tr = [(0, st), (3.2, st), (3.8, (54, 54)), (6.6, (80, 80)), (7.2, (86, 81)), (7.7, (88, 86)), (8.2, (83, 88)), (11, st), (18, st)]
    else:
        cx, cy = min(cones2, key=lambda c: (c[0] - st[0]) ** 2 + (c[1] - st[1]) ** 2)
        k = used.get((cx, cy), 0); used[(cx, cy)] = k + 1
        late = 1.8 if i == 6 else 0; s0 = 3.6 + 0.35 * k
        ox, oy = (cx - 50) / 35 * 4, (cy - 50) / 35 * 4  # runt baksidan av konen
        side = (cy - 50) / 35 * 4, -(cx - 50) / 35 * 4
        tr = [(0, st), (s0, st), (s0 + 2.4 + late, (cx - ox + side[0] * (1 if k == 0 else -1), cy - oy + side[1] * (1 if k == 0 else -1))),
              (s0 + 3 + late, (cx + ox, cy + oy)), (s0 + 3.6 + late, (cx - ox - side[0] * (1 if k == 0 else -1), cy - oy - side[1] * (1 if k == 0 else -1))),
              (s0 + 6.6 + late * 1.6, st), (18, st)]
    pl.append(p(str(i + 1), B, *tr))
pl.append(fixed('T', G, (50, 44)))
ang4 = _m.degrees(_m.atan2((ring_pos(50, 50, 15, 3, 8)[1] - 52) * 6.5, (ring_pos(50, 50, 15, 3, 8)[0] - 50) * 7.7))
add('t02', 'snurra-flaskan', ['Snurra flaskan', 'Lek och reaktion'], 'Ring i mitten · Koner i hörnen och på sidorna', pl,
    [(0, (54, 55)), (3.2, (54, 55)), (3.8, (56, 57)), (6.6, (82, 82)), (7.2, (88, 83)), (7.7, (90, 88)), (8.2, (85, 90)), (11, ring_pos(50, 50, 15, 3, 8)), (18, ring_pos(50, 50, 15, 3, 8))],
    [(0, 'Tränaren snurrar flaskan', 'Spelarna står i en ring runt tränaren.'),
     (3, 'Flaskan pekar på nr 4', 'Nr 4 tar bollen och dribblar runt valfri hörnkon.'),
     (3.6, 'Alla andra sprintar runt närmaste kon', 'Reagera snabbt. Kort sväng runt konen.'),
     (8.5, 'Tillbaka till ringen', 'Första touchen framåt hela vägen hem.'),
     (12.5, 'Den som är sist tillbaka snurrar nästa gång', 'Här kom nr 7 sist.')])
C[-1]['extras'] = [dict(kind='flask', t0=0, t1=12.5, pos=(50, 52), ang=lambda t: (t * 260 if t < 2.6 else ang4 + max(0, 3 - t) / 0.4 * 30) if t < 3 else ang4)]
C[-1]['shapes'] = shapes_base('LEK OCH REAKTION', [('cone', x, y) for x, y in cones2])

# ============ t03 Bollstafett + tre i rad ============
# "Bollen skickas bakåt över huvudet och mellan benen. När bollen når sista spelaren sprintar den till brickan
#  och lägger en väst på en kon, och springer tillbaka först i leden. Först med tre i rad vinner."
def lineup(x, col, t0):
    ys = [50, 57, 64, 71, 78]; out = []
    for i, y in enumerate(ys):
        if i == 4:
            out.append(p(str(i + 1), col, (0, (x, y)), (t0, (x, y)), (t0 + 2.4, (x, 30)), (t0 + 3, (x, 28)), (t0 + 5.4, (x, 50)), (18, (x, 50))))
        else:
            out.append(p(str(i + 1), col, (0, (x, y)), (t0 + 3.6, (x, y)), (t0 + 5, (x, y + 7)), (18, (x, y + 7))))
    return out
def relay(x, t0):
    return [(0, (x, 48)), (0.6, (x, 48)), (1.4, (x, 55)), (2.2, (x, 62)), (3, (x, 69)), (t0 - 0.2, (x, 76)), (t0 + 6.2, (x, 76)), (t0 + 6.6, (x, 48)), (t0 + 7.4, (x, 55)), (t0 + 8.2, (x, 62)), (t0 + 9, (x, 69)), (18, (x, 76))]
pl = lineup(30, B, 4.6) + lineup(70, R, 5.2)
brick = [('cone', x0 + dx, dy) for x0 in (24, 64) for dx in (0, 6, 12) for dy in (12, 18, 24)]
add('t03', 'bollstafett-tre-i-rad', ['Bollstafett', 'Tre i rad'], 'Två lag på led · Varsin bricka med 3 × 3 koner', pl, relay(30, 4.6),
    [(0, 'Bollen skickas bakåt i leden', 'Över huvudet och mellan benen.'),
     (4.6, 'Sista spelaren sprintar till brickan', 'Och lägger en väst på en kon. Tänk innan du lägger den.'),
     (7.6, 'Spring tillbaka och ställ dig först i leden', 'Leden flyttar ett steg bakåt.'),
     (11, 'Bollen skickas bakåt igen', 'Samarbete i leden. Nästa sista spelare springer.'),
     (14.5, 'Först med tre i rad vinner', 'Tre västar i rad på brickan, som i tre i rad.')])
C[-1]['balls'] = [relay(30, 4.6), relay(70, 5.2)]
C[-1]['extras'] = [dict(kind='vest', t0=4.6 + 3, pos=(30, 24), color=B), dict(kind='vest', t0=5.2 + 3, pos=(70, 24), color=R)]
C[-1]['shapes'] = shapes_base('LEK OCH STAFETT', brick)

# ============ t04 Kull + sprint ============
# "Svart lag hör till den röda linjen (vänster) och vitt lag till den gula (höger). Tränaren visar en färg.
#  Laget som hör till färgen sprintar hem till sin linje, det andra laget försöker kulla dem. En poäng per kullad spelare."
pl = []
for i, y in enumerate([30, 40, 50, 60, 70]):
    caught = i in (1, 3)
    pl.append(p(str(i + 1), BLACK, (0, (45, y)), (3.2, (45, y)), (6.4 + (0.6 if caught else 0), ((22 if caught else 13), y + (2 if caught else 0))), (10.5, ((22 if caught else 13), y)), (12, (45, y)), (13.6, (45, y)), (16.5, (66 + i * 2, y)), (18, (70 + i * 2, y))))
    tgt = (24, y + 1) if caught else (24, y); caught2 = i == 2
    pl.append(p(str(i + 1), WHITE, (0, (55, y)), (3.5, (55, y)), (6.8, tgt), (10.5, tgt), (12, (55, y)), (13.3, (55, y)), (16.8, ((76 if caught2 else 87), y)), (18, ((76 if caught2 else 87), y))))
pl.append(fixed('T', G, (50, 88)))
add('t04', 'kull-och-sprint', ['Kull + sprint', 'Lek och reaktion'], 'Svart lag: röd linje till vänster · Vitt lag: gul linje till höger', pl,
    [(0, (50, 84)), (18, (50, 84))],
    [(0, 'Två lag på led bredvid varandra', 'Svart lag hör till röd linje, vitt lag till gul linje.'),
     (3, 'Tränaren visar röd färg', 'Svart lag sprintar hem till den röda linjen.'),
     (3.6, 'Vitt lag försöker kulla dem', 'Explosiv första meter. Vänd snabbt åt rätt håll.'),
     (7, 'En poäng per kullad spelare', 'Vitt kullade två svarta spelare.'),
     (13.3, 'Tränaren visar gul färg', 'Nu sprintar vitt hem till gul linje och svart jagar.')])
C[-1]['extras'] = [dict(kind='signal', t0=3, t1=7.5, pos=(50, 88), color='#e5483b'), dict(kind='signal', t0=13.3, t1=17.5, pos=(50, 88), color=YELLOW)]
C[-1]['shapes'] = shapes_base('LEK OCH REAKTION', [('redcone', 10, y) for y in range(24, 80, 8)] + [('yellowcone', 90, y) for y in range(24, 80, 8)])

# ============ t12 Rondo i stor cirkel ============
# "Blå runt cirkeln, röda jagar inne. Max två touch. Bryter en röd byter den plats med den som slog passningen. 10 passningar i rad ger en poäng."
N = 12; pos = [ring_pos(50, 50, 38, i, N) for i in range(N)]
seq = [0, 4, 7, 2, 9, 5, 11, 6, 1, 8]; bt = []; t = 0
for i in seq: bt += [(t, pos[i]), (t + 0.5, pos[i])]; t += 1.35
mid = ((pos[8][0] + pos[3][0]) / 2, (pos[8][1] + pos[3][1]) / 2)
bt += [(t, mid), (15.5, mid), (17, pos[8]), (18, pos[8])]
chasers = [p('1', R, (0, (42, 42)), (6, (40, 36)), (12, (54, 46)), (13.5, mid), (14.3, mid), (16.8, pos[8]), (18, pos[8])),
           p('2', R, (0, (58, 42)), (6, (62, 46)), (12, (46, 40)), (18, (46, 44))),
           p('3', R, (0, (42, 58)), (6, (48, 62)), (12, (40, 56)), (18, (40, 60))),
           p('4', R, (0, (58, 58)), (6, (54, 54)), (12, (60, 58)), (18, (60, 52)))]
blue = [fixed(str(i + 1), B, pos[i]) if i != 8 else p('9', B, (0, pos[8]), (14.3, pos[8]), (16.8, (52, 46)), (18, (52, 46))) for i in range(N)]
add('t12', 'rondo-i-stor-cirkel', ['Rondo i stor cirkel', '12 mot 4'], '12 spelare runt cirkeln · 4 jagare i mitten · Max två touch', blue + chasers, bt,
    [(0, 'Blått håller bollen runt cirkeln', 'Max två touch. Fyra röda jagar inne i cirkeln.'),
     (2.7, 'Passa förbi jagarna', 'Var redo innan bollen kommer.'),
     (8, 'Tio passningar i rad ger en poäng', 'Jagarna jobbar ihop och stänger.'),
     (13.5, 'Rött bryter passningen', 'Den röda som bröt byter plats med nr 9 som slog passningen.'),
     (16, 'Nr 9 blir jagare', 'Spelet fortsätter direkt.')])
C[-1]['shapes'] = shapes_base('RONDO', [('circle', 50, 50, 38)])

# ============ t14 4 mot 2 till 6 mot 4 ============
# "4 gula och 2 röda inne, 4 röda utanför. När röda vinner bollen eller den går ut blir det 6 röda mot 4 gula som jagar."
inY = [[(0, (32, 32)), (3, (34, 36)), (7, (30, 34)), (8.5, (40, 42)), (18, (42, 46))],
       [(0, (68, 32)), (3, (66, 30)), (7, (70, 36)), (8.5, (58, 42)), (18, (56, 44))],
       [(0, (68, 68)), (3, (70, 66)), (7, (66, 68)), (8.5, (60, 56)), (18, (58, 58))],
       [(0, (32, 68)), (3, (30, 64)), (7, (34, 70)), (8.5, (42, 58)), (18, (44, 56))]]
inR = [[(0, (46, 46)), (3, (54, 40)), (6.5, (40, 58)), (7.5, (36, 64)), (9, (32, 60)), (18, (30, 50))],
       [(0, (54, 54)), (3, (48, 56)), (6.5, (60, 64)), (9, (66, 62)), (18, (70, 54))]]
outR = [(50, 18), (82, 50), (50, 82), (18, 50)]; outR_in = [(50, 30), (70, 50), (50, 70), (30, 50)]
pl = [p(str(i + 1), YELLOW, *inY[i]) for i in range(4)] + [p(str(i + 1), R, *inR[i]) for i in range(2)] + [p(str(i + 3), R, (0, outR[i]), (7.6, outR[i]), (9.2, outR_in[i]), (18, outR_in[i])) for i in range(4)]
ball = [(0, (32, 32)), (0.8, (32, 32)), (1.5, (68, 32)), (2.3, (66, 31)), (3, (69, 66)), (3.8, (70, 66)), (4.5, (32, 66)), (5.3, (30, 64)), (6, (34, 70)), (6.7, (34, 70)), (7.5, (37, 63)),
        (9.3, (32, 60)), (10.2, (50, 31)), (11, (50, 31)), (11.9, (70, 50)), (12.8, (69, 51)), (13.7, (50, 70)), (14.6, (50, 69)), (15.5, (30, 50)), (16.4, (30, 51)), (17.3, (50, 31)), (18, (50, 31))]
add('t14', '4-mot-2-till-6-mot-4-presspel', ['4 mot 2 till 6 mot 4', 'Presspel'], 'Kvadrat · Fyra gula och två röda inne · Fyra röda utanför', pl, ball,
    [(0, 'Fyra gula håller bollen mot två röda', 'Fyra röda står utanför kvadraten.'),
     (2.5, 'Gula: ta vinklar och spela snabbt', 'Två röda jagar.'),
     (7.5, 'Rött vinner bollen', 'Nu blir det sex röda mot fyra gula som jagar.'),
     (8.5, 'Röda utanför gör planen stor direkt', 'Gula pressar direkt när bollen tappas.'),
     (13, 'Byt varje gång bollen byter lag', 'Även när bollen går ut ur kvadraten.')])
C[-1]['shapes'] = shapes_base('ÅTERERÖVRING', [('box', 24, 24, 76, 76)])

# ============ t15 Kvadrat med 2 jagare och 1 joker ============
# "3 röda på sidorna, 1 joker och 2 jagare i mitten. Röda och jokern håller bollen. Fem passningar ger en poäng.
#  Den som tappar bollen byter med jagaren som bröt."
pl = [p('1', R, (0, (24, 50)), (4, (24, 44)), (8, (24, 54)), (18, (24, 50))),
      p('2', R, (0, (50, 24)), (4, (56, 24)), (9, (44, 24)), (18, (50, 24))),
      p('3', R, (0, (76, 50)), (5, (76, 56)), (10, (76, 46)), (12.4, (76, 46)), (14.6, (56, 44)), (18, (54, 46))),
      p('J', G, (0, (50, 50)), (2, (50, 54)), (6, (46, 48)), (11, (52, 46)), (18, (50, 52))),
      p('1', B, (0, (40, 40)), (2, (38, 46)), (4, (46, 34)), (7, (60, 44)), (10.5, (62, 38)), (11.5, (62, 37)), (12.4, (63, 37)), (14.6, (76, 50)), (18, (76, 50))),
      p('2', B, (0, (60, 60)), (3, (56, 56)), (6, (62, 50)), (9, (56, 40)), (12, (58, 60)), (18, (44, 58)))]
ball = [(0, (24, 50)), (0.8, (24, 50)), (1.6, (50, 52)), (2.2, (50, 54)), (3, (56, 24)), (3.6, (56, 24)), (4.5, (76, 55)), (5.2, (76, 56)), (6, (46, 48)), (6.6, (46, 48)), (7.5, (24, 53)), (8.2, (24, 54)),
        (9, (44, 24)), (9.6, (44, 24)), (10.5, (76, 47)), (11, (76, 47)), (11.6, (64, 39)), (12.4, (64, 39)), (14.6, (74, 50)), (18, (74, 50))]
add('t15', 'kvadrat-med-2-jagare-och-1-joker', ['Kvadrat med två jagare', 'Och en joker'], 'Kvadrat · Tre röda på sidorna · Joker och två jagare i mitten', pl, ball,
    [(0, 'Rött passar runt kvadraten', 'Jokern i mitten spelar med laget som har bollen.'),
     (1.6, 'Använd jokern för att spela igenom', 'Max två touch.'),
     (4.5, 'Rör dig längs linjen för en ny vinkel', 'Fem passningar ger en poäng.'),
     (11.6, 'Jagaren bryter passningen från nr 3', 'Nr 3 tappade bollen.'),
     (12.6, 'Nr 3 byter med jagaren som bröt', 'Nr 3 blir jagare och jagaren tar platsen på sidan.')])
C[-1]['shapes'] = shapes_base('RONDO', [('box', 24, 24, 76, 76)])

# ============ t16 Passningsvariant med fem stationer ============
# "Bollen går 1, 2, 3, 4, 2, 5 och tillbaka till 1. Spelaren följer sin passning till nästa station. Ny boll startar när förra är vid 3."
S5 = {1: (20, 86), 2: (50, 62), 3: (18, 36), 4: (82, 20), 5: (82, 80)}
def slot(n, k):
    x, y = S5[n]; return (x, y + 6 * k)
route = [1, 2, 3, 4, 2, 5, 1]
def cycle(t0):
    b = []; ev = []; t = t0
    for k in range(len(route) - 1):
        a, c = route[k], route[k + 1]; dur = 1.6 if (a, c) in [(3, 4), (5, 1)] else 1.0
        b += [(t, slot(a, 0)), (t + 0.5, slot(a, 0))]; ev.append((t + 0.5, a, c, dur)); t += 0.5 + dur
    b.append((t, slot(1, 0))); return b, ev
b1, e1 = cycle(0); b2, e2 = cycle(4.6)
queue = {n: [f'{n}a', f'{n}b'] for n in S5}; tracks = {}
for n in S5:
    tracks[f'{n}a'] = [(0, slot(n, 0))]; tracks[f'{n}b'] = [(0, slot(n, 1))]
for tp, a, c, dur in sorted(e1 + e2):
    mover = queue[a].pop(0)
    tracks[mover] += [(tp, slot(a, 0)), (tp + dur + 0.6, slot(c, len(queue[c])))]
    queue[c].append(mover)
    for k, who in enumerate(queue[a]):
        last = tracks[who][-1][1]; tracks[who] += [(max(tp + 0.1, tracks[who][-1][0] + 0.01), last), (tp + 0.7, slot(a, k))]
pl = [p(who[0], B, *sorted(tr, key=lambda z: z[0])) for who, tr in tracks.items()]
add('t16', 'passningsvariant-med-fem-stationer', ['Passningsvariant', 'Fem stationer'], 'Fem stationer med käppar · Bollen går 1, 2, 3, 4, 2, 5, 1', pl, b1,
    [(0, 'A: 1 till 2, B: 2 till 3', 'Spelaren följer sin passning till nästa station.'),
     (3, 'C: 3 spelar långt till 4', 'Rör dig runt käppen innan mottagningen.'),
     (4.6, 'Ny boll startar när förra är vid 3', 'Två bollar i spel samtidigt.'),
     (6, 'D: 4 till 2, E: 2 till 5', 'Ta emot med bortre foten.'),
     (8.5, 'F: 5 spelar långt till 1', 'Spring efter din passning.')])
C[-1]['balls'] = [b1, b2]
C[-1]['seconds'] = 18
C[-1]['shapes'] = shapes_base('SPELUPPBYGGNAD', [('pole', x + 5, y - 3) for x, y in S5.values()] + [('text', x - 6, y - 5, str(n)) for n, (x, y) in S5.items()])

# ============ t20 Bollinnehav 3 mot 1 ============
# "Vita har tre i vänster ruta med en röd jagare. Röda har tre i höger ruta med en vit jagare. Fem passningar ger en poäng,
#  och då slås bollen långt över till andra rutan som startar sitt 3 mot 1. Vinner jagaren bollen byter den plats med den som tappade."
W = WHITE
add('t20', 'bollinnehav-3-mot-1', ['Bollinnehav 3 mot 1', 'Två rutor'],
    'Två rutor · Vita tre med röd jagare · Röda tre med vit jagare',
    [p('1', W, (0, (14, 32)), (2, (15, 34)), (4.5, (14, 31)), (6, (16, 36)), (8, (16, 36))),
     p('2', W, (0, (40, 34)), (1.5, (40, 34)), (3, (38, 38)), (6, (40, 33)), (8, (39, 35))),
     p('3', W, (0, (26, 68)), (3, (25, 68)), (5, (28, 66)), (7.5, (27, 68)), (9, (27, 68))),
     p('J', R, (0, (27, 46)), (1.5, (32, 42)), (3, (30, 55)), (4.5, (22, 45)), (6, (33, 42)), (7.5, (30, 58)), (9, (28, 50)), (18, (28, 50))),
     p('1', R, (0, (61, 66)), (9.8, (61, 66)), (11, (62, 64)), (13.6, (60, 66)), (15, (62, 62)), (16.5, (74, 50)), (18, (74, 50))),
     p('2', R, (0, (87, 64)), (11, (87, 64)), (12.3, (85, 60)), (18, (86, 62))),
     p('3', R, (0, (74, 30)), (12.3, (74, 30)), (13.6, (72, 33)), (18, (73, 32))),
     p('J', W, (0, (74, 50)), (9.8, (70, 56)), (11, (80, 58)), (12.3, (76, 40)), (13.6, (66, 60)), (14.8, (70, 62)), (16.5, (61, 66)), (18, (61, 66)))],
    [(0, (14, 32)), (1, (14, 32)), (1.5, (40, 34)), (2.5, (40, 34)), (3, (25, 68)), (4, (25, 68)), (4.5, (14, 31)), (5.5, (14, 31)),
     (6, (40, 33)), (7, (40, 33)), (7.5, (27, 68)), (8.4, (28, 67)), (9.8, (61, 66)), (10.5, (61, 66)), (11, (87, 64)), (11.8, (86, 62)),
     (12.3, (74, 30)), (13.1, (73, 32)), (13.6, (60, 66)), (14.2, (61, 65)), (14.8, (70, 62)), (16.5, (62, 65)), (18, (62, 65))],
    [(0, 'Tre vita mot en röd jagare', 'Röda har tre i höger ruta med en vit jagare.'),
     (1.5, 'Vitt passar: ett till fem', 'Triangel ger alltid två passningsvägar. Rör dig när bollen rör sig.'),
     (7.5, 'Fem passningar ger en poäng', 'Då slås bollen långt över till den andra rutan.'),
     (9.8, 'Rött startar sitt 3 mot 1', 'Den vita jagaren styr åt ena hållet.'),
     (14.8, 'Jagaren vinner bollen', 'Jagaren byter plats med nr 1 som tappade bollen.')])
C[-1]['shapes'] = shapes_base('SPELUPPBYGGNAD', [('box', 7, 24, 46, 76), ('box', 54, 24, 93, 76)])

if __name__ == '__main__':
    render(C, sys.argv)
