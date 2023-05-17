import tkinter as tk

from app.windowApps.window.WindowApp import WindowApp

class Placeholder(WindowApp):
    def __init__(self, parent, **args):
        super().__init__(parent, padx=4, pady=4, **args)
        
        self.grid(sticky='nswe')
