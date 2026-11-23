from render_avslut_base import *

C.clear()
add(
    'w21',
    '1-mot-1-och-avslut',
    ['1 mot 1 och avslut'],
    'Försvarare med boll · Anfallare möter · 1 mot 1 mot mål',
    [
        p('A', B, (0, (50, 78)), (2, (50, 78)), (4, (50, 67)), (6, (50, 57)), (8, (39, 47)), (10, (43, 39)), (11, (48, 34))),
        p('F', R, (0, (50, 42)), (2, (50, 42)), (4, (50, 55)), (6, (49, 57)), (8, (46, 51)), (10, (44, 44)), (12, (47, 37))),
        p('MV', R, (0, (50, 31)), (18, (50, 31))),
        fixed('K', G, (42, 87)),
        fixed('K', G, (58, 87)),
    ],
    [
        (0, (50, 40)), (1.8, (50, 40)), (3.4, (50, 69)), (4.2, (50, 61)),
        (6.2, (45, 52)), (7.8, (39, 47)), (9.5, (43, 39)), (10.3, (48, 34)),
        (10.8, (50, 32)), (18, (50, 32)),
    ],
    [
        (0, 'Försvararen passar till anfallaren', 'Anfallaren tar första touchen framåt mot målet i mitten.'),
        (3.4, 'Försvararen kliver ut direkt', 'Anfallaren ska läsa av avståndet och utmana.'),
        (5.5, 'Finta och byt riktning', 'Gå förbi försvararen med en tydlig tempoväxling.'),
        (8.8, 'Avsluta innan försvararen hinner tillbaka', 'Välj hörn efter målvaktens position.'),
        (11, 'Byt roller efter varje försök', 'Lägg till målvakt när spelarna behärskar duellen.'),
    ],
    special='central-goal',
)
C[0]['goals'] = []

_base = makebase
def makebase(c):
    original = c.get('special')
    c['special'] = None
    im = _base(c)
    c['special'] = original
    d = ImageDraw.Draw(im)
    # Tydligt centralt mål med målvakt bakom mållinjen.
    a = xy((42, 34)); b = xy((58, 34))
    d.line((a[0], a[1], b[0], b[1]), fill='#f4f7df', width=5)
    d.line((a[0], a[1], a[0], a[1] - 28), fill='#f4f7df', width=3)
    d.line((b[0], b[1], b[0], b[1] - 28), fill='#f4f7df', width=3)
    d.line((a[0], a[1] - 28, b[0], b[1] - 28), fill='#f4f7df', width=3)
    return im

if __name__ == '__main__':
    c = C[0]
    c['base'] = makebase(c)
    for t in [3, 7, 10]:
        frame(c, t).resize((540, 540)).save(ROOT / f"filmwork/{c['id']}-{t}.jpg")
    path = OUT / (c['slug'] + '.mp4')
    proc = subprocess.Popen([
        'ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24',
        '-s', '1080x1080', '-r', '30', '-i', '-', '-an', '-c:v', 'libx264',
        '-threads', '4', '-preset', 'fast', '-crf', '17', '-pix_fmt', 'yuv420p',
        '-movflags', '+faststart', str(path)
    ], stdin=subprocess.PIPE)
    for f in range(c['seconds'] * 30):
        proc.stdin.write(frame(c, f / 30).tobytes())
    proc.stdin.close()
    assert proc.wait() == 0
    print(path, flush=True)
