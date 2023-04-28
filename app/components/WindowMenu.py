import tkinter as tk
from functools import partial

from .WindowMenuOption import WindowMenuOption

from data import GUI

class WindowMenu(tk.Frame):
    def __init__(self, parent, column=0, row=1,  options=[], **args):
        super().__init__(parent, bg=GUI['colors']['0 color'], highlightbackground=GUI['colors']['1 borderColor'], highlightthickness=1, *args)

        self.grid(column=column, row=row, sticky='wens')
        # self.grid_propagate(False)

        self.options=[]

        self.tabs=[]
        for index, name in enumerate(options):
            self.options.append(WindowMenuOption(self, text=name, column=index))