import pygame
import sys
import os
import random

pygame.init()

win = pygame.display.set_mode((1920/3,1080/3)) # 1920 × 1080
pygame.display.set_caption("dino adventures")

path = "maine\dino\\"
dino = pygame.image.load(path+'dino-stand.png')
restart = pygame.image.load(path+'restart.png')
game_over = pygame.image.load(path+'game_over.png')
chmura = pygame.image.load(path+'chmura.png')
backline = pygame.image.load(path+'backline.png')
dino_r = []
dino_r.append(pygame.image.load(path+'dino-right.png'))
dino_r.append(pygame.image.load(path+'dino-left.png'))
ptak = []
ptak.append(pygame.image.load(path+'ptak1.png'))
ptak.append(pygame.image.load(path+'ptak2.png'))
liczby= []
for x in range(10):
    liczby.append(pygame.image.load(path+str(x)+'.png'))
liczby.append(pygame.image.load(path+'H.png'))
liczby.append(pygame.image.load(path+'I.png'))
kaktus = pygame.image.load(path+'kaktus1.png')

clock = pygame.time.Clock()
delta = 0
sekunda = 0
do_10 = 0
do_100 = 0
backlineX = 5
w_dino_r = 0
spacja = False
delta_v2 =0
dino_rY = 275
G = [1,1,2,2,2,3,3,3,3,4,4,4,4,4,5,5,5,5,6,6,6,6,6,6,7,7,7,8,8,8,9]
G.reverse()
kaktusX = 700

while True:
    #czas
    clock.tick(60) # jeszcze zrobie lepsze ?
    delta += 1
    if(delta == 60):
        delta = 1
        sekunda +=1
        do_10+=1
        if(do_10==10):
            do_10=0
            do_100+=1
            if(do_100==10):
                do_100=0
    #czas
    
    for event in pygame.event.get():
        # wyjście
        if event.type == pygame.QUIT: 
            sys.exit(0)
        # skakanie
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            spacja= True
    
    #skakanie
    if spacja==True :
        delta_v2 += 1
        if(delta_v2 == 30):
            G.reverse()
        if(delta_v2 <30):
            dino_rY-=G[delta_v2]
        else:
            dino_rY+=G[delta_v2-29]
        if(delta_v2==58):
            G.reverse()
            spacja = False
            delta_v2=0
        
        
    
    win.fill((0,0,0))
    #rysowanie
    
    #licznik
    win.blit(liczby[do_10], (610, 10))
    win.blit(liczby[do_100], (600, 10))
    
    #tło
    backlineX -= 5
    if(backlineX<-1200): backlineX=0
    if(backlineX<-560):  win.blit(backline, (backlineX+1200, 315))
    win.blit(backline, (backlineX, 315))
    
    #random kaktus
    kaktusX -= 5
    if(kaktusX <-10):
        kaktusX = 700
    win.blit(kaktus, (kaktusX, 272)) # 25x50

    #dino
    if(delta%6==0):
        w_dino_r +=1
        if(w_dino_r==2):
            w_dino_r=0
    win.blit(dino_r[w_dino_r], (30, dino_rY)) # 44 x 46
    
    #kolsizja kaktus i dino
    if (kaktusX > 28 and kaktusX < 52) and (dino_rY < 277 and dino_rY > 238):
       pass# print("kolizja")  ekran końcowy
    
    #print(kaktusX, dino_rY)
    
    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    #print(mouse_x, mouse_y)
    
    pygame.display.update()
    pygame.display.flip()