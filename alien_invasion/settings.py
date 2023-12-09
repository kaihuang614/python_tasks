class Settings:
    """储存游戏中所有的设置"""

    def __init__(self) -> None:
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.backgroundColor = (230, 230, 230)

        # 飞船设置
        self.ship_speed = 0.5
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed = 1.0
            # 向上 发送
        # self.bullet_width = 3
        # self.bullet_heigh = 5
            #向右发送
        self.bullet_width = 5
        self.bullet_heigh = 3
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # 外星人设置
        self.alien_speed = 0.1
        self.fleet_drop_speed = 10
            # 行动方向:fleet_direction  1向右 -1向左
        self.fleet_direction = 1

        # 加速游戏节奏的速度
        self.speedup_scale = 1.5
        # 敌人分数提高的速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随着游戏进行而变化"""
        #此为最终数值
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 0.1
        self.alien_points = 50

        # 行动方向:fleet_direction  1向右 -1向左
        self.fleet_direction = 1
    def increase_speed(self):
        """提高速度"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        #提高敌人数据
        self.alien_points = int(self.alien_points * self.score_scale)
