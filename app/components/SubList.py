import tkinter as tk
from functools import partial


from .Txt import Txt

from data import GUI, data
from data import  data as d

class SubList(tk.Frame):
    def __init__(self, parent, column=0, row=0, sticky='wens', text='', data=[], **args):
        super().__init__(parent, **args)

        self.grid(column=column, row=row, sticky=sticky)
        # self.focus_set()
        
        self.listElements=[]
        self.bg=args['bg']
        
        for index, el in enumerate(data):
            element=Txt(self, row=index, column=0, text=f"{index+1}:\t{el.name}", bg=self.bg)
            # element.focus_set()
            element.bind("<Button-1>", partial(self.onClick, el=el, **args))
            
            self.listElements.append(element)
        
    def conf(self, data):
        for index, el in enumerate(self.listElements):
            if index >= len(data):
                el.destroy()
                self.listElements.pop(index)
            elif index < len(data):
                el.config(text=f"{index+1}:\t{data[index].name}")
                
        if len(data) > len(self.listElements):
            for index, el in enumerate(data):
                if index > len(self.listElements)-1:
                    element=Txt(self, row=index, column=0, text=f"{index+1}:\t{el.name}", bg=self.bg)
                    # element.focus_set()
                    element.bind("<Button-1>", partial(self.onClick, el=el))
                    
                    self.listElements.append(element)
        
    def onClick(self, e, el, **args):
        data['selectedEntity']=el

        
        
        
        # __init__
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