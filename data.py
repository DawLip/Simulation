import cv2
from PyQt5.QtGui import QImage

imgR = cv2.imread('./resources/img/map.png')
imgR = cv2.cvtColor(imgR, cv2.COLOR_RGB2BGR)
img=imgR

def toQImg():
    height, width, channel = img.shape
    bytesPerLine = 3 * width
    qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)

    return qImg

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

GUIData={}