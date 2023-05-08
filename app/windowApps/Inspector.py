import tkinter as tk

from app.components.WindowApp import WindowApp

from ..components.Txt import Txt

from model.entities.Entity import Entity

from data import data

class Inspector(WindowApp):
    def __init__(self, parent, **args):
        super().__init__(parent, padx=4, pady=4, **args)
        
        self.grid(row=2, sticky='nswe')
        self.columnconfigure(0, weight=1)

    def inicialize(self, **args):
        data['selectedEntity'] = Entity.all[-1]
        self.selectedEntity = Entity.all[-1]
        self.labelList=[]

        self.render(True, **args)

        return super().inicialize(**args)
    
    def refresh(self, **args):
        self.render(**args)
        self.selectedEntity=data['selectedEntity']
        
        return super().refresh(**args)
    
    def render(self, isInicialize=False, **args):
        i=0
        res = []
        for k, value in self.selectedEntity.__dict__.items():
            keyIndex=0
            for i, letter in enumerate(k[::-1]):
                if letter=='_': 
                    keyIndex=i
                    break
            res.append((k[-keyIndex:],value))

        i=0
        for key, value in res:    
            if isInicialize:
                self.labelList.append(Txt(self, row=i, column=0, text=f"{key}: {value}", bg=args['bg']))
            else:
                if i<len(self.labelList):
                    self.labelList[i].config(text=f"{key}: {value}")
            i+=1
    
    
        