import pygame
import sys
import copy
import random
import time
pygame.init()
wys = pygame.display.set_mode((800,600))
pygame.display.update()
box = pygame.Rect(10,50,100,100) # pozycja początkowa a,b wystokość i szerokość c,d
color = [(0,255,0), (255,0,0), (0,0,255)]
nr_c = 0
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        # wyjście
        if event.type == pygame.QUIT: 
            sys.exit(0)
        # wyjście
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            nr_c = 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_g:
            nr_c = 0
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_b:
            nr_c = 2
    
    dt = clock.tick()
    
    mouse_x, mouse_y = pygame.mouse.get_pos() 
    box.x = mouse_x - 50
    box.y = mouse_y - 50
 #   keys= pygame.key.get_pressed()
 #   if keys[pygame.K_w]:
    wys.fill((0,0,0))
    pygame.draw.rect(wys, color[nr_c], box)
    pygame.display.flip()