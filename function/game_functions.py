import sys
import pygame

def check_keydown_event(event,sally,screen,ai_settings,bullets):
    if event.key==pygame.K_RIGHT:
        sally.moving_right=True
    if event.key==pygame.K_LEFT:
        sally.moving_left=True
    if event.key==pygame.K_UP:
        sally.moving_up=True
    if event.key==pygame.K_DOWN:
        sally.moving_down=True
    if event.key==pygame.K_SPACE:
        new_bullet=Bullet(ai_settings,screen,sally)
        bullets.add(new_bullet)

def check_keyup_event(event,sally):
    if event.key==pygame.K_RIGHT:
        sally.moving_right=False
    if event.key==pygame.K_LEFT:
        sally.moving_left=False
    if event.key==pygame.K_UP:
        sally.moving_up=False
    if event.key==pygame.K_DOWN:
        sally.moving_down=False

def check_event(screen,ai_settings,sally,bullets):
    #主逻辑：游戏运行
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
           
            elif event.type==pygame.KEYDOWN:
                check_keydown_event(event,screen,ai_settings,sally,bullets)
            
            #此处用elif，是因为只可能存在一种情况
            elif event.type==pygame.KEYUP:
                check_keyup_event(event,sally)

 
 