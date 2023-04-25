from time import process_time_ns

import math

debug={
    'executionTimerStart':0,
    'timerResult':0,
}

def timerStart():
    debug['executionTimerStart']=process_time_ns()

def timerStop():
    debug['timerResult']=process_time_ns()-debug['executionTimerStart']
    debug['executionTimerStart']=0
    
    return int(debug['timerResult']/1000000)


timerStart()

for i in range(1000000):
    x=i*i

print(timerStop())
