import tkinter as tk

from app.components.WindowApp import WindowApp

from ..components.Txt import Txt

from model.entities.Entity import Entity

class EntityInfo(WindowApp):
    def __init__(self, parent, **args):
        super().__init__(parent, **args)
        
        self.grid(row=2, sticky='nswe')
        self.columnconfigure(0, weight=1)

    def inicialize(self, **args):
        self.selectedEntity = Entity.all[-1]
        self.labelList=[]

        i=0
        res = []
        for k, value in self.selectedEntity.__dict__.items():
            keyIndex=0
            for i, letter in enumerate(k[::-1]):
                if letter=='_': 
                    keyIndex=i
                    break
            res.append((k[-keyIndex:],value))

        for key, value in res:
            self.labelList.append(Txt(self, row=i, column=0, text=f"{key}: {value}", bg=args['bg']))
            i+=1

        return super().inicialize(**args)
    
    def refresh(self, **args):
        i=0
        res = []
        for k, value in self.selectedEntity.__dict__.items():
            keyIndex=0
            for i, letter in enumerate(k[::-1]):
                if letter=='_': 
                    keyIndex=i
                    break
            res.append((k[-keyIndex:],value))

        for key, value in res:
            if i<len(self.labelList):
                self.labelList[i].config(text=f"{key}: {value}")
                i+=1


        return super().refresh(**args)
    
    
        