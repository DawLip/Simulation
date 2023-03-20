import sys,os,random
sys.path.insert(1,os.path.abspath('.'))

from data import data

def cellConstractor(energy=100,x=random.randint(0,data["x"]),y=random.randint(0,data["y"])):
    data["id"]+=1
    return {
        "id":data["id"],
        "type":'cell',
        "x":x,
        "y":y,
        "energy":energy
    }
