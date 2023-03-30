import pygame

from .initializeGUI import initializeGUI
from .updateGUI import updateGUI
from .eventHandling import eventHandling

from data import data

def app(): 
    initializeGUI()
    updateGUI(True)

    while not data['exit']:
        eventHandling()
        updateGUI()

    pygame.quit()