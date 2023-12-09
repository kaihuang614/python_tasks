import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard():
    """显示游戏得分"""

    def __init__(self, ai_game) -> None:
        """初始化得分"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # 显示得分相关设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 准备初始化得分
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_ships(self):
        """显示余下的飞船"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_score(self):
        """将得分转化一张图片"""
        round_score = round(self.stats.score, -1)
        score_str = "{:,}".format(round_score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.backgroundColor)

        # 在右上角显示分数
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """将得分转化一张图片"""
        round_high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(round_high_score)
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.settings.backgroundColor)

        # 在屏幕顶部显示分数
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """将等级转化图片"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(
            level_str, True, self.text_color, self.settings.backgroundColor)

        # 将等级放到等分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.bottom = self.score_rect.bottom + 30
    def check_high_score(self):
        """检查是否产生最高分数"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        """显示分数和余下飞船数"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
