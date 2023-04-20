import tkinter as tk

from .components.Txt import Txt

from model.entities.Entity import Entity

class EntityInfo(tk.Frame):
    def __init__(self, parent, **args):
        super().__init__(parent, padx=2, pady=2, highlightbackground='black', bg='#3E3E42', highlightthickness=2, **args)
        
        self.grid(column=0, row=1, sticky='nesw',columnspan=1)
        
        if len(Entity.all)>0:
            self.columnconfigure(0, weight=1)
            self.selectedEntity = Entity.all[200]
            self.rowconfigure(len(self.entityProperties(self.selectedEntity)), weight=1)
            self.initializeTxts(**args)
        
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
    
    def initializeTxts(self, **args):
        i=0
        for key, value in self.entityProperties(self.selectedEntity):
            Txt(self, row=i, column=0, text=f"{key}: {value}", **args)
            i+=1
    
        