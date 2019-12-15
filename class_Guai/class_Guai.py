import pygame
from pygame.sprite import Sprite

class Guai(Sprite):
    def __init__(self,screen,ai_settings):
        super().__init__()
        self.screen=screen
        self.ai_settings=ai_settings

        self.image=pygame.image.load('dahong.png')
        #创建矩形
        self.rect=self.image.get_rect()
        
        #需要初始位置
        self.rect.left=float(0.5*self.rect.width)
        self.rect.top=float(self.rect.height)

        #需要初始方向，class调用可Settings，这样function不再调用Settings
        self.guai_direction=ai_settings.guai_direction

    #检查撞墙
    def check_edge(self):
        screen_rect=self.screen.get_rect()#必须重新创建，然后存储到一个对象中
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    #横向移动函数，包含方向信息
    def update(self):
        self.rect.x += self.ai_settings.guai_speed_factor*self.guai_direction
    

    #重新绘制怪
    def blitme(self):
        self.screen.blit(self.image,self.rect)