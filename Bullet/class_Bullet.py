import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,screen,ai_settings,sally):
        super().__init__()
        self.screen=screen
        
        self.image=pygame.image.load('bullet.png')
        #创建矩形
        self.rect=self.image.get_rect()
        #调整位置
        self.rect.centerx=sally.rect.centerx
        self.rect.top=sally.rect.top
        
        #表示子弹的位置（只需要纵坐标位置,横坐标不调整）
        self.y_coordinate=float(self.rect.top)

        #多一步，存储了子弹的颜色和速度
        self.speed_factor=ai_settings.bullet_speed_factor

        #更新位置
    def update(self):
        self.y_coordinate -= self.speed_factor
        #反赋值，更新位置
        self.rect.top= self.y_coordinate
   

    #绘制子弹
    def draw_bullet(self):
        self.screen.blit(self.image,self.rect)
