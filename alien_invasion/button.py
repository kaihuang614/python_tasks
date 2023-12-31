import pygame.font


class Button:

    def __init__(self, ai_game, msg):
        """初始化按钮"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # 设置按钮的尺寸和其他属性
        self.width, self.height = 200, 50
        self.button_color = (23, 114, 180)
        self.text_color = (249, 211, 103)
        self.font = pygame.font.SysFont(None, 48)  # 字体格式 字体大小

        # 创建按钮的rect对象
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 按钮的标签
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """将msg渲染为图像,并使其在按钮上面"""
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # 绘制一个按钮
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
