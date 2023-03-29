import pygame

from data import data, GUI

class Section():
    all=[]
    clickableSectionsList=[]
    def __init__(
            self, name="", parent=None,
            size=(100, 100), position=(0,0), 
            bgc=(255,255,255), 
        ):

        self.name=name
        self.parentName=parent
        self.size=size
        self.x=position[0]
        self.y=position[1]
        self.bgc=bgc

        self.toRunDuringUpdate=[]

        self.clickable=False
        self.toUpdate=False
        if name=='map': self.toUpdate=True

        if self.parentName != None: 
            self.parent=[x for x in Section.all if x.name==parent][0]
            self.parentSurface = self.parent.surface
        else: self.parentSurface = GUI['window']
        
        self.surface = pygame.Surface(size)
        self.surface.fill(self.bgc)

        Section.all.append(self)

    def update(self, firstUpdate):
        if firstUpdate:
            self.surface.fill(self.bgc)
    
            # for f in self.toRunDuringUpdate: f()
            if self.parentName != None:
                GUI['window'].blit(self.surface, (self.parent.x+self.x, self.parent.y+self.y))
            else:
                GUI['window'].blit(self.surface, (self.x, self.y))

            