import sys, os
import pygame

from data import data, GUI

def updateGUI():
    GUI['text2']=GUI['font'].render(str(data['tick']), True, (0, 0, 0))


    GUI['window'].fill((255, 0, 0))

    GUI['window'].blits((
        (GUI['topMenu'], (0, 0)),
        (GUI['leftMenu'], (0, 30)),
        (GUI['simArea'], (250, 30)),
        (GUI['rightMenu'], (1920-250, 30)),
        ))


    GUI['topMenu'].fill((70, 70, 70))
    GUI['topBarButtons'][0].update()
    GUI['topMenu'].blit(GUI['topBarButtons'][0].surface, GUI['topBarButtons'][0].position)

    GUI['simArea'].fill((50, 50, 50))
    GUI['simArea'].blit(
        GUI['map'], 
        (
            (1920-500-(data['simWidth']*GUI['texturesSize']))/2,
            (1080-30-(data['simHeight']*GUI['texturesSize']))/2
        ))
    GUI['map'].blits(GUI['sprites'])

    GUI['leftMenu'].fill((230, 230, 230))
    GUI['leftMenu'].blit(GUI['text'], (16,16))
    GUI['leftMenu'].blit(GUI['text2'], (16+100, 16))

    GUI['rightMenu'].fill((230, 230, 230))
    # GUI['rightMenu'].blit(GUI['text'], (16,16))


    GUI['sprites']=[]
    pygame.display.update()
    GUI['clock'].tick(data['frameRate'])