import pygame as pg

pg.init()

p=pg.image.load('dot.png')

screen=pg.display.set_mode((26,26))

p=pg.transform.scale(p, (26,26))

colours=[]

i=True
while i:
    screen.blit(p, (0,0))
    pg.display.update()
    for j in range(26):
        for k in range(26):
            c=screen.get_at((k,j))
            if c not in colours:
                colours+=[c]

    i=False
pg.quit()

print colours
