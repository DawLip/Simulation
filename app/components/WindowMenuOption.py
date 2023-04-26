import tkinter as tk

class WindowMenuOption(tk.Button):
    def __init__(self, parent, column=0, row=0,  **args):
        
        super().__init__(
            parent,
            borderwidth=0,
            highlightthickness=0,
            **args
        )
        self.grid(column=column, row=row, sticky='w')