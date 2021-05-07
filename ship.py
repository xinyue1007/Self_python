import pygame

class Ship():

    def __init__(self,ai_settings,screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings
        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        #self.image = pygame.image.load('images/shipwang.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将每艘新飞船防止在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)
        self.centery = float(ai_settings.screen_height)
        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            #self.rect.centerx += 1
            self.center += self.ai_settings.ship_speed_factor
            self.rect.centerx = self.center
        if self.moving_left and self.rect.left > 0:
            #self.rect.centerx -= 1
            self.center -= self.ai_settings.ship_speed_factor
            self.rect.centerx = self.center
        if self.moving_up and self.rect.top > 0:
            #self.rect.centerx -= 1
            self.centery -= self.ai_settings.ship_speed_factor
            self.rect.centery = self.centery
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            #self.rect.centerx -= 1
            self.centery += self.ai_settings.ship_speed_factor
            self.rect.centery = self.centery

    def blitme(self):
        """在指定的位置上绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        """让飞船再屏幕上居中"""
        self.center = self.screen_rect.centerx


