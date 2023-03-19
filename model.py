import random
from data import objs, data, colors, imgR,  debugData
from constructors import cellConstructor

def model():
    for id, obj in enumerate(objs):
        if obj["type"]=="cell":
            if obj["wait"]>0:           obj["wait"]-=1
            elif obj["energy"]>200:     replicate(obj)
            elif obj["energy"]>0:       goToFood(obj)
            else:                       
                objs.pop(id)
                imgR[obj["y"]][obj["x"]]=colors["dead"]


def replicate(obj):
    cellConstructor(x=obj["x"],y=obj["y"])
    obj["energy"]-=100

def goToFood(obj, range=1):
    # Find neariest food
    neariestFood={"x":100000, "y":100000}
    neariestFoodDist=100000
    idOfNeariestFood=-1

    neariestCell={"x":100000, "y":100000}
    neariestCellDist=100000
    idOfNeariestCell=-1
    for id, food in enumerate(objs):
        if food["type"]=="food":
            if abs(obj["x"]-food["x"]) + abs(obj["y"]-food["y"]) < neariestFoodDist:
                neariestFood=food
                neariestFoodDist=abs(obj["x"]-food["x"])+abs(obj["y"]-food["y"])
                idOfNeariestFood=id
        if food["type"]=="cell":
            if abs(obj["x"]-food["x"]) + abs(obj["y"]-food["y"]) < neariestFoodDist:
                neariestCell=food
                neariestCellDist=abs(obj["x"]-food["x"])+abs(obj["y"]-food["y"])
                idOfNeariestCell=id

    # Eat food
    if neariestFoodDist==1:
        objs.pop(idOfNeariestFood)
        obj["energy"]+=neariestFood["energy"]
        obj["wait"]=10

    # Eat cell
    if neariestCellDist==1:
        imgR[neariestFood["y"]][neariestFood["x"]]=[255,0,0]
        objs.pop(idOfNeariestCell)
        obj["energy"]+=neariestCell["energy"]
        obj["wait"]=15
        debugData["cannibalism"]+=1

    # Retarget to cell
    if neariestCellDist<neariestFoodDist+50:
        neariestFood=neariestFood
        neariestFoodDist=neariestFoodDist
        idOfNeariestFood=idOfNeariestFood

    # Make a move towards neariest food
    if abs(obj["x"]-neariestFood["x"])>=abs(obj["y"]-neariestFood["y"]):
        if obj["x"]-neariestFood["x"]<=0:    obj["x"]+=range
        else:                                obj["x"]-=range
    else:
        if obj["y"]-neariestFood["y"]<=0:    obj["y"]+=range
        else:                                obj["y"]-=range
        
    # Check if space is occupied
    for id, c in enumerate(objs):
        if obj["x"]==c["x"] and obj["y"]==c["y"] and c["type"]=="cell" and c["id"]!=obj["id"]:
            obj["energy"]+=c["energy"]
            objs.pop(id)
            obj["wait"]=100
            break
    
    # Check if cross world border
    if obj["x"]==data["x"]:     obj["x"]=0
    elif obj["x"]==-1:          obj["x"]=data["x"]-1
    elif obj["y"]==data["y"]:   obj["y"]=0
    elif obj["y"]==-1:          obj["y"]=data["y"]-1

    # Pay movement cost
    obj["energy"]-=range
