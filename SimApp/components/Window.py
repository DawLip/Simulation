import tkinter as tk

from .WindowTabs import WindowTabs
# from windows.Simulation import Simulation

class Window(tk.Frame):
    def __init__(self, parent, column=0, row=1, columnspan=1, tabs={}, **args):
        super().__init__(parent, padx=2, pady=2, bg='#2D2D31', **args)

        self.grid(column=column, row=row, sticky='wens', columnspan=columnspan)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.tabs=tabs
        self.selectedTab=0

        self.tabsBar=WindowTabs(self, tabs=tabs)
        if len(self.tabs.keys())>0: 
            self.content=self.tabs[list(self.tabs.keys())[self.selectedTab]](self, highlightbackground='black', bg='#3E3E42', highlightthickness=2, height=256, width=256)
            
