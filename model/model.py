import time
from random import randrange

from .initializeData import initializeData
from .entities.importEntities import Organism

from .entities.tmp.Tmp_food import TmpFood

from data import data

def model():
    time.sleep(0.1)

    initializeData()
    
    while not data['exit']:
        while data['isSimRunning']:
            if not data['tick']%50:
                TmpFood(randrange(data["simWidth"] - 1), randrange(data["simHeight"] - 1))
            for O in Organism.all:
                O.brain()
                
            data['tick'] += 1
            time.sleep(data['modelIterationDelay']/1000)