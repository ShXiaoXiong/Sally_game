import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,screen,ai_settings,sally):
        super().__init__()
        self.screen=screen
        #创建矩形
        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        #调整位置
        self.rect.centerx=sally.rect.centerx
        self.rect.top=sally.rect.top
        
        #表示子弹的位置（只需要纵坐标位置,横坐标不调整）
        self.y_coordinate=float(self.rect.top)

        #多一步，存储了子弹的颜色和速度
        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor

        #更新位置
    def update(self):
        self.y_coordinate -= self.speed_factor
        self.rect.top= self.y_coordinate
        #反赋值，更新位置
        

    #绘制子弹
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
