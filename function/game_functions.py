import sys
import pygame
from class_Bullet import Bullet
from class_Guai import Guai
from time import sleep


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
        
#空格键事件-开火：创建新的子弹，加入子弹编组
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
    
#检查时间：为了获取用户输入，首先是退出事件，然后鼠标、键盘
def check_event(screen,ai_settings,sally,bullets,play_button,stats):
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
           
            elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y=pygame.mouse.get_pos()#获取鼠标点击的位置
                check_play_button(play_button,mouse_x,mouse_y,stats)

            elif event.type==pygame.KEYDOWN:
                check_keydown_event(event,screen,ai_settings,sally,bullets)
            
            #此处用elif，是因为只可能存在一种情况
            elif event.type==pygame.KEYUP:
                check_keyup_event(event,sally)

#检查鼠标点击的位置，整个rect都算，所以按键必须是方形的
#写在一起更好，因为mouse_x,mouse_y是内部引用
def check_play_button(play_button,mouse_x,mouse_y,stats):
    if play_button.rect.collidepoint(mouse_x,mouse_y):
        stats.game_active = True

###########################

#更新子弹：更新子弹的位置-删除飞出屏幕的子弹-检查碰撞
def update_bullets(bullets,screen,ai_settings,guais):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)

    #每一次更新子弹位置后，检查碰撞，删除碰撞的bullets及guais
    collisions=pygame.sprite.groupcollide(bullets,guais,True,True)

    #因为在此处被消灭，所以在此处检查编组alians是否为空
    if len(guais)==0:
        create_fleet(screen,ai_settings,guais)

###########################
#计算分配给空间，并创建舰队
def create_fleet(screen,ai_settings,guais):
    #创建一个怪，读取他的长宽属性，这个怪并不加入编组，是工具怪
    guai=Guai(screen,ai_settings)
    guai_width=float(guai.rect.width)
    guai_height=float(guai.rect.height)
    #计算可用空间：左右各空半格，上方空
    available_space_x=ai_settings.screen_width-guai_width
    available_space_y=ai_settings.screen_height-6*guai_height
    #计算可放的最大数量：横向间距1个，纵向间距0.2个
    number_guai_x=int(available_space_x/(2*guai_width))
    number_guai_y=int(available_space_y/(1.2*guai_height))    
    #创建怪群
    for xx in range(number_guai_x):
        for yy in range(number_guai_y):
            guai=Guai(screen,ai_settings)#正式生成一个怪        
            #重新定x坐标，左边空0.5个怪的宽
            guai.rect.x=0.5*guai_width+2*guai_width*xx
            #重新定y坐标，上方空一个怪的高
            guai.rect.y=guai_height+1.2*guai_height*yy
            guais.add(guai)

####################
#移动方式1   
#检查事项：是否有任意怪撞墙，并执行撞墙动作
def check_fleet_edge(guais):
    for guai in guais:
        if guai.check_edge():#遍历怪，如果有任一撞墙，全部执行撞墙动作，然后break，因为可能有多行怪
            change_fleet_direction_drop(guais)
            break
           
#撞墙动作：全部怪下移并调整方向
def change_fleet_direction_drop(guais):
    for guai in guais:
        guai.guai_direction=-1*guai.guai_direction#Guai中已经存储为属性
        guai.rect.y += guai.ai_settings.guai_drop_speed_factor

#更新怪：
def update_guais(sally,stats,bullets,screen,ai_settings,guais): 
    check_fleet_edge(guais)
    guais.update()
    #spritecollideany（）接受两个实参，一个精灵和一个编组，所以必须按顺序写
    if pygame.sprite.spritecollideany(sally,guais):
        sally_hit(stats,bullets,screen,ai_settings,guais,sally)
    check_guai_bottom(stats,bullets,screen,ai_settings,guais,sally)


#死亡事件：Sally被撞倒
def sally_hit(stats,bullets,screen,ai_settings,guais,sally):
    if stats.sally_left>0:
        stats.sally_left -=1

        #清空两个编组
        guais.empty()
        bullets.empty()
    
        #暂停2秒后，重新创建舰队和重置位置
        sleep(2)
        create_fleet(screen,ai_settings,guais)
        sally.reset_location()
    else:
        self.game_active=True

#死亡事件：怪到底部
def check_guai_bottom(stats,bullets,screen,ai_settings,guais,sally):
    for guai in guais:
        if guai.rect.bottom>=ai_settings.screen_height:
            sally_hit(stats,bullets,screen,ai_settings,guais,sally)
            break



#重绘屏幕
def update_screen(screen,stats,play_button):
    background = pygame.image.load('back.png').convert()
    screen.blit(background,(0,0))
    #如果处于非活动状态，就绘制开始按钮
    if not stats.game_active:
        play_button.draw_button()
    

def update_objects(bullets,sally,guais,screen):
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    sally.blitme()
    guais.draw(screen)
