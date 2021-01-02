import pygame
class Title():
    def __init__(self, msg, screen,):
        self.screen = screen

        self.screen_rect = self.screen.get_rect()
        #填充图片的大小
        self.width , self.height = 400,80
        #背景颜色、字体颜色和字体
        self.button_color = (0,255,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,120)

        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery -(2*self.height)
        self.prep_msg(msg)

    def prep_msg(self, msg):
        '''将其变成图像'''
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_title(self):
        # self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, (self.msg_image_rect.x, self.msg_image_rect.y-self.height))

    def draw_score_title(self):
        # self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, (self.msg_image_rect.x, self.msg_image_rect.y+self.height))

    def draw_high_score(self):
        self.screen.blit(self.msg_image, (self.msg_image_rect.x, self.msg_image_rect.y + 2*self.height))
