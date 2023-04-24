import tkinter as tk

from .components.Txt import Txt

from model.entities.Entity import Entity

class EntityInfo(tk.Frame):
    def __init__(self, parent, **args):
        super().__init__(parent, **args)
        
        self.grid(sticky='nesw')
        
        if len(Entity.all)>0:
            self.columnconfigure(0, weight=1)
            self.selectedEntity = Entity.all[200]
            self.initializeTxts(self.selectedEntity, **args)
        
    def entityProperties(self, obj):
        res = []
        for k, value in obj.__dict__.items():
            keyIndex=0
            for i, letter in enumerate(k[::-1]):
                if letter=='_': 
                    keyIndex=i
                    break
            res.append((k[-keyIndex:],value))
        return res
    
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
    
        