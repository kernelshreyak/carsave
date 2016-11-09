#CarSave Game created in pygame


import pygame,random
from pygame.locals import *
import characters     


#----------------------------------------------------------------------------------
clock = pygame.time.Clock()
FPS = 30
BLUE=(0,255,255)

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Carsave')

intro_screen=pygame.image.load('images/title.png').convert()
gameover=pygame.image.load('images/gameover.png').convert()
youwin=pygame.image.load('images/youwin.png').convert()
clock = pygame.time.Clock()
FPS = 60

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 1000)

player=characters.Player()
enemy=characters.Enemy()

enemies = pygame.sprite.Group()
enemies.add(enemy)
everyone=pygame.sprite.Group()
everyone.add(player)
everyone.add(enemy)


#---------------------------------------------------------------------------------
run=True
while run:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_b:
                run=False
    screen.blit(intro_screen,(0,0))
    pygame.display.flip()
#------------------------------------------------------------------------------


    
#Main Loop
run=True
while run:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run= False
        elif event.type == QUIT:
            run = False
        elif event.type == ADDENEMY:
            new_enemy = characters.Enemy()
            enemies.add(new_enemy)
            everyone.add(new_enemy)
            
    keypress=pygame.key.get_pressed()
   
    player.move(keypress)
    
    T=random.randint(0,10)
    count=0
    
            
    deltat = clock.tick(FPS)
    
    screen.fill(BLUE)
    
    for j in enemies:
        j.move()
    for i in everyone:
        screen.blit(i.image, i.rect)
        
    if pygame.sprite.spritecollideany(player, enemies):
        player.health-=20

    if player.health==0:
        screen.blit(gameover,(0,0))
        player.kill()
        run=False

    if player.rect.top > 600:
        screen.blit(youwin,(0,0))
        run=False
    pygame.display.flip()

