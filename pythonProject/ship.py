import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,my_settings,screen):
        super().__init__()
        self.screen = screen
        self.my_settings = my_settings
        self.image = pygame.image.load("./image/ship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 飞船在界面底部的中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        #把坐标转变成小数
        self.center = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

    def update(self):
        #右
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.my_settings.ship_speed
        #左
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.my_settings.ship_speed
        #上
        elif self.moving_up and self.rect.top > 0:
            self.centery -= self.my_settings.ship_speed
        #下
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.my_settings.ship_speed

        self.rect.centerx = self.center
        self.rect.centery = self.centery

    def draw_ship(self):
        self.screen.blit(self.image,self.rect)
        # 绘制飞船

    def center_ship(self):
        self.center = self.screen_rect.centerx
        self.centery = self.screen_rect.bottom - self.rect.height/2