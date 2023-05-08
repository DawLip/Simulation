import tkinter as tk

from data import GUI 

class Input(tk.Entry):
    def __init__(self, parent, column=0, row=0, sticky='we', text='', **args):
        super().__init__(
            parent, 
            fg=GUI['colors']['Font White'], 
            **args
        )

        self.grid(column=column, row=row, sticky=sticky)
        
        self.insert(0, str(text))
        # self.focus_set()
