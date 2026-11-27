# Teknisk genomgång i åtta roller – åtgärder (27 nov 2026)

Status: ✅ åtgärdat i koden · 👤 kräver beslut eller åtgärd av Sam · ⏭ nästa utvecklingssteg

## Steg 1 – skydda innehållet
- 👤 **Ladda upp appkoden och de 1 348 filerna till den skyddade lagringen.** Automatiserat: `.github/workflows/publicera.yml` + `verktyg/skydd/ladda_upp.py` laddar upp det som saknas vid varje publicering. **Lägg in hemligheten `SUPABASE_SERVICE_ROLE_KEY`** i GitHub (Settings → Secrets and variables → Actions → New repository secret; nyckeln finns i Supabase → Project Settings → API → service_role). Kör sedan Actions → Publicera → Run workflow.
- 👤 Testa på en ny enhet att appen startar från lagringen (Utvecklare visar ”appen från: lagringen”).
- ⏭ Sätt `RESERV = false` i `app/assets/skydd.js` och ta bort filmer, bilder och appkod från det öppna förrådet – **först när punkten ovan är verifierad**, annars slutar appen fungera.
- 👤 Hosting med privat förråd: GitHub Pro eller Cloudflare Pages (gratis med privat förråd).
- ✅ Alla adminfunktioner (`admin_*`) kontrolleras med `is_admin()` i databasen; ägarfunktioner med `club_role(...) = 'owner'`. Utvecklarfliken visas bara för admin.
- 👤 Slå ihop de två Järfälla FA-licenserna (Utvecklare → klubblistan; eller fråga mig så skriver jag SQL).

## Steg 2 – säker utrullning
- ✅ Kontroll vid varje publicering: GitHub Actions stoppar om någon JavaScript-fil har syntaxfel.
- ⏭ Testadress och pull requests (en `ny-design`-gren som publiceras till en testadress, `main` bara via PR). Kräver att hostingen bestäms.
- ✅ **Felbevakning:** fel hos tränarna sparas i Supabase-tabellen `client_errors`. 👤 Kör `supabase/migrations/0012_felbevakning.sql`.
- ✅ **Synken:** hämtar högst var 30:e sekund och var tredje minut när appen är öppen (tidigare varje minut + vid varje fokus); väntande inbjudningar hämtas en gång; statusen visar ”sparar” i stället för ”synkad · 1 väntar”.
- 👤 Avtal med JFA om läroplanen, personuppgiftsbiträdesavtal till klubbarna.
- 👤 Mejlavisering vid kontaktformuläret: kräver en e-posttjänst (t.ex. Resend) + en Supabase-funktion. Säg till så bygger jag den när du har ett konto.

## Steg 3 – bygg för fler klubbar
- ⏭ Flytta övningsbanken till databasen med licenskontroll.
- ⏭ Vite + moduler, ta bort `eval`, skärp CSP utan unsafe-eval.
- ⏭ PKCE-inloggning – avvaktar: med PKCE slutar ”Glömt lösenordet – skicka länk” att fungera när mejlet öppnas i en annan webbläsare (vanligt på telefoner). Görs ihop med egen domän och lösenordsåterställning via kod.
- ⏭ Automatiska tester (Playwright) i Actions, versionsräknare per post, separat adminapp.

## Steg 4 – putsa
- ✅ Mobilmenyn: fyra flikar (Idag, Planering, Övningsbank, Match) + **Mer** (Verktyg, Sparade, Konto, data, Utvecklare för admin). Verktyg har en riktig ikon.
- ✅ Idag säger inte längre ”Inget planerat idag” två gånger; Planering har en kompakt rad (+ Nytt pass, Planera säsongen) när det redan finns pass.
- ✅ Materiallistan: ”västar lag 1/lag 2” (färgen syns i ikonen) i stället för ”orange/blå västar”; ”Material för ditt lag (N spelare)”.
- ✅ Kalendern har ikonen före ”= vanligt lov”.
- ✅ **Egna typsnitt** (inga anrop till Google): DM Sans, Fraunces, Barlow Condensed – Barlow borttaget. Licens OFL i `app/fonts`.
- ✅ **PDF-biblioteken** (jsPDF, PDF.js) ligger i appens egna filer; cdnjs är borttaget ur säkerhetspolicyn.
- ✅ Landningssidan: åldrar 8–17 år (+ lek 6–7), `og:image` (bilder/og-bild.jpg) för delade länkar.
- ⏭ Undertexten i filmerna ligger under uppspelningsknapparna (inbränd text) – kräver omrendering av filmerna med text högre upp.
- ⏭ ”Spara för planen” – ladda ner dagens filmer till enheten.
- ⏭ Föreslagen tid per övning i banken.
