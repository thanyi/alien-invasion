'''这个类用来存各种各样的游戏统计数据'''

class GameStats():
    def __init__(self,my_settings):
        self.my_settings =my_settings
        self.reset_stats()
        self.ship_left = 3
        self.high_score = 0
        self.game_active = False
        self.game_paused = False
        self.game_first_page=True
        self.game_support_active = False
        self.game_bullet_active =False

    def reset_stats(self):
        self.ship_left = self.my_settings.ship_limit   #玩家一开始拥有的命的数量都要被重置

        self.score = 0
        self.level = 1


