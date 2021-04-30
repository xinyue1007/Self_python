import sys
import pygame

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")
    ##set bg
    bg_color = (230,230,230)
    while True:

        for event in pygame.event.get():
            ## error
            ##message = "event.type = " + event.type
            message = "event.type = " + str(event.type)
            print(message)
            if event.type == pygame.QUIT:
                sys.exit()
        ##set bg
        screen.fill(bg_color)
        pygame.display.flip()

run_game()
