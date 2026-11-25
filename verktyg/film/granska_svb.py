# Granskar svb-filmerna utan att rendera: python3 granska_svb.py [BATCH:n:k]
import sys, os, json
os.environ['OF_ONLY_BUILD'] = '1'
import granska, render_avslut_base as base, film_hjalp
a = sys.argv[1:] or ['ALLA']; sys.argv = ['render_svb.py'] + a
import runpy; runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'render_svb.py'), run_name='svb')
bad = 0
for c in list(base.C):
    c['_render'] = 'film_hjalp'; f = granska.check(c)
    if f: bad += 1; print(c['id'], ' '.join(c['title']), '|', '; '.join(f[:4]))
print('granskade', len(base.C), 'med fel', bad)
