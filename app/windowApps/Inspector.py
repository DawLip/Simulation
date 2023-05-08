import tkinter as tk

from app.components.WindowApp import WindowApp

from ..components.Txt import Txt
from ..components.EditField import EditField

from model.entities.Entity import Entity

from data import data

class Inspector(WindowApp):
    def __init__(self, parent, **args):
        super().__init__(parent, padx=4, pady=4, **args)
        
        self.grid(row=2, sticky='nswe')
        self.columnconfigure(0, weight=1)
        

    def inicialize(self, **args):
        self.sections=[
            ['GeneralInfo', [['name', True], ['parent', False]]],
            ['Position', [['x', False], ['y', False]]],
            ['Resources', [['energy', False], ['buildingPoints', False]]]
        ]
        
        data['selectedEntity'] = Entity.all[-1]
        self.selectedEntity = Entity.all[-1]
        self.labelList=[]

        i=0
        for section in self.sections:
            self.labelList.append(Txt(self, row=i, column=0, text=section[0], bg=args['bg']))
            
            i+=1
            for property in section[1]:
                self.labelList.append(EditField(self, row=i, column=0, label=property, bg=args['bg']))
                i+=1
                
            self.labelList.append(Txt(self, row=i, column=0, text='', bg=args['bg']))
            i+=1
                
        self.render(True, **args)

        return super().inicialize(**args)
    
    def refresh(self, **args):
        self.render(**args)
        self.selectedEntity=data['selectedEntity']
        
        return super().refresh(**args)
    
    def render(self, isInicialize=False, **args):
        
        i=0
        dataToShow = []
        for k, value in self.selectedEntity.__dict__.items():
            keyIndex=0
            for i, letter in enumerate(k[::-1]):
                if letter=='_': 
                    keyIndex=i
                    break
            dataToShow.append((k[-keyIndex:],value))


        i=0
        for section in self.sections:
            i+=1
            for property in section[1]:
                self.labelList[i].conf(label=property)
                i+=1
            i+=1
        # i=0
        # for key, value in dataToShow:    
        #     if isInicialize:
        #         self.labelList.append(Txt(self, row=i, column=0, text=f"{key}: {value}", bg=args['bg']))
        #     else:
        #         # if i<len(self.labelList):
        #         #     self.labelList[i].config(text=f"{key}: {value}")
        #         pass
        #     i+=1
    
    
        