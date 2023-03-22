import sys, os
import pygame

from data import data, GUI

def initializeGUI():
    pygame.init()
    pygame.font.init()

    GUI['window'] = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    GUI['clock'] = pygame.time.Clock()
    GUI['font'] = pygame.font.Font(None, 24)


    GUI['leftMenu'] = pygame.Surface((250, 1080))
    GUI['leftMenu'].fill((220, 220, 220))

    GUI['simArea'] = pygame.Surface((1980-250, 1080))
    GUI['simArea'].fill((50, 50, 50))

    GUI['text']=GUI['font'].render("Tick: ", True, (0, 0, 0))


    GUI['textures']['cell'] = pygame.image.load(r'./resources/img/cell.png')  
    GUI['textures']['food'] = pygame.image.load(r'./resources/img/food.png')  

    pygame.display.set_caption('Test')