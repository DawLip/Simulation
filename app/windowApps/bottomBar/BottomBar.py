import tkinter as tk

from ...components.Txt import Txt
from ...components.Input import Input

from data import GUI, data, debug

class BottomBar(tk.Frame):
    def __init__(self, parent, **args):
        bg=GUI['colors']['0 color']
        super().__init__(parent, bg=bg, **args)
        
        self.grid(row=3, column=0, columnspan=3, sticky='nswe')

        self.leftMenu=tk.Frame(self)
        # self.rightMenu=tk.Frame(self, bg=args['bg'])
        
        self.leftMenu.grid(column=0, row=0, sticky='w')
        # self.rightMenu.grid(column=2, row=0, sticky='e')
        
       
        Txt(self.leftMenu, text='Tick:', column=0, bg=bg)
        self.tickCounter = Txt(self.leftMenu, text=debug['tickCounter'], column=1, bg=bg)
        
        Txt(self.leftMenu, text='\tModelIterationDelay:', column=2, bg=bg)
        self.modelIterationDelay = Txt(self.leftMenu, text=data['modelIterationDelay'], column=3, bg=bg)
        
        Txt(self.leftMenu, text='\tSeed:', column=4, bg=bg)
        self.seed = Input(self.leftMenu, text=data['seed'], column=5, bg=bg)
        
        self.refresh()
        
    def refresh(self):
        self.tickCounter.config(text=debug['tickCounter'])
        
        self.modelIterationDelay.config(text=data['modelIterationDelay'])
        
        data['seed']=self.seed.get()
        
        self.after(int(1000/data['GUIframeRate']), self.refresh)
        
    # def commandModelIterationDelay(self):
    #     pass
        
    # def commandSeed(self):
    #     pass
        
            
        # for index, name in enumerate(options['right']):
        #     self.options.append(WindowMenuOption(self.rightMenu, text=name, column=index))
    # def refresh(self):
    #     self.tickCounter.delete(0,"end")
    #     self.tickCounter.insert(0, str(debug['tickCounter']))
        
    #     self.after(int(1000/data['GUIframeRate']), self.refresh)
    