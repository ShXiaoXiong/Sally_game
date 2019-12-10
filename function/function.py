import sys
import pygame

from Role import Sally
from Settings import Settings

def run_game():
    pygame.init()
    pygame.display.set_caption('莎莉打豆豆')
    
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    

    #创建角色
    sally=Sally(screen)

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        screen.fill(ai_settings.bg_color)
        sally.blitme()
        pygame.display.flip()

run_game()

