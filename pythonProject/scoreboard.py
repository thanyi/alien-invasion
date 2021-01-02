'''这个类用来将数据显示出来'''

import pygame.font
from pygame.sprite import Group
from ship import Ship

class ScoreBoard():
    def __init__(self,screen ,my_settings, stats):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.my_settings = my_settings
        self.stats = stats

        #开始改字体
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,24)

        #打印图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()


    def prep_score(self):
        '''创建分数图像以及把图像打印在屏幕上'''
        rounded_score = int(round(self.stats.score, -1))
        score_str =  "{:,}".format(rounded_score)       #得分的字符串

        self.score_image =self.font.render(score_str,True,self.text_color, self.my_settings.screen_bg_color)    #创建个图像

        self.score_rect = self.score_image.get_rect()       #图像的位置对象
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top =20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)         #在屏幕上画出这图像
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)


    def prep_high_score(self):
        high_score = int(round(self.stats.high_score,-1))
        high_score_str ="{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str,True,self.text_color,self.my_settings.screen_bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.my_settings.screen_bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom+10

    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.my_settings,self.screen)
            ship.rect.x = 10 +ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)