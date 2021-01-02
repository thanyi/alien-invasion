
import sys

import pygame
from settings import Setting
from ship import Ship
import game_functions as gf
from alien import Alien
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard
from pause_btn import PauseBtn
from start_page import StartPage
from title import Title
from support import Support


def run_game():
    #初始化
    pygame.init()

    #设置类的对象
    my_settings = Setting()
    screen = pygame.display.set_mode((my_settings.screen_width,my_settings.screen_height))
    pygame.display.set_caption("the first of my game")



    #对象的创建

    play_button = Button( 'play' ,screen) #按钮
    pause_btn = PauseBtn(screen)

    ship = Ship(my_settings,screen)
    aliens = Group()
    bullets = Group()
    stats = GameStats(my_settings)
    sb = ScoreBoard(screen ,my_settings, stats)
    bg = pygame.image.load("./image/back4.png")
    sp = StartPage(screen)
    start_bg = pygame.image.load("./image/back4.png")
    title = Title("Maybe Our Game",screen)
    end_title = Title("HAAAAAAA YOU LOSE",screen)
    score_display = Title("YOUR SCORE:",screen)
    support = Support(screen, my_settings)


    # bgm 的创建
    pygame.mixer.init()
    bg_sound = pygame.mixer.Sound('./music/开头.mp3')
    bg_sound.play()


    gf.create_fleet(screen,my_settings,aliens,ship)

    SUPPLY_TIME = pygame.USEREVENT
    pygame.time.set_timer(SUPPLY_TIME, 30 * 1000)



    while True:
        if stats.game_first_page:
            gf.check_events(ship, my_settings, screen, bullets, stats, play_button, aliens, sb, bg_sound, pause_btn,sp,SUPPLY_TIME,support)
            gf.first_page_show(screen,sp,start_bg,title)
        else:
            gf.check_events(ship,my_settings, screen, bullets, stats ,play_button, aliens, sb, bg_sound, pause_btn,sp,SUPPLY_TIME,support)
            if stats.game_active and not stats.game_paused:
                ship.update()
                gf.update_aliens(aliens,my_settings,ship,stats,bullets,screen,sb,)
                gf.bullet_update(bullets,aliens,screen,my_settings,ship,stats, sb)
                gf.support_upate(support,my_settings,ship,stats)
            gf.screen_update(screen,my_settings,ship,bullets,aliens,stats,play_button,sb, bg, pause_btn,end_title, support, score_display)


run_game()