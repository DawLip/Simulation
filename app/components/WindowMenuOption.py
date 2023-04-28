import tkinter as tk

from data import GUI

class WindowMenuOption(tk.Button):
    def __init__(self, parent, column=0, row=0,  **args):
        super().__init__(
            parent,
            padx=8,
            borderwidth=0,
            highlightthickness=0,
            bg=GUI['colors']['0 color'],
            fg=GUI['colors']['Font White'], 
            **args
        )
        
        
        
        
        self.grid(column=column, row=row, sticky='w')
        
        