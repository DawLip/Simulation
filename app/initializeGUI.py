import sys, os
import pygame

from .UIComponents.section import Section
from .UIComponents.button import Button

from data import data, GUI

def exitButtonAction(): data['exit']=True
def startSimAction(): data['isSimRunning']=True
def stopSimAction(): data['isSimRunning']=False

def initializeGUI():
    pygame.init()
    pygame.font.init()

    GUI['window'] = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    GUI['clock'] = pygame.time.Clock()
    GUI['font'] = pygame.font.Font(None, 24)

    w=GUI['windowWidth']
    h=GUI['windowHeight']
    mw=data['simWidth']
    mh=data['simHeight']

    ts=GUI['texturesSize']

    sections=[
        {
            'name': 'topMenu', 'parent': None,
            'size': (w, 32), 'position':(0, 0),
            'bgc': (40, 40, 40), 'update': False,
        },{
            'name': 'leftMenu', 'parent': None,
            'size': (250, h-30), 'position':(0, 32),
            'bgc': (220, 220, 220), 'update': False,
        },{
            'name': 'simArea', 'parent': None, 
            'size': (w-500, h-30), 'position':(250, 32), 
            'bgc': (50, 50, 50), 'update': False,
        },{
            'name': 'rightMenu', 'parent': None,
            'size': (250, h-30), 'position':(w-250, 32),
            'bgc': (220, 220, 220), 'update': False,
        },{
            'name': 'map', 'parent': 'simArea',     
            'size': (mw*ts, mh*ts), 'position':((w-500-mw*ts)/2, (h-32-mh*ts)/2),
            'bgc': (200, 200, 200),
        },{
            'name': 'exitButton', 'parent': 'topMenu', 'type': "button",      
            'size': (48, 32-8), 'position':(w-48-4, 4),
            'bgc': (255, 255, 255), 'update': False,
            'txt': 'Quit', 'action': exitButtonAction,
        },{
            'name': 'startSimButton', 'parent': 'topMenu', 'type': "button",      
            'size': (48, 32-8), 'position':(0, 4),
            'bgc': (255, 255, 255), 'update': False,
            'txt': 'Start', 'action': startSimAction,
        },{
            'name': 'stopSimButton', 'parent': 'topMenu', 'type': "button",      
            'size': (48, 32-8), 'position':(48+1, 4),
            'bgc': (255, 255, 255), 'update': False,
            'txt': 'Stop', 'action': stopSimAction,
        },
    ]

    for section in sections:
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
            )


    # import textures
    GUI['textures']['cell'] = pygame.image.load(r'./resources/img/cell.png')  
    GUI['textures']['food'] = pygame.image.load(r'./resources/img/food.png')  

    pygame.display.set_caption('Test')

    # Section.all[5].surface.fill((255,0,0))
    # Section.all[0].parentSurface.blit(Section.all[5].surface, (0, 0))