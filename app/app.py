import sys, os
import pygame

from data import data, GUI

from .initializeGUI import initializeGUI
from .updateGUI import updateGUI
from .eventHandling import eventHandling


def app(): 
    initializeGUI()

    updateGUI(True)

    while not data['exit']:
        eventHandling()
        updateGUI()

    pygame.quit()