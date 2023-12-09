import pygame
import unittest
from unittest.mock import MagicMock
from button import Button

class ButtonTestCase(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.mock_game = MagicMock()
        self.mock_game.screen = pygame.display.set_mode((800, 600))
        pygame.font.init()

    def test_prep_msg(self):
        button = Button(self.mock_game, "Start")
        button._prep_msg("Start")
        # self.assertEqual(button.msg_image.get_width(), button.width)
        # self.assertEqual(button.msg_image.get_height(), button.height)
        self.assertEqual(button.msg_image_rect.center, button.rect.center)

if __name__ == '__main__':
    unittest.main()
