import tkinter as tk 
import math
from PIL import ImageTk, Image

from model.entities.importEntities import Entity
from data import data, GUI

imgFood = Image.open("./resources/img/food.png")

class Simulation(tk.Frame):
    def __init__(self, parent, **args):
        super().__init__(parent, **args)

        self.grid(sticky='wens')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        img = Image.new( 'RGBA', (self.winfo_width(), self.winfo_height()), "gray")

        self.img = ImageTk.PhotoImage(img)
        self.imgContainer = tk.Label(self, image=self.img, borderwidth=0, highlightthickness=0)
        self.imgContainer.grid(column=0, row=0)

        self.refresh()


    def refresh(self):
        img = Image.new( 'RGBA', (data['simWidth']*GUI['texturesSize'], data['simHeight']*GUI['texturesSize']), "gray")

        for entity in Entity.all:
            img.paste(entity.img, (entity.x*GUI['texturesSize'], entity.y*GUI['texturesSize']))
            

        self.img = ImageTk.PhotoImage(img)
        self.imgContainer.config(image=self.img)
        
        self.after(math.floor(1000/data['frameRate']), self.refresh)
    
    
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



        

        

        