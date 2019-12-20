import pygame.font

class Button():
    def __init__(self,screen):
        self.screen=screen
        self.screen_rect=screen.get_rect()

        self.image=pygame.image.load('play_button.png')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #初始位置：正中心
        self.rect.center=self.screen_rect.center

    def draw_button(self):
        self.screen.blit(self.image,self.rect)        


