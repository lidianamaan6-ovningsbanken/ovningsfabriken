# SvFF-övningar efter skickade PDF:er, del 2 (spelform 3 mot 3). Regel: först d.mv, sedan d.carry; först mottagarens rörelse, sedan passningen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e9', __file__.replace('render_svff2.py', 'render_extern9.py'))
e9 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e9); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e9.finish, e9.rec, e9.chain, e9.wander, e9.counter, e9.arrivals
lab, hide, show, team, boxes, drive, shoot = e9.lab, e9.hide, e9.show, e9.team, e9.boxes, e9.drive, e9.shoot
factor, swap_color, stand, countdown, countup, win = e9.factor, e9.swap_color, e9.stand, e9.countdown, e9.countup, e9.win
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'

# ============ wj05 Spelarna först – lekmatch utan coachning ============
SV = ('svb',)

def game33(d, goals_top, goals_bottom, rnd_seed=0, score_at=None):
    BP = [(30, 70), (70, 70), (50, 56)]; RP = [(34, 34), (66, 34), (50, 46)]
    team(d, 'b', B, BP); team(d, 'r', R, RP)

# ============ svb45134 Spel 3 mot 3 ============
d = Drill(); game33(d, 1, 1)
b = d.newball(rec(d, 'b2', 0))
d.mv('r2', 0.3, 1.4, (50, 52)); t = drive(d, b, 'b2', 0.4, (44, 48), 10); t = drive(d, b, 'b2', t, (58, 42), 16)   # fint och riktningsförändring
d.mv('r2', t - 0.8, t, (48, 46)); d.mv('b1', 0.6, t, (72, 40)); t = d.pas(b, t + 0.1, rec(d, 'b1', t + 0.8))
tw = win(d, b, 'r1', 'b1', t + 0.5, 0.7); d.mv('b1', tw, tw + 0.9, rec(d, 'r1', tw + 0.9)); tb = win(d, b, 'b1', 'r1', tw + 1.0, 0.8)   # tillbaka direkt
t = drive(d, b, 'b1', tb, (56, 22), 16); tg = d.pas(b, t + 0.1, (50, 9), 0.4); hide(d, b, tg + 0.3)
fp = [(0, 'Spel 3 mot 3 enligt spelformens regler', 'Två små mål.'),
      (0.6, 'Passera med bollen', 'Driv, vänd, utmana, finta och dribbla.'),
      (tw - 0.2, 'Tappar du bollen – ta tillbaka den', 'Försvaret bryter.'),
      (tb + 0.4, 'Driv bort och gör mål', 'Variera gärna med färre spelare och mindre yta.')]
finish(d, 'svb45134', 'spel-3-mot-3-svb45134', ['Spel 3 mot 3', 'Speluppbyggnad'], 'Ca 6 spelare · Yta 15 × 12 m · Två små mål',
       fp, 'SPELUPPBYGGNAD', [('box', 14, 8, 86, 92), ('smallgoal', 50, 8), ('smallgoal', 50, 92)],
       [lab(tw, tw + 1.0, (76, 44), 'BRYT'), lab(tb, tb + 1.2, (60, 30), 'TILLBAKA!'), lab(tg, tg + 1.4, (50, 18), 'MÅL')])

# ============ svb23199 FS – Spel 3 vs 3 ============
d = Drill(); game33(d, 1, 1)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b2', 'b1'], 0.3); t = drive(d, b, 'b1', t, (64, 26), 16); d.mv('r1', t - 1.2, t, (62, 22))
t = d.pas(b, t + 0.1, rec(d, 'b2', t + 0.8)); d.mv('b2', t - 1.2, t, (50, 30)); tg = d.pas(b, t + 0.1, (48, 9), 0.5); hide(d, b, tg + 0.3)
b2 = d.newball((200, 200)); show(d, b2, tg + 0.6, rec(d, 'r0', tg + 0.6))
for k, ps in enumerate([(30, 70), (70, 70), (50, 56)]): d.mv(f'b{k}', tg, tg + 1.6, ps)
t = d.pas(b2, tg + 0.9, rec(d, 'r2', tg + 1.7)); t = drive(d, b2, 'r2', t, (52, 70), 14); tw = win(d, b2, 'b2', 'r2', t + 0.4, 0.7)
fp = [(0, 'Spel 3 mot 3', 'Spela i åldersgruppens spelform eller mindre.'),
      (1.0, 'Förbered matchen', 'Anpassa instruktionerna efter dagens tema.'),
      (tg - 0.4, 'Mål – motståndarna startar', ''),
      (tw - 0.2, 'Bollvinst – anfall igen', 'Spela så nära spelformen som förutsättningarna tillåter.')]
finish(d, 'svb23199', 'fs-spel-3-vs-3-svb23199', ['FS – Spel 3 vs 3', 'Speluppbyggnad'], 'Spelare, boll, västar, koner och mål',
       fp, 'SPELUPPBYGGNAD', [('box', 14, 8, 86, 92), ('smallgoal', 50, 8), ('smallgoal', 50, 92)], [lab(tg, tg + 1.4, (48, 18), 'MÅL')])

# ============ svb22903 FS – En mot en i yta ============
d = Drill()
PR = [((28, 30), (34, 36)), ((70, 28), (64, 34)), ((30, 70), (36, 64)), ((70, 72), (64, 66))]
for k, (a, f) in enumerate(PR): d.p(f'a{k}', '', B, a); d.p(f'f{k}', '', R, f)
balls = [d.newball(rec(d, f'a{k}', 0)) for k in range(4)]
for k, ((ax, ay), (fx, fy)) in enumerate(PR):
    box = (max(12, ax - 16), max(10, ay - 16), min(88, ax + 16), min(90, ay + 16))
    if k == 0:   # försvararen erövrar – rollerna byts
        wander(d, 'a0', 0, 3.6, box, 300, 1.2); d.carry(balls[0], 'a0', 0, 3.6); d.mv('f0', 0.3, 3.4, rec(d, 'a0', 3.4))
        tw = d.pas(balls[0], 3.8, rec(d, 'f0', 4.1), 0.3); wander(d, 'f0', 4.1, 17.9, box, 301, 1.2); d.carry(balls[0], 'f0', 4.1, 17.9)
        d.mv('a0', 4.1, 5.0, rec(d, 'f0', 5.0)); wander(d, 'a0', 5.0, 17.9, box, 302, 1.3)
    else:
        wander(d, f'a{k}', 0, 17.9, box, 310 + k, 1.2); d.carry(balls[k], f'a{k}', 0, 17.9)
        tr = d.pl[f'a{k}']['tr']; d.pl[f'f{k}']['tr'] = [(t, (x + 5, y + 4)) for t, (x, y) in tr]
fp = [(0, 'Två och två med en boll', 'Spelaren med boll ska behålla den.'),
      (1.0, 'Täck bollen med kroppen', 'Vinkla kroppen så att bollen blir långt från motståndaren.'),
      (tw - 0.2, 'Försvararen erövrar – byt roller', 'Vänd, utmana, finta och dribbla.'),
      (tw + 2.0, 'Stegring: två lag', 'Erövra motståndarnas bollar – först med alla bollar vinner.')]
finish(d, 'svb22903', 'fs-en-mot-en-i-yta-svb22903', ['FS – En mot en i yta', 'Behåll bollen'], 'Yta cirka 15 × 12 m · En boll per par',
       fp, 'SPELUPPBYGGNAD', [('box', 10, 8, 90, 92)], [lab(tw, tw + 1.4, (40, 22), 'BYT ROLL')])

# ============ svb45161 Spel mot många mål ============
d = Drill()
KG = [(30, 26), (70, 22), (50, 46), (24, 64), (76, 60), (50, 80)]
BP = [(18, 40), (40, 70), (62, 36)]; RP = [(82, 40), (60, 70), (36, 34)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
balls = [d.newball(rec(d, f'{tm}{k}', 0)) for tm in 'br' for k in range(3)]
route = {('b', 0): [0, 2, 4], ('b', 1): [3, 5, 2], ('b', 2): [1, 4, 5], ('r', 0): [4, 1, 0], ('r', 1): [5, 3, 0], ('r', 2): [0, 3, 2]}
T1 = 6.0
for (tm, k), gs in route.items():
    pid = f'{tm}{k}'; bb = balls[(0 if tm == 'b' else 3) + k]; t = 0.4 + 0.15 * k
    for gi in gs: gx, gy = KG[gi]; t = drive(d, bb, pid, t, (gx + (2 if k % 2 else -2), gy), 15)
    d.mv(pid, t, T1, d.pos(pid)); d.carry(bb, pid, t, T1)
for i, bb in enumerate(balls):
    if i: tt = d.pas(bb, T1 + 0.2, (4, 20 + 12 * i), 0.8); hide(d, bb, tt + 0.1)
GB = [(30, 70), (70, 70), (50, 56)]; GR = [(34, 34), (66, 34), (50, 24)]
for k in range(3): d.mv(f'b{k}', T1 + 0.2, T1 + 2.2, GB[k]); d.mv(f'r{k}', T1 + 0.2, T1 + 2.2, GR[k])
b = balls[0]; d.carry(b, 'b0', T1, T1 + 2.2)
t = d.pas(b, T1 + 2.4, rec(d, 'b2', T1 + 3.2)); d.mv('r2', T1 + 1.8, t, (52, 50)); t = drive(d, b, 'b2', t, (62, 52), 12)
t = drive(d, b, 'b2', t, (74, 58), 14); tg = t; d.carry(b, 'b2', tg, tg + 0.3)
d.mv('r1', tg + 0.4, tg + 1.8, (96, 50))                                                                   # progression 2: färre spelare – en vilar
fp = [(0, 'En boll per spelare', 'Driv genom så många konmål som möjligt.'),
      (2.0, 'Passera – driv, vänd, finta och dribbla', ''),
      (T1 + 0.2, 'Progression 1: två lag spelar', 'Mål genom att driva genom valfritt konmål.'),
      (tg + 0.4, 'Progression 2: färre spelare på planen', 'Vilande uppmuntrar – byt efter 30 sekunder.')]
finish(d, 'svb45161', 'spel-mot-manga-mal-svb45161', ['Spel mot många mål', 'Speluppbyggnad'], 'Ca 6 spelare · Yta 15 × 12 m · Konmål',
       fp, 'SPELUPPBYGGNAD', [('box', 10, 10, 90, 90)] + [('cone', x + dx, y) for x, y in KG for dx in (-3.5, 3.5)], [lab(tg, tg + 1.4, (74, 50), 'MÅL')])
C[-1]['_stuck'] = False

# ============ svb22862 FS – Spel 1 (vanligt spel med mål och målvakter) ============
d = Drill(); d.p('mvr', 'MV', R, (50, 6)); d.p('mvb', 'MV', B, (50, 94)); game33(d, 1, 1)
b = d.newball(rec(d, 'mvb', 0))
t = d.pas(b, 0.4, rec(d, 'b0', 1.2)); t = chain(d, b, t, ['b2', 'b1'], 0.3); t = drive(d, b, 'b1', t, (62, 24), 16)
d.mv('r1', t - 1.0, t, (60, 20)); tg = shoot(d, b, t + 0.05, (54, 1)); hide(d, b, tg + 0.3)
fp = [(0, 'Spel i åldersgruppens spelform', 'Exempel 1: två lag med mål och målvakter.'),
      (1.2, 'Förbered matchen', 'Anpassa instruktionerna efter träningens tema.'),
      (tg - 0.4, 'Avslut', ''),
      (tg + 0.6, 'Fler exempel', 'Driv över kortlinjen · Skjut ner bollar från koner · Spel mot konmål.')]
finish(d, 'svb22862', 'fs-spel-1-svb22862', ['FS – Spel 1', 'Två lag med mål och målvakter'], 'Spelare, boll, västar, koner och mål',
       fp, 'SPELUPPBYGGNAD', [('box', 14, 4, 86, 96)], [lab(tg, tg + 1.4, (54, 14), 'MÅL')])
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ svb23195 FS – Spel 2 (driv över kortlinjen / skjut ner koner) ============
d = Drill(); game33(d, 0, 0)
b = d.newball(rec(d, 'b0', 0))
t = chain(d, b, 0.4, ['b2', 'b1'], 0.3); t = drive(d, b, 'b1', t, (70, 24), 16); d.mv('r1', t - 1.0, t, (64, 22))
t = drive(d, b, 'b1', t, (72, 6), 16); tl = t; d.carry(b, 'b1', tl, tl + 0.4)                              # över kortlinjen
hide(d, b, tl + 0.5); b2 = d.newball((200, 200)); show(d, b2, tl + 0.8, rec(d, 'r2', tl + 0.8))
for k, ps in enumerate([(30, 70), (70, 70), (50, 56)]): d.mv(f'b{k}', tl, tl + 1.6, ps)
t = d.pas(b2, tl + 1.0, rec(d, 'r0', tl + 1.8)); t = drive(d, b2, 'r0', t, (36, 70), 14)
tk = d.pas(b2, t + 0.1, (30, 92), 0.6); hide(d, b2, tk + 0.3)                                              # skjuter ner en boll från konen
fp = [(0, 'Spel 3 mot 3 utan målvakter', 'Spela i åldersgruppens spelform eller mindre.'),
      (1.2, 'Exempel: driv över motståndarnas kortlinje', ''),
      (tl + 0.8, 'Exempel: skjut ner bollar från konerna', 'På motståndarnas kortlinje.'),
      (tk + 0.4, 'Fler varianter', 'Spel mot flera konmål · Driv genom konmål.')]
finish(d, 'svb23195', 'fs-spel-2-svb23195', ['FS – Spel 2', 'Driv över linjen eller skjut ner koner'], 'Spelare, boll, västar och koner',
       fp, 'SPELUPPBYGGNAD', [('box', 14, 6, 86, 94), ('line', [(14, 6), (86, 6)])] + [('yellowcone', x, 94) for x in (30, 50, 70)],
       [lab(tl, tl + 1.4, (72, 14), 'POÄNG'), lab(tk, tk + 1.4, (30, 84), 'TRÄFF')])

# ============ svb58242 Nummerspel ============
d = Drill(); d.p('t', 'T', T_COL, (50, 96))
for k in range(3): d.p(f'b{k}', str(k + 1), B, (6, 38 + 12 * k)); d.p(f'r{k}', str(k + 1), R, (94, 38 + 12 * k))
b = d.newball((200, 200)); show(d, b, 1.0, rec(d, 't', 1.0))
d.mv('b0', 1.0, 2.4, (40, 52)); d.mv('r0', 1.0, 2.4, (60, 46))
t = d.pas(b, 1.2, rec(d, 'b0', 2.4), 1.2); t = drive(d, b, 'b0', t, (40, 30), 12); d.mv('r0', t - 1.2, t, (42, 22))
tw = win(d, b, 'r0', 'b0', t + 0.4, 0.5); t = drive(d, b, 'r0', tw, (60, 66), 16); t = drive(d, b, 'r0', t, (68, 90), 16); tg = t   # driv bort efter erövring
d.carry(b, 'r0', tg, tg + 0.3); hide(d, b, tg + 0.5)
for k in range(3): d.mv(f'b{k}', tg + 0.4, tg + 2.0, [(30, 64), (40, 40), (66, 52)][k]); d.mv(f'r{k}', tg + 0.4, tg + 2.0, [(70, 36), (60, 60), (34, 48)][k])
b2 = d.newball((200, 200)); show(d, b2, tg + 1.8, rec(d, 't', tg + 1.8)); t = d.pas(b2, tg + 2.0, rec(d, 'b0', tg + 3.0), 1.0)
t = d.pas(b2, t + 0.3, rec(d, 'b2', t + 1.0))
fp = [(0, 'Två lag med nummer', 'Tränaren ropar vilket eller vilka nummer som spelar.'),
      (1.0, '”Ettor!” – in och spela', 'Mål genom att driva genom ett konmål, åt båda hållen.'),
      (tw - 0.2, 'Bryt – och driv bort', 'Träna i olika numerär.'),
      (tg + 0.6, 'Progression: alla på planen', 'Båda lagen gör fortfarande mål i båda målen.')]
finish(d, 'svb58242', 'nummerspel-svb58242', ['Nummerspel', 'Speluppbyggnad'], 'Yta ca 15 × 12 m · Konmål i båda ändar · Två lag med nummer',
       fp, 'SPELUPPBYGGNAD', [('box', 12, 10, 88, 90)] + [('cone', x + dx, y) for x in (32, 68) for y in (10, 90) for dx in (-5, 5)],
       [lab(1.0, 2.4, (78, 92), '”1!”'), lab(tg, tg + 1.4, (68, 82), 'MÅL'), lab(tg + 0.6, tg + 2.2, (74, 92), '”ALLA!”')])

# ============ svb22983 FS – Behålla bollen ============
d = Drill()
KP = [(26, 28), (70, 24), (30, 70), (74, 72), (50, 52), (48, 26)]
team(d, 'k', B, KP, [''] * 6); d.p('f', 'F', R, (14, 50))
balls = [d.newball(rec(d, f'k{k}', 0)) for k in range(6)]
for k in range(6):
    if k == 2:
        wander(d, 'k2', 0, 3.4, (12, 14, 88, 86), 400, 1.3); d.carry(balls[2], 'k2', 0, 3.4)
        d.mv('f', 0.4, 3.4, rec(d, 'k2', 3.4)); tw = d.pas(balls[2], 3.6, rec(d, 'f', 3.9), 0.3)
        wander(d, 'f', 3.9, 17.9, (12, 14, 88, 86), 401, 1.3); d.carry(balls[2], 'f', 3.9, 17.9)          # försvararen behåller bollen
        d.mv('k2', 3.9, 5.2, (60, 44)); d.mv('k2', 5.2, 6.6, rec(d, 'k4', 6.6))                              # den som tappade jagar en ny boll
    elif k == 4:
        wander(d, 'k4', 0, 6.6, (12, 14, 88, 86), 404, 1.3); d.carry(balls[4], 'k4', 0, 6.6)
        tw2 = d.pas(balls[4], 6.8, rec(d, 'k2', 7.1), 0.3); wander(d, 'k2', 7.1, 17.9, (12, 14, 88, 86), 402, 1.3); d.carry(balls[4], 'k2', 7.1, 17.9)
        d.mv('k4', 7.1, 8.4, (40, 70)); wander(d, 'k4', 8.4, 17.9, (12, 14, 88, 86), 405, 1.3)
    else:
        wander(d, f'k{k}', 0, 17.9, (12, 14, 88, 86), 410 + k, 1.3); d.carry(balls[k], f'k{k}', 0, 17.9)
swap_lbl = [(3.9, 'k2'), (7.1, 'k4')]
fp = [(0, 'Alla utom en har varsin boll', 'Behåll bollen – driv mot fria ytor, bollen nära foten.'),
      (tw - 0.4, 'Försvararen erövrar bollen', 'Bryt när bollen kommer för långt från foten.'),
      (tw + 0.4, 'Den som tappade blir försvarare', 'Ställ snabbt om när bollen byter ägare.'),
      (tw2 + 0.6, 'Erövra en ny boll så fort du kan', 'Små barn: försvararen håller en väst i handen.')]
finish(d, 'svb22983', 'fs-behalla-bollen-svb22983', ['FS – Behålla bollen', 'Speluppbyggnad'], 'Yta ca 15 × 12 m · Bollar till alla utom en',
       fp, 'SPELUPPBYGGNAD', [('box', 8, 10, 92, 90)], [lab(tw, tw + 1.4, (40, 58), 'ERÖVRAD'), lab(tw2, tw2 + 1.4, (48, 40), 'ERÖVRAD')])
fct = factor(fp)
C[-1]['players'][2]['color'] = (lambda tt, a=tw * fct, c=tw2 * fct: R if a <= tt < c else B)
C[-1]['players'][4]['color'] = (lambda tt, c=tw2 * fct: R if tt >= c else B)
C[-1]['players'][6]['color'] = (lambda tt, a=tw * fct: B if tt >= a else R)

# ============ svb22982 FS – En mot en (Kontring) ============
d = Drill(); d.p('bh', '', B, (50, 94)); d.p('a', 'A', B, (40, 70)); d.p('f', 'F', R, (50, 8))
for k in range(2): d.p(f'q{k}', '', B, (56 + 5 * k, 96))
b = d.newball(rec(d, 'bh', 0))
t = d.pas(b, 0.6, rec(d, 'a', 1.4)); d.mv('f', 0.8, t + 1.2, (48, 40))                                       # försvararen får starta när bollen lämnar foten
d.mv('a', t, t + 0.4, (44, 62)); d.carry(b, 'a', t, t + 0.4); t = drive(d, b, 'a', t + 0.4, (40, 48), 18)   # första tillslaget – upp i fart
t = drive(d, b, 'a', t, (56, 36), 18); d.mv('f', t - 0.8, t, (52, 34))                                      # fint och riktningsförändring
tw = win(d, b, 'f', 'a', t + 0.4, 0.5); t = drive(d, b, 'f', tw, (46, 70), 18); t = drive(d, b, 'f', t, (50, 92), 18); tl = t   # ny anfallare mot andra kortsidan
d.mv('a', tw, tl, (50, 78))
for pid, ps in [('bh', (40, 70)), ('a', (50, 8)), ('f', (56, 96)), ('q0', (50, 94))]: d.mv(pid, tl + 0.4, tl + 2.4, ps)
fp = [(0, 'Bollhållaren spelar in till anfallaren', 'Försvararen startar när bollen lämnar foten.'),
      (1.6, 'Första tillslaget – upp i fart', 'Finter, riktningsförändring och tempoväxling.'),
      (tw - 0.2, 'Brytning – snabb omställning', 'Ny anfallare driver mot andra kortsidan.'),
      (tl + 0.4, 'Rotera: bollhållare – anfallare – försvarare', 'Spela tills bollen är ur spel.')]
finish(d, 'svb22982', 'fs-en-mot-en-svb22982', ['FS – En mot en', 'Kontring'], 'Yta ca 15 × 12 m · Koner på kortsidorna',
       fp, 'KONTRING', [('box', 16, 6, 84, 94), ('line', [(16, 6), (84, 6)]), ('line', [(16, 94), (84, 94)])],
       [lab(tw, tw + 1.2, (64, 40), 'BRYT'), lab(tl, tl + 1.4, (64, 86), 'ÖVER!')])

if __name__ == '__main__': render(C, sys.argv)
