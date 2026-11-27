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
- G18 ✅ (Alla matcher: grundflöde 1 Före matchen → 2 Matchdagen → 3 Efter matchen: vårt eget spel (→ 4 Utvärdera motståndaren för äldre lag), resten under ”Fördjupning (valfritt)”; unika namn; AI-matchplanen visas inte på den öppna sidan)

## Etapp 4 – Förval och innehåll
- G19 ✅ (Övningsbank: sökfältet är tomt vid start, raden visar ”N övningar för ’sökord’ · Rensa sökningen”, och sökningen visar bara övningar där ordet faktiskt finns – bäst träff först) Övningsbanken: sökfältet visade ”6 mot 4 till 6 mot 6” – bara platshållare, resultat följer alltid sökfältet.
- G20 ✅ (Filtret ”Lag eller spelform” grupperat: klubbens lag / spelform; bara den egna klubbens lag) Filter lag/spelform: klubb → lag, sökbart.
- G21 ✅ (”Land” → ”Källa (land eller förbund)”, med förklaring att filtren gäller samtidigt) Filtret ”Land” → ”Källa”, förklara kombination.
- G22 ✅ (Snabbt pass visar ”Förval från <lag>: X spelare, Y min”, säger när man ändrat och har ”Återställ lagets förval”) Generatorn: 12 spelare/75 min, 13–15 år/UEFA B → värden från valt lag, tydligt vad man ändrar.
- G23 ✅ (Läroplan (JFA): ”Inget lag valt – visar 14 år” syns; 6–7 år finns med förklaring och knapp till 3 mot 3-övningar; åldersraden bryts på mobil) Läroplan: 14 år förvalt utan lag; 6–7 år saknas; åldersraden kapas på mobil.
- G24 ✅ (Säsong: kalendern visar lika många veckor som planen (16 val = 16 veckor), årtal vid årsskiftet, vanliga lov markerade) Säsong: 16 valda veckor men 20 i kalendern; årtal; lov/uppehåll.
- G25 ✅ (Spelidé: synliga etiketter Skede/Princip/Ord/Betydelse, rad om att spelidén är din och gäller dina lag, ”✓ Sparad <tid>” och besked vid varje ändring; spelidé och säsongsplan synkas nu till kontot. AI-granskning blir aktuell först om AI slås på) Spelidé: synliga etiketter, lag eller klubb, ”sparat”-besked, AI-förslag granskas.
- G26 ✅ (Utveckling hänvisar till ”Vårt eget spel” i matchen; tomläge visar vad som behövs med knappar) Utveckling: hänvisningen ”Match → steg 8” stämmer inte; riktigt tomläge.
- G27 ✅ (formationen märkt ”exempel / Inte vald” tills den väljs; matchen sparas inte utan motståndarens namn)  Motståndarens formation förvald 1-2-3-1; ”Motståndare” sparas som lagnamn.
- G28 ✅ (Övningsdetalj: bara ”+ Lägg i pass” är huvudknapp; på dator följer filmen/animationen med när man scrollar texten) Övningsdetalj: ”Lägg i pass” huvudknapp, övriga sekundära; tom videokolumn vid scroll.
- G29 ✅ (”Lägg i pass” överallt – knappar och rubrik; hjälpknappen har synlig text ”Hjälp” när det finns plats) Samma ord för samma handling (”Lägg i pass”), ikoner med synlig text.
- G30 ✅ (FIFA-källor med /test/ i adressen länkar först till FIFA Training Centre; PDF:en finns som direktlänk under. Adressen är FIFA:s egen) FIFA-länk med /test/ i adressen.
- G31 ✅ (Sparade: flikarna Favoriter / Mina egna / Klubbens delade, med text om vad som är privat; ”Dela med laget” visas bara när delning finns) Sparade: Favoriter / Mina övningar / Klubbens delade, tydligt privat/delat.
- G32 ✅ (PDF: ”Skapar PDF …”, sedan ruta ”✓ PDF:en är klar” med namn, antal sidor, storlek, förhandsvisning på dator och Öppna / Dela / Ladda ner) PDF: förhandsvisning och tydlig status.

## Etapp 5 – Prestanda, mobil, tillgänglighet
- G33 ✅ (mätt – se Prestanda nedan) Mätning av flikbyten, sök, film, pass, PDF, video – före/efter (se Prestanda nedan).
- G34 ✅ (Matchanalys: videon visas direkt; ”Sparar videon på enheten …” medan den sparas, sedan ”✓ Videon är sparad på enheten”; videon läses först när analysen öppnas) Video: förlopp vid uppladdning, bild direkt, laddas först vid öppning.
- G35 ✅ (sökord, filter och scrollposition är kvar när man öppnar en övning och går tillbaka – testat med bakåtknappen) Sökning och filter kvar när man öppnar en övning och går tillbaka.
- G36 ✅ (valrader för spelform, ålder och lärandemål bryts på mobil i stället för att kapas; automatisk kontroll hittar inget som sticker ut utanför skärmen i Idag, Planering, Bank, Match, Verktyg, Snabbt pass, Säsong eller Pass) Mobil: klippta horisontella rader (ålder, spelform, lag) – synliga val.
- G37 ✅ (automatisk WCAG 2 AA-kontroll (axe) utan fel i alla huvudvyer, övningsdetalj, pass, ny match, datasida och spelidé – både vanligt läge och Solläge; Solläge fungerar nu i alla vyer; synliga etiketter i Spelidé; hjälpknapp med text) Tillgänglighet: etiketter, tangentbord, Solläge-kontrast.

## Kräver beslut eller underlag (👤)
- Rättigheter för JFA:s spelarutbildningsplan och externa källor vid försäljning.
- Pilot med 2–3 klubbar.
- Offentlig presentationssida och prissättning.
- Delning av matchvideo mellan tränare (kräver lagring i molnet och samtycke).

## Prestanda – mätningar
Uppmätt 2026-11-26 i Chromium, mobil (iPhone 13-emulering) och dator. ”4× CPU” = processorn bromsad fyra gånger för att likna en enklare telefon.

| Vad | Före (tidigare mätning) | Nu | 4× CPU |
|---|---|---|---|
| Start, långsamt 4G | 5,9 s | 1,5 s | – |
| Flikbyte (Planering/Bank/Match/Idag) | – | 2–12 ms | 12–39 ms |
| Sök i banken (”avslut”) | 0,21 s | 0,03 s | – |
| Öppna övning med film | – | < 5 ms (filmen laddas när man trycker play) | – |
| Bygga Snabbt pass | – | 0,08–0,1 s | – |
| PDF av en övning | – | – | 0,3 s |
| Matchvideo visas efter val | – | – | 0,2 s |
| Öppna appen utan uppkoppling | fungerade inte | ca 1 s | – |

## Inför ny granskning – checklista
Logga in med ett konto i en klubb som **inte** är JFA (och gärna ett JFA-konto) och gå igenom:
1. **Inloggning:** ”Begär tillgång” finns; klubblistan går att söka i.
2. **Idag:** appen startar här; tre tydliga vägar (Snabbt pass / Tomt pass / Från övningsbanken).
3. **Planering:** flikarna på en rad; tomt läge med fyra vägar; Säsong visar rätt antal veckor, årtal och lov; Spelidé har etiketter och ”Sparad”.
4. **Övningsbank:** sökfältet tomt vid start; sökningen visar bara träffar; filtret ”Källa”; bara egna klubbens lag.
5. **Övning:** ”Lägg i pass” är huvudknappen; filmen följer med vid scroll (dator); PDF visar förhandsvisning och status.
6. **Match:** Ny match sparas först med motståndare och datum; Matcher och Matchanalys är separata flikar; matchvideo har ”Om videon” och ”Ta bort”.
7. **Verktyg:** ”Ladda upp övning” (bild eller PDF) → ”Vad heter övningen?” → hamnar under Sparade → Mina egna; ”Så sparas dina data”; ”Konto och klubb” (Klubbadministration för ansvariga).
8. **Adresser:** byt vy, tryck bakåt – rätt vy kommer tillbaka; kopiera adressen (t.ex. #planering/sasong) och öppna den igen.
9. **JFA-material:** syns inte för andra klubbar (läroplan, SUP, logga).
10. **Inga Claude- eller AI-texter** och inga knappar som säger ”fungerar inte här”.
11. **Solläge och mobil:** allt läsbart, inga rader som kapas.

Kvar att besluta (👤) står ovan: rättigheter, pilot, presentationssida, delning av matchvideo, och om AI ska slås på (kräver API-nyckel).
