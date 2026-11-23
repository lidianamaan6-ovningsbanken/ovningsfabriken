# Omgång 2: tolv av Sams egna övningar, byggda steg för steg efter instruktionen.
from film_hjalp import *
import math as _m

C.clear()
WHITE = '#f3f5ef'

def finish(d, id_, slug, title, setup, phases, label, shapes, extras=None, target=14.5):
    pl = d.players(); balls = d.ballset()
    last = max([t for x in pl for t, _ in x['tr'] if t < 17.9] + [t for bb in balls for t, _ in bb if t < 17.9])
    f = max(1.0, min(2.2, target / last))
    sc = lambda tr: [(t * f if t < 17.9 else max(18, t * f), q) for t, q in tr]
    for x in pl: x['tr'] = sc(x['tr'])
    balls = [sc(bb) for bb in balls]
    phases = [(t * f, h, s_) for t, h, s_ in phases]
    add(id_, slug, title, setup, pl, balls[0], phases)
    C[-1]['balls'] = balls; C[-1]['shapes'] = shapes_base(label, shapes)
    if extras: C[-1]['extras'] = extras

# ============ t17 Passningsspel i romb ============
# Fyra käppar i romb. Spelaren kliver fram till käppen för att ta emot och spelar vidare.
# Bollen: nedifrån till vänster, upp, ner till höger och tillbaka. Följ din passning. Byt håll efter två minuter.
P = {'ner': (50, 82), 'vä': (22, 50), 'upp': (50, 18), 'hö': (78, 50)}
out = {k: ((v[0] - 50) * 0.18, (v[1] - 50) * 0.18) for k, v in P.items()}
def spot(k, n):  # n=0 vid käppen (mottagning), n=1,2 kö bakom
    x, y = P[k]; ox, oy = out[k]; return (x + ox * (0.6 + n), y + oy * (0.6 + n))
d = Drill(); q = {k: [] for k in P}
for k in P:
    for n in (1, 2):
        pid = f'{k}{n}'; d.p(pid, {'ner': '1', 'vä': '2', 'upp': '3', 'hö': '4'}[k], B, spot(k, n)); q[k].append(pid)
b = d.newball(d.at_feet('ner1'))
t = 0.6
def rotate(order, t):
    for a, c in zip(order, order[1:]):
        recv = q[c][0]; d.mv(recv, t, t + 0.6, spot(c, 0))           # kliver fram till käppen
        passer = q[a].pop(0)
        t2 = d.pas(b, t + 0.2, d.at_feet(recv, t + 0.6) if False else (spot(c, 0)[0] + 1.8, spot(c, 0)[1] - 1.2))
        d.mv(passer, t + 0.4, t + 2.0, spot(c, len(q[c])))            # följer sin passning
        q[c].append(passer)
        for n, w in enumerate(q[a]): d.mv(w, t + 0.6, t + 1.2, spot(a, n + 1))
        t = t2 + 0.35
    return t
t = rotate(['ner', 'vä', 'upp', 'hö', 'ner'], t)
t = rotate(['ner', 'hö', 'upp', 'vä', 'ner'], t + 0.6)
finish(d, 't17', 'passningsspel-i-romb', ['Passningsspel i romb', 'Följ din passning'], 'Fyra käppar i en romb · Spelare vid varje station',
       [(0, 'Bollen går nedifrån till vänster', 'Spelaren kliver fram till käppen för att ta emot.'),
        (2.6, 'Vidare upp och ner till höger', 'Öppen kroppsposition. Passa på rätt fot.'),
        (5.5, 'Tillbaka ner – och följ din passning', 'Den som passar springer till stationen den passade till.'),
        (8.3, 'Byt håll efter två minuter', 'Nu går bollen nedifrån till höger, upp, till vänster och ner.')],
       'SPELUPPBYGGNAD', [('pole', x, y) for x, y in P.values()])

# ============ t19 Kort och lång passning ============
# Åtta stationer A–H i en ring, två spelare vid varje. Varannan passning kort till grannstationen, varannan lång tvärs över.
# A kort till B, B lång till C, C kort till D, D lång till G och så vidare. Följ din passning.
ring = 'ABEFDCHG'
POS = {c: ring_pos(50, 50, 38, i, 8) for i, c in enumerate(ring)}
def sp(c, n):
    x, y = POS[c]; dx, dy = (x - 50) / 38, (y - 50) / 38; return (x + dx * 4.5 * n, y + dy * 4.5 * n)
d = Drill(); q = {}
for c in POS:
    q[c] = []
    for n in (0, 1):
        pid = f'{c}{n}'; d.p(pid, c, B, sp(c, n)); q[c].append(pid)
seq = 'ABCDGHEFA'
b = d.newball((sp('A', 0)[0] + 1.8, sp('A', 0)[1] - 1.2)); t = 0.8
for a, c in zip(seq, seq[1:]):
    passer = q[a].pop(0); recv = q[c][0]
    t2 = d.pas(b, t, (sp(c, 0)[0] + 1.8, sp(c, 0)[1] - 1.2))
    d.mv(passer, t + 0.2, t + 0.2 + (2.6 if (a, c) not in {('A', 'B'), ('C', 'D'), ('G', 'H'), ('E', 'F')} else 1.2), sp(c, len(q[c])))
    q[c].append(passer)
    for n, w in enumerate(q[a]): d.mv(w, t + 0.4, t + 1.0, sp(a, n))
    t = t2 + 0.9
finish(d, 't19', 'kort-och-lang-passning', ['Kort och lång passning', 'Åtta stationer'], 'Åtta stationer A–H i en ring · Två spelare vid varje',
       [(0, 'A spelar kort till B', 'Kort passning: insida och hård.'),
        (1.6, 'B spelar långt till C, C kort till D', 'Lång passning: lås fotleden och träffa mitt på bollen.'),
        (5, 'D spelar långt till G', 'Lyft blicken innan du passar.'),
        (7, 'Och så vidare: kort, lång, kort, lång', 'G kort till H, H lång till E, E kort till F, F lång till A.'),
        (13, 'Följ din passning', 'Flera bollar samtidigt när det flyter.')],
       'SPELUPPBYGGNAD', [('text', POS[c][0] + (POS[c][0] - 50) * 0.28, POS[c][1] + (POS[c][1] - 50) * 0.28, c) for c in POS])

# ============ t21 Rondo 8 mot 2 med överflyttning ============
# Två kvadrater med 8 spelare från varje lag. Tränaren kastar ut en boll till blått eller vitt lag.
# Får vitt bollen springer 2 blå direkt över och försöker vinna den. Nuddar en blå bollen springer 2 vita över
# till den blå kvadraten. De blå som jagade springer tillbaka till sin kvadrat och blir delaktiga i rondon.
LB = (8, 24, 46, 76); RB = (54, 24, 92, 76)
def sq8(box):
    x1, y1, x2, y2 = box; mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    return [(x1, y1 + 6), (mx, y1), (x2, y1 + 6), (x2, my), (x2, y2 - 6), (mx, y2), (x1, y2 - 6), (x1, my)]
d = Drill()
for i, ps in enumerate(sq8(LB)): d.p(f'b{i}', str(i + 1), B, ps)
for i, ps in enumerate(sq8(RB)): d.p(f'w{i}', str(i + 1), WHITE, ps)
d.p('T', 'T', G, (50, 90))
W = sq8(RB); Bq = sq8(LB)
b = d.newball((51, 87))
t = d.pas(b, 1.2, (W[5][0] + 1.8, W[5][1] - 1.2), 1.0)                 # tränaren kastar till vitt
d.mv('b3', 1.4, 3.6, (64, 46)); d.mv('b2', 1.4, 3.8, (70, 38))         # två blå springer över
seqw = [5, 3, 1, 7, 4, 2]; tt = t + 0.4
for i in seqw[1:]:
    tt = d.pas(b, tt, (W[i][0] + (1.8 if W[i][0] < 92 else -1.8), W[i][1] - 1.2)) + 0.45
d.mv('b3', 3.6, tt - 1.6, (78, 56)); d.mv('b2', 3.8, tt - 1.6, (72, 34))
touch = (76, 32)
t3 = d.pas(b, tt, touch, 0.4); d.mv('b2', tt - 0.4, t3, touch)          # en blå nuddar bollen
t4 = d.pas(b, t3 + 0.2, (Bq[3][0] + 1.8, Bq[3][1] - 1.2), 1.1)          # bollen till blått
d.mv('w0', t3 + 0.1, t3 + 2.6, (32, 40)); d.mv('w6', t3 + 0.1, t3 + 2.6, (30, 58))   # två vita springer över
d.mv('b2', t3 + 0.3, t3 + 2.8, Bq[2]); d.mv('b3', t3 + 0.3, t3 + 2.8, Bq[3])         # jagarna springer hem
for i in [1, 5, 7, 0]:
    t4 = d.pas(b, t4 + 0.45, (Bq[i][0] + 1.8, Bq[i][1] - 1.2))
d.mv('w0', t3 + 2.6, 17.5, (20, 38)); d.mv('w6', t3 + 2.6, 17.5, (24, 64))
finish(d, 't21', 'rondo-8-mot-2-med-overflyttning', ['Rondo 8 mot 2', 'Med överflyttning'], 'Två kvadrater · Åtta blå och åtta vita',
       [(0, 'Tränaren kastar ut en boll', 'Bollen går till antingen blått eller vitt lag. Här till vitt.'),
        (2.2, 'Två blå springer direkt över', 'De försöker vinna bollen medan de vita passar runt.'),
        (5.5, 'Jagarna samarbetar', 'En pressar och en täcker.'),
        (t3 - 0.1, 'En blå nuddar bollen', 'Två vita springer snabbt över till den blå kvadraten.'),
        (t3 + 1.6, 'De blå jagarna springer tillbaka', 'De blir delaktiga i rondon. Inte samma som jagar hela tiden.')],
       'ÅTERERÖVRING', [('box', *LB), ('box', *RB)])

# ============ t22 Spelavstånd i speluppbyggnad ============
# 8 spelare, 40 × 20 m. Två i varje hörn uppe, två centralt och en i varje hörn nere.
# X1 passar till X2 som gör tillbakaspel till X3. X3 passar till X4 som löper framåt i djupled och passar vidare till X5.
# Övningen vänder från andra hållet.
d = Drill()
TL, TR, BL, BR = (28, 14), (72, 14), (28, 86), (72, 86)
d.p('tl1', 'X5', B, TL); d.p('tl2', 'X5', B, (TL[0] - 4, TL[1] - 3))
d.p('tr1', 'X5', B, TR); d.p('tr2', 'X5', B, (TR[0] + 4, TR[1] - 3))
d.p('c1', 'X2', B, (42, 52)); d.p('c2', 'X4', B, (58, 52))
d.p('bl', 'X1', B, BL); d.p('br', 'X3', B, BR)
b = d.newball((BL[0] + 1.8, BL[1] - 1.2))
d.mv('c1', 0.3, 1.2, (40, 60)); t = d.pas(b, 0.8, (41.8, 58.8))                   # X1 till X2 som kommer emot
t = d.pas(b, t + 0.3, (BR[0] - 1.8, BR[1] - 1.2))                                  # tillbakaspel till X3
d.mv('c2', t, t + 2.4, (62, 30)); t = d.pas(b, t + 0.4, (63.8, 28.8))              # X3 i djupled till X4
t = d.pas(b, t + 0.4, (TR[0] - 1.8, TR[1] + 1.2))                                  # X4 till X5
d.mv('c1', t - 1, t + 0.6, (42, 52)); d.mv('c2', t - 0.2, t + 1.4, (58, 52))
# vänder: uppifrån vänster ner
d.mv('c2', t + 1.6, t + 2.4, (60, 42)); t = d.pas(b, t + 1.6, (TL[0] + 1.8, TL[1] + 1.2), 1.0)
t = d.pas(b, t + 0.3, (59.8, 43.2))                                                # X5 till central
t = d.pas(b, t + 0.3, (TR[0] - 1.8, TR[1] + 1.2))                                  # tillbakaspel
d.mv('c1', t, t + 2.4, (38, 72)); t = d.pas(b, t + 0.4, (39.8, 70.8))              # djupled nedåt
t = d.pas(b, t + 0.4, (BL[0] + 1.8, BL[1] - 1.2))
finish(d, 't22', 'spelavstand-i-speluppbyggnad', ['Spelavstånd', 'I speluppbyggnad'], '8 spelare · Yta 40 × 20 m',
       [(0, 'X1 passar till X2', 'X2 kommer emot bollen centralt.'),
        (1.8, 'X2 gör tillbakaspel till X3', 'Spänn tillslagsfoten genom att vinkla tårna uppåt.'),
        (3.2, 'X3 passar till X4 som löper i djupled', 'Tajma löpning och passning i djupled.'),
        (5.2, 'X4 passar vidare till X5', 'Variera längden på passningarna.'),
        (7.6, 'Övningen vänder från andra hållet', 'Byt de centrala spelarna efter en viss tid.')],
       'SPELUPPBYGGNAD', [('box', 20, 8, 80, 92), ('cone', 20, 8), ('cone', 80, 8), ('cone', 20, 92), ('cone', 80, 92)])

# ============ t23 Passning med väggspel ============
# Tre stationer på rad över planen med käppar. A: 1 passar till 2. B: 2 passar till 3 vid käppen.
# C: 3 spelar vägg tillbaka till 2 som har löpt förbi. D: 2 passar vidare till nästa station. E: ny passning upp. Alla följer sin passning.
d = Drill(); X = [16, 50, 84]
for i, x in enumerate(X):
    d.p(f's{i}a', '1', B, (x, 84)); d.p(f's{i}b', '1', B, (x, 90))
    d.p(f's{i}2', '2', B, (x, 62)); d.p(f's{i}3', '3', B, (x + 8, 40))
b = d.newball((X[0] + 1.8, 82.8)); t = 0.6
for i, x in enumerate(X):
    t = d.pas(b, t, (x + 1.8, 60.8)); d.mv(f's{i}a', t - 0.6, t + 0.8, (x - 3, 66))             # A: 1 till 2, följer
    t = d.pas(b, t + 0.35, (x + 6.2, 41.2)); d.mv(f's{i}2', t - 0.6, t + 0.4, (x - 2, 34))       # B: 2 till 3, löper förbi
    t = d.pas(b, t + 0.25, (x + 0, 32.8)); d.mv(f's{i}3', t - 0.4, t + 0.6, (x + 6, 44))         # C: vägg till 2
    if i < 2:
        nx = X[i + 1]; t = d.pas(b, t + 0.35, (nx + 1.8, 82.8), 1.3)                              # D: vidare till nästa station
        d.mv(f's{i}2', t - 1.3, t + 1.2, (nx - 4, 88))
    else:
        d.carry(b, f's{i}2', t, t + 1.6); d.mv(f's{i}2', t, t + 1.6, (x, 26))
    t += 0.2
finish(d, 't23', 'passning-med-vaggspel', ['Passning med väggspel', 'Tre stationer'], 'Tre stationer på rad · Käppar · Spelare på led vid varje start',
       [(0, 'A: 1 passar till 2', 'Alla följer sin passning.'),
        (1.6, 'B: 2 passar till 3 vid käppen', 'Löp direkt efter passningen.'),
        (2.4, 'C: 3 spelar vägg till 2 som löpt förbi', 'Väggspelet på ett tillslag.'),
        (3.4, 'D: 2 passar vidare till nästa station', 'Passa i löpriktningen.'),
        (4.8, 'E: ny passning upp', 'Samma mönster på station två och tre.')],
       'SPELUPPBYGGNAD', [('pole', x + 8, 36) for x in X] + [('text', x, 96, f'STATION {i + 1}') for i, x in enumerate(X)])

# ============ t24 Uppvärmning: passningsspel ============
# Två banor, en på varje planhalva, käppar och spelare på led. A: passa och få tillbaka. B: passa till spelaren som rör sig
# runt käppen. C: passning ner. D: lång passning till nästa led. Följ din passning.
d = Drill(); balls = []
for k, (x0, col) in enumerate([(10, B), (56, R)]):
    S, M, Pk, Q = (x0 + 8, 84), (x0 + 8, 62), (x0 + 26, 40), (x0 + 8, 18)
    d.p(f'{k}s1', 'A', col, S); d.p(f'{k}s2', 'A', col, (S[0], S[1] + 6))
    d.p(f'{k}m', 'B', col, M); d.p(f'{k}r', 'C', col, (Pk[0] - 6, Pk[1] + 6)); d.p(f'{k}q', 'D', col, Q); d.p(f'{k}q2', 'D', col, (Q[0], Q[1] - 6))
    bb = d.newball((S[0] + 1.8, S[1] - 1.2)); off = 0.6 + k * 0.5
    t = d.pas(bb, off, (M[0] + 1.8, M[1] + 1.2)); t = d.pas(bb, t + 0.3, (S[0] + 1.8, S[1] - 1.2))     # A
    d.path(f'{k}r', t - 0.6, [(Pk[0] + 4, Pk[1] + 3), (Pk[0] + 3, Pk[1] + 8)])
    t = d.pas(bb, t + 0.5, (Pk[0] + 4.8, Pk[1] + 9)); d.mv(f'{k}s1', t - 0.8, t + 1.2, (Pk[0] - 4, Pk[1] + 10))  # B
    t = d.pas(bb, t + 0.4, (M[0] + 1.8, M[1] + 1.2)); d.mv(f'{k}r', t - 0.5, t + 1.2, (M[0] + 5, M[1] + 4))     # C ner
    t = d.pas(bb, t + 0.4, (Q[0] + 1.8, Q[1] + 1.2), 1.2); d.mv(f'{k}m', t - 1.0, t + 1.4, (Q[0], Q[1] + 6))     # D lång
    d.mv(f'{k}s2', 2, 3.2, S)
finish(d, 't24', 'uppvarmning-passningsspel', ['Uppvärmning', 'Passningsspel'], 'Två banor · En på varje planhalva · Käppar och spelare på led',
       [(0, 'A: passa och få tillbaka', 'Varje lag kör sin bana.'),
        (2.3, 'B: passa till spelaren som rör sig runt käppen', 'Rör dig runt käppen innan du tar emot.'),
        (4, 'C: passning ner', 'Ta emot med bortre foten.'),
        (5.2, 'D: lång passning till nästa led', 'Fart i passningarna.'),
        (6.8, 'Följ din passning', 'Ny spelare startar från leden.')],
       'SPELUPPBYGGNAD', [('line', [(50, 5), (50, 95)]), ('pole', 36, 40), ('pole', 82, 40)])

# ============ t25 Passningsvariant 1 (A–F) ============
# A och C på vänster sida, B och D vid käppar, E och F i andra änden. A passar till B. B lägger upp till C som kommer framåt.
# C slår till D. D lägger tillbaka till A som har löpt fram. A slår långt till E, och A löper till F. Alla går en station vidare.
d = Drill()
A0, C0, B0, D0, E0, F0 = (22, 90), (14, 64), (42, 76), (52, 44), (76, 10), (28, 10)
for k, ps in [('A', A0), ('C', C0), ('B', B0), ('D', D0), ('E', E0), ('F', F0)]: d.p(k, k, B, ps)
d.p('A2', 'A', B, (A0[0] - 5, A0[1] + 4))
b = d.newball((A0[0] + 1.8, A0[1] - 1.2))
t = d.pas(b, 0.6, (B0[0] - 1.6, B0[1] + 1.2))                                        # A till B
d.mv('C', t - 0.6, t + 0.6, (20, 56)); t = d.pas(b, t + 0.3, (21.8, 55))             # B lägger upp till C som kommer fram
t = d.pas(b, t + 0.4, (D0[0] - 1.6, D0[1] + 1.4))                                    # C slår till D
d.mv('A', 1.2, t + 0.9, (38, 54)); t = d.pas(b, t + 0.3, (39.6, 53))                 # D lägger tillbaka till A som löpt fram
t = d.pas(b, t + 0.4, (E0[0] - 1.8, E0[1] + 1.2), 1.4)                               # A långt till E
d.mv('A', t - 1.2, t + 2.2, (F0[0] + 5, F0[1] + 2))                                  # A löper till F
d.mv('B', t, t + 2.2, (20, 60)); d.mv('C', t, t + 2.2, (D0[0] - 5, D0[1] + 4)); d.mv('D', t, t + 2.2, (E0[0] - 6, E0[1] + 4))
d.mv('A2', t, t + 1, A0)
finish(d, 't25', 'passningsvariant-1-a-f', ['Passningsvariant 1', 'A–F'], 'Stationer A–F över en hel plan · Käppar vid B och D',
       [(0, 'A passar till B', 'Lägg av med rätt tyngd.'),
        (1.5, 'B lägger upp till C som kommer framåt', 'Rätt tajming på löpningarna.'),
        (2.7, 'C slår till D', 'A har börjat löpa fram.'),
        (4.2, 'D lägger tillbaka till A', 'A har löpt fram.'),
        (5.5, 'A slår långt till E och löper till F', 'Lång passning: titta upp innan.'),
        (7.6, 'Alla går en station vidare', 'Nästa A startar med en ny boll.')],
       'SPELUPPBYGGNAD', [('pole', B0[0] + 4, B0[1] - 2), ('pole', D0[0] + 4, D0[1] - 2)] + [('text', x - 6, y + 6, k) for k, (x, y) in [('A', A0), ('C', C0), ('B', B0), ('D', D0), ('E', E0), ('F', F0)]])

# ============ t26 Ajax uppvärmning ============
# Halvplan med dockor och bollar vid start. A: passning till spelaren som kommer fram mellan dockorna (B).
# C: vidare till nästa mellan dockorna. D: ny spelare kommer fram. E: passning upp till toppen. G: lång passning tillbaka till start.
DK = [((38, 70), (52, 70)), ((52, 48), (66, 48)), ((36, 32), (50, 32))]
GAP = [(45, 70), (59, 48), (43, 32)]
d = Drill()
d.p('s1', 'S', B, (30, 90)); d.p('s2', 'S', B, (24, 92))
d.p('b1', 'B', B, (45, 80)); d.p('b2', 'C', B, (66, 58)); d.p('b3', 'D', B, (34, 40)); d.p('top', 'T', B, (60, 10))
b = d.newball((31.8, 88.8))
d.mv('b1', 0.2, 1.4, GAP[0]); t = d.pas(b, 0.8, (GAP[0][0] + 1.8, GAP[0][1] + 1.2))                    # A
d.mv('b2', t - 0.6, t + 0.6, GAP[1]); t = d.pas(b, t + 0.4, (GAP[1][0] + 1.8, GAP[1][1] + 1.2))       # C
d.mv('b1', t - 1, t + 1, (GAP[1][0] - 3, GAP[1][1] + 8))
d.mv('b3', t - 0.4, t + 0.8, GAP[2]); t = d.pas(b, t + 0.4, (GAP[2][0] + 1.8, GAP[2][1] + 1.2))       # D: ny spelare kommer fram
d.mv('b2', t - 1, t + 1, (GAP[2][0] + 5, GAP[2][1] + 8))
t = d.pas(b, t + 0.5, (61.8, 11.2)); d.mv('b3', t - 0.8, t + 1.4, (54, 16))                            # E: upp till toppen
t = d.pas(b, t + 0.5, (31.8, 88.8), 1.7); d.mv('top', t - 1.5, t + 1.4, (36, 86))                      # G: lång tillbaka
finish(d, 't26', 'ajax-uppvarmning', ['Ajax uppvärmning', 'Passningsövning'], 'Halvplan med dockor · Bollar vid start',
       [(0, 'A: passning till B mellan dockorna', 'Visa dig mellan dockorna.'),
        (1.9, 'C: vidare till nästa mellan dockorna', 'Vänd med första touchen.'),
        (3.3, 'D: ny spelare kommer fram', 'Alla följer sin passning.'),
        (4.8, 'E: passning upp till toppen', 'Spela med rätt tyngd.'),
        (6.4, 'G: lång passning tillbaka till start', 'Lång passning med båge tillbaka.')],
       'SPELUPPBYGGNAD', [('pole', *pos_) for pr in DK for pos_ in pr] + [('text', 30, 97, 'START')])

# ============ t27 Passningsövning dubbel 1 ============
# Dockor centralt, spelare vid mål (1), centralt (2) och på kanterna (3), start vid mittcirkeln.
# Start passar till 2. 2 vänder och slår ut till 3 på kanten. 3 spelar diagonalt in till 1 vid målet. Alla följer passningen. Kör åt båda hållen.
d = Drill()
def side(sfx, f, col):
    S, Dm, Two, Three, One = f((44, 56)), f((50, 32)), f((44, 36)), f((88, 26)), f((50, 9))
    d.p('s' + sfx, 'S', col, S); d.p('2' + sfx, '2', col, Two); d.p('3' + sfx, '3', col, Three); d.p('1' + sfx, '1', col, One)
    bb = d.newball((S[0] + 1.8, S[1] - 1.2))
    d.path('2' + sfx, 0.4, [f((44, 28)), f((56, 30)), f((56, 38))], speed=1.4)
    t = d.pas(bb, 1.4, (f((56, 38))[0] + 1.8, f((56, 38))[1]))
    d.mv('s' + sfx, t - 0.6, t + 1.6, f((52, 42)))
    t = d.pas(bb, t + 0.6, (Three[0] - 1.8, Three[1] + 1.2)); d.mv('2' + sfx, t - 0.8, t + 1.6, f((82, 32)))
    t = d.pas(bb, t + 0.4, (One[0] + 1.8, One[1] + 1.6)); d.mv('3' + sfx, t - 0.8, t + 1.6, f((56, 14)))
    return Dm
dm1 = side('a', lambda q: q, B); dm2 = side('b', lambda q: (100 - q[0], 100 - q[1]), R)
finish(d, 't27', 'passningsovning-dubbel-1', ['Passningsövning dubbel 1', 'Åt båda hållen'], 'Dockor centralt · Spelare vid mål, centralt och på kanterna',
       [(0, 'Start passar upp till 2', '2 rör sig runt dockan innan mottagningen.'),
        (2.4, '2 vänder och slår ut till 3 på kanten', 'Öppen kroppsposition.'),
        (4.2, '3 spelar diagonalt in till 1 vid målet', 'Diagonalen med rätt tyngd.'),
        (6, 'Alla följer passningen', 'Kör åt båda hållen samtidigt.')],
       'SPELUPPBYGGNAD', [('pole', 50, 30), ('pole', 50, 70), ('circle', 50, 50, 9), ('line', [(0, 50), (100, 50)])])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ t28 Passningsövning dubbel 2 ============
# Dockor vid straffområdet och mittcirkeln. Vänster spelare passar kort upp. Mottagaren slår diagonalt ner i löpningen
# från spelaren som bågar runt dockan. Bollen går vidare till höger och in mellan dockorna. Följ din passning.
d = Drill()
V, U, Rn, H = (20, 46), (26, 26), (50, 70), (82, 40)
d.p('v', 'V', B, V); d.p('u', 'U', B, U); d.p('r', 'L', B, Rn); d.p('h', 'H', B, H); d.p('v2', 'V', B, (V[0] - 5, V[1] + 4))
b = d.newball((V[0] + 1.8, V[1] - 1.2))
t = d.pas(b, 0.6, (U[0] + 1.8, U[1] + 1.2)); d.mv('v', t - 0.4, t + 1.4, (U[0] - 4, U[1] + 4))           # kort upp
d.path('r', t - 0.4, [(42, 60), (40, 52), (46, 46)], speed=1.3)                                          # båglöpning runt dockan
t = d.pas(b, t + 0.6, (47.8, 45.2)); d.mv('u', t - 0.6, t + 1.6, (44, 52))                             # diagonalt i löpningen
t = d.pas(b, t + 0.4, (H[0] - 1.8, H[1] + 1.2)); d.mv('r', t - 0.6, t + 1.6, (76, 44))                 # vidare till höger
d.mv('u', t - 0.3, t + 1.0, (50, 24))
t = d.pas(b, t + 0.4, (51.8, 22.8)); d.mv('h', t - 0.6, t + 1.6, (56, 20))                             # in mellan dockorna
d.carry(b, 'u', t, t + 0.8); d.mv('u', t, t + 0.8, (50, 18)); d.mv('v2', 1, 2, V)
finish(d, 't28', 'passningsovning-dubbel-2', ['Passningsövning dubbel 2', 'Båglöpning och diagonal'], 'Dockor vid straffområdet och mittcirkeln · Spelare runt om',
       [(0, 'Vänster spelare passar kort upp', 'Spelaren vid mittcirkeln börjar bågen runt dockan.'),
        (1.6, 'Diagonalt ner i löpningen', 'Båglöpning i rätt tid. Passa framför löparen.'),
        (3.2, 'Bollen går vidare till höger', 'Lyft blicken.'),
        (4.6, 'In mellan dockorna', 'Följ din passning.')],
       'SPELUPPBYGGNAD', [('pole', 44, 21), ('pole', 58, 21), ('pole', 44, 60), ('circle', 50, 72, 9)])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ t29 Rondo med rörelse ============
# Flera ringar, 3 mot 1 i ringarna och några tomma. Tränaren med bollar vid sidan. Spela 3 mot 1. På signal eller efter
# fem passningar löper en spelare till en tom ring, får en lång passning och de andra följer efter. Jagaren följer med och pressar.
RG = [(26, 30), (74, 30), (26, 72), (74, 72)]
def tri(c, k):
    v = _m.radians(-90 + 120 * k); return (c[0] + 9 * _m.cos(v), c[1] + 9 * _m.sin(v) * 1.2)
d = Drill()
for g, (ring_, col) in enumerate([(0, B), (3, R)]):
    for k in range(3): d.p(f'g{g}{k}', str(k + 1), col, tri(RG[ring_], k))
    d.p(f'j{g}', 'J', G, RG[ring_])
d.p('T', 'T', G, (50, 94))
for g, (ring_, new, t_run) in enumerate([(0, 1, 6.4), (3, 2, 8.6)]):
    bb = d.newball((tri(RG[ring_], 0)[0] + 1.8, tri(RG[ring_], 0)[1] - 1.2)); t = 0.5 + g * 0.4
    for k in [1, 2, 0, 1, 2]:
        t = d.pas(bb, t + 0.35, (tri(RG[ring_], k)[0] + 1.8, tri(RG[ring_], k)[1] - 1.2))
        d.mv(f'j{g}', t - 0.5, t, ((RG[ring_][0] * 2 + tri(RG[ring_], k)[0]) / 3, (RG[ring_][1] * 2 + tri(RG[ring_], k)[1]) / 3))
    d.mv(f'g{g}0', t, t + 2.2, tri(RG[new], 0))                                             # en spelare löper till tom ring
    t2 = d.pas(bb, t + 1.0, (tri(RG[new], 0)[0] + 1.8, tri(RG[new], 0)[1] - 1.2), 1.4)      # lång passning
    d.mv(f'g{g}1', t2 - 0.6, t2 + 2, tri(RG[new], 1)); d.mv(f'g{g}2', t2 - 0.6, t2 + 2, tri(RG[new], 2))   # följer efter
    d.mv(f'j{g}', t2 - 0.4, t2 + 1.8, ((RG[new][0] * 2 + tri(RG[new], 0)[0]) / 3, (RG[new][1] * 2 + tri(RG[new], 0)[1]) / 3))  # jagaren pressar
    tt = t2 + 2
    for k in [1, 2, 0, 1]:
        tt = d.pas(bb, tt + 0.35, (tri(RG[new], k)[0] + 1.8, tri(RG[new], k)[1] - 1.2))
finish(d, 't29', 'rondo-med-rorelse', ['Rondo med rörelse', '3 mot 1 i ringar'], 'Flera ringar · 3 mot 1 i några · Några ringar tomma',
       [(0, 'Spela 3 mot 1 i ringen', 'Tre spelare och en jagare i varje ring. Tränaren står vid sidan med bollar.'),
        (4.6, 'Efter fem passningar: löp till en tom ring', 'Se den tomma ytan. Löp när passningen kan komma.'),
        (6.2, 'Lång passning till löparen', 'Passa långt och följ med direkt.'),
        (8, 'De andra följer efter', 'Jagaren följer med och pressar i den nya ringen.')],
       'SPELUPPBYGGNAD', [('circle', x, y, 13) for x, y in RG])

# ============ t44 Possession och omställning till avslut ============
# Mittzon med 3 mot 3 + 2 och fyra småmål, ändzoner med målvakt och försvarare. Laget med boll håller den i mittzonen.
# Efter fem passningar får de anfalla in i ändzonen mot försvararna och avsluta. Tappar de bollen kontrar motståndarna mot småmålen.
d = Drill()
for k, ps in enumerate([(34, 54), (62, 46), (50, 62)]): d.p(f'b{k}', str(k + 1), B, ps)
for k, ps in enumerate([(42, 44), (58, 58), (48, 50)]): d.p(f'r{k}', str(k + 1), R, ps)
d.p('j1', 'J', G, (24, 46)); d.p('j2', 'J', G, (76, 56))
d.p('fd', 'F', R, (50, 20)); d.p('fm', 'MV', R, (50, 6)); d.p('bd', 'F', B, (50, 80)); d.p('bm', 'MV', B, (50, 94))
b = d.newball((35.8, 52.8)); t = 0.5
for who in ['j1', 'b0', 'b1', 'j2', 'b2']:
    tgt = d.pos(who); t = d.pas(b, t + 0.35, (tgt[0] + 1.8, tgt[1] - 1.2))
d.mv('r0', 1, t, (44, 52)); d.mv('r1', 1, t, (60, 52)); d.mv('r2', 1, t, (52, 56))
d.mv('b0', t - 0.6, t + 1.6, (40, 22)); d.mv('b1', t - 0.6, t + 1.6, (62, 24))                  # anfall in i ändzonen
t = d.pas(b, t + 0.6, (41.8, 22.8)); d.mv('fd', t - 0.8, t + 0.6, (46, 18))
t = d.pas(b, t + 0.3, (60.2, 22.8)); t = d.pas(b, t + 0.3, (55, -1), 0.5); d.mv('fm', t - 0.5, t, (54, 6))
# ny boll: blått tappar, rött kontrar mot småmål
d.mv('b0', t + 0.2, t + 2, (40, 46)); d.mv('b1', t + 0.2, t + 2, (58, 46))
b2 = d.newball((51.8, 54.8)); d.mv('b2', 0, 0.1, (50, 62))
t3 = t + 0.6; d.mv('b2', t3, t3 + 0.5, (50, 56)); d.pl  # blå nr 3 med bollen
d.balls[b2] = [(0, (200, 200)), (t3 - 0.01, (200, 200)), (t3, (51.8, 54.8))]
d.mv('r2', t3, t3 + 0.6, (50, 54)); t4 = d.pas(b2, t3 + 0.7, (60, 56), 0.4); d.mv('r1', t3 + 0.3, t4, (60, 57))   # rött vinner
d.carry(b2, 'r1', t4, t4 + 1.6); d.mv('r1', t4, t4 + 1.6, (80, 60))
d.pas(b2, t4 + 1.7, (93, 60), 0.4)
finish(d, 't44', 'possession-och-omstallning-till-avslut', ['Possession och omställning', 'Till avslut'], 'Mittzon 3 mot 3 + 2 · Fyra småmål · Ändzoner med målvakt och försvarare',
       [(0, 'Laget med boll håller den i mittzonen', 'Bollinnehav med syfte: leta efter vägen framåt.'),
        (3.6, 'Efter fem passningar: anfall in i ändzonen', 'Mot försvararen och målvakten.'),
        (5.6, 'Avsluta innan försvaret är på plats', 'Snabbt avslut.'),
        (8.4, 'Tappar de bollen kontrar motståndarna', 'Rött vinner bollen och kontrar mot småmålen.'),
        (10.5, 'Snabb omställning när bollen vinns', 'Mål i småmål.')],
       'OMSTÄLLNING', [('zone', 4, 30, 96, 70, (200, 220, 200), 'MITTZON'), ('smallgoal', 7, 40), ('smallgoal', 7, 60), ('smallgoal', 93, 40), ('smallgoal', 93, 60)])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

if __name__ == '__main__':
    render(C, sys.argv)
