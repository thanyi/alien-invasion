import pygame
from button import Button
import random
from pygame.sprite import Sprite

class Support(Sprite):


    def __init__(self, screen,my_settings):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.visible = True

        self.support_image = pygame.image.load("./image/support.png")
        self.rect = self.support_image.get_rect()
        self.rect.centerx = random.randint(1,1200)
        self.rect.centery = 0

        # self.y = float(self.rect.y)

        # self.prep_msg(msg)


    def draw_support(self):
        if self.visible:
            self.screen.blit(self.support_image, self.rect)

    def update_support(self,my_settings):
        self.rect.y += 1

    def support_reset(self):
        self.rect.y = 0
        self.visible = True
