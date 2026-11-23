from render_avslut_base import *

C.clear()

add('t70', 'possession-5-mot-3-med-spelvandning',
    ['Possession 5 mot 3', 'Med spelvändning'],
    'Två rutor · 5 mot 3 · Sex passningar före spelvändning',
    [p('1', B, (0,(16,25)),(2,(16,25)),(4,(26,19)),(6,(35,28)),(8,(39,39)),(10,(63,31)),(12,(68,29)),(15,(74,38))),
     p('2', B, (0,(36,20)),(3,(36,20)),(5,(31,27)),(7,(22,35)),(9,(32,43)),(12,(59,38)),(15,(70,42))),
     p('3', B, (0,(18,46)),(4,(18,46)),(6,(30,45)),(8,(39,45)),(10,(57,45)),(13,(66,47))),
     p('4', B, (0,(37,48)),(5,(37,48)),(7,(42,40)),(9,(40,29)),(12,(62,25))),
     p('5', B, (0,(28,34)),(4,(28,34)),(6,(20,38)),(8,(31,35)),(10,(70,32)),(14,(75,46))),
     p('M', B, (0,(70,37)),(8,(70,37)),(9,(70,34)),(12,(66,30))),
     p('1', R, (0,(22,29)),(5,(22,29)),(7,(28,32)),(9,(38,34)),(12,(60,34)),(15,(65,38)),(17,(38,37))),
     p('2', R, (0,(29,39)),(4,(29,39)),(7,(34,38)),(9,(40,38)),(12,(69,35)),(15,(71,39)),(17,(33,43))),
     p('3', R, (0,(40,30)),(6,(40,30)),(8,(42,35)),(10,(73,35)),(14,(71,42)),(17,(25,34))),
     p('1', R, (0,(60,22)),(8,(60,22)),(10,(63,27)),(13,(68,33))),
     p('2', R, (0,(78,24)),(8,(78,24)),(10,(75,29)),(13,(72,36))),
     p('3', R, (0,(83,43)),(8,(83,43)),(10,(78,39)),(13,(73,39)))],
    [(0,(16,25)),(1,(34,20)),(2,(18,46)),(3,(37,48)),(4,(28,34)),(5,(16,25)),(6,(35,28)),(6.5,(42,31)),(7.3,(55,34)),(8.2,(70,37)),(9,(70,32)),(10,(74,34)),(11,(65,40)),(12,(70,44)),(13,(74,46)),(14,(71,42)),(15,(62,39)),(16,(50,40)),(17,(34,40)),(18,(25,34))],
    [(0,'Fem mot tre i vänstra rutan','Blått behåller bollen. En blå spelare väntar i den andra rutan.'),
     (1,'Passning 1 och 2','Spela med bra avstånd – pressa inte fram en passning.'),
     (3,'Passning 3 och 4','De tre röda flyttar tillsammans mot bollen.'),
     (5,'Passning 5 och 6','Efter sex passningar får blått vända spelet.'),
     (6.5,'Blått spelar långt till den andra rutan','Tre blå spelare följer passningen in i nästa yta.'),
     (8.2,'Spelvändningen når den blå mottagaren','Rött pressar direkt i den nya rutan.'),
     (10,'Rött pressar direkt efter spelvändningen','Blått försöker behålla bollen i den nya rutan.'),
     (15,'Bollvinst – rött spelar tillbaka över','Rött vänder spelet till sina medspelare. Lagen byter uppgift.')],
    special='two-boxes')
C[-1]['seconds'] = 18
C[-1]['goals'] = []

_base = makebase
def makebase(c):
    im = _base(c)
    d = ImageDraw.Draw(im)
    d.rectangle((850,20,1050,58),fill='#0a1e17')
    d.text((1040,44),'POSSESSION',font=F(19,True),fill='#adc5b6',anchor='rm')
    def line(points, fill='#d2e3cc', width=3):
        d.line([xy(point) for point in points], fill=fill, width=width)
    # Two distinct possession areas and the clear route across the middle.
    for x1, y1, x2, y2 in [(7,12,45,54),(55,12,93,54)]:
        a=xy((x1,y1)); b=xy((x2,y2)); d.rounded_rectangle((*a,*b),radius=9,outline='#e4ecd6',width=4)
    line([(50,12),(50,54)], fill='#89aa92', width=2)
    return im

if __name__ == '__main__':
    c=C[0]; c['base']=makebase(c)
    for t in [3,7,10,15]: frame(c,t).resize((540,540)).save(ROOT/f'filmwork/{c["id"]}-{t}.jpg')
    path=OUT/(c['slug']+'.mp4')
    proc=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s','1080x1080','-r','30','-i','-','-an','-c:v','libx264','-threads','4','-preset','fast','-crf','17','-pix_fmt','yuv420p','-movflags','+faststart',str(path)],stdin=subprocess.PIPE)
    for f in range(c['seconds']*30): proc.stdin.write(frame(c,f/30).tobytes())
    proc.stdin.close(); assert proc.wait()==0
    print(path, flush=True)
