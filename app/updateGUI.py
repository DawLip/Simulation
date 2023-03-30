import pygame

from .UIComponents.UIComponents import Section
from .renderMap import renderMap

from data import data, GUI

def updateGUI(firstUpdate=False):
    for section in Section.all:
        section.update(firstUpdate)

    renderMap()
    pygame.display.update()
    
    GUI['clock'].tick(data['frameRate'])