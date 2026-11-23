# Granskar alla filmer bildruta för bildruta utan att rendera dem.
import importlib.util, sys, os, json
import render_avslut_base as base
HERE = os.path.dirname(os.path.abspath(__file__))
# vilken fil som gjort den film som ligger i appen
SOURCES = [('render_pilot.py', ['t11', 't57']), ('render_omgang1.py', ['t05', 't08', 't09', 't10']),
           ('render_rattade.py', None), ('render_omgang2.py', None), ('render_omgang3.py', None),
           ('render_omgang4.py', None), ('render_omgang5.py', None), ('render_extern1.py', None), ('render_extern2.py', None), ('render_extern3.py', None), ('render_extern4.py', None), ('render_extern5.py', None), ('render_extern6.py', None), ('render_extern7.py', None), ('render_extern8.py', None), ('render_extern9.py', None), ('render_extern10.py', None), ('render_extern11.py', None), ('render_extern12.py', None), ('render_extern13.py', None), ('render_extern14.py', None), ('render_extern15.py', None), ('render_extern16.py', None), ('render_extern17.py', None), ('render_extern18.py', None)]
def load(fn):
    spec = importlib.util.spec_from_file_location('m_' + fn[:-3], os.path.join(HERE, fn))
    m = importlib.util.module_from_spec(spec); a = sys.argv; sys.argv = ['x', 'NONE']; spec.loader.exec_module(m); sys.argv = a
    return list(base.C)
def check(c):
    if c.get('_render') == 'film_hjalp':
        import film_hjalp; film_hjalp.stick_balls(c)
    issues = []; secs = c['seconds']; fps = 30
    tracks = [('spelare ' + p['label'], p['tr']) for p in c['players']] + [('boll', b) for b in c['balls']]
    for name, tr in tracks:
        ts = [t for t, _ in tr]
        if any(b < a for a, b in zip(ts, ts[1:])): issues.append(f'{name}: tider i fel ordning')
    def P(tr, t): return base.at(tr, t)
    for name, tr in tracks:
        prev = None; pv = None; flips = 0; maxv = 0
        for f in range(secs * fps + 1):
            t = f / fps; x, y = P(tr, t)
            if x > 120 or any(abs(tt - t) < 0.05 and q[0] > 150 for tt, q in tr): prev = None; continue
            if prev:
                vx, vy = (x - prev[0]) * fps, (y - prev[1]) * fps; v = (vx * vx + vy * vy) ** .5; maxv = max(maxv, v)
                if pv and v > 3 and (pv[0] * vx + pv[1] * vy) < -0.5 * (pv[0] ** 2 + pv[1] ** 2) ** .5 * v: flips += 1
                pv = (vx, vy) if v > 3 else pv
            prev = (x, y)
            if name != 'boll' and not (-3 <= x <= 103 and -3 <= y <= 103): issues.append(f'{name}: utanför planen vid {t:.1f}s'); break
        lim = 140 if name == 'boll' else 45
        if maxv > lim: issues.append(f'{name}: hoppar (fart {maxv:.0f})')
        if flips > 6 and name != 'boll': issues.append(f'{name}: skakar fram och tillbaka ({flips} gånger)')
    # boll som ligger still utan någon spelare vid sig
    for bi, tr in enumerate(c['balls']):
        still = 0; where = None
        for f in range(secs * 10):
            t = f / 10; x, y = P(tr, t); x2, y2 = P(tr, t + 0.1)
            if x > 120 or any(abs(tt - t) < 0.15 and q[0] > 150 for tt, q in tr): still = 0; continue
            near = min(((P(p['tr'], t)[0] - x) ** 2 + (P(p['tr'], t)[1] - y) ** 2) ** .5 for p in c['players'])
            in_goal = y < 6 or y > 94 or x < 9 or x > 91
            if ((x2 - x) ** 2 + (y2 - y) ** 2) ** .5 < 0.3 and near > 5 and not in_goal and t > 0.3 and t < c['seconds'] - 0.5:
                still += 1; where = where or (round(t, 1), round(x), round(y))
            else:
                if still >= 4: issues.append(f'boll ligger still utan spelare vid {where[0]}s ({where[1]},{where[2]})')
                still = 0; where = None
    # spelare ovanpå varandra länge
    pl = c['players']
    for i in range(len(pl)):
        for j in range(i + 1, len(pl)):
            close = sum(1 for f in range(0, secs * 10) if ((lambda a, b: ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** .5)(P(pl[i]['tr'], f / 10), P(pl[j]['tr'], f / 10)) < 1.5))
            if close > 25: issues.append(f'spelare {pl[i]["label"]} och {pl[j]["label"]} ovanpå varandra i {close / 10:.1f}s')
    return sorted(set(issues))
if __name__ == '__main__':
    import sys as _sys
    only_files = _sys.argv[1:]
    report = {}
    for fn, only in SOURCES:
        if only_files and fn not in only_files: continue
        for c in load(fn):
            if only and c['id'] not in only: continue
            if fn not in ('render_pilot.py', 'render_omgang1.py'): c['_render'] = 'film_hjalp'
            report[c['id']] = dict(fil=fn, titel=' '.join(c['title']), fel=check(c))
    bad = {k: v for k, v in report.items() if v['fel']}
    print('granskade filmer:', len(report), '| med fel:', len(bad))
    for k, v in bad.items():
        print(f"\n{k} {v['titel']} ({v['fil']})"); [print('  -', e) for e in v['fel'][:8]]
    json.dump(report, open(os.path.join(HERE, 'granskning.json'), 'w'), ensure_ascii=False, indent=1)
