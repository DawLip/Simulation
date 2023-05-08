import time
from random import randrange

from .initializeData import initializeData
from .entities.importEntities import Organism, Entity

from .entities.tmp.TmpFood import TmpFood

from data import data, debug

def model():
    initializeData()
    
    if not data['isModelReady']:
        data['isModelReady'] = True
        
    while not data['exit']:
        time.sleep(.01)
        while data['isSimRunning'] or data['isMakeStep']:
            if data['isMakeStep']:  data['isMakeStep']=False
            
            if not data['tick']%10:
                TmpFood(randrange(data["simWidth"] - 1), randrange(data["simHeight"] - 1))
            for organism in Organism.all:
                organism.brain()
                
            data['tick'] += 1

            debug['tickCounter']+=1
            # time.sleep(data['modelIterationDelay']/1000)
            if data['modelIterationDelay']>0:
                time.sleep(data['modelIterationDelay']/1000)
