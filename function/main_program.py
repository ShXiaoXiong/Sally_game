import sys
import pygame

from class_Player import Sally
from class_Guai import Guai
from Settings import Settings
from pygame.sprite import Group
import game_functions as gf
from class_Bullet import Bullet
from button import Button
from game_stats import Gamestats


#主程序，创建了一系列整个游戏都要用到的对象
def run_game():
    pygame.init()
    pygame.display.set_caption('莎莉打豆豆')
    
    #创建屏幕，初始化设置，初始化统计信息
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    stats= Gamestats(ai_settings)

    #创建开始按钮
    play_button=Button(screen)

    #创建角色
    sally=Sally(screen,ai_settings)
    guais=Group()
    gf.create_fleet(screen,ai_settings,guais)

    #在循环外部创建子弹编组
    bullets=Group()
   
    #游戏主循环（即每一帧）：检查玩家输入，然后更新sally，更新子弹，重绘屏幕
    while True:
        #在主循环中，任何情况下都要调用check_event()，以获取用户输入，包括按键和退出
        gf.check_event(screen,ai_settings,sally,bullets,play_button,stats)
        #在主循环中，任何情况下都要画背景图，并检查游戏是否活动
        gf.update_screen(screen,stats,play_button)
        #更新各个对象：XXX这写得不好，可以分类来更新
        if stats.game_active:
            sally.update()
            gf.update_bullets(bullets,screen,ai_settings,guais)
            gf.update_guais(sally,stats,bullets,screen,ai_settings,guais)
            gf.update_objects(bullets,sally,guais,screen)
        
        pygame.display.flip()#刷新屏幕

run_game()

