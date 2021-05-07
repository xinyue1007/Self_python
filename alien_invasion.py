import sys
import form as form
import pygame
from pygame.sprite import Group

import game_functions as gf
from GsmeStats import GameStats
from alien import Alien
from settings import Settings
from ship import Ship


def run_game():

    ##初始化pygame、设置和屏幕对象
    pygame.init()

    ##screen = pygame.display.set_mode((1200,800))
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")

    stats = GameStats(ai_settings)


    ship = Ship(ai_settings,screen)
    #创建一个用于存储子弹的编组
    bullets = Group()
    #alien =Alien(ai_settings,screen)
    #创建一组外星人
    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)


    ##set bg
    ##bg_color = (230,230,230)
    while True:

        # for event in pygame.event.get():
        #     ## error
        #     ##message = "event.type = " + event.type
        #     message = "event.type = " + str(event.type)
        #     print(message)
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        #game_functions.check_events()
        gf.check_events(ai_settings,screen,ship,bullets)
        if stats.game_active:
            ship.update()
            bullets.update()
            # 删除已消失的子弹
            gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
            # for bullet in bullets.copy():
            #     if bullet.rect.bottom <=0:
            #         bullets.remove(bullet)
            # print(len(bullets))
            #screen.fill(ai_settings.bg_color)
            #ship.blitme()
            ##set bg
            #screen.fill(bg_color)
            #pygame.display.flip()
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)

run_game()
