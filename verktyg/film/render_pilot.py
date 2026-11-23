# Pilot: tre nya filmer i samma stil som de 61 befintliga.
# Bygger på render_avslut_base.py (samma plan, spelare, boll, textruta och logga).
from render_avslut_base import *

C.clear()

def shapes_base(label, shapes):
    """Ritar etikett uppe till höger och egna ytor: rutor, småmål, linjer och koner."""
    def mk(c):
        c = dict(c); c['goals'] = []
        im = makebase_orig(c)
        d = ImageDraw.Draw(im)
        d.rectangle((760, 20, 1050, 60), fill='#0a1e17')
        d.text((1040, 44), label, font=F(19, True), fill='#adc5b6', anchor='rm')
        for s in shapes:
            kind = s[0]
            if kind == 'box':
                _, x1, y1, x2, y2 = s
                a = xy((x1, y1)); b = xy((x2, y2))
                d.rounded_rectangle((*a, *b), radius=9, outline='#e4ecd6', width=4)
            elif kind == 'line':
                d.line([xy(p_) for p_ in s[1]], fill='#89aa92', width=2)
            elif kind == 'smallgoal':  # litet mål, öppning mot planens mitt
                _, x, y = s
                cx, cy = xy((x, y)); w, h = 34, 20
                d.rectangle((cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2), outline='#eef4d9', width=3)
            elif kind == 'cone':
                _, x, y = s
                xx, yy = xy((x, y)); d.polygon([(xx, yy - 8), (xx - 7, yy + 6), (xx + 7, yy + 6)], fill='#ff965b')
        return im
    return mk

makebase_orig = makebase

# ---------- 1. Bollinnehav 3 mot 1 (t20) ----------
add('t20', 'bollinnehav-3-mot-1', ['Bollinnehav 3 mot 1', 'Två rutor'],
    'Två rutor bredvid varandra · 3 mot 1 i varje · Fem passningar ger poäng',
    [p('1', B, (0, (14, 32)), (2, (15, 34)), (4.5, (14, 31)), (6, (16, 36)), (8, (16, 36))),
     p('2', B, (0, (40, 34)), (1.5, (40, 34)), (3, (38, 38)), (6, (40, 33)), (8, (39, 35))),
     p('3', B, (0, (26, 68)), (3, (25, 68)), (5, (28, 66)), (7.5, (27, 68)), (9, (27, 68))),
     p('1', R, (0, (27, 46)), (1.5, (32, 42)), (3, (30, 55)), (4.5, (22, 45)), (6, (33, 42)), (7.5, (30, 58)), (9, (28, 50)), (18, (28, 50))),
     p('1', R, (0, (61, 66)), (9.8, (61, 66)), (11, (62, 64)), (13.6, (60, 66)), (15, (62, 62)), (16, (74, 50)), (18, (74, 50))),
     p('2', R, (0, (87, 64)), (11, (87, 64)), (12.3, (85, 60)), (18, (86, 62))),
     p('3', R, (0, (74, 30)), (12.3, (74, 30)), (13.6, (72, 33)), (18, (73, 32))),
     p('1', B, (0, (74, 50)), (9.8, (70, 56)), (11, (80, 58)), (12.3, (76, 40)), (13.6, (66, 60)), (14.8, (70, 62)), (16, (62, 64)), (18, (62, 64)))],
    [(0, (14, 32)), (1, (14, 32)), (1.5, (40, 34)), (2.5, (40, 34)), (3, (25, 68)), (4, (25, 68)), (4.5, (14, 31)), (5.5, (14, 31)),
     (6, (40, 33)), (7, (40, 33)), (7.5, (27, 68)), (8.4, (28, 67)), (9.8, (61, 66)), (10.5, (61, 66)), (11, (87, 64)), (11.8, (86, 62)),
     (12.3, (74, 30)), (13.1, (73, 32)), (13.6, (60, 66)), (14.2, (61, 65)), (14.8, (70, 62)), (18, (66, 63))],
    [(0, 'Tre mot en i varje ruta', 'Blått behåller bollen i vänster ruta. Rött väntar i höger.'),
     (1.5, 'Passning ett till fem', 'Rör dig när bollen rör sig, så finns alltid två passningsvägar.'),
     (7.5, 'Fem passningar ger en poäng', 'Bollen slås långt över till den andra rutan.'),
     (9.8, 'Rött startar sitt 3 mot 1', 'Den blå jagaren styr åt ena hållet.'),
     (14.8, 'Jagaren vinner bollen', 'Jagaren byter plats med spelaren som tappade bollen.')])
C[-1]['shapes'] = shapes_base('SPELUPPBYGGNAD', [('box', 7, 24, 46, 76), ('box', 54, 24, 93, 76)])

# ---------- 2. Passning i tre: A, B, C och D (t11) ----------
def trio(y):
    return [p('V', B, (0, (14, y)), (18, (14, y))),
            p('M', B, (0, (50, y)), (0.6, (46, y)), (2.2, (50, y)), (4.6, (54, y)), (6.2, (50, y)), (8.6, (46, y)), (9.6, (47, y)), (11, (50, y)), (18, (50, y))),
            p('H', B, (0, (86, y)), (18, (86, y)))]
def ballL(y):
    return [(0, (16, y)), (0.4, (16, y)), (1.3, (44, y)), (1.8, (44, y)), (2.6, (16, y)), (8.2, (16, y)), (9.1, (44, y)), (9.7, (45, y + 1)), (11, (84, y)), (12.6, (84, y)), (14.3, (16, y)), (18, (16, y))]
def ballR(y):
    return [(0, (86, y + 5)), (4.2, (86, y + 5)), (4.4, (84, y)), (5.3, (56, y)), (5.8, (56, y)), (6.6, (84, y)), (7, (86, y + 5)), (18, (86, y + 5))]
add('t11', 'passning-i-tre-a-b-c-och-d', ['Passning i tre', 'A, B, C och D'],
    'Grupper om tre på rad · Ytterspelarna har boll · Mittspelaren jobbar',
    trio(34) + trio(66),
    ballL(34),
    [(0, 'A: vänster spelar till mitten', 'Mitten spelar tillbaka direkt med öppen kropp.'),
     (4.2, 'B: samma sak åt höger', 'Mitten vänder sig och möter passningen från höger.'),
     (8.2, 'C: mitten tar emot från vänster', 'Ta emot med bortre foten och spela långt till höger.'),
     (12.6, 'D: lång passning tillbaka', 'Passningen ska ha rätt tyngd hela vägen fram.'),
     (15, 'Byt mittspelare efter 45 sekunder', 'Alla grupper kör samtidigt. Alla får jobba i mitten.')])
C[-1]['balls'] = [ballL(34), ballR(34), ballL(66), ballR(66)]
C[-1]['shapes'] = shapes_base('SPELUPPBYGGNAD', [('cone', 14, 42), ('cone', 50, 42), ('cone', 86, 42), ('cone', 14, 74), ('cone', 50, 74), ('cone', 86, 74)])

# ---------- 3. 4 mot 4 + 1 till fyra småmål med väggspelare (t57) ----------
add('t57', '4-mot-4-plus-1-till-fyra-smamal-med-vaggspelare', ['4 mot 4 + 1', 'Fyra småmål med väggspelare'],
    'Småmål i varje hörn · Joker i mitten · Fyra väggspelare på sidorna',
    [p('1', B, (0, (32, 64)), (1, (32, 64)), (2, (36, 58))),
     p('2', B, (0, (46, 48)), (1.2, (44, 47)), (2.4, (40, 42)), (4, (34, 36))),
     p('3', B, (0, (40, 32)), (2, (38, 30)), (3.4, (28, 27)), (4.6, (22, 24)), (6, (22, 24)), (9, (30, 34))),
     p('4', B, (0, (62, 40)), (9, (64, 40)), (11.6, (74, 34)), (12.6, (78, 31)), (14, (82, 26)), (15, (84, 24))),
     p('1', R, (0, (36, 44)), (2, (38, 44)), (4.5, (28, 32)), (9, (40, 48))),
     p('2', R, (0, (24, 56)), (3, (24, 50)), (5, (20, 34)), (9, (30, 56))),
     p('3', R, (0, (64, 58)), (8, (78, 70)), (9.2, (78, 70)), (11, (74, 58))),
     p('4', R, (0, (70, 30)), (9, (72, 30)), (11, (78, 32)), (12.5, (79, 33)), (14, (74, 40))),
     p('J', G, (0, (50, 52)), (9, (52, 52)), (10, (50, 50)), (13, (52, 48))),
     fixed('V', G, (5, 50)), fixed('V', G, (95, 50)), fixed('V', G, (50, 9)), fixed('V', G, (50, 91))],
    [(0, (32, 62)), (1, (32, 62)), (1.6, (44, 49)), (2.2, (44, 49)), (3, (7, 50)), (3.5, (7, 50)), (4.6, (22, 26)), (5.1, (20, 23)), (5.6, (13, 16)), (8.6, (13, 16)),
     (9, (78, 68)), (9.6, (78, 68)), (10.3, (50, 52)), (10.8, (52, 51)), (11.6, (93, 50)), (12, (93, 50)), (12.6, (79, 35)), (13.2, (80, 31)), (14, (82, 28)), (14.8, (85, 24)), (15.4, (88, 17)), (18, (88, 17))],
    [(0, '4 mot 4 + joker, fyra småmål', 'Jokern och väggspelarna spelar med laget som har bollen.'),
     (2.2, 'Använd väggspelaren', 'Väggspelarna har två touch. Spela vidare direkt.'),
     (4.6, 'Avslut direkt efter väggspel', 'Mål direkt efter passning från en väggspelare ger två poäng.'),
     (9, 'Rött vänder spelet via jokern', 'Löp mot det mål som är öppet.'),
     (12.6, 'Närmaste spelare pressar direkt', 'Blått vinner bollen och avslutar i närmaste mål.')])
C[-1]['shapes'] = shapes_base('AVSLUT OCH MÅL', [('box', 8, 14, 92, 86), ('smallgoal', 11, 16), ('smallgoal', 89, 16), ('smallgoal', 11, 84), ('smallgoal', 89, 84)])

if __name__ == '__main__':
    for c in C:
        if len(sys.argv) > 1 and c['id'] not in sys.argv[1:]: continue
        c['base'] = c['shapes'](c)
        for t in [1, 4, 8, 11, 15]: frame(c, t).resize((540, 540)).save(ROOT / f"filmwork/{c['id']}-{t}.jpg")
        path = OUT / (c['slug'] + '.mp4')
        proc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', '1080x1080', '-r', '30', '-i', '-', '-an', '-c:v', 'libx264', '-threads', '4', '-preset', 'fast', '-crf', '17', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', str(path)], stdin=subprocess.PIPE)
        for f in range(c['seconds'] * 30): proc.stdin.write(frame(c, f / 30).tobytes())
        proc.stdin.close(); assert proc.wait() == 0
        print(c['id'], path.name, flush=True)
