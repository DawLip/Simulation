import tkinter as tk

from data import GUI 

class Txt(tk.Label):
    def __init__(self, parent, column=0, row=0, sticky='w', **args):
        super().__init__(
            parent, 
            fg=GUI['colors']['Font White'], 
            **args
        )

        self.grid(column=column, row=row, sticky=sticky)
