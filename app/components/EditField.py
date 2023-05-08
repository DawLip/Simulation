import tkinter as tk

from ..components.Txt import Txt
from ..components.Input import Input

from data import GUI, data

class EditField(tk.Frame):
    def __init__(self, parent, column=0, row=0, sticky='wesn', label='', **args):
        super().__init__(
            parent, 
            **args
        )
        
        self.columnconfigure(1, weight=1)
        
        self.selectedEntityId=id(data['selectedEntity'])
        
        self.label=Txt(self, row=0, column=0, text=f'  {label[0]}: ', bg=args['bg'])
        if label[1]:
            self.field=Input(
                self, row=0, column=1, 
                textvariable=eval(f'data["selectedEntity"].{label[0]}'), validate="focusout",
                bg=args['bg']
            )
            self.field.insert(0, str(eval(f'data["selectedEntity"].{label[0]}')))
        else:
            self.field=Txt(self, row=0, column=1, text=eval(f'data["selectedEntity"].{label[0]}'), bg=args['bg'])

        self.grid(column=column, row=row, sticky=sticky)
        
    def conf(self, label):
        if label[1]:
            if self.selectedEntityId == id(data['selectedEntity']):
                if self.field.get() != str(eval(f'data["selectedEntity"].{label[0]}')):
                    setattr(data["selectedEntity"], label[0], self.field.get())
                    
                    self.field.delete(0,"end")
                    self.field.insert(0, str(eval(f'data["selectedEntity"].{label[0]}')))
            else:
                self.selectedEntityId=id(data['selectedEntity'])
                self.field.delete(0,"end")
                self.field.insert(0, str(eval(f'data["selectedEntity"].{label[0]}')))
        else:
            self.field.config(text=str(eval(f'data["selectedEntity"].{label[0]}')))
