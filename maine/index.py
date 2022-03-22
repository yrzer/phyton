from cmath import log10
import pygame
import sys
import os
import random

pygame.init()

win = pygame.display.set_mode((1920/3,1080/3)) # 1920 × 1080
pygame.display.set_caption("dino adventures")

path = "maine\dino\\"
dino = pygame.image.load(path+'dino-stand.png') 
dino_m = pygame.image.load(path+'dino-stand_mrug.png')
restart = pygame.image.load(path+'restart.png')
game_over = pygame.image.load(path+'game_over.png')
chmura = pygame.image.load(path+'chmura.png')
backline = pygame.image.load(path+'backline.png')
dino_r = []
dino_r.append(pygame.image.load(path+'dino-right.png'))# 44 x 46
dino_r.append(pygame.image.load(path+'dino-left.png'))# 44 x 46
dino_r.append(pygame.transform.scale(pygame.image.load(path+'dino-right-d.png'), (57, 35)))
dino_r.append(pygame.transform.scale(pygame.image.load(path+'dino-left-d.png'), (57, 35)))
ptak = []
ptak.append(pygame.image.load(path+'ptak1.png'))
ptak.append(pygame.image.load(path+'ptak2.png'))
liczby= []
for x in range(10):
    liczby.append(pygame.image.load(path+str(x)+'.png'))
liczby.append(pygame.image.load(path+'H.png'))
liczby.append(pygame.image.load(path+'I.png'))
kaktus = pygame.image.load(path+'kaktus1.png')
# pygame.display.set_icon("icon.png")


clock = pygame.time.Clock()

delta = 0
sekunda = 0
do_10 = 0
do_100 = 0
do_1000 = 0
backlineX = 5
w_dino_r = 0
spacja = False
delta_v2 =0
dino_rY = 275
G = [1,1,2,2,2,3,3,3,3,4,4,4,4,4,5,5,5,5,6,6,6,6,6,6,7,7,7,8,8,8,9]
G.reverse()
kaktusX = 700
end = False
if_start = True
start_p = True
end_l = False

s_dol = False

def start():
    global delta, sekunda, do_10, do_100,do_1000, backlineX, w_dino_r, spacja, delta_v2, dino_rY, G, kaktusX, end, if_start, start_p, end_l
    if start_p == True:
        delta = 0
        sekunda = 0
        do_10 = 0
        do_100 = 0
        do_1000 = 0
        backlineX = 5
        w_dino_r = 0
        spacja = False
        delta_v2 =0
        dino_rY = 275
        kaktusX = 700
        end = False
        if_start = True
        start_p = False
        end_l = False
    
    win.blit(backline, (backlineX, 315))
    win.blit(dino, (30, dino_rY)) 
    
    if sekunda%5 == 0:
        win.blit(dino_m, (30, dino_rY)) 
    
    if spacja==True:
        sekunda = 0
        delta = 0
        do_10 = 0
        do_100 = 0
        do_1000 = 0
        if_start = False
    


def czas():
    global clock, delta, sekunda, do_10, do_100
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
                do_1000+=1
                if(do_1000==10):
                    do_1000=0

def rysowanie():
    global backlineX, kaktusX, w_dino_r, end, dino_rY
    #licznik
    win.blit(liczby[do_10], (610, 10))
    win.blit(liczby[do_100], (600, 10))
    win.blit(liczby[do_1000], (590, 10))
    
    #tło
    backlineX -= 5
    if(backlineX < -1200): backlineX=0
    if(backlineX < -560): win.blit(backline, (backlineX+1200, 315))
    win.blit(backline, (backlineX, 315))
    
    #random kaktus
    kaktusX -= 5
    if(kaktusX <-10):
        kaktusX = 700
    win.blit(kaktus, (kaktusX, 272)) # 25x50

    #dino
    if(delta%6==0):
        if s_dol == True:# w dół
            w_dino_r +=1
            if(w_dino_r>=4):
                w_dino_r=2
        else:
            w_dino_r +=1
            if(w_dino_r>=2):
                w_dino_r=0
    if w_dino_r == 3 or w_dino_r == 4:
        dulll = dino_rY + 6
    else: dulll = dino_rY
    win.blit(dino_r[w_dino_r], (30,  dulll)) # 44 x 46
    
    # kolsizja kaktus i dino
    if (kaktusX > 28 and kaktusX < 52) and (dino_rY < 277 and dino_rY > 238):
       end = True # print("kolizja")  ekran końcowy
    else:
       end = False

def end_game():
    global end, if_start, start_p, end_l, l1,l2,l3
    win.blit(game_over, (220, 140))
    # scoreboard
    l = 323
    if end_l == False:
        l1 = do_10
        l2 = do_100
        l3 = do_1000
        end_l = True
    win.blit(liczby[l1], (l, 220))
    win.blit(liczby[l2], (l-10, 220))
    win.blit(liczby[l3], (l-20, 220))
    
    win.blit(restart, (300, 180))
    if ((mouse_x, mouse_y) > (300,180) and (mouse_x, mouse_y) < (336,212)) and pygame.mouse.get_pressed()[0]:
        # ekarn startowy
        end = False # print("restart game")
        if_start = True
        start_p = True
    

while True:
    # if start restet czas i takie tam
    #czas
    czas()
    #czas
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        # wyjście
        if event.type == pygame.QUIT: 
            sys.exit(0)
        
    if keys[pygame.K_UP]:
        spacja = True
    if keys[pygame.K_SPACE]:
        spacja = True
    if keys[pygame.K_DOWN]:
        s_dol = True
    else:
        s_dol = False
        
    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    #skakanie
    if spacja==True:
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
        
        
    
    win.fill((0,0,0)) #rysowanie  
    
    if if_start == True:
        start()
    else:
        if end == True: end_game()
        else: 
            rysowanie()
            # if sekunda == 666: nowy_poziom[doom]
    
    
    # print(mouse_x, mouse_y)
    
    pygame.display.update()
    pygame.display.flip()


"""
import mysql.connector

config = {
  'user': 'scott',
  'password': 'password',
  'host': '127.0.0.1',
  'database': 'employees',
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

cnx.close()

"""