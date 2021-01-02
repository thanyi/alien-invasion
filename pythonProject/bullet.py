import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self , my_settings , ship, screen):
        super().__init__()
        self.my_settings = my_settings
        self.screen = screen
        self.image = pygame.image.load('./image/bullet2.png')
        self.rect = self.image.get_rect()
        #子弹的位置
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #子弹的速度
        self.speed = my_settings.bullet_speed
        #子弹的运动坐标的中间变量
        self.y = float(self.rect.y)

    #打印子弹的函数
    def draw_bullet(self):
        self.screen.blit(self.image,self.rect)

    #子弹的变化函数
    def update(self):
        self.y -= self.my_settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet_up(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.image, (self.rect.centerx,self.rect.y + 3*self.rect.width))
        self.screen.blit(self.image, (self.rect.centerx,self.rect.y -3*self.rect.width))