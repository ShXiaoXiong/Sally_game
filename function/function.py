import sys
import pygame

from Role import Sally
from Settings import Settings
import game_functions as gf

def run_game():
    pygame.init()
    pygame.display.set_caption('莎莉打豆豆')
    
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    

    #创建角色
    sally=Sally(screen)

    while True:
        gf.check_event(sally)
        
        #屏幕更新写在此处，避免循环引用
        background = pygame.image.load('back.png').convert()
        screen.blit(background,(0,0))
        sally.blitme()
        pygame.display.flip()


run_game()

