import tkinter as tk

from components.Window import Window
from components.TopMenu import TopMenu

from windowApps.simulation.Simulation import Simulation
from windowApps.Placeholder import Placeholder


class App(tk.Tk):
    rootWindow=None
    topMenu=None
    windows=[]

    def __init__(self):
        super().__init__()

        self.width=1920
        self.height=1080-66

        self.geometry(f"{self.width}x{self.height}+-10+0")
        self.title("SimApp")

        # Grid configure
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)

        # Inicialize windows
        self.windowApps={
            'Simulation': Simulation,
            'Placeholder': Placeholder,
        }

        # Render windows
        TopMenu(self)
        
        self.windows.append(Window(self, column=0, width=256,              tabs={'AllEntitiesInfo': self.windowApps['Placeholder']}))
        self.windows.append(Window(self, column=1,                         tabs={'Simulation': self.windowApps['Simulation']}))
        self.windows.append(Window(self, column=2, width=256,              tabs={'EntityInfo': self.windowApps['Placeholder']}))

        self.windows.append(Window(self, row=2, column=0, columnspan=3, height=256, tabs={'Placeholder': self.windowApps['Placeholder']}))

