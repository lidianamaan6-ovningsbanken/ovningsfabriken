from PIL import Image,ImageDraw,ImageFont
from pathlib import Path
import subprocess,bisect,json,math,sys,os
ROOT=Path(os.environ.get('OF_FILM_OUTPUT','./film-output')).resolve();OUT=ROOT/'filmer';OUT.mkdir(parents=True,exist_ok=True);(ROOT/'filmwork').mkdir(exist_ok=True)
B='#32cbea';R='#fb6b65';G='#b9edbf'
logo=Image.open(os.environ.get('OF_LOGO_PNG','/tmp/finish-logo.png')).convert('RGBA');logo=logo.crop(logo.getbbox())
fonts={}
def F(n,b=False):
 k=(n,b)
 if k not in fonts:fonts[k]=ImageFont.truetype('/usr/share/fonts/truetype/noto/NotoSans-'+('Bold' if b else 'Regular')+'.ttf',n)
 return fonts[k]
def xy(p):return (155+7.7*p[0],240+6.5*p[1])
def at(tr,t):
 i=bisect.bisect_right([p[0] for p in tr],t)
 if not i:return tr[0][1]
 if i==len(tr):return tr[-1][1]
 a,p=tr[i-1];b,q=tr[i];w=(t-a)/(b-a)
 return tuple(x+(y-x)*w for x,y in zip(p,q))
def p(l,c,*tr):return dict(label=l,color=c,tr=list(tr))
def fixed(l,c,pos):return p(l,c,(0,pos))
def mv(x=50,y=5):return p('MV',G,(0,(x,y)),(6,(x,y)),(11,(x+5,y)),(20,(x,y)))
C=[]
def add(id,slug,title,setup,players,ball,phases,**kwargs):C.append(dict(id=id,slug=slug,title=title,setup=setup,players=players,balls=[ball],phases=phases,seconds=18,goals=[(50,0)],**kwargs))
add('t07','Rolig-avslutsovning-i-par',['Rolig avslutsövning','I par'],'Ett mål i mitten · Två köer · En målvakt',
[p('A',G,(0,(28,12)),(2,(28,12)),(6,(22,33)),(11,(28,71))),p('B',B,(0,(57,75)),(3,(57,75)),(5,(55,64)),(7,(48,56)),(9,(46,53)),(12,(65,20))),fixed('A',G,(23,7)),fixed('A',G,(18,4)),fixed('B',B,(64,82)),fixed('B',B,(69,89)),p('MV',R,(0,(50,36)),(6,(50,36)),(8,(54,36)))],
[(0,(28,13)),(2,(28,13)),(3,(16,29)),(4,(26,49)),(5,(55,62)),(6,(52,61)),(7,(48,56)),(8,(45,53)),(8.8,(45,37)),(18,(45,37))],
[(0,'A spelar en lång boll runt målet','B väntar framför målet och förbereder avslutet.'),(2,'Bollen går i båge runt målet','Anpassa bollens tyngd till mottagarens löpning.'),(5,'Ta emot och förbered avslutet','Avsluta direkt eller efter en touch.'),(8,'Lågt avslut i hörnet','Följ upp returen om målvakten räddar.'),(11,'Byt kö efter din aktion','Vilket lag gör flest mål på fem minuter?')],special='central')
add('t13','Djupledspassningar-med-baglopning',['Djupledspassningar','Med båglöpning'],'Passning · Tillbakaspel · Djupledslöpning · Inlägg',
[p('1',B,(0,(50,85)),(3,(50,83)),(7,(52,62))),p('2',B,(0,(50,57)),(3,(50,57)),(4,(66,62)),(5,(85,53)),(7,(93,26)),(9,(90,18))),fixed('3',G,(75,48)),p('4',B,(0,(44,42)),(6,(44,36)),(9,(44,20)),(10,(47,17))),fixed('1',B,(45,92)),fixed('2',B,(48,65)),mv()],
[(0,(50,83)),(1,(50,83)),(2,(50,59)),(3,(50,59)),(4,(50,81)),(5,(75,50)),(6,(75,50)),(7,(93,28)),(8,(92,23)),(9,(90,20)),(10,(47,19)),(11,(47,-2)),(18,(47,-2))],
[(0,'1 spelar till 2','2 lägger tillbaka till startspelaren.'),(4,'1 spelar ut till 3','2 börjar sin båglöpning utanför kantspelaren.'),(6,'3 spelar framför löparen','Djupledspassningen ska ge 2 fart framåt.'),(9,'Spela in i straffområdet','Möt inlägget i fart och gå till avslut.'),(12,'Alla går en station vidare','Växla sida och behåll samma passningsmönster.')])
add('t18','Y-passning-dubbel-med-avslut',['Y-passning dubbel','Med avslut'],'Två Y-formationer · Två målvakter · Samtidigt spel',
[p('A',B,(0,(27,47)),(5,(27,45))),p('B',B,(0,(27,30)),(3,(27,30)),(6,(26,17))),p('C',B,(0,(8,30)),(3,(8,30)),(5,(12,27))),fixed('A',B,(22,48)),fixed('A',B,(32,48)),p('A',R,(0,(73,53)),(5,(73,55))),p('B',R,(0,(73,70)),(3,(73,70)),(6,(74,83))),p('C',R,(0,(92,70)),(3,(92,70)),(5,(88,73))),fixed('A',R,(68,52)),fixed('A',R,(78,52)),mv(27,5),mv(73,95)],
[(0,(27,45)),(1,(27,45)),(2,(27,32)),(3,(27,32)),(4,(8,29)),(5,(12,27)),(6,(26,19)),(7,(26,17)),(8,(25,-2)),(18,(25,-2))],
[(0,'A spelar upp till B','Samma mönster går samtidigt åt båda hållen.'),(3,'B lägger av ut på kanten','C möter bollen med rättvänd kropp.'),(5,'B löper in mot mål','C passar framför anfallaren.'),(7,'Avsluta på första eller andra touch','Låt första touchen förbereda skottet.'),(10,'Följ passningen till nästa station','Vilken grupp gör flest mål?')],special='double')
C[-1]['goals']=[(27,0),(73,100)];C[-1]['balls'].append([(t,(100-x,100-y)) for t,(x,y) in C[-1]['balls'][0]])
add('t30','Avslutstraning-med-forsvar',['Avslutsträning','Med försvar'],'Anfallare runt boxen · Två försvarare · Målvakt',
[p('1',B,(0,(50,78)),(4,(50,69)),(10,(46,43))),p('2',B,(0,(15,48)),(3,(15,48)),(6,(17,30))),p('3',B,(0,(85,48)),(6,(85,48)),(7,(83,38))),p('4',B,(0,(43,43)),(6,(43,35)),(8,(45,18))),p('5',B,(0,(65,43)),(7,(65,27)),(9,(65,19))),fixed('6',B,(8,56)),fixed('7',B,(92,55)),p('1',R,(0,(37,28)),(5,(32,25)),(8,(36,21))),p('2',R,(0,(66,28)),(6,(70,25)),(9,(60,20))),mv()],
[(0,(50,76)),(1,(50,76)),(2,(15,50)),(3,(15,50)),(4,(50,69)),(5,(85,50)),(6,(85,48)),(7,(83,38)),(8,(45,20)),(8.6,(45,18)),(9.3,(45,-2)),(18,(45,-2))],
[(0,'Spela runt straffområdet','Två försvarare skyddar ytan framför målvakten.'),(4,'Flytta bollen innan försvaret hinner','Växla kant och skapa en ny passningsvinkel.'),(7,'Löp in i boxen när bollen är på kanten','Sök ett tidigt avslut mellan försvararna.'),(9.3,'Direktavslut ger två poäng','Övriga mål ger en poäng.'),(12,'Vid bollvinst spelar försvaret ut','Spela till mittspelaren och starta om.')])
add('t31','Avsluta-med-fel-fot',['Avsluta med fel fot','Träna den svagare foten'],'Tre köer · Portar och dockor · Ett stort mål',
[p('1',B,(0,(20,83)),(2,(20,83)),(4,(20,60)),(6,(29,48)),(7,(32,29)),(8,(32,27)),(12,(25,24))),p('2',R,(0,(80,83)),(9,(80,83)),(11,(80,60)),(13,(71,48)),(14,(68,29)),(15,(68,27))),fixed('1',B,(15,91)),fixed('1',B,(10,96)),fixed('2',R,(85,91)),fixed('2',R,(90,96)),fixed('3',B,(50,83)),fixed('3',B,(50,90)),fixed('3',B,(50,96)),mv()],
[(0,(20,81)),(2,(20,81)),(4,(20,58)),(6,(29,46)),(7,(32,27)),(8,(32,25)),(8.7,(44,-2)),(9,(80,81)),(11,(80,58)),(13,(71,46)),(14,(68,27)),(15,(68,25)),(15.7,(55,-2)),(22,(55,-2))],
[(0,'Vänster kö avslutar med höger','Driv fram och genom porten.'),(5,'Förbi dockan – förbered rätt fot','Sätt stödjefoten bredvid bollen.'),(8,'Avsluta med högerfoten','Mål med den svagare foten ger två poäng.'),(9,'Höger kö avslutar med vänster','Driv igenom porten och förbi dockan.'),(15,'Avsluta med vänsterfoten','Träffa mitt på bollen och följ igenom.')],special='ports')
C[-1]['seconds']=22
add('t32','Kombination-runt-dockor-dubbel',['Kombination runt dockor','Dubbel med avslut'],'A till B · Avlägg till C · Vändning och avslut',
[p('A',B,(0,(25,46)),(5,(25,38))),fixed('B',G,(25,30)),p('C',B,(0,(8,39)),(2,(8,39)),(3,(11,28)),(4,(18,23)),(5,(30,24)),(7,(29,16))),fixed('A',B,(20,48)),fixed('A',B,(30,48)),p('A',R,(0,(75,54)),(5,(75,62))),fixed('B',G,(75,70)),p('C',R,(0,(92,61)),(2,(92,61)),(3,(89,72)),(4,(82,77)),(5,(70,76)),(7,(71,84))),fixed('A',R,(70,52)),fixed('A',R,(80,52)),mv(25,5),mv(75,95)],
[(0,(25,44)),(1,(25,44)),(2,(25,32)),(3,(25,32)),(5,(30,26)),(6,(30,22)),(7,(29,18)),(8,(25,-2)),(18,(25,-2))],
[(0,'A passar upp till B','Två grupper arbetar samtidigt åt varsitt håll.'),(2,'C startar en båglöpning','Löp runt dockan och bli spelbar.'),(3,'B lägger av till C','Väg av passningen så att C kan vända.'),(6,'Vänd upp och avsluta','Använd första eller andra touchen till skottet.'),(10,'Alla går en station vidare','Byt roller och behåll tajmingen i kombinationen.')],special='double-dummies')
C[-1]['goals']=[(25,0),(75,100)];C[-1]['balls'].append([(t,(100-x,100-y)) for t,(x,y) in C[-1]['balls'][0]])
add('t33','3-mot-5-anfallsspel',['3 mot 5 anfallsspel','Anfall via kanterna'],'Tre centrala + två på kanten · Fyra försvarare + MV',
[p('1',B,(0,(50,76)),(3,(50,63)),(6,(45,30)),(9,(43,18))),p('2',B,(0,(31,64)),(4,(31,53)),(8,(32,19))),p('3',B,(0,(69,64)),(4,(69,54)),(8,(65,20))),p('V',B,(0,(8,47)),(3,(8,47)),(7,(8,28))),p('H',B,(0,(92,47)),(3,(92,47)),(7,(92,28))),p('1',R,(0,(25,31)),(6,(21,25))),p('2',R,(0,(42,28)),(7,(37,21))),p('3',R,(0,(62,28)),(7,(58,21))),p('4',R,(0,(78,31)),(7,(76,23))),mv()],
[(0,(50,74)),(1,(50,74)),(2,(31,62)),(3,(8,45)),(4,(8,40)),(5,(8,33)),(6,(8,28)),(8,(32,21)),(9,(32,19)),(9.7,(45,-2)),(18,(45,-2))],
[(0,'Anfallet har tre centralt och två brett','Fyra försvarare och målvakt skyddar målet.'),(3,'Spela ut på kanten','Kantspelaren får inte tacklas under inlägget.'),(6,'Fyll främre och bortre stolpen','Anfallarna tajmar sina löpningar in i boxen.'),(9,'Avsluta inom sex passningar','Inlägget ska komma innan försvaret hinner hem.'),(12,'Vid bollvinst spelar rött ut','Boll över mittlinjen ger försvaret en poäng.')])
add('t34','Overlapp-med-avslut',['Överlapp','Med avslut'],'60 × 45 m · Sex mot sex + två målvakter',
[p('1',B,(0,(22,60)),(3,(30,51)),(4,(38,45)),(6,(43,36))),p('2',B,(0,(15,77)),(2,(15,72)),(4,(9,51)),(6,(11,30)),(8,(14,22))),p('3',B,(0,(49,56)),(4,(49,42)),(8,(42,17))),p('4',B,(0,(74,55)),(8,(68,20))),fixed('5',B,(40,75)),fixed('6',B,(68,76)),p('1',R,(0,(23,39)),(4,(31,39)),(8,(24,27))),p('2',R,(0,(44,29)),(8,(44,22))),p('3',R,(0,(64,29)),(8,(62,22))),fixed('4',R,(82,38)),fixed('5',R,(40,51)),fixed('6',R,(69,50)),mv(),mv(50,95)],
[(0,(22,58)),(1,(22,58)),(3,(30,49)),(4,(38,43)),(6,(11,28)),(7,(12,25)),(8,(14,22)),(9,(42,19)),(9.7,(42,17)),(10.4,(45,-2)),(18,(45,-2))],
[(0,'Bollhållaren driver inåt','Det öppnar ytan längs sidlinjen.'),(2,'Medspelaren startar överlappet','Löp utanför bollhållaren med fart.'),(5,'Spela fram den överlappande spelaren','Passa framför löparen i fri yta.'),(8,'Inlägg och avslut','Fyll ytan framför mål.'),(11,'Mål efter överlapp ger två poäng','Övriga mål ger en poäng. Fortsätt spelet.')],special='full')
C[-1]['goals']=[(50,0),(50,100)]
add('t35','Avslut-efter-inlagg-A-B-C',['Avslut efter inlägg','A, B och C'],'Tre stationer · Inlägg från kanten · Ett stort mål',
[p('A',B,(0,(28,81)),(3,(28,75)),(6,(36,49)),(9,(43,17))),p('B',B,(0,(51,59)),(4,(51,59)),(7,(65,37)),(9,(68,18))),p('C',G,(0,(87,55)),(5,(87,55)),(7,(91,32)),(8,(92,25))),fixed('A',B,(22,89)),fixed('A',B,(16,94)),mv()],
[(0,(28,79)),(1,(28,79)),(3,(51,61)),(4,(51,61)),(5,(87,53)),(6,(89,43)),(7,(91,30)),(8,(92,23)),(9,(43,19)),(9.7,(43,17)),(10.4,(47,-2)),(18,(47,-2))],
[(0,'A passar till B','B öppnar kroppen mot C på kanten.'),(4,'B spelar vidare till C','A och B startar sina löpningar mot boxen.'),(6,'C driver och tittar upp','Välj mottagare före inlägget.'),(8,'En mot främre – en mot bortre','Löp i båge för att möta bollen.'),(10.4,'Avslut och rotation medsols','A går till B, B till C och C till A.')])
add('t36','Anfallsovning-med-ytterbackar',['Anfallsövning','Med ytterbackar'],'Nio anfallare · Fyra försvarare · En målvakt',
[fixed('MB',B,(38,88)),fixed('MB',B,(63,88)),p('VB',B,(0,(10,76)),(5,(10,76)),(9,(8,48))),p('HB',B,(0,(90,76)),(5,(90,76)),(7,(93,47)),(9,(94,25))),p('VY',B,(0,(16,45)),(6,(16,45)),(8,(22,40)),(10,(33,18))),p('HY',B,(0,(83,45)),(6,(91,43)),(8,(76,36)),(10,(62,19))),fixed('MF',B,(43,65)),p('MF',B,(0,(60,62)),(6,(60,62)),(10,(52,37))),p('9',B,(0,(50,42)),(6,(50,42)),(10,(47,16))),fixed('1',R,(24,24)),fixed('2',R,(42,23)),fixed('3',R,(62,23)),fixed('4',R,(80,24)),mv()],
[(0,(38,86)),(1,(38,86)),(3,(43,63)),(4,(43,63)),(5,(60,60)),(6,(60,60)),(7,(93,45)),(8,(93,35)),(9,(94,23)),(10,(47,18)),(10.7,(47,16)),(11.4,(45,-2)),(18,(45,-2))],
[(0,'Mittbacken startar via mittfältet','Mittfältarna kombinerar centralt.'),(5,'Ytterbackarna startar längs kanten','Spela framför den löpande ytterbacken.'),(7,'Yttern går först ut – sedan in','Anfallaren fyller främre stolpen.'),(9,'Fyll boxen och säkra returen','Vänsterytter bortre, mittfältare vid halvmånen.'),(11.4,'Avslut – upprepa från andra sidan','Den andra mittfältaren ligger kvar som ankare.')])
add('t37','Everton-avslutsovning',['Everton','Avslutsövning'],'A till B till C · Tillbaka till A · Inlägg från D',
[p('A',B,(0,(50,84)),(3,(50,78)),(5,(49,57)),(7,(49,52))),p('B',B,(0,(50,54)),(3,(50,54)),(6,(44,35)),(9,(41,17))),p('C',B,(0,(16,51)),(4,(16,51)),(7,(26,37)),(9,(65,18))),p('D',G,(0,(88,46)),(6,(88,46)),(8,(93,28))),fixed('A',B,(44,92)),fixed('A',B,(56,92)),mv()],
[(0,(50,82)),(1,(50,82)),(2,(50,56)),(3,(50,56)),(4,(16,53)),(5,(49,59)),(6,(49,59)),(7,(90,40)),(8,(93,26)),(9,(41,19)),(9.7,(41,17)),(10.4,(46,-2)),(18,(46,-2))],
[(0,'A passar till B','B lägger ut till C på vänsterkanten.'),(4,'C spelar tillbaka till A','A har löpt fram och öppnar mot höger.'),(6,'A hittar D på högerkanten','B och C löper in i straffområdet.'),(8,'D slår inlägg mellan MV och försvar','Tajma anfallarnas löpningar mot bollen.'),(10.4,'Avslut – gå en station vidare','Jobba med få touch och snabb bollförflyttning.')])
add('t38','Man-City-avslutsovning',['Man City','Avslutsövning'],'A till B till C · Diagonal mellan dockorna · Avslut',
[fixed('A',B,(50,86)),fixed('B',G,(50,57)),fixed('C',G,(86,48)),p('D',B,(0,(15,47)),(4,(15,47)),(5,(18,34)),(6,(30,25)),(7,(43,27)),(9,(45,17))),fixed('A',B,(44,93)),fixed('A',B,(56,93)),mv()],
[(0,(50,84)),(1,(50,84)),(2,(50,59)),(3,(50,59)),(4,(86,50)),(5,(86,50)),(7,(43,29)),(8,(44,23)),(9,(45,19)),(9.7,(45,-2)),(18,(45,-2))],
[(0,'A passar upp till B','B lägger ut bollen till C på höger sida.'),(4,'D startar när C tar emot','Löp i båge in mellan dockorna.'),(5,'C slår diagonalen framför löparen','Passningen ska ge D möjlighet att avsluta.'),(8,'Första touchen förbereder skottet','Avsluta direkt när passningen ger rätt läge.'),(10,'Byt station medsols','Behåll tajmingen mellan passning och löpning.')],special='dummies')
def makebase(c):
 im=Image.new('RGB',(1080,1080),'#0a1e17');d=ImageDraw.Draw(im)
 sm=logo.copy();sm.thumbnail((300,75));im.paste(sm,(39,9),sm)
 d.text((1040,44),'AVSLUT OCH MÅL',font=F(19,True),fill='#adc5b6',anchor='rm')
 for i,t in enumerate(c['title']):d.text((39,125+i*57),t,font=F(44 if i==0 else 35,True),fill='#edf4e8',anchor='lm')
 d.text((540,215),c['setup'],font=F(18,True),fill='#c4dac8',anchor='mm')
 for j in range(12):d.rectangle((155,240+j*650/12,925,240+(j+1)*650/12),fill=('#286843','#25623e')[j%2])
 d.rectangle((155,240,925,890),outline='#b2cdb1',width=3)
 def line(pts):d.line([xy(a) for a in pts],fill='#b2cdb1',width=2)
 def goal(x,y):
  a=xy((x-7,y-2 if y==0 else y));b=xy((x+7,y if y==0 else y+2));d.rectangle((*a,*b),outline='#eef4d9',width=3)
 if c.get('special')=='central':
  a=xy((43,34));b=xy((57,37));d.rectangle((*a,*b),outline='#eef4d9',width=3);line([(25,38),(25,61),(75,61),(75,38)])
 else:
  for x,y in c['goals']:
   goal(x,y)
   if y==0:line([(x-22,0),(x-22,20),(x+22,20),(x+22,0)])
   else:line([(x-22,100),(x-22,80),(x+22,80),(x+22,100)])
 if c.get('special') in ['double','double-dummies','full']:line([(0,50),(100,50)])
 def dummy(pos):
  x,y=xy(pos);d.rounded_rectangle((x-9,y-18,x+9,y+14),radius=5,fill='#ebc451',outline='#fff3bc',width=2);d.line((x,y+15,x,y+28),fill='#fff3bc',width=3)
 if c.get('special')=='ports':
  for x in [20,50,80]:
   for dx in [-6,6]:
    xx,yy=xy((x+dx,61));d.polygon([(xx,yy-7),(xx-6,yy+5),(xx+6,yy+5)],fill='#ff965b')
   dummy((x,43))
 if c.get('special')=='dummies':
  for x in [28,38,62,72]:dummy((x,36))
 if c.get('special')=='double-dummies':dummy((16,31));dummy((84,69))
 wm=logo.copy();wm.thumbnail((420,160));wm.putalpha(wm.getchannel('A').point(lambda a:round(a*.24)));im.paste(wm,(round(540-wm.width/2),round(565-wm.height/2)),wm)
 d.rounded_rectangle((40,960,1040,1056),radius=17,fill='#143526',outline='#315846',width=2)
 return im
def frame(c,t):
 im=c['base'].copy();d=ImageDraw.Draw(im)
 for pl in c['players']:
  x,y=xy(at(pl['tr'],t));r=18
  d.ellipse((x-r,y-r,x+r,y+r),fill=pl['color'],outline='#e5efd8',width=2)
  d.text((x,y),pl['label'],font=F(12,True),fill='#153b2b',anchor='mm')
 for tr in c['balls']:
  x,y=xy(at(tr,t));d.ellipse((x-8,y-8,x+8,y+8),fill='#fffef0',outline='#142d22',width=2);d.regular_polygon((x,y,3),5,fill='#162d23',rotation=t*60)
 _,h,s=max([p for p in c['phases'] if p[0]<=t],key=lambda p:p[0])
 d.text((62,992),h,font=F(26,True),fill='#eef5e8',anchor='lm');d.text((62,1032),s,font=F(21),fill='#b4cbbb',anchor='lm')
 return im
if __name__=='__main__':
 (ROOT/'filmwork/catalog.json').write_text(json.dumps([{k:c[k] for k in ['id','slug','title']} for c in C],ensure_ascii=False))
 for c in C:
  if len(sys.argv)>1 and c['id'] not in sys.argv[1:]:continue
  c['base']=makebase(c)
  for t in [0,5,9]:frame(c,t).resize((540,540)).save(ROOT/f"filmwork/{c['id']}-{t}.jpg")
  path=OUT/(c['slug']+'.mp4');proc=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s','1080x1080','-r','30','-i','-','-an','-c:v','libx264','-threads','4','-preset','fast','-crf','17','-pix_fmt','yuv420p','-movflags','+faststart',str(path)],stdin=subprocess.PIPE)
  for f in range(c['seconds']*30):proc.stdin.write(frame(c,f/30).tobytes())
  proc.stdin.close();assert proc.wait()==0
  print(c['id'],flush=True)
