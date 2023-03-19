import random
import time

from renderer import renderer
from iterationFunction import iterationFunction
from data import baseSpaciesModel, baseFoodModel, d

# Create spacies
for i in range(d["numberOfInitSpacies"]):
    d["entities"].append(baseSpaciesModel.copy())
    if i==0: d["entities"][i]["id"] = 0
    else: d["entities"][i]["id"] = d["entities"][i-1]["id"]+1
    
    d["entities"][i]["Sex"] = bool(random.randint(0,1))
    d["entities"][i]["x"] = random.randint(1, d["mapWidth"]-1)
    d["entities"][i]["y"] = random.randint(1, d["mapHeight"]-1)
    #entities[i]["name"] = 

d["entities"][0]["IsPlayer"]=True
d["entities"][0]["Name"]="name"
d["entities"][0]["Icon"]="@"
d["entities"][0]["type"]="animal"

# Simulation loop
isRunningSimulation = True
while isRunningSimulation:
    iterationFunction()
    renderer(d["entities"], d["mapWidth"], d["mapHeight"])
    time.sleep(0.1)