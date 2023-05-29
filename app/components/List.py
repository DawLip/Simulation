import tkinter as tk
from functools import partial


from ..components.Txt import Txt

from data import GUI, data
from data import  data as d

class List(tk.Frame):
    def __init__(self, parent, column=0, row=0, sticky='w', onClick=None, text='', data=[], **args):
        super().__init__(parent, **args)

        self.grid(column=column, row=row, sticky='wens')
        
        
        self.listElements=[]
        self.data=data
        self.args = args
        
        self.onClick = onClick
        self.bg=args['bg']
        self.iconExpanded = tk.PhotoImage(file = f"./resources/GUI/downArrow.png")
        self.iconNotExpanded = tk.PhotoImage(file = f"./resources/GUI/arrowRight.png")
        
        self.onClick=onClick
        
        self.renderData(**args)
        
    def renderData(self, **args):    
        for index, el in enumerate(self.data):
            if      el['type'] == 'Text':               self.addElement(el, index, **args)
            elif    el['type'] == 'ExpandableList':     self.addList(el=el, index=index)
                    
    def addElement(self, el, index, **args):
        element=Txt(self, row=index, column=0, text=f"{el['text']}", bg=self.bg)
        # element=Txt(self, row=index, column=0, text=f"{el['text']}", bg=self.bg)
        element.bind("<Button-1>", partial(el['onClick'], el=el, **args))
        self.listElements.append(element)
        
    def addList(self, el, index):
        element=tk.Frame(self, bg=self.bg)
        element.grid(row=index, column=0, sticky='wens')
        element.columnconfigure(1, weight=1)
                
        # icon = tk.Label(element, image=self.iconNotExpanded, bg=self.bg)
        icon = tk.Label(element, image=self.iconNotExpanded, bg=self.bg)
        icon.grid(row=0, column=0, sticky='wens')
        
        label = Txt(element, row=0, column=1, text=el['text'], bg=self.bg, sticky='w')
        
        icon.bind("<Button-1>", partial(self.onExpandClick, parent=element, data=el['data'], index=index))
        label.bind("<Button-1>", partial(self.onExpandClick, parent=element, data=el['data'], index=index))
        
        self.listElements.append({
            'el': element, 
            'icon': icon, 
            'label': label, 
            'isExpand': False,
            'list': None
        })
                
    def conf(self, data, listElementsBase=None):
        if listElementsBase==None:
            listElementsBase=self.listElements
            
        # Update all    
        for index, el in enumerate(data):
            elType=el['type']
            txtNew = el['text']
            
            if elType=='ExpandableList':
                element=listElementsBase[index]
                label = element['label']
                txtOld = label['text']
                listOfElements = element['list']
                
                data=el['data']
                
                # Update present
                if txtOld != txtNew:
                    label.config(text=txtNew)
                
                if listOfElements != None: 
                    listOfElements.conf(data=data)
                          
            elif el['type']=='Text':
                if index >= len(listElementsBase):
                    self.addElement(el, index, **self.args)
                    
                element=listElementsBase[index]
                txtOld = element['text']
                
                if txtOld != txtNew:
                    element.config(text=txtNew)
        # for index, el in enumerate(self.listElements):
        #     if isinstance(el, dict):
        #         if index >= len(data):
        #             # Destroy   
        #             el['el'].destroy()
        #             self.listElements.pop(index)
        #         else:
        #             # Update present
        #             txt = data[index]['text']
        #             if el['label']['text'] != txt:
        #                 el['label'].config(text=txt)
                
            #     if el['list'] != None: el['list'].conf(data=data)
            # elif isinstance(el, str):
            #     print(el, '\n\n\n\n\n\n')
            
                # if el['list'] != None:
                #     el['list'].conf(data[index])
                
        
        # Create new
        # for index, el in enumerate(data):
        #     if index >= len(self.listElements):
        #         self.addList(el=el, index=index)
                
        # self.data=data
                
        # print(self.listElements)
        # oldData = self.data
        
        # for index, el in enumerate(data):
        #     # Is more than previous
        #     if len(data) > len(oldData):
        #         self.addList(el=el, index=index)
        #     # elif len(data) < len(oldData):
        #     #     self.listElements[index].destroy()
        #     #     self.listElements.pop(index)
    
        #     # Update
        #     if isinstance(el, str):
        #         self.listElements[index].config(text=f"{el}")
        
        # self.data=data         
                
    def onExpandClick(self, e, parent, data, index):
        if self.listElements[index]['isExpand']:
            self.listElements[index]['list'].destroy()
            
            self.listElements[index]['list']=None
            self.listElements[index]['isExpand']=False
            
            self.listElements[index]['icon'].config(image=self.iconNotExpanded)  
        else:
            self.listElements[index]['list'] = List(
                parent, row=1, column=1, 
                data=data, 
                bg=self.bg
            )
            
            self.listElements[index]['isExpand']=True
            self.listElements[index]['icon'].config(image=self.iconExpanded)
            
                
        
    # def conf(self, data):
    #     for index, el in enumerate(self.listElements):
    #         if index >= len(data):
    #             el.destroy()
    #             self.listElements.pop(index)
    #         elif index < len(data):
    #             el.config(text=f"{index+1}:\t{data[index].name}")
                
    #     if len(data) > len(self.listElements):
    #         for index, el in enumerate(data):
    #             if index > len(self.listElements)-1:
    #                 element=Txt(self, row=index, column=0, text=f"{index+1}:\t{el.name}", bg=self.bg)
    #                 element.bind("<Button-1>", partial(self.onClick, el=el))
                    
    #                 self.listElements.append(element)
    #     elif len(data) < len(self.listElements):
    #         i=0
    #         for index, el in enumerate(data):
    #             self.listElements[i].bind("<Button-1>", partial(self.onClick, el=el))
    #             i+=1
        
    # def onClick(self, e, el, **args):
    #     data['selectedEntity']=el

        
        
        
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