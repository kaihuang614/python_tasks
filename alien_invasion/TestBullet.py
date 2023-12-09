import pygame
import unittest
from bullet import Bullet

class TestBullet(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.settings = SomeSettings()  # 替换为真实的设置对象
        self.ship = SomeShip()  # 替换为真实的飞船对象
        self.bullet = Bullet(self.screen, self.settings, self.ship)

    def test_bullet_update(self):
        self.bullet.update()
        self.assertEqual(self.bullet.x, self.bullet.rect.x)

    def test_bullet_draw_bullet(self):
        self.bullet.draw_bullet()
        # 编写断言来检查绘制是否成功

if __name__ == '__main__':
    unittest.main()
