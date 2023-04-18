import tkinter as tk

class WindowTab(tk.Button):
    def __init__(self, parent, column=0, row=0,  **args):
        super().__init__(
            parent, 
            bg='#4B4B52', fg='#D8D8E6', 
            activebackground='#4B4B52', activeforeground='#D8D8E6',
            **args
        )

        self.grid(column=column, row=row, sticky='w')