import threading
import time

from model.model import model
from app.App import App

from data import data


def appStart():
    app = App()


if __name__ == "__main__":
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


# Simulation 0.1.1
# GUI:
#   add
#       -basic menu template
#       -map resizing
#       -moving camera
#       -windowApp refreshing
#       -basic windowApp menu bars
#   changes
#       -move App.py file to "app" folder
#       -simulation render framerate depends now on simulation render time
#   bugfix
#       -whole app close correctly now
#       -app does not wait 1s before start
#       -optimalization GUI rendering
# model:
#   - start adding colisions
