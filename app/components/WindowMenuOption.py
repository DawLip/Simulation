import tkinter as tk
import random

from model.initializeData import initializeData

from model.entities.Entity import Entity

from data import GUI, data

class WindowMenuOption(tk.Button):
    def __init__(self, parent, column=0, row=0, **args):
        self.parent=parent
        self.isMaximized=False
        self.imgs = {
            'Step': tk.PhotoImage(file = "./resources/GUI/simStep.png"),
            'Start': tk.PhotoImage(file = "./resources/GUI/simStart.png"),
            'Pause': tk.PhotoImage(file = "./resources/GUI/simPause.png"),
            'DecreaseSpeed': tk.PhotoImage(file = "./resources/GUI/simDecreaseSpeed.png"),
            'IncreaseSpeed': tk.PhotoImage(file = "./resources/GUI/simIncreaseSpeed.png"),
            'Restart': tk.PhotoImage(file = "./resources/GUI/simRestart.png"),
            'Maximize': tk.PhotoImage(file = "./resources/GUI/simMaximize.png"),
        }
        
        if args['text'] in self.imgs:   img=self.imgs[args['text']]
        else:                           img=None
        
        super().__init__(
            parent,
            padx=8,
            borderwidth=0,
            highlightthickness=0,
            bg=GUI['colors']['0 color'],
            fg=GUI['colors']['Font White'], 
            image=img,
            command=getattr(self, f'command{args["text"]}'),
            **args
        )
        
        self.grid(column=column, row=row, sticky='we')
        
    
    def commandStart(self):
        data['isSimRunning'] = not data['isSimRunning']
        
        if data['isSimRunning']:    self.config(image=self.imgs['Pause'])
        else:                       self.config(image=self.imgs['Start'])
        
    def commandDecreaseSpeed(self):
        if not data['modelIterationDelay']<=20:
            data['modelIterationDelay']-=10
        
    def commandMaximize(self):
        if self.isMaximized:
            GUI['windows'][0].grid(column=0, row=1, sticky='wens', columnspan=1)
            GUI['windows'][2].grid(column=2, row=1, sticky='wens', columnspan=1)
            GUI['windows'][3].grid(column=0, row=2, sticky='wens', columnspan=3)
        else:
            GUI['windows'][0].grid_forget()
            GUI['windows'][2].grid_forget()
            GUI['windows'][3].grid_forget()
        self.isMaximized = not self.isMaximized
    
    def commandStep(self):              data['isMakeStep']=True
    def commandIncreaseSpeed(self):     data['modelIterationDelay']+=10
    def commandRestart(self):           data['isSimRestart']=True  
    def commandTick(self):              pass
    