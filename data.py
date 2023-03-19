import cv2

imgR = cv2.imread('./map.png')
imgR = cv2.cvtColor(imgR, cv2.COLOR_RGB2BGR)

colors={
    'cell': [0,0,0],
    'food': [0,255,0],
    'dead': [128,128,0],
    'eaten': [255,0,0],
}

objs=[]

data={
    "x": 256,
    "y": 128,
    "speed": 10,
    "tick": 1,
    "id": 0
}

debugData={
    "cannibalism":0
}