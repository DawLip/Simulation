import threading
import time
import random

from model.model import model
from app.App import App

from data import data


def appStart():
    app = App()


if __name__ == "__main__":
    random.seed(12345678)
    
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


# Simulation 0.2
# GUI:
#   - graphical update
# model:
#   - add "name" property for Entity
#   - add memory for Organism 
#   - finish handling collisions
