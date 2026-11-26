# Granskning 1 – åtgärdslista

Varje punkt från granskningen har ett nummer. Status: ⬜ ej påbörjad · 🔧 pågår · ✅ klar (med var det syns) · 👤 kräver beslut/åtgärd av Sam.

## Etapp 1 – Releaseblockerare
- G1 ✅ (Match → Ny match: utkast med Spara match/Avbryt, sparas först med motståndare och datum; formationen märkt ”exempel” tills den väljs) Ny match skapas direkt när man öppnar formuläret → ska vara utkast tills man sparar, med Avbryt och krav på uppgifter.
- G2 ✅ (Sparade → Lagbanken-raden borta när delning saknas; AI-knappar som inte fungerar på den öppna sidan döljs: matchplan, roller, alternativ, anpassa, mönster m.fl.) Texten om ”Claude-versionen” (Lagbanken, AI-anpassning) ska bort helt.
- G3 ✅ (Verktyg → Rita: ”Rita ny övning” + ”Ladda upp övning” som fungerar utan AI – bilden sparas som egen övning under ”Mina egna övningar”, kan ändras, visas för spelarna, läggas i pass och skrivas ut som PDF; Snabbt pass har ”Ladda upp en övning”; Snabbt pass: whiteboard-fotot och AI-generatorn för enskilda övningar borta; reflektion säger ”Reflektionen är sparad”) ”Fota eller ladda upp – Fungerar inte här just nu” och whiteboard-foto i generatorn: färdigställ eller ta bort ur aktiva flöden.
- G4 ✅ (Planering: Läroplan-fliken, ”Säsong från JFA-läroplanen”, JFA:s SUP i lagkortet, läroplansfilter i banken och JFA-loggan i hjälpen visas bara för JFA; andra klubbar ser sina egna lag i generatorn och banken) JFA-innehåll och JFA-logga visas för alla: läroplan, SUP, hjälp, generatorns lag. Ska bara visas för JFA, andra klubbar får neutralt innehåll.
- G5 ✅ Granskarens tomma testmatch ligger bara i granskarens webbläsare. Den kan tas bort där (öppna matchen → Ta bort två gånger) utan att något annat påverkas. Felet som skapade den är rättat (G1).

## Etapp 2 – Klubb- och lagmodell, data och förtroende
- G6 ✅ (Inloggning → ”Begär tillgång”: sökbar klubblista, namn, e-post, roll, antal tränare – sparas i Supabase-tabellen leads; finns även på sidan ”Ingen aktiv licens”. Lagväljaren utan inloggning har sökbar klubb) Klubblistan: sökbar, väg för klubbar som saknas (begär tillgång).
- G7 ✅ (Inloggad tränare ser bara klubbens lag: Idag → lagrutan, bankens lagfilter, generatorns lag; byte av lag går via klubbens lagval) Inloggad klubb ser bara sina lag och sitt material (generator, filter, läroplan).
- G8 ✅ (Verktyg → ”Så sparas dina data” + länk i Konto och välkomstrutan: konto / bara enheten / delas med klubben / spelare / ta bort; välkomsttexten säger rätt beroende på inloggning) Tydlig modell för var data sparas (enhet / konto / delat), samma besked överallt + sida ”Så sparas dina data”.
- G9 ✅ (Matchanalys: rutan ”Om videon” – bara på enheten, laddas aldrig upp, ingen annan ser den, ligger kvar tills den tas bort; knapp ”Ta bort videon och analysen”) Matchvideo: tydligt att den bara finns på enheten, vem som ser den, hur länge, hur den tas bort.
- G10 ✅ (Konto: ”Klubbadministration · du är ansvarig” med förklaring av rollerna, roll per tränare, bjud in/ta bort; Verktyg-kortet heter ”Konto och klubb” och visar Klubbadministration för ansvariga) Klubbadministration: roller (ansvarig/tränare), bjuda in/ta bort tränare – finns, ska synas tydligt.

## Etapp 3 – Arbetsflöde och navigation
- G11 ✅ (Appen startar alltid på Idag när den öppnas utan länk; Idag visar Snabbt pass / Tomt pass / Från övningsbanken) Första vyn: ny tränare hamnar på Idag med tydlig start (inte på Matcher).
- G12 ✅ (Egen adress per vy: #idag, #planering/sasong, #ovningsbank, #match/analys, #verktyg … Bakåt stänger först öppen övning/pass/match och går sedan till förra vyn; länk öppnar rätt vy efter omladdning. Pass delas fortfarande via Dela/PDF eftersom passen är privata) Adress per vy + bakåtknappen fungerar (dela länk till pass/säsongsplan).
- G13 ✅ (alla flikar i Planering på en rad, lika breda; Läroplan bara för JFA) Planering: flikarna jämnt fördelade, inte två navigationsnivåer som förvirrar.
- G14 ✅ (Planering → Pass: fyra vägar med syfte – Snabbt pass, Tomt pass, Från övningsbanken, Planera säsongen; samma namn på Idag; dubbletten ”Övningar och progressioner” borta från Verktyg) Skapa pass: tre vägar → tydliga syften (Snabbt pass / Avancerad planering / Tomt pass / Från övningsbanken).
- G15 ✅ (”Snabbt pass” i stället för ”på en minut”; passet byggs direkt ur banken utan väntan. AI-väntestatus blir aktuell först om AI slås på – se 👤) ”Träningspass på en minut” – bara om löftet håller; AI-väntestatus, avbryt.
- G16 ✅ (Tomlägen med nästa steg: Pass (fyra vägar), Säsong (”+ Lägg till en period”), Utveckling (checklista med knappar), Match (Ny match)) Tomma lägen med tydligt nästa steg: Planering, Pass, Match, Utveckling.
- G17 ✅ (Match har två flikar: Matcher och Matchanalys (video), egen rubrik, förklaring i tre steg och egen adress #match/analys) Match och Matchanalys separeras.
- G18 🔧 (unika namn: ”Utvärdera motståndaren” (7), ”Vårt eget spel” (8), för yngre ”Efter matchen: vårt eget spel”; yngre lag har grundflöde + Fördjupning – samma upplägg för äldre lag återstår) Matchflödet: grundflöde + fördjupningar, unika namn (två ”Efter matchen”).

## Etapp 4 – Förval och innehåll
- G19 ⬜ Övningsbanken: sökfältet visade ”6 mot 4 till 6 mot 6” – bara platshållare, resultat följer alltid sökfältet.
- G20 ⬜ Filter lag/spelform: klubb → lag, sökbart.
- G21 ⬜ Filtret ”Land” → ”Källa”, förklara kombination.
- G22 ⬜ Generatorn: 12 spelare/75 min, 13–15 år/UEFA B → värden från valt lag, tydligt vad man ändrar.
- G23 ⬜ Läroplan: 14 år förvalt utan lag; 6–7 år saknas; åldersraden kapas på mobil.
- G24 ⬜ Säsong: 16 valda veckor men 20 i kalendern; årtal; lov/uppehåll.
- G25 ⬜ Spelidé: synliga etiketter, lag eller klubb, ”sparat”-besked, AI-förslag granskas.
- G26 ✅ (Utveckling hänvisar till ”Vårt eget spel” i matchen; tomläge visar vad som behövs med knappar) Utveckling: hänvisningen ”Match → steg 8” stämmer inte; riktigt tomläge.
- G27 🔧 (formation märkt exempel klar, lagnamn kräver ifyllt namn)  Motståndarens formation förvald 1-2-3-1; ”Motståndare” sparas som lagnamn.
- G28 ⬜ Övningsdetalj: ”Lägg i pass” huvudknapp, övriga sekundära; tom videokolumn vid scroll.
- G29 ⬜ Samma ord för samma handling (”Lägg i pass”), ikoner med synlig text.
- G30 ⬜ FIFA-länk med /test/ i adressen.
- G31 ⬜ Sparade: Favoriter / Mina övningar / Klubbens delade, tydligt privat/delat.
- G32 ⬜ PDF: förhandsvisning och tydlig status.

## Etapp 5 – Prestanda, mobil, tillgänglighet
- G33 ⬜ Mätning av flikbyten, sök, film, pass, PDF, video – före/efter (se Prestanda nedan).
- G34 ⬜ Video: förlopp vid uppladdning, bild direkt, laddas först vid öppning.
- G35 ⬜ Sökning och filter kvar när man öppnar en övning och går tillbaka.
- G36 ⬜ Mobil: klippta horisontella rader (ålder, spelform, lag) – synliga val.
- G37 ⬜ Tillgänglighet: etiketter, tangentbord, Solläge-kontrast.

## Kräver beslut eller underlag (👤)
- Rättigheter för JFA:s spelarutbildningsplan och externa källor vid försäljning.
- Pilot med 2–3 klubbar.
- Offentlig presentationssida och prissättning.
- Delning av matchvideo mellan tränare (kräver lagring i molnet och samtycke).

## Prestanda – mätningar
(fylls i)
