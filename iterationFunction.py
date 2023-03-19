from json.encoder import INFINITY
import random
import math

from data import baseSpaciesModel, baseFoodModel, d

def filterEntities(entities):
    animals=[]
    for i in range(len(entities)):
        if entities[i]["type"]=="animal": animals.append(entities[i])
    return animals

def spawnFood():
    if d["iteration"]==0:
        for i in range((d["numberOfInitSpacies"]*2 + random.randint(-5, 5))):
            d["entities"].append(baseFoodModel.copy())
            d["entities"][-1]["x"] = random.randint(1, d["mapWidth"]-1)
            d["entities"][-1]["y"] = random.randint(1, d["mapHeight"]-1)

def findNeariestFood(animal):
    neariestFood = {}
    distance = math.inf

    for entity in d["entities"]:
        if entity["type"]!="food": continue
        if entity["id"] == animal["id"]: continue

        distanceToCheck = abs(entity["x"]-animal["x"])+abs(entity["y"]-animal["y"])
        if distanceToCheck<distance:
            distance = distanceToCheck
            neariestFood = entity
    return neariestFood

def goToNeariestFood(animal, food):
    2+2

def move():
    animals = filterEntities(d["entities"])

    for animal in animals:
        food = findNeariestFood(animal)
        goToNeariestFood(animal, food)

def iterationFunction():
    spawnFood()
    move()
    d["iteration"] += 1