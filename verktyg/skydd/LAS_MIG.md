# Skyddat innehåll

Appens kod (med alla övningar) och alla övningsfilmer och förhandsbilder ska bara nå
tränare som är inloggade och har aktiv klubblicens.

## Hur det fungerar
- `app/app.html` laddar inte appens kod direkt. `assets/grind.js` kontrollerar inloggning och licens,
  sedan hämtar `assets/skydd.js` koden från Supabase-lagringen `skyddat` (`app/<version>.js`)
  via en tillfällig länk och sparar den på enheten per version.
- Filmer och bilder står i koden som `data-skydd-src`, `data-skydd-poster` och `data-skydd-href`
  (bara filnamn). `skydd.js` byter dem mot tillfälliga länkar (1 timme) till `media/<filnamn>`.
- Lagringens säkerhetsregler (migrering 0008): bara aktiv licens eller admin får läsa, bara admin får lägga in.
- `bygg_lista.py` skriver `app/assets/skydd-lista.json` (körs automatiskt av `koppla_in_filmer.py`).

## Efter varje publicering
Öppna appen som admin → Utvecklare → **Skyddad lagring** → *Ladda upp saknade filer*.
Tills dess används den öppna reserven på GitHub (`RESERV = true` i `skydd.js`).

## När kodförrådet blir privat (sista steget)
1. Gör förrådet privat och flytta publiceringen (GitHub Pro eller Cloudflare Pages).
2. Publicera inte `app/assets/*.mp4`, `*.jpg` (övningsbilder), `app-*.js` eller `nya-filmer/`.
3. Sätt `RESERV = false` i `app/assets/skydd.js`.
4. Byt ut filerna i git-historiken eller räkna med att gamla versioner redan kan ha kopierats.
