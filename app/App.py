import tkinter as tk
from tkinter import Menu

from .components.Window import Window
from .components.TopMenu import TopMenu

from .windowApps.simulation.Simulation import Simulation
from .windowApps.Placeholder import Placeholder
from .windowApps.AllEntitiesInfo import AllEntitiesInfo
from .windowApps.EntityInfo import EntityInfo
from .windowApps.Debug import Debug

from data import data


class App(tk.Tk):
    rootWindow=None
    topMenu=None
    windows=[]
    keyPressed=None

    def __init__(self):
        super().__init__()

        self.width=1920
        self.height=1080-66

        self.geometry(f"{self.width}x{self.height}+-10+0")
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
            'AllEntitiesInfo': AllEntitiesInfo,
            'EntityInfo': EntityInfo,
            'Debug': Debug,
        }

        # Render windows
        TopMenu(self)
        
        self.windows.append(Window(self, column=0, width=256,              tabs={'AllEntitiesInfo': self.windowApps['AllEntitiesInfo'], 'Debug':self.windowApps['Debug']}))
        self.windows.append(Window(self, column=1,                         tabs={'Simulation': self.windowApps['Simulation']}))
        self.windows.append(Window(self, column=2, width=256,              tabs={'EntityInfo': self.windowApps['EntityInfo']}))

        self.windows.append(Window(self, row=2, column=0, columnspan=3, height=256, tabs={'Placeholder': self.windowApps['Placeholder']}))

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
