import threading
from model.model import model
import time

from App import App
def appStart():
    app = App()

if __name__ =="__main__":
    modelT = threading.Thread(target=model)
    appT = threading.Thread(target=appStart)
    # debugT = threading.Thread(target=debug)
 
    modelT.start()
    time.sleep(1)
    appT.start()
    # debugT.start()
    # appT.join()
    
    
# Simulation 0.1
# GUI:
#  - rewrite GUI to "tkinter"
#  - add basic Simulation rendering
#  - add basic (not refreshing) windows menagment
# model:
#  - add constructors for: Entity, Organism, AdditionalCell, MapConstructor, OrganicMatter, CollisionMap
#  - add basic "AI" for Organism