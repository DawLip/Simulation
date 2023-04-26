import threading
import time

from model.model import model
from app.App import App

from data import data

def appStart():
    app = App()

if __name__ =="__main__":
    modelT = threading.Thread(target=model)
    appT = threading.Thread(target=appStart)
    # debugT = threading.Thread(target=debug)
 
    modelT.start()
    while not data['isModelReady']:
        time.sleep(0.1)
    appT.start()
        
    # debugT.start()

    appT.join()
    modelT.join()
    
    
# Simulation 0.1
# GUI:
#  - rewrite GUI to "tkinter"
#  - add basic Simulation rendering
#  - add basic (not refreshing) windows menagment
# model:
#  - add constructors for: Entity, Organism, AdditionalCell, MapConstructor, OrganicMatter, CollisionMap
#  - add basic "AI" for Organism