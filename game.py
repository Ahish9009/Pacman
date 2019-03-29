import pygame as pg
import math, random

pg.init()

s_size=(650,650)
d_size=(7,7)
screen=pg.display.set_mode(s_size)
pg.display.set_caption('Pacman')

TNR1=pg.font.SysFont("Times New Roman", 30)
TNR2=pg.font.SysFont("Times New Roman", 18)
TNR3=pg.font.SysFont("Times New Roman", 14)

score=TNR1.render('SCORE',1,(255,255,255,255))
distance=TNR1.render('DISTANCE',1,(255,255,255,255))
cm=TNR3.render('cm',1,(255,255,255,255))

#clock
clock=pg.time.Clock()

bg=pg.image.load('board4.png')
pco0=pg.image.load('pacman_mo0.png') #0 shows direction
pco1=pg.image.load('pacman_mo1.png') #0 shows direction
pco2=pg.image.load('pacman_mo2.png') #0 shows direction
pco3=pg.image.load('pacman_mo3.png') #0 shows direction
pcc=pg.image.load('pacman_mc.png') #closed is same for all
dot=pg.image.load('dot.png')
dg=pg.image.load('dot.png')
gp=pg.image.load('gp.png')
gp1=pg.image.load('gp1.png')
ghost1=pg.image.load('g1.png')
ghost2=pg.image.load('g2.png')
ghost3=pg.image.load('g3.png')
ghost4=pg.image.load('g4.png')
paused=pg.image.load('paused.png')
go=pg.image.load('go.png')
outline=pg.image.load('outline.png')

bg=pg.transform.scale(bg, s_size)
pco0=pg.transform.scale(pco0, (26,26))
pco1=pg.transform.scale(pco1, (26,26))
pco2=pg.transform.scale(pco2, (26,26))
pco3=pg.transform.scale(pco3, (26,26))
pcc=pg.transform.scale(pcc, (26,26))
dot=pg.transform.scale(dot, d_size)
dg=pg.transform.scale(dg, (12,12))
gp=pg.transform.scale(gp, (26,26))
gp1=pg.transform.scale(gp1, (26,26))
ghost1=pg.transform.scale(ghost1, (26,26))
ghost2=pg.transform.scale(ghost2, (26,26))
ghost3=pg.transform.scale(ghost3, (26,26))
ghost4=pg.transform.scale(ghost4, (26,26))
paused=pg.transform.scale(paused, s_size)
go=pg.transform.scale(go, s_size)
outline=pg.transform.scale(outline, (26,26))

flag=-1 
spd=4 #speed of pacman

#pos of the green dots
posg=[(35,504),(606,504),(36,210),(606,210)]

#pos of the white dots which is received from t1.py
pos=[(150, 97), (585, 98), (36, 100), (59, 100), (82, 100), (105, 100), (128, 100), (173, 100), (196, 100), \
     (219, 100), (242, 100), (265, 100), (288, 100), (356, 100), (379, 100), (402, 100), (425, 100), (448, 100),\
     (470, 100), (493, 100), (516, 100), (539, 100), (562, 100), (608, 100), (150, 117), (288, 118), (356, 118), \
     (493, 118), (38, 122), (608, 122), (150, 135), (288, 136), (356, 136), (493, 136), (38, 139), (608, 140), \
     (150, 154), (36, 155), (288, 155), (356, 155), (493, 155), (608, 156), (82, 172), (128, 172), (150, 172), \
     (196, 172), (265, 172), (333, 172), (379, 172), (402, 172), (448, 172), (539, 172), (585, 172), (36, 173), \
     (59, 173), (105, 173), (173, 173), (219, 173), (242, 173), (310, 173), (356, 173), (425, 173), (470, 173), \
     (493, 173), (516, 173), (562, 173), (608, 175), (150, 190), (36, 192), (219, 192), (425, 192), (493, 192), \
     (608, 192), (150, 208), (219, 210), (425, 210), (493, 210), (150, 226), (82, 228), \
     (128, 228), (220, 228), (265, 228), (379, 228), (402, 228), (425, 228), (516, 228), (585, 228), (36, 229), \
     (59, 229), (105, 229), (242, 229), (289, 229), (360, 229), (493, 229), (539, 229), (562, 229), (608, 229), \
     (150, 245), (289, 247), (360, 247), (493, 247), (150, 262), (289, 266), (360, 266), (493, 266), (150, 282), \
     (220, 283), (243, 283), (289, 283), (312, 283), (358, 283), (380, 283), (425, 283), (266, 284), (335, 284), \
     (403, 284), (493, 284), (150, 300), (425, 301), (220, 302), (493, 302), (220, 320), (425, 320), (150, 321), \
     (493, 321), (16, 338), (39, 338), (62, 338), (85, 338), (108, 338), (130, 338), (153, 338), (176, 338), \
     (199, 338), (222, 338), (425, 338), (448, 338), (470, 338), (493, 338), (516, 338), (539, 338), (562, 338), \
     (585, 338), (630, 338), (220, 357), (150, 358), (425, 358), (493, 358), (220, 375), (425, 375), (150, 376), \
     (493, 376), (220, 393), (243, 393), (266, 393), (289, 393), (312, 393), (335, 393), (358, 393), (380, 393), \
     (403, 393), (426, 393), (150, 395), (493, 395), (220, 412), (150, 413), (425, 413), (493, 413), (150, 430), \
     (220, 430), (425, 432), (493, 432), (82, 449), (128, 449), (150, 449), (196, 449), (265, 449), (402, 449), \
     (448, 449), (470, 449), (516, 449), (539, 449), (585, 449), (36, 450), (59, 450), (105, 450), (173, 450), \
     (219, 450), (242, 450), (356, 450), (379, 450), (425, 450), (493, 450), (562, 450), (608, 450), (288, 451), \
     (150, 467), (36, 468), (288, 468), (356, 468), (493, 468), (608, 468), (150, 486), (36, 487), (288, 487), \
     (356, 487), (493, 487), (608, 487), (402, 504), (470, 504), (59, 505), (82, 505), (150, 505), (175, 505), \
     (219, 505), (289, 505), (358, 505), (379, 505), (425, 505), (448, 505), (493, 505), (562, 505), (585, 505), \
     (198, 510), (243, 510), (266, 510), (312, 510), (335, 510), (150, 523), (82, 524), (219, 524), (425, 524), \
     (493, 524), (562, 524), (150, 541), (82, 542), (219, 542), (425, 542), (493, 542), (562, 542), (59, 559), \
     (82, 559), (128, 559), (150, 559), (265, 559), (402, 559), (539, 559), (585, 559), (36, 561), (105, 561), \
     (219, 561), (242, 561), (288, 561), (356, 561), (379, 561), (425, 561), (493, 561), (516, 561), (562, 561), \
     (608, 562), (36, 579), (288, 579), (356, 579), (608, 579), (36, 597), (356, 597), (608, 597), (82, 615), \
     (128, 615), (265, 615), (402, 615), (470, 615), (516, 615), (585, 615), (36, 616), (59, 616), (105, 616), \
     (150, 616), (173, 616), (196, 616), (219, 616), (242, 616), (288, 616), (310, 616), (333, 616), (356, 616), \
     (379, 616), (425, 616), (448, 616), (493, 616), (539, 616), (562, 616), (608, 616)]

#directions
#      /\   +1
# -1 <    > +1
#      \/   -1

class pacman:
##    #contains colors of ghosts and pacman
##    ghostcolors=[(42,191,242,255),(255,0,0,255),(180, 180, 223, 255), (54, 83, 230, 255),(252,182,74,255),(224, 224, 224, 255),(253,195,212,255),(223,223,223,255),(28,28,224,255),(27,27,223,255),(71, 57, 0, 255), (255, 204, 0, 255), (255, 210, 0, 255), (254, 203, 0, 255), (4, 3, 0, 255), (253, 202, 0, 255), (3, 2, 0, 255), (251, 201, 0, 255), (255, 213, 0, 255), (154, 123, 0, 255), (187, 150, 0, 255), (5, 4, 0, 255), (1, 1, 0, 255), (255, 215, 0, 255),(255,204,1,255),(255,1,1,255),(167, 134, 6, 255),(253, 202, 1, 255),(255, 218, 1, 255),(255, 216, 1, 255),(254, 196, 213, 255),(255,210,1,255),(253, 195, 213, 255),(43, 192, 243, 255)]
##    #contains colors only of ghosts
##    ghosts=[(42,191,242,255),(255,0,0,255),(252,182,74,255),(253,195,212,255),(27,27,223,255),(223,223,223,255),(28,28,224,255),(180, 180, 223, 255), (54, 83, 230, 255), (224, 224, 224, 255)]
##    #contains colors of white and green dots
##    dotcolors=[(255,255,255,255),(0,255,0,255),(1,255,1,255),(1,254,1,255),(1,253,1,255)]
##    #contains colors of ghosts when the powerup is active
##    powerghost=[(180, 180, 223, 255), (54, 83, 230, 255), (224, 224, 224, 255),(28,28,224,255),(27,27,223,255),(223,223,223,255)]
    ghostcolors=[(255,204,1,255)]
    ghosts=[]
    dotcolors=[]
    powerghost=[]

    def __init__(self, x, y, h, v, pos):
        self.x=x #x coordinate
        self.y=y #y coordinate
        self.h=h #speed in horizontal direction
        self.v=v #speed in vertical direction
        self.buff=False #buffer time between turns for ghost to avoid continuous turning
        self.ctr=0 #to count and reach the threshold to remove buffer and allow turning for ghost again
        self.pctr=0 #to count each iteration of main loop when power is being used to cause flashing of ghosts when powerup is coming to an end 
        self.repeater=0 #to repeat the click during the buffer
        self.eaten=0 #counts how many white dots have been eaten
        self.eaten_g=0 #counts how many green dots have been eaten
        self.score=0 #counts the total score
        self.distance=0 #counts the distance travelled 
        self.lives=5 #counts the lives used
        self.stop=False #to stop the game temporarily when a ghost catches pacman

    def addcolor(self, dotcolor, dgcolor, pccolor, gpcolor, gp1color, g1color, g2color, g3color, g4color):
        pacman.dotcolors+=dotcolor
        pacman.dotcolors+=dgcolor
        pacman.ghostcolors+=pccolor
        pacman.ghostcolors+=gpcolor
        pacman.ghostcolors+=gp1color
        pacman.powerghost+=gpcolor
        pacman.powerghost+=gp1color
        pacman.ghosts+=g1color
        pacman.ghosts+=g2color
        pacman.ghosts+=g3color
        pacman.ghosts+=g4color
        pacman.ghostcolors+=g1color
        pacman.ghostcolors+=g2color
        pacman.ghostcolors+=g3color
        pacman.ghostcolors+=g4color

    def reset(self): #to reset the reuired features when a life is lost
        self.x=(s_size[0]/2)-13 #sets pacman back to the original position
        self.y=385
        self.h=spd
        self.v=0
        self.ctr=0 
        #puts ghosts back into the box and resets horizontal and vertical speeds
        g1.x=260
        g1.y=340
        g1.h=0
        g1.v=spd
        g2.x=305
        g2.y=320
        g2.h=0
        g2.v=spd
        g3.x=335
        g3.y=320
        g3.h=0
        g3.v=spd
        g4.x=365
        g4.y=320
        g4.h=-spd
        g4.v=0

    def check_touchedghost(self): #checks if the pacman touches the ghost
        #checks and finds if any of the ghost color is on top of the pacman, which would mean that a ghost has caught pacman
        for j in range(26):
            for k in range(26):
                try: #to avoid pixel out of range error
                    c=screen.get_at((self.x+k,self.y+j)) #gets the colors on the pacman

                    if c in pacman.ghosts or (c[0]==255 and c[1]<50): #second condition for red ghost
                        if not p: #if powerup is not active
                            self.stop=True
                    if c in pacman.powerghost:
                        if p: #if powerup is active
                            #generates list of positions for all ghosts
                            g1_x=range(g1.x,g1.x+26)
                            g1_y=range(g1.y,g1.y+26)
                            g2_x=range(g2.x,g2.x+26)
                            g2_y=range(g2.y,g2.y+26)
                            g3_x=range(g3.x,g3.x+26)
                            g3_y=range(g3.y,g3.y+26)
                            g4_x=range(g4.x,g4.x+26)
                            g4_y=range(g4.y,g4.y+26)

                            #checks if a ghost is eaten 
                            if self.x+k in g1_x: 
                                if self.y+j in g1_y:
                                    g1.x=260
                                    g1.y=340
                                    self.eaten_g+=1
                            if self.x+k in g2_x:
                                if self.y+j in g2_y:
                                    g2.x=305
                                    g2.y=320
                                    self.eaten_g+=1
                            if self.x+k in g3_x:
                                if self.y+j in g3_y:
                                    g3.x=335
                                    g3.y=320
                                    self.eaten_g+=1
                            if self.x+k in g4_x:
                                if self.y+j in g4_y:
                                    g4.x=365
                                    g4.y=320
                                    self.eaten_g+=1

                except:
                    pass

    def update_score(self): #to update score
        self.score=(self.eaten*5)+(self.eaten_g*50)

    def update_distance(self):
        self.distance+=spd

    def check_power(self,posg,eaten_g,eaten):
        points_x=range(self.x,self.x+26)
        points_y=range(self.y,self.y+26)
        totalpoints=[]
        p=False
        for j in points_x:
            for k in points_y:
                totalpoints+=[(j,k)]
        for j in posg:
            if j in totalpoints:
                if j not in eaten_g:
                    eaten_g+=[j]
                    p=True
                    eaten=[]
                    self.peaten=self.eaten_g
                    self.pscore=self.score

        return eaten_g, p, eaten
        
    def check_eaten(self,pos,eaten):
        if self.h==spd:
            points_x=range(self.x+13, self.x+26)
            points_y=range(self.y, self.y+26)
            totalpoints=[]
        
            for j in points_x:
                for k in points_y:
                    totalpoints+=[(j,k)]

            for j in pos:
                if j in totalpoints and j not in eaten:
                    self.eaten+=1
                    eaten+=[j]
        elif self.h==-spd:
            points_x=range(self.x, self.x+13)
            points_y=range(self.y, self.y+26)
            totalpoints=[]
        
            for j in points_x:
                for k in points_y:
                    totalpoints+=[(j,k)]

            for j in pos:
                if j in totalpoints and j not in eaten:
                    self.eaten+=1
                    eaten+=[j]
        elif self.v==spd:
            points_x=range(self.x, self.x+26)
            points_y=range(self.y, self.y+13)
            totalpoints=[]
        
            for j in points_x:
                for k in points_y:
                    totalpoints+=[(j,k)]

            for j in pos:
                if j in totalpoints and j not in eaten:
                    self.eaten+=1
                    eaten+=[j]
        else:
            points_x=range(self.x, self.x+26)
            points_y=range(self.y+13, self.y+26)
            totalpoints=[]
        
            for j in points_x:
                for k in points_y:
                    totalpoints+=[(j,k)]

            for j in pos:
                if j in totalpoints and j not in eaten:
                    self.eaten+=1
                    eaten+=[j]
        return eaten

    def check_edge(self):
        if self.x>s_size[0]-10:
            self.x=0-13 #to make it appear slowly
        elif self.x+26<0+10:
            self.x=s_size[0]-13

    def check_turn(self,d): #d=0 - right, d=1 - left, d=2 - up, d=3 - down
        t=40
        if d==0:
            col=False
##            if self.v!=0:
            if self.h!=0:
                t=2
            for k in range(1,t+1): #checks t pixels right
                try:
                    c=screen.get_at((self.x+26+k,self.y))
                    if c[0]+c[1]+c[2]>75 and c not in pacman.dotcolors and c not in pacman.ghostcolors:
                
                        col=True
                except:
                    continue
            for k in range(1,t+1): #checks t pixels right from middle
                try:
                    c=screen.get_at((self.x+26+1+k,self.y+13))
                    if c[0]+c[1]+c[2]>75 and c not in pacman.dotcolors and c not in pacman.ghostcolors:
                       
                        col=True
                except:
                    continue
            for k in range(1,t+1): #checks t pixels right from bottom
                try:
                    c=screen.get_at((self.x+26+k,self.y+26))
                    if c[0]+c[1]+c[2]>75 and c not in pacman.dotcolors and c not in pacman.ghostcolors:
                        
                        col=True
                except:
                    continue

            if not col:
                self.h=spd
                self.v=0
                self.buff=True
                
        if d==1: #to turn left
            col=False

##            if self.v!=0:
            if self.h!=0:
                t=2
                
            for k in range(1,t+1): #checks t pixels left
                try:
                    c=screen.get_at((self.x-k+1,self.y))
                    
                    if c[0]+c[1]+c[2]>75 and c not in pacman.dotcolors and c not in pacman.ghostcolors:
                        col=True
                except:
                    continue
            
            for k in range(1,t+1): #checks t pixels left from middle
                try:
                    c=screen.get_at((self.x-k-2,self.y+13)) #to stop from seeing its own color
                    if c[0]+c[1]+c[2]>75 and c not in pacman.dotcolors and c not in pacman.ghostcolors:
                        
                        col=True
                except:
                    continue
        
            for k in range(1,t+1): #checks t pixels left from bottom
                try:
                    c=screen.get_at((self.x-k,self.y+26))
                    
                    if c[0]+c[1]+c[2]>75 and c not in pacman.dotcolors and c not in pacman.ghostcolors:
                        col=True
                except:
                    continue
            
            if not col:
                self.h=-spd
                self.v=0
                self.buff=True
        if d==2:
            col=False
            if self.v!=0:
                t=2
            
            for k in range(1,t+1): #checks t pixels right
                try:
                    c=screen.get_at((self.x,self.y-k))
                    if c[0]+c[1]+c[2]>75 and c not in pacman.dotcolors and c not in pacman.ghostcolors:
                        col=True
                except:
                    continue
            for k in range(1,t+1): #checks t pixels right from middle
                try:
                    c=screen.get_at((self.x+13,self.y-1-k))
                    if c[0]+c[1]+c[2]>75 and c not in pacman.dotcolors and c not in pacman.ghostcolors:
                        col=True
                except:
                    continue

            for k in range(1,t+1): #checks t pixels right from bottom
                try:
                    c=screen.get_at((self.x+26,self.y-k))
                    if c[0]+c[1]+c[2]>75 and c not in pacman.dotcolors and c not in pacman.ghostcolors:
                        col=True
                except:
                    continue

            if not col:                        
                self.v=spd
                self.h=0
                self.buff=True
        if d==3:
            col=False
            if self.v!=0:
                t=2
            
            for k in range(1,t+1): #checks t pixels down
                try:
                    c=screen.get_at((self.x,self.y+26+k))
                    if c[0]+c[1]+c[2]>75 and c not in pacman.dotcolors and c not in pacman.ghostcolors:
                        
                        col=True
                except:
                    continue
            for k in range(1,t+1): #checks t pixels down from middle
                try:
                    c=screen.get_at((self.x+13,self.y+26+1+k))
                    if c[0]+c[1]+c[2]>75 and c not in pacman.dotcolors and c not in pacman.ghostcolors:
                        
                        col=True
                except:
                    continue

            for k in range(1,t+1): #checks t pixels down from bottom
                try:
                    c=screen.get_at((self.x+26,self.y+26+k))
                    if c[0]+c[1]+c[2]>75 and c not in pacman.dotcolors and c not in pacman.ghostcolors:
                        
                        col=True
                except:
                    continue

            if not col:
                self.v=-spd
                self.h=0
                self.buff=True

    def check_contact(self,spd,t):
        if self.h==spd:
            col=False
            for k in range(1,t+1): #checks t pixels right from top
                try:
                    c=screen.get_at((self.x+26+k,self.y))                    
                    if c[0]+c[1]+c[2]>75 and (c not in pacman.dotcolors) and (c not in pacman.ghostcolors):
                    
                        col=True
                except:
                    continue
            for k in range(1,t+1): #checks spd pixels right from bottom
                try:
                    c=screen.get_at((self.x+26+k+5,self.y+13))
                    if c[0]+c[1]+c[2]>75 and c not in pacman.dotcolors and c not in pacman.ghostcolors:
                        if c in pacman.ghostcolors:
                            break

                        col=True
                except:
                    continue
            for k in range(1,t+1): #checks spd pixels right from bottom
                try:
                    c=screen.get_at((self.x+26+k,self.y+26))
                    if c[0]+c[1]+c[2]>75 and c not in pacman.dotcolors and c not in pacman.ghostcolors:
                        if c in pacman.ghostcolors:
                            break
                        
                        col=True
                except:
                    continue
            if col:
                self.h=-spd
        elif self.h==-spd:
            col=False
            for k in range(1,t+1): #checks spd pixels behind
                try:
                    c=screen.get_at((self.x-k,self.y))
                    if c[0]+c[1]+c[2]>75 and c not in pacman.dotcolors and c not in pacman.ghostcolors:

                        col=True
                except:
                    continue
            for k in range(1,t+1): #checks spd pixels behind
                try:
                    c=screen.get_at((self.x-k-1,self.y+13))
                    if c[0]+c[1]+c[2]>75 and c not in pacman.dotcolors and c not in pacman.ghostcolors:

                        col=True
                except:
                    continue
            for k in range(1,t+1): #checks spd pixels ahead from bottom
                try:
                    c=screen.get_at((self.x-k,self.y+26))
                    if c[0]+c[1]+c[2]>75 and c not in pacman.dotcolors and c not in pacman.ghostcolors:

                        col=True
                except:
                    continue
            if col:
                self.h=spd
                
        elif self.v==spd:
            col=False
            for k in range(1,t+1): #checks spd pixels above from left
                try:
                    c=screen.get_at((self.x,self.y-k+1))
                    if c[0]+c[1]+c[2]>75 and c not in pacman.dotcolors and c not in pacman.ghostcolors:

                        col=True
                except:
                    continue
            for k in range(1,t+1): #checks t pixels above from middle
                try:
                    c=screen.get_at((self.x+13,self.y-k-5))
                    if c[0]+c[1]+c[2]>75 and c not in pacman.dotcolors and c not in pacman.ghostcolors:

                        col=True
                except:
                    continue
            for k in range(1,t+1): #checks spd pixels above from right
                try:
                    c=screen.get_at((self.x+26,self.y-k+1))
                    if c[0]+c[1]+c[2]>75 and c not in pacman.dotcolors and c not in pacman.ghostcolors:

                        col=True
                except:
                    continue

            if col:
                self.v=-spd
        elif self.v==-spd:
            col=False
            for k in range(1,t+1): #checks spd pixels below from left
                try:
                    c=screen.get_at((self.x,self.y+26+k))
                    if c[0]+c[1]+c[2]>75 and c not in pacman.dotcolors and c not in pacman.ghostcolors:
  
                        col=True
                except:
                    continue
            for k in range(1,t+1): #checks spd pixels below from middle
                try:
                    c=screen.get_at((self.x+13,self.y+26+k+5))
                    if c[0]+c[1]+c[2]>75 and c not in pacman.dotcolors and c not in pacman.ghostcolors:

                        col=True
                except:
                    continue
            for k in range(1,t+1): #checks spd pixels below from right
                try:
                    c=screen.get_at((self.x+26,self.y+26+k))
                    if c[0]+c[1]+c[2]>75 and c not in pacman.dotcolors and c not in pacman.ghostcolors:

                        col=True
                except:
                    continue

            if col:
                self.v=spd

ctr=0
i=True
while i:

    if flag==-1: #to get all colours of pacman, dot, etc on screen to prevent errors
        flag=0
        
        dotcolor=[]
        dgcolor=[]
        pccolor=[]
        gpcolor=[]
        gp1color=[]
        g1color=[]
        g2color=[]
        g3color=[]
        g4color=[]

        #for white dot
        screen.blit(dot, (0,0))
        pg.display.update()
        for j in range(7):
            for k in range(7):
                c=screen.get_at((k,j))

                if c!=(0,0,0,255) and c not in dotcolor:
                    dotcolor+=[c]

        #for green dot
        screen.fill((0,0,0))
        screen.blit(dg, (0,0))
        pg.display.update()
        for j in range(12):
            for k in range(12):
                c=screen.get_at((k,j))
              
                if c!=(0,0,0,255) and c not in dgcolor:
                    dgcolor+=[c]

        #for pacman
        screen.fill((0,0,0))
        screen.blit(pcc, (0,0))
        pg.display.update()
        for j in range(26):
            for k in range(26):
                c=screen.get_at((k,j))

                if c!=(0,0,0,255) and c not in pccolor:
                    pccolor+=[c]
        screen.fill((0,0,0))
        screen.blit(pco0, (0,0))
        pg.display.update()
        for j in range(26):
            for k in range(26):
                c=screen.get_at((k,j))

                if c!=(0,0,0,255) and c not in pccolor:
                    pccolor+=[c]
        screen.fill((0,0,0))
        screen.blit(pco1, (0,0))
        pg.display.update()
        for j in range(26):
            for k in range(26):
                c=screen.get_at((k,j))

                if c!=(0,0,0,255) and c not in pccolor:
                    pccolor+=[c]
        screen.fill((0,0,0))
        screen.blit(pco2, (0,0))
        pg.display.update()
        for j in range(26):
            for k in range(26):
                c=screen.get_at((k,j))

                if c!=(0,0,0,255) and c not in pccolor:
                    pccolor+=[c]
        screen.fill((0,0,0))
        screen.blit(pco3, (0,0))
        pg.display.update()
        for j in range(26):
            for k in range(26):
                c=screen.get_at((k,j))

                if c!=(0,0,0,255) and c not in pccolor:
                    pccolor+=[c]

        #for ghost 1
        screen.fill((0,0,0))
        screen.blit(ghost1, (0,0))
        pg.display.update()
        for j in range(26):
            for k in range(26):
                c=screen.get_at((k,j))

                if c!=(0,0,0,255) and c not in g1color:
                    g1color+=[c]

        #for ghost 2
        screen.fill((0,0,0))
        screen.blit(ghost2, (0,0))
        pg.display.update()
        for j in range(26):
            for k in range(26):
                c=screen.get_at((k,j))

                if c!=(0,0,0,255) and c not in g2color:
                    g2color+=[c]
                    
        #for ghost 3
        screen.fill((0,0,0))
        screen.blit(ghost3, (0,0))
        pg.display.update()
        for j in range(26):
            for k in range(26):
                c=screen.get_at((k,j))

                if c!=(0,0,0,255) and c not in g3color:
                    g3color+=[c]
                    
        #for ghost 4
        screen.fill((0,0,0))
        screen.blit(ghost4, (0,0))
        pg.display.update()
        for j in range(26):
            for k in range(26):
                c=screen.get_at((k,j))

                if c!=(0,0,0,255) and c not in g4color:
                    g4color+=[c]

        #for powered ghosts
        screen.fill((0,0,0))
        screen.blit(gp, (0,0))
        pg.display.update()
        for j in range(26):
            for k in range(26):
                c=screen.get_at((k,j))

                if c!=(0,0,0,255) and c not in gpcolor:
                    gpcolor+=[c]
                    
        #for powered ghost 2
        screen.fill((0,0,0))
        screen.blit(gp1, (0,0))
        pg.display.update()
        for j in range(26):
            for k in range(26):
                c=screen.get_at((k,j))

                if c!=(0,0,0,255) and c not in gp1color:
                    gp1color+=[c]
        
    if flag==0:
        #initial
        flag=1
        screen.blit(bg, (0,0))
        screen.blit(pcc, ((s_size[0]/2)-13,385))

        player=pacman((s_size[0]/2)-13,385,spd,0,pos)
        g1=pacman(260,340,0,spd,pos)
        g2=pacman(305,320,0,spd,pos)
        g3=pacman(335,320,0,spd,pos)
        g4=pacman(365,320,-spd,0,pos)
        player.lives-=1

        print len(g1color)
        print len(g2color)
        print len(g3color)
        print len(g4color)
        print len(pccolor)

        #to add and adjust to different colors on different devices
        player.addcolor(dotcolor, dgcolor, pccolor, gpcolor, gp1color, g1color, g2color, g3color, g4color)

        p=False #p for power
        eaten=[]
        eaten_g=[]

    if flag==2:
        pg.time.delay(2000)
        
        player.reset()
        flag=1

    if flag==3:
        screen.blit(go, (0,0))
        screen.blit(score,(230,485))
        screen.blit(sc, (380,485))
        screen.blit(distance, (200, 525))
        screen.blit(dis, (380, 525))

    if flag==5:
        screen.blit(paused, (0,0))
    
    if flag==1:
        if player.stop:
            player.lives-=1

            if player.lives>=0:
                player.stop=False
                flag=2
            else:
                flag=3

        if not player.stop and flag==1:

            #if power is active
            if p:
                player.pctr+=1
                
                if player.eaten_g>=player.peaten+4 or player.score>player.pscore+(5*80):
                    p=False
            
            if len(eaten)==len(pos): #to reshow dots when all are eaten
                eaten=[]
                eaten_g=[]
                
            sc=TNR1.render(str(player.score),1,(255,255,255))
            dis=TNR1.render(str(player.distance/5),1,(255,255,255))
            
            screen.blit(bg, (0,0))
            screen.blit(score, (280,0))
            screen.blit(distance, (450,0))
            screen.blit(sc, (310,30))
            screen.blit(dis, (500,30))
            screen.blit(cm, (550,55))

            #to show lives left
            for j in range(5):
                screen.blit(outline, (0+(j*30),45))
                            
            for j in range(player.lives):
                screen.blit(pco0, (0+(j*30),45))
            
            #to blit dots
            for j in pos:
                if j not in eaten:
                    screen.blit(dot, j)

            for j in posg:
                if j not in eaten_g:
                    screen.blit(dg, j)
            
            #to blit the pacman and change its mouth depending on direction it is moving
            if ctr%3==0:
                screen.blit(pcc,(player.x,player.y))
            else:
                if player.h==spd:
                    screen.blit(pco0,(player.x,player.y))
                elif player.h==-spd:
                    screen.blit(pco1,(player.x,player.y))
                elif player.v==spd:
                    screen.blit(pco2,(player.x,player.y))
                else:
                    screen.blit(pco3,(player.x,player.y))

            if not p:
                screen.blit(ghost1,(g1.x,g1.y))
                screen.blit(ghost2,(g2.x,g2.y))
                screen.blit(ghost3,(g3.x,g3.y))
                screen.blit(ghost4,(g4.x,g4.y))
            elif player.eaten_g<player.peaten+3 and player.score<player.pscore+(50*5):
                screen.blit(gp,(g1.x,g1.y))
                screen.blit(gp,(g2.x,g2.y))
                screen.blit(gp,(g3.x,g3.y))
                screen.blit(gp,(g4.x,g4.y))
            else:
                if player.pctr%6 in [0,1,2]:
                    screen.blit(gp,(g1.x,g1.y))
                    screen.blit(gp,(g2.x,g2.y))
                    screen.blit(gp,(g3.x,g3.y))
                    screen.blit(gp,(g4.x,g4.y))
                else:
                    screen.blit(gp1,(g1.x,g1.y))
                    screen.blit(gp1,(g2.x,g2.y))
                    screen.blit(gp1,(g3.x,g3.y))
                    screen.blit(gp1,(g4.x,g4.y))

            ctr+=1

            if player.h!=0:
                player.x+=player.h
                player.update_distance()
            if player.v!=0:
                player.y+=-player.v
                player.update_distance()
            if player.buff:
                player.ctr+=1
                player.check_turn(player.repeater)
                if player.ctr==25:
                    player.ctr=0
                    player.buff=False

            if not p:
                eaten_g,p,eaten=player.check_power(posg,eaten_g,eaten)

            eaten=player.check_eaten(pos,eaten)
            player.update_score()
            player.check_edge()
            player.check_contact(spd,spd)
            player.check_touchedghost()

            #for first ghost
            if g1.h!=0:
                g1.x+=g1.h
            if g1.v!=0:
                g1.y+=-g1.v

            g1.check_edge()
            g1.check_contact(spd,spd)
            if g1.h!=0 and not g1.buff:
                n=random.randint(2,3)
                g1.check_turn(n)
            elif g1.v!=0 and not g1.buff:
                n=random.randint(-2,1)
                g1.check_turn(n)
            if g1.buff:
                g1.ctr+=1
                if g1.ctr==25:
                    g1.ctr=0
                    g1.buff=False

            #for second ghost
            if g2.h!=0:
                g2.x+=g2.h
            if g2.v!=0:
                g2.y+=-g2.v

            g2.check_edge()
            g2.check_contact(spd,spd)
            if g2.h!=0 and not g2.buff:
                n=random.randint(2,5)
                g2.check_turn(n)
            elif g2.v!=0 and not g2.buff:
                n=random.randint(-2,1)
                g2.check_turn(n)
            if g2.buff:
                g2.ctr+=1
                if g2.ctr==25:
                    g2.ctr=0
                    g2.buff=False

            #for third ghost
            if g3.h!=0:
                g3.x+=g3.h
            if g3.v!=0:
                g3.y+=-g3.v

            g3.check_edge()
            g3.check_contact(spd,spd)
            if g3.h!=0 and not g3.buff:
                n=random.randint(2,5)
                g3.check_turn(n)
            elif g3.v!=0 and not g3.buff:
                n=random.randint(-2,1)
                g3.check_turn(n)
            if g3.buff:
                g3.ctr+=1
                if g3.ctr==25:
                    g3.ctr=0
                    g3.buff=False

            #for fourth ghost
                    
            #to move the ghost
            if g4.h!=0:
                g4.x+=g4.h
            if g4.v!=0:
                g4.y+=-g4.v
            #------------------------
            g4.check_edge() #checks if it is going out of the game area
            g4.check_contact(spd,spd) #checks if it touches any wall without being asked to turn

            if g4.h!=0 and not g4.buff: #to make sure direction has not been recently changed 
                n=random.randint(2,3)
                g4.check_turn(n)
            elif g4.v!=0 and not g4.buff:
                n=random.randint(-2,1)
                g4.check_turn(n)
            if g4.buff:
                g4.ctr+=1
                if g4.ctr==25:
                    g4.ctr=0
                    g4.buff=False
          
                
    for event in pg.event.get():
        if event.type==pg.QUIT:
            i=False

        if event.type==pg.KEYDOWN:

            if event.key==pg.K_p:
                if flag==5:
                    flag=old
                elif flag!=5:
                    old=flag
                    flag=5
        
            if event.key==pg.K_RIGHT:
                player.check_turn(0)
                player.buff=True
                player.repeater=0 #to repeat the click during the buffer to see if any click within a given distance satisfies the click
                    
            if event.key==pg.K_LEFT:
                player.check_turn(1)
                player.buff=True
                player.repeater=1
                    
            if event.key==pg.K_UP:
                player.check_turn(2)
                player.buff=True
                player.repeater=2
                
            if event.key==pg.K_DOWN:
                player.check_turn(3)
                player.buff=True
                player.repeater=3

    clock.tick(20)
 
    pg.display.update()

pg.quit()
