import tkinter as tk

from .components.Txt import Txt

from model.entities.Entity import Entity

class AllEntitiesInfo(tk.Frame):
    def __init__(self, parent, **args):
        super().__init__(parent, padx=2, pady=2, highlightbackground='black', bg='#3E3E42', highlightthickness=2, **args)
        
        self.grid(column=0, row=1, sticky='nesw',columnspan=1)
        
        if len(Entity.all)>0:
            self.columnconfigure(0, weight=1)
           
            self.initializeTxts(Entity.all, **args)
        
    def initializeTxts(self, obj, **args):
        d = {}
        for entity in obj:
            isFirstElement=True
            for element in list(d.keys()):
                if entity.__class__.__name__==element:
                    d[entity.__class__.__name__]+=1
                    isFirstElement=False
                    break
                
            if isFirstElement:
                d[entity.__class__.__name__]=1
        i=0
        self.rowconfigure(len(d.items()), weight=1)
        for key, value in d.items():
            Txt(self, row=i, column=0, text=f"{key}: {value}", **args)
            i+=1
    
        