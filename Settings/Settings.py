import pygame

class Settings():

    #屏幕大小
    def __init__(self):
        self.screen_width=1000
        self.screen_height=700

        
        #玩家移动速度
        self.speed_factor=3.5

        #子弹设置
        self.bullet_speed_factor=5.5
        self.bullet_width=20
        self.bullet_height=50
        self.bullet_color=(12,42,53)
        self.bullet_allowed=5