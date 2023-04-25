import tkinter as tk

from app.components.WindowApp import WindowApp

from ..components.Txt import Txt

from model.entities.Entity import Entity

class EntityInfo(WindowApp):
    def __init__(self, parent, **args):
        super().__init__(parent, **args)
        
        self.grid(sticky='nswe')
        self.columnconfigure(0, weight=1)

    def inicialize(self):
        self.selectedEntity = Entity.all[-1]
        return super().inicialize()
    
    def refresh(self, **args):
        if len(Entity.all)>0:
            self.initializeTxts(self.selectedEntity, **args)

        return super().refresh(**args)

    def initializeTxts(self, obj, **args):
        i=0
        res = []
        for k, value in obj.__dict__.items():
            keyIndex=0
            for i, letter in enumerate(k[::-1]):
                if letter=='_': 
                    keyIndex=i
                    break
            res.append((k[-keyIndex:],value))
        for key, value in res:
            Txt(self, row=i, column=0, text=f"{key}: {value}", bg=args['bg'])
            i+=1
    
    
        