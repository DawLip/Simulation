import tkinter as tk
from functools import partial

from .Txt import Txt

from data import GUI 
from .SubList import SubList

class List(tk.Frame):
    def __init__(self, parent, column=0, row=0, sticky='wens', text='', data='', **args):
        super().__init__(parent, **args)

        self.grid(column=column, row=row, sticky=sticky)
        self.focus_set()
        
        self.iconExpanded = tk.PhotoImage(file = f"./resources/GUI/downArrow.png")
        self.iconNotExpanded = tk.PhotoImage(file = f"./resources/GUI/arrowRight.png")
        self.isExpanded = False
        self.expandEl = None
        
        self.icon = tk.Label(self, image=self.iconNotExpanded, bg=args['bg'])
        self.icon.grid(row=0, column=0)
        self.label = Txt(self, row=0, column=1, text=text, bg=args['bg'])
        
        self.icon.bind("<Button-1>", partial(self.onClick, data=data, **args))
        self.label.bind("<Button-1>", partial(self.onClick, data=data, **args))
        
    def conf(self, text):
        self.label.config(text=text)
        
    def onClick(self, e, **args):
        if self.isExpanded:     
            self.icon.config(image=self.iconNotExpanded)
            self.expandEl.destroy()
        else:     
            self.icon.config(image=self.iconExpanded)
            self.expandEl=SubList(self, row=1, column=0, text=f"", data=args['data'], bg=args['bg'])
        
        self.isExpanded = not self.isExpanded
