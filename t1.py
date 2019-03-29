import pygame as pg

pg.init()

s=(700,700)
screen=pg.display.set_mode(s)

img=pg.image.load('board3.png')
img=pg.transform.scale(img, (650,650))
pos=[]

i=True
while i:

    screen.blit(img, (0,0))
    for j in range(s[1]):
        for k in range(s[0]):
            c=screen.get_at((k,j))
            if c[0]+c[1]+c[2]<50:
                try:
                    c1=screen.get_at((k+1,j))
                    if c1[0]+c1[1]+c1[2]>200:
                        a=True
                        for m in range(-10,11):
                            for n in range(-10,11):
                                c2=screen.get_at((k+1+n,j+m))
                                if c2==(255,0,0,255):
                                    a=False

                        if a:
                            screen.set_at((k+1,j),(255,0,0,255))
                            pg.display.update()
                            pos+=[(k+1,j)]
                except:
                    pass
    pg.display.update()

    print pos
    i=False
    for event in pg.event.get():
        if event.type==pg.QUIT:
            i=False
pg.quit()
