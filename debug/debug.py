from time import process_time_ns

from data import debug

def timerStart():
    debug['executionTimerStart']=process_time_ns()

def timerStop():
    debug['timerResult']=process_time_ns()-debug['executionTimerStart']
    debug['executionTimerStart']=0

    return int(debug['timerResult']/1000000)
