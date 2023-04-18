import tkinter as tk

class Placeholder(tk.Frame):
    def __init__(self, parent, **args):
        super().__init__(parent, **args)

        self.grid(sticky='wens')