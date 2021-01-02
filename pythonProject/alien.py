import pygame
from pygame.sprite import Sprite
import random


class Alien(Sprite):
    def __init__(self,my_settings,screen):
        super().__init__()
        self.screen = screen
        self.my_settings = my_settings
        self.image = pygame.image.load('./image/alien2.png')
        self.rect = self.image.get_rect()

        # self.rect.x = self.rect.width
        # self.rect.y = self.rect.height

        self.rect.x = random.randint(1,1100)
        self.rect.y = random.randint(100,500)
        self.alien_direction = 1

        self.x = float(self.rect.x)

    def draw_alien(self):
        self.screen.blit(self.image,(self.rect.x,self.rect.y))

    def update(self):
        # self.x += (self.my_settings.alien_speed * self.my_settings.fleet_direction)
        self.x += (self.my_settings.alien_speed * self.alien_direction)
        self.rect.x = self.x


    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


