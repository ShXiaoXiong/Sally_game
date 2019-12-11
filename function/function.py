import sys
import pygame

from Role import Sally
from Settings import Settings
from pygame.sprite import Group
import game_functions as gf
from Bullet import Bullet

#主程序，创建了一系列整个游戏都要用到的对象
def run_game():
    pygame.init()
    pygame.display.set_caption('莎莉打豆豆')
    
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))

    #创建角色
    sally=Sally(screen,ai_settings)
    #在循环外部创建子弹编组
    bullets=Group()
   
    #游戏主循环
    while True:
        gf.check_event(sally,ai_settings,screen,bullets)
        
        sally.update()
        bullets.update()
        #屏幕背景更新写在sally.update()和sally.biltme()中间，避免循环引用
        
        background = pygame.image.load('back.png').convert()
        screen.blit(background,(0,0))
        
        for bullet in bullets.sprites():
            bullet.draw_bullet()

        sally.blitme()
        pygame.display.flip()


run_game()

