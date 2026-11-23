# Externa övningar, omgång 8 (tolv st). Regel: först d.mv, sedan d.carry; hide före show.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e4', __file__.replace('render_extern8.py', 'render_extern4.py'))
e4 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e4); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e4.finish, e4.rec, e4.chain, e4.wander, e4.counter, e4.arrivals
lab, hide, show, team, boxes, drive, shoot = e4.lab, e4.hide, e4.show, e4.team, e4.boxes, e4.drive, e4.shoot
factor, swap_color, stand = e4.factor, e4.swap_color, e4.stand
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'
def countdown(t0, n, pos, step=1.0): return [lab(t0 + i * step, t0 + (i + 1) * step, pos, str(n - i)) for i in range(n)]
def countup(t0, n, pos, step=1.0): return [lab(t0 + i * step, t0 + (i + 1) * step, pos, str(i + 1)) for i in range(n)]

# ============ fs5 Frispark – överlämning och skott ============
d = Drill(); d.p('mv', 'MV', R, (50, 5))
team(d, 'm', R, [(45, 30), (50, 30), (55, 30)], ['M', 'M', 'M'])
d.p('l', 'L', B, (48, 42)); d.p('s', 'S', B, (44, 50)); team(d, 'r', B, [(34, 40), (64, 40)])
b = d.newball((51, 41))
t = d.pas(b, 1.2, (60, 41), 0.6)                                                      # i sidled ur murens skugga
d.mv('s', 0.9, t + 0.1, (58, 44)); tg = d.pas(b, t + 0.1, (52, 5), 0.5)                # skott på första touchen
d.mv('mv', tg - 0.4, tg, (52, 5))
d.mv('r0', t, tg + 0.7, (42, 14)); d.mv('r1', t, tg + 0.7, (60, 14))
t = d.pas(b, tg + 0.05, rec(d, 'r0', tg + 0.6), 0.55); tr = shoot(d, b, t + 0.05, (44, 1))   # retur – löparen följer in
for pid, ps in [('l', (48, 42)), ('s', (44, 50)), ('r0', (34, 40)), ('r1', (64, 40))]: d.mv(pid, tr + 0.4, tr + 2.6, ps)
d.mv('mv', tr, tr + 1.0, (50, 5))
b2 = d.newball((200, 200)); show(d, b2, tr + 2.7, (51, 41))
t = d.pas(b2, tr + 3.4, (40, 41), 0.6); d.mv('s', tr + 3.1, t + 0.1, (42, 45)); d.mv('l', tr + 3.4, tr + 4.0, (54, 44))
tg2 = d.pas(b2, t + 0.1, (44, 1), 0.5); d.mv('r0', t, tg2 + 0.6, (40, 14)); d.mv('r1', t, tg2 + 0.6, (56, 12))
fp = [(0, 'Frispark centralt utanför straffområdet', 'Mur på tre. En lägger, en skjuter.'),
      (1.1, 'Rulla bollen i sidled ur murens skugga', 'Skytten skjuter på första touchen.'),
      (tg + 0.1, 'Löparna följer in på returen', 'Två löpare för returer.'),
      (tr + 2.7, 'Samma sak åt andra hållet', 'Variera sidan på överlämningen.')]
finish(d, 'fs5', 'frispark-overlamning-och-skott', ['Frispark', 'Överlämning och skott'], 'Frispark centralt strax utanför straffområdet · Mur på tre · Skytt och läggare',
       fp, 'FAST SITUATION', [])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ fs6 Frisparksförsvar – mur och linje ============
d = Drill(); d.p('mv', 'MV', R, (50, 5))
WP = [(60, 26), (62, 28), (64, 30)]; team(d, 'm', R, WP, ['M', 'M', 'M'])
DP = [(36, 22), (44, 22), (52, 22)]; team(d, 'f', R, DP); AP = [(38, 28), (46, 30), (54, 32)]; team(d, 'a', B, AP)
d.p('h', 'H', B, (72, 38)); d.p('k', 'K', B, (80, 34))
b = d.newball(rec(d, 'h', 0))
tcall = 0.3
for k, ps in enumerate([(40, 10), (48, 8), (54, 12)]): d.mv(f'a{k}', 1.6, 3.0, ps)
for k, ps in enumerate([(38, 10), (46, 8), (52, 10)]): d.mv(f'f{k}', 1.6, 3.0, ps)              # linjen löper med
t = d.pas(b, 2.0, rec(d, 'f1', 3.0), 1.0); tc = d.pas(b, t + 0.05, (40, 40), 0.7); hide(d, b, tc + 0.3)   # inlägg rensas
for k in range(3): d.mv(f'a{k}', tc, tc + 2.0, AP[k]); d.mv(f'f{k}', tc, tc + 2.0, DP[k])
b2 = d.newball((200, 200)); show(d, b2, tc + 2.1, rec(d, 'h', tc + 2.1))
t = d.pas(b2, tc + 2.6, rec(d, 'k', tc + 3.2)); d.mv('k', t, t + 0.8, (72, 26)); d.carry(b2, 'k', t, t + 0.8)   # kort variant
d.mv('f2', t - 0.4, t + 0.8, rec(d, 'k', t + 0.8)); tw = d.pas(b2, t + 0.85, rec(d, 'f2', t + 1.1), 0.3)
d.mv('f2', tw, tw + 1.2, (60, 42)); d.carry(b2, 'f2', tw, tw + 1.2)
fp = [(0, 'Målvakten ropar antalet i muren', 'Och ställer den mot närmaste stolpen.'),
      (1.6, 'Övriga håller linje med löparna', 'Anfallarna väljer skott, inlägg eller kort variant.'),
      (tc - 0.4, 'Rensning: poäng till försvaret', ''),
      (tw - 0.3, 'Kort variant – försvaret vinner bollen', 'Poäng till försvaret.')]
finish(d, 'fs6', 'frisparksforsvar-mur-och-linje', ['Frisparksförsvar', 'Mur och linje'], 'Mur som målvakten ställer upp · Resten i linje med löparna',
       fp, 'FAST SITUATION', [], [lab(tcall, 1.6, (50, 16), '”TRE I MUREN!”'), lab(tc, tc + 1.6, (40, 48), '+1'), lab(tw, tw + 1.6, (60, 50), '+1')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ fs7 Inkast – väggspel och vändning ============
d = Drill(); d.p('k', 'K', B, (2, 66))
team(d, 's', B, [(14, 58), (18, 74)]); d.p('dp', 'D', B, (30, 40)); team(d, 'f', R, [(20, 62), (24, 70)])
b = d.newball((2, 64))
d.mv('s0', 0.4, 1.2, (8, 58)); t = d.pas(b, 0.8, rec(d, 's0', 1.4), 0.6)                         # inkast
d.mv('k', t, t + 0.6, (8, 68)); t = d.pas(b, t + 0.05, rec(d, 'k', t + 0.6), 0.5); p1 = t        # lägger tillbaka på ett touch
d.mv('dp', 0.8, t + 0.8, (30, 30)); d.mv('f0', 0.6, t, (12, 60))
t = d.pas(b, t + 0.2, rec(d, 's1', t + 1.0)); p2 = t; d.mv('s1', p1 - 0.8, p2, (22, 66))
t = d.pas(b, t + 0.2, rec(d, 'dp', t + 1.1)); p3 = t                                              # ut ur ytan
d.mv('f1', p1, p3, (26, 54))
d.mv('dp', p3, p3 + 1.4, (40, 26)); d.carry(b, 'dp', p3, p3 + 1.4)
fp = [(0, 'Inkast på egen planhalva', 'Två erbjuder sig kort och en djupt.'),
      (p1 - 0.8, 'Lägg tillbaka på ett touch', 'Kastaren spelar vidare.'),
      (p2 - 0.3, 'Framåt eller till den djupa', 'Två försvarare stör.'),
      (p3 - 0.2, 'Tre passningar ut ur ytan: 1 poäng', '')]
finish(d, 'fs7', 'inkast-vaggspel-och-vandning', ['Inkast', 'Väggspel och vändning'], 'Inkast på egen planhalva · Två som erbjuder sig och en djupt',
       fp, 'FAST SITUATION', [('zone', 0, 46, 36, 84, (200, 220, 200), 'YTAN')], counter([p1, p2, p3], pos=(20, 90)))

# ============ fs8 Inkastförsvar – stäng mottagaren ============
d = Drill(); d.p('mv', 'MV', R, (50, 4)); d.p('k', 'K', B, (98, 20))
AP = [(86, 16), (84, 28), (76, 22)]; team(d, 'a', B, AP); team(d, 'f', R, [(84, 12), (82, 24), (72, 20)])   # försvararna på goal-side
b = d.newball((98, 18))
d.mv('a1', 0.4, 1.4, (88, 32)); d.mv('f1', 0.5, 1.4, (86, 29))
t = d.pas(b, 1.2, (88, 32), 0.6); d.mv('f1', 1.4, t, (88, 31)); tw = t                             # försvararen vinner bollen
d.carry(b, 'f1', tw, tw + 0.2)
t = d.pas(b, tw + 0.3, rec(d, 'f2', tw + 1.0)); d.mv('f2', tw, tw + 0.8, (70, 28))
t = drive(d, b, 'f2', t, (62, 44), 20); tk = d.pas(b, t + 0.1, (50, 60), 0.8); hide(d, b, tk + 0.3)   # ut till konen
d.mv('a2', tw, tw + 1.6, (68, 34)); d.mv('a1', tw, tw + 1.0, (93, 38))
fp = [(0, 'Motståndarnas inkast nära egen kortlinje', 'Tre anfallare och kastaren mot tre försvarare.'),
      (0.5, 'Markera på goal-side', 'Släpp ingen löpare bakom dig.'),
      (tw - 0.2, 'Bollvinst: 1 poäng', ''),
      (tk - 0.6, 'Ut till konen: 2 poäng', 'Anfallarna får 1 poäng om de tar sig ut ur ytan.')]
finish(d, 'fs8', 'inkastforsvar-stang-mottagaren', ['Inkastförsvar', 'Stäng mottagaren'], 'Motståndarnas inkast nära egen kortlinje',
       fp, 'FAST SITUATION', [('zone', 62, 2, 100, 40, (230, 120, 110), 'YTAN'), ('cone', 50, 60)], [lab(tw, tw + 1.6, (78, 44), '+1'), lab(tk, tk + 1.8, (50, 68), '+2')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ k01 3 mot 2 efter bollvinst ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
AP = [(30, 90), (50, 92), (70, 90)]; team(d, 'a', B, AP); team(d, 'f', R, [(42, 62), (58, 62)])
b = d.newball(rec(d, 'f0', 0))
t = d.pas(b, 0.4, rec(d, 'a1', 1.4)); t0 = t                                                   # försvararna spelar in och följer efter
d.mv('f0', 0.6, 2.4, (44, 54)); d.mv('f1', 0.6, 2.4, (58, 50))
for k, ps in enumerate([(28, 52), (50, 66), (72, 50)]): d.mv(f'a{k}', t0, t0 + 2.4, ps)
d.carry(b, 'a1', t0, t0 + 2.4); t = d.pas(b, t0 + 2.5, rec(d, 'a2', t0 + 3.2))
d.mv('f1', t - 0.6, t + 0.6, (64, 40)); d.mv('f0', t - 0.6, t + 0.8, (52, 36))
d.mv('a2', t, t + 1.0, (70, 30)); d.carry(b, 'a2', t, t + 1.0); t += 1.0
d.mv('a0', t - 2.0, t, (36, 22)); t = d.pas(b, t + 0.1, rec(d, 'a0', t + 0.8)); tg = shoot(d, b, t + 0.05, (44, 1))
fp = [(0, 'Försvararna spelar in bollen', 'Och följer efter. Tre anfallare startar vid mittlinjen.'),
      (t0, 'Åtta sekunder på sig', 'Anfallarna ska avsluta snabbt.'),
      (tg - 0.6, 'Mål inom 8 sekunder: 2 poäng', 'Efter 8 sekunder ger mål 1 poäng.'),
      (tg + 0.6, 'Grupper om fem roterar', 'Nästa grupp startar.')]
finish(d, 'k01', '3-mot-2-efter-bollvinst', ['3 mot 2', 'Efter bollvinst'], 'Halv plan · Mål med målvakt · Tre anfallare vid mittlinjen, två försvarare',
       fp, 'KONTRING', [], countdown(t0, 8, (84, 50), (tg - t0) / 6) + [lab(tg, tg + 2, (44, 16), '+2')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ k02 Fem sekunder till mål 4 mot 4 ============
d = Drill(); d.p('mvr', 'MV', R, (50, 4)); d.p('mvb', 'MV', B, (50, 96)); d.p('t', 'T', T_COL, (97, 56))
BP = [(30, 60), (70, 60), (42, 42), (60, 36)]; RP = [(34, 30), (66, 30), (44, 54), (58, 64)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b2', 'b3'], 0.3)
d.mv('r1', t - 1.0, t + 0.2, rec(d, 'b3', t + 0.2)); tw = d.pas(b, t + 0.3, rec(d, 'r1', t + 0.5), 0.3)   # bollvinst
t = d.pas(b, tw + 0.2, rec(d, 'r3', tw + 0.9)); t = drive(d, b, 'r3', t, (56, 80), 24); tg = shoot(d, b, t, (52, 99))   # mål inom fem sekunder
d.mv('r3', tw - 0.6, tw + 0.2, (60, 58)); d.mv('b1', tw, tg, (62, 78)); d.mv('b2', tw, tg, (48, 70))
hide(d, b, tg + 0.3)
b2 = d.newball((200, 200)); show(d, b2, tg + 1.0, rec(d, 't', tg + 1.0))
t = d.pas(b2, tg + 1.3, rec(d, 'b2', tg + 2.2)); t = chain(d, b2, t, ['b0', 'b3'], 0.3)
fp = [(0, 'Fyra mot fyra med målvakter', 'Tränaren har extra bollar vid sidan.'),
      (tw - 0.2, 'Bollvinst – tränaren räknar högt', 'Mål inom fem sekunder räknas dubbelt.'),
      (tg - 0.3, 'Mål inom fem sekunder: dubbelt', ''),
      (tg + 1.0, 'Tränaren spelar in en ny boll', 'Spelet fortsätter direkt.')]
finish(d, 'k02', 'fem-sekunder-till-mal-4-mot-4', ['Fem sekunder till mål', '4 mot 4'], 'Plan 40 × 30 m · Två mål med målvakter',
       fp, 'KONTRING', [('box', 6, 2, 94, 98)], countup(tw + 0.1, 3, (84, 70), (tg - tw) / 3) + [lab(tg, tg + 1.8, (52, 86), 'x2')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ k03 2 mot 1 från mittzonen ============
d = Drill(); d.p('mv', 'MV', R, (50, 4)); d.p('f', 'F', R, (50, 50))
team(d, 'a', B, [(40, 92), (60, 92)]); team(d, 'q', B, [(34, 98), (66, 98)], ['', ''])
b = d.newball(rec(d, 'a0', 0))
t = drive(d, b, 'a0', 0.4, (42, 58), 20); d.mv('a1', 0.4, t, (62, 56))
d.mv('f', t - 0.4, t + 0.3, (44, 52))                                                       # försvararen kliver på
t = d.pas(b, t + 0.1, rec(d, 'a1', t + 0.8)); d.mv('a1', t, t + 1.2, (60, 28)); d.carry(b, 'a1', t, t + 1.2); t += 1.2   # passa
tg = shoot(d, b, t + 0.1, (54, 1)); hide(d, b, tg + 0.4)
d.mv('a0', tg, tg + 2.6, (34, 92)); d.mv('a1', tg, tg + 2.6, (66, 92)); d.mv('f', tg, tg + 1.4, (50, 50))
d.mv('q0', tg - 1.0, tg + 0.4, (40, 90)); d.mv('q1', tg - 1.0, tg + 0.4, (60, 90))
b2 = d.newball((200, 200)); show(d, b2, tg + 0.5, rec(d, 'q1', tg + 0.5))
t = drive(d, b2, 'q1', tg + 0.7, (58, 58), 20); d.mv('q0', tg + 0.7, t, (40, 56))
d.mv('f', t - 0.4, t + 0.2, (54, 52))
d.mv('q1', t, t + 1.0, (66, 40)); d.carry(b2, 'q1', t, t + 1.0); t += 1.0                    # dribbla förbi
tg2 = shoot(d, b2, t + 0.1, (46, 1)); d.mv('f', t - 1.0, t, (58, 44))
fp = [(0, 'Driv in i mittzonen', 'Två anfallare mot en försvarare.'),
      (1.6, 'Försvararen kliver på: passa', 'Medspelaren tar bollen mot mål.'),
      (tg + 0.5, 'Nästa par: dribbla förbi', 'Läs försvararen – passa eller dribbla.'),
      (tg2 - 0.4, 'Avsluta', 'Byt försvarare efter tre anfall.')]
finish(d, 'k03', '2-mot-1-fran-mittzonen', ['2 mot 1', 'Från mittzonen'], 'Plan 30 × 20 m · Mittzon · Ett mål med målvakt',
       fp, 'ÖVERLÄGE', [('box', 20, 2, 80, 98), ('zone', 20, 42, 80, 60, (200, 220, 200), 'MITTZON')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ k04 Kontringsstafett ============
d = Drill()
for tm, x0, col in (('b', 34, B), ('r', 66, R)):
    for k in range(4): d.p(f'{tm}{k}', str(k // 2 + 1), col, (x0 + (-4 if k % 2 == 0 else 4), 86 + 6 * (k // 2)))
balls = {}
ex = []
for tm, x0 in (('b', 34), ('r', 66)):
    off = 0.0 if tm == 'b' else 0.3
    for pair in range(2):
        p, q = f'{tm}{2 * pair}', f'{tm}{2 * pair + 1}'
        t0 = 0.4 + off + pair * 7.0
        b = d.newball((200, 200)) if pair else d.newball(rec(d, p, 0))
        if pair:
            d.mv(p, t0 - 1.4, t0 - 0.2, (x0 - 4, 86)); d.mv(q, t0 - 1.4, t0 - 0.2, (x0 + 4, 86)); show(d, b, t0 - 0.1, rec(d, p, t0 - 0.1))
        t = t0
        for (pa, qa, y) in [(p, q, 70), (q, p, 54), (p, q, 40)]:
            d.mv(pa, t, t + 1.0, (x0 - 4 if pa == p else x0 + 4, y + 6)); d.mv(qa, t, t + 1.2, (x0 + 4 if qa == q else x0 - 4, y)); d.carry(b, pa, t, t + 0.6)
            t = d.pas(b, t + 0.7, rec(d, qa, t + 1.2)); t += 0.1
        tg = shoot(d, b, t + 0.05, (x0, 13)); hide(d, b, tg + 0.3)                                  # avslut i småmålet
        ex.append(lab(tg, tg + 1.4, (x0, 22), 'MÅL'))
        d.mv(p, tg + 0.3, tg + 2.6, (x0 - 4, 98 - 6 * (1 - pair))); d.mv(q, tg + 0.3, tg + 2.6, (x0 + 4, 98 - 6 * (1 - pair)))
fp = [(0, 'Två lag tävlar mot varandra', 'Två spelare i taget.'),
      (1.2, 'Passa er fram till konen', 'Och avsluta i småmålet.'),
      (5.6, 'Nästa par startar', 'När paret före har avslutat.'),
      (12, 'Första laget klart med alla vinner', 'Mål ger extra poäng.')]
finish(d, 'k04', 'kontringsstafett', ['Kontringsstafett', 'Lek och stafett'], 'Två led bredvid varandra · Kon 20 m bort · Litet mål efter',
       fp, 'STAFETT', [('cone', 34, 34), ('cone', 66, 34), ('smallgoal', 34, 12), ('smallgoal', 66, 12)], ex)

# ============ k05 Djupt direkt: 5 mot 3 över planen ============
d = Drill(); d.p('mv', 'MV', R, (50, 4)); d.p('t', 'T', T_COL, (50, 98))
AP = [(24, 82), (40, 76), (60, 76), (76, 82), (50, 88)]; team(d, 'a', B, AP); DP = [(34, 44), (50, 40), (66, 44)]; team(d, 'f', R, DP)
b = d.newball(rec(d, 't', 0))
t = d.pas(b, 0.4, rec(d, 'a4', 1.0))
t = d.pas(b, t + 0.2, rec(d, 'a1', t + 0.8)); p1 = t                                               # 1
d.mv('a3', t - 1.0, t + 0.6, (74, 40)); t = d.pas(b, t + 0.2, rec(d, 'a3', t + 1.4)); p2 = t       # 2 – djupt direkt
d.mv('f2', p1, p2, (64, 34)); d.mv('a2', p1, p2 + 0.4, (54, 26))
t = d.pas(b, t + 0.2, rec(d, 'a2', t + 0.8)); p3 = t; tg = shoot(d, b, t + 0.05, (46, 1))            # 3 och avslut
d.mv('f1', p2, p3, (50, 22))
for k in range(5): d.mv(f'a{k}', tg + 0.4, tg + 2.8, AP[k])
for k in range(3): d.mv(f'f{k}', tg + 0.4, tg + 2.8, DP[k])
b2 = d.newball((200, 200)); show(d, b2, tg + 1.4, rec(d, 't', tg + 1.4))
t = d.pas(b2, tg + 3.0, rec(d, 'a0', tg + 3.6)); t = d.pas(b2, t + 0.2, rec(d, 'a1', t + 0.8))
d.mv('f0', t - 0.4, t + 1.0, (40, 58)); t2 = d.pas(b2, t + 0.3, (40, 56), 0.5); tw = t2            # försvararen bryter
d.carry(b2, 'f0', tw, tw + 0.3); tt = d.pas(b2, tw + 0.4, rec(d, 't', tw + 1.6))                   # till tränaren: 1 poäng
fp = [(0, 'Anfallarna vinner bollen från tränaren', 'Fem anfallare, tre försvarare och målvakt.'),
      (p1 - 0.3, 'Bara tre passningar innan avslut', 'Spela djupt direkt.'),
      (tg - 0.3, 'Avslut', 'Ny boll från tränaren.'),
      (tw - 0.2, 'Försvararna vinner bollen', 'Spela till tränaren: 1 poäng.')]
finish(d, 'k05', 'djupt-direkt-5-mot-3-over-planen', ['Djupt direkt', '5 mot 3 över planen'], 'Halv plan i längd · Stort mål med målvakt · Spelzon i andra änden',
       fp, 'KONTRING', [('zone', 8, 68, 92, 94, (200, 220, 200), 'SPELZON')], counter([p1, p2, p3], pos=(86, 60), last=None) + [lab(tt, tt + 1.6, (50, 90), '+1 FÖRSVAR')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ k06 Brytning och kontring mot småmål ============
d = Drill(); d.p('mv', 'MV', R, (50, 4))
AP = [(30, 60), (50, 66), (70, 60), (40, 44), (60, 42)]; team(d, 'a', ORA, AP, ['A'] * 5)
BP = [(32, 32), (50, 28), (68, 32), (42, 48), (58, 52)]; team(d, 'b', B, BP, ['B'] * 5)
b = d.newball(rec(d, 'a1', 0))
t = chain(d, b, 0.4, ['a0', 'a3', 'a4'], 0.3)
d.mv('b4', t - 1.0, t + 0.2, rec(d, 'a4', t + 0.2)); tw = d.pas(b, t + 0.3, rec(d, 'b4', t + 0.5), 0.3)   # brytning
t = d.pas(b, tw + 0.2, rec(d, 'b2', tw + 1.0)); d.mv('b2', tw, tw + 1.0, (70, 58))
t = drive(d, b, 'b2', t, (68, 84), 22); tg = shoot(d, b, t, (70, 95)); hide(d, b, tg + 0.3)                # småmål inom 6 sekunder
d.mv('a2', tw, tg, (64, 80)); d.mv('a4', tw, tg, (60, 66))
fp = [(0, 'Lag A anfaller mot målvakten', 'Lag B försvarar.'),
      (tw - 0.2, 'Brytning', 'Lag B kontrar mot två småmål på mittlinjen.'),
      (tg - 0.4, 'Mål inom 6 sekunder: 2 poäng', ''),
      (tg + 0.6, 'Byt roller efter fyra minuter', '')]
finish(d, 'k06', 'brytning-och-kontring-mot-smamal', ['Brytning och kontring', 'Mot småmål'], 'Plan 30 × 25 m · Stort mål mot två småmål',
       fp, 'KONTRING', [('smallgoal', 30, 96), ('smallgoal', 70, 96)], countdown(tw + 0.1, 6, (86, 70), (tg - tw) / 5) + [lab(tg, tg + 1.8, (70, 86), '+2')])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ oa1 4 mot 4 med tre portar ============
d = Drill()
BP = [(30, 60), (70, 60), (42, 44), (60, 70)]; RP = [(36, 36), (64, 34), (50, 54), (46, 68)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b3', 0))
t = chain(d, b, 0.4, ['b1', 'b2'], 0.3)
d.mv('b2', t, t + 1.8, (50, 6)); d.carry(b, 'b2', t, t + 1.8); tp = t + 1.5                        # driver genom en port
d.mv('r1', t, t + 1.4, (56, 16))
t = d.pas(b, t + 2.0, rec(d, 'r1', t + 2.6), 0.6) if False else t + 1.8
hide(d, b, t + 0.2)
for k in range(4): d.mv(f'b{k}', t + 0.2, t + 2.2, BP[k]); d.mv(f'r{k}', t + 0.2, t + 2.2, RP[k])
show(d, b, t + 2.3, rec(d, 'b0', t + 2.3))
t = d.pas(b, t + 2.5, rec(d, 'b2', t + 3.2))
d.mv('r2', t - 1.0, t + 0.2, rec(d, 'b2', t + 0.2)); tw = d.pas(b, t + 0.3, rec(d, 'r2', t + 0.5), 0.3)   # bollvinst
t = d.pas(b, tw + 0.3, rec(d, 'r3', tw + 1.0)); d.mv('r3', t, t + 1.6, (50, 94)); d.carry(b, 'r3', t, t + 1.6); tp2 = t + 1.3   # in i port inom fyra touch
d.mv('b3', t, t + 1.4, (56, 84))
fp = [(0, 'Fyra mot fyra – varsin kortsida', 'Tre konportar på varje kortsida.'),
      (tp - 0.8, 'Driv igenom en port: poäng', ''),
      (tw - 0.2, 'Bollvinst', 'Poäng inom fyra touch räknas dubbelt.'),
      (tp2 - 0.4, 'Snabbt igenom porten: dubbelt', '')]
finish(d, 'oa1', '4-mot-4-med-tre-portar', ['4 mot 4', 'Med tre portar'], 'Plan 30 × 30 m · Tre konportar på varje kortsida',
       fp, 'SMÅLAGSSPEL', [('box', 8, 6, 92, 94)] + [('cone', x + dx, y) for x in (24, 50, 76) for dx in (-3, 3) for y in (6, 94)],
       [lab(tp, tp + 1.6, (50, 16), '+1'), lab(tp2, tp2 + 1.8, (50, 84), 'x2')] + countup(tw + 0.1, 4, (84, 74), (tp2 - tw) / 4))

# ============ oa3 Vem har bollen? Färgleken ============
d = Drill(); d.p('t', 'T', T_COL, (96, 52))
BP = [(30, 30), (60, 26), (36, 64), (66, 62)]; RP = [(44, 40), (72, 44), (26, 46), (54, 72)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
for k in range(4): wander(d, f'b{k}', 0, 1.6, boxes([BP[k]], 4)[0], 1100 + k, 1.4); wander(d, f'r{k}', 0, 1.6, boxes([RP[k]], 4)[0], 1110 + k, 1.4)
b = d.newball(rec(d, 't', 0))
t = d.pas(b, 1.4, (60, 50), 0.8)                                                                   # ”BLÅ!” – kastar in
d.mv('b1', 1.6, t, (61, 49)); t = d.pas(b, t + 0.3, rec(d, 'b3', t + 1.0)); d.mv('r1', t - 0.6, t + 0.6, (70, 56))
d.mv('b3', t, t + 1.0, (60, 84)); d.carry(b, 'b3', t, t + 1.0); tg = shoot(d, b, t + 1.05, (52, 93)); hide(d, b, tg + 0.3)   # mål i småmålet
d.mv('r3', t, tg, (56, 80))
for k in range(4): wander(d, f'b{k}', tg + 0.4, tg + 2.2, boxes([BP[k]], 5)[0], 1120 + k, 1.4); wander(d, f'r{k}', tg + 0.4, tg + 2.2, boxes([RP[k]], 5)[0], 1130 + k, 1.4)
b2 = d.newball(rec(d, 't', 0))
t2 = d.pas(b2, tg + 2.2, (40, 40), 0.8)                                                            # ”RÖD!”
d.mv('r0', tg + 2.4, t2, (41, 39)); t = d.pas(b2, t2 + 0.3, rec(d, 'r2', t2 + 1.0))
d.mv('r2', t, t + 1.0, (12, 44)); d.carry(b2, 'r2', t, t + 1.0); tg2 = shoot(d, b2, t + 1.05, (6, 50))
d.mv('b2', t, tg2, (20, 56))
fp = [(0, 'Två lag inne i rutan', 'Tränaren har bollarna.'),
      (1.2, 'Tränaren ropar en färg och kastar in', 'Den färgen anfaller, det andra laget försvarar.'),
      (tg - 0.6, 'Mål i vilket småmål som helst', ''),
      (tg + 2.0, 'Ny färg – ny boll', 'Reagera snabbt!')]
finish(d, 'oa3', 'vem-har-bollen-fargleken', ['Vem har bollen?', 'Färgleken'], 'Ruta 20 × 20 m · Ett litet mål på varje sida',
       fp, 'LEK', [('box', 8, 8, 92, 92), ('smallgoal', 50, 8), ('smallgoal', 50, 92), ('smallgoal', 8, 50), ('smallgoal', 92, 50)],
       [lab(1.0, 2.6, (82, 44), '”BLÅ!”'), lab(tg + 1.8, tg + 3.4, (82, 44), '”RÖD!”')])

if __name__ == '__main__': render(C, sys.argv)
