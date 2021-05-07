import sys
import form as form
import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():

    ##初始化pygame、设置和屏幕对象
    pygame.init()

    ##screen = pygame.display.set_mode((1200,800))


    pygame.display.set_caption("Alien Invasion")

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    ship = Ship(ai_settings,screen)
    #创建一个用于存储子弹的编组
    bullets = Group()


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
        #game_functions.check_events()q
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        bullets.update()
        # 删除已消失的子弹
        gf.update_bullets(bullets)
        # for bullet in bullets.copy():
        #     if bullet.rect.bottom <=0:
        #         bullets.remove(bullet)
        # print(len(bullets))
        #screen.fill(ai_settings.bg_color)
        #ship.blitme()
        ##set bg
        #screen.fill(bg_color)
        #pygame.display.flip()
        gf.update_screen(ai_settings,screen,ship,bullets)

run_game()
