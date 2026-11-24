# Databasen (Supabase)

Projekt: `fwgvfmkdmrpmgririxpt`, region Stockholm (eu-north-1).

- `migrations/` – tabeller och säkerhetsregler, körs i nummerordning.
- `seed.sql` – startdata: kategorier och övningar.

## Tabeller

| Tabell | Vad | Vem får göra vad |
|---|---|---|
| `categories` | Teman, t.ex. Återerövring | Alla får läsa |
| `exercises` | Övningsbanken | Alla ser publicerade övningar med `is_public = true`. Övriga syns inte utan inloggning. |
| `coach_items` | Tränarens pass, matcher, favoriter och inställningar (en rad per sak) | Varje inloggad tränare läser och skriver bara sina egna rader. Utloggade kommer inte åt tabellen alls. |
| `leads` | Förfrågningar från kontaktformuläret | Besökare får bara skicka in. Läses i Supabase under Table Editor → leads. |

## Lägga till en övning på startsidan

I Supabase: Table Editor → `exercises` → Insert row. Sätt `is_public` till true
och `published_at` till dagens datum. Övningen syns direkt på startsidan.
