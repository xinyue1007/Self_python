import sys
import form as form
import pygame

from settings import Settings
from ship import Ship


def run_game():

    ##初始化pygame、设置和屏幕对象
    pygame.init()

    ##screen = pygame.display.set_mode((1200,800))


    pygame.display.set_caption("Alien Invasion")

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    ship = Ship(screen)


    ##set bg
    ##bg_color = (230,230,230)
    while True:

        for event in pygame.event.get():
            ## error
            ##message = "event.type = " + event.type
            message = "event.type = " + str(event.type)
            print(message)
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        ##set bg
        #screen.fill(bg_color)
        pygame.display.flip()

run_game()
