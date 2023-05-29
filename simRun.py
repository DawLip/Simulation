import threading
import time
import random

from model.model import model
from app.App import App

from data import data


def appStart():
    app = App()


if __name__ == "__main__":
    random.seed(data['seed'])
    data['isSimRunning']=True
    modelT = threading.Thread(target=model)
    # appT = threading.Thread(target=appStart)
    # debugT = threading.Thread(target=debug)

    modelT.start()
    while not data['isModelReady']:
        time.sleep(0.1)
    # appT.start()

    # debugT.start()

    # appT.join()
    modelT.join()


# Simulation 0.3
# GUI:
#   - add selected Entity indicator
#   - add simulation control buttons
#   - add BottomBar
#   - add seed menagment
#   - bug fix focus
#   - change window Entities listing
# model:
#  add AdditionalCell
#   - now Organisms can add AdditionalCells (cross only)
#   - tmp: Organisms prioritize adding AdditionalCells
#   - Collisions is working for AdditionalCells, but Organisms can stuck
