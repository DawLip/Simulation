import tkinter as tk 
import math
from functools import partial

from data import data

class WindowApp(tk.Frame):
    def __init__(self, parent, **args):
        super().__init__(parent, **args)

        self.grid(column=0, row=1, sticky='wens')

        self.inicialize()
        self.refresh(**args)

    def inicialize(self):
        pass

    def refresh(self, frameRate=data['GUIframeRate'], **args):
        self.after(math.floor(1000/frameRate), partial(self.refresh, **args))