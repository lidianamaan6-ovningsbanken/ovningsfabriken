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
| `clubs`, `licenses` | Klubbar och deras licens (antal platser, giltig till) | Medlemmar läser sin klubb. Bara admin skapar och ändrar (via Utvecklare-fliken). |
| `club_members` | Vilka tränare som hör till klubben (ansvarig eller tränare) | Kollegor ser varandra. Ändras bara via funktionerna nedan. |
| `club_invites` | Inbjudningslänkar | Bara klubbens ansvariga (och admin) ser dem. |
| `app_admins` | Vem som är admin | Läses bara av en själv. Läggs till med SQL, se nedan. |
| `leads` | Förfrågningar från kontaktformuläret | Besökare får bara skicka in. Läses i Supabase under Table Editor → leads. |

## Lägga till en övning på startsidan

I Supabase: Table Editor → `exercises` → Insert row. Sätt `is_public` till true
och `published_at` till dagens datum. Övningen syns direkt på startsidan.

## Inloggning och licenser

- Appen kräver inloggning (e-post + lösenord). Nya tränare skapar konto via en inbjudningslänk: `app.html?inbjudan=<kod>`.
- Admin skapar klubb + licens i Utvecklare-fliken och får en **ägarlänk** till klubbens ansvariga.
- Den ansvariga bjuder in kollegor under Konto → *Bjud in en kollega*. Det går inte att bjuda in fler än licensens platser.
- **Enhetsgräns:** varje konto får vara aktivt på högst 2 enheter (ändras per klubb i Utvecklare). En tredje enhet måste logga ut en annan, högst 6 byten per dygn. Admin ser antal byten per klubb för att upptäcka delade lösenord.
- Funktioner: `register_device`, `replace_device`, `forget_device`, `admin_set_devices`, `my_access`, `create_invite`, `revoke_invite`, `accept_invite`, `remove_member`, `admin_create_club`, `admin_owner_link`, `admin_set_license`, `admin_clubs`.

### Engångsinställningar i Supabase
1. Authentication → Sign In / Providers → Email: stäng av **Confirm email** (annars väntar nya konton på ett mejl som inte kommer).
2. Gör dig själv till admin i SQL Editor (byt till din e-post):
   `insert into public.app_admins (user_id) select id from auth.users where email = 'din@epost.se';`
