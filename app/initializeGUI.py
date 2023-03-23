import sys, os
import pygame

from .components.Button import Button
from data import data, GUI

def sectionConstructor(section):
    GUI[section['name']] = pygame.Surface(section['size'])
    GUI[section['name']].fill(section['color'])

def initializeGUI():
    pygame.init()
    pygame.font.init()

    width=GUI['windowWidth']
    height=GUI['windowHeight']
    mapWidth=data['simWidth']
    mapWeight=data['simHeight']

    textureSize=GUI['texturesSize']

    sections=[
        {'name': 'topMenu',  'size': (width, 30),             'color': (70, 70, 70)},
        {'name': 'leftMenu', 'size': (250, height-30),        'color': (220, 220, 220)},
        {'name': 'simArea',  'size': (width-500, height-30),  'color': (50, 50, 50)},
        {'name': 'rightMenu','size': (250, height-30),        'color': (220, 220, 220)},
        {'name': 'map',      'size': (mapWidth*textureSize, mapWeight*textureSize), 'color': (255, 255, 255)},
    ]

    GUI['window'] = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    GUI['clock'] = pygame.time.Clock()
    GUI['font'] = pygame.font.Font(None, 24)

    GUI['topBarButtons'].append(Button(position=(width-104, 4), action='exit'))

    for section in sections:
        sectionConstructor(section)

    GUI['text']=GUI['font'].render("Tick: ", True, (0, 0, 0))


    # import textures
    GUI['textures']['cell'] = pygame.image.load(r'./resources/img/cell.png')  
    GUI['textures']['food'] = pygame.image.load(r'./resources/img/food.png')  

    pygame.display.set_caption('Test')