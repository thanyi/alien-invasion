import pygame


class StartPage():
    def __init__(self,screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.start_btn_image = pygame.image.load("./image/start.png")
        self.start_btn_rect = self.start_btn_image.get_rect()

        self.exit_btn_image = pygame.image.load("./image/exit.png")
        self.exit_btn_rect = self.exit_btn_image.get_rect()

        self.start_btn_rect.centerx = self.screen_rect.centerx
        self.start_btn_rect.centery = self.screen_rect.centery

        self.exit_btn_rect.centerx = self.screen_rect.centerx
        self.exit_btn_rect.centery = self.screen_rect.centery + 2*self.start_btn_rect.height




    def draw_start_btn(self):
        self.screen.blit(self.start_btn_image,self.start_btn_rect)

    def draw_exit_btn(self):
        self.screen.blit(self.exit_btn_image, self.exit_btn_rect)

