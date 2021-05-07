import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    """表示外星人"""
    def __init__(self,ai_settings,screen):
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings =ai_settings

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #每个外星人最初再左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        """向左或向右移动"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect();
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <=0:
            return True