import tkinter as tk

from .Txt import Txt

from data import GUI 

class List(tk.Frame):
    # def __init__(self, parent, column=0, row=0, sticky='wens', text='', bg='', **args):
    def __init__(self, parent, column=0, row=0, sticky='wens', text='', **args):
        # super().__init__(parent, bg='red', **args)
        super().__init__(parent, **args)

        self.grid(column=column, row=row, sticky=sticky)
        
        self.iconImg = tk.PhotoImage(file = f"./resources/GUI/arrowRight.png")
        
        # self.icon = tk.Label(self, image=self.iconImg, bg=bg).grid(row=0, column=0)
        # self.label = Txt(self, row=0, column=1, text=text, bg=bg)
        self.icon = tk.Label(self, image=self.iconImg, bg=args['bg']).grid(row=0, column=0)
        self.label = Txt(self, row=0, column=1, text=text, bg=args['bg'])
        
        self.focus_set()
        # self.bind('<Button-1>', self.onClick)
        
    def conf(self, text):
        self.label.config(text=text)
        
    def onClick(self, e):
        print(e)
