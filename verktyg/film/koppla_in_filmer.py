"""Kopplar in nya övningsfilmer i appen (app/assets/app-*.js).
Användning: python3 koppla_in_filmer.py <bank.json> id=slug [id=slug ...]
Filmen ska ligga i nya-filmer/<slug>.mp4. Skapar stillbild, lägger till id i
OF_EXERCISE_FILM_IDS, en videorad per övning och stänger av den ritade animationen."""
import sys, json, html, shutil, subprocess, glob, os
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
bank = {e['id']: e['name'] for e in json.load(open(sys.argv[1]))}
M = dict(a.split('=', 1) for a in sys.argv[2:])
js = glob.glob(f'{R}/app/assets/app-*.js')[0]; s = open(js, encoding='utf-8').read()
new = {i: sl for i, sl in M.items() if f"if (b?.id === '{i}') h += '<video" not in s}
for i, sl in new.items():
    shutil.copy(f'{R}/nya-filmer/{sl}.mp4', f'{R}/app/assets/{sl}.mp4')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', '6', '-i', f'{R}/app/assets/{sl}.mp4', '-frames:v', '1', '-vf', 'scale=720:720', '-q:v', '4', f'{R}/app/assets/{sl}.jpg'], check=True)
a = 'const OF_EXERCISE_FILM_IDS = new Set(['
s = s.replace(a, a + ''.join(f'"{i}", ' for i in new), 1)
anchor = "  if (!["
k = s.index(anchor + "'"); 
lines = ''.join(f"""  if (b?.id === '{i}') h += '<video class="of-exercise-film" controls playsinline preload="metadata" data-skydd-poster="{sl}.jpg" aria-label="{html.escape(bank[i]).replace("'", "&#39;")} – övningsfilm"><source data-skydd-src="{sl}.mp4" type="video/mp4">Din webbläsare kan inte spela filmen. <a data-skydd-href="{sl}.mp4" target="_blank" rel="noopener">Öppna filmen</a>.</video>';\n""" for i, sl in new.items())
s = s[:k] + lines + anchor + ''.join(f"'{i}', " for i in new) + s[k + len(anchor):]
with open(js, 'w', encoding='utf-8') as fh: fh.write(s)
print('nya:', len(new), 'totalt filmer i appen:', s[:s.index('])')].count('"'))

# Versionsnummer på kodfilen så att telefoner hämtar den nya versionen direkt
import hashlib, re
v = hashlib.sha1(s.encode('utf-8')).hexdigest()[:10]
for page in [f'{R}/app/app.html']:
    t = open(page, encoding='utf-8').read()
    t = re.sub(r'(<meta name="of-app" content="app-[0-9a-f]+\.js)(\?v=[0-9a-z]+)?"', r'\1?v=' + v + '"', t)
    with open(page, 'w', encoding='utf-8') as fh: fh.write(t)
print('version', v)
# Lista över skyddade filer (övningsfilmer, bilder och appens kod) för den låsta lagringen
import subprocess
subprocess.run(['python3', f'{R}/verktyg/skydd/bygg_lista.py'], check=True)
