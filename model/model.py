import time

from .initializeData import initializeData
from .entities.importEntities import Organism

from data import data

def model():
    time.sleep(0.1)

    initializeData()
    
    while not data['exit']:
        while data['isSimRunning']:
            # [x for x in Entity.all][0].x+=1
            for O in Organism.all:
                O.move()
            time.sleep(data['modelIterationDelay']/1000)