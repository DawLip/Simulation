import pygame

from data import data, GUI
from .UIComponents.section import Section

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
