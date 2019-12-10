import sys
import pygame

def check_event(sally):
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()

            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    sally.rect.centerx +=1
 