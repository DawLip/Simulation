import sys, os
import time

from .initializeData import initializeData

from data import data, GUI

def model():
    initializeData()
    
    while not data['exit']:
        

        data['tick']+=1
        time.sleep(data['modelIterationDelay']/1000)