# Att göra innan lansering

Sparat för senare. Bocka av när det är klart.

## Måste fixas
- [ ] Uppdatera integritetspolicyn: förfrågningar sparas nu i Supabase (Stockholm), inte via mejl
- [ ] Kontaktuppgifter: e-post, telefon, bolagsnamn och org.nr i sidfoten
- [x] Gör `ny-design.html` till den riktiga startsidan (`index.html`)
- [x] Byt länken "Prova appen" från den tillfälliga chatgpt.site-adressen (går nu till app/)

## Gör sidan starkare
- [ ] Mejlnotis när en klubb skickar en förfrågan
- [ ] Foto på Sam till "Om"-delen
- [ ] UEFA C-raden (bekräfta först att det stämmer)
- [ ] Skärmdumpar från appen i en mobilram
- [ ] Flytta in alla 1 200+ övningar i databasen (då visas "Det här finns i banken" automatiskt)
- [ ] Ålder och antal spelare för alla övningar i databasen
- [ ] Kontrollera att alla 1 200 övningar har video, annars justera texten "Animerade videor"
- [ ] Fler övningsvideor

## Appen

Sams riktiga app (v61) ligger i `app/`, utan server: `index.html` = lagval, `app.html` = appen.
27 nya övningsfilmer är inkopplade (88 filmer totalt). Min första egna version ligger i `app-ny/`.

### Backend (påbörjad i app-ny/)
- [x] Steg 1: inloggning med e-postlänk, appens skal och övningsbanken (1 450 övningar från databasen)
- [ ] Steg 2: lag, klubbar och licenser. **Innan leverans:** bara tränare med licens ska komma åt övningarna (i dag räcker det att logga in)
- [ ] Steg 3: träningspass (bygga pass, köra med timer, utrustningslista)
- [ ] Steg 4: läroplan, säsong och spelidé
- [ ] Steg 5: match (förberedelse, matchdag, efter matchen)
- [ ] Egen e-posttjänst (t.ex. Resend) så att inloggningsmejlen blir på svenska och inte begränsas till 2 i timmen
- [ ] Bilder på övningarna i banken (som i gamla appen)
- [ ] Byt "Prova appen" på hemsidan till den nya appen när den är redo
