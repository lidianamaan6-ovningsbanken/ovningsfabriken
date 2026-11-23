# Filmverktyg för övningsanimationer

Samma verktyg som gjorde de 61 befintliga filmerna (från appens `Appverktyg/`),
plus `render_pilot.py` med nya koreografier.

Kör en film:

    OF_FILM_OUTPUT=./ut OF_LOGO_PNG=verktyg/film/logo.png python3 verktyg/film/render_pilot.py t20

Kräver Python med Pillow, ffmpeg och typsnittet Noto Sans (`fonts-noto-core`).
Varje film är 1080 × 1080, 18 sekunder, cirka 9 sekunder att rendera.

En koreografi = spelarnas och bollens positioner över tid (planen är 0–100 i båda led)
och 4–6 texter för momenten.
