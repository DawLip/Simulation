import pygame

from .UIComponents.UIComponents import Section, Button
from .sections import sections

from data import GUI

def initializeGUI():
    pygame.init()
    pygame.font.init()

    GUI['window'] = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    GUI['clock'] = pygame.time.Clock()
    GUI['font'] = pygame.font.Font(None, 24)

    for section in sections():
        if 'type' in section:
            if section['type']=='button':       Button(**section)
        else:                                   Section(**section)

    # import textures
    GUI['textures']['cell'] = pygame.image.load(r'./resources/img/cell.png')  
    GUI['textures']['food'] = pygame.image.load(r'./resources/img/food.png')  

    pygame.display.set_caption('Test')