import time

from .initializeData import initializeData

from data import data, GUI

def model():
    time.sleep(0.5)

    initializeData()
    
    while not data['exit']:
        while data['isSimRunning']:
            # [x for x in Entity.all][0].x+=1
            time.sleep(data['modelIterationDelay']/1000)