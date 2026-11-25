# SvFF-övningar efter skickade PDF:er, del 1 (spelform 3 mot 3). Regel: först d.mv, sedan d.carry; först mottagarens rörelse, sedan passningen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e9', __file__.replace('render_svff1.py', 'render_extern9.py'))
e9 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e9); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e9.finish, e9.rec, e9.chain, e9.wander, e9.counter, e9.arrivals
lab, hide, show, team, boxes, drive, shoot = e9.lab, e9.hide, e9.show, e9.team, e9.boxes, e9.drive, e9.shoot
factor, swap_color, stand, countdown, countup, win = e9.factor, e9.swap_color, e9.stand, e9.countdown, e9.countup, e9.win
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'

# ============ wj05 Spelarna först – lekmatch utan coachning ============
SV = ('svb',)

# ============ svb45157 Spel mot två mål ============
# 3 mot 3. Fyra små mål i hörnen, lagen gör mål i två mål var.
d = Drill()
BP = [(30, 70), (70, 70), (50, 56)]; RP = [(34, 34), (66, 34), (50, 46)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b0', 0))
d.mv('r0', 0.4, 1.8, (28, 44)); t = d.pas(b, 0.6, rec(d, 'b2', 1.4)); t = drive(d, b, 'b2', t, (44, 40), 12)   # driver – vänstra målet stängt
d.mv('r2', t - 0.8, t + 0.2, (40, 34)); tw = win(d, b, 'r2', 'b2', t + 0.4, 0.6)                                     # röd bryter
d.mv('b2', tw, tw + 0.8, rec(d, 'r2', tw + 0.9)); tb = win(d, b, 'b2', 'r2', tw + 1.0, 0.8)                         # tar tillbaka direkt
t = drive(d, b, 'b2', tb, (66, 28), 14); t = drive(d, b, 'b2', t, (76, 18), 14); tg = d.pas(b, t + 0.1, (79, 13), 0.4); hide(d, b, tg + 0.3)
d.mv('r1', tb, tg, (70, 26))
fp = [(0, 'Tre mot tre – två mål var', 'Blå gör mål uppe, röd gör mål nere.'),
      (1.6, 'Passera med bollen', 'Driv, vänd, utmana, finta och dribbla.'),
      (tw - 0.2, 'Bryt och ta tillbaka', 'Tappar du bollen – vinn den direkt igen.'),
      (tb + 0.4, 'Driv bort från motståndaren', 'Mot det mål som är öppet.')]
finish(d, 'svb45157', 'spel-mot-tva-mal-3v3-svb45157', ['Spel mot två mål', 'Spelform 3 mot 3'], 'Ca 6 spelare · Yta 15 × 12 m · Fyra små mål',
       fp, 'SPELUPPBYGGNAD', [('box', 14, 10, 86, 90), ('smallgoal', 20, 12), ('smallgoal', 80, 12), ('smallgoal', 20, 88), ('smallgoal', 80, 88)],
       [lab(tw, tw + 1.0, (40, 48), 'BRYT'), lab(tb, tb + 1.2, (52, 30), 'TILLBAKA!'), lab(tg, tg + 1.6, (72, 22), 'MÅL!')])

# ============ svb122292 Spel med fokus på 1 mot 1-situationer ============
d = Drill(); d.p('mvr', 'MV', R, (50, 6)); d.p('mvb', 'MV', B, (50, 94))
BP = [(26, 70), (74, 70), (40, 50), (62, 40)]; RP = [(30, 34), (70, 34), (56, 56), (42, 24)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b0', 0))
d.mv('b3', 0.4, 1.4, (64, 44)); d.mv('r1', 0.4, 1.6, (66, 36))
t = d.pas(b, 0.6, rec(d, 'b3', 1.6), 1.0); d.mv('b3', t, t + 0.4, (66, 40)); d.carry(b, 'b3', t, t + 0.4); tv = t   # vänder upp
t = drive(d, b, 'b3', t + 0.4, (60, 30), 12); d.mv('r1', t - 0.8, t, (64, 26))                                     # utmanar
t = drive(d, b, 'b3', t, (72, 22), 18); d.mv('r1', t - 0.4, t + 0.4, (64, 22))                                     # riktningsförändring + tempo
d.mv('mvr', t - 0.6, t + 0.2, (56, 8)); tg = shoot(d, b, t + 0.05, (58, 7)); d.carry(b, 'mvr', tg, tg + 0.6)        # målvakten fångar
for k, ps in enumerate([(24, 62), (76, 62), (44, 44), (60, 30)]): d.mv(f'b{k}', tg, tg + 1.6, ps)
t = d.pas(b, tg + 0.8, rec(d, 'r0', tg + 1.8), 1.0); d.mv('b0', tg + 0.6, t + 0.4, (32, 46))                       # pressar sidställd
tw = win(d, b, 'b0', 'r0', t + 0.7, 0.8)
fp = [(0, 'Två lag med målvakter', 'Spel enligt spelformens regler.'),
      (tv - 0.4, 'Bli rättvänd – vänd upp', 'Orientera dig innan bollen kommer.'),
      (tv + 0.8, 'Utmana!', 'Riktningsförändring och tempoväxling.'),
      (tg + 0.6, 'Målvakten fångar – försvararen pressar', 'Sidställd, i pressavstånd, bryt mellan tillslagen.')]
finish(d, 'svb122292', 'spel-med-fokus-pa-1-mot-1-situationer-svb122292', ['Spel med fokus på', '1 mot 1-situationer'], '8–16 spelare · Yta 55 × 40 m · Två mål',
       fp, 'AVSLUT', [('box', 8, 4, 92, 96)], [lab(t - 0.2, t + 1.2, (40, 40), 'BRYT')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ svb48719 SvFF D – Spelövning (spelform 3v3) ============
# Start: två matcher 1 mot 1 mot konmål i samma yta. Progression: 2 mot 2, två mål var.
d = Drill()
d.p('a0', '1', B, (30, 74)); d.p('f0', '1', R, (30, 46)); d.p('a1', '2', B, (70, 74)); d.p('f1', '2', R, (70, 46))
b0 = d.newball(rec(d, 'a0', 0)); b1 = d.newball(rec(d, 'a1', 0))
t = drive(d, b0, 'a0', 0.4, (26, 50), 12); d.mv('f0', 0.4, t, (30, 40)); t = drive(d, b0, 'a0', t, (36, 28), 16); d.mv('f0', t - 0.6, t, (30, 24))
t = drive(d, b0, 'a0', t, (32, 14), 14); ta = t                                                                     # driver genom konmålet
t = drive(d, b1, 'a1', 0.6, (70, 56), 12); d.mv('f1', 0.6, t, (68, 48)); tw = win(d, b1, 'f1', 'a1', t + 0.4, 0.5)
t = drive(d, b1, 'f1', tw, (68, 84), 14); tb = t
tp = max(ta, tb) + 0.8; hide(d, b0, tp - 0.2); hide(d, b1, tp - 0.2)
for pid, ps in [('a0', (34, 76)), ('a1', (60, 70)), ('f0', (40, 30)), ('f1', (62, 36))]: d.mv(pid, tp - 0.2, tp + 1.2, ps)
b2 = d.newball((200, 200)); show(d, b2, tp + 1.2, rec(d, 'a0', tp + 1.2))
t = d.pas(b2, tp + 1.4, rec(d, 'a1', tp + 2.2)); d.mv('f1', tp + 1.4, t, (64, 54)); d.mv('a0', tp + 1.6, t + 0.6, (30, 46))
t = d.pas(b2, t + 0.3, rec(d, 'a0', t + 1.1)); t = drive(d, b2, 'a0', t, (24, 16), 16); d.mv('f0', t - 1.2, t, (30, 22))
fp = [(0, 'Två matcher 1 mot 1 i samma yta', 'Mål görs i konmålen.'),
      (ta - 0.3, 'Driv genom konmålet', ''),
      (tw - 0.2, 'Bollvinst – anfall åt andra hållet', 'Byten när bollen går ur spel.'),
      (tp + 0.2, 'Progression: 2 mot 2', 'Lagen försvarar två mål var.')]
finish(d, 'svb48719', 'svff-d-spelovning-spelform-3v3-svb48719', ['SvFF D – Spelövning', 'Spelform 3 mot 3'], '6–11 spelare · Yta 15 × 10 m · Konmål',
       fp, 'SPELUPPBYGGNAD', [('box', 12, 10, 88, 90)] + [('cone', x + dx, y) for x in (30, 70) for y in (10, 90) for dx in (-5, 5)],
       [lab(ta, ta + 1.2, (32, 22), 'MÅL'), lab(t, t + 1.4, (24, 22), 'MÅL')])

# ============ svb140353 Futsal – Nummerspel (U7–U8) ============
d = Drill(); d.p('t', 'T', T_COL, (50, 96))
for k in range(3): d.p(f'b{k}', str(k + 1), B, (6, 38 + 12 * k)); d.p(f'r{k}', str(k + 1), R, (94, 38 + 12 * k))
b = d.newball((200, 200)); show(d, b, 1.0, rec(d, 't', 1.0))
d.mv('b1', 1.0, 2.4, (40, 52)); d.mv('r1', 1.0, 2.4, (60, 46))
t = d.pas(b, 1.2, rec(d, 'b1', 2.4), 1.2); t = drive(d, b, 'b1', t, (38, 30), 12); d.mv('r1', t - 1.2, t, (40, 22))   # mot övre målen – stängt
t = drive(d, b, 'b1', t, (52, 54), 14); t = drive(d, b, 'b1', t, (64, 76), 16); d.mv('r1', t - 1.8, t, (50, 64))      # spelvändning
t = drive(d, b, 'b1', t, (66, 90), 16); tg = t; d.carry(b, 'b1', tg, tg + 0.3)
for pid, ps in [('b1', (6, 50)), ('r1', (94, 50))]: d.mv(pid, tg + 0.4, tg + 2.2, ps)
hide(d, b, tg + 0.5); b2 = d.newball((200, 200)); show(d, b2, tg + 1.0, rec(d, 't', tg + 1.0))
for pid, ps in [('b0', (36, 40)), ('b2', (40, 66)), ('r0', (60, 40)), ('r2', (62, 62))]: d.mv(pid, tg + 1.0, tg + 2.4, ps)
t = d.pas(b2, tg + 1.2, rec(d, 'r2', tg + 2.4), 1.2); t = d.pas(b2, t + 0.3, rec(d, 'r0', t + 1.1))
fp = [(0, 'Två lag med nummer', 'Tränaren ropar vilket eller vilka nummer som spelar.'),
      (1.0, '”Tvåor!” – in och spela', 'Tills det blir mål eller bollen går ur spel.'),
      (2.6, 'Titta upp – vilket mål är ledigt?', 'Spelvändning utnyttjar den fria ytan.'),
      (tg + 0.8, '”Ettor och treor!”', 'Driv genom konmålen – båda riktningarna gäller.')]
finish(d, 'svb140353', 'futsal-nummerspel-u7-u8-svb140353', ['Futsal – Nummerspel', 'U7–U8'], 'Yta ca 15 × 8 m · Konmål i båda ändar · Två lag med nummer',
       fp, 'SPELUPPBYGGNAD', [('box', 12, 10, 88, 90)] + [('cone', x + dx, y) for x in (32, 68) for y in (10, 90) for dx in (-5, 5)],
       [lab(1.0, 2.4, (78, 92), '”2!”'), lab(tg, tg + 1.4, (66, 82), 'MÅL'), lab(tg + 0.8, tg + 2.4, (74, 92), '”1 och 3!”')])

# ============ svb140478 Futsal – Doppboll (U7+) ============
# Handbollskast, studs i golvet före varje passning, inte springa med bollen, mål = kasta till lagkamrat i målområdet.
d = Drill()
BP = [(30, 72), (70, 74), (50, 56)]; RP = [(36, 40), (64, 42), (50, 28)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b0', 0)); ex = []
def dopp(src, dst, t, fly=0.8):
    sx, sy = d.pos(src); dx, dy = rec(d, dst, t + fly); mx, my = (sx + dx) / 2, (sy + dy) / 2
    t1 = d.pas(b, t, (mx, my), fly / 2); ex.append(lab(t1 - 0.1, t1 + 0.5, (mx, my - 5), 'DOPP')); return d.pas(b, t1, rec(d, dst, t + fly), fly / 2)
d.mv('b2', 0.4, 1.4, (52, 48)); t = dopp('b0', 'b2', 0.6)
d.mv('b1', t - 0.6, t + 0.6, (72, 40)); t = dopp('b2', 'b1', t + 0.5)
d.mv('r0', t - 0.4, t + 0.8, (60, 30)); tw = win(d, b, 'r0', 'b1', t + 1.4, 0.0) if False else None
d.mv('b0', t, t + 1.2, (40, 26)); tl = t + 0.5
d.mv('r1', tl - 0.6, tl + 0.4, (58, 30)); t2 = d.pas(b, tl, (60, 31), 0.5); d.carry(b, 'r1', t2, t2 + 0.4)             # röd bryter passningen
d.mv('r2', t2, t2 + 1.4, (50, 80)); t3 = dopp('r1', 'r2', t2 + 0.6, 1.0)                                               # snabb omställning – kast till målområdet
fp = [(0, 'Två lag – kasta till varandra', 'Handbollskast. Fånga med båda händerna, kroppen bakom bollen.'),
      (0.6, 'Doppa bollen i golvet före varje passning', 'Inte springa med bollen.'),
      (tl - 0.3, 'Försvaret bryter passningen', 'Får inte slå bollen ur händerna.'),
      (t2 + 0.4, 'Ställ om – kasta till lagkamrat i målområdet', 'Rörelse och spelbarhet.')]
finish(d, 'svb140478', 'futsal-doppboll-u7-svb140478', ['Futsal – Doppboll', 'U7+'], 'Yta ca 18 × 12 m · Målområde i varje ände',
       fp, 'SPELUPPBYGGNAD', [('box', 12, 6, 88, 94), ('zone', 30, 6, 70, 18, (240, 210, 90), 'MÅLOMRÅDE'), ('zone', 30, 82, 70, 94, (240, 210, 90), 'MÅLOMRÅDE')],
       ex + [lab(t2, t2 + 1.0, (66, 24), 'BRUTEN'), lab(t3, t3 + 1.6, (64, 86), 'MÅL!')])

# ============ Trappan (två versioner) ============
TRAPPA = ['3 MOT 3', '3 MOT 2', '3 MOT 1', '3 MOT 2', '3 MOT 3', '2 MOT 3', '1 MOT 3', '2 MOT 3', '3 MOT 3']
def trappan(id_, slug, title, setup, caps, shapes):
    d = Drill()
    BP = [(30, 66), (70, 66), (50, 76)]; RP = [(34, 36), (66, 36), (50, 26)]; OUT_B = [(6, 60), (6, 70), (6, 80)]; OUT_R = [(94, 20), (94, 30), (94, 40)]
    team(d, 'b', B, BP); team(d, 'r', R, RP)
    b = d.newball(rec(d, 'b2', 0)); S = 1.5; ex = []
    for i, txt in enumerate(TRAPPA): ex.append(lab(0.3 + i * S, 0.3 + (i + 1) * S, (50, 96), txt))
    # steg 1–3: röda går ut, blått i överläge spelar och gör mål
    d.mv('r2', 0.3 + S - 0.3, 0.3 + S + 1.3, OUT_R[2]); d.mv('r1', 0.3 + 2 * S - 0.3, 0.3 + 2 * S + 1.3, OUT_R[1])
    t = chain(d, b, 0.5, ['b0', 'b1', 'b2', 'b0'], 0.25); t = drive(d, b, 'b0', t, (44, 16), 18); tg = d.pas(b, t, (50, 7), 0.4); hide(d, b, tg + 0.3)
    d.mv('r0', 0.5, tg, (42, 26))
    # steg 4–5: röda tillbaka in
    d.mv('r1', 0.3 + 3 * S - 0.3, 0.3 + 3 * S + 1.3, RP[1]); d.mv('r2', 0.3 + 4 * S - 0.3, 0.3 + 4 * S + 1.3, RP[2])
    # steg 6–7: blåa går ut, rött i överläge
    d.mv('b2', 0.3 + 5 * S - 0.3, 0.3 + 5 * S + 1.3, OUT_B[2]); d.mv('b1', 0.3 + 6 * S - 0.3, 0.3 + 6 * S + 1.3, OUT_B[1])
    b2 = d.newball((200, 200)); t0 = 0.3 + 5 * S; show(d, b2, t0, rec(d, 'r2', t0))
    t = chain(d, b2, t0 + 0.2, ['r1', 'r0', 'r1'], 0.3); d.mv('b0', t0, t, (54, 58)); t = drive(d, b2, 'r1', t, (60, 80), 16)
    d.mv('b1', 0.3 + 7 * S - 0.3, 0.3 + 7 * S + 1.3, BP[1]); d.mv('b2', 0.3 + 8 * S - 0.3, 0.3 + 8 * S + 1.3, BP[2])
    tg2 = d.pas(b2, max(t, 0.3 + 7 * S), (50, 93), 0.5); hide(d, b2, tg2 + 0.3)
    fp = [(0, *caps[0]), (0.3 + S, *caps[1]), (0.3 + 5 * S, *caps[2]), (0.3 + 8 * S, *caps[3])]
    finish(d, id_, slug, title, setup, fp, 'SPELUPPBYGGNAD', shapes, ex + [lab(tg, tg + 1.2, (50, 16), 'MÅL'), lab(tg2, tg2 + 1.2, (50, 84), 'MÅL')], target=15.5)
    C[-1]['_stuck'] = False

trappan('svb45133', 'trappan-3v3-svb45133', ['Trappan', 'Spelform 3 mot 3'], 'Ca 6 spelare · Yta 15 × 12 m · Två små mål',
        [('Tre mot tre – antalet byts var halvminut', '3v3 · 3v2 · 3v1 · 3v2 · 3v3 · 2v3 · 1v3 · 2v3 · 3v3'),
         ('Överläge: passera med bollen', 'Driv, vänd, utmana, finta och dribbla.'),
         ('Underläge: bryt och ta tillbaka', 'Driv bort från motståndaren när du vunnit bollen.'),
         ('Upprepa två gånger', 'Låt olika spelare vara på planen i underläget.')],
        [('box', 14, 8, 86, 92), ('smallgoal', 50, 8), ('smallgoal', 50, 92)])

trappan('svb140451', 'futsal-trappan-u7-u12-svb140451', ['Futsal – Trappan', 'U7–U12'], 'Ca 6 spelare · Yta 15 × 12 m · Konmål eller småmål',
        [('Tre mot tre – antalet byts var halvminut', '3v3 · 3v2 · 3v1 · 3v2 · 3v3 · 2v3 · 1v3 · 2v3 · 3v3'),
         ('Överläge offensivt: använd hela planen', 'Överläge defensivt: pressa tillsammans.'),
         ('Underläge defensivt: styr och fördröj', 'Underläge offensivt: utmana och var kreativa.'),
         ('Upprepa två gånger', 'Olika spelare i underläget varje gång.')],
        [('box', 14, 8, 86, 92), ('cone', 44, 8), ('cone', 56, 8), ('cone', 44, 92), ('cone', 56, 92)])

# ============ svb140356 Futsal – Spel mot många mål (U7–U10) ============
d = Drill()
KG = [(30, 26), (70, 22), (50, 46), (24, 62), (76, 58), (50, 80)]
BP = [(18, 40), (40, 70), (62, 36)]; RP = [(82, 40), (60, 70), (36, 34)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
balls = [d.newball(rec(d, f'{tm}{k}', 0)) for tm in 'br' for k in range(3)]
route = {('b', 0): [0, 2, 4], ('b', 1): [3, 5, 2], ('b', 2): [1, 4, 5], ('r', 0): [4, 1, 0], ('r', 1): [5, 3, 0], ('r', 2): [0, 3, 2]}
T1 = 6.0
for (tm, k), gs in route.items():
    pid = f'{tm}{k}'; bb = balls[(0 if tm == 'b' else 3) + k]; t = 0.4 + 0.15 * k
    for gi in gs:
        gx, gy = KG[gi]; t = drive(d, bb, pid, t, (gx + (2 if k % 2 else -2), gy), 15)
    d.mv(pid, t, T1, d.pos(pid)); d.carry(bb, pid, t, T1)
for i, bb in enumerate(balls):
    if i: tt = d.pas(bb, T1 + 0.2, (4, 20 + 12 * i), 0.8); hide(d, bb, tt + 0.1)   # bollarna läggs åt sidan
GB = [(30, 70), (70, 70), (50, 56)]; GR = [(34, 34), (66, 34), (50, 24)]
for k in range(3): d.mv(f'b{k}', T1 + 0.2, T1 + 1.6, GB[k]); d.mv(f'r{k}', T1 + 0.2, T1 + 1.6, GR[k])
b = balls[0]; d.carry(b, 'b0', T1, T1 + 1.6)
t = d.pas(b, T1 + 1.8, rec(d, 'b2', T1 + 2.6)); d.mv('r2', T1 + 1.8, t, (52, 50)); t = drive(d, b, 'b2', t, (62, 52), 12)
t = drive(d, b, 'b2', t, (74, 58), 14); tg = t; d.carry(b, 'b2', tg, tg + 0.4)
fp = [(0, 'Alla har varsin boll', 'Driv genom så många konmål som möjligt.'),
      (2.0, 'Titta upp – hitta fria ytor och tomma mål', 'Driv, finta och ändra riktning.'),
      (T1 + 0.2, 'Nu spelar lagen mot varandra', 'Mål genom att driva igenom valfritt konmål.'),
      (tg - 0.6, 'Försvaret: pressa och bryt', 'Ställ om snabbt till en fri yta eller ett tomt mål.')]
finish(d, 'svb140356', 'futsal-spel-mot-manga-mal-u7-u10-svb140356', ['Futsal – Spel mot många mål', 'U7–U10'], 'Ca 6 spelare · Yta ca 15 × 8 m · Många konmål',
       fp, 'SPELUPPBYGGNAD', [('box', 10, 10, 90, 90)] + [('cone', x + dx, y) for x, y in KG for dx in (-3.5, 3.5)], [lab(tg, tg + 1.4, (74, 50), 'MÅL')])
C[-1]['_stuck'] = False

# ============ svb140354 Futsal – Spel mot två mål (U7–U8) ============
d = Drill()
BP = [(30, 70), (70, 70), (50, 56)]; RP = [(34, 36), (66, 36), (50, 46)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b0', 0))
d.mv('r0', 0.4, 1.6, (30, 28)); t = drive(d, b, 'b0', 0.4, (30, 52), 12)                                         # vänstra målet stängt
d.mv('b2', 0.6, t, (50, 42)); t = d.pas(b, t + 0.2, rec(d, 'b2', t + 0.9)); d.mv('r2', t - 0.6, t + 0.4, (46, 36))
d.mv('b1', t - 0.8, t + 0.4, (72, 34)); t = d.pas(b, t + 0.2, rec(d, 'b1', t + 1.0)); tsw = t                        # vänd spelet
t = drive(d, b, 'b1', t, (70, 14), 16); tg = t; d.carry(b, 'b1', tg, tg + 0.3); d.mv('r1', tsw - 0.4, tg, (60, 26))
hide(d, b, tg + 0.5); b2 = d.newball((200, 200)); show(d, b2, tg + 0.9, rec(d, 'r1', tg + 0.9))
t = drive(d, b2, 'r1', tg + 1.0, (58, 50), 14); tw = win(d, b2, 'b2', 'r1', t + 0.4, 0.8); t = drive(d, b2, 'b2', tw, (38, 22), 16)
fp = [(0, 'Tre mot tre – två mål på varje sida', 'Driv, finta och passa förbi motspelarna.'),
      (1.6, 'Titta upp – vilket mål är bäst?', ''),
      (tsw - 0.4, 'Vänd på spelet till det fria målet', ''),
      (tw - 0.2, 'Försvaret erövrar bollen – ställ om', 'Progression: byt spelriktning – bredare och kortare plan.')]
finish(d, 'svb140354', 'futsal-spel-mot-tva-mal-u7-u8-svb140354', ['Futsal – Spel mot två mål', 'U7–U8'], 'Ca 6 spelare · Yta ca 15 × 8 m · Två konmål på varje sida',
       fp, 'SPELUPPBYGGNAD', [('box', 14, 10, 86, 90)] + [('cone', x + dx, y) for x in (30, 70) for y in (10, 90) for dx in (-5, 5)],
       [lab(tsw, tsw + 1.2, (78, 44), 'VÄND'), lab(tg, tg + 1.4, (70, 20), 'MÅL'), lab(tw, tw + 1.2, (64, 46), 'BOLLVINST')])

if __name__ == '__main__': render(C, sys.argv)
