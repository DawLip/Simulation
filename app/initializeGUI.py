import sys, os
import pygame

from .UIComponents.section import Section
from .UIComponents.button import Button
from .sections import sections

from data import data, GUI

def initializeGUI():
    pygame.init()
    pygame.font.init()

    GUI['window'] = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    GUI['clock'] = pygame.time.Clock()
    GUI['font'] = pygame.font.Font(None, 24)

    

    for section in sections():
        if 'type' in section:
            if section['type']=='button':
                Button(
                    name=section['name'],
                    parent=section['parent'],
                    size=section['size'],
                    position=section['position'],
                    bgc=section['bgc'],
                    txt=section['txt'],
                    action=section['action']
                )
        else:
            Section(
                name=section['name'],
                parent=section['parent'],
                size=section['size'],
                position=section['position'],
                bgc=section['bgc'],
                toUpdate=section['update']
            )


    # import textures
    GUI['textures']['cell'] = pygame.image.load(r'./resources/img/cell.png')  
    GUI['textures']['food'] = pygame.image.load(r'./resources/img/food.png')  

    pygame.display.set_caption('Test')