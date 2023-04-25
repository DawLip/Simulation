import tkinter as tk

class WindowTab(tk.Button):
    def __init__(self, parent, text, column=0, row=0,  **args):
        if text == "AllEntitiesInfo" or text == "EntityInfo": self.img = tk.PhotoImage(file = "./resources/GUI/GUItmp1.png"),
        elif text == "Simulation": self.img = tk.PhotoImage(file = "./resources/GUI/GUItmp2.png"),
        else: self.img = tk.PhotoImage(file = "./resources/GUI/GUItmp3.png"),

        super().__init__(
            parent,
            image=self.img,
            borderwidth=0,
            highlightthickness=0,
            **args
        )
        self.grid(column=column, row=row, sticky='w')