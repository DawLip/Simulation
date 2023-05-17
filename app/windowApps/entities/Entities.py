import tkinter as tk
import copy

from app.windowApps.window.WindowApp import WindowApp

from ...components.Txt import Txt
from .ExpandableList import ExpandableList
from ...components.List import List

from model.entities.Entity import Entity
from model.entities.Organism import Organism
from model.entities.AdditionalCell import AdditionalCell
from model.entities.tmp.TmpFood import TmpFood

from data import debug, data

class Entities(WindowApp):
    def __init__(self, parent, **args):
        super().__init__(parent, padx=4, pady=4, **args)
        
        self.grid(row=2, sticky='nesw')
        self.columnconfigure(0, weight=1)

    def inicialize(self, **args):
        self.labelList=[]
        
        self.render(True, **args)

        return super().inicialize(**args)

    def refresh(self, **args):
        self.render(**args)
        return super().refresh(**args)

    def render(self, isInicialize=False, **args):
        # Separate Entities childs
        entitiesChilds = {}
        for entity in Entity.all:
            entitiesChilds[entity.__class__.__name__]=True
            
        # Make data
        # data=[eval(f'{key}.all') for key, value in entitiesChilds.items()]
        data=[]
        for key, value in entitiesChilds.items():
            # data.append([key, [str(e.name) for e in eval(f'{key}.all')]])
            data.append({
                'type': 'ExpandableList',
                'text': f'{key}: {len(eval(f"{key}.all"))}',
                'data': [
                    {
                        'type': 'text',
                        'text': f'{index+1}\t{entity.name}',
                        'onClick': self.onClick
                    } for index, entity in enumerate(eval(f'{key}.all')) 
                ],
                'onClick': self.onClick
            })
            
        # List data        
        if isInicialize:
            if isInicialize:
                self.list=List(
                    self, 
                    row=0, column=0, 
                    data=data, 
                    bg=args['bg']
                )
        else:
            self.list.conf(data=data)
            # self.list.conf(data=data)
            # pass
            # render lists   
            # List(self, row=0, data=[eval(f'{key}.all') for key, value in data.items()], bg=args['bg'])
        # print([data[0] for data in data])
        
    def onClick(self, e, el, **args):
        # data['selectedEntity']=el
        pass
        
             
        # i=0
        # for key, value in  data.items():
        #     if isInicialize or len(data.items()) > len(self.labelList):
        #         self.labelList.append(ExpandableList(self, row=i, column=0, text=f"{key}: {value}", data=eval(f'{key}.all'), bg=args['bg']))
        #     else:
        #         self.labelList[i].conf(text=f"{key}: {value}", data=eval(f'{key}.all'))
        #     i+=1
        
        
            
    
        