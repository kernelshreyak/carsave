#Character classes for CarSave game

import pygame, math, sys, random
from pygame.locals import *



class Player(pygame.sprite.Sprite):    # Player car
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load('images/car1.png').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect()
        self.health=100
        
    def move(self, pressed_keys):
        if pressed_keys[K_w]:
            self.rect.move_ip(0, -2.0)
        if pressed_keys[K_s]:
            self.rect.move_ip(0, 2.0)
        if pressed_keys[K_a]:
            self.rect.move_ip(-2.0, 0)
        if pressed_keys[K_d]:
            self.rect.move_ip(2.0, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0





class Enemy(pygame.sprite.Sprite):     #Enemy car
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load('images/car2.png').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(
            center=(random.randint(820, 900), random.randint(0, 600)))
        self.velx= random.randint(5, 15)
        self.vely=0
        
    def move(self):
        self.rect.move_ip(-self.velx,0)
        
        if self.rect.right < 0:
            self.kill()
        if self.rect.top > 600:
            self.kill()
