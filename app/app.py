import sys, os
import pygame

from data import data, GUI, entities

from .initializeGUI import initializeGUI
from .updateGUI import updateGUI
from .renderMap import renderMap
from .eventHandling import eventHandling


def app(): 
    initializeGUI()

    while not data['exit']:
        eventHandling()
        renderMap()
        updateGUI()

    pygame.quit()