# SvFF-övningar efter skickade PDF:er, del 6 (målvaktsserien Ö2–Ö7). Regel: först d.mv, sedan d.carry; först mottagarens rörelse, sedan passningen.
import importlib.util, sys
from film_hjalp import *
_s = importlib.util.spec_from_file_location('e9', __file__.replace('render_svff6.py', 'render_extern9.py'))
e9 = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ['x', 'NONE']; _s.loader.exec_module(e9); sys.argv = _a
finish, rec, chain, wander, counter, arrivals = e9.finish, e9.rec, e9.chain, e9.wander, e9.counter, e9.arrivals
lab, hide, show, team, boxes, drive, shoot = e9.lab, e9.hide, e9.show, e9.team, e9.boxes, e9.drive, e9.shoot
factor, swap_color, stand, countdown, countup, win = e9.factor, e9.swap_color, e9.stand, e9.countdown, e9.countup, e9.win
C.clear()
WHITE = '#f3f5ef'; YEL = '#f2cf45'; ORA = '#ff9a4d'; T_COL = '#1b211e'

# ============ wj05 Spelarna först – lekmatch utan coachning ============
SV = ('svb',)

def keeper_pair(id_, slug, title, caps, dive):
    """Två målvakter i var sitt mål 5–8 m isär, skjuter på varandra."""
    d = Drill(); d.p('m1', 'MV1', YEL, (50, 22)); d.p('m2', 'MV2', B, (50, 78))
    t = 0.6; ex = []
    plan = [('m1', 'm2', 0), ('m2', 'm1', 1), ('m1', 'm2', 2), ('m2', 'm1', 3)]
    sides = [-1, 1, 1, -1]
    for k, (sh, kp, _n) in enumerate(plan):
        bb = d.newball(rec(d, sh, t - 0.2) if k == 0 else (200, 200))
        if k: show(d, bb, t - 0.1, rec(d, sh, t - 0.1))
        gy = 78 if kp == 'm2' else 22
        if dive:
            gx = 50 + sides[k] * 13; d.mv(kp, t + 0.35, t + 1.0, (gx - 1.8, gy + 1.2)); txt = 'KASTA SIG'
        else:
            gx = 50 + (0 if k % 2 == 0 else sides[k] * 7); d.mv(kp, t + 0.3, t + 1.0, (gx - 1.8, gy + 1.2)); txt = 'LÅG' if k % 2 == 0 else 'HÖG'
        tc = d.pas(bb, t + 0.1, (gx, gy), 0.9); d.carry(bb, kp, tc, tc + 1.0); hide(d, bb, tc + 1.1)
        ex.append(lab(tc, tc + 1.0, (gx + 14, gy), txt)); d.mv(kp, tc + 1.1, tc + 1.8, (50, gy)); t = tc + 1.9
    fp = [(0, *caps[0]), (0.8, *caps[1]), (3.4, *caps[2]), (t - 1.2, *caps[3])]
    finish(d, id_, slug, title, 'Två spelare · Två mål (eller konmål) 5–8 m isär · Bollar', fp, 'MÅLVAKT',
           [('ugoal', 50, 20, 'up'), ('ugoal', 50, 80, 'down'), ('cone', 34, 20), ('cone', 66, 20), ('cone', 34, 80), ('cone', 66, 80)], ex)

keeper_pair('svb89719', 'o2-fardighetsovning-1-fanga-bollen-svb89719', ['Ö2 – Färdighetsövning 1', 'Fånga bollen'],
            [('MV1 skjuter mot MV2 som fångar', 'Sedan tvärtom.'),
             ('Lägre bollar: händerna under bollen', 'Fånga mellan underarmarna och kroppen.'),
             ('Högre bollar: möt med händerna', 'Greppa bollen framför kroppen. Vid sidan: kom bakom bollen.'),
             ('Avsluten är förutbestämda', 'Målvakten vet höjden. Alternativ: kasta högre bollar.')], False)
keeper_pair('svb89720', 'o3-fardighetsovning-2-kasta-sig-och-fanga-bollen-svb89720', ['Ö3 – Färdighetsövning 2', 'Kasta sig och fånga bollen'],
            [('MV1 skjuter vid sidan om MV2', 'MV2 kastar sig och fångar – sedan tvärtom.'),
             ('Lägre bollar: landa på sidan', 'Kroppen bakom bollen, möt den med båda händerna.'),
             ('Högre bollar: frånskjut med foten närmast bollen', ''),
             ('Avsluten är förutbestämda', 'Målvakten vet hörn och höjd. Alternativ: kasta högre bollar.')], True)

# ============ svb89721 Ö4 – Färdighetsövning 3 – skott ============
d = Drill(); d.p('m1', 'MV', YEL, (50, 8)); d.p('m2', 'MV', B, (50, 92)); d.p('s1', '', R, (36, 74)); d.p('s2', '', R, (64, 26))
t = 0.5; ex = []
for k, (kp, sp, other, gy) in enumerate([('m2', 's1', 'm1', 8), ('m1', 's2', 'm2', 92), ('m2', 's1', 'm1', 8)]):
    bb = d.newball(rec(d, kp, t - 0.1) if k == 0 else (200, 200))
    if k: show(d, bb, t - 0.1, rec(d, kp, t - 0.1))
    sx, sy = d.pos(sp); d.mv(sp, t, t + 0.8, (sx + (6 if gy == 8 else -6), (sy - 18) if gy == 8 else (sy + 18)))
    tr = d.pas(bb, t + 0.1, rec(d, sp, t + 1.0), 0.9)                                                           # rullar ut
    save = k != 1; gx = 44 if k == 0 else 57
    if save:
        d.mv(other, tr + 0.1, tr + 0.6, (gx - 1.8, gy + (1.2 if gy == 8 else -1.2))); tc = d.pas(bb, tr + 0.2, (gx, gy + (0 if gy == 8 else 0)), 0.5)
        d.carry(bb, other, tc, tc + 0.5); hide(d, bb, tc + 0.6); ex.append(lab(tc, tc + 1.2, (gx + 14, gy + (8 if gy == 8 else -8)), 'RÄDDNING'))
    else:
        d.mv(other, tr + 0.1, tr + 0.6, (54, gy)); tc = d.pas(bb, tr + 0.2, (40, 99), 0.5); hide(d, bb, tc + 0.3); ex.append(lab(tc, tc + 1.2, (32, 86), 'PALMING / MÅL'))
    d.mv(sp, tc + 0.3, tc + 1.8, (36, 74) if sp == 's1' else (64, 26)); d.mv(other, tc + 0.7, tc + 1.3, (50, gy)); t = tc + 1.2
fp = [(0, 'Målvakten rullar ut till medspelaren', 'Som avslutar mot det andra målet.'),
      (1.4, 'Fånga lägre och högre bollar', 'Händerna under bollen – eller möt den framför kroppen.'),
      (3.8, 'Upprepa från det andra målet', 'Kasta sig: landa på sidan, frånskjut med närmaste foten.'),
      (t - 1.0, 'Byt uppgifter efter varje skott', 'Palming: stöt iväg bollen mot långsidan.')]
finish(d, 'svb89721', 'o4-fardighetsovning-3-skott-svb89721', ['Ö4 – Färdighetsövning 3', 'Skott'], 'Fyra spelare · Två mål 15–20 m isär',
       fp, 'MÅLVAKT', [('box', 22, 4, 78, 96)], ex)
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ svb89722 Ö5 – Spelövning 1 – skott (2 mot 2) ============
d = Drill(); d.p('mvb', 'MV', B, (50, 90)); d.p('mvr', 'MV', R, (50, 10)); d.p('b', '', B, (40, 58)); d.p('r', '', R, (60, 42))
b = d.newball(rec(d, 'mvb', 0)); ex = []
t = d.pas(b, 0.4, rec(d, 'b', 1.2)); t = drive(d, b, 'b', t, (44, 34), 16); d.mv('r', t - 1.0, t, (50, 30))
d.mv('mvr', t - 0.2, t + 0.4, (44.2, 11.2)); tc = d.pas(b, t + 0.1, (46, 10), 0.4); d.carry(b, 'mvr', tc, tc + 0.5); ex.append(lab(tc, tc + 1.2, (62, 14), 'FÅNGAD'))
d.mv('r', tc, tc + 1.0, (56, 36)); t = d.pas(b, tc + 0.6, rec(d, 'r', tc + 1.4)); t = drive(d, b, 'r', t, (58, 62), 16); d.mv('b', t - 1.2, t, (52, 66))
tg = d.pas(b, t + 0.1, (60, 99), 0.4); d.mv('mvb', tg - 0.4, tg, (46, 90)); hide(d, b, tg + 0.3); ex.append(lab(tg, tg + 1.2, (66, 84), 'MÅL'))
fp = [(0, 'Två lag – spel 2 mot 2', 'Avsluta så ofta som möjligt.'),
      (tc - 0.4, 'Fånga lägre och högre bollar', 'Händerna under bollen – eller möt den framför kroppen.'),
      (tc + 0.6, 'Kasta sig – eller palma', 'Landa på sidan, stöt bollen mot långsidan.'),
      (tg + 0.4, 'Byt målvakter', '')]
finish(d, 'svb89722', 'o5-spelovning-1-skott-svb89722', ['Ö5 – Spelövning 1', 'Skott'], 'Fyra spelare · Spelplan 15 × 10 m · Två mål',
       fp, 'MÅLVAKT', [('box', 22, 6, 78, 94)], ex)
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ svb89723 Ö6 – Spelövning 2 – skott (4 mot 4) ============
d = Drill(); d.p('mvb', 'MV', B, (50, 92)); d.p('mvr', 'MV', R, (50, 8))
BP = [(30, 66), (70, 64), (50, 52)]; RP = [(34, 36), (66, 34), (50, 46)]
team(d, 'b', B, BP); team(d, 'r', R, RP)
b = d.newball(rec(d, 'b0', 0)); ex = []
t = chain(d, b, 0.4, ['b2', 'b1'], 0.3); d.mv('b1', t - 0.6, t + 0.6, (66, 42)); t = drive(d, b, 'b1', t, (62, 36), 14)    # passerar mitten först
d.mv('mvr', t - 0.2, t + 0.3, (55.2, 9.2)); tc = d.pas(b, t + 0.1, (57, 8), 0.5); d.carry(b, 'mvr', tc, tc + 0.5); ex.append(lab(tc, tc + 1.2, (70, 14), 'RÄDDNING'))
t = d.pas(b, tc + 0.7, rec(d, 'r0', tc + 1.5), 0.8); t = chain(d, b, t, ['r2'], 0.3); t = drive(d, b, 'r2', t, (48, 62), 14)
tg = d.pas(b, t + 0.1, (40, 99), 0.4); d.mv('mvb', tg - 0.4, tg, (54, 92)); hide(d, b, tg + 0.3); ex.append(lab(tg, tg + 1.2, (36, 84), 'MÅL'))
fp = [(0, 'Spel 4 mot 4', 'Sträva efter många avslut.'),
      (1.4, 'Avsluta först på motståndarnas planhalva', ''),
      (tc - 0.3, 'Målvakten: fånga, kasta sig eller palma', 'Landa på sidan med kroppen bakom bollen.'),
      (tg + 0.4, 'Byt så att alla får vara målvakt', '')]
finish(d, 'svb89723', 'o6-spelovning-2-skott-svb89723', ['Ö6 – Spelövning 2', 'Skott'], 'Åtta spelare · Spelplan 20 × 15 m · Två mål',
       fp, 'MÅLVAKT', [('box', 14, 4, 86, 96), ('line', [(14, 50), (86, 50)])], ex)
C[-1]['goals'] = [(50, 0), (50, 100)]; C[-1]['keep_goals'] = True

# ============ svb89724 Ö7 – Färdighetsövning 4 – bollstafett ============
d = Drill(); ex = []
for tm, x, col in (('b', 32, B), ('r', 68, R)):
    d.p(f'{tm}0', '', col, (x, 88)); d.p(f'{tm}1', 'X1', col, (x, 26)); d.p(f'{tm}2', 'X2', col, (x - 6, 92)); d.p(f'{tm}3', 'X3', col, (x + 6, 92))
for tm, x in (('b', 32), ('r', 68)):
    sp = 1.0 if tm == 'b' else 0.9
    bb = d.newball(rec(d, f'{tm}0', 0)); t = 0.5 + (0.2 if tm == 'r' else 0)
    t = drive(d, bb, f'{tm}0', t, (x, 64), 14 * sp); tc = d.pas(bb, t + 0.1, rec(d, f'{tm}1', t + 0.8), 0.7)   # skott längs marken – X1 fångar
    d.mv(f'{tm}0', t + 0.2, t + 2.4, (x + 10, 96)); d.carry(bb, f'{tm}1', tc, tc + 0.4)
    t = drive(d, bb, f'{tm}1', tc + 0.4, (x, 50), 14 * sp); tc2 = d.pas(bb, t + 0.1, rec(d, f'{tm}3', t + 0.9), 0.8)
    d.mv(f'{tm}1', t + 0.2, t + 2.4, (x, 26) if False else (x - 10, 96)); d.carry(bb, f'{tm}3', tc2, tc2 + 0.6)
    if tm == 'b': ex += [lab(tc, tc + 1.0, (x + 10, 28), 'FÅNGA'), lab(tc2, tc2 + 1.0, (x + 14, 90), 'FÅNGA')]
fp = [(0, 'Lag om fyra – bollhållaren driver till linjen', 'Skjuter längs marken till X1 som fångar.'),
      (1.6, 'Lägre bollar: händerna under bollen', 'Fånga mellan underarmarna och kroppen.'),
      (3.6, 'X1 driver till linjen och skjuter till X3', 'Den som skjutit ställer sig bakom X3.'),
      (6.0, 'Klart när alla är tillbaka på sina platser', 'Progression: spring med bollen i händerna och kasta.')]
finish(d, 'svb89724', 'o7-fardighetsovning-4-bollstafett-svb89724', ['Ö7 – Färdighetsövning 4', 'Bollstafett'], 'Lag med fyra spelare · Yta 15 × 5 m · Bollar och koner',
       fp, 'LEK', [('line', [(18, 56), (82, 56)]), ('cone', 32, 56), ('cone', 68, 56)], ex)
C[-1]['_stuck'] = True

if __name__ == '__main__': render(C, sys.argv)
