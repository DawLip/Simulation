import tkinter as tk
from PIL import Image

from data import GUI, data

class WindowMenuOption(tk.Button):
    def __init__(self, parent, column=0, row=0, **args):
        self.parent=parent
        self.imgs = {
            'Step': tk.PhotoImage(file = "./resources/GUI/simStep.png"),
            'Start': tk.PhotoImage(file = "./resources/GUI/simStart.png"),
            'Pause': tk.PhotoImage(file = "./resources/GUI/simPause.png"),
            'FullSpeed': tk.PhotoImage(file = "./resources/GUI/simFullSpeed.png"),
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
        
    def commandStep(self):
        data['isMakeStep']=True
    
    def commandStart(self):
        data['isSimRunning'] = not data['isSimRunning']
        
        if data['isSimRunning']:    self.config(image=self.imgs['Pause'])
        else:                       self.config(image=self.imgs['Start'])
        
    def commandFullSpeed(self):
        data['modelIterationDelay']=1
        
    def commandTick(self):
        pass