import pygame
###全部是常数
class Settings():

    #屏幕大小
    def __init__(self):
        self.screen_width=1000
        self.screen_height=700

        
        #玩家设置 
        self.speed_factor=3.5
        self.health=3
        
        #怪移动速度
        self.guai_speed_factor=2
        self.guai_drop_speed_factor=50
        self.guai_direction=1


        #子弹设置（图片在类中设置）
        self.bullet_speed_factor=8
        self.bullet_allowed=5