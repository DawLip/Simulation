import pygame

from .UIComponents.UIComponents import Section
from .updateGUI import updateGUI

from data import data, GUI

def eventHandling():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            data['exit']=True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            for s in Section.clickableSectionsList:
                x, y=pygame.mouse.get_pos()
                w=s.size[0]
                h=s.size[1]

                if s.x < x < s.x+w and s.y < y < s.y+h:
                    s.action()
                    
        elif event.type == pygame.VIDEORESIZE:
            GUI['windowWidth']=event.w
            GUI['windowHeight']=event.h

            updateGUI(True)
            pygame.display.update()
