import tkinter as tk

from OpenGL import GL, GLU

from .SimulationWindow import SimulationWindow        

class Simulation(tk.Frame):
    def __init__(self, parent, **args):
        super().__init__(parent, **args)

        self.grid(sticky='wens')

        # self.rowconfigure(0, weight=1)
        # self.columnconfigure(0, weight=1)

        self.simulationWindow = SimulationWindow(self,width=1500, height=750)
        self.simulationWindow.grid(sticky='wens')
        self.simulationWindow.animate = 50

        # GLU.gluPerspective(90, (self.width/self.height), 0.1, 50.0)
        # GL.glTranslatef(0.0,0.0, -5)

        

        