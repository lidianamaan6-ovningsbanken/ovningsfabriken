# Omgång 5: de sista tretton av Sams egna övningar, steg för steg efter instruktionen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('o3', __file__.replace('render_omgang5.py', 'render_omgang3.py'))
o3 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(o3); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = o3.finish, o3.rec, o3.chain, o3.wander, o3.counter, o3.arrivals
C.clear()
def newball_at(d, t, pos):
    b = d.newball((200, 200)); d.balls[b] = [(0, (200, 200)), (t - 0.01, (200, 200)), (t, pos)]; return b
def lab(t0, t1, pos, text): return dict(kind='label', t0=t0, t1=t1, pos=pos, text=text)
def four(d, pre, col, pts, start=1):
    for k, ps in enumerate(pts): d.p(f'{pre}{k}', str(k + start), col, ps)

# ============ po03 Possession med konportar längs kanterna ============
d = Drill()
four(d, 'b', B, [(32, 34), (64, 32), (66, 64), (36, 66)]); four(d, 'r', R, [(46, 42), (56, 50), (46, 58), (58, 40)])
for k in range(4): wander(d, f'b{k}', 0, 8, (24, 28, 76, 72), 300 + k, 2); wander(d, f'r{k}', 0, 18, (28, 30, 72, 70), 310 + k, 1.6)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b1', 'b2', 'b3', 'b0', 'b1', 'b2']); cnt = arrivals(d, b)[:6]
d.mv('b1', t - 1.2, t + 1.2, (91, 46))                                                    # lagkamraten löper ut på andra sidan porten
d.mv('b2', t - 0.6, t, (74, 52))                                                          # öppnar vinkeln mot porten
t = d.pas(b, t + 0.4, (92.8, 45)); tp = t
d.mv('b1', tp + 0.3, tp + 1.6, (74, 40)); d.carry(b, 'b1', tp + 0.3, tp + 1.6)
t = chain(d, b, tp + 1.8, ['b3', 'b0'])
finish(d, 'po03', 'possession-med-konportar-vid-sidorna', ['Possession med konportar', 'Mottagning på andra sidan'], 'Yta ca 25 × 30 m · Fyra konportar på sidorna · Två lag i mitten',
       [(0, 'Två lag i mitten', 'Räkna passningarna i rad.'),
        (cnt[-1] - 0.2, 'Sex passningar i rad', 'Öppna vinkeln mot porten. Dra försvararen bort från porten.'),
        (tp - 0.8, 'Genom porten till en lagkamrat', 'Lagkamraten tar emot på andra sidan: en poäng.'),
        (tp + 0.4, 'Spelet fortsätter direkt', 'Ny sexkedja. Först till tre. Försvar: stäng porten närmast bollen.')],
       'SPELUPPBYGGNAD', [('box', 18, 20, 82, 80)] + [('cone', x, y + dd) for x in (18, 82) for y in (38, 62) for dd in (-5, 5)],
       counter(cnt + [tp]))

# ============ po04 Possession med avslut – 2 mot 1 ute ============
d = Drill()
four(d, 'b', B, [(30, 42), (62, 40), (68, 58), (36, 60)]); four(d, 'r', R, [(44, 46), (56, 50), (50, 56), (42, 54)])
d.p('ba', 'A', B, (50, 22)); d.p('rf', 'F', R, (46, 18)); d.p('mv1', 'MV', G, (50, 5))
d.p('ra', 'A', R, (50, 78)); d.p('bf', 'F', B, (54, 82)); d.p('mv2', 'MV', G, (50, 95))
for k in range(4): wander(d, f'b{k}', 0, 8, (24, 38, 76, 62), 320 + k); wander(d, f'r{k}', 0, 8, (24, 38, 76, 62), 330 + k, 1.6)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b1', 'b2', 'b3', 'b0', 'b1', 'b2']); cnt = arrivals(d, b)[:6]
d.mv('ba', t - 1, t + 0.4, (40, 24)); t = d.pas(b, t + 0.3, rec(d, 'ba', t + 0.9)); tout = t       # ut till anfallaren
d.mv('b2', tout - 0.5, tout + 1.8, (62, 22)); d.mv('rf', tout, tout + 1.4, (46, 16))                 # en spelare följer med: 2 mot 1
t = d.pas(b, t + 1.4, rec(d, 'b2', t + 2)); t = d.pas(b, t + 0.2, (56, -1), 0.5); d.mv('mv1', t - 0.5, t, (53, 5)); tg = t
d.mv('b3', tg - 1.5, tg + 0.4, (48, 52)); d.mv('b2', tg + 0.2, tg + 2.2, (66, 46))
b2 = newball_at(d, tg + 0.6, rec(d, 'b3', tg + 0.6)); chain(d, b2, tg + 0.8, ['b0', 'b1', 'b2', 'b3'])
finish(d, 'po04', 'possession-med-avslut-2-mot-1-ute', ['Possession med avslut', '2 mot 1 ute'], 'Mittzon för possession · Avslutszon i varje ände',
       [(0, 'Lagen spelar keep away i mitten', 'En anfallare och en försvarare i varje avslutszon.'),
        (cnt[-1] - 0.2, 'Sex passningar: ut till anfallaren', 'Rätt passning i rätt ögonblick.'),
        (tout, 'En spelare från mitten följer med', '2 mot 1 mot försvararen och målvakten. Löpningen ska vara snabb.'),
        (tg - 0.8, 'Snabbt beslut i 2 mot 1', 'Avslut.'),
        (tg + 0.6, 'Ny boll i mitten efter avslutet', 'Försvar: läs när utspelet kommer.')],
       'AVSLUT OCH MÅL', [('zone', 4, 34, 96, 66, (200, 220, 200), 'MITTZON')], counter(cnt + [tout], pos=(80, 30), last='UT!'))
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ po05 Possession 8 mot 8 + 1 – fem aggressiva sekunder ============
d = Drill()
bl = [(16, 22), (40, 18), (66, 20), (86, 26), (14, 76), (40, 82), (64, 80), (86, 74)]
rd = [(30, 34), (52, 32), (72, 38), (28, 52), (72, 56), (30, 66), (50, 68), (68, 66)]
four(d, 'b', B, bl); four(d, 'r', R, rd); d.p('j', 'J', G, (50, 50))
for k in range(8): wander(d, f'b{k}', 0, 6, (12, 16, 88, 84), 340 + k, 2.4); wander(d, f'r{k}', 0, 6, (22, 28, 78, 72), 350 + k, 2.4)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b1', 'j', 'b3', 'b7', 'j', 'b5'])
d.mv('r5', t - 1, t, (38, 78)); tw = d.pas(b, t + 0.3, rec(d, 'r5', t + 0.8), 0.4)
for k in range(8): d.mv(f'b{k}', tw, tw + 1.4, (36 + (k % 4) * 4, 66 + (k // 4) * 6))               # alla deltar i återerövringen
t = chain(d, b, tw, ['r3', 'j', 'r1', 'r2'], 0.3)
tz = tw + 5
for k in range(8): d.mv(f'b{k}', tz, tz + 1.8, [(34, 34), (50, 30), (66, 34), (40, 46), (60, 46), (34, 60), (50, 62), (66, 60)][k])   # kompakt zonförsvar
t = chain(d, b, max(t, tz + 0.2), ['r0', 'r7'])
d.mv('r7', t, t + 1.2, (84, 60)); tsig = t + 1.2                                                     # motståndare instängd vid sidlinjen
d.mv('b4', tsig, tsig + 1, (80, 58)); d.mv('b7', tsig, tsig + 1, (82, 66)); tw2 = d.pas(b, tsig + 1.1, rec(d, 'b4', tsig + 1.3), 0.3)
finish(d, 'po05', 'possession-8-mot-8-plus-1-fem-aggressiva-sekunder', ['Possession 8 mot 8 + 1', 'Fem aggressiva sekunder'], 'Halv plan · Två lag om åtta · Jokern är pivot i mitten',
       [(0, 'Håll bollen med max två tillslag', 'Fria positioner men planen ska vara stor. Trianglar runt jokern.'),
        (tw - 0.3, 'Bollförlust: alla försvarar aggressivt', 'I fem sekunder. Koncentrera många nära bollen.'),
        (tz, 'Lyckas det inte: kompakt zonförsvar', 'Försvara inifrån och ut och vänta på signalen.'),
        (tsig - 0.2, 'Signal: motståndare instängd vid sidlinjen', 'Andra signaler: dålig passning eller dålig mottagning.'),
        (tw2, 'Blått vinner tillbaka bollen', 'Alla deltar i återerövringen.')],
       'ÅTERERÖVRING', [('box', 10, 14, 90, 86)],
       [lab(tw + 0.4 + i, tw + 1.4 + i, (50, 10), f'PRESS {5 - i}') for i in range(5)] + [lab(tz, tsig, (50, 10), 'ZONFÖRSVAR'), lab(tsig, tsig + 1.6, (50, 10), 'SIGNAL!')])

# ============ po06 Possession 4 mot 4 + 3 – rutor och mittcirkel ============
d = Drill(); RU = [(22, 28), (78, 28), (78, 72), (22, 72)]
four(d, 'b', B, [(34, 36), (64, 34), (66, 64), (36, 64)]); four(d, 'r', R, [(44, 42), (56, 44), (56, 58), (44, 56)])
d.p('em', 'E', G, (50, 50)); d.p('eo1', 'E', G, (50, 9)); d.p('eo2', 'E', G, (50, 91))
b = d.newball(rec(d, 'b0', 0)); t = 0.4; marks = []
d.mv('b0', t, t + 1.4, RU[0]); d.carry(b, 'b0', t, t + 1.4); t += 1.4; marks.append((t, RU[0]))      # dribbla in i en ruta
t = d.pas(b, t + 0.3, (51.8, 10.2)); t = d.pas(b, t + 0.3, rec(d, 'em', t + 0.7))                     # med hjälp av de extra spelarna
marks.append((t, (50, 50)))
d.mv('b2', t - 1, t + 0.4, RU[2]); t = d.pas(b, t + 0.3, (RU[2][0] + 1.8, RU[2][1] - 1.2)); marks.append((t, RU[2]))
for k in range(4): wander(d, f'r{k}', 0, t, (30, 30, 70, 70), 360 + k, 1.4)
d.mv('r2', t - 0.4, t + 0.6, (74, 66)); tl = d.pas(b, t + 0.8, rec(d, 'r2', t + 1), 0.3)
for k, ps in enumerate([(60, 62), (70, 54), (64, 74), (56, 70)]): d.mv(f'b{k}', tl, tl + 1.4, ps)
t = chain(d, b, tl, ['r1', 'eo2', 'r3'])
finish(d, 'po06', 'possession-4-mot-4-plus-3-rutor-och-mittcirkel', ['Possession 4 mot 4 + 3', 'Rutor och mittcirkel'], 'Fyra rutor och en mittcirkel · En extra i mitten och två utanför',
       [(0, 'Passa eller dribbla in i rutorna', 'Poäng för varje ruta.'),
        (2, 'Använd de extra spelarna', 'En i mitten och två på utsidan.'),
        (marks[-1][0] - 0.8, 'Bryt igenom zoner', 'Variant: poäng för att flytta bollen från en ruta till den motsatta.'),
        (tl, 'Snabb omställning åt båda hållen', 'Större variant: 9 mot 9 + 3 med två målvakter.')],
       'SPELUPPBYGGNAD', [('box', 10, 14, 90, 86), ('circle', 50, 50, 8)] + [('box', x - 7, y - 7, x + 7, y + 7) for x, y in RU],
       [lab(tt, tt + 1.4, (p_[0], p_[1] - 9), '+1') for tt, p_ in marks if p_ != (50, 50)])

# ============ po07 Possession 4 mot 4 + 2 – fyra kvadrater ============
d = Drill(); RU = [(20, 26), (80, 26), (80, 74), (20, 74)]
four(d, 'b', B, [(34, 34), (66, 34), (66, 66), (34, 66)]); four(d, 'r', R, [(44, 40), (56, 40), (56, 60), (44, 60)])
d.p('em', 'E', G, (50, 50)); d.p('eo', 'E', G, (50, 91))
b = d.newball(rec(d, 'b0', 0)); t = 0.3; marks = []
for k, ru in enumerate(RU):
    d.mv(f'b{k}', t, t + 1.2, ru); t = d.pas(b, t + 0.5, (ru[0] + 1.8, ru[1] - 1.2)); marks.append((t, ru))
    if k == 2: t = d.pas(b, t + 0.3, rec(d, 'em', t + 0.8)); marks.append((t, (50, 50)))
    d.mv(f'b{k}', t + 0.2, t + 1.4, [(38, 36), (62, 36), (62, 64), (38, 64)][k])
for k in range(4): wander(d, f'r{k}', 0, t, (30, 30, 70, 70), 370 + k, 1.4)
t = d.pas(b, t + 0.3, rec(d, 'em', t + 0.8)); marks.append((t, (50, 50))); tb = t
d.mv('r1', tb, tb + 0.8, rec(d, 'em', tb + 0.8)); tl = d.pas(b, tb + 0.9, rec(d, 'r1', tb + 1), 0.3)
for k in range(4): d.mv(f'b{k}', tl, tl + 1.2, (d.pos('r1')[0] + [-6, 6, -4, 6][k], d.pos('r1')[1] + [-5, -5, 6, 6][k]))
tr_ = d.pas(b, tl + 1.4, rec(d, 'b1', tl + 1.6), 0.3)
finish(d, 'po07', 'possession-4-mot-4-plus-2-fyra-kvadrater', ['Possession 4 mot 4 + 2', 'Fyra kvadrater'], 'Fyra kvadrater i hörnen · Mittcirkel · En extra i mitten och en utanför',
       [(0, 'Poäng för varje kvadrat', 'Överlägsenhet med de extra spelarna.'),
        (3, 'Håll planen stor', 'Snabba beslut.'),
        (tb, 'Alla fyra kvadraterna och mittcirkeln: bonus', 'I samma anfall.'),
        (tl - 0.2, 'Vid bollförlust: vinn tillbaka direkt', 'Alla jagar.')],
       'SPELUPPBYGGNAD', [('box', 10, 14, 90, 86), ('circle', 50, 50, 8)] + [('box', x - 7, y - 7, x + 7, y + 7) for x, y in RU],
       [lab(tt, tt + 1.4, (p_[0], p_[1] - 9), '+1') for tt, p_ in marks if p_ != (50, 50)] + [lab(tb, tb + 2.2, (50, 10), 'BONUS')])

# ============ po08 Possession 7 mot 7 + 2 – bryt försvarslinjen ============
d = Drill()
for k, ps in enumerate([(36, 84), (64, 84)]): d.p(f'aA{k}', str(k + 1), B, ps)
d.p('jA', 'J', G, (50, 90)); d.p('dA0', '1', R, (42, 76)); d.p('dA1', '2', R, (58, 76))
for k, x in enumerate([22, 40, 60, 78]): d.p(f'c{k}', str(k + 3), R, (x, 50))
for k, ps in enumerate([(32, 56), (68, 44)]): d.p(f'm{k}', str(k + 3), B, ps)
for k, ps in enumerate([(36, 16), (64, 16)]): d.p(f'aB{k}', str(k + 5), B, ps)
d.p('jB', 'J', G, (50, 10)); d.p('dB0', '7', R, (42, 24)); d.p('dB1', '8', R, (58, 24))
b = d.newball(rec(d, 'aA0', 0))
t = chain(d, b, 0.4, ['jA', 'aA1', 'aA0'])
d.mv('m0', t - 1, t + 0.5, (46, 54)); d.mv('c1', t - 0.8, t + 0.5, (44, 52)); d.mv('aB0', t - 0.6, t + 1, (44, 26))
t = d.pas(b, t + 0.3, rec(d, 'aB0', t + 1.2), 1.2); tB = t                                # linjebrytande passning
d.mv('c2', tB - 0.4, tB + 1.6, (54, 28)); d.mv('dA1', tB - 0.4, tB + 2.0, (60, 50)); d.mv('c1', tB, tB + 1.5, (40, 50)); d.mv('c3', tB, tB + 1.5, (80, 50))
t = chain(d, b, t, ['jB', 'aB1'])
d.mv('dB0', t - 0.8, t + 0.4, rec(d, 'aB1', t + 0.4)); tw = d.pas(b, t + 0.6, rec(d, 'dB0', t + 1), 0.3)
t2 = chain(d, b, tw, ['c2', 'dB1'])
finish(d, 'po08', 'possession-7-mot-7-plus-2-bryt-forsvarslinjen', ['Possession 7 mot 7 + 2', 'Bryt försvarslinjen'], 'Anfallszon A och B · Central zon med fyra försvarare',
       [(0, 'Börja med 3 mot 2 i zon A', 'Två anfallare och en joker mot två försvarare.'),
        (tB - 1.6, 'Linjebrytande passning till zon B', 'Rörelse mellan försvararna.'),
        (tB, 'En mittback kliver in i zon B', 'En försvarare från A fyller linjen. Ingen mottagning bakom linjen (offside).'),
        (tB + 2.4, 'Försvar: kompakt linje, stäng centralt', 'Jokern hjälper laget med boll.'),
        (tw, 'Försvaret vinner bollen', 'Två passningar i följd ger nytt anfall till dem.')],
       'SPELUPPBYGGNAD', [('zone', 4, 66, 96, 96, (60, 150, 220), 'ZON A'), ('zone', 4, 4, 96, 34, (60, 150, 220), 'ZON B'), ('line', [(4, 50), (96, 50)])],
       [lab(t2, t2 + 2, (50, 40), 'NYTT ANFALL')])

# ============ po09 Possession 4 mot 4 + joker – fyra mål ============
d = Drill()
four(d, 'b', B, [(50, 86), (30, 66), (70, 66), (50, 44)]); four(d, 'r', R, [(36, 56), (64, 56), (50, 30), (50, 16)]); d.p('j', 'J', G, (52, 56))
b = d.newball(rec(d, 'b0', 0))
d.mv('b3', 1, 3, (36, 24)); d.mv('b2', 1, 3.2, (72, 40))
t = chain(d, b, 0.6, ['b1', 'j', 'b2', 'b3'])                                                 # framåt från spelaren längst bak
d.mv('b3', t, t + 1, (30, 16)); d.carry(b, 'b3', t, t + 1); t = d.pas(b, t + 1.1, (30, 3), 0.4); tg = t
finish(d, 'po09', 'possession-4-mot-4-plus-joker-fyra-mal', ['Possession 4 mot 4 + joker', 'Fyra mål'], 'Två mål i varje ände · Jokern spelar med laget i boll',
       [(0, 'Anfallet börjar i egen försvarszon', 'Bygg från bakre leden.'),
        (1.6, 'Bollen spelas framåt till anfallarna', 'Från spelaren längst bak, via jokern.'),
        (tg - 1.4, 'Tålamod – forcera inte', 'Avslut först när bollen nått anfallarna.'),
        (tg, 'Varianter', 'Minsta antal passningar, tre zoner, extra poäng för spel genom mitten.')],
       'SPELUPPBYGGNAD', [('box', 10, 6, 90, 94), ('line', [(10, 33), (90, 33)]), ('line', [(10, 67), (90, 67)]), ('smallgoal', 30, 5), ('smallgoal', 70, 5), ('smallgoal', 30, 95), ('smallgoal', 70, 95)])

# ============ po10 Anfall 6 mot 4 i 1-3-1 ============
d = Drill()
pos6 = {'mb': (50, 86), 'p1': (36, 66), 'v': (14, 50), 'p2': (64, 62), 'h': (86, 50), 'a': (50, 28)}
for k, (pid, ps) in enumerate(pos6.items()): d.p(pid, ['MB', '4', '7', '8', '11', '9'][k], B, ps)
four(d, 'r', R, [(30, 34), (46, 30), (60, 30), (72, 36)]); d.p('mv', 'MV', G, (50, 6))
b = d.newball(rec(d, 'mb', 0))
t = d.pas(b, 0.6, rec(d, 'p1', 1.2)); t = d.pas(b, t + 0.3, rec(d, 'p2', t + 1)); tpp = t            # passning mellan pivoterna
d.mv('a', t - 0.4, t + 0.4, (52, 32)); t = d.pas(b, t + 0.3, rec(d, 'a', t + 0.9)); tback = t        # anfallaren med ryggen mot mål
d.mv('p1', t - 1, t + 0.4, (42, 42)); t = d.pas(b, t + 0.3, rec(d, 'p1', t + 0.8))                   # spelar till rättvänd pivot
t = d.pas(b, t + 0.3, (46, -1), 0.6); d.mv('mv', t - 0.6, t, (42, 6)); tg = t
b2 = newball_at(d, tg + 0.8, rec(d, 'v', tg + 0.8)); d.mv('r0', tg + 0.6, tg + 1.4, (18, 48))
tw = d.pas(b2, tg + 1.2, rec(d, 'r0', tg + 1.5), 0.3); d.mv('r0', tw, tw + 1.6, (28, 90)); d.carry(b2, 'r0', tw, tw + 1.6); d.pas(b2, tw + 1.7, (30, 99), 0.4)
finish(d, 'po10', 'anfall-6-mot-4-i-1-3-1', ['Anfall 6 mot 4', 'I 1-3-1'], 'Anfallande lag 6 (1-3-1 + mittback) · Försvar 4 + målvakt · Två minimål',
       [(0, 'Varje anfall startar hos mittbacken', 'Bredd och djup.'),
        (tpp - 0.6, 'Villkor: passning mellan pivoterna', 'Mål räknas bara om ett villkor uppfyllts.'),
        (tback - 0.4, 'Anfallaren tar emot med ryggen mot mål', 'Och spelar till en rättvänd pivot. Trianglar och rörelse utan boll.'),
        (tg - 0.6, 'Mål räknas', 'Villkoret är uppfyllt.'),
        (tw - 0.2, 'Försvaret kontrar mot minimålen', 'Omställning åt båda hållen.')],
       'AVSLUT OCH MÅL', [('smallgoal', 30, 97), ('smallgoal', 70, 97)])
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ po11 Possession 6 mot 6 + 4 mål – bryt linjen ============
d = Drill()
four(d, 'b', B, [(20, 66), (40, 62), (60, 62), (80, 66)]); d.p('ba0', '5', B, (38, 14)); d.p('ba1', '6', B, (62, 14))
four(d, 'r', R, [(20, 34), (40, 38), (60, 38), (80, 34)]); d.p('ra0', '5', R, (38, 86)); d.p('ra1', '6', R, (62, 86))
b = d.newball(rec(d, 'b1', 0))
t = chain(d, b, 0.4, ['b0', 'b1', 'b2', 'b3'])                                                 # max två tillslag
d.mv('r1', 1, 3, (36, 44)); d.mv('r2', 1, 3, (54, 44)); d.mv('r0', 1.4, 3.4, (24, 40)); d.mv('r3', 3, 4.6, (70, 42))   # 1-3: en pressar, tre stänger
d.mv('ba1', t - 0.8, t + 0.4, (66, 20)); t = d.pas(b, t + 0.3, rec(d, 'ba1', t + 1.1), 0.9); tbr = t      # linjebrytande passning
t = d.pas(b, t + 0.3, (70, 3), 0.4); tg = t                                                    # två tillslag totalt
finish(d, 'po11', 'possession-6-mot-6-plus-4-mal-bryt-linjen', ['Possession 6 mot 6', 'Fyra mål – bryt linjen'], 'Plan delad på mitten · Två mål i varje ände · Fyra mittfältare och två anfallare per lag',
       [(0, 'Mittfältarna rör bollen med max två tillslag', 'De får inte korsa mittlinjen. Skapa passningslinjer.'),
        (1.8, 'Försvar: närmaste pressar, tre stänger', 'Zonförsvar 1-3 med ansvar. Anfallarna försvarar inte.'),
        (tbr - 0.9, 'Linjebrytande passning till anfallaren', 'Snabba passningar med precision.'),
        (tbr, 'Två tillslag totalt för att göra mål', 'Kontroll och avslut.')],
       'SPELUPPBYGGNAD', [('line', [(0, 50), (100, 50)]), ('smallgoal', 30, 4), ('smallgoal', 70, 4), ('smallgoal', 30, 96), ('smallgoal', 70, 96)], [lab(tbr, tbr + 1.6, (50, 30), '2 TILLSLAG')])

# ============ po12 Matchspel med omvända mål ============
d = Drill()
four(d, 'b', B, [(50, 80), (24, 62), (76, 62), (40, 46)]); d.p('b4', '5', B, (60, 40))
four(d, 'r', R, [(50, 22), (30, 36), (70, 36), (44, 56)]); d.p('r4', '5', R, (58, 58))
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b1', 'b3'])
d.mv('b2', 1, t + 0.4, (84, 40)); t = d.pas(b, t + 0.4, rec(d, 'b2', t + 1.2), 1.0); tsw = t          # sidbyte innan målchans
d.mv('b2', t, t + 1.6, (84, 12)); d.carry(b, 'b2', t, t + 1.6); t += 1.6                              # rundar målet
d.mv('b4', t - 1.2, t + 0.2, (56, 10)); t = d.pas(b, t + 0.2, rec(d, 'b4', t + 0.6)); tin = t        # inlägg
t = d.pas(b, t + 0.6, (50, 22), 0.4); tg = t                                                          # avslut inom två sekunder in i det omvända målet
finish(d, 'po12', 'matchspel-med-omvanda-mal', ['Matchspel', 'Med omvända mål'], 'Fem mot fem · Målen vända bakåt mot startpunkterna',
       [(0, 'Målen är vända bakåt', 'Laget måste runda och planera anfallet.'),
        (tsw - 1, 'Bonus för sidbyte innan målchans', 'Byt sida snabbt.'),
        (tsw + 0.2, 'Runda målet', 'Läs spelet – ingen fast position.'),
        (tin - 0.2, 'Avslut inom två sekunder efter inlägg: bonus', 'Vid bollförlust: spelare bakom bollen direkt.')],
       'OMSTÄLLNING', [('box', 8, 6, 92, 94), ('ugoal', 50, 24, 'up'), ('ugoal', 50, 76, 'down')], [lab(tsw, tsw + 1.6, (50, 50), 'SIDBYTE +1'), lab(tg, tg + 1.8, (50, 32), 'BONUS')])

# ============ po13 Smålagsspel 4 mot 4 + 4 neutrala ============
d = Drill()
four(d, 'b', B, [(34, 64), (66, 64), (40, 44), (60, 46)]); four(d, 'r', R, [(36, 36), (64, 36), (44, 56), (58, 54)])
for k, ps in enumerate([(12, 16), (88, 16), (88, 84), (12, 84)]): d.p(f'n{k}', 'N', G, ps)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['n3', 'b0', 'b1', 'n1', 'b3'])                                           # neutrala spelar snabbt tillbaka
d.mv('b3', t, t + 1, (54, 18)); d.carry(b, 'b3', t, t + 1); t = d.pas(b, t + 1.1, (52, 1), 0.4); tg = t
b2 = newball_at(d, tg + 0.4, (50, 50)); d.mv('r2', tg + 0.2, tg + 1, (50, 52))                   # direkt i mitten, ingen paus
t = d.pas(b2, tg + 0.5, rec(d, 'r2', tg + 1.0), 0.4); t = chain(d, b2, t, ['n2', 'r3'])
finish(d, 'po13', 'smalagsspel-4-mot-4-plus-4-neutrala', ['Smålagsspel 4 mot 4', 'Plus fyra neutrala'], 'Rektangel med mål i båda ändar · En neutral i varje hörn',
       [(0, 'Använd de neutrala för att skapa yta', 'Neutrala spelar snabbt tillbaka.'),
        (2.4, 'Possession under press', 'Orientering – rätt mål.'),
        (tg - 1, 'Mål', 'Först till tre mål.'),
        (tg + 0.4, 'Spelet startar direkt i mitten', 'Ingen paus. Snabb växling försvar–anfall.')],
       'SPELUPPBYGGNAD', [('box', 14, 18, 86, 82)])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ po14 Zonanfall – från rondo till anfall ============
d = Drill(); RP = [(32, 62), (50, 52), (68, 62), (62, 80), (38, 80)]
for k, ps in enumerate(RP): d.p(f'b{k}', str(k + 1), B, ps)
d.p('r0', '1', R, (46, 66)); d.p('r1', '2', R, (54, 70)); d.p('mv', 'MV', G, (50, 6))
b = d.newball(rec(d, 'b0', 0))
d.mv('r0', 0.5, 4, (40, 64)); d.mv('r1', 0.5, 5, (58, 72))
t = chain(d, b, 0.4, ['b1', 'b2', 'b3', 'b4', 'b0']); cnt = arrivals(d, b)[:5]
d.mv('b2', t - 1, t + 0.6, (88, 46)); t = d.pas(b, t + 0.3, rec(d, 'b2', t + 1.1), 1.0); tw = t      # ut på kanten
for pid, ps in [('b0', (40, 24)), ('b1', (54, 20)), ('b4', (32, 36)), ('b3', (64, 34))]: d.mv(pid, tw - 0.6, tw + 2.2, ps)   # snabb växling till anfall
d.mv('r0', tw - 0.4, tw + 2.2, (46, 20)); d.mv('r1', tw - 0.4, tw + 2.2, (58, 24))                  # rondons försvarare blir försvarare
d.mv('b2', tw, tw + 1.6, (88, 22)); d.carry(b, 'b2', tw, tw + 1.6); t = d.pas(b, tw + 1.7, rec(d, 'b0', tw + 2.4))
t = d.pas(b, t + 0.2, (46, -1), 0.5); tg = t
finish(d, 'po14', 'zonanfall-fran-rondo-till-anfall', ['Zonanfall', 'Från rondo till anfall'], 'Rondoruta på mittfältet · Mål med målvakt framför',
       [(0, 'Rondo 5 mot 2', '5–6 passningar först.'),
        (cnt[-1], 'Ut på kanten', 'Bollen spelas ut när passningarna är klara.'),
        (tw, 'Snabb växling till anfall', 'Försvararna i rondon blir försvarare i anfallet.'),
        (tg - 0.8, 'Avslut mot mål', 'Tillbaka till rondon och kör igen.')],
       'OMSTÄLLNING', [('box', 26, 46, 74, 86)], counter(cnt, pos=(50, 42), last=None))
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

# ============ po15 Anfall i 3-2-5 – fem korridorer ============
d = Drill(); COR = [10, 30, 50, 70, 90]
SB = [(40, 74), (60, 74), (50, 84), (34, 86), (66, 86)]
for k, ps in enumerate(SB): d.p(f'b{k}', str(k + 1), B, ps)
for k, ps in enumerate([(44, 78), (56, 80), (50, 70)]): d.p(f'r{k}', str(k + 1), R, ps)
d.p('r3', '4', R, (40, 30)); d.p('r4', '5', R, (60, 30)); d.p('mv', 'MV', G, (50, 6))
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b1', 'b2', 'b3']); cnt = arrivals(d, b)[:3]; tx = t                     # tre passningar i startrutan
targets = [(COR[0], 30), (COR[1], 44), (COR[2], 24), (COR[3], 44), (COR[4], 30)]
for k in range(5): d.mv(f'b{k}', tx, tx + 2.4, targets[k])                                     # alla fem korridorer besatta
for k, ps in enumerate([(30, 40), (50, 46), (70, 40)]): d.mv(f'r{k}', tx, tx + 2.4, ps)       # två försvarare går in: 5 mot 5
d.mv('r3', tx, tx + 2, (36, 22)); d.mv('r4', tx, tx + 2, (64, 22))
d.carry(b, 'b3', tx, tx + 2.4); t = tx + 2.4
t = chain(d, b, t, ['b2', 'b4'])
d.mv('b4', t, t + 1, (88, 16)); d.carry(b, 'b4', t, t + 1); t = d.pas(b, t + 1.1, rec(d, 'b2', t + 1.6)); t = d.pas(b, t + 0.2, (52, -1), 0.5)
finish(d, 'po15', 'anfall-i-3-2-5-fem-korridorer', ['Anfall i 3-2-5', 'Fem korridorer'], 'Halv plan i fem korridorer · Startruta · Fem mot tre',
       [(0, 'Fem mot tre i startrutan', 'Tre passningar ut ur byggzonen.'),
        (cnt[-1], 'Laget lämnar startrutan', 'Två försvarare går in: 5 mot 5.'),
        (tx + 1, 'Besätt alla fem korridorer', 'Balans inför omställning.'),
        (tx + 3.4, 'Anfall mot mål', 'Vinner försvaret bollen går det direkt i kontring.')],
       'SPELUPPBYGGNAD', [('line', [(x, 6), (x, 64)]) for x in (20, 40, 60, 80)] + [('box', 28, 66, 72, 94)], counter(cnt, pos=(50, 62), last=None))
C[-1]['goals'] = [(50, 0)]; C[-1]['keep_goals'] = True

if __name__ == '__main__':
    render(C, sys.argv)
