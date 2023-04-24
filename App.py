import tkinter as tk

from app.components.Window import Window
from app.components.TopMenu import TopMenu

from app.windowApps.simulation.Simulation import Simulation
from app.windowApps.Placeholder import Placeholder
from app.windowApps.AllEntitiesInfo import AllEntitiesInfo
from app.windowApps.EntityInfo import EntityInfo


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
            'AllEntitiesInfo': AllEntitiesInfo,
            'EntityInfo': EntityInfo,
        }

        # Render windows
        TopMenu(self)
        
        self.windows.append(Window(self, column=0, width=256,              tabs={'AllEntitiesInfo': self.windowApps['AllEntitiesInfo']}))
        self.windows.append(Window(self, column=1,                         tabs={'Simulation': self.windowApps['Simulation']}))
        self.windows.append(Window(self, column=2, width=256,              tabs={'EntityInfo': self.windowApps['EntityInfo']}))

        self.windows.append(Window(self, row=2, column=0, columnspan=3, height=256, tabs={'Placeholder': self.windowApps['Placeholder']}))

        self.mainloop()

