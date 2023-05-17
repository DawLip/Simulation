import tkinter as tk

from data import GUI

class WindowTab(tk.Button):
    def __init__(self, parent, name, column=0, row=0,  **args):
        self.img = tk.PhotoImage(file = f"./resources/GUI/Tabs/{name}Tab.png")

        super().__init__(
            parent,
            image=self.img,
            bg=GUI['colors']['3 color'],
            borderwidth=0,
            highlightthickness=0,
            **args
        )
        
        self.grid(column=column, row=row, sticky='w')