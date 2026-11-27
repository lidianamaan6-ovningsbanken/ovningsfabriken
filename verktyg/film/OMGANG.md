# Så görs en omgång övningsfilmer (externa övningar)

1. Nästa övningar: de i `data/extern.json` vars id inte finns i `OF_EXERCISE_FILM_IDS` i `app/assets/app-*.js`
   (hoppa över typen "Skadeförebyggande uppvärmning" – går inte att visa på en plan).
2. Skriv `render_externN.py` (bygg på `render_extern9.py`: finish, rec, chain, wander, win, countup, countdown, swap_color ...).
   Regler: följ instruktionstexten exakt · `d.mv` före `d.carry` · mottagarens rörelse före passningen · `hide` före `show`.
3. Lägg till filen i `SOURCES` i `granska.py` och kör
   `OF_FILM_OUTPUT=/tmp/g OF_LOGO_PNG=logo.png python3 granska.py render_externN.py` tills 0 fel.
4. Rendera: `OF_FILM_OUTPUT=<ut> OF_LOGO_PNG=logo.png python3 render_externN.py <id> ...`
   och bygg översiktsark med `python3 ark.py <ut> <ut> <id> ...` – titta på dem.
5. Kopiera mp4 till `nya-filmer/`, kör `python3 verktyg/film/koppla_in_filmer.py verktyg/film/data/bank.json id=slug ...`.
6. Committa, pusha till `ny-design` och `main`, testa live med
   `node verktyg/film/filmtest.js https://ovningsfabriken.se/app/ "id=namn" ...`.
Kräver `fonts-noto-core` och ffmpeg.
