import pygame

class PauseBtn():
    def __init__(self,screen):
        # 暂停按钮
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.pause_btn_image = pygame.image.load("./image/pause.png")
        self.pause_btn_rect = self.pause_btn_image.get_rect()
        self.pause_btn_rect.bottom = self.screen_rect.bottom - 30
        self.pause_btn_rect.left = self.pause_btn_rect.width

    def draw_pause_btn(self):
        self.screen.blit(self.pause_btn_image, self.pause_btn_rect)