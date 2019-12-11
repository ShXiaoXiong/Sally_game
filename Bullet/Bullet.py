import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,screen,ai_settings,sally):
        super(Bullet,self).__init__()
        self.screen=screen

        self.rect=pygame.Rect(0,0,as_settings.bullet_width,as_settings.bullet_height)
        self.rect.centerx=sally.rect.centerx
        self.rect.top=sally.rect.top
        
        #表示子弹的位置（只需要纵坐标位置,横坐标不调整）
        self.y_coordinate=float(self.rect.top)

        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor

    def update(self):
        self.y_coordinate -= ai_settings.bullet_speed_factor
        self.rect.top= self.y_coordinate#反赋值，更新位置
        

    #绘制子弹
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
