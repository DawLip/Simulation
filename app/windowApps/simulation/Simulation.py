import tkinter as tk 
import math
from PIL import ImageTk, Image, ImageDraw

from app.components.WindowApp import WindowApp

from model.entities.importEntities import Entity
from data import data, GUI, debug

from debug.debug import timerStart, timerStop

imgFood = Image.open("./resources/img/food.png")

class Simulation(WindowApp):
    def __init__(self, parent, **args):
        self.x=0
        self.y=0

        super().__init__(parent, **args)

        self.grid(row=2, sticky='wens')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

    def inicialize(self):
        self.scale=1

        self.dPressed=False
        self.aPressed=False
        self.wPressed=False
        self.sPressed=False

        img = Image.new( 'RGBA', (self.winfo_width(), self.winfo_height()), "gray")
        self.img = ImageTk.PhotoImage(img)

        self.imgContainer = tk.Label(self, image=self.img, borderwidth=0, highlightthickness=0)
        self.imgContainer.grid(column=0, row=0)

        self.imgContainer.bind('<MouseWheel>', self.onScroll)
        self.imgContainer.bind_all('<KeyPress>', self.onKeyPress)
        self.imgContainer.bind_all('<KeyRelease>', self.onKeyRelease)

        return super().inicialize()

    def refresh(self, **args):
        timerStart()

        const=20
        if self.dPressed:
            self.x+=const*self.scale
        if self.aPressed:
            self.x-=const*self.scale
        if self.wPressed:
            self.y-=const*self.scale
        if self.sPressed:
            self.y+=const*self.scale

        img = Image.new( 'RGBA', (data['simWidth']*GUI['texturesSize'], data['simHeight']*GUI['texturesSize']), "gray")

        for entity in Entity.all:
            img.paste( entity.img, (entity.x*GUI['texturesSize'], entity.y*GUI['texturesSize']), entity.img)      

        img.thumbnail((math.floor(self.winfo_width()*self.scale), math.floor(self.winfo_height()*self.scale)))
        
        img = img.crop((self.x, self.y, self.winfo_width()+self.x, self.winfo_height()+self.y))
        
        self.img = ImageTk.PhotoImage(img)
        self.imgContainer.config(image=self.img)

        # set framerate
        executionTime=timerStop()
        if executionTime<5: executionTime=5
        fr=int(1000/executionTime)
        data['frameRate']=fr

        return super().refresh(frameRate=fr)
    
    def onScroll(self, e):
        self.scale = self.scale - self.scale*.1*e.delta/120*-1

    def onKeyPress(self, e):
        if e.char=='d':
            self.dPressed=True
        elif e.char=='a':
            self.aPressed=True
        elif e.char=='w':
            self.wPressed=True
        elif e.char=='s':
            self.sPressed=True
            
    def onKeyRelease(self, e):
        if e.char=='d':
            self.dPressed=False
        elif e.char=='a':
            self.aPressed=False
        elif e.char=='w':
            self.wPressed=False
        elif e.char=='s':
            self.sPressed=False
    
    
    # def refresh(self):
    #     self.update()
    #     # img = Image.new( 'RGB', (self.winfo_width(), self.winfo_height()), "gray")
    #     img = Image.new( 'RGB', (600, 600), "gray")

    #     for entity in Entity.all:
    #         img.paste(imgFood, (entity.x*5, entity.y*5))

    #     self.img = ImageTk.PhotoImage(img)
    #     self.imgContainer.config(image=self.img)

    #     self.after(1/30, self.refresh())


        # imgPixelMap = img.load() # create the pixel map

        # for i in range(img.size[0]):    # for every col:
        #     for j in range(img.size[1]):    # For every row
        #         pixels[i,j] = (i, j, 100) # set the colour 

        # img = Image.open("./resources/img/food.png")

        # for y in range(img.size[0]):    
        #     for x in range(img.size[1]):    
        #         if x==10 and y==5:
        #             imgPixelMap[x,y] = (0, 0, 0) 



        

        

        