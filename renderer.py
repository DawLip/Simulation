import os
clear = lambda: os.system('cls')

def search(entities, x, y):
    for i in range(len(entities)):
        if entities[i]["x"]==x and entities[i]["y"]==y: return entities[i]
    return -1

def renderer(entities, mapWidth, mapHeight):
    toRender = ""

    for i in range(mapHeight):
        for j in range(mapWidth):
            entity = search(entities, j, i)

            if j == 0 or j==mapWidth-1:     toRender += "|"
            elif i == 0 or i==mapHeight-1:  toRender += "_"
            elif entity != -1:              toRender += entity["Icon"]
            else:                           toRender += " "
        toRender += "\n"
    clear()
    print(toRender)
    print(str(entities).replace("}, {", "\n",))