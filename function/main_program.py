import sys
import pygame

from class_Player import Sally
from class_Guai import Guai
from Settings import Settings
from pygame.sprite import Group
import game_functions as gf
from class_Bullet import Bullet

#主程序，创建了一系列整个游戏都要用到的对象
def run_game():
    pygame.init()
    pygame.display.set_caption('莎莉打豆豆')
    
    #创建屏幕
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))

    #创建角色
    sally=Sally(screen,ai_settings)
    guais=Group()
    gf.create_fleet(screen,ai_settings,guais)
    #在循环外部创建子弹编组
    bullets=Group()
   
    #游戏主循环：检查玩家输入，然后更新sally，更新子弹，重绘屏幕
    while True:
        gf.check_event(screen,ai_settings,sally,bullets)
        sally.update()
        gf.update_bullets(bullets)   
        gf.update_screen(screen,bullets,sally,guais)

run_game()

