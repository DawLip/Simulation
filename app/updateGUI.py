import sys, os
import pygame

from data import data, GUI

def updateGUI():
    GUI['text2']=GUI['font'].render(str(data['tick']), True, (0, 0, 0))


    GUI['window'].fill((255, 0, 0))

    GUI['window'].blits((
        (GUI['leftMenu'], (0, 0)),
        (GUI['simArea'], (250, 0))
        ))

    GUI['simArea'].fill((50, 50, 50))
    GUI['simArea'].blits(GUI['sprites'])

    GUI['leftMenu'].fill((230, 230, 230))
    GUI['leftMenu'].blit(GUI['text'], (16,16))
    GUI['leftMenu'].blit(GUI['text2'], (16+100, 16))

    GUI['sprites']=[]

    pygame.display.update()

    GUI['clock'].tick(data['frameRate'])