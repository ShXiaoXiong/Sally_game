import pygame

class Sally():
    def __init__(self,screen,ai_settings):
        self.screen=screen
        self.ai_settings=ai_settings

        self.image=pygame.image.load('sally.png')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #初始位置
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False

        #后续位置的坐标
        self.x_coordinate=float(self.rect.centerx)
        self.y_coordinate=float(self.rect.bottom)

    #移动的主逻辑
    #双if中每个if判断都是独立的，即左右可以抵消。
    #if-elif是一个整体，尽管列出多个选择，但只选择一个合适的执行。如果同时按住右左，总优先执行if
    def update(self):
        if self.moving_right and self.rect.right<self.ai_settings.screen_width:
            self.x_coordinate += float(self.ai_settings.speed_factor)
        if self.moving_left and self.rect.left>0:
            self.x_coordinate -= float(self.ai_settings.speed_factor)
        if self.moving_up and self.rect.top>0:
            self.y_coordinate -= float(self.ai_settings.speed_factor)
        if self.moving_down and self.rect.bottom<self.ai_settings.screen_height:
            self.y_coordinate += float(self.ai_settings.speed_factor)

        self.rect.centerx=self.x_coordinate
        self.rect.bottom=self.y_coordinate

    #重新绘制
    def blitme(self):
        self.screen.blit(self.image,self.rect)