import tkinter as tk

from app.components.WindowApp import WindowApp

from ..components.Txt import Txt

from model.entities.Entity import Entity

from data import debug

class Debug(WindowApp):
    def __init__(self, parent, **args):
        super().__init__(parent, padx=4, pady=4, **args)
        
        self.grid(sticky='nswe')
        self.columnconfigure(0, weight=1)

    def inicialize(self, **args):
        self.selectedEntity = Entity.all[-1]
        return super().inicialize()
    
    def refresh(self, **args):
        i=0
        for key, value in debug.items():
            Txt(self, row=i, column=0, text=f"{key}: {value}", bg=args['bg'])
            i+=1

        return super().refresh(**args)
    
    
        