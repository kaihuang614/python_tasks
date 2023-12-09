class GameState:
    """跟踪游戏的统计信息"""
    
    def __init__(self,ai_game):
        """初始化统计信息"""
        self.settings = ai_game.settings
        self.reset_stats()
        #最高分数
        self.high_score = 0
        #刚开始游戏处于非活动状态
        #等待点击
        self.game_active = False

        # 读取历史最高得分初始化历史最高的分
        filename = 'high_score.txt'
        #如果没有历史最大值就初始化位0
        self.highestScore = 0
        with open(filename,'r') as f_obj:
            for score in f_obj:
                self.highestScore = int(score)
        self.high_score = self.highestScore


    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        #玩家生命值
        self.ships_left = self.settings.ship_limit
        #玩家得分
        self.score = 0
        #游戏等级
        self.level = 1