import tkinter as tk

from app.components.WindowApp import WindowApp

from ..components.Txt import Txt
from ..components.List import List

from model.entities.Entity import Entity

from data import debug

class Entities(WindowApp):
    def __init__(self, parent, **args):
        super().__init__(parent, padx=4, pady=4, **args)
        
        self.grid(row=2, sticky='nesw')
        self.columnconfigure(0, weight=1)

    def inicialize(self, **args):
        self.labelList=[]
        
        self.render(True, **args)

        return super().inicialize(**args)

    def refresh(self, **args):
        self.render(**args)
        return super().refresh(**args)

    def render(self, isInicialize=False, **args):
        d = {}
        for entity in Entity.all:
            isFirstElement=True
            for element in list(d.keys()):
                if entity.__class__.__name__==element:
                    d[entity.__class__.__name__]+=1
                    isFirstElement=False
                    break
                
            if isFirstElement:
                d[entity.__class__.__name__]=1
                
        i=0
        for key, value in  d.items():
            if isInicialize:
                self.labelList.append(List(self, row=i, column=0, text=f"{key}: {value}", bg=args['bg']))
            else:               
                self.labelList[i].conf(text=f"{key}: {value}")
            i+=1
        
        
            
    
        