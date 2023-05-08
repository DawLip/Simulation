import tkinter as tk

from app.components.WindowApp import WindowApp

from data import GUI

class BottomBar(tk.Frame):
    def __init__(self, parent, **args):
        super().__init__(parent, bg=GUI['colors']['0 color'], **args)
        
        self.grid(row=3, column=0, columnspan=3, sticky='nswe')
    