
import pygame.font
from pygame.sprite import Group
from class_Player import Xueliang


class Scoreboard():
    def __init__(self,screen,ai_settings,stats):
        self.screen=screen
        self.screen_rect=screen.get_rect()
       
        self.ai_settings=ai_settings
        self.stats=stats


        #显示得分的字体
        self.text_color_1=(30,30,30)
        self.text_color_2=(241,10,30)

        self.font=pygame.font.Font('msyhl.ttc',32)# 读取字体和字号
       
        #准备初始得分图像，把可能变化的信息调出去了
        self.prep_score()
        self.prep_level()
        self.prep_xueliang()

    def prep_score(self):
        round_score=round(self.stats.score,0)
        score_str='{:,}'.format(round_score)
        score_str='分数: ' + score_str
        self.score_image=self.font.render(score_str,True,self.text_color_1)#不加第四个参数就是背景透明


        #位置
        self.score_rect= self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right - 40
        self.score_rect.top=20


    def prep_level(self):
        level_str='难度：' + str(self.stats.level)
        self.level_image=self.font.render(level_str,True,self.text_color_2)#不加第四个参数就是背景透明

        #位置
        self.level_rect= self.level_image.get_rect()
        self.level_rect.centerx=self.screen_rect.centerx
        self.level_rect.top=20

    def prep_xueliang(self):
        self.xueliang=Group()
        for xueliang_number in range(self.stats.sally_left):
            yiming=Xueliang(self.screen,self.ai_settings)
            yiming.rect.x= 50 + xueliang_number * yiming.rect.width
            yiming.rect.y=20
            self.xueliang.add(yiming)

        #位置
        self.level_rect= self.level_image.get_rect()
        self.level_rect.centerx=self.screen_rect.centerx
        self.level_rect.top=20

    def draw_board(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.xueliang.draw(self.screen)
