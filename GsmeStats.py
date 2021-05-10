

class GameStats():
    """跟踪游戏统计信息"""
    def __init__(self,ai_settings):
        """"初始化统计信息"""
        self.ai_settings = ai_settings
        # 游戏启动时处于活动状态
        self.game_active = False
        self.reset_stats()
        #在任何情况下都不应重置最高分
        self.high_score = 0

    def reset_stats(self):
        """初始化再游戏运行期间可能变比的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
