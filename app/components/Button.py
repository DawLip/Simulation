import pygame

from data import data, GUI

class Button():
    def __init__(self, txt="Button", size=(100, 20), position=(0,0), bgc=(255, 255, 255), action=None):
        self.size=size
        self.position=position
        self.action=action
        
        self.txt = GUI['font'].render(txt, True, (0, 0, 0))

        self.surface = pygame.Surface(size)
        self.surface.fill(bgc)

    def update(self):
        self.surface.blit(self.txt, (2,2))
    
    def action(self, action=None):
        if action!=None:              action()
        elif self.action=='exit':     data['exit']=True