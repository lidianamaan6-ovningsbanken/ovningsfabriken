from render_avslut_base import *
C.clear()
add('t39','Bayern-avslutsovning',['Bayern','Avslutsövning'],'Lång passning · Avlägg · Diagonal löpning · Avslut',
[p('A',B,(0,(12,68)),(3,(12,68)),(5,(34,54)),(7,(46,45))),p('B',B,(0,(88,68)),(5,(88,68)),(7,(77,44)),(9,(61,19)),(10,(60,17))),fixed('C',G,(50,35)),fixed('D',G,(50,88)),fixed('A',B,(8,76)),fixed('B',B,(92,76)),mv()],
[(0,(12,66)),(1,(12,66)),(3,(88,66)),(4,(88,66)),(5,(50,37)),(6,(50,37)),(7,(46,47)),(8,(46,47)),(9,(61,21)),(10,(60,19)),(10.7,(54,-2)),(13,(50,86)),(18,(50,86))],
[(0,'A slår den långa passningen till B','Anpassa tyngden så att B kan spela vidare.'),(4,'B spelar in till C','A löper framåt för att få avlägget.'),(6,'C lägger av till A på en touch','B startar sin diagonala löpning bakom försvaret.'),(8,'A spelar framför B i djupled','Löp bakom och gå mot mål.'),(10.7,'B avslutar – D spelar nästa boll','Rotera stationer efter aktionen.')],special='bayern')
add('t40','Avslut-inlagg-fran-bada-kanter',['Avslut efter inlägg','Från båda kanter'],'Två banor · Främre och bortre stolpen · Returboll',
[p('A',B,(0,(46,76)),(3,(46,76)),(6,(57,42)),(8,(62,18)),(11,(65,23))),p('B',B,(0,(30,58)),(4,(30,58)),(8,(39,18)),(11,(43,22))),p('C',G,(0,(12,51)),(4,(12,51)),(7,(9,22))),p('A',R,(0,(56,79)),(13,(56,79)),(16,(43,42)),(18,(38,18))),p('B',R,(0,(70,58)),(14,(70,58)),(18,(61,18)),(21,(58,22))),p('C',G,(0,(88,51)),(14,(88,51)),(17,(91,22))),fixed('T',G,(73,3)),mv()],
[(0,(46,74)),(1,(46,74)),(2,(30,60)),(3,(30,60)),(4,(12,53)),(5,(11,43)),(7,(9,24)),(8,(39,20)),(8.7,(39,18)),(9.4,(44,-2)),(10,(73,5)),(11,(43,24)),(11.7,(51,-2)),(12,(56,77)),(13,(56,77)),(14,(70,60)),(15,(88,49)),(17,(91,24)),(18,(61,20)),(18.7,(61,18)),(19.4,(56,-2)),(20,(73,5)),(21,(58,24)),(22,(49,-2)),(26,(49,-2))],
[(0,'A till B – vidare till C på vänsterkanten','A och B börjar löpa in i straffområdet.'),(5,'C förbi käppen – hårt och lågt inlägg','Fyll främre och bortre stolpen.'),(9.4,'Tränaren spelar in en returboll','Var redo att avsluta igen direkt.'),(12,'Starta från högerkanten','Samma mönster från den andra sidan.'),(19.4,'Ny returboll från tränaren','Följ upp avslutet och byt station.')],special='wing-poles')
C[-1]['seconds']=26
add('t41','Tavling-1-mot-1-plus-avslut',['Tävling 1 mot 1','Med avslut'],'Två passningsmönster · En duellruta · Stort mål',
[fixed('A',B,(24,89)),fixed('B',B,(20,71)),fixed('C',B,(38,63)),fixed('K',B,(8,53)),p('1',B,(0,(44,79)),(5,(44,79)),(7,(46,42)),(8,(45,38)),(9,(34,28)),(10,(37,20))),fixed('A',R,(76,89)),fixed('B',R,(80,71)),fixed('C',R,(62,63)),fixed('K',R,(92,53)),p('1',R,(0,(56,79)),(5,(56,79)),(7,(54,43)),(8,(52,37)),(10,(43,24))),mv()],
[(0,(24,87)),(1,(24,87)),(2,(20,69)),(3,(38,61)),(4,(8,51)),(5,(8,51)),(7,(46,44)),(8,(45,40)),(9,(34,30)),(10,(37,22)),(10.7,(45,-2)),(18,(45,-2))],
[(0,'Båda lagen passar A till B till C','Passningsmönstren går samtidigt på varsin sida.'),(4,'C spelar ut till kanten','Kantspelaren förbereder inspelet i rutan.'),(6,'Första bollen i rutan blir spelbollen','En spelare från varje lag sprintar till duellen.'),(8,'Blått först – anfall i en mot en','Rött försvarar och styr bort från mitten.'),(10.7,'Avslut i stora målet ger poäng','Vid röd bollvinst kan rött kontra mot småmålen.')],special='duel-box')
C[-1]['balls'].append([(0,(76,87)),(1,(76,87)),(2,(80,69)),(3,(62,61)),(4,(92,51)),(18,(92,51))])
add('t42','Avslut-pa-djupled',['Avslut','På djupled'],'B till A till C · Avlägg till B · D löper bakom',
[p('B',B,(0,(52,87)),(3,(52,83)),(5,(52,59)),(7,(52,56))),fixed('A',G,(58,65)),p('C',G,(0,(47,37)),(2,(47,37)),(4,(47,46))),p('D',B,(0,(17,44)),(6,(17,44)),(7,(22,29)),(8,(35,21)),(9,(37,19))),fixed('B',B,(46,94)),fixed('B',B,(58,94)),mv()],
[(0,(52,85)),(1,(52,85)),(2,(58,67)),(3,(58,67)),(4,(47,48)),(5,(52,61)),(6,(52,61)),(8,(35,23)),(9,(37,21)),(9.7,(57,-2)),(18,(57,-2))],
[(0,'B passar till A','C kommer mot bollen från straffområdet.'),(3,'A hittar C som möter','C lägger av till B som har löpt fram.'),(6,'D startar när B tar emot','B söker passningen bakom käppen.'),(8,'Passningen framför djupledslöparen','D tar emot i fart och förbereder avslutet.'),(9.7,'Avsluta lågt i bortre hörnet','Alla går en station vidare.')],special='deep-pole')
add('t43','City-avslut-dubbel-variant',['City avslut','Dubbel variant'],'Två mål på samma kortsida · Två banor · Andraboll',
[fixed('A',B,(23,80)),fixed('B',G,(24,52)),p('C',B,(0,(12,62)),(3,(12,62)),(5,(20,42)),(10,(28,26))),p('D',B,(0,(40,46)),(3,(40,46)),(5,(34,26)),(6,(30,18))),fixed('T',G,(6,14)),fixed('A',B,(18,89)),fixed('A',R,(77,80)),fixed('B',G,(76,52)),p('C',R,(0,(88,62)),(3,(88,62)),(5,(80,42)),(10,(72,26))),p('D',R,(0,(60,46)),(3,(60,46)),(5,(66,26)),(6,(70,18))),fixed('T',G,(94,14)),fixed('A',R,(82,89)),mv(25,5),mv(75,5)],
[(0,(23,78)),(1,(23,78)),(2,(24,54)),(3,(12,60)),(4,(12,60)),(5,(34,28)),(6,(30,20)),(7,(25,-2)),(8,(6,16)),(9,(6,16)),(10,(28,28)),(11,(28,26)),(12,(30,-2)),(18,(30,-2))],
[(0,'Två banor spelar samtidigt','A passar upp och anfallaren lägger av.'),(3,'Djupledspassning framför löparen','Avsluta med fart in mot målet.'),(7,'Första avslutet – var redo igen','Tränaren har en andra boll vid sidan.'),(9,'Tränaren spelar nästa boll direkt','Nästa spelare möter och går till avslut.'),(12,'Andra avslutet – följ passningen','Rotera roller och starta en ny repetition.')],special='city-twin')
C[-1]['goals']=[(25,0),(75,0)];C[-1]['balls'].append([(t,(100-x,y)) for t,(x,y) in C[-1]['balls'][0]])
add('t45','3-mot-2-med-kontring-till-smamal',['3 mot 2','Med kontring till småmål'],'Tre korridorer · Stort mål · Två kontringsmål',
[p('6',B,(0,(28,78)),(3,(28,70)),(5,(36,36)),(6,(39,24)),(10,(28,78)),(14,(35,51)),(19,(29,58))),p('8',B,(0,(50,81)),(4,(49,59)),(10,(50,81)),(14,(50,58)),(18,(45,64))),p('9',B,(0,(73,78)),(3,(73,61)),(4,(68,49)),(10,(73,78)),(14,(65,51)),(18,(70,65))),p('1',R,(0,(43,36)),(5,(43,29)),(10,(43,36)),(13,(42,46)),(16,(31,68)),(19,(26,87))),p('2',R,(0,(59,36)),(4,(65,45)),(10,(59,36)),(14,(60,45)),(17,(65,66)),(19,(68,87))),fixed('7',B,(8,86)),fixed('10',B,(92,86)),mv()],
[(0,(50,79)),(1,(50,79)),(3,(73,63)),(4,(68,51)),(5,(36,38)),(6,(39,26)),(7,(44,-2)),(10,(50,79)),(11,(50,79)),(12,(36,60)),(13,(42,48)),(14,(39,55)),(16,(31,70)),(17,(65,68)),(19,(68,89)),(20,(70,102)),(24,(70,102))],
[(0,'Anfallarna söker stora målet','Tre mot två och målvakt i första situationen.'),(3,'Dra försvararen – spela den fria','9 lockar ut och hittar 6 på andra sidan.'),(6,'Avsluta innan försvaret hinner flytta','Nästa grupp startar efter avslutet.'),(10,'Ny situation – försvararna vinner','Rött tar bollen och ställer om direkt.'),(16,'Kontra mot ett av småmålen','Fördröj och styr ut som försvarare.'),(20,'Poäng i småmålet – ny grupp','Börja om med tre nya anfallare.')],special='corridors')
C[-1]['seconds']=24
add('t46','6-mot-4-till-6-mot-6',['6 mot 4','Till 6 mot 6'],'Sex anfallare · Fyra försvarare · Två väntar in',
[p('1',B,(0,(16,63)),(3,(14,51)),(6,(15,32)),(10,(16,63)),(17,(25,45))),p('2',B,(0,(38,67)),(3,(38,65)),(7,(39,41)),(10,(38,67)),(17,(43,42))),p('3',B,(0,(63,67)),(7,(64,43)),(10,(63,67)),(17,(61,43))),p('4',B,(0,(85,63)),(7,(84,32)),(10,(85,63)),(17,(77,44))),p('5',B,(0,(42,44)),(6,(40,18)),(10,(42,44)),(17,(43,26))),p('6',B,(0,(60,44)),(6,(64,19)),(10,(60,44)),(17,(60,27))),p('1',R,(0,(29,27)),(6,(26,22)),(10,(29,27)),(17,(30,25))),p('2',R,(0,(43,26)),(6,(44,21)),(10,(43,26)),(17,(42,25))),p('3',R,(0,(58,26)),(6,(58,21)),(10,(58,26)),(17,(57,25))),p('4',R,(0,(73,27)),(6,(72,21)),(10,(73,27)),(17,(71,25))),p('8',R,(0,(27,89)),(10,(27,89)),(13,(35,57)),(15,(37,51)),(17,(38,48))),p('6',R,(0,(73,89)),(10,(73,89)),(13,(65,57)),(15,(66,49)),(17,(77,50)),(19,(94,50))),fixed('T',G,(50,95)),mv()],
[(0,(50,93)),(1,(50,93)),(2,(38,65)),(3,(38,65)),(4,(14,49)),(5,(14,43)),(6,(40,20)),(7,(43,-2)),(10,(50,93)),(11,(50,93)),(12,(63,65)),(13,(63,61)),(14,(66,51)),(15,(66,51)),(17,(77,52)),(19,(94,52)),(20,(98,52)),(24,(98,52))],
[(0,'Tränaren startar sex mot fyra','Två röda mittfältare väntar vid mittlinjen.'),(3,'Spela snabbt medan överläget finns','Fyll boxen och sök det tidiga avslutet.'),(10,'Ny boll – de två väntande kommer in','Nu spelar lagen sex mot sex.'),(14,'Rött vinner och söker en port','Försvararna håller ihop och stänger mitten.'),(19,'Driv eller passa genom porten','Poäng för rött – starta nästa repetition.')],special='side-gates')
C[-1]['seconds']=24
oldbase=makebase
def makebase(c):
 im=oldbase(c);d=ImageDraw.Draw(im)
 def line(ps):d.line([xy(a) for a in ps],fill='#c9d9ae',width=2)
 def pole(pos):
  x,y=xy(pos);d.line((x,y-15,x,y+17),fill='#ffd66d',width=5)
 def goal(x,y):
  a=xy((x-6,y if y else -2));b=xy((x+6,y+2 if y else 0));d.rectangle((*a,*b),outline='#edf4df',width=3)
 z=c.get('special')
 if z=='bayern':
  for x in [27,73]:pole((x-4,47));pole((x+4,47))
 elif z=='wing-poles':pole((14,36));pole((86,36))
 elif z=='duel-box':
  line([(31,38),(69,38),(69,53),(31,53),(31,38)])
  goal(12,77);goal(88,77)
 elif z=='deep-pole':pole((25,37));pole((60,61))
 elif z=='city-twin':
  line([(50,0),(50,100)]);pole((22,67));pole((78,67))
 elif z=='corridors':
  for x in [40,60]:line([(x,35),(x,100)])
  goal(30,100);goal(70,100)
 elif z=='side-gates':
  line([(0,85),(100,85)])
  for x in [5,95]:pole((x,45));pole((x,56))
 return im
if __name__=='__main__':
 (ROOT/'filmwork/catalog-next.json').write_text(json.dumps([{k:c[k] for k in ['id','slug','title']} for c in C],ensure_ascii=False))
 for c in C:
  if len(sys.argv)>1 and c['id'] not in sys.argv[1:]:continue
  c['base']=makebase(c)
  for t in [5,9,15]:frame(c,t).resize((540,540)).save(ROOT/f"filmwork/{c['id']}-{t}.jpg")
  path=OUT/(c['slug']+'.mp4');proc=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s','1080x1080','-r','30','-i','-','-an','-c:v','libx264','-threads','4','-preset','fast','-crf','17','-pix_fmt','yuv420p','-movflags','+faststart',str(path)],stdin=subprocess.PIPE)
  for f in range(c['seconds']*30):proc.stdin.write(frame(c,f/30).tobytes())
  proc.stdin.close();assert proc.wait()==0
  print(c['id'],flush=True)
