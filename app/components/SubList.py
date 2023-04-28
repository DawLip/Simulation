import tkinter as tk
from functools import partial


from .Txt import Txt

from data import GUI 

class SubList(tk.Frame):
    def __init__(self, parent, column=0, row=0, sticky='wens', text='', data=[], **args):
        super().__init__(parent, **args)

        self.grid(column=column, row=row, sticky=sticky)
        self.focus_set()
        
        for index, el in enumerate(data):
            Txt(self, row=index, column=0, text=f"{el.name}", bg=args['bg'])
        # self.iconExpanded = tk.PhotoImage(file = f"./resources/GUI/downArrow.png")
        # self.iconNotExpanded = tk.PhotoImage(file = f"./resources/GUI/arrowRight.png")
        # self.isExpanded = False
        # self.expandEl = None
        
        # self.icon = tk.Label(self, image=self.iconNotExpanded, bg=args['bg'])
        # self.icon.grid(row=0, column=0)
        # self.label = Txt(self, row=0, column=1, text=text, bg=args['bg'])
        
        # self.bind('<Button-1>', self.onClick)
        # for child in  self.winfo_children():
        #     child.bind("<Button-1>", partial(self.onClick, **args))
        #     child.bind("<Button-1>", partial(self.onClick, **args))
        
    def conf(self, text):
        self.label.config(text=text)
        
    def onClick(self, e, **args):
        print(e)
