import pygame

from data import data, GUI
from .section import Section

class Txt(Section):
    def __init__(
            # Section attrs
            self, name="", parent=None,
            size=(100, 100), position=(4,4), 
            bgc=(255,255,255), toUpdate=False,
            type="txt",

            # Txt attrs
            txt="Text",
            fontSize=24,
        ):
        
        super().__init__(name, parent, size, position, bgc, toUpdate, type)

        self.txt=txt
        self.font=pygame.font.Font(None, fontSize)

        # self.toRunDuringUpdate.append(self.updateTxt)
        
    def update(self, firstUpdate):
        if firstUpdate:
            # self.surface.fill(self.bgc)
            txt = self.font.render(self.txt, True, (0, 0, 0))
            # self.parentSurface.blit(txt, (self.x, self.y))

            GUI['window'].blit(txt, (self.x, self.y))
