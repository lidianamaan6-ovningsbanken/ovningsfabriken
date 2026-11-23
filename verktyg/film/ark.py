import sys
from PIL import Image
src, out, ids = sys.argv[1], sys.argv[2], sys.argv[3:]
T = (1, 4, 7.5, 11, 14.5)
for part in range(0, len(ids), 4):
    grp = ids[part:part + 4]; im = Image.new('RGB', (360 * 5, 360 * len(grp)), 'white')
    for r, i in enumerate(grp):
        for c, t in enumerate(T): im.paste(Image.open(f'{src}/filmwork/{i}-{t}.jpg'), (c * 360, r * 360))
    im.save(f'{out}-del{part // 4 + 1}.png')
