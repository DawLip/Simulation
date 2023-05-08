import tkinter as tk
from functools import partial

from .WindowMenuOption import WindowMenuOption

from data import GUI

class WindowMenu(tk.Frame):
    def __init__(self, parent, column=0, row=1,  options={}, **args):
        bg=GUI['colors']['0 color']
        highlightbackground=GUI['colors']['1 borderColor']
        
        super().__init__(parent, bg=bg, highlightbackground=highlightbackground, highlightthickness=1, *args)

        self.grid(column=column, row=row, sticky='wens')
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(2, weight=1)
        # self.grid_propagate(False)

        self.options=[]

        self.leftMenu=tk.Frame(self, bg=bg)
        self.midMenu=tk.Frame(self, bg=bg)
        self.rightMenu=tk.Frame(self, bg=bg)
        
        self.leftMenu.grid(column=0, row=0, sticky='w')
        self.midMenu.grid(column=1, row=0, sticky='we')
        self.rightMenu.grid(column=2, row=0, sticky='e')
        
        for index, name in enumerate(options['left']):
            self.options.append(WindowMenuOption(self.leftMenu, text=name, column=index))
            
        for index, name in enumerate(options['mid']):
            self.options.append(WindowMenuOption(self.midMenu, text=name, column=index))
            
        for index, name in enumerate(options['right']):
            self.options.append(WindowMenuOption(self.rightMenu, text=name, column=index))