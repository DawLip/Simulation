import pygame

from data import data, GUI

def eventHandling():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            data['exit']=True
            break

        