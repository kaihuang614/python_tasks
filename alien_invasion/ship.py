import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """管理飞船"""

    def __init__(self, ai_game) -> None:
        """初始化飞船,并设置初始位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()  # 矩形对象

        # 加载飞船图像并获取外接矩形
        # 向上飞船
        # self.image = pygame.image.load('resource/image/rocket.bmp')
        # 向左飞船
        self.image = pygame.image.load('resource/image/rocket-left.bmp')
        self.rect = self.image.get_rect()

        # 对于新飞船，出现在屏幕底部的中央
        # self.rect.midbottom = self.screen_rect.midbottom
        # 出现在屏幕左侧
        self.rect.midleft = self.screen_rect.midleft


        # 在飞船的属性x中存储小数值
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船位置"""
        # 飞船左右移动
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # 飞船上下移动
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed



        # 及时更新rect
        self.rect.x = self.x
        self.rect.y = self.y

    def center_ship(self):
        """让飞船居中"""
        # 飞船居中
        # self.rect.midbottom = self.screen_rect.midbottom

        # 飞船据屏幕左侧
        self.rect.midleft = self.screen_rect.midleft
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
