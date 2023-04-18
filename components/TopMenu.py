import tkinter as tk

class TopMenu(tk.Frame):
    def __init__(self, parent, **args):
        super().__init__(parent, bg='#010102', height=48, **args)

        self.grid(column=0, row=0, sticky=tk.N + tk.S + tk.W + tk.E, columnspan=3)

        # highlightbackground="black",highlightthickness=2
        # self.bg=bg
        # redbutton = tk.Button(container, text="Red", fg="red")
        # redbutton.pack( side = tk.LEFT)