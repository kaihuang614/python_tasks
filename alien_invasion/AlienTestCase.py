import unittest
from unittest.mock import MagicMock
from pygame import Surface
from alien import Alien

class AlienTestCase(unittest.TestCase):
    def setUp(self):
        # 创建游戏对象
        self.mock_game = MagicMock()
        self.mock_game.screen = Surface((800, 600))
        self.mock_game.settings = MagicMock()
        self.mock_game.settings.alien_speed = 2
        self.mock_game.settings.fleet_direction = 1

    def test_check_edges(self):
        # 创建外星人对象
        alien = Alien(self.mock_game)
        alien.rect.right = self.mock_game.screen.get_rect().right + 1
        # 调用方法
        result = alien.check_edges()
        # 检查结果
        self.assertTrue(result)

    def test_update(self):
        # 创建外星人对象
        alien = Alien(self.mock_game)
        alien.rect.x = 100
        # 调用方法
        alien.update()
        # 检查位置是否正确更新
        self.assertEqual(alien.x, 102)

if __name__ == '__main__':
    unittest.main()
