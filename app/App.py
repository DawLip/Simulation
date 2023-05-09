import tkinter as tk
from tkinter import Menu

from .components.Window import Window
from .components.TopMenu import TopMenu

from .windowApps.simulation.Simulation import Simulation
from .windowApps.Placeholder import Placeholder
from .windowApps.Entities import Entities
from .windowApps.Inspector import Inspector
from .windowApps.Debug import Debug

from .windowApps.BottomBar import BottomBar

from data import data, GUI


class App(tk.Tk):
    rootWindow=None
    topMenu=None
    windows=[]
    keyPressed=None

    def __init__(self):
        super().__init__()

        self.width=self.winfo_screenwidth()
        self.height=self.winfo_screenheight()

        self.geometry(f"{self.width}x{self.height}+0+0")
        self.state("zoomed")
        self.title("SimApp")

        self.protocol("WM_DELETE_WINDOW", self.onExit)

        self.initMenu()

        # Grid configure
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)

        # Inicialize windows
        self.windowApps={
            'Simulation': Simulation,
            'Placeholder': Placeholder,
            'Entities': Entities,
            'Inspector': Inspector,
            'Debug': Debug,
        }

        # Render windows
        self.windows.append(Window(self, column=0, width=256,              tabs={'Entities': self.windowApps['Entities'], 'Debug':self.windowApps['Debug']}))
        self.windows.append(Window(self, column=1,                         tabs={'Simulation': self.windowApps['Simulation']}))
        self.windows.append(Window(self, column=2, width=256,              tabs={'Inspector': self.windowApps['Inspector']}))

        self.windows.append(Window(self, row=2, column=0, columnspan=3, height=256, tabs={'Placeholder': self.windowApps['Placeholder']}))
        
        self.windows.append(BottomBar(self, height=48))
        
        GUI['windows']=self.windows

        self.mainloop()

    def onExit(self):
        data['isSimRunning'] = False
        data['exit'] = True

        self.destroy()
    
    def initMenu(self):
        self.menuBar=Menu(self)
        self.config(menu=self.menuBar)

        file_menu = Menu(self.menuBar, tearoff=0)

        file_menu.add_command(label='New')
        file_menu.add_command(label='Open...')
        file_menu.add_command(label='Close')
        file_menu.add_separator()

        file_menu.add_command(label='Exit', command=self.destroy)
        self.menuBar.add_cascade(label="File", menu=file_menu)

        help_menu = Menu( self.menuBar, tearoff=0)

        help_menu.add_command(label='Welcome')
        help_menu.add_command(label='About...')

        self.menuBar.add_cascade(label="Help", menu=help_menu)
        

