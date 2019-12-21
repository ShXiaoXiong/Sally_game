import pygame
###初始化静态设置
class Settings():

    #屏幕大小
    def __init__(self):
        self.screen_width=1000
        self.screen_height=700

        
        #玩家设置 
        self.health=3
        
        #怪设置
        self.guai_drop_speed_factor=50


        #子弹设置（图片在类中设置）

        self.bullet_allowed=5

        #加速参数
        self.speedup_scale=1.5
        
        self.initialize_dynamic_settings()

    #将可变的，速度参数全部调整到这来
    def initialize_dynamic_settings(self):
        self.speed_factor=4
        self.bullet_speed_factor=8
        self.guai_speed_factor=2
        self.guai_direction=1
        self.guai_points=100


    def increase_speed(self):
        self.speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.guai_speed_factor *= self.speedup_scale
        self.guai_points *= int(self.speedup_scale)
