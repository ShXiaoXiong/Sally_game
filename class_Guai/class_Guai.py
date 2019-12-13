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
        self.rect.top=float(0.2*self.rect.height)
       
    #重新绘制怪
    def blitme(self):
        self.screen.blit(self.image,self.rect)