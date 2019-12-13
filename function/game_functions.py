import sys
import pygame
from class_Bullet import Bullet
from class_Guai import Guai

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
    elif event.key==pygame.K_q:
        sys.exit()
        
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


#创建第一个怪，然后计算空间
def create_fleet(screen,ai_settings,guais):
    #创建一个怪，读取他的长宽属性，这个怪并不加入编组，是工具怪
    guai=Guai(screen,ai_settings)
    guai_width=float(guai.rect.width)
    guai_height=float(guai.rect.height)
    #计算可用空间：左右各空半格，上方空0.2格
    available_space_x=ai_settings.screen_width-guai_width
    available_space_y=0.4*ai_settings.screen_height-0.2*guai_height
    #计算可放的最大数量：横向间距1个，纵向间距0.2个
    number_guai_x=int(available_space_x/(2*guai_width))
    number_guai_y=int(available_space_y/(1.2*guai_height))    
    
    #创建循环
    for xx in range(number_guai_x):
        guai=Guai(screen,ai_settings)#正式生成一个怪        
        #重新定x坐标
        guai.rect.x=0.5*guai_width+2*guai_width*(xx-1)
        #重新定y坐标，为循环，每次循环后加入编组
        for yy in range(number_guai_y):
            guai.rect.y=0.2*guai_height+1.2*guai_height*(yy-1)
            guais.add(guai)



#重绘屏幕
def update_screen(screen,bullets,sally,guais):
    background = pygame.image.load('back.png').convert()
    screen.blit(background,(0,0))
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    sally.blitme()
    guais.draw(screen)
    pygame.display.flip()

 