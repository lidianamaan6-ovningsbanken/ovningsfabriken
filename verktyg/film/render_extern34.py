# Externa övningar, omgång 34 (tolv st). Regel: först d.mv, sedan d.carry; först mottagarens rörelse, sedan passningen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e9', __file__.replace('render_extern34.py', 'render_extern9.py'))
e9 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e9); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e9.finish, e9.rec, e9.chain, e9.wander, e9.counter, e9.arrivals
lab, hide, show, team, boxes, drive, shoot = e9.lab, e9.hide, e9.show, e9.team, e9.boxes, e9.drive, e9.shoot
factor, swap_color, stand, countdown, countup, win = e9.factor, e9.swap_color, e9.stand, e9.countdown, e9.countup, e9.win
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'

# ============ wj05 Spelarna först – lekmatch utan coachning ============
d = Drill(); d.p('v', 'L', T_COL, (96, 50))
BP = [(30, 66), (66, 64), (48, 48)]; RP = [(34, 36), (62, 34), (52, 56)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b0', 0))
t = d.pas(b, 0.4, rec(d, 'b2', 1.2)); t = drive(d, b, 'b2', t, (40, 20), 16); d.mv('r2', 1.6, t, (42, 26))
tf = t + 0.2; stand(d, 'b2', t, tf + 1.0); d.carry(b, 'b2', t, tf + 1.0)                                       # frispark – direkt
t = d.pas(b, tf + 1.2, rec(d, 'b1', tf + 2.0)); t = drive(d, b, 'b1', t, (58, 14), 16); tg = d.pas(b, t + 0.1, (50, 4), 0.4); hide(d, b, tg + 0.3)
b2 = d.newball((200, 200)); show(d, b2, tg + 0.8, (51.8, 92))                                                # inspark i stället för inkast
d.mv('r1', tg - 1.8, tg + 0.8, (50, 94)); t = d.pas(b2, tg + 1.0, rec(d, 'r0', tg + 2.0), 1.0)
fp = [(0, '3 mot 3 eller 4 mot 4', 'En vuxen är spelledare, inte domare.'),
      (tf - 0.2, 'Alla frisparkar direkta', 'Inga straffar.'),
      (tg - 0.4, 'Mål – vuxna applåderar bara', 'Ingen coachning från sidan.'),
      (tg + 0.8, 'Inspark i stället för inkast', 'Fria byten, alla spelar lika mycket.')]
finish(d, 'wj05', 'spelarna-forst-lekmatch-utan-coachning', ['Spelarna först', 'Lekmatch utan coachning'], 'Två små planer · Småmål',
       fp, 'SMÅLAGSSPEL', [('box', 14, 4, 86, 96), ('smallgoal', 50, 4), ('smallgoal', 50, 96)], [lab(tg, tg + 1.6, (78, 44), 'APPLÅD!')])

# ============ wj06 8-mannamatch med rullande målvakt ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96))
BP = [(20, 76), (40, 80), (60, 80), (80, 76), (34, 58), (66, 58), (50, 44)]; RP = [(20, 24), (40, 20), (60, 20), (80, 24), (34, 42), (66, 42), (50, 58)]
team(d, 'b', B, BP); team(d, 'r', R, RP); d.p('bs', '', B, (98, 52))
b = d.newball(rec(d, 'b1', 0))
t = chain(d, b, 0.4, ['b4', 'b6'], 0.3); d.mv('b1', t - 1.2, t + 1.0, (42, 24)); t = d.pas(b, t + 0.2, rec(d, 'b1', t + 1.2))   # backen går upp
tg = shoot(d, b, t + 0.05, (44, 1)); hide(d, b, tg + 0.3)
d.mv('bs', tg + 0.4, tg + 2.0, (80, 60)); d.mv('b3', tg + 0.4, tg + 2.4, (98, 46))                            # fritt byte
fp = [(0, 'Sju utespelare och en målvakt', 'JFA spelar U12 8 mot 8.'),
      (2.0, 'Backen går upp i anfallet', ''),
      (tg - 0.4, 'Mål av en back räknas dubbelt', 'Eller om en back assisterat.'),
      (tg + 0.4, 'Fria byten när som helst', 'Målvakten byts varje period.')]
finish(d, 'wj06', '8-mannamatch-med-rullande-malvakt', ['8-mannamatch', 'Med rullande målvakt'], 'Halvplan · Mål 5 × 2 m · Bytesszon i mitten',
       fp, 'SMÅLAGSSPEL', [('zone', 94, 42, 100, 58, (240, 210, 90), '')], [lab(tg, tg + 1.8, (44, 14), 'x2')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ wj07 Kraque-utmaningen – nivå för nivå ============
d = Drill()
ST = [(28, 32), (72, 32), (28, 70), (72, 70)]; LV = ['NIVÅ 1: STUDS OCH FÅNGA', 'NIVÅ 2: FOT–FOT–FÅNGA', 'NIVÅ 3: TIO I RAD']
for k, ps in enumerate(ST): d.p(f'p{k}', '', B, ps)
for k, (x, y) in enumerate(ST):
    bb = d.newball((x + 1.8, y - 4)); tr = d.balls[bb]; t = 0.4 + 0.2 * k
    for lvl, n in enumerate([1, 2, 4]):
        for rep in range(3 if lvl < 2 else 1):
            for j in range(n): tr += [(t, (x + 1.8, y - 4)), (t + 0.25, (x + 1.8, y - 9)), (t + 0.5, (x + 1.8, y - 4))]; t += 0.5
            t += 0.3
fp = [(0, 'Varje spelare på sin nivå', 'En boll per spelare.'),
      (2.0, 'Klarar du tre gånger – gå upp en nivå', ''),
      (5.4, 'Fot–fot–fånga', ''),
      (10.0, 'Markera din nivå på tavlan', 'Inspirerat av JFA Challenge Game.')]
finish(d, 'wj07', 'kraque-utmaningen-niva-for-niva', ['Kraque-utmaningen', 'Nivå för nivå'], 'En boll per spelare',
       fp, 'TEKNIK', [], [lab(0.4, 2.6, (50, 50), LV[0]), lab(2.6, 7.6, (50, 50), LV[1]), lab(7.6, 12.0, (50, 50), LV[2])])
C[-1]['_stuck'] = True

# ============ wm01 Sulrondo – futsalfötter ============
d = Drill()
SQ = [(50, 24), (76, 50), (50, 76), (24, 50)]
for k, ps in enumerate(SQ): d.p(f'p{k}', '', B, ps)
team(d, 'f', R, [(44, 46), (56, 54)], ['', ''])
b = d.newball(rec(d, 'p0', 0)); t = 0.4; h = 0
for rep, nk in enumerate([1, 2, 3, 0, 2, 1, 0, 3]):
    d.mv('f0', t, t + 0.7, ((SQ[h][0] + SQ[nk][0]) / 2 * 0.5 + 25, (SQ[h][1] + SQ[nk][1]) / 2 * 0.5 + 25))
    t = d.pas(b, t + 0.1, rec(d, f'p{nk}', t + 0.8)); d.carry(b, f'p{nk}', t, t + 0.4); t += 0.45; h = nk       # mottagning med sulan
tw = win(d, b, 'f1', f'p{h}', t + 0.4, 0.5)
d.mv('f1', tw + 0.3, tw + 1.4, SQ[h]); d.mv(f'p{h}', tw + 0.3, tw + 1.4, (52, 50))                             # byter med den som tappade
wander(d, 'f0', t, 17.9, (42, 42, 58, 58), 11800, 1.4)
fp = [(0, 'Fyra mot två', 'Ruta 8 × 8 m.'),
      (1.4, 'Mottagning med sulan', 'Max tre touch.'),
      (5.0, 'Tät teknik under press', 'Futsalkulturen i Marocko och arabvärlden.'),
      (tw - 0.2, 'Bollvinst – byt med den som tappade', '')]
finish(d, 'wm01', 'sulrondo-futsalfotter', ['Sulrondo', 'Futsalfötter'], 'Ruta 8 × 8 m · Fyra mot två',
       fp, 'RONDO', [('box', 18, 18, 82, 82)], [lab(1.4, 5.0, (50, 90), 'SULAN')])

# ============ wm02 Teknik i trötthet ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
CN = [(30, 84), (36, 76), (30, 68), (36, 60)]
for tm, x, col in (('b', 34, B), ('r', 66, R)):
    for k in range(2): d.p(f'{tm}{k}', '', col, (x - 4 + 8 * k, 94))
for tm, x, col in (('b', 34, B), ('r', 66, R)):
    for k in range(2):
        pid = f'{tm}{k}'; bb = d.newball(rec(d, pid, 0)); t = 0.4 + 5.4 * k + (0.3 if tm == 'r' else 0)
        if k: d.mv(pid, t - 1.4, t, (x, 92))
        d.carry(bb, pid, 0, t)
        pts = [(cx - 34 + x + (4 if i % 2 == 0 else -4), cy) for i, (cx, cy) in enumerate(CN)] + [(x, 52)]       # fint och vändning i konbanan
        t1 = d.path(pid, t, pts, 1.2); d.carry(bb, pid, t, t1)
        d.mv(pid, t1, t1 + 1.0, (x + (8 if x < 50 else -8), 26)); d.carry(bb, pid, t1, t1 + 1.0); t1 += 1.0       # sprint med boll
        tg = shoot(d, bb, t1 + 0.1, (46 if x < 50 else 54, 1)); hide(d, bb, tg + 0.3)
        d.mv(pid, tg + 0.2, tg + 3.0, (x + (-10 if x < 50 else 10) + (-6 * k if x < 50 else 6 * k), 96))                                         # jogg tillbaka
fp = [(0, 'Två led tävlar mot varandra', ''),
      (1.0, 'Fint och vändning i konbanan', ''),
      (3.0, 'Sprint med boll – avslut', 'Poäng för mål och snabbast tid.'),
      (7.0, '6–8 repetitioner per spelare', 'Teknik och fysik tillsammans.')]
finish(d, 'wm02', 'teknik-i-trotthet', ['Teknik i', 'trötthet'], 'Konbana 10 m · Sprint 20 m · Mål med målvakt',
       fp, 'AVSLUT', [('cone', c[0], c[1]) for c in CN] + [('cone', c[0] + 32, c[1]) for c in CN])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ wm03 Gatufotboll – vinnaren stannar ============
d = Drill()
BP = [(34, 66), (64, 64), (48, 50)]; RP = [(36, 34), (62, 32), (52, 56)]
team(d, 'b', B, BP); team(d, 'r', R, RP); team(d, 'w', WHITE, [(96, 40), (96, 50), (96, 60)], ['', '', ''])
b = d.newball(rec(d, 'b0', 0))
t = d.pas(b, 0.4, rec(d, 'b2', 1.2)); t = d.pas(b, t + 0.3, rec(d, 'b1', t + 1.0)); t = drive(d, b, 'b1', t, (58, 30), 16)   # mål bara från anfallshalvan
tg = d.pas(b, t + 0.1, (50, 8), 0.5); hide(d, b, tg + 0.3)
for k, ps in enumerate([(96, 72), (96, 80), (96, 88)]): d.mv(f'r{k}', tg + 0.3, tg + 2.6, ps)                    # vinnaren stannar, nytt lag in
for k, ps in enumerate([(36, 34), (62, 32), (52, 56)]): d.mv(f'w{k}', tg + 0.3, tg + 2.6, ps)
b2 = d.newball((200, 200)); show(d, b2, tg + 2.7, rec(d, 'w2', tg + 2.7))
t = d.pas(b2, tg + 2.9, rec(d, 'w0', tg + 3.6)); t = d.pas(b2, t + 0.3, rec(d, 'w1', t + 1.0))
fp = [(0, 'Tre mot tre, fler lag väntar', 'Mål av två stenar eller koner.'),
      (2.4, 'Mål bara från anfallshalvan', 'Ingen målvakt.'),
      (tg + 0.3, 'Vinnaren stannar – nytt lag in', 'Först till tre mål.'),
      (tg + 3.0, 'Variant: vägg-väggspel', 'Spela på bänkar eller väggar.')]
finish(d, 'wm03', 'gatufotboll-vinnaren-stannar', ['Gatufotboll', 'Vinnaren stannar'], 'Liten yta 15 × 25 m · Mål av stenar',
       fp, 'SMÅLAGSSPEL', [('box', 18, 6, 82, 94), ('line', [(18, 50), (82, 50)]), ('cone', 45, 6), ('cone', 55, 6), ('cone', 45, 94), ('cone', 55, 94)])

# ============ ct01 Korridorkaos – två bollar ============
d = Drill()
LX = [(6, 34), (34, 66), (66, 94)]
for k, (x1, x2) in enumerate(LX): d.p(f'b{k}', '', B, ((x1 + x2) / 2 - 5, 62)); d.p(f'r{k}', '', R, ((x1 + x2) / 2 + 5, 38))
for k, (x1, x2) in enumerate(LX):
    wander(d, f'b{k}', 0, 17.9, (x1 + 4, 20, x2 - 4, 84), 11900 + k, 1.6); wander(d, f'r{k}', 0, 17.9, (x1 + 4, 16, x2 - 4, 80), 11910 + k, 1.6)
b1 = d.newball(rec(d, 'b0', 0)); b2 = d.newball(rec(d, 'r2', 0))
t = d.pas(b1, 0.4, rec(d, 'b1', 1.4)); t = d.pas(b1, t + 0.3, rec(d, 'b2', t + 1.4)); t = d.pas(b1, t + 0.3, rec(d, 'b1', t + 1.4))
t = d.pas(b2, 0.8, rec(d, 'r1', 1.8)); t = d.pas(b2, t + 0.3, rec(d, 'r0', t + 1.4)); t = d.pas(b2, t + 0.3, rec(d, 'r1', t + 1.4))
fp = [(0, 'Tre mot tre, två bollar samtidigt', 'Varje spelare äger sin korridor.'),
      (2.0, 'Ingen får lämna sin korridor', ''),
      (6.0, 'Mål räknas bara om den andra bollen', 'Inte ligger på egen planhalva.'),
      (11.0, 'Byt korridor varje omgång', 'Omgångar på tre minuter.')]
finish(d, 'ct01', 'korridorkaos-tva-bollar', ['Korridorkaos', 'Två bollar'], 'Yta 20 × 30 m i tre korridorer · Fyra minimål',
       fp, 'SMÅLAGSSPEL', [('box', 6, 6, 94, 94), ('line', [(34, 6), (34, 94)]), ('line', [(66, 6), (66, 94)]), ('line', [(6, 50), (94, 50)]),
                          ('smallgoal', 30, 6), ('smallgoal', 70, 6), ('smallgoal', 30, 94), ('smallgoal', 70, 94)])

# ============ ct02 Försvara målet – 30-sekundersregeln ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96)); d.p('t', 'T', T_COL, (97, 50))
BP = [(30, 66), (70, 64), (44, 48), (58, 32), (50, 78)]; RP = [(34, 36), (66, 34), (52, 54), (42, 22), (60, 70)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b2', 'b3'], 0.3); tg = shoot(d, b, t + 0.1, (46, 1)); hide(d, b, tg + 0.3)
b2 = d.newball((200, 200)); show(d, b2, tg + 0.8, rec(d, 'mvr', tg + 0.8))
for k, ps in enumerate([(30, 76), (70, 74), (44, 66), (58, 60), (50, 84)]): d.mv(f'b{k}', tg, tg + 2.0, ps)        # försvara målet
t = d.pas(b2, tg + 1.0, rec(d, 'r0', tg + 2.0), 1.0); t = chain(d, b2, t, ['r2', 'r4'], 0.3)
tw = win(d, b2, 'b4', 'r4', t + 0.4, 0.5); d.mv('b4', tw, tw + 1.0, (50, 70)); d.carry(b2, 'b4', tw, tw + 1.0)
fp = [(0, 'Fem mot fem med målvakter', ''),
      (tg - 0.3, 'Mål – men inte godkänt än', ''),
      (tg + 0.8, 'Försvara i 30 sekunder', 'Tränaren räknar högt.'),
      (tw - 0.2, 'Inget insläppt – målet godkänt', 'Släpper laget in stryks målet.')]
finish(d, 'ct02', 'forsvara-malet-30-sekundersregeln', ['Försvara målet', '30-sekundersregeln'], 'Plan 30 × 40 m · Två mål med målvakter',
       fp, 'SMÅLAGSSPEL', [], countdown(tg + 0.6, 6, (88, 30), (tw - tg) / 6) + [lab(tw + 0.4, tw + 2.0, (88, 30), 'GODKÄNT')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ ct03 Värdemålet – passningar höjer priset ============
d = Drill()
BP = [(28, 64), (70, 66), (40, 44), (62, 34)]; RP = [(34, 36), (66, 40), (50, 56), (44, 24)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
for k in range(4): wander(d, f'r{k}', 0, 17.9, boxes([RP[k]], 4)[0], 12000 + k, 1.6)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b2', 'b1', 'b3', 'b2'], 0.3); cnt = arrivals(d, b)[:4]
t = drive(d, b, 'b2', t, (46, 14), 16); tg = d.pas(b, t + 0.1, (50, 4), 0.4); hide(d, b, tg + 0.3)
fp = [(0, 'Fyra mot fyra', 'Laget räknar högt.'),
      (cnt[1], 'Varje passning höjer priset', 'Max 6 poäng.'),
      (tg - 0.4, 'Mål efter fyra passningar: 4 poäng', ''),
      (tg + 0.4, 'Bollförlust nollställer räkningen', '')]
finish(d, 'ct03', 'vardemalet-passningar-hojer-priset', ['Värdemålet', 'Passningar höjer priset'], 'Yta 20 × 25 m · Småmål',
       fp, 'SMÅLAGSSPEL', [('box', 12, 4, 88, 96), ('smallgoal', 50, 4), ('smallgoal', 50, 96)], counter(cnt, pos=(84, 50), last=None) + [lab(tg, tg + 1.8, (50, 14), '+4')])

# ============ ct04 Tajma löpningen – bakom backlinjen ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
d.p('p', 'P', WHITE, (50, 72)); team(d, 'a', B, [(40, 40), (60, 40)])
b = d.newball(rec(d, 'p', 0))
d.mv('a0', 0.4, 1.6, (40, 32)); t = d.pas(b, 1.4, (42, 30), 0.9); toff = t                                   # för tidigt – offside
hide(d, b, toff + 0.4); d.mv('a0', toff, toff + 1.6, (40, 40))
b2 = d.newball((200, 200)); show(d, b2, toff + 1.0, rec(d, 'p', toff + 1.0))
d.mv('a1', toff + 1.4, toff + 2.6, (58, 42)); d.mv('a0', toff + 1.4, toff + 2.2, (44, 46))                       # den ena möter, den andra går i djupet
t = d.pas(b2, toff + 2.2, rec(d, 'a1', toff + 3.4), 1.0); d.mv('a1', toff + 2.6, t, (56, 20)); d.carry(b2, 'a1', t, t + 0.3)
tg = shoot(d, b2, t + 0.35, (46, 1))
fp = [(0, 'Konlinjen är backlinjen', 'Ca 25 m från mål.'),
      (toff - 0.6, 'Förbi konerna när passningen slås = offside', 'Nästa på tur.'),
      (toff + 2.2, 'Rätt tajmad löpning', 'En går i djupet, en möter.'),
      (tg - 0.3, 'Avslut', '')]
finish(d, 'ct04', 'tajma-lopningen-bakom-backlinjen', ['Tajma löpningen', 'Bakom backlinjen'], 'Konlinje ca 25 m från mål · Målvakt',
       fp, 'AVSLUT', [('cone', x, 38) for x in range(14, 90, 12)], [lab(toff, toff + 1.4, (62, 30), 'OFFSIDE')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ ct05 Vänd och välj rätt mål ============
d = Drill(); d.p('t', 'T', T_COL, (50, 90)); d.p('s', '', B, (50, 62))
GL = [(20, 14), (50, 8), (80, 14)]; GC = ['redcone', 'yellowcone', 'cone']; NM = ['”RÖD!”', '”GUL!”', '”ORANGE!”']
t = 0.4; ex = []
for rep, gi in enumerate([1, 0, 2]):
    bb = d.newball(rec(d, 't', t)); t1 = d.pas(bb, t, rec(d, 's', t + 0.9)); ex.append(lab(t, t + 1.2, (70, 76), NM[gi]))
    gx, gy = GL[gi]; d.mv('s', t1, t1 + 0.5, (50 + (gx - 50) * 0.15, 58)); d.carry(bb, 's', t1, t1 + 0.5)     # vänd på första touchen
    tg = d.pas(bb, t1 + 0.6, (gx, gy + 1), 0.6); hide(d, bb, tg + 0.3); t = tg + 0.6
fp = [(0, 'Ryggen mot målen', 'Tre små mål i olika färger.'),
      (0.6, 'Tränaren ropar färgen', 'I samma stund som passningen slås.'),
      (2.0, 'Vänd och avsluta i rätt mål', 'Dubbelt för vändning på första touchen.'),
      (t - 1.0, 'Nästa färg', '')]
finish(d, 'ct05', 'vand-och-valj-ratt-mal', ['Vänd och välj', 'rätt mål'], 'Tre små mål i olika färger 12–16 m bort',
       fp, 'AVSLUT', [(GC[i], x + dx, y) for i, (x, y) in enumerate(GL) for dx in (-4, 4)], ex)

# ============ ct06 Tredje man till kant och inlägg ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
d.p('bk', 'B', B, (50, 84)); d.p('an', 'A', B, (50, 46)); d.p('mf', 'M', B, (36, 64)); d.p('yt', 'Y', B, (88, 52))
b = d.newball(rec(d, 'bk', 0))
t = d.pas(b, 0.4, rec(d, 'an', 1.4)); d.mv('mf', 0.6, t + 0.6, (42, 52)); t = d.pas(b, t + 0.1, rec(d, 'mf', t + 0.7))   # lägger av till mittfältaren
t = d.pas(b, t + 0.2, rec(d, 'yt', t + 1.4)); t = drive(d, b, 'yt', t, (88, 16), 18)                           # ut till kanten
d.mv('an', t - 2.4, t + 0.4, (56, 10)); d.mv('mf', t - 2.4, t + 0.6, (42, 14))                                  # nära och bortre stolpen
t = d.pas(b, t + 0.1, rec(d, 'mf', t + 1.1), 1.0); tg = shoot(d, b, t + 0.05, (44, 1))
fp = [(0, 'Backen spelar in till anfallaren', ''),
      (1.6, 'Tredje man – mittfältaren', 'Anfallaren lägger av.'),
      (3.4, 'Ut till kanten – inlägg', ''),
      (tg - 0.6, 'Nära och bortre stolpen', 'Rotera positioner.')]
finish(d, 'ct06', 'tredje-man-till-kant-och-inlagg', ['Tredje man', 'Till kant och inlägg'], 'Planhalva · Mål med målvakt',
       fp, 'AVSLUT', [])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

if __name__ == '__main__': render(C, sys.argv)
