import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget,QLineEdit
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QTimer
import random
from model import model
import copy
from constructors import cellConstructor
from debug import debug

from data import colors, objs, data, imgR
img=copy.deepcopy(imgR)

# test
def renderMap():
    for obj in objs:
        img[obj["y"]][obj["x"]]=colors[obj["type"]]

    scaledImg = QPixmap(toQImg()).scaledToWidth(data["x"]*6)
    label.setPixmap(scaledImg)
    label2.setText(str(data["tick"]))

def toQImg():
    height, width, channel = img.shape
    bytesPerLine = 3 * width
    qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)

    return qImg
            
def respawnFood():
    if data["tick"]%10==0:
        objs.append({
            "type": "food",
            "x": random.randint(0, data["x"]-1),
            "y": random.randint(0, data["y"]-1),
            "energy": 50,
        })

def initializeData():
    for _ in range(1):
        cellConstructor(
            x=random.randint(0, data["x"]-1), 
            y=random.randint(0, data["y"]-1),
            wait=0
            )

def initializeGUI():
    global label
    global label2

    window.setWindowTitle("Sim")
    window.setGeometry(0,0,data["x"],data["y"])

    label = QLabel(window, alignment=Qt.AlignCenter)
    label.setPixmap(QPixmap(toQImg()))
    window.setCentralWidget(label)

    label2 = QLabel(window, text=str(data["tick"]), alignment=Qt.AlignCenter)
    label2.setText(str(data["tick"]))
    
    window.show()

def initialize():
    initializeData()
    initializeGUI()

def main():
    timer.singleShot(data["speed"], main)
    data["tick"]+=1

    global img
    img=copy.deepcopy(imgR)

    respawnFood()
    model()
    if data["tick"]%5==0:       renderMap()

    if data["tick"]%100==0:     debug()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()

    initialize()
    
    timer = QTimer()
    timer.singleShot(0, main)

    sys.exit(app.exec())