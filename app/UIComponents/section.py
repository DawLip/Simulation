import pygame

from data import data, GUI

class Section():
    all=[]
    clickableSectionsList=[]
    def __init__(
            self, name="", parent=None,
            size=(100, 100), position=(0,0), 
            bgc=(255,255,255), toUpdate=False
        ):

        self.name=name

        self.parentName=parent
        if self.parentName != None: 
            self.parent=[x for x in Section.all if x.name==parent][0]
            self.parentSurface = self.parent.surface
            self.x=self.parent.x+position[0]
            self.y=self.parent.y+position[1]
        else: 
            self.parentSurface = GUI['window']
            self.x=position[0]
            self.y=position[1]
            

        self.size=size
        
        self.bgc=bgc

        self.toRunDuringUpdate=[]

        self.clickable=False
        self.toUpdate=toUpdate
        if name=='map': self.toUpdate=True
        
        self.surface = pygame.Surface(size)
        self.surface.fill(self.bgc)

        Section.all.append(self)

    def update(self, firstUpdate):
        if firstUpdate or self.toUpdate:
            self.surface.fill(self.bgc)

            # for f in self.toRunDuringUpdate: f()
            if self.parentName != None:
                GUI['window'].blit(self.surface, (self.x, self.y))
            else:
                GUI['window'].blit(self.surface, (self.x, self.y))

            