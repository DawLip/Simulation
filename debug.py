from data import colors, objs, data, debugData

def debug():
    cellCounter = 0
    deadCounter = 0
    foodCounter = 0

    for obj in objs:
        if obj["type"]=="cell":    cellCounter+=1
        if obj["type"]=="dead":    deadCounter+=1
        if obj["type"]=="food":    foodCounter+=1

    print(f'Objects: {len(objs)}\tCells: {cellCounter}\tDeads: {deadCounter}\tFood: {foodCounter}\tCannibalism: {debugData["cannibalism"]}')