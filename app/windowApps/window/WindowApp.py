import tkinter as tk 
import math
from functools import partial

from data import data

class WindowApp(tk.Frame):
    def __init__(self, parent, **args):
        super().__init__(parent, **args)

        self.grid_propagate(False)
        self.grid(column=0, row=2, sticky='wens')
        
        self.bind("<Button-1>", self.setFocus)

        self.inicialize(**args)
        self.refresh(**args)

    def inicialize(self, **args):
        pass

    def refresh(self, frameRate=data['GUIframeRate'], **args):
        self.after(int(1000/frameRate), partial(self.refresh, **args))
        
    def setFocus(self, e):
        self.focus_set()