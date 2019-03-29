import pygame as pg

pg.init()

p=pg.image.load('pacman_mo0.png')

screen=pg.display.set_mode((26,26))

p=pg.transform.scale(p,(26,26))

i=True
while i:
    screen.blit(p, (0,0))
    pg.display.update()

    for j in range(26):
        for k in range(26):
            c=screen.get_at((k,j))
            if c!=(0,0,0,255):
                screen.set_at((k,j), (255,204,0))
    pg.display.update()

    pg.image.save(screen, 'try.jpg')

    i=False
pg.quit()
