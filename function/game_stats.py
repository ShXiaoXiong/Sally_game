class Gamestats():
    ###初始化统计信息
    def __init__(self,ai_settings):
        self.ai_settings=ai_settings
        
        #一开始处于非活动状态
        self.game_active = False

        self.reset_stats()

    def reset_stats(self):
        ###初始化游戏中可能变化的统计信息
        self.sally_left=self.ai_settings.health
        self.score=0
        self.level=1