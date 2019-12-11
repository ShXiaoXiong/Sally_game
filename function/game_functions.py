import sys
import pygame
from Bullet import Bullet

#按键
def check_keydown_event(event,screen,ai_settings,sally,bullets):
    if event.key==pygame.K_RIGHT:
        sally.moving_right=True
    if event.key==pygame.K_LEFT:
        sally.moving_left=True
    if event.key==pygame.K_UP:
        sally.moving_up=True
    if event.key==pygame.K_DOWN:
        sally.moving_down=True
    if event.key==pygame.K_SPACE:
        fire_bullet(bullets,ai_settings,screen,sally)
        
#开火
def fire_bullet(bullets,ai_settings,screen,sally):
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet=Bullet(screen,ai_settings,sally)
        bullets.add(new_bullet)
#松键
def check_keyup_event(event,sally):
    if event.key==pygame.K_RIGHT:
        sally.moving_right=False
    if event.key==pygame.K_LEFT:
        sally.moving_left=False
    if event.key==pygame.K_UP:
        sally.moving_up=False
    if event.key==pygame.K_DOWN:
        sally.moving_down=False
    
#获取用户输入
def check_event(screen,ai_settings,sally,bullets):
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
           
            elif event.type==pygame.KEYDOWN:
                check_keydown_event(event,screen,ai_settings,sally,bullets)
            
            #此处用elif，是因为只可能存在一种情况
            elif event.type==pygame.KEYUP:
                check_keyup_event(event,sally)
#更新子弹
def update_bullets(bullets):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)

#重绘屏幕
def update_screen(screen,bullets,sally):
    background = pygame.image.load('back.png').convert()
    screen.blit(background,(0,0))
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    sally.blitme()
    pygame.display.flip()

 