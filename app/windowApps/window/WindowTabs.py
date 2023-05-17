import tkinter as tk
from functools import partial

from .WindowTab import WindowTab

from data import GUI

class WindowTabs(tk.Frame):
    def __init__(self, parent, column=0, row=0, tabs=[], command=None, **args):
        super().__init__(parent, *args, bg=GUI['colors']['3 color'])

        self.grid(column=column, row=row, sticky='we')

        self.tabs=[]
        for index, tab in enumerate(tabs.keys()):
            self.tabs.append(WindowTab(self, name=tab, column=index, command=partial(command, index)))