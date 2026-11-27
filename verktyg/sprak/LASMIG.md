# Språk i Övningsfabriken

Appen och webbplatsen skrivs på svenska. `app/assets/sprak.js` översätter det som visas på skärmen
med en ordlista per språk (`app/assets/sprak/<språk>.json`, övningsbanken i `bank-<språk>.json`).
Det tränaren själv skriver (namn, anteckningar) och egennamn (klubbar, personer) översätts aldrig.

## Källor
- `en_hand.tsv` – engelska, handöversatt. Går alltid före maskinen. `{}` = mall, `#` = siffra, `@ord` = enstaka ord.
- `kort.tsv` – de viktigaste orden (meny, knappar, passdelar) handöversatta till alla språk.
- `cache/sv-en.json` – maskinöversättning svenska → engelska (Argos Translate, körs lokalt, inget skickas ut).
- `cache/en-<språk>.json` – maskinöversättning engelska → övriga språk.

## Ny text i appen
1. `node extract.js` och `node extract_tpl.js` (i en mapp med acorn installerat) → strings.json, templates.json
2. `python3 master.py <mappen>` → cache/master.json
3. `python3 mt_run.py cache/... ` för det som saknas (bara nya texter översätts, resten finns i cachen)
4. `python3 bygg_sprak.py` → språkfilerna och versionsnumren i sprak.js
