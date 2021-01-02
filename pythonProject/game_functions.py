import pygame
import sys
from bullet import Bullet
from alien import Alien
from pygame.sprite import Group
from time import sleep
import random
from button import Button
from title import Title
#按下的函数
def check_keydown(event,ship,my_settings,screen,bullets):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:  # 按下右键
        ship.moving_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a :  # 按下左键
        ship.moving_left = True
    elif event.key == pygame.K_UP or event.key == pygame.K_w :  # 按下 上键
        ship.moving_up = True
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s :  # 按下 下键
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(my_settings,bullets,ship,screen)




#不按的函数
def check_keyup(event,ship):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d: #松开右键
        ship.moving_right = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a: # 松开左键
        ship.moving_left = False
    elif event.key == pygame.K_UP :  # 按下上键
        ship.moving_up = False
    elif event.key == pygame.K_DOWN :  # 按下下键
        ship.moving_down = False


def check_events(ship,my_settings, screen, bullets, stats ,play_button, aliens, sb, bg_sound, pause_btn,sp,SUPPLY_TIME,support):
    '''对游戏的事件的监听函数'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, ship, my_settings, screen, bullets)
        elif event.type ==pygame.KEYUP:
            check_keyup(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats,play_button, mouse_x,mouse_y,aliens,bullets,screen,my_settings, ship, sb, bg_sound)
            check_pause_btn(stats, pause_btn, mouse_x, mouse_y, aliens, bullets, screen, my_settings, ship, sb,)
            check_start_btn(stats,sp, mouse_x, mouse_y,)
            check_exit_btn(sp, mouse_x, mouse_y, )

        elif event.type == SUPPLY_TIME:
            support.support_reset()

def check_start_btn(stats,sp, mouse_x, mouse_y,):
    '''点击了start按钮之后'''
    start_btn_checked = sp.start_btn_rect.collidepoint(mouse_x, mouse_y)
    if start_btn_checked:
        stats.game_first_page = False

def check_exit_btn(sp, mouse_x, mouse_y,):
    '''点击了start按钮之后'''
    exit_btn_checked = sp.exit_btn_rect.collidepoint(mouse_x, mouse_y)
    if exit_btn_checked:
        sys.exit()



def check_play_button(stats,play_button, mouse_x,mouse_y,aliens,bullets,screen,my_settings, ship,sb,bg_sound):
    '''点击了play按钮之后'''
    bg_sound.stop()
    button_checked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_checked and not stats.game_active:
        my_settings.initialize_dynamic_settings()

        #重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True
        stats.game_support_active = False
        #清空现有的外星人和子弹列表
        aliens.empty()
        bullets.empty()

        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()


        #创建一群新的外星人和子弹列表
        create_fleet(screen,my_settings,aliens,ship)
        ship.center_ship()

def check_pause_btn(stats,pause_btn, mouse_x,mouse_y,aliens,bullets,screen,my_settings, ship,sb):
    '''点击了暂停按钮之后'''

    pause_btn_checked = pause_btn.pause_btn_rect.collidepoint(mouse_x,mouse_y)
    if pause_btn_checked and stats.game_paused:
        stats.game_paused = False

    elif pause_btn_checked and not stats.game_paused:
        stats.game_paused = True


def screen_update(screen,my_settings,ship,bullets,aliens,stats,play_button,sb, bg, pause_btn,end_title,support,score_display):
    # 关于背景图片
    screen.fill(0)
    screen.blit(bg, (0, 0))
    pause_btn.draw_pause_btn()


    ship.draw_ship()

    for bullet in bullets.sprites():    #很多的在这个编组里的子弹需要被一个个打印出来
        if stats.game_bullet_active:
            bullet.draw_bullet_up()
        else:
            bullet.draw_bullet()

    aliens.draw(screen)         #将某一个编组绘制出来的函数
    sb.show_score()
    if not stats.game_active and not stats.game_paused:
        screen.fill(0)
        screen.blit(bg, (0, 0))
        play_button.draw_replay_button()   #函数写在最后可以把按钮绘制在最上层
        end_title.draw_title()
        score_display.draw_score_title()
        h_score = Title(str(stats.high_score),screen)
        h_score.draw_high_score()


    support.draw_support()


    pygame.display.flip()   #让绘制出来的函数可见

def support_upate(support,my_settings,ship,stats):
    support.update_support(my_settings)
    #检查补给到没到
    check_support_ship_collide(support,ship,stats)


def fire_bullet(my_settings,bullets,ship,screen):
    '''子弹发射'''
    pygame.mixer.init()
    pygame.mixer.music.load('./music/shoot.mp3')
    pygame.mixer.music.play(loops=0)
    if len(bullets) <= my_settings.bullet_allowed:
        new_bullet = Bullet(my_settings, ship, screen)
        bullets.add(new_bullet)


def bullet_update(bullets,aliens,screen,my_settings,ship,stats, sb):
    '''超出去的子弹就删掉，以及子弹和外星人的碰撞'''

    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #子弹的检查，打到外星人后的情况
    check_aliens_bullets_collide(bullets, aliens, screen, my_settings, ship, stats, sb)

def update_aliens(aliens,my_settings,ship,stats,bullets,screen,sb,):
    '''#让每个外星人都开始移动,并且碰到边界就返回,还有碰到我们自己的飞船时候的问题'''
    check_fleet_edges(my_settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(stats, my_settings, aliens, bullets, screen, ship, sb, )
    check_aliens_bottom(screen, aliens, my_settings, stats, bullets, ship, sb)


def check_support_ship_collide(support,ship,stats):
    '''support和飞船撞上'''
    if pygame.sprite.collide_rect(support, ship, ):
        support.visible = False
        stats.game_bullet_active = True



def check_aliens_bullets_collide(bullets, aliens, screen, my_settings, ship, stats, sb):
    '''子弹和外星人撞上的时候'''
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += my_settings.alien_points*len(aliens)
            sb.prep_score()
            check_high_score(stats, sb)

    if len(aliens) == 0:

        bullets.empty()    # 子弹删除

        my_settings.increase_speed()  #难度增加

        stats.level +=1
        sb.prep_level()
        create_fleet(screen, my_settings, aliens, ship) # 又来一堆外星人



# # 多个外星人的绘制
def create_fleet(screen,my_settings,aliens,ship):
    for e in range(10):
        create_alien(screen,aliens,my_settings)

#外星人的创建
def create_alien(screen,aliens,my_settings):
    alien = Alien(my_settings,screen,)

    aliens.add(alien)




def get_number_aliens_x(my_settings,alien_width):
    available_space_x = my_settings.screen_width - 2 * alien_width  # 一行除开两边的可以容纳外星人的空间
    number_aliens_x = int(available_space_x / (2 * alien_width))  # 一行中可容纳外星人的数目
    return number_aliens_x


def get_number_rows(my_settings,alien_height,ship_height,):
    available_space_y = my_settings.screen_height - 3*(alien_height) - ship_height
    number_rows = int(available_space_y/(2*alien_height))
    return number_rows







def check_fleet_edges(my_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(my_settings,aliens)
            break


def change_fleet_direction(my_settings,aliens):
    '''敌人碰到边界下移时候用的函数'''
    for alien in aliens.sprites():
        if alien.check_edges():
            alien.rect.y+=my_settings.fleet_drop_speed
            alien.alien_direction *=-1

    # my_settings.fleet_direction *=-1
    #改了就可以改方向



def ship_hit(stats,my_settings,aliens,bullets,screen,ship,sb,):
    if stats.ship_left >0:

        stats.ship_left -= 1
        #更新记分牌
        sb.prep_ships()
        #清空两个列表
        aliens.empty()
        bullets.empty()

        #创建一群新的外星人
        create_fleet(screen, my_settings, aliens, ship)
        ship.center_ship()

        sleep(0.5)

    elif stats.ship_left == 2:
        stats.game_support_active = True
    else:
        stats.game_active = False




def check_aliens_bottom(screen,aliens ,my_settings, stats, bullets,ship,sb):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(stats,my_settings,aliens,bullets,screen,ship,sb)
            break


def check_high_score(stats,sb):
    if stats.high_score < stats.score:
        stats.high_score = stats.score
        sb.prep_high_score()

def first_page_show(screen,sp,start_bg,title):
    screen.fill(0)
    screen.blit(start_bg,(0,0))

    title.draw_title()
    sp.draw_start_btn()
    sp.draw_exit_btn()

    pygame.display.flip()