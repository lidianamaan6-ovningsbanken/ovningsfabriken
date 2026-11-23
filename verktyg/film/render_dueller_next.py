from render_avslut_base import *

C.clear()

add('w22', 'reaktionsduell-1-mot-1', ['Reaktionsduell 1 mot 1'],
    'Två motsatta mål · Start sida vid sida · Tränaren rullar in bollen',
    [p('A', B, (0,(44,50)), (1.5,(44,49)), (2.5,(43,44)), (4,(42,37)), (6,(45,27)), (8,(47,16)), (9,(50,9))),
     p('F', R, (0,(56,50)), (1.5,(56,49)), (2.5,(54,48)), (4,(52,44)), (6,(50,37)), (8,(49,26)), (9,(50,20))),
     p('MV', R, (0,(50,5)), (18,(50,5))),
     p('MV', R, (0,(50,95)), (18,(50,95))),
     fixed('T', G, (94,50))],
    [(0,(91,50)),(1,(78,50)),(2,(51,50)),(2.6,(44,47)),(4,(42,38)),(6,(45,28)),(8,(48,16)),(9,(50,7)),(18,(50,7))],
    [(0,'Tränaren rullar in bollen mellan spelarna','Starta på passningen – inte på en signal.'),
     (2,'Båda reagerar och går mot bollen','Första spelaren dit får anfalla.'),
     (3,'Blå vinner bollen och anfaller sitt mål','Orange ställer om direkt och försvarar.'),
     (6,'Första touchen framåt – skydda bollen','Försvararen försöker komma goal side.'),
     (9,'Avslut mot det tilldelade målet','Byt vem som startar med fördel efter varje duell.')], special='double')
C[-1]['goals']=[(50,0),(50,100)]

add('w23', '2-mot-1-blir-2-mot-2', ['2 mot 1 blir 2 mot 2'],
    'Två anfallare mot en · Andra försvararen startar vid sidan',
    [p('A1',B,(0,(37,78)),(2,(37,72)),(4,(43,61)),(6,(48,49)),(8,(44,37)),(10,(46,24))),
     p('A2',B,(0,(63,78)),(2,(63,73)),(4,(59,64)),(6,(55,52)),(8,(54,40)),(10,(52,28))),
     p('F1',R,(0,(50,43)),(2,(50,43)),(4,(48,51)),(6,(49,55)),(8,(48,45)),(10,(49,39))),
     p('F2',R,(0,(94,47)),(3,(94,47)),(4.5,(82,49)),(6,(69,51)),(8,(59,45)),(10,(55,38))),
     p('MV',R,(0,(50,5)),(18,(50,5)))],
    [(0,(37,78)),(1,(37,75)),(2.5,(50,68)),(3.5,(50,57)),(4.4,(44,60)),(5.2,(58,57)),(6.5,(54,46)),(8,(53,35)),(9,(49,25)),(10,(48,10)),(11,(48,2)),(18,(48,2))],
    [(0,'2 mot 1 – anfallarna startar med boll','Den andra försvararen väntar utanför spelplanen.'),
     (2,'Driv mot första försvararen','Bind honom innan du väljer att passa.'),
     (3.5,'Spela till medspelaren när försvararen kliver','Den fria anfallaren går framåt med fart.'),
     (4.5,'Andra försvararen startar in','Nu förändras övningen till 2 mot 2.'),
     (7,'Fortsätt anfalla – försvararna pressar ihop','Skapa avslut innan försvaret hinner organisera sig.'),
     (11,'Avslut mot målvakten','Vid bollvinst spelar försvararna till tränaren för poäng.')])

add('w24', 'duell-med-ryggen-mot-mal', ['Duell med ryggen mot mål'],
    'Passare bakom · Anfallare vänd från mål · Försvarare i ryggen',
    [p('A',B,(0,(50,38)),(2,(50,38)),(3.5,(50,37)),(5,(45,35)),(6.5,(39,30)),(8,(40,20)),(9,(42,13))),
     p('F',R,(0,(50,49)),(2,(50,49)),(4,(50,46)),(5.5,(48,40)),(7,(44,34)),(8.5,(43,24))),
     p('P',G,(0,(50,79)),(18,(50,79))),p('MV',R,(0,(50,5)),(18,(50,5)))],
    [(0,(50,77)),(2,(50,77)),(3.3,(50,40)),(4.5,(50,38)),(5.5,(44,35)),(6.7,(40,30)),(8,(41,20)),(9,(42,10)),(10,(42,2)),(18,(42,2))],
    [(0,'Passaren spelar in till anfallaren','Anfallaren tar emot med ryggen mot mål.'),
     (3.3,'Försvararen ligger bakom anfallaren','Känn kontakten och håll kroppen mellan boll och motståndare.'),
     (5,'Vänd bort från försvararen','Första touchen går åt sidan och framåt mot mål.'),
     (7,'Skapa en fri skottlinje','Försvararen följer efter och försöker störa avslutet.'),
     (10,'Avslut – försvararen spelar tillbaka vid bollvinst','Byt roller efter tre försök.')])

add('w25', '1-mot-1-mot-fyra-portar', ['1 mot 1 mot fyra portar'],
    'Kvadrat · En port på varje sida · Vinnaren anfaller direkt',
    [p('A',B,(0,(50,34)),(1.5,(50,34)),(3,(39,31)),(4.5,(34,39)),(6,(39,47)),(8,(50,57)),(9,(50,64)),(11,(42,49)),(13,(31,40))),
     p('F',R,(0,(58,39)),(1.5,(58,39)),(3,(48,36)),(4.5,(40,39)),(6,(43,45)),(8,(47,51)),(9,(50,56)),(11,(44,49)),(13,(30,40)))],
    [(0,(50,34)),(1.5,(50,34)),(3,(39,31)),(4.5,(34,39)),(6,(39,47)),(8,(49,59)),(9,(50,66)),(10,(50,67)),(10.8,(48,58)),(12,(39,48)),(13,(30,40)),(14,(6,40)),(18,(6,40))],
    [(0,'1 mot 1 i kvadraten – fyra portar är mål','Anfallaren börjar med boll och väljer vilken port som helst.'),
     (2,'Finta mot vänsterporten','Försvararen stänger vägen utan att lämna hela ytan.'),
     (5,'Byt riktning och öka tempot','Anfallaren byter till den nedre porten.'),
     (9,'Bollvinst – rollerna skiftar direkt','Den som vinner bollen anfaller omedelbart.'),
     (14,'Driv hela bollen genom porten','Byt efter 45 sekunder.')], special='four-gates')
C[-1]['goals']=[]

add('w26', 'sprintduell-runt-kappen', ['Sprintduell runt käppen'],
    'Två startkäppar 30 m från mål · Båda startar med ryggen mot mål',
    [p('A',B,(0,(30,58)),(1.5,(30,58)),(3,(24,51)),(4.5,(22,42)),(6,(29,34)),(8,(40,25)),(10,(47,15)),(11,(49,8))),
     p('B',R,(0,(70,58)),(1.5,(70,58)),(3,(76,51)),(4.5,(78,43)),(6,(71,37)),(8,(61,30)),(10,(55,23)),(11,(52,18))),
     p('MV',R,(0,(50,5)),(18,(50,5))),p('T',G,(0,(50,83)),(18,(50,83)))],
    [(0,(50,81)),(1,(50,72)),(2,(50,60)),(3,(50,49)),(4,(48,43)),(5,(35,36)),(6,(32,31)),(7,(36,27)),(8,(41,20)),(9,(46,12)),(10,(48,5)),(18,(48,5))],
    [(0,'Tränaren spelar bollen mot mål','Spelarna vänder först efter att bollen lämnat foten.'),
     (2,'Sprinta runt varsin käpp','Ta en båge runt käppen – spring inte rakt igenom den.'),
     (5,'Blå kommer först till bollen','Orange jagar tillbaka och försöker försvara.'),
     (7,'Första touchen går framåt mot mål','Skydda bollen medan försvararen kommer ikapp.'),
     (10,'Avslut mot målvakten','Byt startkäpp och roller efter varje försök.')], special='sprint-poles')

_base = makebase
def makebase(c):
    original = c.get('special')
    c['special'] = None
    im = _base(c)
    c['special'] = original
    d = ImageDraw.Draw(im)
    def pole(pos):
        x,y=xy(pos); d.line((x,y-16,x,y+18),fill='#ffd66d',width=5)
    z=original
    if z == 'four-gates':
        for x,y,dx,dy in [(50,7,14,0),(50,93,14,0),(7,50,0,14),(93,50,0,14)]:
            px,py=xy((x,y));
            if dx: d.line((px-dx,py-14,px-dx,py+14),fill='#ffcc67',width=5); d.line((px+dx,py-14,px+dx,py+14),fill='#ffcc67',width=5)
            else: d.line((px-14,py-dy,px+14,py-dy),fill='#ffcc67',width=5); d.line((px-14,py+dy,px+14,py+dy),fill='#ffcc67',width=5)
    elif z == 'sprint-poles':
        pole((30,57)); pole((70,57))
    return im

if __name__ == '__main__':
    for c in C:
        c['base'] = makebase(c)
        for t in [3,7,10]: frame(c,t).resize((540,540)).save(ROOT/f"filmwork/{c['id']}-{t}.jpg")
        path=OUT/(c['slug']+'.mp4')
        proc=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s','1080x1080','-r','30','-i','-','-an','-c:v','libx264','-threads','4','-preset','fast','-crf','17','-pix_fmt','yuv420p','-movflags','+faststart',str(path)],stdin=subprocess.PIPE)
        for f in range(c['seconds']*30): proc.stdin.write(frame(c,f/30).tobytes())
        proc.stdin.close(); assert proc.wait()==0
        print(c['id'], flush=True)
