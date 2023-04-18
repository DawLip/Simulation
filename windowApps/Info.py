import tkinter as tk

from .components.Txt import Txt

class Info(tk.Frame):
    def __init__(self, parent, **args):
        super().__init__(parent, padx=2, pady=2, highlightbackground='black', bg='#3E3E42', highlightthickness=2, **args)
        
        self.grid(column=0, row=1, sticky='nesw',columnspan=1)
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(3, weight=1)
        
        Txt(self,row=0,column=0,text='x: 10',**args)
        Txt(self,row=1,column=0,text='y: 20',**args)
        Txt(self,row=2,column=0,text='energy: 120',**args)
        