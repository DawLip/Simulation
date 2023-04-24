import tkinter as tk

class Txt(tk.Label):
    def __init__(self, parent, column=0, row=0, sticky='w', **args):
        super().__init__(
            parent, 
            fg='#D8D8E6', 
            **args
        )
        self.grid(column=column, row=row, sticky=sticky)
