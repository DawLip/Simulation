import sys, os
import time

from .initializeData import initializeData
from .entity import Entity
from app.UIComponents.section import Section

from data import data, GUI

def model():
    time.sleep(0.5)

    initializeData()
    
    while not data['exit']:
        while data['isSimRunning']:
            # [x for x in Section.all if x.name=='map'][0].x+=1
            time.sleep(data['modelIterationDelay']/1000)