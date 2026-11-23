import granska, film_hjalp, render_avslut_base as base
rows=[]
for fn, only in granska.SOURCES:
    for c in granska.load(fn):
        if only and c['id'] not in only: continue
        if fn not in ('render_pilot.py','render_omgang1.py'): film_hjalp.stick_balls(c)
        last=0
        for tr in c['balls']:
            prev=None
            for f in range(c['seconds']*10+1):
                t=f/10; x,y=base.at(tr,t)
                if x<120 and prev and ((x-prev[0])**2+(y-prev[1])**2)**.5>0.4: last=max(last,t)
                prev=(x,y) if x<120 else None
        rows.append((round(c['seconds']-last,1), c['id'], ' '.join(c['title'])))
rows.sort(reverse=True)
for r in rows: print(r)
