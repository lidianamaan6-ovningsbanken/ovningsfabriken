# Hjälpfunktioner för nya filmer i samma stil som de befintliga.
# Bygger på render_avslut_base.py och lägger till planelement, lagfärger,
# svansar, flaska, tränarsignal, västar och platsbyten.
from render_avslut_base import *
import math as _m

makebase_orig = makebase
WHITE = '#f3f5ef'; BLACK = '#1b211e'; YELLOW = '#f2cf45'; ORANGE = '#ff965b'

def shapes_base(label, shapes):
    def mk(c):
        c = dict(c)
        if not c.get('keep_goals'): c['goals'] = []
        im = makebase_orig(c); d = ImageDraw.Draw(im)
        d.rectangle((700, 20, 1050, 60), fill='#0a1e17')
        d.text((1040, 44), label, font=F(19, True), fill='#adc5b6', anchor='rm')
        for s in shapes:
            k = s[0]
            if k == 'zone':
                _, x1, y1, x2, y2, col, txt = s; a = xy((x1, y1)); b = xy((x2, y2))
                ov = Image.new('RGBA', im.size, (0, 0, 0, 0)); od = ImageDraw.Draw(ov)
                od.rectangle((*a, *b), fill=col + (70,), outline=col + (200,), width=3); im.paste(ov, (0, 0), ov); d = ImageDraw.Draw(im)
                if txt: d.text((b[0] - 10, a[1] + 16), txt, font=F(15, True), fill='#e4ecd6', anchor='rm')
            elif k == 'line':  # linje mellan punkter (t.ex. zongränser)
                d.line([xy(q) for q in s[1]], fill='#e4ecd6', width=3)
            elif k == 'box':
                _, x1, y1, x2, y2 = s; a = xy((x1, y1)); b = xy((x2, y2)); d.rounded_rectangle((*a, *b), radius=9, outline='#e4ecd6', width=4)
            elif k == 'ring':
                _, cx, cy, r, n = s
                for i in range(n):
                    v = 2 * _m.pi * i / n; xx, yy = xy((cx + r * _m.cos(v), cy + r * _m.sin(v) * 770 / 650 * 0.85))
                    d.polygon([(xx, yy - 7), (xx - 6, yy + 5), (xx + 6, yy + 5)], fill=ORANGE)
            elif k == 'circle':
                _, cx, cy, r = s; x, y = xy((cx, cy)); rx = 7.7 * r; ry = 6.5 * r * 770 / 650 * 0.85
                d.ellipse((x - rx, y - ry, x + rx, y + ry), outline='#b2cdb1', width=3)
            elif k == 'ugoal':  # mål med öppningen åt ett håll ('up' eller 'down')
                _, x, y, side = s; cx, cy = xy((x, y)); w, h = 46, 18; sg = -1 if side == 'up' else 1
                d.line([(cx - w / 2, cy - sg * h / 2), (cx - w / 2, cy + sg * h / 2), (cx + w / 2, cy + sg * h / 2), (cx + w / 2, cy - sg * h / 2)], fill='#eef4d9', width=4)
            elif k == 'smallgoal':
                _, x, y = s; cx, cy = xy((x, y)); d.rectangle((cx - 17, cy - 10, cx + 17, cy + 10), outline='#eef4d9', width=3)
            elif k in ('cone', 'redcone', 'yellowcone'):
                _, x, y = s; xx, yy = xy((x, y)); col = {'cone': ORANGE, 'redcone': '#e5483b', 'yellowcone': YELLOW}[k]
                d.polygon([(xx, yy - 8), (xx - 7, yy + 6), (xx + 7, yy + 6)], fill=col)
            elif k == 'pole':
                _, x, y = s; xx, yy = xy((x, y)); d.line((xx, yy - 22, xx, yy + 6), fill=YELLOW, width=5); d.ellipse((xx - 5, yy + 3, xx + 5, yy + 9), fill='#b98d1d')
            elif k == 'text':
                _, x, y, txt = s; d.text(xy((x, y)), txt, font=F(16, True), fill='#e4ecd6', anchor='mm')
        return im
    return mk

def light(col):
    col = col.lstrip('#'); r, g, b = (int(col[i:i + 2], 16) for i in (0, 2, 4)); return 0.299 * r + 0.587 * g + 0.114 * b > 150

def frame2(c, t):
    im = c['base'].copy(); d = ImageDraw.Draw(im)
    ex = c.get('extras', [])
    for e in ex:  # under spelarna
        if e['t0'] <= t < e.get('t1', 999) and e['kind'] == 'vest':
            x, y = xy(e['pos']); d.rectangle((x - 9, y - 16, x + 9, y - 4), fill=e['color'], outline='#ffffff', width=2)
    for pl in c['players']:
        x, y = xy(at(pl['tr'], t)); r = 18
        for k in range(pl.get('tails', lambda t: 0)(t) if callable(pl.get('tails')) else 0):
            d.rectangle((x - 6 + k * 7, y + 12, x + 0 + k * 7, y + 30), fill=YELLOW, outline='#7a5c00')
        col = pl['color'](t) if callable(pl['color']) else pl['color']   # färg kan bytas vid rollbyte
        d.ellipse((x - r, y - r, x + r, y + r), fill=col, outline='#e5efd8', width=2)
        d.text((x, y), pl['label'], font=F(12, True), fill=('#153b2b' if light(col) else '#f3f5ef'), anchor='mm')
    for tr in c['balls']:
        if at(tr, t)[0] > 120 or any(abs(tt - t) < 0.05 and q[0] > 150 for tt, q in tr): continue
        x, y = xy(at(tr, t)); d.ellipse((x - 8, y - 8, x + 8, y + 8), fill='#fffef0', outline='#142d22', width=2); d.regular_polygon((x, y, 3), 5, fill='#162d23', rotation=t * 60)
    for e in ex:  # över spelarna
        if not (e['t0'] <= t < e.get('t1', 999)): continue
        if e['kind'] == 'flask':
            x, y = xy(e['pos']); ang = e['ang'](t) if callable(e['ang']) else e['ang']
            dx, dy = _m.cos(_m.radians(ang)), _m.sin(_m.radians(ang))
            d.line((x - 22 * dx, y - 22 * dy, x + 22 * dx, y + 22 * dy), fill='#7fd1b9', width=11)
            d.line((x + 22 * dx, y + 22 * dy, x + 32 * dx, y + 32 * dy), fill='#d9f3ea', width=6)
        elif e['kind'] == 'signal':
            x, y = xy(e['pos']); d.rounded_rectangle((x - 26, y - 62, x + 26, y - 26), radius=6, fill=e['color'], outline='#ffffff', width=3)
        elif e['kind'] == 'label':
            x, y = xy(e['pos']); d.text((x, y), e['text'], font=F(20, True), fill=YELLOW, anchor='mm')
    _, h, s = max([p_ for p_ in c['phases'] if p_[0] <= t], key=lambda p_: p_[0])
    d.text((62, 992), h, font=F(26, True), fill='#eef5e8', anchor='lm'); d.text((62, 1032), s, font=F(21), fill='#b4cbbb', anchor='lm')
    return im

def follow(track, dx=2.2, dy=1.6):
    return [(t, (x + dx, y + dy)) for t, (x, y) in track]

def ring_pos(cx, cy, r, i, n, a0=-90):
    v = _m.radians(a0 + 360 * i / n); return (cx + r * _m.cos(v), cy + r * _m.sin(v) * 0.85 * 770 / 650)

def render(C, argv, thumbs=(1, 4, 7.5, 11, 14.5)):
    for c in C:
        if len(argv) > 1 and c['id'] not in argv[1:]: continue
        stick_balls(c)
        c['base'] = c['shapes'](c)
        for t in thumbs: frame2(c, t).resize((360, 360)).save(ROOT / f"filmwork/{c['id']}-{t}.jpg")
        path = OUT / (c['slug'] + '.mp4')
        proc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', '1080x1080', '-r', '30', '-i', '-', '-an', '-c:v', 'libx264', '-threads', '4', '-preset', 'fast', '-crf', '17', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', str(path)], stdin=subprocess.PIPE)
        for f in range(c['seconds'] * 30): proc.stdin.write(frame2(c, f / 30).tobytes())
        proc.stdin.close(); assert proc.wait() == 0
        print(c['id'], path.name, flush=True)

class Drill:
    """Bygger en övning steg för steg: spelare, löpningar, passningar och dribblingar."""
    def __init__(self):
        self.pl = {}; self.order = []; self.balls = []
    def p(self, pid, label, color, pos):
        self.pl[pid] = dict(label=label, color=color, tr=[(0, pos)]); self.order.append(pid)
    def pos(self, pid):
        return self.pl[pid]['tr'][-1][1]
    def mv(self, pid, t0, t1, to):
        # En ny rörelse tar över från där spelaren är vid t0 (tidigare planerade steg efter t0 stryks).
        tr = self.pl[pid]['tr']; t0 = max(0, t0)
        if t0 < tr[-1][0]:
            cur = at(tr, t0)
            while len(tr) > 1 and tr[-1][0] > t0: tr.pop()
            if tr[-1][0] < t0: tr.append((t0, cur))
            else: tr[-1] = (tr[-1][0], cur) if tr[-1][0] == t0 else tr[-1]
        elif t0 > tr[-1][0]: tr.append((t0, tr[-1][1]))
        t1 = max(t1, t0 + 0.3)
        tr.append((t1, to))
    def path(self, pid, t0, pts, speed=1.0):
        t = t0
        for q in pts:
            cx, cy = self.pos(pid); d = ((q[0] - cx) ** 2 + (q[1] - cy) ** 2) ** .5
            dt = max(0.3, d / 18 / speed); self.mv(pid, t, t + dt, q); t += dt
        return t
    def newball(self, pos):
        self.balls.append([(0, pos)]); return len(self.balls) - 1
    def bpos(self, b):
        return self.balls[b][-1][1]
    def pas(self, b, t0, to, dur=None):
        tr = self.balls[b]; t0 = max(t0, tr[-1][0])
        if dur is None:
            cx, cy = tr[-1][1]; d = ((to[0] - cx) ** 2 + (to[1] - cy) ** 2) ** .5; dur = max(0.45, d / 55)
        if t0 > tr[-1][0]: tr.append((t0, tr[-1][1]))
        tr.append((t0 + dur, to)); return t0 + dur
    def carry(self, b, pid, t0, t1, off=(1.8, -1.2)):
        tr = self.balls[b]; t = max(t0, tr[-1][0])
        while t <= t1 + 1e-6:
            x, y = at(self.pl[pid]['tr'], t); tr.append((t, (x + off[0], y + off[1]))); t = round(t + 0.2, 3)
    def at_feet(self, pid, t=None, off=(1.8, -1.2)):
        x, y = self.pos(pid) if t is None else at(self.pl[pid]['tr'], t); return (x + off[0], y + off[1])
    def players(self):
        return [dict(label=self.pl[k]['label'], color=self.pl[k]['color'], tr=self.pl[k]['tr']) for k in self.order]
    def ballset(self):
        return [b if b[-1][0] >= 18 else b + [(18, b[-1][1])] for b in self.balls]

def stick_balls(c, reach=4.5, end=18.0):
    """Bollen följer med spelaren som har den så länge den inte är i rörelse.
    Nästa passning startar där bollen faktiskt är."""
    if c.get('_stuck'): return
    pls = c['players']
    def nearest(x, y, t):
        best = None
        for p in pls:
            px, py = at(p['tr'], t); dd = ((px - x) ** 2 + (py - y) ** 2) ** .5
            if dd <= reach and (best is None or dd < best[0]): best = (dd, p, (x - px, y - py))
        return best
    def in_goal(x, y): return y < 6 or y > 94 or x < 9 or x > 91
    res = []
    for tr0 in c['balls']:
        tr = []
        for t, q in sorted(tr0, key=lambda z: z[0]):
            if tr and abs(tr[-1][0] - t) < 1e-9: tr[-1] = (t, q)
            else: tr.append((t, q))
        T = max(end, tr[-1][0])
        if tr[-1][0] < T: tr.append((T, tr[-1][1]))
        orig = [q for _, q in tr]
        # varje punkt där bollen stannar eller vänder landar hos närmaste spelare
        snapped = []
        for k, (t, q) in enumerate(tr):
            if q[0] < 150 and not in_goal(*q):
                best = None
                for p in pls:
                    px, py = at(p['tr'], t); dd = ((px - q[0]) ** 2 + (py - q[1]) ** 2) ** .5
                    if dd <= 10 and (best is None or dd < best[0]): best = (dd, px, py)
                if best and best[0] > 2.6: q = (best[1] + 1.8, best[2] - 1.2)
            if k > 0 and orig[k] == orig[k - 1]: q = snapped[-1][1]
            snapped.append((t, q))
        tr = snapped
        out = [tr[0]]
        for k in range(len(tr) - 1):
            (ta, pa), (tb, pb) = out[-1], tr[k + 1]
            still = orig[k] == orig[k + 1] and tb - ta >= 0.15
            if still and pa[0] < 150 and not in_goal(*pa):
                nb = nearest(pa[0], pa[1], ta)
                if nb:
                    _, p, off = nb; t = ta + 0.1
                    while t < tb - 0.05:
                        px, py = at(p['tr'], t); out.append((t, (px + off[0], py + off[1]))); t += 0.1
                    px, py = at(p['tr'], tb); out.append((tb, (px + off[0], py + off[1])))
                    continue
            out.append((tb, pb))
        res.append(out)
    c['balls'] = res; c['_stuck'] = True
