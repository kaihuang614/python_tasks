import unittest
from ship import Ship
from unittest.mock import MagicMock
from pygame import Surface

class ShipTestCase(unittest.TestCase):
    """测试Ship类"""

    def setUp(self):
        """创建一个Ship实例用于测试"""
        
        self.mock_game = MagicMock()
        self.mock_game.screen = Surface((800, 600))
        self.mock_game.settings = MagicMock()
        self.ship = Ship(self.mock_game)

    def test_initial_position(self):
        """测试飞船的初始位置是否正确"""
        self.assertEqual(self.ship.rect.midleft, (0, 240))

    # def test_move_right(self):
    #     """测试向右移动飞船"""
    #     self.ship.move_right()
    #     self.assertEqual(self.ship.rect.midleft, (1, 240))

    # def test_move_left(self):
    #     """测试向左移动飞船"""
    #     self.ship.move_left()
    #     self.assertEqual(self.ship.rect.midleft, (-1, 240))

    # def test_move_up(self):
    #     """测试向上移动飞船"""
    #     self.ship.move_up()
    #     self.assertEqual(self.ship.rect.midleft, (0, 239))

    # def test_move_down(self):
    #     """测试向下移动飞船"""
    #     self.ship.move_down()
    #     self.assertEqual(self.ship.rect.midleft, (0, 241))

if __name__ == '__main__':
    unittest.main()
