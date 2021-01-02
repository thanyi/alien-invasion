import random



class Setting ():
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.screen_bg_color = (0,0,0)

        self.bullet_speed = 3

        self.ship_limit = 3

        self.bullet_allowed = 3

        self.speedup_scale = 1.1

        self.fleet_drop_speed =20  #撞到边缘的时候下降的大小

        #这个是控制方向的数值 ，1是右，-1是左


    def initialize_dynamic_settings(self):
        #速度
        self.ship_speed = 1.5
        self.bullet_speed = 3
        self.alien_speed = 1
        #方向
        # self.fleet_direction = 1
        #分数
        self.alien_points = 50




    def increase_speed(self):
        '''速度提高'''
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *=self.speedup_scale
